from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceEventType(str, Enum):
    """Invoice Event Type"""

    ISSUE_INVOICE = "issue_invoice"
    APPLY_CREDIT_NOTE = "apply_credit_note"
    CREATE_CREDIT_NOTE = "create_credit_note"
    APPLY_PAYMENT = "apply_payment"
    APPLY_DEBIT_NOTE = "apply_debit_note"
    CREATE_DEBIT_NOTE = "create_debit_note"
    REFUND_INVOICE = "refund_invoice"
    VOID_INVOICE = "void_invoice"
    VOID_REMAINDER = "void_remainder"
    BACKPORT_INVOICE = "backport_invoice"
    CHANGE_INVOICE_STATUS = "change_invoice_status"
    CHANGE_INVOICE_COLLECTION_METHOD = "change_invoice_collection_method"
    REMOVE_PAYMENT = "remove_payment"
    FAILED_PAYMENT = "failed_payment"
    CHANGE_CHARGEBACK_STATUS = "change_chargeback_status"

    __str__ = str.__str__


InvoiceEventTypeOrStr: TypeAlias = Annotated[InvoiceEventType | str, open_enum_validator(InvoiceEventType)]
