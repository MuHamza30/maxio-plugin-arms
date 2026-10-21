import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const CollectionMethod1 = {
  Automatic: "automatic",
  Remittance: "remittance",
  Prepaid: "prepaid",
} as const;
export type CollectionMethod1 = (typeof CollectionMethod1)[keyof typeof CollectionMethod1] | (string & {});

export const collectionMethod1Schema: EnumSchema<CollectionMethod1> =
  s.enumOf<CollectionMethod1>(CollectionMethod1);
