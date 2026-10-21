import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** A handle for the line item kind for allocation preview */
export const AllocationPreviewLineItemKind = {
  QuantityBasedComponent: "quantity_based_component",
  OnOffComponent: "on_off_component",
  Coupon: "coupon",
  Tax: "tax",
} as const;
export type AllocationPreviewLineItemKind =
  | (typeof AllocationPreviewLineItemKind)[keyof typeof AllocationPreviewLineItemKind]
  | (string & {});

export const allocationPreviewLineItemKindSchema: EnumSchema<AllocationPreviewLineItemKind> =
  s.enumOf<AllocationPreviewLineItemKind>(AllocationPreviewLineItemKind);
