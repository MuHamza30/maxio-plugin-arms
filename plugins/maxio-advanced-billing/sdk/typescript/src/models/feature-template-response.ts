import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { featureTemplateSchema, type FeatureTemplate } from "./feature-template.js";

export type FeatureTemplateResponse = {
  /**
   * A feature that can be granted to subscribers, defined once at the site level and then attached
   * to products or components.
   */
  feature: FeatureTemplate;
};

export const featureTemplateResponseSchema: Schema<FeatureTemplateResponse> =
  s.object<FeatureTemplateResponse>({
    feature: featureTemplateSchema,
  });
