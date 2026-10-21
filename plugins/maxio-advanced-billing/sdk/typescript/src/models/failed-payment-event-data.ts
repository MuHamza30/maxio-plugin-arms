import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoicePaymentMethodTypeSchema,
  type InvoicePaymentMethodType,
} from "./invoice-payment-method-type.js";

/** Example schema for an `failed_payment` event */
export type FailedPaymentEventData = {
  /** The monetary value of the payment, expressed in cents. */
  amountInCents: number;
  /** The monetary value of the payment, expressed in dollars. */
  appliedAmount: number;
  /** The memo passed when the payment was created. */
  memo?: string | null;
  paymentMethod: InvoicePaymentMethodType;
  /** The transaction ID of the failed payment. */
  transactionId: number;
};

export const failedPaymentEventDataSchema: Schema<FailedPaymentEventData> = s.object<FailedPaymentEventData>({
  amountInCents: s.int(),
  appliedAmount: s.int(),
  memo: s.optionalNullable(s.string()),
  paymentMethod: invoicePaymentMethodTypeSchema,
  transactionId: s.int(),
  _keysMap: {
    amountInCents: "amount_in_cents",
    appliedAmount: "applied_amount",
    paymentMethod: "payment_method",
    transactionId: "transaction_id",
  },
});
