import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  listSubscriptionGroupsItemSchema,
  type ListSubscriptionGroupsItem,
} from "./list-subscription-groups-item.js";
import {
  listSubscriptionGroupsMetaSchema,
  type ListSubscriptionGroupsMeta,
} from "./list-subscription-groups-meta.js";

export type ListSubscriptionGroupsResponse = {
  subscriptionGroups?: ListSubscriptionGroupsItem[];
  meta?: ListSubscriptionGroupsMeta;
};

export const listSubscriptionGroupsResponseSchema: Schema<ListSubscriptionGroupsResponse> =
  s.object<ListSubscriptionGroupsResponse>({
    subscriptionGroups: s.optional(s.array(s.lazy(() => listSubscriptionGroupsItemSchema))),
    meta: s.optional(s.lazy(() => listSubscriptionGroupsMetaSchema)),
    _keysMap: {
      subscriptionGroups: "subscription_groups",
    },
  });
