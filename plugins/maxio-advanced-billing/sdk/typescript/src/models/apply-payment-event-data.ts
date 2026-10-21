import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceConsolidationLevelSchema,
  type InvoiceConsolidationLevel,
} from "./invoice-consolidation-level.js";
import { invoiceEventPaymentSchema, type InvoiceEventPayment } from "./unions/invoice-event-payment.js";

/** Example schema for an `apply_payment` event */
export type ApplyPaymentEventData = {
  consolidationLevel: InvoiceConsolidationLevel;
  /** The payment memo */
  memo: string;
  /**
   * The full, original amount of the payment transaction as a string in full units. Incoming
   * payments can be split amongst several invoices, which will result in a `applied_amount` less
   * than the `original_amount`. Example: A $100.99 payment, of which $40.11 is applied to this
   * invoice, will have an `original_amount` of `"100.99"`.
   */
  originalAmount: string;
  /**
   * The amount of the payment applied to this invoice. Incoming payments can be split amongst
   * several invoices, which will result in a `applied_amount` less than the `original_amount`.
   * Example: A $100.99 payment, of which $40.11 is applied to this invoice, will have an
   * `applied_amount` of `"40.11"`.
   */
  appliedAmount: string;
  /** The time the payment was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" */
  transactionTime: Date;
  /** A nested data structure detailing the method of payment */
  paymentMethod: InvoiceEventPayment;
  /** The Chargify id of the original payment */
  transactionId?: number;
  parentInvoiceNumber?: number | null;
  remainingPrepaymentAmount?: string | null;
  prepayment?: boolean;
  external?: boolean;
};

export const applyPaymentEventDataSchema: Schema<ApplyPaymentEventData> = s.object<ApplyPaymentEventData>({
  consolidationLevel: invoiceConsolidationLevelSchema,
  memo: s.string(),
  originalAmount: s.string(),
  appliedAmount: s.string(),
  transactionTime: s.dateTime(),
  paymentMethod: invoiceEventPaymentSchema,
  transactionId: s.optional(s.int()),
  parentInvoiceNumber: s.optionalNullable(s.int()),
  remainingPrepaymentAmount: s.optionalNullable(s.string()),
  prepayment: s.optional(s.boolean()),
  external: s.optional(s.boolean()),
  _keysMap: {
    consolidationLevel: "consolidation_level",
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
    transactionTime: "transaction_time",
    paymentMethod: "payment_method",
    transactionId: "transaction_id",
    parentInvoiceNumber: "parent_invoice_number",
    remainingPrepaymentAmount: "remaining_prepayment_amount",
  },
});
