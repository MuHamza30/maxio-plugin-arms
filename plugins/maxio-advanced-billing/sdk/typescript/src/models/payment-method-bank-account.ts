import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceEventPaymentMethodSchema,
  type InvoiceEventPaymentMethod,
} from "./invoice-event-payment-method.js";

export type PaymentMethodBankAccount = {
  maskedAccountNumber: string;
  maskedRoutingNumber: string;
  type: InvoiceEventPaymentMethod;
};

export const paymentMethodBankAccountSchema: Schema<PaymentMethodBankAccount> =
  s.object<PaymentMethodBankAccount>({
    maskedAccountNumber: s.string(),
    maskedRoutingNumber: s.string(),
    type: invoiceEventPaymentMethodSchema,
    _keysMap: {
      maskedAccountNumber: "masked_account_number",
      maskedRoutingNumber: "masked_routing_number",
    },
  });
