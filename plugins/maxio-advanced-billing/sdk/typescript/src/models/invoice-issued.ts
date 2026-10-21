import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceLineItemEventDataSchema,
  type InvoiceLineItemEventData,
} from "./invoice-line-item-event-data.js";

export type InvoiceIssued = {
  uid: string;
  number: string;
  role: string;
  dueDate: string | null;
  /** Invoice issue date. Can be an empty string if value is missing. */
  issueDate: string;
  /** Paid date. Can be an empty string if value is missing. */
  paidDate: string;
  dueAmount: string;
  paidAmount: string;
  taxAmount: string;
  refundAmount: string;
  totalAmount: string;
  statusAmount: string;
  productName: string;
  consolidationLevel: string;
  lineItems: InvoiceLineItemEventData[];
};

export const invoiceIssuedSchema: Schema<InvoiceIssued> = s.object<InvoiceIssued>({
  uid: s.string(),
  number: s.string(),
  role: s.string(),
  dueDate: s.nullable(s.dateOnly()),
  issueDate: s.string(),
  paidDate: s.string(),
  dueAmount: s.string(),
  paidAmount: s.string(),
  taxAmount: s.string(),
  refundAmount: s.string(),
  totalAmount: s.string(),
  statusAmount: s.string(),
  productName: s.string(),
  consolidationLevel: s.string(),
  lineItems: s.array(s.lazy(() => invoiceLineItemEventDataSchema)),
  _keysMap: {
    dueDate: "due_date",
    issueDate: "issue_date",
    paidDate: "paid_date",
    dueAmount: "due_amount",
    paidAmount: "paid_amount",
    taxAmount: "tax_amount",
    refundAmount: "refund_amount",
    totalAmount: "total_amount",
    statusAmount: "status_amount",
    productName: "product_name",
    consolidationLevel: "consolidation_level",
    lineItems: "line_items",
  },
});
