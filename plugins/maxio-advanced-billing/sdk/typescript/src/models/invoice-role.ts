import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const InvoiceRole = {
  Unset: "unset",
  Signup: "signup",
  Renewal: "renewal",
  Usage: "usage",
  Reactivation: "reactivation",
  Proration: "proration",
  Migration: "migration",
  Adhoc: "adhoc",
  Backport: "backport",
  BackportBalanceReconciliation: "backport-balance-reconciliation",
} as const;
export type InvoiceRole = (typeof InvoiceRole)[keyof typeof InvoiceRole] | (string & {});

export const invoiceRoleSchema: EnumSchema<InvoiceRole> = s.enumOf<InvoiceRole>(InvoiceRole);
