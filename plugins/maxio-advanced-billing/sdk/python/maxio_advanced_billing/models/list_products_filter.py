from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prepaid_product_price_point_filter import PrepaidProductPricePointFilter, PrepaidProductPricePointFilterDict


class ListProductsFilter(SdkBaseModel):
    ids: Optional[list[int]] = UNSET
    """Allows fetching products with matching id based on provided values. Use in query ``filter[ids]=1,2,3``."""

    prepaid_product_price_point: Optional[PrepaidProductPricePointFilter] = UNSET
    """Allows fetching products only if a prepaid product price point is present or not. To use this filter you also
    have to include the following param in the request ``include=prepaid_product_price_point``. Use in query
    ``filter[prepaid_product_price_point][product_price_point_id]=not_null``."""

    use_site_exchange_rate: Optional[bool] = UNSET
    """Allows fetching products with matching use_site_exchange_rate based on provided value (refers to default price
    point). Use in query ``filter[use_site_exchange_rate]=true``."""


class ListProductsFilterDict(TypedDict):
    ids: NotRequired[list[int]]
    prepaid_product_price_point: NotRequired[PrepaidProductPricePointFilterDict]
    use_site_exchange_rate: NotRequired[bool]
