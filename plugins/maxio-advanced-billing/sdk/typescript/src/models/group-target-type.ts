import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The type of object indicated by the id attribute. */
export const GroupTargetType = {
  Customer: "customer",
  Subscription: "subscription",
  Self: "self",
  Parent: "parent",
  Eldest: "eldest",
} as const;
export type GroupTargetType = (typeof GroupTargetType)[keyof typeof GroupTargetType] | (string & {});

export const groupTargetTypeSchema: EnumSchema<GroupTargetType> = s.enumOf<GroupTargetType>(GroupTargetType);
