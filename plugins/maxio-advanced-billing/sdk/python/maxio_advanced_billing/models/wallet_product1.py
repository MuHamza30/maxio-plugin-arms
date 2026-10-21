from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.item_category import ItemCategoryOrStr


class WalletProduct1(SdkBaseModel):
    name: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    taxable: Optional[bool] = UNSET
    tax_code: OptionalNullable[str] = UNSET
    accounting_code: OptionalNullable[str] = UNSET
    item_category: OptionalNullable[ItemCategoryOrStr] = UNSET
    """One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other"""


class WalletProduct1Dict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str | None]
    taxable: NotRequired[bool]
    tax_code: NotRequired[str | None]
    accounting_code: NotRequired[str | None]
    item_category: NotRequired[ItemCategoryOrStr | None]
