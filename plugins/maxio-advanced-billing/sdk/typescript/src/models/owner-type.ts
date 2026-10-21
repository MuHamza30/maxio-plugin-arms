import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The polymorphic owner type. `subscription` is the only value currently supported. */
export const OwnerType = {
  Subscription: "subscription",
} as const;
export type OwnerType = (typeof OwnerType)[keyof typeof OwnerType] | (string & {});

export const ownerTypeSchema: EnumSchema<OwnerType> = s.enumOf<OwnerType>(OwnerType);
