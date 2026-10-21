import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PrepaidProductPricePointFilter = {
  /** Passed as a parameter to list methods to return only non null values. @default "not_null" */
  productPricePointId?: "not_null";
};

export const prepaidProductPricePointFilterSchema: Schema<PrepaidProductPricePointFilter> =
  s.object<PrepaidProductPricePointFilter>({
    productPricePointId: s.defaulted(s.literal("not_null"), "not_null"),
    _keysMap: {
      productPricePointId: "product_price_point_id",
    },
  });
