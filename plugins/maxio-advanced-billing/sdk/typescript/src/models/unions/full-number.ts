import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type FullNumber = string | number;

export const fullNumberSchema: Schema<FullNumber> = s.of<FullNumber>(s.union([s.string(), s.int()]));
