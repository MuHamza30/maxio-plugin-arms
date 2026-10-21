import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { invoiceEventSchema, type InvoiceEvent } from "./unions/invoice-event.js";

export type ListInvoiceEventsResponse = {
  events?: InvoiceEvent[];
  page?: number;
  perPage?: number;
  totalPages?: number;
};

export const listInvoiceEventsResponseSchema: Schema<ListInvoiceEventsResponse> =
  s.object<ListInvoiceEventsResponse>({
    events: s.optional(s.array(s.lazy(() => invoiceEventSchema))),
    page: s.optional(s.int()),
    perPage: s.optional(s.int()),
    totalPages: s.optional(s.int()),
    _keysMap: {
      perPage: "per_page",
      totalPages: "total_pages",
    },
  });
