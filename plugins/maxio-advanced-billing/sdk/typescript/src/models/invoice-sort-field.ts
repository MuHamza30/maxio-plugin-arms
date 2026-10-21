import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const InvoiceSortField = {
  Status: "status",
  TotalAmount: "total_amount",
  DueAmount: "due_amount",
  CreatedAt: "created_at",
  UpdatedAt: "updated_at",
  IssueDate: "issue_date",
  DueDate: "due_date",
  Number: "number",
} as const;
export type InvoiceSortField = (typeof InvoiceSortField)[keyof typeof InvoiceSortField] | (string & {});

export const invoiceSortFieldSchema: EnumSchema<InvoiceSortField> =
  s.enumOf<InvoiceSortField>(InvoiceSortField);
