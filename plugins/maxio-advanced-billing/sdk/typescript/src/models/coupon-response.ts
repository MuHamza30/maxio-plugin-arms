import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { couponSchema, type Coupon } from "./coupon.js";

export type CouponResponse = {
  coupon?: Coupon;
};

export const couponResponseSchema: Schema<CouponResponse> = s.object<CouponResponse>({
  coupon: s.optional(s.lazy(() => couponSchema)),
});
