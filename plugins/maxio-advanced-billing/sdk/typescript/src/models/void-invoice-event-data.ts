import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditNoteSchema, type CreditNote } from "./credit-note.js";

/** Example schema for an `void_invoice` event */
export type VoidInvoiceEventData = {
  creditNoteAttributes: CreditNote | null;
  /** The memo provided during invoice voiding. */
  memo: string | null;
  /** The amount of the void. */
  appliedAmount: string | null;
  /** The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" */
  transactionTime: Date | null;
  /** If true, the invoice is an advance invoice. */
  isAdvanceInvoice: boolean;
  /** The reason for the void. */
  reason: string;
};

export const voidInvoiceEventDataSchema: Schema<VoidInvoiceEventData> = s.object<VoidInvoiceEventData>({
  creditNoteAttributes: s.nullable(s.lazy(() => creditNoteSchema)),
  memo: s.nullable(s.string()),
  appliedAmount: s.nullable(s.string()),
  transactionTime: s.nullable(s.dateTime()),
  isAdvanceInvoice: s.boolean(),
  reason: s.string(),
  _keysMap: {
    creditNoteAttributes: "credit_note_attributes",
    appliedAmount: "applied_amount",
    transactionTime: "transaction_time",
    isAdvanceInvoice: "is_advance_invoice",
  },
});
