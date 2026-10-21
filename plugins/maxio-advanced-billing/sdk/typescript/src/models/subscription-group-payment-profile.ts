import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionGroupPaymentProfile = {
  id?: number;
  firstName?: string;
  lastName?: string;
  maskedCardNumber?: string;
};

export const subscriptionGroupPaymentProfileSchema: Schema<SubscriptionGroupPaymentProfile> =
  s.object<SubscriptionGroupPaymentProfile>({
    id: s.optional(s.int()),
    firstName: s.optional(s.string()),
    lastName: s.optional(s.string()),
    maskedCardNumber: s.optional(s.string()),
    _keysMap: {
      firstName: "first_name",
      lastName: "last_name",
      maskedCardNumber: "masked_card_number",
    },
  });
