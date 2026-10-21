import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";
import { priceSchema, type Price } from "./price.js";
import { pricingSchemeSchema, type PricingScheme } from "./pricing-scheme.js";

export type ComponentPricePointItem = {
  name?: string;
  handle?: string;
  /**
   * The identifier for the pricing scheme. See [Product
   * Components](https://help.chargify.com/products/product-components.html) for an overview of
   * pricing schemes.
   */
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
  prices?: Price[];
};

export const componentPricePointItemSchema: Schema<ComponentPricePointItem> =
  s.object<ComponentPricePointItem>({
    name: s.optional(s.string()),
    handle: s.optional(s.string()),
    pricingScheme: s.optional(s.lazy(() => pricingSchemeSchema)),
    interval: s.optional(s.int()),
    intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
    prices: s.optional(s.array(s.lazy(() => priceSchema))),
    _keysMap: {
      pricingScheme: "pricing_scheme",
      intervalUnit: "interval_unit",
    },
  });
