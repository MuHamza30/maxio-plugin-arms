from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceDisplaySettings(SdkBaseModel):
    hide_zero_subtotal_lines: Optional[bool] = UNSET
    include_discounts_on_lines: Optional[bool] = UNSET


class InvoiceDisplaySettingsDict(TypedDict):
    hide_zero_subtotal_lines: NotRequired[bool]
    include_discounts_on_lines: NotRequired[bool]
