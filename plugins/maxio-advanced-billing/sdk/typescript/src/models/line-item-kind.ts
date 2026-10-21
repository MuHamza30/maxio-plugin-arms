import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** A handle for the line item kind */
export const LineItemKind = {
  Baseline: "baseline",
  Initial: "initial",
  Trial: "trial",
  QuantityBasedComponent: "quantity_based_component",
  PrepaidUsageComponent: "prepaid_usage_component",
  OnOffComponent: "on_off_component",
  MeteredComponent: "metered_component",
  EventBasedComponent: "event_based_component",
  Coupon: "coupon",
  Tax: "tax",
} as const;
export type LineItemKind = (typeof LineItemKind)[keyof typeof LineItemKind] | (string & {});

export const lineItemKindSchema: EnumSchema<LineItemKind> = s.enumOf<LineItemKind>(LineItemKind);
