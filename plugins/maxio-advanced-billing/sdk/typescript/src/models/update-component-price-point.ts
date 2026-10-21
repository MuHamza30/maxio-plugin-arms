import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";
import { updatePriceSchema, type UpdatePrice } from "./update-price.js";

export type UpdateComponentPricePoint = {
  name?: string;
  handle?: string;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
  pricingScheme?: PricingScheme;
  /**
   * Whether to use the site level exchange rate or define your own prices for each currency if you
   * have multiple currencies defined on the site.
   */
  useSiteExchangeRate?: boolean;
  /** Whether or not the price point includes tax */
  taxIncluded?: boolean;
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
  prices?: UpdatePrice[];
};

export const updateComponentPricePointSchema: Schema<UpdateComponentPricePoint> =
  s.object<UpdateComponentPricePoint>({
    name: s.optional(s.string()),
    handle: s.optional(s.string()),
    pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
    useSiteExchangeRate: s.optional(s.boolean()),
    taxIncluded: s.optional(s.boolean()),
    interval: s.optional(s.int()),
    intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
    prices: s.optional(s.array(s.lazy(() => updatePriceSchema))),
    _keysMap: {
      pricingScheme: "pricing_scheme",
      useSiteExchangeRate: "use_site_exchange_rate",
      taxIncluded: "tax_included",
      intervalUnit: "interval_unit",
    },
  });
