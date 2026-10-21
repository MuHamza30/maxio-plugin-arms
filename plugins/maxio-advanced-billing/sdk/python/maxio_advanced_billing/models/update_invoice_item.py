from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.component_id3 import ComponentId3, ComponentId3Dict
from .unions.price_point_id4 import PricePointId4, PricePointId4Dict
from .unions.product_id import ProductId, ProductIdDict
from .unions.product_price_point_id import ProductPricePointId, ProductPricePointIdDict
from .unions.quantity3 import Quantity3, Quantity3Dict
from .unions.unit_price7 import UnitPrice7, UnitPrice7Dict


class UpdateInvoiceItem(SdkBaseModel):
    """A line item change for a draft ad hoc invoice. Supports the same attributes as line items on invoice creation,
    plus ``uid`` and ``_destroy`` for updating or removing existing line items."""

    title: Optional[str] = UNSET
    quantity: Optional[Quantity3] = UNSET
    """The quantity can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065. If you submit a value with
    more than 8 decimal places, we will round it down to the 8th decimal place."""

    unit_price: Optional[UnitPrice7] = UNSET
    """The unit_price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065. If you submit a value with
    more than 8 decimal places, we will round it down to the 8th decimal place."""

    taxable: Optional[bool] = UNSET
    """Set to true to automatically calculate taxes. Site must be configured to use and calculate taxes. If using
    AvaTax, a tax_code parameter must also be sent."""

    tax_code: Optional[str] = UNSET
    """A string representing the tax code related to the product type. This is especially important when using AvaTax to
    tax based on locale. This attribute has a max length of 25 characters."""

    period_range_start: Optional[str] = UNSET
    """YYYY-MM-DD"""

    period_range_end: Optional[str] = UNSET
    """YYYY-MM-DD"""

    product_id: Optional[ProductId] = UNSET
    """Product handle or product id."""

    component_id: Optional[ComponentId3] = UNSET
    """Component handle or component id."""

    price_point_id: Optional[PricePointId4] = UNSET
    """Price point handle or id. For component."""

    product_price_point_id: Optional[ProductPricePointId] = UNSET
    description: Optional[str] = UNSET
    uid: Optional[str] = UNSET
    """Unique identifier of an existing line item on the invoice. When provided, the matching line item is updated with
    the submitted attributes. When omitted, a new line item is added to the invoice."""

    destroy: Optional[bool] = Field(default=UNSET, alias="_destroy")
    """Set to ``true`` together with ``uid`` to remove the matching line item from the invoice. Line items not
    referenced in the request remain unchanged."""


class UpdateInvoiceItemDict(TypedDict):
    title: NotRequired[str]
    quantity: NotRequired[Quantity3Dict]
    unit_price: NotRequired[UnitPrice7Dict]
    taxable: NotRequired[bool]
    tax_code: NotRequired[str]
    period_range_start: NotRequired[str]
    period_range_end: NotRequired[str]
    product_id: NotRequired[ProductIdDict]
    component_id: NotRequired[ComponentId3Dict]
    price_point_id: NotRequired[PricePointId4Dict]
    product_price_point_id: NotRequired[ProductPricePointIdDict]
    description: NotRequired[str]
    uid: NotRequired[str]
    destroy: NotRequired[bool]
