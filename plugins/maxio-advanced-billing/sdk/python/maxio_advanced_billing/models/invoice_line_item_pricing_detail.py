from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceLineItemPricingDetail(SdkBaseModel):
    label: Optional[str] = UNSET
    amount: Optional[str] = UNSET


class InvoiceLineItemPricingDetailDict(TypedDict):
    label: NotRequired[str]
    amount: NotRequired[str]
