import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";
import { voidInvoiceEventDataSchema, type VoidInvoiceEventData } from "./void-invoice-event-data.js";

export type VoidInvoiceEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.VoidInvoice */
  eventType?: InvoiceEventType;
  /** Example schema for an `void_invoice` event */
  eventData: VoidInvoiceEventData;
};

export const voidInvoiceEventSchema: Schema<VoidInvoiceEvent> = s.object<VoidInvoiceEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.VoidInvoice),
  eventData: voidInvoiceEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
