import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createOrUpdateProductSchema, type CreateOrUpdateProduct } from "./create-or-update-product.js";

export type CreateOrUpdateProductRequest = {
  product: CreateOrUpdateProduct;
};

export const createOrUpdateProductRequestSchema: Schema<CreateOrUpdateProductRequest> =
  s.object<CreateOrUpdateProductRequest>({
    product: createOrUpdateProductSchema,
  });
