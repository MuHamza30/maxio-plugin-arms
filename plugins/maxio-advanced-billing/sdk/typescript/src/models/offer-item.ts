import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { currencyPriceSchema, type CurrencyPrice } from "./currency-price.js";
import { intervalUnitSchema, type IntervalUnit } from "./interval-unit.js";

export type OfferItem = {
  componentId?: number;
  pricePointId?: number;
  startingQuantity?: string;
  editable?: boolean;
  componentUnitPrice?: string;
  componentName?: string;
  pricePointName?: string;
  currencyPrices?: CurrencyPrice[];
  /**
   * The numerical interval. e.g., an interval of '30' coupled with an interval_unit of day would
   * mean this component price point would renew every 30 days. This property is only available for
   * sites with Multifrequency enabled.
   */
  interval?: number;
  /**
   * A string representing the interval unit for this component price point, either month or day.
   * This property is only available for sites with Multifrequency enabled.
   */
  intervalUnit?: IntervalUnit | null;
};

export const offerItemSchema: Schema<OfferItem> = s.object<OfferItem>({
  componentId: s.optional(s.int()),
  pricePointId: s.optional(s.int()),
  startingQuantity: s.optional(s.string()),
  editable: s.optional(s.boolean()),
  componentUnitPrice: s.optional(s.string()),
  componentName: s.optional(s.string()),
  pricePointName: s.optional(s.string()),
  currencyPrices: s.optional(s.array(s.lazy(() => currencyPriceSchema))),
  interval: s.optional(s.int()),
  intervalUnit: s.optionalNullable(s.lazy(() => intervalUnitSchema)),
  _keysMap: {
    componentId: "component_id",
    pricePointId: "price_point_id",
    startingQuantity: "starting_quantity",
    componentUnitPrice: "component_unit_price",
    componentName: "component_name",
    pricePointName: "price_point_name",
    currencyPrices: "currency_prices",
    intervalUnit: "interval_unit",
  },
});
