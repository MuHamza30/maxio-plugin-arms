from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .create_allocation import CreateAllocation, CreateAllocationDict
from .enums.collection_method import CollectionMethodOrStr
from .enums.credit_type import CreditTypeOrStr


class AllocateComponents(SdkBaseModel):
    proration_upgrade_scheme: Optional[str] = UNSET
    proration_downgrade_scheme: Optional[str] = UNSET
    allocations: Optional[list[CreateAllocation]] = UNSET
    accrue_charge: Optional[bool] = UNSET
    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    payment_collection_method: Optional[CollectionMethodOrStr] = UNSET
    """(Optional) If not passed, the allocation(s) will use the payment collection method on the subscription."""

    initiate_dunning: Optional[bool] = UNSET
    """If true, if the immediate component payment fails, initiate dunning for the subscription. Otherwise, leave the
    charges on the subscription to pay for at renewal."""


class AllocateComponentsDict(TypedDict):
    proration_upgrade_scheme: NotRequired[str]
    proration_downgrade_scheme: NotRequired[str]
    allocations: NotRequired[list[CreateAllocationDict]]
    accrue_charge: NotRequired[bool]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    payment_collection_method: NotRequired[CollectionMethodOrStr]
    initiate_dunning: NotRequired[bool]
