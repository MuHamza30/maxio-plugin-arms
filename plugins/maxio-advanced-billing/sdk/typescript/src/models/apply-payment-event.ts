import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { applyPaymentEventDataSchema, type ApplyPaymentEventData } from "./apply-payment-event-data.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ApplyPaymentEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.ApplyPayment */
  eventType?: InvoiceEventType;
  /** Example schema for an `apply_payment` event */
  eventData: ApplyPaymentEventData;
};

export const applyPaymentEventSchema: Schema<ApplyPaymentEvent> = s.object<ApplyPaymentEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.ApplyPayment),
  eventData: applyPaymentEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
