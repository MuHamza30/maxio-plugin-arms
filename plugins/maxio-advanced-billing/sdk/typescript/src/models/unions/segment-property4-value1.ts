import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type SegmentProperty4Value1 = string | number | boolean;

export const segmentProperty4Value1Schema: Schema<SegmentProperty4Value1> = s.of<SegmentProperty4Value1>(
  s.union([s.string(), s.float64(), s.int(), s.boolean()]),
);
