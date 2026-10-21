import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditNoteSchema, type CreditNote } from "./credit-note.js";
import { InvoiceEventType, invoiceEventTypeSchema } from "./invoice-event-type.js";
import { invoiceSchema, type Invoice } from "./invoice.js";

export type CreateCreditNoteEvent = {
  id: number;
  timestamp: Date;
  invoice: Invoice;
  /** @default InvoiceEventType.CreateCreditNote */
  eventType?: InvoiceEventType;
  /** Example schema for an `create_credit_note` event */
  eventData: CreditNote;
};

export const createCreditNoteEventSchema: Schema<CreateCreditNoteEvent> = s.object<CreateCreditNoteEvent>({
  id: s.int(),
  timestamp: s.dateTime(),
  invoice: invoiceSchema,
  eventType: s.defaulted(invoiceEventTypeSchema, InvoiceEventType.CreateCreditNote),
  eventData: creditNoteSchema,
  _keysMap: {
    eventType: "event_type",
    eventData: "event_data",
  },
});
