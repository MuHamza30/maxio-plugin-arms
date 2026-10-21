import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionInclude = {
  Coupons: "coupons",
  SelfServicePageToken: "self_service_page_token",
} as const;
export type SubscriptionInclude =
  | (typeof SubscriptionInclude)[keyof typeof SubscriptionInclude]
  | (string & {});

export const subscriptionIncludeSchema: EnumSchema<SubscriptionInclude> =
  s.enumOf<SubscriptionInclude>(SubscriptionInclude);
