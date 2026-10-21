import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

export type CreateComponentPricePoint = {
  name: string;
  handle?: string;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme: PricingScheme;
  prices: Price[];
  /**
   * Whether to use the site level exchange rate or define your own prices for each currency if you
   * have multiple currencies defined on the site. Setting not supported when creating price points
   * in bulk.
   *
   * @default true
   */
  useSiteExchangeRate?: boolean;
  /**
   * Whether or not the price point includes tax. Setting not supported when creating price points
   * in bulk.
   */
  taxIncluded?: boolean;
  /**
   * The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would
   * mean this price point would renew every 30 days. This property is only available for sites with
   * Multifrequency enabled.
   */
  interval?: number;
  /**
   * A string representing the interval unit for this price point, either month or day. This
   * property is only available for sites with Multifrequency enabled.
   */
  intervalUnit?: IntervalUnit | null;
};

export const createComponentPricePointSchema: Schema<CreateComponentPricePoint> =
  s.object<CreateComponentPricePoint>({
    name: s.string(),
    handle: s.optional(s.string()),
    pricingScheme: pricingSchemeSchema,
    prices: s.array(s.lazy(() => priceSchema)),
    useSiteExchangeRate: s.defaulted(s.boolean(), true),
    taxIncluded: s.optional(s.boolean()),
    interval: s.optional(s.int()),
    intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
    _keysMap: {
      pricingScheme: "pricing_scheme",
      useSiteExchangeRate: "use_site_exchange_rate",
      taxIncluded: "tax_included",
      intervalUnit: "interval_unit",
    },
  });
