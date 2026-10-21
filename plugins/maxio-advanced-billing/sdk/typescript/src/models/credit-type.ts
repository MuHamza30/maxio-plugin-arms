import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
 * site setting if one is not provided.
 */
export const CreditType = {
  Full: "full",
  Prorated: "prorated",
  None: "none",
} as const;
export type CreditType = (typeof CreditType)[keyof typeof CreditType] | (string & {});

export const creditTypeSchema: EnumSchema<CreditType> = s.enumOf<CreditType>(CreditType);
