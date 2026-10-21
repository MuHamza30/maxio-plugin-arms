from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoicePaymentType(str, Enum):
    """The type of payment to be applied to an Invoice. Defaults to external."""

    EXTERNAL = "external"
    PREPAYMENT = "prepayment"
    SERVICE_CREDIT = "service_credit"
    PAYMENT = "payment"

    __str__ = str.__str__


InvoicePaymentTypeOrStr: TypeAlias = Annotated[InvoicePaymentType | str, open_enum_validator(InvoicePaymentType)]
