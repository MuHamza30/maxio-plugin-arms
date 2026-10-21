import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceEventPaymentMethodSchema,
  type InvoiceEventPaymentMethod,
} from "./invoice-event-payment-method.js";

export type PaymentMethodExternal = {
  details: string | null;
  kind: string;
  memo: string | null;
  type: InvoiceEventPaymentMethod;
};

export const paymentMethodExternalSchema: Schema<PaymentMethodExternal> = s.object<PaymentMethodExternal>({
  details: s.nullable(s.string()),
  kind: s.string(),
  memo: s.nullable(s.string()),
  type: invoiceEventPaymentMethodSchema,
});
