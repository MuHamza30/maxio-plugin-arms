import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";
import { issueInvoiceEventDataSchema, type IssueInvoiceEventData } from "./issue-invoice-event-data.js";

export type IssueInvoiceEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.IssueInvoice */
  eventType?: InvoiceEventType;
  /** Example schema for an `issue_invoice` event */
  eventData: IssueInvoiceEventData;
};

export const issueInvoiceEventSchema: Schema<IssueInvoiceEvent> = s.object<IssueInvoiceEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.IssueInvoice),
  eventData: issueInvoiceEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
