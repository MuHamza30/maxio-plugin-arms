import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type SegmentProperty3Value1 = string | number | boolean;

export const segmentProperty3Value1Schema: Schema<SegmentProperty3Value1> = s.of<SegmentProperty3Value1>(
  s.union([s.string(), s.float64(), s.int(), s.boolean()]),
);
