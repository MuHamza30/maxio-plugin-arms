from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateCurrencyPrice(SdkBaseModel):
    currency: Optional[str] = UNSET
    """ISO code for a currency defined on the site level"""

    price: Optional[float] = UNSET
    """Price for the price level in this currency"""

    price_id: Optional[int] = UNSET
    """ID of the price that this corresponds with"""


class CreateCurrencyPriceDict(TypedDict):
    currency: NotRequired[str]
    price: NotRequired[float]
    price_id: NotRequired[int]
