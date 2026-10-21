import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ListMrrFilter = {
  /** Submit ids in order to limit results. Use in query: `filter[subscription_ids]=1,2,3`. */
  subscriptionIds?: number[];
};

export const listMrrFilterSchema: Schema<ListMrrFilter> = s.object<ListMrrFilter>({
  subscriptionIds: s.optional(s.array(s.int())),
  _keysMap: {
    subscriptionIds: "subscription_ids",
  },
});
