import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditNoteSchema, type CreditNote } from "./credit-note.js";
import {
  invoiceConsolidationLevelSchema,
  type InvoiceConsolidationLevel,
} from "./invoice-consolidation-level.js";

/** Example schema for an `refund_invoice` event */
export type RefundInvoiceEventData = {
  /** If true, credit was created and applied it to the invoice. */
  applyCredit: boolean;
  /**
   * Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold
   * one of the following values:
   *
   * * "none": A normal invoice with no consolidation.
   * * "child": An invoice segment which has been combined into a consolidated invoice.
   * * "parent": A consolidated invoice, whose contents are composed of invoice segments.
   *
   * "Parent" invoices do not have lines of their own, but they have subtotals and totals which
   * aggregate the member invoice segments.
   *
   * See also the [invoice consolidation
   * documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation).
   */
  consolidationLevel?: InvoiceConsolidationLevel;
  creditNoteAttributes: CreditNote;
  /** The refund memo. */
  memo?: string;
  /** The full, original amount of the refund. */
  originalAmount?: string;
  /** The ID of the payment transaction to be refunded. */
  paymentId: number;
  /** The amount of the refund. */
  refundAmount: string;
  /** The ID of the refund transaction. */
  refundId: number;
  /** The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" */
  transactionTime: Date;
};

export const refundInvoiceEventDataSchema: Schema<RefundInvoiceEventData> = s.object<RefundInvoiceEventData>({
  applyCredit: s.boolean(),
  consolidationLevel: s.optional(s.lazy(() => invoiceConsolidationLevelSchema)),
  creditNoteAttributes: creditNoteSchema,
  memo: s.optional(s.string()),
  originalAmount: s.optional(s.string()),
  paymentId: s.int(),
  refundAmount: s.string(),
  refundId: s.int(),
  transactionTime: s.dateTime(),
  _keysMap: {
    applyCredit: "apply_credit",
    consolidationLevel: "consolidation_level",
    creditNoteAttributes: "credit_note_attributes",
    originalAmount: "original_amount",
    paymentId: "payment_id",
    refundAmount: "refund_amount",
    refundId: "refund_id",
    transactionTime: "transaction_time",
  },
});
