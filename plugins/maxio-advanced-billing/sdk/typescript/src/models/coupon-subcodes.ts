import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CouponSubcodes = {
  codes?: string[];
};

export const couponSubcodesSchema: Schema<CouponSubcodes> = s.object<CouponSubcodes>({
  codes: s.optional(s.array(s.string())),
});
