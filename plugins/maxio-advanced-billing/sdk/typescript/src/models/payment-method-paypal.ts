import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceEventPaymentMethodSchema,
  type InvoiceEventPaymentMethod,
} from "./invoice-event-payment-method.js";

export type PaymentMethodPaypal = {
  email: string;
  type: InvoiceEventPaymentMethod;
};

export const paymentMethodPaypalSchema: Schema<PaymentMethodPaypal> = s.object<PaymentMethodPaypal>({
  email: s.string(),
  type: invoiceEventPaymentMethodSchema,
});
