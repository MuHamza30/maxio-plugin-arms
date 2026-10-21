import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceEventPaymentSchema, type InvoiceEventPayment } from "./unions/invoice-event-payment.js";

/** Example schema for an `remove_payment` event */
export type RemovePaymentEventData = {
  /** Transaction ID of the original payment that was removed */
  transactionId: number;
  /** Memo of the original payment */
  memo: string;
  /** Full amount of the original payment */
  originalAmount?: string;
  /** Applied amount of the original payment */
  appliedAmount: string;
  /** Transaction time of the original payment, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" */
  transactionTime: Date;
  /** A nested data structure detailing the method of payment */
  paymentMethod: InvoiceEventPayment;
  /** The flag that shows whether the original payment was a prepayment or not */
  prepayment: boolean;
};

export const removePaymentEventDataSchema: Schema<RemovePaymentEventData> = s.object<RemovePaymentEventData>({
  transactionId: s.int(),
  memo: s.string(),
  originalAmount: s.optional(s.string()),
  appliedAmount: s.string(),
  transactionTime: s.dateTime(),
  paymentMethod: invoiceEventPaymentSchema,
  prepayment: s.boolean(),
  _keysMap: {
    transactionId: "transaction_id",
    originalAmount: "original_amount",
    appliedAmount: "applied_amount",
    transactionTime: "transaction_time",
    paymentMethod: "payment_method",
  },
});
