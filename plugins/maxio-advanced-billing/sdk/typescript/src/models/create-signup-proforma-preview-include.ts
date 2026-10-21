import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const CreateSignupProformaPreviewInclude = {
  NextProformaInvoice: "next_proforma_invoice",
} as const;
export type CreateSignupProformaPreviewInclude =
  | (typeof CreateSignupProformaPreviewInclude)[keyof typeof CreateSignupProformaPreviewInclude]
  | (string & {});

export const createSignupProformaPreviewIncludeSchema: EnumSchema<CreateSignupProformaPreviewInclude> =
  s.enumOf<CreateSignupProformaPreviewInclude>(CreateSignupProformaPreviewInclude);
