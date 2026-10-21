import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** A handle for the component type */
export const ComponentKind = {
  MeteredComponent: "metered_component",
  QuantityBasedComponent: "quantity_based_component",
  OnOffComponent: "on_off_component",
  PrepaidUsageComponent: "prepaid_usage_component",
  EventBasedComponent: "event_based_component",
  WalletProduct: "wallet_product",
} as const;
export type ComponentKind = (typeof ComponentKind)[keyof typeof ComponentKind] | (string & {});

export const componentKindSchema: EnumSchema<ComponentKind> = s.enumOf<ComponentKind>(ComponentKind);
