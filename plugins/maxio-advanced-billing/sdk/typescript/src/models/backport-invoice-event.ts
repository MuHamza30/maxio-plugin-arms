import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type BackportInvoiceEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.BackportInvoice */
  eventType?: InvoiceEventType;
  /** Example schema for an `backport_invoice` event */
  eventData: Invoice;
};

export const backportInvoiceEventSchema: Schema<BackportInvoiceEvent> = s.object<BackportInvoiceEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.BackportInvoice),
  eventData: invoiceSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
