import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { trialTypeSchema, type TrialType } from "./trial-type.js";
import { expirationIntervalSchema, type ExpirationInterval } from "./unions/expiration-interval.js";
import { initialChargeInCentsSchema, type InitialChargeInCents } from "./unions/initial-charge-in-cents.js";
import { intervalSchema, type Interval } from "./unions/interval.js";
import { priceInCentsSchema, type PriceInCents } from "./unions/price-in-cents.js";
import { trialIntervalSchema, type TrialInterval } from "./unions/trial-interval.js";
import { trialPriceInCentsSchema, type TrialPriceInCents } from "./unions/trial-price-in-cents.js";

/**
 * (Optional) Used in place of `product_price_point_id` to define a custom price point unique to the
 * subscription. A subscription can have up to 30 custom price points. Exceeding this limit will
 * result in an API error.
 */
export type SubscriptionCustomPrice = {
  /** (Optional) */
  name?: string;
  /** (Optional) */
  handle?: string;
  /** Required if using `custom_price` attribute. */
  priceInCents: PriceInCents;
  /** Required if using `custom_price` attribute. */
  interval: Interval;
  /** Required if using `custom_price` attribute. */
  intervalUnit: IntervalUnit | null;
  /** (Optional) */
  trialPriceInCents?: TrialPriceInCents;
  /** (Optional) */
  trialInterval?: TrialInterval;
  /** (Optional) */
  trialIntervalUnit?: IntervalUnit;
  /**
   * Indicates how a trial is handled when the trial period ends and there is no credit card on
   * file. For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not
   * send any emails or statements. For `payment_expected`, the subscription transitions to a Past
   * Due state. Maxio will send normal dunning emails and statements according to your other
   * settings.
   */
  trialType?: TrialType | null;
  /** (Optional) */
  initialChargeInCents?: InitialChargeInCents;
  /** (Optional) */
  initialChargeAfterTrial?: boolean;
  /** (Optional) */
  expirationInterval?: ExpirationInterval;
  /** (Optional) */
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
  /** (Optional) */
  taxIncluded?: boolean;
};

export const subscriptionCustomPriceSchema: Schema<SubscriptionCustomPrice> =
  s.object<SubscriptionCustomPrice>({
    name: s.optional(s.string()),
    handle: s.optional(s.string()),
    priceInCents: priceInCentsSchema,
    interval: intervalSchema,
    intervalUnit: s.nullable(s.lazy(() => intervalUnitSchema)),
    trialPriceInCents: s.optional(s.lazy(() => trialPriceInCentsSchema)),
    trialInterval: s.optional(s.lazy(() => trialIntervalSchema)),
    trialIntervalUnit: s.optional(s.lazy(() => intervalUnitSchema)),
    trialType: s.optionalNullable(s.lazy(() => trialTypeSchema)),
    initialChargeInCents: s.optional(s.lazy(() => initialChargeInCentsSchema)),
    initialChargeAfterTrial: s.optional(s.boolean()),
    expirationInterval: s.optional(s.lazy(() => expirationIntervalSchema)),
    expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
    taxIncluded: s.optional(s.boolean()),
    _keysMap: {
      priceInCents: "price_in_cents",
      intervalUnit: "interval_unit",
      trialPriceInCents: "trial_price_in_cents",
      trialInterval: "trial_interval",
      trialIntervalUnit: "trial_interval_unit",
      trialType: "trial_type",
      initialChargeInCents: "initial_charge_in_cents",
      initialChargeAfterTrial: "initial_charge_after_trial",
      expirationInterval: "expiration_interval",
      expirationIntervalUnit: "expiration_interval_unit",
      taxIncluded: "tax_included",
    },
  });
