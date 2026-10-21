import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { trialTypeSchema, type TrialType } from "./trial-type.js";

export type CreateOrUpdateProduct = {
  /** The product name */
  name: string;
  /** The product API handle */
  handle?: string;
  /** The product description */
  description: string;
  /** E.g. Internal ID or SKU Number */
  accountingCode?: string;
  /**
   * Deprecated value that can be ignored unless you have legacy hosted pages. For Public Signup
   * Page users, read this attribute from under the signup page.
   */
  requireCreditCard?: boolean;
  /** The product price, in integer cents */
  priceInCents: number;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this product would renew every 30 days.
   */
  interval: number;
  /** A string representing the interval unit for this product, either month or day */
  intervalUnit: IntervalUnit;
  /** The product trial price, in integer cents */
  trialPriceInCents?: number;
  /**
   * The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of
   * day would mean this product trial would last 30 days.
   */
  trialInterval?: number;
  /** A string representing the trial interval unit for this product, either month or day */
  trialIntervalUnit?: IntervalUnit | null;
  /**
   * Indicates how a trial is handled when the trial period ends and there is no credit card on
   * file. For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not
   * send any emails or statements. For `payment_expected`, the subscription transitions to a Past
   * Due state. Maxio will send normal dunning emails and statements according to your other
   * settings.
   */
  trialType?: TrialType | null;
  /**
   * The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an
   * expiration_interval_unit of day would mean this product would expire after 30 days.
   */
  expirationInterval?: number;
  /**
   * A string representing the expiration interval unit for this product, either month, day or never
   */
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
  autoCreateSignupPage?: boolean;
  /**
   * A string representing the tax code related to the product type. This is especially important
   * when using AvaTax to tax based on locale. This attribute has a max length of 25 characters.
   */
  taxCode?: string;
  /**
   * (Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is
   * sent as the commodity code on invoice line items for this product instead of the default
   * derived from item_category.
   */
  unspscCode?: string | null;
};

export const createOrUpdateProductSchema: Schema<CreateOrUpdateProduct> = s.object<CreateOrUpdateProduct>({
  name: s.string(),
  handle: s.optional(s.string()),
  description: s.string(),
  accountingCode: s.optional(s.string()),
  requireCreditCard: s.optional(s.boolean()),
  priceInCents: s.int(),
  interval: s.int(),
  intervalUnit: intervalUnitSchema,
  trialPriceInCents: s.optional(s.int()),
  trialInterval: s.optional(s.int()),
  trialIntervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  trialType: s.optionalNullable(s.lazy(() => trialTypeSchema)),
  expirationInterval: s.optional(s.int()),
  expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
  autoCreateSignupPage: s.optional(s.boolean()),
  taxCode: s.optional(s.string()),
  unspscCode: s.optionalNullable(s.string()),
  _keysMap: {
    accountingCode: "accounting_code",
    requireCreditCard: "require_credit_card",
    priceInCents: "price_in_cents",
    intervalUnit: "interval_unit",
    trialPriceInCents: "trial_price_in_cents",
    trialInterval: "trial_interval",
    trialIntervalUnit: "trial_interval_unit",
    trialType: "trial_type",
    expirationInterval: "expiration_interval",
    expirationIntervalUnit: "expiration_interval_unit",
    autoCreateSignupPage: "auto_create_signup_page",
    taxCode: "tax_code",
    unspscCode: "unspsc_code",
  },
});
