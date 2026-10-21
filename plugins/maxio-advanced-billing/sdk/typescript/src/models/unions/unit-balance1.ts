import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type UnitBalance1 = number | string;

export const unitBalance1Schema: Schema<UnitBalance1> = s.of<UnitBalance1>(s.union([s.int(), s.string()]));
