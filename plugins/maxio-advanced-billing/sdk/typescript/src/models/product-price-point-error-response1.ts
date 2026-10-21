import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { productPricePointErrorsSchema, type ProductPricePointErrors } from "./product-price-point-errors.js";

export type ProductPricePointErrorResponse1 = {
  errors: ProductPricePointErrors;
};

export const productPricePointErrorResponse1Schema: Schema<ProductPricePointErrorResponse1> =
  s.object<ProductPricePointErrorResponse1>({
    errors: productPricePointErrorsSchema,
  });
