from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Reason(str, Enum):
    """Set whenever ``status`` isn't ``active``. Accompanying ``stopped``: ``entitlement_missing`` (an ordinary product
    or component change removed the entitlement), ``wallet_archived`` (the wallet was archived),
    ``subscription_terminated`` (the subscription reached a terminal state), ``feature_removed`` (the subscription no
    longer has this Feature), ``wallet_behavior_disabled`` (the Feature no longer has ``wallet_behavior`` configured),
    ``superseded_by_replacement`` (a later entitlement now funds this wallet instead), or ``subscription_prepaid`` (the
    subscription switched to prepaid, which cannot carry an active wallet). Accompanying ``erroring``:
    ``allowance_not_representable`` (the entitlement's current allowance doesn't fit the wallet's amount encoding) or
    ``balance_at_capacity`` (granting it would push the balance past the maximum supported value)."""

    ENTITLEMENT_MISSING = "entitlement_missing"
    WALLET_ARCHIVED = "wallet_archived"
    SUBSCRIPTION_TERMINATED = "subscription_terminated"
    FEATURE_REMOVED = "feature_removed"
    WALLET_BEHAVIOR_DISABLED = "wallet_behavior_disabled"
    SUPERSEDED_BY_REPLACEMENT = "superseded_by_replacement"
    SUBSCRIPTION_PREPAID = "subscription_prepaid"
    ALLOWANCE_NOT_REPRESENTABLE = "allowance_not_representable"
    BALANCE_AT_CAPACITY = "balance_at_capacity"

    __str__ = str.__str__


ReasonOrStr: TypeAlias = Annotated[Reason | str, open_enum_validator(Reason)]
