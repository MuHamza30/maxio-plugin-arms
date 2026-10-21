import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  changeInvoiceCollectionMethodEventDataSchema,
  type ChangeInvoiceCollectionMethodEventData,
} from "./change-invoice-collection-method-event-data.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ChangeInvoiceCollectionMethodEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.ChangeInvoiceCollectionMethod */
  eventType?: InvoiceEventType;
  /** Example schema for an `change_invoice_collection_method` event */
  eventData: ChangeInvoiceCollectionMethodEventData;
};

export const changeInvoiceCollectionMethodEventSchema: Schema<ChangeInvoiceCollectionMethodEvent> =
  s.object<ChangeInvoiceCollectionMethodEvent>({
    id: s.int(),
    timestamp: s.dateTime(),
    invoice: invoiceSchema,
    eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.ChangeInvoiceCollectionMethod),
    eventData: changeInvoiceCollectionMethodEventDataSchema,
    _keysMap: {
      eventType: "event_type",
      eventData: "event_data",
    },
  });
