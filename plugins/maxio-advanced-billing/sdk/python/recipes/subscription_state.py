"""Subscription states for Maxio Advanced Billing: who has access, and what a state means for a signup.

Synchronous and pure: no I/O, no lock, no clock. Call it from sync or async code alike.

What it does
- `standing(state)` puts each state of the SDK's `SubscriptionState` enum into one of four groups:
      live         active, trialing, past_due, soft_failure. Access is on.
      transient    pending, assessing. Maxio is in the middle of a change. Keep the access decision you
                   made before; do not make a new one from this state.
      recoverable  on_hold, suspended, unpaid, awaiting_signup, paused. Not billing, but not over:
                   on_hold resumes, a prepayment restores suspended. No access. Never create a second
                   subscription beside one of these.
      ended        canceled, expired, trial_ended, failed_to_create. No access. A new signup or a
                   reactivation is possible.
  It returns "unclassified" for a state the enum does not have (Maxio added it after this SDK was
  generated) and for a subscription that came back with no state. Treat that like transient: change
  nothing, look at the subscription, update the SDK.
- `has_access(state)` is True for the four live states and False for everything else, the transient and
  unclassified ones included. Use it for a first decision, when you have stored none.
- `access_decision(state, previous=...)` is the decision to store: True for live, False for recoverable
  and ended, and `previous` unchanged for transient and unclassified.
- A guard fails when the SDK gains a state this file does not classify. mypy and pyright report the
  `match` below as incomplete, and importing this file raises ImportError naming the state.

What it does not do
- It does not read a subscription and does not store your decision. You pass `subscription.state` in
  (it may be UNSET, which is accepted) and you keep `previous`.
- It does not act on webhooks. Re-read the subscription before you change access because of an event
  (knowledge/rules.md R20).

Words
- Maxio's schema calls six states "End of Life" (not billing): the four ended ones plus on_hold and
  suspended. Here those two are recoverable, because they come back and a new signup beside them is wrong.
- A paused subscription is on_hold. `paused` means the merchant's own Maxio account is in arrears, and
  no API call produces it.

Listing everyone with access
- The `state` filter of `list_subscriptions` takes other values than this enum (`SubscriptionStateFilter`),
  and the SDK types it as one value per call. It has no value for soft_failure, pending, assessing,
  failed_to_create or paused. So list with no state filter (recipes/list_all.py) and keep the rows
  whose standing is "live". For a transient row use the decision you stored for it; with none, count
  assessing in (a renewal in progress; its entitlements stay on) and pending out (lifecycles.md L3).

Rules: knowledge/rules.md R16, knowledge/lifecycles.md L3

Copy into your project and adapt. Not part of the SDK's API. Needs the SDK and the standard library.
"""

from __future__ import annotations

from typing import Final, Literal, NoReturn, TypeAlias

from maxio_advanced_billing.core import UnsetType
from maxio_advanced_billing.models.enums import SubscriptionState, SubscriptionStateOrStr

Standing: TypeAlias = Literal["live", "transient", "recoverable", "ended", "unclassified"]


def _not_classified(state: NoReturn) -> NoReturn:
    """The guard. A type checker accepts the call below only while `_classify` names every member."""
    raise ImportError(
        f"subscription_state.py does not classify the SDK's subscription state {state!r}. "
        "Decide its standing in _classify before you use this file."
    )


def _classify(state: SubscriptionState) -> Standing:
    match state:
        case (
            SubscriptionState.ACTIVE
            | SubscriptionState.TRIALING
            | SubscriptionState.PAST_DUE  # in dunning: access stays on
            | SubscriptionState.SOFT_FAILURE  # a merchant-side failure, retried by Maxio
        ):
            return "live"
        case SubscriptionState.PENDING | SubscriptionState.ASSESSING:
            return "transient"
        case (
            SubscriptionState.ON_HOLD  # paused by the merchant; resumes
            | SubscriptionState.SUSPENDED  # prepaid balance used up; a prepayment restores it
            | SubscriptionState.UNPAID  # dunning ended with "mark unpaid"
            | SubscriptionState.AWAITING_SIGNUP  # created to start later
            | SubscriptionState.PAUSED  # the merchant's Maxio account is in arrears; no API call produces it
        ):
            return "recoverable"
        case (
            SubscriptionState.CANCELED
            | SubscriptionState.EXPIRED
            | SubscriptionState.TRIAL_ENDED
            | SubscriptionState.FAILED_TO_CREATE
        ):
            return "ended"
        case _:
            _not_classified(state)


# Built at import, so a state the SDK has and `_classify` lacks stops the import instead of reaching a caller.
_STANDING: Final[dict[SubscriptionState, Standing]] = {state: _classify(state) for state in SubscriptionState}


def _states(wanted: Standing) -> frozenset[SubscriptionState]:
    return frozenset(state for state, group in _STANDING.items() if group == wanted)


LIVE_STATES: Final = _states("live")
TRANSIENT_STATES: Final = _states("transient")
RECOVERABLE_STATES: Final = _states("recoverable")
ENDED_STATES: Final = _states("ended")


def standing(state: SubscriptionStateOrStr | UnsetType) -> Standing:
    """The group `state` belongs to. Takes the enum member, the wire string, or the UNSET of a missing field."""
    if isinstance(state, UnsetType):
        return "unclassified"
    try:
        return _STANDING[SubscriptionState(state)]
    except ValueError:  # not a member: Maxio added the state after this SDK was generated
        return "unclassified"


def has_access(state: SubscriptionStateOrStr | UnsetType) -> bool:
    """True for active, trialing, past_due and soft_failure. False for everything else.

    A transient or unclassified state also gives False here, which is right only when you have no
    earlier decision. When you have one, use `access_decision`.
    """
    return standing(state) == "live"


def access_decision(state: SubscriptionStateOrStr | UnsetType, *, previous: bool) -> bool:
    """The access decision to store for a subscription that is now in `state`.

    `previous` is the decision you stored last for this subscription. It comes back unchanged for a
    transient state and for an unclassified one: neither is a basis for changing access.
    """
    match standing(state):
        case "live":
            return True
        case "recoverable" | "ended":
            return False
        case "transient" | "unclassified":
            return previous
