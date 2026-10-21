import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  applyCreditNoteEventDataSchema,
  type ApplyCreditNoteEventData,
} from "./apply-credit-note-event-data.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type ApplyCreditNoteEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.ApplyCreditNote */
  eventType?: InvoiceEventType;
  /** Example schema for an `apply_credit_note` event */
  eventData: ApplyCreditNoteEventData;
};

export const applyCreditNoteEventSchema: Schema<ApplyCreditNoteEvent> = s.object<ApplyCreditNoteEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.ApplyCreditNote),
  eventData: applyCreditNoteEventDataSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
