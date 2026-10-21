import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreditCardAttributes = {
  fullNumber?: string;
  expirationMonth?: string;
  expirationYear?: string;
};

export const creditCardAttributesSchema: Schema<CreditCardAttributes> = s.object<CreditCardAttributes>({
  fullNumber: s.optional(s.string()),
  expirationMonth: s.optional(s.string()),
  expirationYear: s.optional(s.string()),
  _keysMap: {
    fullNumber: "full_number",
    expirationMonth: "expiration_month",
    expirationYear: "expiration_year",
  },
});
