import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const QScope = {
  FullName: "full_name",
  FirstName: "first_name",
  LastName: "last_name",
  Organization: "organization",
  CustomerReference: "customer_reference",
  SubscriptionReference: "subscription_reference",
} as const;
export type QScope = (typeof QScope)[keyof typeof QScope] | (string & {});

export const qScopeSchema: EnumSchema<QScope> = s.enumOf<QScope>(QScope);
