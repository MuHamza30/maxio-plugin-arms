import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { feature1Schema, type Feature1 } from "./feature1.js";

export type UpdateFeatureTemplateRequest = {
  /**
   * `key` cannot be changed once set. `kind` cannot be changed once any feature catalog item has
   * been created from this template.
   */
  feature: Feature1;
};

export const updateFeatureTemplateRequestSchema: Schema<UpdateFeatureTemplateRequest> =
  s.object<UpdateFeatureTemplateRequest>({
    feature: feature1Schema,
  });
