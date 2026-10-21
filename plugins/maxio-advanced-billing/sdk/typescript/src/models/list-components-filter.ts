import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ListComponentsFilter = {
  /**
   * Allows fetching components with matching id based on provided value. Use in query
   * `filter[ids]=1,2,3`.
   */
  ids?: number[];
  /**
   * Allows fetching components with matching use_site_exchange_rate based on provided value (refers
   * to default price point). Use in query `filter[use_site_exchange_rate]=true`.
   */
  useSiteExchangeRate?: boolean;
};

export const listComponentsFilterSchema: Schema<ListComponentsFilter> = s.object<ListComponentsFilter>({
  ids: s.optional(s.array(s.int())),
  useSiteExchangeRate: s.optional(s.boolean()),
  _keysMap: {
    useSiteExchangeRate: "use_site_exchange_rate",
  },
});
