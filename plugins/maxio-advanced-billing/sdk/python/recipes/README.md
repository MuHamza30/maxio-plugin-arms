# Recipes

Five source files to copy into your project, for what Maxio requires and this SDK does not do for you.
Each needs only the SDK and the Python standard library. They are not part of the SDK's API and are not
installed with the package: copy the file, adapt it, own it. Each file's opening docstring says exactly
what it does and what it leaves to you; this page is the overview.

All five are **synchronous**. See [From async code](#from-async-code) before you use them in an asyncio
application.

| Recipe | What it does | Rules | What it leaves to you |
|---|---|---|---|
| `recipes/safe_signup.py` | Creates one subscription per signup. Looks it up by your reference first; sends the create once with your `uniqueness_token` at the top level of the body, no automatic retry and a 130 second timeout; after a 409, a 5xx, a 408, a timeout or an unreadable answer it reads back by reference, on a timer of its own, instead of resending. Returns `Created`, `Existing`, `Recovered` or `Unknown`, never a bare subscription; `Existing` and `Recovered` carry the subscription's standing. Raises only on a definite rejection (a 4xx other than 408 and 409), when no connection was made, or for an error outside the unknown set. `find_customer` looks the customer up by your user id: call it before every signup (L2 step 4). `find_held_subscription` finds a subscription that customer already holds on the plan in a state that allows no second one beside it (L2 step 6), skipping one under this signup's own reference, which `safe_signup` reports as `Existing`. | `knowledge/rules.md` R11, R12, R13, R14, R16 · `knowledge/lifecycles.md` L2 | Minting the token once per signup and storing it; a deterministic reference; a per-customer claim in a store all your instances share (it does not serialize concurrent signups); calling `find_customer` first, then `find_held_subscription` when it found one, and naming the customer by the answer (D1); the payment source (D2); the collection method (D3); reading a rejection (R13); calling again after `Unknown` |
| `recipes/list_all.py` | Pages a list that takes `page` and `per_page` and returns an array: 200 a page, stops only on an empty page, raises at a page ceiling, drops rows seen before when given a key. `list_all_subscriptions` sorts by id, ascending. Also ships `PlanlessSubscriptionTransport`, an optional workaround for an SDK limitation (below). | `knowledge/rules.md` R8 | The ceiling and what to do when it is hit; unwrapping a list that returns an object; never looping a list that takes no `page`; the filters that fail open (R9) |
| `recipes/subscription_state.py` | Puts every state of the SDK's `SubscriptionState` into `live`, `transient`, `recoverable` or `ended`; `has_access` and `access_decision`. Fails at type-check time and at import when the SDK gains a state it does not classify. | `knowledge/rules.md` R16 · `knowledge/lifecycles.md` L3 | Storing your last access decision; listing without a `state` filter to find everyone with access; re-reading a subscription before acting on a webhook (R20) |
| `recipes/verify_webhook.py` | Checks the hex HMAC-SHA256 signature over the raw body in constant time; `False`, never an exception, for a missing or malformed signature. Finds the header in a mapping, a WSGI environ or ASGI pairs, any case, `str` or `bytes`. | `knowledge/rules.md` R19 | Keeping the body bytes as received; answering 200 fast; skipping a webhook `id` already processed; re-reading the resource (R20); the shared key |
| `recipes/request_limit.py` | At most four requests in flight per site in this process, first come first served, with a bounded wait; nested use in one thread holds one slot. `maxio_retry_options()` gives the client retry policy below. | `knowledge/rules.md` R10, R11 | Pausing for minutes after a 429; sharing the limit with other processes and hosts; taking the slot in the thread that makes the call |

## The client these recipes expect

The SDK retries by default: three more sends after about 1, 2 and 4 seconds, for a GET, HEAD, PUT or
OPTIONS that answers 408, 429, 500, 502, 503 or 504 or gets no answer. Two parts of that are wrong for
Maxio. A 429 asks for a pause of minutes, not seconds (R10). And `retry_subscription`,
`reactivate_subscription`, `activate_subscription`, and `update_subscription` with payment details, are
`PUT`s that can take a payment, while `verify_bank_account` is a `PUT` capped at ten attempts (R11). Build
the client without both:

<!-- example: client -->
```python
def maxio_client(api_key: str, site: str) -> MaxioAdvancedBillingClient:
    return MaxioAdvancedBillingClient(
        basic_auth={"username": api_key, "password": "x"},
        server_config={"production": {"us": {"site": site}}},
        # The SDK's default policy, without 429 among the statuses and without PUT among the methods.
        retry_options=maxio_retry_options(),
    )
```

`maxio_retry_options` is in `request_limit.py`. Written out, the two options it sets are
`"status_codes_to_retry": frozenset({408, 500, 502, 503, 504})` and
`"http_methods_to_retry": frozenset({"GET", "HEAD", "OPTIONS"})` in the client's `retry_options`.

On a client you do not control, turn retry off for one call, and give a payment write more than Maxio's
120 second cut-off:

<!-- example: one-call -->
```python
def retry_payment(client: MaxioAdvancedBillingClient, subscription_id: int) -> models.SubscriptionResponse:
    # One send whatever the client's policy, and a timeout above Maxio's 120 second cut-off.
    return client.subscription_status.retry_subscription(
        subscription_id, request_options={"max_retries": 0, "timeout": 130.0}
    )
```

Proven by counting sends at a fake transport: by default one GET that answers 429 is sent four times
within about seven seconds and each of the five `PUT`s is sent four times on a 429, a 503, a 504 or a
timeout; with the client above, and with the two options written out, each is sent once, while a GET
that answers 503 is still sent four times; `max_retries: 0` sends each `PUT` once on a default client. A
POST is never resent by default.

## Sending `uniqueness_token`

The spec declares `uniqueness_token` on no request, so no SDK model has it and the SDK map does not show
it. Models keep and send keys they do not declare, so build the body by validating a mapping:

<!-- example: token -->
```python
def create_body(subscription: models.CreateSubscription, token: str) -> models.CreateSubscriptionRequest:
    return models.CreateSubscriptionRequest.model_validate({"subscription": subscription, "uniqueness_token": token})
```

The two spellings a type checker sees, `CreateSubscriptionRequest(subscription=..., uniqueness_token=...)`
and a dict passed as `body=`, are rejected by mypy and pyright in strict mode, although both reach the
wire at run time. A misspelt key is accepted and sent as spelt, with no error anywhere: only a test that
reads the request the SDK built proves the token is there. `safe_signup.py` writes the field name once,
and its tests check the body on the wire. The smallest such test:

<!-- example: wire-test -->
```python
class Created201:
    """A canned 201. The SDK reads a response through these six members."""

    url = "https://acme.chargify.com/subscriptions.json"
    status_code = 201
    headers: Mapping[str, str] = {"content-type": "application/json"}

    def read(self) -> bytes:
        return b'{"subscription": {"id": 1, "state": "active"}}'

    def iter_bytes(self, chunk_size: int | None) -> Iterator[bytes]:
        yield self.read()

    def close(self) -> None: ...


class CapturingTransport:
    """Stands in for the network: keeps every request the SDK built and answers 201."""

    def __init__(self) -> None:
        self.requests: list[HttpRequest] = []

    def send(self, request: HttpRequest) -> HttpResponse:
        self.requests.append(request)
        return Created201()

    def close(self) -> None: ...


def test_the_token_is_at_the_top_level_of_the_body() -> None:
    transport = CapturingTransport()
    client = MaxioAdvancedBillingClient(custom_http_client=transport, basic_auth={"username": "key", "password": "x"})
    body = models.CreateSubscriptionRequest.model_validate(
        {"subscription": models.CreateSubscription(product_handle="pro-monthly"), "uniqueness_token": "token-1"}
    )

    client.subscriptions.create_subscription(body=body)

    sent = transport.requests[0].body
    assert isinstance(sent, JsonBody)
    payload = cast("dict[str, Any]", json.loads(sent.content))
    assert payload["uniqueness_token"] == "token-1"  # a misspelt key fails here, and nowhere else
    assert "uniqueness_token" not in payload["subscription"]
```

## Using `safe_signup`

<!-- example: signup -->
```python
def sign_up(
    client: MaxioAdvancedBillingClient, signup_id: str, token: str, user_id: str, email: str, card_token: str
) -> str:
    card = models.PaymentProfileAttributes(chargify_token=card_token)
    customer = find_customer(client, user_id)  # the customer Maxio holds under your user id
    if customer is not None:
        if find_held_subscription(client, customer, "pro-monthly", signup_id) is not None:  # one held beside
            return "not subscribed: the customer already holds this plan"
        subscription = models.CreateSubscription(
            product_handle="pro-monthly", customer_reference=user_id, credit_card_attributes=card
        )
    else:  # none yet: this create makes it, with your user id as its reference
        subscription = models.CreateSubscription(
            product_handle="pro-monthly",
            customer_attributes=models.CustomerAttributes(reference=user_id, email=email),
            credit_card_attributes=card,
        )
    result = safe_signup(
        client,
        reference=signup_id,  # from your own signup record, the same on every call
        uniqueness_token=token,  # minted once, stored with that record, the same on every call
        payment_collection_method=CollectionMethod.AUTOMATIC,
        subscription=subscription,
    )
    match result:
        case Created():
            return "subscribed"
        case Existing(standing="live") | Recovered(standing="live"):
            return "subscribed"
        case Existing(standing=standing) | Recovered(standing=standing):
            return f"not subscribed: the subscription under this reference is {standing}"
        case Unknown():
            return "not known yet: call again later with the same reference and token"
```

`Unknown` is never a failure. Its `create_failure` and `read_back_failure` say what went wrong, as does
`Recovered.create_failure`. Wait until 120 seconds have passed since the first send, then call again with
the same reference and the same token. A 201 then means the first copy never arrived; finding the
subscription, or a 409, means it did. Only when that call answers 409 and still finds nothing under the
reference did the first attempt fail, and only then is a new token right (`knowledge/rules.md` R11). The result's `kind` (`"created"`, `"existing"`, `"recovered"`, `"unknown"`) narrows the type as
`match` does.

## Subscriptions with no product: an SDK limitation

On a site with Maxio's new Catalog experience a subscription can have no product, and Maxio then sends
`product`, `product_price_point_id` and `product_price_point_type` as `null`. This SDK's `Subscription`
model has no `null` for those three fields, so it raises `pydantic.ValidationError` for the whole
response. On a list page the good rows fail with the bad one, so `list_all_subscriptions` raises; in
`safe_signup` the first lookup raises, and a create that succeeded comes back as `Unknown`.

If your site has such subscriptions, build the client over `PlanlessSubscriptionTransport` from
`list_all.py`. It deletes those three keys when they are `null`, inside every object under a
`"subscription"` key of a 2xx JSON answer, before the SDK decodes it; the fields then read as `UNSET`.
It is a workaround for an SDK limitation, in recipe code, and no part of the SDK. It does not cover
`list_exported_subscriptions`, whose rows have no `"subscription"` wrapper. Remove it when the SDK
accepts the nulls.

<!-- example: planless -->
```python
def planless_client(api_key: str, site: str) -> MaxioAdvancedBillingClient:
    return MaxioAdvancedBillingClient(
        # With a transport of your own the client's timeout= is not used: give it to Httpx2Client.
        custom_http_client=PlanlessSubscriptionTransport(Httpx2Client(timeout=30.0)),
        basic_auth={"username": api_key, "password": "x"},
        server_config={"production": {"us": {"site": site}}},
    )
```

## From async code

The recipes are synchronous: a call blocks its thread until Maxio answers, for more than two minutes in
the worst case of `safe_signup`. Called on an asyncio event loop that stops every other task for that
long. Run the call in a worker thread with `asyncio.to_thread`, and take the request slot inside that
thread:

<!-- example: async -->
```python
async def sign_up_from_async_code(
    client: MaxioAdvancedBillingClient, site: str, signup_id: str, token: str, body: models.CreateSubscription
) -> SignupResult:
    def blocking() -> SignupResult:
        with maxio_slot(site):  # taken in the worker thread, never on the event loop
            return safe_signup(
                client,
                reference=signup_id,
                uniqueness_token=token,
                payment_collection_method=CollectionMethod.REMITTANCE,
                subscription=body,
            )

    return await asyncio.to_thread(blocking)
```

What the request limit means there:

- `maxio_slot` counts threads. Taken in the worker thread as above, a burst of tasks still has at most
  four requests in flight. Entered on the event loop itself it raises `RuntimeError`, because there it
  would block every task.
- A call waiting for a slot holds a worker thread. `asyncio.to_thread` uses the loop's default executor,
  which every `to_thread` call in your application shares, so a burst of Maxio calls can take all its
  threads. Give the loop an executor of a size you chose, or a separate one for Maxio calls.
- Cancelling the awaiting task, or `asyncio.wait_for` running out, does not stop the thread: the
  signup goes on, and its result is lost. Call again with the same reference and token to learn it.
- `verify_webhook.py` and `subscription_state.py` do no I/O and can be called on the loop directly.

The SDK also has an `AsyncMaxioAdvancedBillingClient`. No async port of these recipes is shipped: it
would be a second copy of the signup flow and the limiter to keep in step, and it would need the whole
test suite again against an async transport. A worker thread per call costs little for signups and
webhooks; if you port them anyway, port the tests with them.

## Copying them in

- **Python 3.10 or later**, the SDK's own floor. Each file is a plain module; `from __future__ import
  annotations` is the only import trick.
- `safe_signup.py` imports `subscription_state.py`; copy both. Inside a package, change its line
  `from subscription_state import Standing, standing` to `from .subscription_state import Standing,
  standing` as the comment above it says.
- **Checked under** mypy 2.4.0 `--strict` with `warn_unreachable`, `warn_return_any` and the error codes
  `redundant-expr`, `truthy-bool`, `ignore-without-code` and `possibly-undefined` (the SDK's own mypy
  settings), and pyright 1.1.414 in `strict` mode, each for Python 3.10 and 3.14, with no error and no
  `type: ignore`. The tests pass on CPython 3.10 and 3.12.
- **Stricter than that:** mypy's `--disallow-any-expr` reports three lines in `safe_signup.py` and one
  in `request_limit.py`, because pydantic's `model_extra`, `model_copy` and `model_validate` are typed
  with `Any`. Pyright's optional rules that `strict` leaves off report style only: an `__init__` that
  does not call `object.__init__`, an unused return value, and implicit string concatenation.
- Importing the SDK emits a `UserWarning` (its `Contract` model has a field named `register`). A project
  that runs with warnings as errors needs
  `ignore:Field name "register" in "Contract" shadows an attribute in parent "SdkBaseModel":UserWarning`.

## Tests

The tests run offline against a fake transport at the SDK's `custom_http_client` seam, and import these
files where they are. They live outside the SDK folder, in `recipe-tests/python/` at the root of this
repository; its README has the one command that runs them, the type checks and the mutation check.
Every code block on this page is copied from a file those tests type-check and run, and a test fails
when this page and that file differ.
