import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  invoicePaymentApplicationSchema,
  type InvoicePaymentApplication,
} from "./invoice-payment-application.js";

export type MultiInvoicePayment = {
  /** The numeric ID of the transaction. */
  transactionId?: number;
  /** Dollar amount of the sum of the paid invoices. */
  totalAmount?: string;
  /**
   * The ISO 4217 currency code (3 character string) representing the currency of invoice
   * transaction.
   */
  currencyCode?: string;
  applications?: InvoicePaymentApplication[];
};

export const multiInvoicePaymentSchema: Schema<MultiInvoicePayment> = s.object<MultiInvoicePayment>({
  transactionId: s.optional(s.int()),
  totalAmount: s.optional(s.string()),
  currencyCode: s.optional(s.string()),
  applications: s.optional(s.array(s.lazy(() => invoicePaymentApplicationSchema))),
  _keysMap: {
    transactionId: "transaction_id",
    totalAmount: "total_amount",
    currencyCode: "currency_code",
  },
});
