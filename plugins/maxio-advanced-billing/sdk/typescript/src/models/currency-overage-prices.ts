import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentCurrencyPriceSchema, type ComponentCurrencyPrice } from "./component-currency-price.js";
import { componentPriceSchema, type ComponentPrice } from "./component-price.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { pricePointTypeSchema, type PricePointType } from "./price-point-type.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

/** Extends a component price point with currency overage prices. */
export type CurrencyOveragePrices = {
  id?: number;
  /**
   * Price point type. We expose the following types:
   * 1. **default**: a price point that is marked as a default price for a certain product.
   * 2. **custom**: a custom price point.
   * 3. **catalog**: a price point that is **not** marked as a default price for a certain product
   *    and is **not** a custom one.
   */
  type?: PricePointType;
  /**
   * Note: Refer to type attribute instead.
   *
   * @deprecated
   */
  default?: boolean;
  name?: string;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme?: PricingScheme;
  componentId?: number;
  handle?: string | null;
  archivedAt?: Date | null;
  createdAt?: Date;
  updatedAt?: Date;
  prices?: ComponentPrice[];
  /**
   * Whether to use the site level exchange rate or define your own prices for each currency if you
   * have multiple currencies defined on the site. Defaults to true during creation.
   */
  useSiteExchangeRate?: boolean;
  /**
   * (only used for Custom Pricing - ie. when the price point's type is `custom`) The id of the
   * subscription that the custom price point is for.
   */
  subscriptionId?: number;
  taxIncluded?: boolean;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this component price point would renew every 30 days. This property is only available for
   * sites with Multifrequency enabled.
   */
  interval?: number | null;
  /**
   * A string representing the interval unit for this component price point, either month or day.
   * This property is only available for sites with Multifrequency enabled.
   */
  intervalUnit?: IntervalUnit | null;
  /**
   * An array of currency pricing data is available when multiple currencies are defined for the
   * site. It varies based on the use_site_exchange_rate setting for the price point. This parameter
   * is present only in the response of read endpoints, after including the appropriate query
   * parameter. The clone endpoint always returns currency prices if they are present.
   */
  currencyPrices?: ComponentCurrencyPrice[];
  /** Applicable only to prepaid usage components. An array of overage price brackets. */
  overagePrices?: ComponentPrice[];
  /** Applicable only to prepaid usage components. Pricing scheme for overage pricing. */
  overagePricingScheme?: PricingScheme;
  /**
   * Applicable only to prepaid usage components. Boolean which controls whether or not the
   * allocated quantity should be renewed at the beginning of each period.
   */
  renewPrepaidAllocation?: boolean;
  /**
   * Applicable only to prepaid usage components. Boolean which controls whether or not remaining
   * units should be rolled over to the next period.
   */
  rolloverPrepaidRemainder?: boolean;
  /**
   * Applicable only to prepaid usage components where rollover_prepaid_remainder is true. The
   * number of `expiration_interval_unit`s after which rollover amounts should expire.
   */
  expirationInterval?: number | null;
  /**
   * Applicable only to prepaid usage components where rollover_prepaid_remainder is true. A string
   * representing the expiration interval unit for this component, either month or day.
   */
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
  /**
   * Applicable only to prepaid usage components. An array of currency pricing data for overage
   * prices.
   */
  currencyOveragePrices?: ComponentCurrencyPrice[];
};

export const currencyOveragePricesSchema: Schema<CurrencyOveragePrices> = s.object<CurrencyOveragePrices>({
  id: s.optional(s.int()),
  type: s.optional(s.lazy(() => pricePointTypeSchema)),
  default: s.optional(s.boolean()),
  name: s.optional(s.string()),
  pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
  componentId: s.optional(s.int()),
  handle: s.optionalNullable(s.string()),
  archivedAt: s.optionalNullable(s.dateTime()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  prices: s.optional(s.array(s.lazy(() => componentPriceSchema))),
  useSiteExchangeRate: s.optional(s.boolean()),
  subscriptionId: s.optional(s.int()),
  taxIncluded: s.optional(s.boolean()),
  interval: s.optionalNullable(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  currencyPrices: s.optional(s.array(s.lazy(() => componentCurrencyPriceSchema))),
  overagePrices: s.optional(s.array(s.lazy(() => componentPriceSchema))),
  overagePricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
  renewPrepaidAllocation: s.optional(s.boolean()),
  rolloverPrepaidRemainder: s.optional(s.boolean()),
  expirationInterval: s.optionalNullable(s.int()),
  expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
  currencyOveragePrices: s.optional(s.array(s.lazy(() => componentCurrencyPriceSchema))),
  _keysMap: {
    pricingScheme: "pricing_scheme",
    componentId: "component_id",
    archivedAt: "archived_at",
    createdAt: "created_at",
    updatedAt: "updated_at",
    useSiteExchangeRate: "use_site_exchange_rate",
    subscriptionId: "subscription_id",
    taxIncluded: "tax_included",
    intervalUnit: "interval_unit",
    currencyPrices: "currency_prices",
    overagePrices: "overage_prices",
    overagePricingScheme: "overage_pricing_scheme",
    renewPrepaidAllocation: "renew_prepaid_allocation",
    rolloverPrepaidRemainder: "rollover_prepaid_remainder",
    expirationInterval: "expiration_interval",
    expirationIntervalUnit: "expiration_interval_unit",
    currencyOveragePrices: "currency_overage_prices",
  },
});
