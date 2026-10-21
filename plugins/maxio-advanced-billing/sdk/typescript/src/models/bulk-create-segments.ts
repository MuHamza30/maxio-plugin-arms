import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createSegmentSchema, type CreateSegment } from "./create-segment.js";

export type BulkCreateSegments = {
  segments?: CreateSegment[];
};

export const bulkCreateSegmentsSchema: Schema<BulkCreateSegments> = s.object<BulkCreateSegments>({
  segments: s.optional(s.array(s.lazy(() => createSegmentSchema))),
});
