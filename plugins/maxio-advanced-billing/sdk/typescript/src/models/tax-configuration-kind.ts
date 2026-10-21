import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const TaxConfigurationKind = {
  Custom: "custom",
  ManagedAvalara: "managed avalara",
  LinkedAvalara: "linked avalara",
  DigitalRiver: "digital river",
} as const;
export type TaxConfigurationKind =
  | (typeof TaxConfigurationKind)[keyof typeof TaxConfigurationKind]
  | (string & {});

export const taxConfigurationKindSchema: EnumSchema<TaxConfigurationKind> =
  s.enumOf<TaxConfigurationKind>(TaxConfigurationKind);
