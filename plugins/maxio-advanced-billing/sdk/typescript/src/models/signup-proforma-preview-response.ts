import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { signupProformaPreviewSchema, type SignupProformaPreview } from "./signup-proforma-preview.js";

export type SignupProformaPreviewResponse = {
  proformaInvoicePreview: SignupProformaPreview;
};

export const signupProformaPreviewResponseSchema: Schema<SignupProformaPreviewResponse> =
  s.object<SignupProformaPreviewResponse>({
    proformaInvoicePreview: signupProformaPreviewSchema,
    _keysMap: {
      proformaInvoicePreview: "proforma_invoice_preview",
    },
  });
