import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be
 * calculated against the remaining price, after prior discounts have been calculated. For
 * `full-price`, Percentage-based discounts will always be calculated against the original item
 * price, before other discounts are applied.
 */
export const CompoundingStrategy = {
  Compound: "compound",
  FullPrice: "full-price",
} as const;
export type CompoundingStrategy =
  | (typeof CompoundingStrategy)[keyof typeof CompoundingStrategy]
  | (string & {});

export const compoundingStrategySchema: EnumSchema<CompoundingStrategy> =
  s.enumOf<CompoundingStrategy>(CompoundingStrategy);
