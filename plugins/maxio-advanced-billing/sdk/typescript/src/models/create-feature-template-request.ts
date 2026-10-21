import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { featureSchema, type Feature } from "./feature.js";

export type CreateFeatureTemplateRequest = {
  feature: Feature;
};

export const createFeatureTemplateRequestSchema: Schema<CreateFeatureTemplateRequest> =
  s.object<CreateFeatureTemplateRequest>({
    feature: featureSchema,
  });
