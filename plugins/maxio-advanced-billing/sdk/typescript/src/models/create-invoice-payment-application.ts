import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreateInvoicePaymentApplication = {
  /**
   * Unique identifier for the invoice. It has the prefix "inv_" followed by alphanumeric
   * characters.
   */
  invoiceUid: string;
  /** Dollar amount of the invoice payment (eg. "10.50" => $10.50). */
  amount: string;
};

export const createInvoicePaymentApplicationSchema: Schema<CreateInvoicePaymentApplication> =
  s.object<CreateInvoicePaymentApplication>({
    invoiceUid: s.string(),
    amount: s.string(),
    _keysMap: {
      invoiceUid: "invoice_uid",
    },
  });
