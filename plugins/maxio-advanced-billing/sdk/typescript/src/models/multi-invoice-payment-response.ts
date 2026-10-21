import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { multiInvoicePaymentSchema, type MultiInvoicePayment } from "./multi-invoice-payment.js";

export type MultiInvoicePaymentResponse = {
  payment: MultiInvoicePayment;
};

export const multiInvoicePaymentResponseSchema: Schema<MultiInvoicePaymentResponse> =
  s.object<MultiInvoicePaymentResponse>({
    payment: multiInvoicePaymentSchema,
  });
