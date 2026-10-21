import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  listProformaInvoicesMetaSchema,
  type ListProformaInvoicesMeta,
} from "./list-proforma-invoices-meta.js";
import { proformaInvoiceSchema, type ProformaInvoice } from "./proforma-invoice.js";

export type ListProformaInvoicesResponse = {
  proformaInvoices?: ProformaInvoice[];
  meta?: ListProformaInvoicesMeta;
};

export const listProformaInvoicesResponseSchema: Schema<ListProformaInvoicesResponse> =
  s.object<ListProformaInvoicesResponse>({
    proformaInvoices: s.optional(s.array(s.lazy(() => proformaInvoiceSchema))),
    meta: s.optional(s.lazy(() => listProformaInvoicesMetaSchema)),
    _keysMap: {
      proformaInvoices: "proforma_invoices",
    },
  });
