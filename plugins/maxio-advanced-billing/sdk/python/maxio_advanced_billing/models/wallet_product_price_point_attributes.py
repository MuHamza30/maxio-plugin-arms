from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.interval_unit import IntervalUnitOrStr
from .enums.pricing_scheme import PricingSchemeOrStr
from .price1 import Price1, Price1Dict


class WalletProductPricePointAttributes(SdkBaseModel):
    """A price point to create for the Wallet Product, in the same call that creates or updates it."""

    name: str
    """The price point's name. Required. Omitting it fails validation with a message that reads ``Name: cannot be
    blank.``, not naming the price point."""

    handle: Optional[str] = UNSET
    pricing_scheme: Optional[PricingSchemeOrStr] = UNSET
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    unit_price: OptionalNullable[str] = UNSET
    """Required when ``pricing_scheme`` is ``per_unit``."""

    tax_included: Optional[bool] = UNSET
    interval: Optional[int] = UNSET
    """Requires Multifrequency to be enabled on the site."""

    interval_unit: Optional[IntervalUnitOrStr] = UNSET
    use_site_exchange_rate: Optional[bool] = UNSET
    prices: Optional[list[Price1]] = UNSET
    """Required for every ``pricing_scheme`` other than ``per_unit``."""


class WalletProductPricePointAttributesDict(TypedDict):
    name: str
    handle: NotRequired[str]
    pricing_scheme: NotRequired[PricingSchemeOrStr]
    unit_price: NotRequired[str | None]
    tax_included: NotRequired[bool]
    interval: NotRequired[int]
    interval_unit: NotRequired[IntervalUnitOrStr]
    use_site_exchange_rate: NotRequired[bool]
    prices: NotRequired[list[Price1Dict]]
