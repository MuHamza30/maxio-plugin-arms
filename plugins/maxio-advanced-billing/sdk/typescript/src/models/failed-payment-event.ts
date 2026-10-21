import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { failedPaymentEventDataSchema, type FailedPaymentEventData } from "./failed-payment-event-data.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type FailedPaymentEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.FailedPayment */
  eventType?: InvoiceEventType;
  /** Example schema for an `failed_payment` event */
  eventData: FailedPaymentEventData;
};

export const failedPaymentEventSchema: Schema<FailedPaymentEvent> = s.object<FailedPaymentEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.FailedPayment),
  eventData: failedPaymentEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
