import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { applyCreditNoteEventSchema, type ApplyCreditNoteEvent } from "../apply-credit-note-event.js";
import { applyDebitNoteEventSchema, type ApplyDebitNoteEvent } from "../apply-debit-note-event.js";
import { applyPaymentEventSchema, type ApplyPaymentEvent } from "../apply-payment-event.js";
import { backportInvoiceEventSchema, type BackportInvoiceEvent } from "../backport-invoice-event.js";
import {
  changeChargebackStatusEventSchema,
  type ChangeChargebackStatusEvent,
} from "../change-chargeback-status-event.js";
import {
  changeInvoiceCollectionMethodEventSchema,
  type ChangeInvoiceCollectionMethodEvent,
} from "../change-invoice-collection-method-event.js";
import {
  changeInvoiceStatusEventSchema,
  type ChangeInvoiceStatusEvent,
} from "../change-invoice-status-event.js";
import { createCreditNoteEventSchema, type CreateCreditNoteEvent } from "../create-credit-note-event.js";
import { createDebitNoteEventSchema, type CreateDebitNoteEvent } from "../create-debit-note-event.js";
import { failedPaymentEventSchema, type FailedPaymentEvent } from "../failed-payment-event.js";
import { issueInvoiceEventSchema, type IssueInvoiceEvent } from "../issue-invoice-event.js";
import { refundInvoiceEventSchema, type RefundInvoiceEvent } from "../refund-invoice-event.js";
import { removePaymentEventSchema, type RemovePaymentEvent } from "../remove-payment-event.js";
import { voidInvoiceEventSchema, type VoidInvoiceEvent } from "../void-invoice-event.js";
import { voidRemainderEventSchema, type VoidRemainderEvent } from "../void-remainder-event.js";

export type InvoiceEvent1 =
  | (ApplyCreditNoteEvent & { eventType: "apply_credit_note" })
  | (ApplyDebitNoteEvent & { eventType: "apply_debit_note" })
  | (ApplyPaymentEvent & { eventType: "apply_payment" })
  | (BackportInvoiceEvent & { eventType: "backport_invoice" })
  | (ChangeChargebackStatusEvent & { eventType: "change_chargeback_status" })
  | (ChangeInvoiceCollectionMethodEvent & { eventType: "change_invoice_collection_method" })
  | (ChangeInvoiceStatusEvent & { eventType: "change_invoice_status" })
  | (CreateCreditNoteEvent & { eventType: "create_credit_note" })
  | (CreateDebitNoteEvent & { eventType: "create_debit_note" })
  | (FailedPaymentEvent & { eventType: "failed_payment" })
  | (IssueInvoiceEvent & { eventType: "issue_invoice" })
  | (RefundInvoiceEvent & { eventType: "refund_invoice" })
  | (RemovePaymentEvent & { eventType: "remove_payment" })
  | (VoidInvoiceEvent & { eventType: "void_invoice" })
  | (VoidRemainderEvent & { eventType: "void_remainder" });

export const invoiceEvent1Schema: Schema<InvoiceEvent1> = s.discriminatedUnion<InvoiceEvent1>("event_type", {
  apply_credit_note: applyCreditNoteEventSchema,
  apply_debit_note: applyDebitNoteEventSchema,
  apply_payment: applyPaymentEventSchema,
  backport_invoice: backportInvoiceEventSchema,
  change_chargeback_status: changeChargebackStatusEventSchema,
  change_invoice_collection_method: changeInvoiceCollectionMethodEventSchema,
  change_invoice_status: changeInvoiceStatusEventSchema,
  create_credit_note: createCreditNoteEventSchema,
  create_debit_note: createDebitNoteEventSchema,
  failed_payment: failedPaymentEventSchema,
  issue_invoice: issueInvoiceEventSchema,
  refund_invoice: refundInvoiceEventSchema,
  remove_payment: removePaymentEventSchema,
  void_invoice: voidInvoiceEventSchema,
  void_remainder: voidRemainderEventSchema,
});
