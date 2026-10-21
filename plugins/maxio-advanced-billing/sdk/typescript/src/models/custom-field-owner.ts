import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const CustomFieldOwner = {
  Customer: "Customer",
  Subscription: "Subscription",
} as const;
export type CustomFieldOwner = (typeof CustomFieldOwner)[keyof typeof CustomFieldOwner] | (string & {});

export const customFieldOwnerSchema: EnumSchema<CustomFieldOwner> =
  s.enumOf<CustomFieldOwner>(CustomFieldOwner);
