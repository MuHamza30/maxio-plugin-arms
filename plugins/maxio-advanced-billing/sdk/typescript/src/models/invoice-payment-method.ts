import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoicePaymentMethod = {
  details?: string;
  kind?: string;
  memo?: string;
  type?: string;
  cardBrand?: string;
  cardExpiration?: string;
  lastFour?: string | null;
  maskedCardNumber?: string;
};

export const invoicePaymentMethodSchema: Schema<InvoicePaymentMethod> = s.object<InvoicePaymentMethod>({
  details: s.optional(s.string()),
  kind: s.optional(s.string()),
  memo: s.optional(s.string()),
  type: s.optional(s.string()),
  cardBrand: s.optional(s.string()),
  cardExpiration: s.optional(s.string()),
  lastFour: s.optionalNullable(s.string()),
  maskedCardNumber: s.optional(s.string()),
  _keysMap: {
    cardBrand: "card_brand",
    cardExpiration: "card_expiration",
    lastFour: "last_four",
    maskedCardNumber: "masked_card_number",
  },
});
