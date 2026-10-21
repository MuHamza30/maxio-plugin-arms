import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { metadataSchema, type Metadata } from "./metadata.js";

export type PaginatedMetadata = {
  totalCount?: number;
  currentPage?: number;
  totalPages?: number;
  perPage?: number;
  metadata?: Metadata[];
};

export const paginatedMetadataSchema: Schema<PaginatedMetadata> = s.object<PaginatedMetadata>({
  totalCount: s.optional(s.int()),
  currentPage: s.optional(s.int()),
  totalPages: s.optional(s.int()),
  perPage: s.optional(s.int()),
  metadata: s.optional(s.array(s.lazy(() => metadataSchema))),
  _keysMap: {
    totalCount: "total_count",
    currentPage: "current_page",
    totalPages: "total_pages",
    perPage: "per_page",
  },
});
