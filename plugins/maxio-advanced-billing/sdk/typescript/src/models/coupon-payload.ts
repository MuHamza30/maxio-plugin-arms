import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { compoundingStrategySchema, type CompoundingStrategy } from "./compounding-strategy.js";
import { percentageSchema, type Percentage } from "./unions/percentage.js";

export type CouponPayload = {
  /**
   * Required when creating a new coupon. This name is not displayed to customers and is limited to
   * 255 characters.
   */
  name?: string;
  /**
   * Required when creating a new coupon. The code is limited to 255 characters. May contain
   * uppercase alphanumeric characters and these special characters (which allow for email addresses
   * to be used): “%”, “@”, “+”, “-”, “_”, and “.”.
   */
  code?: string;
  /**
   * Required when creating a new coupon. A description of the coupon that can be displayed to
   * customers in transactions and on statements. The description is limited to 255 characters.
   */
  description?: string;
  /**
   * Required when creating a new percentage coupon. Can't be used together with amount_in_cents.
   * Percentage discount.
   */
  percentage?: Percentage;
  /**
   * Required when creating a new flat amount coupon. Can't be used together with percentage. Flat
   * USD discount.
   */
  amountInCents?: number;
  /**
   * If set to true, discount is not limited (credits will carry forward to next billing). Can't be
   * used together with restrictions.
   */
  allowNegativeBalance?: boolean;
  recurring?: boolean;
  /**
   * After the end of the given day, this coupon code will be invalid for new signups. Recurring
   * discounts started before this date will continue to recur even after this date.
   */
  endDate?: string;
  productFamilyId?: string;
  /** A stackable coupon can be combined with other coupons on a Subscription. */
  stackable?: boolean;
  /**
   * Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be
   * calculated against the remaining price, after prior discounts have been calculated. For
   * `full-price`, Percentage-based discounts will always be calculated against the original item
   * price, before other discounts are applied.
   */
  compoundingStrategy?: CompoundingStrategy;
  excludeMidPeriodAllocations?: boolean;
  applyOnCancelAtEndOfPeriod?: boolean;
  applyOnSubscriptionExpiration?: boolean;
};

export const couponPayloadSchema: Schema<CouponPayload> = s.object<CouponPayload>({
  name: s.optional(s.string()),
  code: s.optional(s.string()),
  description: s.optional(s.string()),
  percentage: s.optional(s.lazy(() => percentageSchema)),
  amountInCents: s.optional(s.int()),
  allowNegativeBalance: s.optional(s.boolean()),
  recurring: s.optional(s.boolean()),
  endDate: s.optional(s.dateOnly()),
  productFamilyId: s.optional(s.string()),
  stackable: s.optional(s.boolean()),
  compoundingStrategy: s.optional(s.lazy(() => compoundingStrategySchema)),
  excludeMidPeriodAllocations: s.optional(s.boolean()),
  applyOnCancelAtEndOfPeriod: s.optional(s.boolean()),
  applyOnSubscriptionExpiration: s.optional(s.boolean()),
  _keysMap: {
    amountInCents: "amount_in_cents",
    allowNegativeBalance: "allow_negative_balance",
    endDate: "end_date",
    productFamilyId: "product_family_id",
    compoundingStrategy: "compounding_strategy",
    excludeMidPeriodAllocations: "exclude_mid_period_allocations",
    applyOnCancelAtEndOfPeriod: "apply_on_cancel_at_end_of_period",
    applyOnSubscriptionExpiration: "apply_on_subscription_expiration",
  },
});
