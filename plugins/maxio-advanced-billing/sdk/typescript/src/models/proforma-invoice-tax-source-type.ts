import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ProformaInvoiceTaxSourceType = {
  Tax: "Tax",
  Avalara: "Avalara",
} as const;
export type ProformaInvoiceTaxSourceType =
  | (typeof ProformaInvoiceTaxSourceType)[keyof typeof ProformaInvoiceTaxSourceType]
  | (string & {});

export const proformaInvoiceTaxSourceTypeSchema: EnumSchema<ProformaInvoiceTaxSourceType> =
  s.enumOf<ProformaInvoiceTaxSourceType>(ProformaInvoiceTaxSourceType);
