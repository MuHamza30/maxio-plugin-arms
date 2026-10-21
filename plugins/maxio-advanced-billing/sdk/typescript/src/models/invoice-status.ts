import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The current status of the invoice. See [Invoice
 * Statuses](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview#invoice-statuses)
 * for more.
 */
export const InvoiceStatus = {
  Draft: "draft",
  Open: "open",
  Paid: "paid",
  Pending: "pending",
  Voided: "voided",
  Canceled: "canceled",
  Processing: "processing",
} as const;
export type InvoiceStatus = (typeof InvoiceStatus)[keyof typeof InvoiceStatus] | (string & {});

export const invoiceStatusSchema: EnumSchema<InvoiceStatus> = s.enumOf<InvoiceStatus>(InvoiceStatus);
