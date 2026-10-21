import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CouponUsage = {
  /** The Chargify id of the product */
  id?: number;
  /** Name of the product */
  name?: string;
  /** Number of times the coupon has been applied */
  signups?: number;
  /** Dollar amount of customer savings as a result of the coupon. */
  savings?: number | null;
  /** Dollar amount of customer savings as a result of the coupon. */
  savingsInCents?: number | null;
  /** Total revenue of all subscriptions that have received a discount from this coupon. */
  revenue?: number | null;
  /** Total revenue of all subscriptions that have received a discount from this coupon. */
  revenueInCents?: number;
};

export const couponUsageSchema: Schema<CouponUsage> = s.object<CouponUsage>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  signups: s.optional(s.int()),
  savings: s.optionalNullable(s.int()),
  savingsInCents: s.optionalNullable(s.int()),
  revenue: s.optionalNullable(s.int()),
  revenueInCents: s.optional(s.int()),
  _keysMap: {
    savingsInCents: "savings_in_cents",
    revenueInCents: "revenue_in_cents",
  },
});
