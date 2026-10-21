import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { creditNoteSchema, type CreditNote } from "./credit-note.js";

export type ListCreditNotesResponse = {
  creditNotes: CreditNote[];
};

export const listCreditNotesResponseSchema: Schema<ListCreditNotesResponse> =
  s.object<ListCreditNotesResponse>({
    creditNotes: s.array(s.lazy(() => creditNoteSchema)),
    _keysMap: {
      creditNotes: "credit_notes",
    },
  });
