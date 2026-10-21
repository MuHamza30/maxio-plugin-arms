import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** (Optional) */
export type InitialChargeInCents = string | number;

export const initialChargeInCentsSchema: Schema<InitialChargeInCents> = s.of<InitialChargeInCents>(
  s.union([s.string(), s.int()]),
);
