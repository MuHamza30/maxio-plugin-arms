import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type OfferDiscount = {
  couponCode?: string;
  couponId?: number;
  couponName?: string;
};

export const offerDiscountSchema: Schema<OfferDiscount> = s.object<OfferDiscount>({
  couponCode: s.optional(s.string()),
  couponId: s.optional(s.int()),
  couponName: s.optional(s.string()),
  _keysMap: {
    couponCode: "coupon_code",
    couponId: "coupon_id",
    couponName: "coupon_name",
  },
});
