import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { productSchema, type Product } from "./product.js";

export type ProductResponse = {
  product: Product;
};

export const productResponseSchema: Schema<ProductResponse> = s.object<ProductResponse>({
  product: productSchema,
});
