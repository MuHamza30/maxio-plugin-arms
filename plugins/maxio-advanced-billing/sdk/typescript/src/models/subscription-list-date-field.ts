import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const SubscriptionListDateField = {
  UpdatedAt: "updated_at",
} as const;
export type SubscriptionListDateField =
  | (typeof SubscriptionListDateField)[keyof typeof SubscriptionListDateField]
  | (string & {});

export const subscriptionListDateFieldSchema: EnumSchema<SubscriptionListDateField> =
  s.enumOf<SubscriptionListDateField>(SubscriptionListDateField);
