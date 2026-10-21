import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { featureTemplateSchema, type FeatureTemplate } from "./feature-template.js";

export type FeatureTemplatesListResponse = {
  items: FeatureTemplate[];
  /** Total number of feature templates matching the filters, across all pages. */
  totalCount: number;
  /**
   * Number of archived feature templates matching the filters. Returned as `0` unless the active
   * result set is empty or `status=archived` was requested.
   */
  archivedCount: number;
};

export const featureTemplatesListResponseSchema: Schema<FeatureTemplatesListResponse> =
  s.object<FeatureTemplatesListResponse>({
    items: s.array(s.lazy(() => featureTemplateSchema)),
    totalCount: s.int(),
    archivedCount: s.int(),
    _keysMap: {
      totalCount: "total_count",
      archivedCount: "archived_count",
    },
  });
