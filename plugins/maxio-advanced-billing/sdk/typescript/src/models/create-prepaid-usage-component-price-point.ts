import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { expirationIntervalUnitSchema, type ExpirationIntervalUnit } from "./expiration-interval-unit.js";
import { overagePricingSchema, type OveragePricing } from "./overage-pricing.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

export type CreatePrepaidUsageComponentPricePoint = {
  name: string;
  handle?: string;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme: PricingScheme;
  prices: Price[];
  overagePricing: OveragePricing;
  /**
   * Whether to use the site level exchange rate or define your own prices for each currency if you
   * have multiple currencies defined on the site.
   *
   * @default true
   */
  useSiteExchangeRate?: boolean;
  /**
   * (only for prepaid usage components) Boolean which controls whether or not remaining units
   * should be rolled over to the next period.
   */
  rolloverPrepaidRemainder?: boolean;
  /**
   * (only for prepaid usage components) Boolean which controls whether or not the allocated
   * quantity should be renewed at the beginning of each period.
   */
  renewPrepaidAllocation?: boolean;
  /**
   * (only for prepaid usage components where rollover_prepaid_remainder is true) The number of
   * `expiration_interval_unit`s after which rollover amounts should expire.
   */
  expirationInterval?: number;
  /**
   * (only for prepaid usage components where rollover_prepaid_remainder is true) A string
   * representing the expiration interval unit for this component, either month or day.
   */
  expirationIntervalUnit?: ExpirationIntervalUnit | null;
};

export const createPrepaidUsageComponentPricePointSchema: Schema<CreatePrepaidUsageComponentPricePoint> =
  s.object<CreatePrepaidUsageComponentPricePoint>({
    name: s.string(),
    handle: s.optional(s.string()),
    pricingScheme: pricingSchemeSchema,
    prices: s.array(s.lazy(() => priceSchema)),
    overagePricing: overagePricingSchema,
    useSiteExchangeRate: s.defaulted(s.boolean(), true),
    rolloverPrepaidRemainder: s.optional(s.boolean()),
    renewPrepaidAllocation: s.optional(s.boolean()),
    expirationInterval: s.optional(s.float64()),
    expirationIntervalUnit: s.optionalNullable(s.lazy(() => expirationIntervalUnitSchema)),
    _keysMap: {
      pricingScheme: "pricing_scheme",
      overagePricing: "overage_pricing",
      useSiteExchangeRate: "use_site_exchange_rate",
      rolloverPrepaidRemainder: "rollover_prepaid_remainder",
      renewPrepaidAllocation: "renew_prepaid_allocation",
      expirationInterval: "expiration_interval",
      expirationIntervalUnit: "expiration_interval_unit",
    },
  });
