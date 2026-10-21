import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type NewUnitBalance = number | string;

export const newUnitBalanceSchema: Schema<NewUnitBalance> = s.of<NewUnitBalance>(
  s.union([s.int(), s.string()]),
);
