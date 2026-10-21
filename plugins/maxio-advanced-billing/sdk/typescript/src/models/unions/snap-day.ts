import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'. */
export type SnapDay = number | string;

export const snapDaySchema: Schema<SnapDay> = s.of<SnapDay>(s.union([s.int(), s.string()]));
