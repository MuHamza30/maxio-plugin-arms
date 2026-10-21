import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceEventPaymentMethodSchema,
  type InvoiceEventPaymentMethod,
} from "./invoice-event-payment-method.js";

export type PaymentMethodCreditCard = {
  cardBrand: string;
  cardExpiration?: string;
  lastFour?: string | null;
  maskedCardNumber: string;
  type: InvoiceEventPaymentMethod;
};

export const paymentMethodCreditCardSchema: Schema<PaymentMethodCreditCard> =
  s.object<PaymentMethodCreditCard>({
    cardBrand: s.string(),
    cardExpiration: s.optional(s.string()),
    lastFour: s.optionalNullable(s.string()),
    maskedCardNumber: s.string(),
    type: invoiceEventPaymentMethodSchema,
    _keysMap: {
      cardBrand: "card_brand",
      cardExpiration: "card_expiration",
      lastFour: "last_four",
      maskedCardNumber: "masked_card_number",
    },
  });
