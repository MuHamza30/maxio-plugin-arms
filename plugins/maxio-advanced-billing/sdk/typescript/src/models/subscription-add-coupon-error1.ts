import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionAddCouponError1 = {
  codes?: string[];
  couponCode?: string[];
  couponCodes?: string[];
  subscription?: string[];
};

export const subscriptionAddCouponError1Schema: Schema<SubscriptionAddCouponError1> =
  s.object<SubscriptionAddCouponError1>({
    codes: s.optional(s.array(s.string())),
    couponCode: s.optional(s.array(s.string())),
    couponCodes: s.optional(s.array(s.string())),
    subscription: s.optional(s.array(s.string())),
    _keysMap: {
      couponCode: "coupon_code",
      couponCodes: "coupon_codes",
    },
  });
