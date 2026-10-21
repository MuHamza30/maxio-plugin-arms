import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type SegmentProperty1Value1 = string | number | boolean;

export const segmentProperty1Value1Schema: Schema<SegmentProperty1Value1> = s.of<SegmentProperty1Value1>(
  s.union([s.string(), s.float64(), s.int(), s.boolean()]),
);
