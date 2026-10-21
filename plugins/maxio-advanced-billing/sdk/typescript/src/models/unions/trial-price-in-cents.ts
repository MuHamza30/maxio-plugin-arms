import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** (Optional) */
export type TrialPriceInCents = string | number;

export const trialPriceInCentsSchema: Schema<TrialPriceInCents> = s.of<TrialPriceInCents>(
  s.union([s.string(), s.int()]),
);
