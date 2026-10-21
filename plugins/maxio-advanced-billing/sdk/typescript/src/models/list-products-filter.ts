import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  prepaidProductPricePointFilterSchema,
  type PrepaidProductPricePointFilter,
} from "./prepaid-product-price-point-filter.js";

export type ListProductsFilter = {
  /**
   * Allows fetching products with matching id based on provided values. Use in query
   * `filter[ids]=1,2,3`.
   */
  ids?: number[];
  /**
   * Allows fetching products only if a prepaid product price point is present or not. To use this
   * filter you also have to include the following param in the request
   * `include=prepaid_product_price_point`. Use in query
   * `filter[prepaid_product_price_point][product_price_point_id]=not_null`.
   */
  prepaidProductPricePoint?: PrepaidProductPricePointFilter;
  /**
   * Allows fetching products with matching use_site_exchange_rate based on provided value (refers
   * to default price point). Use in query `filter[use_site_exchange_rate]=true`.
   */
  useSiteExchangeRate?: boolean;
};

export const listProductsFilterSchema: Schema<ListProductsFilter> = s.object<ListProductsFilter>({
  ids: s.optional(s.array(s.int())),
  prepaidProductPricePoint: s.optional(s.lazy(() => prepaidProductPricePointFilterSchema)),
  useSiteExchangeRate: s.optional(s.boolean()),
  _keysMap: {
    prepaidProductPricePoint: "prepaid_product_price_point",
    useSiteExchangeRate: "use_site_exchange_rate",
  },
});
