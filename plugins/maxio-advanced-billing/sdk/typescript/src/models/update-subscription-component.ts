import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentCustomPriceSchema, type ComponentCustomPrice } from "./component-custom-price.js";

export type UpdateSubscriptionComponent = {
  componentId?: number;
  /**
   * Create or update custom pricing unique to the subscription. Used in place of `price_point_id`.
   */
  customPrice?: ComponentCustomPrice;
};

export const updateSubscriptionComponentSchema: Schema<UpdateSubscriptionComponent> =
  s.object<UpdateSubscriptionComponent>({
    componentId: s.optional(s.int()),
    customPrice: s.optional(s.lazy(() => componentCustomPriceSchema)),
    _keysMap: {
      componentId: "component_id",
      customPrice: "custom_price",
    },
  });
