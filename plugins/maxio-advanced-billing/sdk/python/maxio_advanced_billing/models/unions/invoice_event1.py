from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..apply_credit_note_event import ApplyCreditNoteEvent, ApplyCreditNoteEventDict
from ..apply_debit_note_event import ApplyDebitNoteEvent, ApplyDebitNoteEventDict
from ..apply_payment_event import ApplyPaymentEvent, ApplyPaymentEventDict
from ..backport_invoice_event import BackportInvoiceEvent, BackportInvoiceEventDict
from ..change_chargeback_status_event import ChangeChargebackStatusEvent, ChangeChargebackStatusEventDict
from ..change_invoice_collection_method_event import (
    ChangeInvoiceCollectionMethodEvent,
    ChangeInvoiceCollectionMethodEventDict,
)
from ..change_invoice_status_event import ChangeInvoiceStatusEvent, ChangeInvoiceStatusEventDict
from ..create_credit_note_event import CreateCreditNoteEvent, CreateCreditNoteEventDict
from ..create_debit_note_event import CreateDebitNoteEvent, CreateDebitNoteEventDict
from ..failed_payment_event import FailedPaymentEvent, FailedPaymentEventDict
from ..issue_invoice_event import IssueInvoiceEvent, IssueInvoiceEventDict
from ..refund_invoice_event import RefundInvoiceEvent, RefundInvoiceEventDict
from ..remove_payment_event import RemovePaymentEvent, RemovePaymentEventDict
from ..void_invoice_event import VoidInvoiceEvent, VoidInvoiceEventDict
from ..void_remainder_event import VoidRemainderEvent, VoidRemainderEventDict

InvoiceEvent1: TypeAlias = Annotated[
    (
        Annotated[ApplyCreditNoteEvent, Tag("apply_credit_note")]
        | Annotated[ApplyDebitNoteEvent, Tag("apply_debit_note")]
        | Annotated[ApplyPaymentEvent, Tag("apply_payment")]
        | Annotated[BackportInvoiceEvent, Tag("backport_invoice")]
        | Annotated[ChangeChargebackStatusEvent, Tag("change_chargeback_status")]
        | Annotated[ChangeInvoiceCollectionMethodEvent, Tag("change_invoice_collection_method")]
        | Annotated[ChangeInvoiceStatusEvent, Tag("change_invoice_status")]
        | Annotated[CreateCreditNoteEvent, Tag("create_credit_note")]
        | Annotated[CreateDebitNoteEvent, Tag("create_debit_note")]
        | Annotated[FailedPaymentEvent, Tag("failed_payment")]
        | Annotated[IssueInvoiceEvent, Tag("issue_invoice")]
        | Annotated[RefundInvoiceEvent, Tag("refund_invoice")]
        | Annotated[RemovePaymentEvent, Tag("remove_payment")]
        | Annotated[VoidInvoiceEvent, Tag("void_invoice")]
        | Annotated[VoidRemainderEvent, Tag("void_remainder")]
    ),
    WireDiscriminator("event_type"),
]

InvoiceEvent1Dict: TypeAlias = (
    ApplyCreditNoteEventDict
    | ApplyDebitNoteEventDict
    | ApplyPaymentEventDict
    | BackportInvoiceEventDict
    | ChangeChargebackStatusEventDict
    | ChangeInvoiceCollectionMethodEventDict
    | ChangeInvoiceStatusEventDict
    | CreateCreditNoteEventDict
    | CreateDebitNoteEventDict
    | FailedPaymentEventDict
    | IssueInvoiceEventDict
    | RefundInvoiceEventDict
    | RemovePaymentEventDict
    | VoidInvoiceEventDict
    | VoidRemainderEventDict
)
