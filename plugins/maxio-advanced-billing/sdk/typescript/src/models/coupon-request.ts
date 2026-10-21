import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { couponPayloadSchema, type CouponPayload } from "./coupon-payload.js";

export type CouponRequest = {
  coupon?: CouponPayload;
  /**
   * An object where the keys are product IDs or handles (prefixed with 'handle:'), and the values
   * are booleans indicating if the coupon should be applicable to the product.
   */
  restrictedProducts?: Record<string, boolean>;
  /**
   * An object where the keys are component IDs or handles (prefixed with 'handle:'), and the values
   * are booleans indicating if the coupon should be applicable to the component.
   */
  restrictedComponents?: Record<string, boolean>;
};

export const couponRequestSchema: Schema<CouponRequest> = s.object<CouponRequest>({
  coupon: s.optional(s.lazy(() => couponPayloadSchema)),
  restrictedProducts: s.optional(s.record(s.string(), s.boolean())),
  restrictedComponents: s.optional(s.record(s.string(), s.boolean())),
  _keysMap: {
    restrictedProducts: "restricted_products",
    restrictedComponents: "restricted_components",
  },
});
