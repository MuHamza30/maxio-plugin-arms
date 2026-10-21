import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createSegmentSchema, type CreateSegment } from "./create-segment.js";

export type CreateSegmentRequest = {
  segment: CreateSegment;
};

export const createSegmentRequestSchema: Schema<CreateSegmentRequest> = s.object<CreateSegmentRequest>({
  segment: createSegmentSchema,
});
