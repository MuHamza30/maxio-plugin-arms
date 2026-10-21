import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CouponCurrency = {
  id?: number | null;
  currency?: string;
  price?: number | null;
  couponId?: number;
};

export const couponCurrencySchema: Schema<CouponCurrency> = s.object<CouponCurrency>({
  id: s.optionalNullable(s.int()),
  currency: s.optional(s.string()),
  price: s.optionalNullable(s.float64()),
  couponId: s.optional(s.int()),
  _keysMap: {
    couponId: "coupon_id",
  },
});
