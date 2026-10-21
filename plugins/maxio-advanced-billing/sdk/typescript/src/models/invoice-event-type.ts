import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Invoice Event Type */
export const InvoiceEventType = {
  IssueInvoice: "issue_invoice",
  ApplyCreditNote: "apply_credit_note",
  CreateCreditNote: "create_credit_note",
  ApplyPayment: "apply_payment",
  ApplyDebitNote: "apply_debit_note",
  CreateDebitNote: "create_debit_note",
  RefundInvoice: "refund_invoice",
  VoidInvoice: "void_invoice",
  VoidRemainder: "void_remainder",
  BackportInvoice: "backport_invoice",
  ChangeInvoiceStatus: "change_invoice_status",
  ChangeInvoiceCollectionMethod: "change_invoice_collection_method",
  RemovePayment: "remove_payment",
  FailedPayment: "failed_payment",
  ChangeChargebackStatus: "change_chargeback_status",
} as const;
export type InvoiceEventType = (typeof InvoiceEventType)[keyof typeof InvoiceEventType] | (string & {});

export const invoiceEventTypeSchema: EnumSchema<InvoiceEventType> =
  s.enumOf<InvoiceEventType>(InvoiceEventType);
