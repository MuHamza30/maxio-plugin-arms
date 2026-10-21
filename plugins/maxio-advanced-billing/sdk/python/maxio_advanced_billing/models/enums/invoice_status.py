from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceStatus(str, Enum):
    """The current status of the invoice. See `Invoice Statuses
    <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses>`__
    for more."""

    DRAFT = "draft"
    OPEN = "open"
    PAID = "paid"
    PENDING = "pending"
    VOIDED = "voided"
    CANCELED = "canceled"
    PROCESSING = "processing"

    __str__ = str.__str__


InvoiceStatusOrStr: TypeAlias = Annotated[InvoiceStatus | str, open_enum_validator(InvoiceStatus)]
