import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ListProformaInvoicesMeta = {
  totalCount?: number;
  currentPage?: number;
  totalPages?: number;
  statusCode?: number;
};

export const listProformaInvoicesMetaSchema: Schema<ListProformaInvoicesMeta> =
  s.object<ListProformaInvoicesMeta>({
    totalCount: s.optional(s.int()),
    currentPage: s.optional(s.int()),
    totalPages: s.optional(s.int()),
    statusCode: s.optional(s.int()),
    _keysMap: {
      totalCount: "total_count",
      currentPage: "current_page",
      totalPages: "total_pages",
      statusCode: "status_code",
    },
  });
