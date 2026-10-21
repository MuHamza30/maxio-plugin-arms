import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateSegmentSchema, type UpdateSegment } from "./update-segment.js";

export type UpdateSegmentRequest = {
  segment: UpdateSegment;
};

export const updateSegmentRequestSchema: Schema<UpdateSegmentRequest> = s.object<UpdateSegmentRequest>({
  segment: updateSegmentSchema,
});
