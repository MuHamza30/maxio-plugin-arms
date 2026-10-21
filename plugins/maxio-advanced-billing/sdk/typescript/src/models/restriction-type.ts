import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const RestrictionType = {
  Component: "Component",
  Product: "Product",
} as const;
export type RestrictionType = (typeof RestrictionType)[keyof typeof RestrictionType] | (string & {});

export const restrictionTypeSchema: EnumSchema<RestrictionType> = s.enumOf<RestrictionType>(RestrictionType);
