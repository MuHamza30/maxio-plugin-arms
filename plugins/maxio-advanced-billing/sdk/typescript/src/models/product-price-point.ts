import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { currencyPriceSchema, type CurrencyPrice } from "./currency-price.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { pricePointTypeSchema, type PricePointType } from "./price-point-type.js";
import { trialTypeSchema, type TrialType } from "./trial-type.js";

export type ProductPricePoint = {
  id?: number;
  /** The product price point name */
  name?: string;
  /** The product price point API handle */
  handle?: string | null;
  /** The product price point price, in integer cents */
  priceInCents?: number;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this product price point would renew every 30 days.
   */
  interval?: number;
  /** A string representing the interval unit for this product price point, either month or day */
  intervalUnit?: IntervalUnit;
  /** The product price point trial price, in integer cents */
  trialPriceInCents?: number | null;
  /**
   * The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of
   * day would mean this product price point trial would last 30 days.
   */
  trialInterval?: number | null;
  /**
   * A string representing the trial interval unit for this product price point, either month or day
   */
  trialIntervalUnit?: IntervalUnit | null;
  /**
   * Indicates how a trial is handled when the trial period ends and there is no credit card on
   * file. For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not
   * send any emails or statements. For `payment_expected`, the subscription transitions to a Past
   * Due state. Maxio will send normal dunning emails and statements according to your other
   * settings.
   */
  trialType?: TrialType | null;
  /** reserved for future use */
  introductoryOffer?: boolean | null;
  /** The product price point initial charge, in integer cents */
  initialChargeInCents?: number | null;
  initialChargeAfterTrial?: boolean | null;
  /**
   * The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an
   * expiration_interval_unit of day would mean this product price point would expire after 30 days.
   */
  expirationInterval?: number | null;
  /**
   * A string representing the expiration interval unit for this product price point, either month,
   * day or never
   */
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
  /** The product id this price point belongs to */
  productId?: number;
  /** Timestamp indicating when this price point was archived */
  archivedAt?: Date | null;
  /** Timestamp indicating when this price point was created */
  createdAt?: Date;
  /** Timestamp indicating when this price point was last updated */
  updatedAt?: Date;
  /**
   * Whether or not to use the site's exchange rate or define your own pricing when your site has
   * multiple currencies defined.
   */
  useSiteExchangeRate?: boolean;
  /** The type of price point */
  type?: PricePointType;
  /** Whether or not the price point includes tax */
  taxIncluded?: boolean;
  /** The subscription id this price point belongs to */
  subscriptionId?: number | null;
  /**
   * An array of currency pricing data is available when multiple currencies are defined for the
   * site. It varies based on the use_site_exchange_rate setting for the price point. This parameter
   * is present only in the response of read endpoints, after including the appropriate query
   * parameter.
   */
  currencyPrices?: CurrencyPrice[];
};

export const productPricePointSchema: Schema<ProductPricePoint> = s.object<ProductPricePoint>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  handle: s.optionalNullable(s.string()),
  priceInCents: s.optional(s.int()),
  interval: s.optional(s.int()),
  intervalUnit: s.optional(s.lazy(() => intervalUnitSchema)),
  trialPriceInCents: s.optionalNullable(s.int()),
  trialInterval: s.optionalNullable(s.int()),
  trialIntervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  trialType: s.optionalNullable(s.lazy(() => trialTypeSchema)),
  introductoryOffer: s.optionalNullable(s.boolean()),
  initialChargeInCents: s.optionalNullable(s.int()),
  initialChargeAfterTrial: s.optionalNullable(s.boolean()),
  expirationInterval: s.optionalNullable(s.int()),
  expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
  productId: s.optional(s.int()),
  archivedAt: s.optionalNullable(s.dateTime()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  useSiteExchangeRate: s.optional(s.boolean()),
  type: s.optional(s.lazy(() => pricePointTypeSchema)),
  taxIncluded: s.optional(s.boolean()),
  subscriptionId: s.optionalNullable(s.int()),
  currencyPrices: s.optional(s.array(s.lazy(() => currencyPriceSchema))),
  _keysMap: {
    priceInCents: "price_in_cents",
    intervalUnit: "interval_unit",
    trialPriceInCents: "trial_price_in_cents",
    trialInterval: "trial_interval",
    trialIntervalUnit: "trial_interval_unit",
    trialType: "trial_type",
    introductoryOffer: "introductory_offer",
    initialChargeInCents: "initial_charge_in_cents",
    initialChargeAfterTrial: "initial_charge_after_trial",
    expirationInterval: "expiration_interval",
    expirationIntervalUnit: "expiration_interval_unit",
    productId: "product_id",
    archivedAt: "archived_at",
    createdAt: "created_at",
    updatedAt: "updated_at",
    useSiteExchangeRate: "use_site_exchange_rate",
    taxIncluded: "tax_included",
    subscriptionId: "subscription_id",
    currencyPrices: "currency_prices",
  },
});
