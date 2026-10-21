import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { debitNoteSchema, type DebitNote } from "./debit-note.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type CreateDebitNoteEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.CreateDebitNote */
  eventType?: InvoiceEventType;
  /** Example schema for an `create_debit_note` event */
  eventData: DebitNote;
};

export const createDebitNoteEventSchema: Schema<CreateDebitNoteEvent> = s.object<CreateDebitNoteEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.CreateDebitNote),
  eventData: debitNoteSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
