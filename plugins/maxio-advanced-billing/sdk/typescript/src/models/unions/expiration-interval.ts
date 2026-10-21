import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** (Optional) */
export type ExpirationInterval = string | number;

export const expirationIntervalSchema: Schema<ExpirationInterval> = s.of<ExpirationInterval>(
  s.union([s.string(), s.int()]),
);
