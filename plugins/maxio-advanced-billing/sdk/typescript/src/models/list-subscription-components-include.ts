import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const ListSubscriptionComponentsInclude = {
  Subscription: "subscription",
  HistoricUsages: "historic_usages",
} as const;
export type ListSubscriptionComponentsInclude =
  | (typeof ListSubscriptionComponentsInclude)[keyof typeof ListSubscriptionComponentsInclude]
  | (string & {});

export const listSubscriptionComponentsIncludeSchema: EnumSchema<ListSubscriptionComponentsInclude> =
  s.enumOf<ListSubscriptionComponentsInclude>(ListSubscriptionComponentsInclude);
