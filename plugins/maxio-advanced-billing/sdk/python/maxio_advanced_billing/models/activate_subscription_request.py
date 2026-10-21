from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ActivateSubscriptionRequest(SdkBaseModel):
    revert_on_failure: OptionalNullable[bool] = UNSET
    """You may choose how to handle the activation failure. ``true`` means do not change the subscription’s state and
    billing period. ``false`` means to continue through with the activation and enter an end-of-life state. If this
    parameter is omitted or ``null`` is passed it will default to the value set in the site settings (default:
    ``true``)."""


class ActivateSubscriptionRequestDict(TypedDict):
    revert_on_failure: NotRequired[bool | None]
