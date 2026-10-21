import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceRefund = {
  transactionId?: number;
  paymentId?: number;
  memo?: string;
  originalAmount?: string;
  appliedAmount?: string;
  /** The transaction ID for the refund as returned from the payment gateway */
  gatewayTransactionId?: string | null;
  gatewayUsed?: string;
  gatewayHandle?: string | null;
  achLateReject?: boolean | null;
};

export const invoiceRefundSchema: Schema<InvoiceRefund> = s.object<InvoiceRefund>({
  transactionId: s.optional(s.int()),
  paymentId: s.optional(s.int()),
  memo: s.optional(s.string()),
  originalAmount: s.optional(s.string()),
  appliedAmount: s.optional(s.string()),
  gatewayTransactionId: s.optionalNullable(s.string()),
  gatewayUsed: s.optional(s.string()),
  gatewayHandle: s.optionalNullable(s.string()),
  achLateReject: s.optionalNullable(s.boolean()),
  _keysMap: {
    transactionId: "transaction_id",
    paymentId: "payment_id",
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
    gatewayTransactionId: "gateway_transaction_id",
    gatewayUsed: "gateway_used",
    gatewayHandle: "gateway_handle",
    achLateReject: "ach_late_reject",
  },
});
