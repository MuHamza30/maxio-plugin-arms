import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { compoundingStrategySchema, type CompoundingStrategy } from "./compounding-strategy.js";
import { amount2Schema, type Amount2 } from "./unions/amount2.js";
import { percentage1Schema, type Percentage1 } from "./unions/percentage1.js";
import { productFamilyIdSchema, type ProductFamilyId } from "./unions/product-family-id.js";

export type CreateInvoiceCoupon = {
  code?: string;
  subcode?: string;
  percentage?: Percentage1;
  amount?: Amount2;
  description?: string;
  productFamilyId?: ProductFamilyId;
  /**
   * Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be
   * calculated against the remaining price, after prior discounts have been calculated. For
   * `full-price`, Percentage-based discounts will always be calculated against the original item
   * price, before other discounts are applied.
   */
  compoundingStrategy?: CompoundingStrategy;
};

export const createInvoiceCouponSchema: Schema<CreateInvoiceCoupon> = s.object<CreateInvoiceCoupon>({
  code: s.optional(s.string()),
  subcode: s.optional(s.string()),
  percentage: s.optional(s.lazy(() => percentage1Schema)),
  amount: s.optional(s.lazy(() => amount2Schema)),
  description: s.optional(s.string()),
  productFamilyId: s.optional(s.lazy(() => productFamilyIdSchema)),
  compoundingStrategy: s.optional(s.lazy(() => compoundingStrategySchema)),
  _keysMap: {
    productFamilyId: "product_family_id",
    compoundingStrategy: "compounding_strategy",
  },
});
