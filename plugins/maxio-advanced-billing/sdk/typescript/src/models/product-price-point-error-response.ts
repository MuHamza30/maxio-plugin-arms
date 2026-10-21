import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { productPricePointErrorsSchema, type ProductPricePointErrors } from "./product-price-point-errors.js";

export type ProductPricePointErrorResponse = {
  errors: ProductPricePointErrors;
};

export const productPricePointErrorResponseSchema: Schema<ProductPricePointErrorResponse> =
  s.object<ProductPricePointErrorResponse>({
    errors: productPricePointErrorsSchema,
  });
