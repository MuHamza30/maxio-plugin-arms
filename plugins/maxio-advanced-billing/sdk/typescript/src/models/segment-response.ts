import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { segmentSchema, type Segment } from "./segment.js";

export type SegmentResponse = {
  segment?: Segment;
};

export const segmentResponseSchema: Schema<SegmentResponse> = s.object<SegmentResponse>({
  segment: s.optional(s.lazy(() => segmentSchema)),
});
