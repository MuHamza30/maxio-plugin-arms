import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
 * site setting if one is not provided. Values are:
 *
 * `full` - A full price credit is added for the amount owed.
 *
 * `prorated` - A prorated credit is added for the amount owed.
 *
 * `none` - No charge is added.
 */
export const DowngradeCreditCreditType = {
  Full: "full",
  Prorated: "prorated",
  None: "none",
} as const;
export type DowngradeCreditCreditType =
  | (typeof DowngradeCreditCreditType)[keyof typeof DowngradeCreditCreditType]
  | (string & {});

export const downgradeCreditCreditTypeSchema: EnumSchema<DowngradeCreditCreditType> =
  s.enumOf<DowngradeCreditCreditType>(DowngradeCreditCreditType);
