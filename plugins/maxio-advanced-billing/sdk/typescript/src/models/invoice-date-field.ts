import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const InvoiceDateField = {
  CreatedAt: "created_at",
  DueDate: "due_date",
  IssueDate: "issue_date",
  UpdatedAt: "updated_at",
  PaidDate: "paid_date",
} as const;
export type InvoiceDateField = (typeof InvoiceDateField)[keyof typeof InvoiceDateField] | (string & {});

export const invoiceDateFieldSchema: EnumSchema<InvoiceDateField> =
  s.enumOf<InvoiceDateField>(InvoiceDateField);
