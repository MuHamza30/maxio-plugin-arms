import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * PCI-safe cardholder fields only. Full card numbers, CVV, and billing address are never included.
 */
export type PaymentProfileParams = {
  firstName?: string;
  lastName?: string;
  cardType?: string;
};

export const paymentProfileParamsSchema: Schema<PaymentProfileParams> = s.object<PaymentProfileParams>({
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  cardType: s.optional(s.string()),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
    cardType: "card_type",
  },
});
