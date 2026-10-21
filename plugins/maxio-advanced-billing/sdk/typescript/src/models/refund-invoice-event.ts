import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";
import { refundInvoiceEventDataSchema, type RefundInvoiceEventData } from "./refund-invoice-event-data.js";

export type RefundInvoiceEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.RefundInvoice */
  eventType?: InvoiceEventType;
  /** Example schema for an `refund_invoice` event */
  eventData: RefundInvoiceEventData;
};

export const refundInvoiceEventSchema: Schema<RefundInvoiceEvent> = s.object<RefundInvoiceEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.RefundInvoice),
  eventData: refundInvoiceEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
