from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PrepaidProductPricePointFilter(SdkBaseModel):
    product_price_point_id: Literal["not_null"] = "not_null"
    """Passed as a parameter to list methods to return only non null values."""


class PrepaidProductPricePointFilterDict(TypedDict):
    product_price_point_id: Literal["not_null"]
