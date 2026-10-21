import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * You may choose how to handle the reactivation charge for that subscription: 1) `prorated` A
 * prorated charge for the product price will be attempted to complete the period 2) `immediate` A
 * full-price charge for the product price will be attempted immediately 3) `delayed` A full-price
 * charge for the product price will be attempted at the next renewal.
 */
export const ReactivationCharge = {
  Prorated: "prorated",
  Immediate: "immediate",
  Delayed: "delayed",
} as const;
export type ReactivationCharge = (typeof ReactivationCharge)[keyof typeof ReactivationCharge] | (string & {});

export const reactivationChargeSchema: EnumSchema<ReactivationCharge> =
  s.enumOf<ReactivationCharge>(ReactivationCharge);
