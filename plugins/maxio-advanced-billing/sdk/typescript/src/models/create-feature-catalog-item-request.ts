import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { feature2Schema, type Feature2 } from "./feature2.js";

/**
 * The owning product or component is taken from the URL and must not be included in the request
 * body.
 */
export type CreateFeatureCatalogItemRequest = {
  feature: Feature2;
};

export const createFeatureCatalogItemRequestSchema: Schema<CreateFeatureCatalogItemRequest> =
  s.object<CreateFeatureCatalogItemRequest>({
    feature: feature2Schema,
  });
