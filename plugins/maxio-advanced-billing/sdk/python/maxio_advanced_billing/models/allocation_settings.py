from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.credit_type import CreditTypeOrStr


class AllocationSettings(SdkBaseModel):
    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    downgrade_credit: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    accrue_charge: Optional[str] = UNSET
    """Either "true" or "false"."""


class AllocationSettingsDict(TypedDict):
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    downgrade_credit: NotRequired[CreditTypeOrStr | None]
    accrue_charge: NotRequired[str]
