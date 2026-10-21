import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  changeInvoiceStatusEventDataSchema,
  type ChangeInvoiceStatusEventData,
} from "./change-invoice-status-event-data.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ChangeInvoiceStatusEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.ChangeInvoiceStatus */
  eventType?: InvoiceEventType;
  /** Example schema for an `change_invoice_status` event */
  eventData: ChangeInvoiceStatusEventData;
};

export const changeInvoiceStatusEventSchema: Schema<ChangeInvoiceStatusEvent> =
  s.object<ChangeInvoiceStatusEvent>({
    id: s.int(),
    timestamp: s.dateTime(),
    invoice: invoiceSchema,
    eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.ChangeInvoiceStatus),
    eventData: changeInvoiceStatusEventDataSchema,
    _keysMap: {
      eventType: "event_type",
      eventData: "event_data",
    },
  });
