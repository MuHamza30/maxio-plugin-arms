import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";
import { voidRemainderEventDataSchema, type VoidRemainderEventData } from "./void-remainder-event-data.js";

export type VoidRemainderEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.VoidRemainder */
  eventType?: InvoiceEventType;
  /** Example schema for an `void_remainder` event */
  eventData: VoidRemainderEventData;
};

export const voidRemainderEventSchema: Schema<VoidRemainderEvent> = s.object<VoidRemainderEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.VoidRemainder),
  eventData: voidRemainderEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
