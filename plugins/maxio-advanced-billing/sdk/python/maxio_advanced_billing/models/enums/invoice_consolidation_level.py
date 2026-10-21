from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceConsolidationLevel(str, Enum):
    """Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold one of the
    following values:

    * "none": A normal invoice with no consolidation.
    * "child": An invoice segment which has been combined into a consolidated invoice.
    * "parent": A consolidated invoice, whose contents are composed of invoice segments.

    "Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member
    invoice segments.

    See also the `invoice consolidation documentation
    <https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation>`__."""

    NONE = "none"
    CHILD = "child"
    PARENT = "parent"

    __str__ = str.__str__


InvoiceConsolidationLevelOrStr: TypeAlias = Annotated[
    InvoiceConsolidationLevel | str, open_enum_validator(InvoiceConsolidationLevel)
]
