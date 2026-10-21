import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The type of credit to be created when upgrading/downgrading. Defaults to the component and then
 * site setting if one is not provided. Values are:
 *
 * `full` - A charge is added for the full price of the component.
 *
 * `prorated` - A charge is added for the prorated price of the component change.
 *
 * `none` - No charge is added.
 */
export const UpgradeChargeCreditType = {
  Full: "full",
  Prorated: "prorated",
  None: "none",
} as const;
export type UpgradeChargeCreditType =
  | (typeof UpgradeChargeCreditType)[keyof typeof UpgradeChargeCreditType]
  | (string & {});

export const upgradeChargeCreditTypeSchema: EnumSchema<UpgradeChargeCreditType> =
  s.enumOf<UpgradeChargeCreditType>(UpgradeChargeCreditType);
