import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoicePaymentApplication = {
  /**
   * Unique identifier for the paid invoice. It has the prefix "inv_" followed by alphanumeric
   * characters.
   */
  invoiceUid?: string;
  /**
   * Unique identifier for the payment. It has the prefix "pmt_" followed by alphanumeric
   * characters.
   */
  applicationUid?: string;
  /** Dollar amount of the paid invoice. */
  appliedAmount?: string;
};

export const invoicePaymentApplicationSchema: Schema<InvoicePaymentApplication> =
  s.object<InvoicePaymentApplication>({
    invoiceUid: s.optional(s.string()),
    applicationUid: s.optional(s.string()),
    appliedAmount: s.optional(s.string()),
    _keysMap: {
      invoiceUid: "invoice_uid",
      applicationUid: "application_uid",
      appliedAmount: "applied_amount",
    },
  });
