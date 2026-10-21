import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * An array of segment uids to refund or the string 'all' to indicate that all segments should be
 * refunded
 */
export type SegmentUids = string[] | string;

export const segmentUidsSchema: Schema<SegmentUids> = s.of<SegmentUids>(
  s.union([s.array(s.string()), s.string()]),
);
