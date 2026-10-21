import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * (For calendar billing subscriptions only) The way that the resumed subscription's charge should
 * be handled
 */
export const ResumptionCharge = {
  Prorated: "prorated",
  Immediate: "immediate",
  Delayed: "delayed",
} as const;
export type ResumptionCharge = (typeof ResumptionCharge)[keyof typeof ResumptionCharge] | (string & {});

export const resumptionChargeSchema: EnumSchema<ResumptionCharge> =
  s.enumOf<ResumptionCharge>(ResumptionCharge);
