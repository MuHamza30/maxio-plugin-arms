"""Safe signup for Maxio Advanced Billing: at most one subscription per signup, also after a timeout.

Synchronous: it blocks the calling thread, for more than two minutes in the worst case (the create
alone waits up to 130 seconds for an answer). From async code call it with `asyncio.to_thread`
(recipes/README.md, "From async code"). Needs recipes/subscription_state.py beside it.

What one call does
1. Looks the subscription up by `reference`. Found: returns Existing. Nothing is created.
2. Sends the create once. The body is yours, with `reference` and `payment_collection_method` set
   inside "subscription" and `uniqueness_token` at the top level beside it. For this one request the
   SDK's automatic retry is off and the timeout is 130 seconds, so that Maxio's own 120 second cut-off
   answers first.
3. A 2xx it can read: returns Created.
4. A 4xx other than 408 and 409: Maxio rejected the request. The SDK's ApiError propagates unchanged.
   A 429 propagates too, but it is not a fault in the request: pause for minutes (knowledge/rules.md
   R10), then call again with the same token.
   A connection that could not be made (NEVER_SENT below): the request never left, and the httpx2
   error propagates. Nothing was created in either case.
5. A 409: a copy of this request arrived before. Reads back by reference. Found: Recovered. Not found:
   Unknown with first_copy_arrived True.
6. A timeout, a dropped connection, a 5xx, a 408, any other status, or a 2xx it cannot read
   (UNKNOWN_OUTCOME below): the outcome is unknown. Reads back by reference. Found: Recovered. Not
   found: Unknown with first_copy_arrived False.
7. The read-back itself fails, for any reason: Unknown, carrying the create's failure and the
   read-back's failure. Each read-back request waits at most READ_BACK_TIMEOUT_SECONDS, whatever the
   client's own timeout; the client's retry policy applies to it.
Any other exception from the create (a bug, a closed client) propagates. It never sends the create
twice. Calling it again with the same arguments is the resend.

The result is a value to branch on (`match`, `isinstance` or `.kind`), never a bare subscription
- Created(subscription): this call created the subscription.
- Existing(subscription, standing): it was there before this call sent anything.
- Recovered(subscription, standing, create_failure): found by the read-back after an unknown outcome.
- Unknown(first_copy_arrived, create_failure, read_back_failure): it may or may not exist. Do not
  report a failure and do not mint a new token. Wait until 120 seconds have passed since your first
  send (Maxio may still be working on it), then call again with the same reference and the same token.
  Created then means the first copy never arrived and this one was processed. Existing or Recovered
  means it did arrive. Only when that call returns Unknown with first_copy_arrived true (a 409) and
  nothing under the reference did the first attempt fail: only then start again with a new token.

Existing and Recovered carry `standing` (recipes/subscription_state.py), because a subscription found
by reference is not always a successful signup
- live: the user is subscribed. The signup is done.
- transient: Maxio is still creating or assessing it. It exists, so create nothing. Read it again soon.
- recoverable: it exists and is not billing (on hold, suspended, unpaid, awaiting signup). No access.
  Never sign up again beside it. Resume it, pay it or activate it.
- ended: canceled, expired, trial ended, or failed to create. This is not a successful signup. Reactivate
  it, or sign up again under a new reference with a new token: this reference keeps finding the ended one.
- unclassified: the SDK does not know its state. Read `subscription.state` yourself. Create nothing.

What you must supply
- `reference`: a subscription reference taken from your own data, the same on every call for this
  signup (the id of the signup record you claimed). Never random: it is how the subscription is found.
- `uniqueness_token`: mint a long random value (uuid4) once per logical signup, store it with your own
  record of that signup before the first call, and pass the same value on every call for that signup.
  Mint a new one only after Maxio rejected the request (step 4, not a 429) and you corrected it, or
  once the first attempt is known to have failed (see Unknown above). This file never mints one, and
  refuses a token equal to the reference, which could then never change. Maxio keeps a token for at
  least 60 minutes, per site and per API key, so the lookup in step 1 and your own record are the
  lasting guard.
- `payment_collection_method`: required, with no default. Left out, the site's own default applies.
- `subscription`: the rest of the create body. The product, exactly one customer source
  (`customer_reference`, `customer_id` or `customer_attributes`), and a payment source or none. If it
  already names a reference or a collection method, they must equal the arguments. It must not carry
  `uniqueness_token`: that belongs beside it, and this file puts it there.

What it does not do
- It does not serialize concurrent signups for one customer. Two calls at the same moment both miss
  the lookup and both create, and Maxio's token is not known to stop requests that are in flight
  together (one test run saw duplicates). Hold a per-customer claim in a store every instance of your
  application shares, around this call.
- It does not look the customer up by itself, and does not check how many customer sources the body
  names. Call `find_customer` (below) before every signup and name the customer by what it answers:
  `customer_attributes` for a customer who already exists creates a second customer
  (knowledge/decisions.md D1). When it finds one, call `find_held_subscription` (below) too: this
  call looks only at its own reference, and a customer who already holds the plan under another
  reference gets a second subscription beside it.
- It does not decide the collection method, and does not read a rejection for you. A 422 can be a
  3-D Secure `action_link` or an account block that no change to the request fixes.
- It cannot be cancelled and takes no deadline. If your caller stops waiting (a cancelled task, a
  future that timed out), the thread still sends the create and reads back, and the result is lost: call
  again with the same token to learn it. Never put a deadline under 120 seconds on it. A
  KeyboardInterrupt during the create propagates with no read-back: treat that as Unknown too.
- It does not hold a request slot. Wrap the call in recipes/request_limit.py; it then uses one slot.

Two things this SDK does that you will meet here
- A rejection whose body it cannot decode (a 422 that is not JSON or has no `errors` list) raises
  ValueError (pydantic.ValidationError is one) and the status is lost. This file cannot tell that from
  an unreadable 2xx, so it is step 6.
- A subscription with no product cannot be decoded at all. See recipes/list_all.py for what to do.

The lookup before the create runs under the client's own timeout and retry policy.

Rules: knowledge/rules.md R11, R12, R13, R14, R16, knowledge/lifecycles.md L2 (`find_customer` is step 4,
`find_held_subscription` the part of step 6 about the customer's other subscriptions)

Copy into your project and adapt. Not part of the SDK's API. Needs the SDK and the standard library.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Literal, TypeAlias

import httpx2  # the SDK's HTTP library: its exceptions reach you unwrapped
from maxio_advanced_billing import MaxioAdvancedBillingClient, models
from maxio_advanced_billing.core import ApiError, Failure, RequestOptionsDict, UnsetType, unwrap
from maxio_advanced_billing.models.enums import CollectionMethod, SortingDirection, SubscriptionSort

# Copied into a package? Make this line `from .subscription_state import Standing, standing`.
from subscription_state import Standing, standing

# Above Maxio's 120 second cut-off, so this client is not the first to give up on a create that still
# lands. The SDK's default is 30 seconds.
CREATE_TIMEOUT_SECONDS: Final = 130.0

# The read-back after a create was sent has a bound of its own, so it cannot wait for ever on a client
# built with a long timeout.
READ_BACK_TIMEOUT_SECONDS: Final = 30.0

# The request never left this process: no connection was made. Raised, as nothing was created.
NEVER_SENT: Final = (httpx2.ConnectError, httpx2.ConnectTimeout, httpx2.PoolTimeout, httpx2.UnsupportedProtocol)

# Sent, and no answer that can be read: the create may have landed. The HTTP library's errors once a
# connection was made; a socket or timeout error a custom transport raises itself; and ValueError, which
# is what the SDK raises for a body it cannot decode (pydantic.ValidationError is one).
UNKNOWN_OUTCOME: Final = (httpx2.RequestError, OSError, ValueError)

# The spec declares this field on no request, so no SDK model has it and no type checker checks its
# spelling. It is written once, here.
_TOKEN_FIELD: Final = "uniqueness_token"


@dataclass(frozen=True)
class Created:
    """This call created the subscription."""

    subscription: models.Subscription
    kind: Literal["created"] = field(default="created", init=False)


@dataclass(frozen=True)
class Existing:
    """The subscription was there before this call sent anything. Check `standing` before you treat it
    as a successful signup."""

    subscription: models.Subscription
    standing: Standing
    kind: Literal["existing"] = field(default="existing", init=False)


@dataclass(frozen=True)
class Recovered:
    """The create's outcome was unknown and the read-back found the subscription. Check `standing`.

    `create_failure` is what the create raised: an ApiError for a 409, a 408 or a 5xx, or the error of
    an answer that never came or could not be read.
    """

    subscription: models.Subscription
    standing: Standing
    create_failure: Exception
    kind: Literal["recovered"] = field(default="recovered", init=False)


@dataclass(frozen=True)
class Unknown:
    """The subscription may or may not exist. Wait, then call again with the same reference and token.

    `first_copy_arrived` is True after a 409: Maxio received a copy of this request, and its outcome is
    not known. `create_failure` is what the create raised. `read_back_failure` is what the read-back
    raised, or None when the read-back answered "not there".
    """

    first_copy_arrived: bool
    create_failure: Exception
    read_back_failure: Exception | None
    kind: Literal["unknown"] = field(default="unknown", init=False)


SignupResult: TypeAlias = Created | Existing | Recovered | Unknown


def safe_signup(
    client: MaxioAdvancedBillingClient,
    *,
    reference: str,
    uniqueness_token: str,
    payment_collection_method: CollectionMethod,
    subscription: models.CreateSubscription,
) -> SignupResult:
    """Create the subscription for one signup, or find the one that signup already has.

    Raises:
        ApiError: Maxio rejected the create with a 4xx other than 408 and 409, or the first lookup
            failed. In both cases no subscription was created by this call.
        httpx2.ConnectError, httpx2.ConnectTimeout, httpx2.PoolTimeout, httpx2.UnsupportedProtocol: The
            create never left this process (NEVER_SENT), or the first lookup failed this way.
        ValueError: The reference or the token is blank, the token equals the reference, `subscription`
            names another reference or collection method or carries `uniqueness_token`, or the first
            lookup could not be read. Nothing was sent to create anything.
        Exception: Whatever else the first lookup raised, and any exception from the create outside
            UNKNOWN_OUTCOME.
    """
    body = _create_body(reference, uniqueness_token, payment_collection_method, subscription)
    existing = find_subscription(client, reference)
    if existing is not None:
        return Existing(existing, standing(existing.state))
    try:
        # max_retries 0: one send, whatever retry policy the client was built with.
        options: RequestOptionsDict = {"timeout": CREATE_TIMEOUT_SECONDS, "max_retries": 0}
        created = _subscription_in(client.subscriptions.create_subscription(body=body, request_options=options))
    except ApiError as error:
        if 400 <= error.status_code < 500 and error.status_code not in (408, 409):
            raise  # a definite rejection: nothing was created
        return _read_back(client, reference, first_copy_arrived=error.status_code == 409, create_failure=error)
    except NEVER_SENT:
        raise  # no connection was made: nothing was created
    except UNKNOWN_OUTCOME as error:  # no answer, or an answer that cannot be read: it may have landed
        return _read_back(client, reference, first_copy_arrived=False, create_failure=error)
    return Created(created)


def find_subscription(
    client: MaxioAdvancedBillingClient, reference: str, *, timeout_seconds: float | None = None
) -> models.Subscription | None:
    """The subscription with your reference, or None. Only a 404 is "not there"; any other failure raises.

    `timeout_seconds` bounds each request; None leaves the client's own timeout in force.
    """
    options: RequestOptionsDict = {"timeout": timeout_seconds}
    result = client.subscriptions.with_raw_response.find_subscription(reference=reference, request_options=options)
    if isinstance(result, Failure) and result.status_code == 404:
        return None
    return _subscription_in(unwrap(result))


def find_customer(
    client: MaxioAdvancedBillingClient, reference: str, *, timeout_seconds: float | None = None
) -> models.Customer | None:
    """The customer with `reference`, your own user id, or None. Only a 404 is "not there"; any other
    failure raises, because "could not look it up" read as "does not exist" turns an outage into a
    second customer. It sends no write.

    Call it before every signup, one for a "new" customer too (knowledge/lifecycles.md L2 step 4): a
    resend after a lost answer meets the customer the first attempt created.
    - Found: pass it, with the signup's reference, to `find_held_subscription` before you sign it up
      again (L2 step 6), then name the customer with `customer_reference=reference`.
    - None: send `customer_attributes` with `reference` in it, so the new customer has it.

    `timeout_seconds` bounds each request; None leaves the client's own timeout in force.
    """
    if not reference.strip():
        raise ValueError("reference is empty: pass your own user id")
    options: RequestOptionsDict = {"timeout": timeout_seconds}
    result = client.customers.with_raw_response.read_customer_by_reference(reference, request_options=options)
    if isinstance(result, Failure) and result.status_code == 404:
        return None
    return unwrap(result).customer


HELD_MAX_PAGES: Final = 50  # the most pages of one customer's subscriptions find_held_subscription reads


def find_held_subscription(
    client: MaxioAdvancedBillingClient,
    customer: models.Customer,
    product_handle: str,
    signup_reference: str,
    *,
    timeout_seconds: float | None = None,
) -> models.Subscription | None:
    """A subscription that `customer` already holds on `product_handle` and that leaves no room for a
    second one beside it, or None (knowledge/lifecycles.md L2 step 6 and the fourth column of L3;
    knowledge/rules.md R16). Call it with what `find_customer` found, before you sign that customer up
    again: a customer the task calls "new" can be one who already holds the plan. Pass this signup's own
    `reference` too. A subscription carrying it is this signup's earlier attempt, not a second plan: it is
    skipped here, and `safe_signup` finds it by that reference and returns `Existing`.
    - Found: do not create. Its `standing` (subscription_state.py) says what to tell the user: "live",
      the customer already has the plan; "transient", Maxio is still working on it, so read it again;
      "recoverable", resume it or collect on it; "unclassified", decide by hand.
    - None: nothing on this plan blocks a signup. An "ended" one (canceled, expired, trial ended,
      failed to create) does not: sign up again, or bring a canceled or trial-ended one back with a
      reactivation if that is what the user wants (knowledge/decisions.md D12).

    It pages `list_subscriptions` filtered by `customer_id`, 200 a page in id order, until a page comes
    back empty (knowledge/rules.md R8); `list_customer_subscriptions` declares no paging. It matches the
    product by `product.handle`, so a subscription with no product is not matched (on a new-Catalog
    site, build the client over `PlanlessSubscriptionTransport` from list_all.py, or such a page cannot
    be decoded). Any failure raises, never read as "nothing held", and so does a row with no
    subscription in it. It sends no write.

    `timeout_seconds` bounds each request; None leaves the client's own timeout in force.
    """
    customer_id = customer.id
    if isinstance(customer_id, UnsetType) or customer_id <= 0:
        raise ValueError("the customer has no id: pass what find_customer returned")
    if not product_handle.strip():
        raise ValueError("product_handle is empty: pass the plan's handle")
    if not signup_reference.strip():
        raise ValueError("signup_reference is empty: pass this signup's reference")
    options: RequestOptionsDict = {"timeout": timeout_seconds}
    for page in range(1, HELD_MAX_PAGES + 1):
        rows = client.subscriptions.list_subscriptions(
            page=page,
            per_page=200,
            sort=SubscriptionSort.ID,
            direction=SortingDirection.ASC,
            customer_id=customer_id,
            request_options=options,
        )
        if len(rows) == 0:  # the only end signal
            return None
        for row in rows:
            subscription = _subscription_in(row)
            product = subscription.product
            if isinstance(product, UnsetType) or product.handle != product_handle:
                continue
            if subscription.reference == signup_reference:  # this signup itself: safe_signup's to report
                continue
            if standing(subscription.state) != "ended":
                return subscription
    raise RuntimeError(f"customer {customer_id} has more than {HELD_MAX_PAGES} pages of subscriptions: check by hand")


def _read_back(
    client: MaxioAdvancedBillingClient, reference: str, *, first_copy_arrived: bool, create_failure: Exception
) -> Recovered | Unknown:
    try:
        found = find_subscription(client, reference, timeout_seconds=READ_BACK_TIMEOUT_SECONDS)
    except Exception as read_back_failure:  # a failed read-back must not replace the unknown outcome
        return Unknown(first_copy_arrived, create_failure, read_back_failure)
    if found is None:
        return Unknown(first_copy_arrived, create_failure, None)
    return Recovered(found, standing(found.state), create_failure)


def _subscription_in(response: models.SubscriptionResponse) -> models.Subscription:
    if isinstance(response.subscription, UnsetType):
        # The SDK types the wrapper optional. A 2xx without it is unreadable, which is not "not there".
        raise ValueError("Maxio answered 2xx without a subscription")
    return response.subscription


def _create_body(
    reference: str,
    uniqueness_token: str,
    payment_collection_method: CollectionMethod,
    subscription: models.CreateSubscription,
) -> models.CreateSubscriptionRequest:
    if not reference.strip():
        raise ValueError("reference is empty: pass the subscription reference from your own data")
    if not uniqueness_token.strip():
        raise ValueError("uniqueness_token is empty: mint one per logical signup and store it")
    if uniqueness_token == reference:
        raise ValueError("uniqueness_token equals reference: a corrected request needs a new token, same reference")
    if _TOKEN_FIELD in (subscription.model_extra or {}):
        raise ValueError("subscription carries uniqueness_token: pass it as uniqueness_token, which sends it beside")
    _refuse_conflict("reference", subscription.reference, reference)
    _refuse_conflict("payment_collection_method", subscription.payment_collection_method, payment_collection_method)
    inner = subscription.model_copy(
        update={"reference": reference, "payment_collection_method": payment_collection_method}
    )
    # SDK models keep and send keys they do not declare (docs/models.md, "Fields the spec does not
    # declare"), so validating a mapping puts the token at the top level of the body. Maxio wants it
    # there, not nested inside "subscription", and it does not read the Idempotency-Key header the SDK sends.
    return models.CreateSubscriptionRequest.model_validate({"subscription": inner, _TOKEN_FIELD: uniqueness_token})


def _refuse_conflict(name: str, in_body: object, passed: object) -> None:
    if not isinstance(in_body, UnsetType) and in_body != passed:
        raise ValueError(f"subscription.{name} is {in_body!r} and {name}={passed!r} was passed: give it once")
