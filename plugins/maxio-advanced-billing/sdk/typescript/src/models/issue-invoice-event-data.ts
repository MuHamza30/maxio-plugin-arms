import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoiceConsolidationLevelSchema,
  type InvoiceConsolidationLevel,
} from "./invoice-consolidation-level.js";
import { invoiceStatusSchema, type InvoiceStatus } from "./invoice-status.js";

/** Example schema for an `issue_invoice` event */
export type IssueInvoiceEventData = {
  /**
   * Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold
   * one of the following values:
   *
   * * "none": A normal invoice with no consolidation.
   * * "child": An invoice segment which has been combined into a consolidated invoice.
   * * "parent": A consolidated invoice, whose contents are composed of invoice segments.
   *
   * "Parent" invoices do not have lines of their own, but they have subtotals and totals which
   * aggregate the member invoice segments.
   *
   * See also the [invoice consolidation
   * documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation).
   */
  consolidationLevel: InvoiceConsolidationLevel;
  /**
   * The status of the invoice before event occurrence. See [Invoice
   * Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses)
   * for more.
   */
  fromStatus: InvoiceStatus;
  /**
   * The status of the invoice after event occurrence. See [Invoice
   * Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses)
   * for more.
   */
  toStatus: InvoiceStatus;
  /** Amount due on the invoice, which is `total_amount - credit_amount - paid_amount`. */
  dueAmount: string;
  /** The invoice total, which is `subtotal_amount - discount_amount + tax_amount`.' */
  totalAmount: string;
};

export const issueInvoiceEventDataSchema: Schema<IssueInvoiceEventData> = s.object<IssueInvoiceEventData>({
  consolidationLevel: invoiceConsolidationLevelSchema,
  fromStatus: invoiceStatusSchema,
  toStatus: invoiceStatusSchema,
  dueAmount: s.string(),
  totalAmount: s.string(),
  _keysMap: {
    consolidationLevel: "consolidation_level",
    fromStatus: "from_status",
    toStatus: "to_status",
    dueAmount: "due_amount",
    totalAmount: "total_amount",
  },
});
