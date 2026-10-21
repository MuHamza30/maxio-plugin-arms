import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'. */
export type SnapDay1 = string | number;

export const snapDay1Schema: Schema<SnapDay1> = s.of<SnapDay1>(s.union([s.string(), s.int()]));
