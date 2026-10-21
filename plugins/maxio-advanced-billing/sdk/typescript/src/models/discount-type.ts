import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const DiscountType = {
  Amount: "amount",
  Percent: "percent",
} as const;
export type DiscountType = (typeof DiscountType)[keyof typeof DiscountType] | (string & {});

export const discountTypeSchema: EnumSchema<DiscountType> = s.enumOf<DiscountType>(DiscountType);
