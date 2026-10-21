from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.credit_type import CreditTypeOrStr
from .enums.item_category import ItemCategoryOrStr


class UpdateComponent(SdkBaseModel):
    handle: Optional[str] = UNSET
    name: Optional[str] = UNSET
    """The name of the Component, suitable for display on statements. e.g., Text Messages."""

    description: OptionalNullable[str] = UNSET
    """The description of the component."""

    accounting_code: OptionalNullable[str] = UNSET
    taxable: Optional[bool] = UNSET
    """Boolean flag describing whether a component is taxable or not."""

    tax_code: OptionalNullable[str] = UNSET
    """A string representing the tax code related to the component type. This is especially important when using AvaTax
    to tax based on locale. This attribute has a max length of 25 characters."""

    item_category: OptionalNullable[ItemCategoryOrStr] = UNSET
    """One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other"""

    display_on_hosted_page: Optional[bool] = UNSET
    upgrade_charge: OptionalNullable[CreditTypeOrStr] = UNSET
    """The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if
    one is not provided."""

    unspsc_code: OptionalNullable[str] = UNSET
    """(Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the
    commodity code on invoice line items for this component instead of the default derived from item_category."""


class UpdateComponentDict(TypedDict):
    handle: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str | None]
    accounting_code: NotRequired[str | None]
    taxable: NotRequired[bool]
    tax_code: NotRequired[str | None]
    item_category: NotRequired[ItemCategoryOrStr | None]
    display_on_hosted_page: NotRequired[bool]
    upgrade_charge: NotRequired[CreditTypeOrStr | None]
    unspsc_code: NotRequired[str | None]
