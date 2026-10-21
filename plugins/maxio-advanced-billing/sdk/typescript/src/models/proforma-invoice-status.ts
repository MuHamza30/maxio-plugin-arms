import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ProformaInvoiceStatus = {
  Draft: "draft",
  Voided: "voided",
  Archived: "archived",
} as const;
export type ProformaInvoiceStatus =
  | (typeof ProformaInvoiceStatus)[keyof typeof ProformaInvoiceStatus]
  | (string & {});

export const proformaInvoiceStatusSchema: EnumSchema<ProformaInvoiceStatus> =
  s.enumOf<ProformaInvoiceStatus>(ProformaInvoiceStatus);
