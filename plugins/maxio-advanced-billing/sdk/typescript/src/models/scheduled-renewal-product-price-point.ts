import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { intervalSchema, type Interval } from "./unions/interval.js";
import { priceInCentsSchema, type PriceInCents } from "./unions/price-in-cents.js";

/** Custom pricing for a product within a scheduled renewal. */
export type ScheduledRenewalProductPricePoint = {
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
  taxIncluded?: boolean;
  /** The product price point initial charge, in integer cents. */
  initialChargeInCents?: number;
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
};

export const scheduledRenewalProductPricePointSchema: Schema<ScheduledRenewalProductPricePoint> =
  s.object<ScheduledRenewalProductPricePoint>({
    name: s.optional(s.string()),
    handle: s.optional(s.string()),
    priceInCents: priceInCentsSchema,
    interval: intervalSchema,
    intervalUnit: s.nullable(s.lazy(() => intervalUnitSchema)),
    taxIncluded: s.optional(s.boolean()),
    initialChargeInCents: s.optional(s.int()),
    expirationInterval: s.optional(s.int()),
    expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
    _keysMap: {
      priceInCents: "price_in_cents",
      intervalUnit: "interval_unit",
      taxIncluded: "tax_included",
      initialChargeInCents: "initial_charge_in_cents",
      expirationInterval: "expiration_interval",
      expirationIntervalUnit: "expiration_interval_unit",
    },
  });
