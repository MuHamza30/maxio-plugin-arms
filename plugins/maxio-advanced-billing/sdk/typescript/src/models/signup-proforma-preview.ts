import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { proformaInvoiceSchema, type ProformaInvoice } from "./proforma-invoice.js";

export type SignupProformaPreview = {
  currentProformaInvoice?: ProformaInvoice;
  nextProformaInvoice?: ProformaInvoice;
};

export const signupProformaPreviewSchema: Schema<SignupProformaPreview> = s.object<SignupProformaPreview>({
  currentProformaInvoice: s.optional(s.lazy(() => proformaInvoiceSchema)),
  nextProformaInvoice: s.optional(s.lazy(() => proformaInvoiceSchema)),
  _keysMap: {
    currentProformaInvoice: "current_proforma_invoice",
    nextProformaInvoice: "next_proforma_invoice",
  },
});
