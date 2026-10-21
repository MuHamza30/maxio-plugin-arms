import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  applyDebitNoteEventDataSchema,
  type ApplyDebitNoteEventData,
} from "./apply-debit-note-event-data.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ApplyDebitNoteEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.ApplyDebitNote */
  eventType?: InvoiceEventType;
  /** Example schema for an `apply_debit_note` event */
  eventData: ApplyDebitNoteEventData;
};

export const applyDebitNoteEventSchema: Schema<ApplyDebitNoteEvent> = s.object<ApplyDebitNoteEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.ApplyDebitNote),
  eventData: applyDebitNoteEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
