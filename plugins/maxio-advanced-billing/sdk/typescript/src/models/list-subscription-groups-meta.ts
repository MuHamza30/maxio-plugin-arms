import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ListSubscriptionGroupsMeta = {
  currentPage?: number;
  totalCount?: number;
};

export const listSubscriptionGroupsMetaSchema: Schema<ListSubscriptionGroupsMeta> =
  s.object<ListSubscriptionGroupsMeta>({
    currentPage: s.optional(s.int()),
    totalCount: s.optional(s.int()),
    _keysMap: {
      currentPage: "current_page",
      totalCount: "total_count",
    },
  });
