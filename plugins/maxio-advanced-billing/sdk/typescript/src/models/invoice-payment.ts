import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoicePaymentMethodSchema, type InvoicePaymentMethod } from "./invoice-payment-method.js";

export type InvoicePayment = {
  transactionTime?: Date;
  memo?: string;
  originalAmount?: string;
  appliedAmount?: string;
  paymentMethod?: InvoicePaymentMethod;
  transactionId?: number;
  prepayment?: boolean;
  gatewayHandle?: string | null;
  gatewayUsed?: string;
  /** The transaction ID for the payment as returned from the payment gateway */
  gatewayTransactionId?: string | null;
  /**
   * Date reflecting when the payment was received from a customer. Must be in the past. Applicable
   * only to `external` payments.
   */
  receivedOn?: string | null;
  uid?: string;
};

export const invoicePaymentSchema: Schema<InvoicePayment> = s.object<InvoicePayment>({
  transactionTime: s.optional(s.dateTime()),
  memo: s.optional(s.string()),
  originalAmount: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  paymentMethod: s.optional(s.lazy(() => invoicePaymentMethodSchema)),
  transactionId: s.optional(s.int()),
  prepayment: s.optional(s.boolean()),
  gatewayHandle: s.optionalNullable(s.string()),
  gatewayUsed: s.optional(s.string()),
  gatewayTransactionId: s.optionalNullable(s.string()),
  receivedOn: s.optionalNullable(s.dateOnly()),
  uid: s.optional(s.string()),
  _keysMap: {
    transactionTime: "transaction_time",
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
    paymentMethod: "payment_method",
    transactionId: "transaction_id",
    gatewayHandle: "gateway_handle",
    gatewayUsed: "gateway_used",
    gatewayTransactionId: "gateway_transaction_id",
    receivedOn: "received_on",
  },
});
