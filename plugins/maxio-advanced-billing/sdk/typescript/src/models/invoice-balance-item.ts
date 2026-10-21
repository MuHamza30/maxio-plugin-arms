import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoiceBalanceItem = {
  uid?: string;
  number?: string;
  outstandingAmount?: string;
};

export const invoiceBalanceItemSchema: Schema<InvoiceBalanceItem> = s.object<InvoiceBalanceItem>({
  uid: s.optional(s.string()),
  number: s.optional(s.string()),
  outstandingAmount: s.optional(s.string()),
  _keysMap: {
    outstandingAmount: "outstanding_amount",
  },
});
