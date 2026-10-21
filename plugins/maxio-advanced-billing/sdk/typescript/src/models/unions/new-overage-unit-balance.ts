import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type NewOverageUnitBalance = number | string;

export const newOverageUnitBalanceSchema: Schema<NewOverageUnitBalance> = s.of<NewOverageUnitBalance>(
  s.union([s.int(), s.string()]),
);
