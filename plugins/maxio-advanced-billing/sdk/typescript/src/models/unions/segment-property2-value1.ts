import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type SegmentProperty2Value1 = string | number | boolean;

export const segmentProperty2Value1Schema: Schema<SegmentProperty2Value1> = s.of<SegmentProperty2Value1>(
  s.union([s.string(), s.float64(), s.int(), s.boolean()]),
);
