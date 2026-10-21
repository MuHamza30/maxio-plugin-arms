from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pricing_scheme import PricingSchemeOrStr
from .price import Price, PriceDict


class ScheduledRenewalComponentCustomPrice(SdkBaseModel):
    """Custom pricing for a component within a scheduled renewal."""

    tax_included: Optional[bool] = UNSET
    """Whether or not the price point includes tax"""

    pricing_scheme: PricingSchemeOrStr
    """Omit for On/Off components."""

    prices: list[Price]
    """On/off components only need one price bracket starting at 1."""


class ScheduledRenewalComponentCustomPriceDict(TypedDict):
    tax_included: NotRequired[bool]
    pricing_scheme: PricingSchemeOrStr
    prices: list[PriceDict]
