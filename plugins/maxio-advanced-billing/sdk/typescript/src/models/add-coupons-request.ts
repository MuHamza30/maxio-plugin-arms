import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type AddCouponsRequest = {
  codes?: string[];
};

export const addCouponsRequestSchema: Schema<AddCouponsRequest> = s.object<AddCouponsRequest>({
  codes: s.optional(s.array(s.string())),
});
