import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { subscriptionFilterSchema, type SubscriptionFilter } from "./subscription-filter.js";

export type ListSubscriptionComponentsForSiteFilter = {
  /**
   * Allows fetching components allocation with matching currency based on provided values. Use in
   * query `filter[currencies]=USD,EUR`.
   */
  currencies?: string[];
  /**
   * Allows fetching components allocation with matching use_site_exchange_rate based on provided
   * value. Use in query `filter[use_site_exchange_rate]=true`.
   */
  useSiteExchangeRate?: boolean;
  /** Nested filter used for List Subscription Components For Site Filter */
  subscription?: SubscriptionFilter;
};

export const listSubscriptionComponentsForSiteFilterSchema: Schema<ListSubscriptionComponentsForSiteFilter> =
  s.object<ListSubscriptionComponentsForSiteFilter>({
    currencies: s.optional(s.array(s.string())),
    useSiteExchangeRate: s.optional(s.boolean()),
    subscription: s.optional(s.lazy(() => subscriptionFilterSchema)),
    _keysMap: {
      useSiteExchangeRate: "use_site_exchange_rate",
    },
  });
