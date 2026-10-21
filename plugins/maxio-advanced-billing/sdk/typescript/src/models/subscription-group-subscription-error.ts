import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Object which contains subscription errors. */
export type SubscriptionGroupSubscriptionError = {
  product?: string[];
  productPricePointId?: string[];
  paymentProfile?: string[];
  paymentProfileChargifyToken?: string[];
  base?: string[];
  paymentProfileExpirationMonth?: string[];
  paymentProfileExpirationYear?: string[];
  paymentProfileFullNumber?: string[];
};

export const subscriptionGroupSubscriptionErrorSchema: Schema<SubscriptionGroupSubscriptionError> =
  s.object<SubscriptionGroupSubscriptionError>({
    product: s.optional(s.array(s.string())),
    productPricePointId: s.optional(s.array(s.string())),
    paymentProfile: s.optional(s.array(s.string())),
    paymentProfileChargifyToken: s.optional(s.array(s.string())),
    base: s.optional(s.array(s.string())),
    paymentProfileExpirationMonth: s.optional(s.array(s.string())),
    paymentProfileExpirationYear: s.optional(s.array(s.string())),
    paymentProfileFullNumber: s.optional(s.array(s.string())),
    _keysMap: {
      productPricePointId: "product_price_point_id",
      paymentProfile: "payment_profile",
      paymentProfileChargifyToken: "payment_profile.chargify_token",
      paymentProfileExpirationMonth: "payment_profile.expiration_month",
      paymentProfileExpirationYear: "payment_profile.expiration_year",
      paymentProfileFullNumber: "payment_profile.full_number",
    },
  });
