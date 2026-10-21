import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { trialTypeSchema, type TrialType } from "./trial-type.js";

export type CreateProductPricePoint = {
  /** The product price point name */
  name: string;
  /** The product price point API handle */
  handle?: string;
  /** The product price point price, in integer cents */
  priceInCents: number;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this product price point would renew every 30 days.
   */
  interval: number;
  /** A string representing the interval unit for this product price point, either month or day */
  intervalUnit: IntervalUnit;
  /** The product price point trial price, in integer cents */
  trialPriceInCents?: number;
  /**
   * The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of
   * day would mean this product price point trial would last 30 days.
   */
  trialInterval?: number;
  /**
   * A string representing the trial interval unit for this product price point, either month or day
   */
  trialIntervalUnit?: IntervalUnit;
  /**
   * Indicates how a trial is handled when the trial period ends and there is no credit card on
   * file. For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not
   * send any emails or statements. For `payment_expected`, the subscription transitions to a Past
   * Due state. Maxio will send normal dunning emails and statements according to your other
   * settings.
   */
  trialType?: TrialType | null;
  /** The product price point initial charge, in integer cents */
  initialChargeInCents?: number;
  initialChargeAfterTrial?: boolean;
  /**
   * The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an
   * expiration_interval_unit of day would mean this product price point would expire after 30 days.
   */
  expirationInterval?: number;
  /**
   * A string representing the expiration interval unit for this product price point, either month,
   * day or never
   */
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
  /**
   * Whether or not to use the site's exchange rate or define your own pricing when your site has
   * multiple currencies defined.
   *
   * @default true
   */
  useSiteExchangeRate?: boolean;
};

export const createProductPricePointSchema: Schema<CreateProductPricePoint> =
  s.object<CreateProductPricePoint>({
    name: s.string(),
    handle: s.optional(s.string()),
    priceInCents: s.int(),
    interval: s.int(),
    intervalUnit: intervalUnitSchema,
    trialPriceInCents: s.optional(s.int()),
    trialInterval: s.optional(s.int()),
    trialIntervalUnit: s.optional(s.lazy(() => intervalUnitSchema)),
    trialType: s.optionalNullable(s.lazy(() => trialTypeSchema)),
    initialChargeInCents: s.optional(s.int()),
    initialChargeAfterTrial: s.optional(s.boolean()),
    expirationInterval: s.optional(s.int()),
    expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
    useSiteExchangeRate: s.defaulted(s.boolean(), true),
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
      useSiteExchangeRate: "use_site_exchange_rate",
    },
  });
