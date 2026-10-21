import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { metafieldSchema, type Metafield } from "./metafield.js";

export type ListMetafieldsResponse = {
  totalCount?: number;
  currentPage?: number;
  totalPages?: number;
  perPage?: number;
  metafields?: Metafield[];
};

export const listMetafieldsResponseSchema: Schema<ListMetafieldsResponse> = s.object<ListMetafieldsResponse>({
  totalCount: s.optional(s.int()),
  currentPage: s.optional(s.int()),
  totalPages: s.optional(s.int()),
  perPage: s.optional(s.int()),
  metafields: s.optional(s.array(s.lazy(() => metafieldSchema))),
  _keysMap: {
    totalCount: "total_count",
    currentPage: "current_page",
    totalPages: "total_pages",
    perPage: "per_page",
  },
});
