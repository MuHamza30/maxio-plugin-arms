from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .billing_manifest_item import BillingManifestItem, BillingManifestItemDict


class BillingManifest(SdkBaseModel):
    line_items: Optional[list[BillingManifestItem]] = UNSET
    total_in_cents: Optional[int] = UNSET
    total_discount_in_cents: Optional[int] = UNSET
    total_tax_in_cents: Optional[int] = UNSET
    subtotal_in_cents: Optional[int] = UNSET
    start_date: OptionalNullable[RFC3339DateTime] = UNSET
    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    period_type: OptionalNullable[str] = UNSET
    existing_balance_in_cents: Optional[int] = UNSET


class BillingManifestDict(TypedDict):
    line_items: NotRequired[list[BillingManifestItemDict]]
    total_in_cents: NotRequired[int]
    total_discount_in_cents: NotRequired[int]
    total_tax_in_cents: NotRequired[int]
    subtotal_in_cents: NotRequired[int]
    start_date: NotRequired[RFC3339DateTime | None]
    end_date: NotRequired[RFC3339DateTime | None]
    period_type: NotRequired[str | None]
    existing_balance_in_cents: NotRequired[int]
