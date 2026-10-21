import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ComponentPricePointErrorItem = {
  componentId?: number;
  message?: string;
  pricePoint?: number;
};

export const componentPricePointErrorItemSchema: Schema<ComponentPricePointErrorItem> =
  s.object<ComponentPricePointErrorItem>({
    componentId: s.optional(s.int()),
    message: s.optional(s.string()),
    pricePoint: s.optional(s.int()),
    _keysMap: {
      componentId: "component_id",
      pricePoint: "price_point",
    },
  });
