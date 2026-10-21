import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceBalanceItemSchema, type InvoiceBalanceItem } from "./invoice-balance-item.js";

export type InvoicePreviousBalance = {
  capturedAt?: Date;
  invoices?: InvoiceBalanceItem[];
};

export const invoicePreviousBalanceSchema: Schema<InvoicePreviousBalance> = s.object<InvoicePreviousBalance>({
  capturedAt: s.optional(s.dateTime()),
  invoices: s.optional(s.array(s.lazy(() => invoiceBalanceItemSchema))),
  _keysMap: {
    capturedAt: "captured_at",
  },
});
