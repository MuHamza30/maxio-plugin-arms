import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The type of entry */
export const ServiceCreditType = {
  Credit: "Credit",
  Debit: "Debit",
} as const;
export type ServiceCreditType = (typeof ServiceCreditType)[keyof typeof ServiceCreditType] | (string & {});

export const serviceCreditTypeSchema: EnumSchema<ServiceCreditType> =
  s.enumOf<ServiceCreditType>(ServiceCreditType);
