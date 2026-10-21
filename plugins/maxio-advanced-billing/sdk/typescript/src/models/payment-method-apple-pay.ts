import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceEventPaymentMethodSchema,
  type InvoiceEventPaymentMethod,
} from "./invoice-event-payment-method.js";

export type PaymentMethodApplePay = {
  type: InvoiceEventPaymentMethod;
};

export const paymentMethodApplePaySchema: Schema<PaymentMethodApplePay> = s.object<PaymentMethodApplePay>({
  type: invoiceEventPaymentMethodSchema,
});
