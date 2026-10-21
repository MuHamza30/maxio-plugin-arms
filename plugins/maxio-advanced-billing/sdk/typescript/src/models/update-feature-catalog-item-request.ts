import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { feature3Schema, type Feature3 } from "./feature3.js";

export type UpdateFeatureCatalogItemRequest = {
  feature: Feature3;
};

export const updateFeatureCatalogItemRequestSchema: Schema<UpdateFeatureCatalogItemRequest> =
  s.object<UpdateFeatureCatalogItemRequest>({
    feature: feature3Schema,
  });
