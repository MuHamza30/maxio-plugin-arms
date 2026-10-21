from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.item_category import ItemCategoryOrStr
from .wallet_product_price_point_attributes import (
    WalletProductPricePointAttributes,
    WalletProductPricePointAttributesDict,
)


class WalletProduct(SdkBaseModel):
    name: str
    unit_name: str
    """The name of the unit the Wallet Product's usage is measured in, for example ``tokens``."""

    handle: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    taxable: Optional[bool] = UNSET
    tax_code: OptionalNullable[str] = UNSET
    accounting_code: OptionalNullable[str] = UNSET
    item_category: OptionalNullable[ItemCategoryOrStr] = UNSET
    """One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other"""

    price_point: Optional[WalletProductPricePointAttributes] = UNSET
    """Creates one price point for the Wallet Product in the same call. Ignored if ``price_points`` is also sent."""

    price_points: Optional[list[WalletProductPricePointAttributes]] = UNSET
    """Creates several price points for the Wallet Product in the same call, winning over ``price_point`` if both are
    sent. The first price point created becomes the Wallet Product's default. The whole call is one transaction: if any
    price point in the array fails validation, nothing is created, including the Wallet Product itself."""


class WalletProductDict(TypedDict):
    name: str
    unit_name: str
    handle: NotRequired[str]
    description: NotRequired[str | None]
    taxable: NotRequired[bool]
    tax_code: NotRequired[str | None]
    accounting_code: NotRequired[str | None]
    item_category: NotRequired[ItemCategoryOrStr | None]
    price_point: NotRequired[WalletProductPricePointAttributesDict]
    price_points: NotRequired[list[WalletProductPricePointAttributesDict]]
