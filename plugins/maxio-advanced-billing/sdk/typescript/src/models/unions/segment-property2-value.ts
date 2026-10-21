import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * A value that will occur in your events that you want to bill upon. The type of the value depends
 * on the property type in the related event based billing metric.
 */
export type SegmentProperty2Value = string | number | boolean;

export const segmentProperty2ValueSchema: Schema<SegmentProperty2Value> = s.of<SegmentProperty2Value>(
  s.union([s.string(), s.float64(), s.int(), s.boolean()]),
);
