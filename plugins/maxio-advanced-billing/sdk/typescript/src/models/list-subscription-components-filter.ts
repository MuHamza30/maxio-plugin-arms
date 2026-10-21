import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ListSubscriptionComponentsFilter = {
  /**
   * Allows fetching components allocation with matching currency based on provided values. Use in
   * query `filter[currencies]=EUR,USD`.
   */
  currencies?: string[];
  /**
   * Allows fetching components allocation with matching use_site_exchange_rate based on provided
   * value. Use in query `filter[use_site_exchange_rate]=true`.
   */
  useSiteExchangeRate?: boolean;
};

export const listSubscriptionComponentsFilterSchema: Schema<ListSubscriptionComponentsFilter> =
  s.object<ListSubscriptionComponentsFilter>({
    currencies: s.optional(s.array(s.string())),
    useSiteExchangeRate: s.optional(s.boolean()),
    _keysMap: {
      useSiteExchangeRate: "use_site_exchange_rate",
    },
  });
