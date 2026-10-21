import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { segmentSchema, type Segment } from "./segment.js";

export type ListSegmentsResponse = {
  segments?: Segment[];
};

export const listSegmentsResponseSchema: Schema<ListSegmentsResponse> = s.object<ListSegmentsResponse>({
  segments: s.optional(s.array(s.lazy(() => segmentSchema))),
});
