from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionGroupCustomer(SdkBaseModel):
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    organization: Optional[str] = UNSET
    email: Optional[str] = UNSET
    reference: Optional[str] = UNSET


class SubscriptionGroupCustomerDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    organization: NotRequired[str]
    email: NotRequired[str]
    reference: NotRequired[str]
