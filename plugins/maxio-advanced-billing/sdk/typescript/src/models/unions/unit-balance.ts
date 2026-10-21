import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type UnitBalance = string | number;

export const unitBalanceSchema: Schema<UnitBalance> = s.of<UnitBalance>(s.union([s.string(), s.int()]));
