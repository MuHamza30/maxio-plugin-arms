import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoicePrePaymentSchema, type InvoicePrePayment } from "./invoice-pre-payment.js";
import { paidInvoiceSchema, type PaidInvoice } from "./paid-invoice.js";

export type RecordPaymentResponse = {
  paidInvoices?: PaidInvoice[];
  prepayment?: InvoicePrePayment | null;
};

export const recordPaymentResponseSchema: Schema<RecordPaymentResponse> = s.object<RecordPaymentResponse>({
  paidInvoices: s.optional(s.array(s.lazy(() => paidInvoiceSchema))),
  prepayment: s.optionalNullable(s.lazy(() => invoicePrePaymentSchema)),
  _keysMap: {
    paidInvoices: "paid_invoices",
  },
});
