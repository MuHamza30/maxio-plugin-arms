import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CouponSubcodesResponse = {
  createdCodes?: string[];
  duplicateCodes?: string[];
  invalidCodes?: string[];
};

export const couponSubcodesResponseSchema: Schema<CouponSubcodesResponse> = s.object<CouponSubcodesResponse>({
  createdCodes: s.optional(s.array(s.string())),
  duplicateCodes: s.optional(s.array(s.string())),
  invalidCodes: s.optional(s.array(s.string())),
  _keysMap: {
    createdCodes: "created_codes",
    duplicateCodes: "duplicate_codes",
    invalidCodes: "invalid_codes",
  },
});
