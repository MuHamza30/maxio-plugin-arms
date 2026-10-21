import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** 'proforma' value is deprecated in favor of proforma_adhoc and proforma_automatic. */
export const ProformaInvoiceRole = {
  Unset: "unset",
  Proforma: "proforma",
  ProformaAdhoc: "proforma_adhoc",
  ProformaAutomatic: "proforma_automatic",
} as const;
export type ProformaInvoiceRole =
  | (typeof ProformaInvoiceRole)[keyof typeof ProformaInvoiceRole]
  | (string & {});

export const proformaInvoiceRoleSchema: EnumSchema<ProformaInvoiceRole> =
  s.enumOf<ProformaInvoiceRole>(ProformaInvoiceRole);
