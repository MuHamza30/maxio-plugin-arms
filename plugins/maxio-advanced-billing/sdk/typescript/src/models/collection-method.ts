import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The type of payment collection to be used in the subscription. For legacy Statements Architecture
 * valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid
 * options are - `remittance`, `automatic`, `prepaid`.
 */
export const CollectionMethod = {
  Automatic: "automatic",
  Remittance: "remittance",
  Prepaid: "prepaid",
  Invoice: "invoice",
} as const;
export type CollectionMethod = (typeof CollectionMethod)[keyof typeof CollectionMethod] | (string & {});

export const collectionMethodSchema: EnumSchema<CollectionMethod> =
  s.enumOf<CollectionMethod>(CollectionMethod);
