import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";
import { removePaymentEventDataSchema, type RemovePaymentEventData } from "./remove-payment-event-data.js";

export type RemovePaymentEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.RemovePayment */
  eventType?: InvoiceEventType;
  /** Example schema for an `remove_payment` event */
  eventData: RemovePaymentEventData;
};

export const removePaymentEventSchema: Schema<RemovePaymentEvent> = s.object<RemovePaymentEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.RemovePayment),
  eventData: removePaymentEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
