import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { productFamilySchema, type ProductFamily } from "./product-family.js";

export type ProductFamilyResponse = {
  productFamily?: ProductFamily;
};

export const productFamilyResponseSchema: Schema<ProductFamilyResponse> = s.object<ProductFamilyResponse>({
  productFamily: s.optional(s.lazy(() => productFamilySchema)),
  _keysMap: {
    productFamily: "product_family",
  },
});
