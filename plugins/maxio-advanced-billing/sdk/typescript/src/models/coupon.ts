import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { compoundingStrategySchema, type CompoundingStrategy } from "./compounding-strategy.js";
import { couponCurrencySchema, type CouponCurrency } from "./coupon-currency.js";
import { couponRestrictionSchema, type CouponRestriction } from "./coupon-restriction.js";
import { discountTypeSchema, type DiscountType } from "./discount-type.js";
import { recurringSchemeSchema, type RecurringScheme } from "./recurring-scheme.js";

export type Coupon = {
  id?: number;
  name?: string;
  code?: string;
  description?: string;
  amount?: number | null;
  amountInCents?: number | null;
  productFamilyId?: number;
  productFamilyName?: string | null;
  startDate?: Date;
  /**
   * After the given time, this coupon code will be invalid for new signups. Recurring discounts
   * started before this date will continue to recur even after this date.
   */
  endDate?: Date | null;
  percentage?: string | null;
  recurring?: boolean;
  recurringScheme?: RecurringScheme;
  durationPeriodCount?: number | null;
  durationInterval?: number | null;
  durationIntervalUnit?: string | null;
  durationIntervalSpan?: string | null;
  /** If set to true, discount is not limited (credits will carry forward to next billing). */
  allowNegativeBalance?: boolean;
  archivedAt?: Date | null;
  conversionLimit?: string | null;
  /** A stackable coupon can be combined with other coupons on a Subscription. */
  stackable?: boolean;
  /**
   * Applicable only to stackable coupons. For `compound`, Percentage-based discounts will be
   * calculated against the remaining price, after prior discounts have been calculated. For
   * `full-price`, Percentage-based discounts will always be calculated against the original item
   * price, before other discounts are applied.
   */
  compoundingStrategy?: CompoundingStrategy | null;
  useSiteExchangeRate?: boolean;
  createdAt?: Date;
  updatedAt?: Date;
  discountType?: DiscountType;
  excludeMidPeriodAllocations?: boolean;
  applyOnCancelAtEndOfPeriod?: boolean;
  applyOnSubscriptionExpiration?: boolean;
  couponRestrictions?: CouponRestriction[];
  /** Returned in read, find, and list endpoints if the query parameter is provided. */
  currencyPrices?: CouponCurrency[];
};

export const couponSchema: Schema<Coupon> = s.object<Coupon>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  code: s.optional(s.string()),
  description: s.optional(s.string()),
  amount: s.optionalNullable(s.float64()),
  amountInCents: s.optionalNullable(s.int()),
  productFamilyId: s.optional(s.int()),
  productFamilyName: s.optionalNullable(s.string()),
  startDate: s.optional(s.dateTime()),
  endDate: s.optionalNullable(s.dateTime()),
  percentage: s.optionalNullable(s.string()),
  recurring: s.optional(s.boolean()),
  recurringScheme: s.optional(s.lazy(() => recurringSchemeSchema)),
  durationPeriodCount: s.optionalNullable(s.int()),
  durationInterval: s.optionalNullable(s.int()),
  durationIntervalUnit: s.optionalNullable(s.string()),
  durationIntervalSpan: s.optionalNullable(s.string()),
  allowNegativeBalance: s.optional(s.boolean()),
  archivedAt: s.optionalNullable(s.dateTime()),
  conversionLimit: s.optionalNullable(s.string()),
  stackable: s.optional(s.boolean()),
  compoundingStrategy: s.optionalNullable(s.lazy(() => compoundingStrategySchema)),
  useSiteExchangeRate: s.optional(s.boolean()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  discountType: s.optional(s.lazy(() => discountTypeSchema)),
  excludeMidPeriodAllocations: s.optional(s.boolean()),
  applyOnCancelAtEndOfPeriod: s.optional(s.boolean()),
  applyOnSubscriptionExpiration: s.optional(s.boolean()),
  couponRestrictions: s.optional(s.array(s.lazy(() => couponRestrictionSchema))),
  currencyPrices: s.optional(s.array(s.lazy(() => couponCurrencySchema))),
  _keysMap: {
    amountInCents: "amount_in_cents",
    productFamilyId: "product_family_id",
    productFamilyName: "product_family_name",
    startDate: "start_date",
    endDate: "end_date",
    recurringScheme: "recurring_scheme",
    durationPeriodCount: "duration_period_count",
    durationInterval: "duration_interval",
    durationIntervalUnit: "duration_interval_unit",
    durationIntervalSpan: "duration_interval_span",
    allowNegativeBalance: "allow_negative_balance",
    archivedAt: "archived_at",
    conversionLimit: "conversion_limit",
    compoundingStrategy: "compounding_strategy",
    useSiteExchangeRate: "use_site_exchange_rate",
    createdAt: "created_at",
    updatedAt: "updated_at",
    discountType: "discount_type",
    excludeMidPeriodAllocations: "exclude_mid_period_allocations",
    applyOnCancelAtEndOfPeriod: "apply_on_cancel_at_end_of_period",
    applyOnSubscriptionExpiration: "apply_on_subscription_expiration",
    couponRestrictions: "coupon_restrictions",
    currencyPrices: "currency_prices",
  },
});
