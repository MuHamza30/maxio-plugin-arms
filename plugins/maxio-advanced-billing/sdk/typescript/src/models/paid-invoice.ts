import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceStatusSchema, type InvoiceStatus } from "./invoice-status.js";

export type PaidInvoice = {
  /** The uid of the paid invoice */
  invoiceId?: string;
  /**
   * The current status of the invoice. See [Invoice
   * Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses)
   * for more.
   */
  status?: InvoiceStatus;
  /** The remaining due amount on the invoice */
  dueAmount?: string;
  /** The total amount paid on this invoice (including any prior payments) */
  paidAmount?: string;
};

export const paidInvoiceSchema: Schema<PaidInvoice> = s.object<PaidInvoice>({
  invoiceId: s.optional(s.string()),
  status: s.optional(s.lazy(() => invoiceStatusSchema)),
  dueAmount: s.optional(s.string()),
  paidAmount: s.optional(s.string()),
  _keysMap: {
    invoiceId: "invoice_id",
    dueAmount: "due_amount",
    paidAmount: "paid_amount",
  },
});
