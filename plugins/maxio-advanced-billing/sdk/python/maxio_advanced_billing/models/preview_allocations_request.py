from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .create_allocation import CreateAllocation, CreateAllocationDict
from .enums.credit_type import CreditTypeOrStr


class PreviewAllocationsRequest(SdkBaseModel):
    allocations: list[CreateAllocation]
    effective_proration_date: Optional[Date] = UNSET
    """To calculate proration amounts for a future time. Only within a current subscription period. Only ISO8601 format
    is supported."""

    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""


class PreviewAllocationsRequestDict(TypedDict):
    allocations: list[CreateAllocationDict]
    effective_proration_date: NotRequired[Date]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
