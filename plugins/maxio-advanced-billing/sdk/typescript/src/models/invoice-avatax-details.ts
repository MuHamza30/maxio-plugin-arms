import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceAvataxDetails = {
  id?: number | null;
  status?: string | null;
  documentCode?: string | null;
  commitDate?: Date | null;
  modifyDate?: Date | null;
};

export const invoiceAvataxDetailsSchema: Schema<InvoiceAvataxDetails> = s.object<InvoiceAvataxDetails>({
  id: s.optionalNullable(s.int()),
  status: s.optionalNullable(s.string()),
  documentCode: s.optionalNullable(s.string()),
  commitDate: s.optionalNullable(s.dateTime()),
  modifyDate: s.optionalNullable(s.dateTime()),
  _keysMap: {
    documentCode: "document_code",
    commitDate: "commit_date",
    modifyDate: "modify_date",
  },
});
