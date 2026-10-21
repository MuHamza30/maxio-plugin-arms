import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Required if using `custom_price` attribute. */
export type Interval = string | number;

export const intervalSchema: Schema<Interval> = s.of<Interval>(s.union([s.string(), s.int()]));
