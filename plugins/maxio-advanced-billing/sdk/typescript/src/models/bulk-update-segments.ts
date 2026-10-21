import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { bulkUpdateSegmentsItemSchema, type BulkUpdateSegmentsItem } from "./bulk-update-segments-item.js";

export type BulkUpdateSegments = {
  segments?: BulkUpdateSegmentsItem[];
};

export const bulkUpdateSegmentsSchema: Schema<BulkUpdateSegments> = s.object<BulkUpdateSegments>({
  segments: s.optional(s.array(s.lazy(() => bulkUpdateSegmentsItemSchema))),
});
