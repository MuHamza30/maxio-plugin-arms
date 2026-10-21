import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createProductFamilySchema, type CreateProductFamily } from "./create-product-family.js";

export type CreateProductFamilyRequest = {
  productFamily: CreateProductFamily;
};

export const createProductFamilyRequestSchema: Schema<CreateProductFamilyRequest> =
  s.object<CreateProductFamilyRequest>({
    productFamily: createProductFamilySchema,
    _keysMap: {
      productFamily: "product_family",
    },
  });
