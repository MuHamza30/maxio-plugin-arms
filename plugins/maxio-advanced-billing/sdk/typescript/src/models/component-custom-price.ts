import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

/**
 * Create or update custom pricing unique to the subscription. Used in place of `price_point_id`.
 */
export type ComponentCustomPrice = {
  /** Whether or not the price point includes tax */
  taxIncluded?: boolean;
  /** Omit for On/Off components. */
  pricingScheme?: PricingScheme;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this component price point would renew every 30 days. This property is only available for
   * sites with Multifrequency enabled.
   */
  interval?: number;
  /**
   * A string representing the interval unit for this component price point, either month or day.
   * This property is only available for sites with Multifrequency enabled.
   */
  intervalUnit?: IntervalUnit | null;
  /**
   * (Optional) Id of the price point to use for list price calculations when overriding the
   * customer price.
   */
  listPricePointId?: number | null;
  /**
   * When true, list price calculations will continue to use the default price point even when a
   * `custom_price` is supplied.
   */
  useDefaultListPrice?: boolean;
  /** On/off components only need one price bracket starting at 1. */
  prices: Price[];
  /**
   * Applicable only to prepaid usage components. Controls whether the allocated quantity renews
   * each period.
   */
  renewPrepaidAllocation?: boolean;
  /**
   * Applicable only to prepaid usage components. Controls whether remaining units roll over to the
   * next period.
   */
  rolloverPrepaidRemainder?: boolean;
  /**
   * Applicable only when rollover is enabled. Number of `expiration_interval_unit`s after which
   * rollover amounts expire.
   */
  expirationInterval?: number | null;
  /**
   * Applicable only when rollover is enabled. Interval unit for rollover expiration (month or day).
   */
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
};

export const componentCustomPriceSchema: Schema<ComponentCustomPrice> = s.object<ComponentCustomPrice>({
  taxIncluded: s.optional(s.boolean()),
  pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  listPricePointId: s.optionalNullable(s.int()),
  useDefaultListPrice: s.optional(s.boolean()),
  prices: s.array(s.lazy(() => priceSchema)),
  renewPrepaidAllocation: s.optional(s.boolean()),
  rolloverPrepaidRemainder: s.optional(s.boolean()),
  expirationInterval: s.optionalNullable(s.int()),
  expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
  _keysMap: {
    taxIncluded: "tax_included",
    pricingScheme: "pricing_scheme",
    intervalUnit: "interval_unit",
    listPricePointId: "list_price_point_id",
    useDefaultListPrice: "use_default_list_price",
    renewPrepaidAllocation: "renew_prepaid_allocation",
    rolloverPrepaidRemainder: "rollover_prepaid_remainder",
    expirationInterval: "expiration_interval",
    expirationIntervalUnit: "expiration_interval_unit",
  },
});
