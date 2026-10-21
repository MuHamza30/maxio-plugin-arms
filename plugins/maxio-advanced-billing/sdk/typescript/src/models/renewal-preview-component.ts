import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentId2Schema, type ComponentId2 } from "./unions/component-id2.js";
import { pricePointId3Schema, type PricePointId3 } from "./unions/price-point-id3.js";

export type RenewalPreviewComponent = {
  /** Either the component's Chargify id or its handle prefixed with `handle:` */
  componentId?: ComponentId2;
  /**
   * The quantity for which you wish to preview billing. This is useful if you want to preview a
   * predicted, higher usage value than is currently present on the subscription.
   *
   * This quantity represents:
   *
   * - Whether or not an on/off component is enabled - use 0 for disabled or 1 for enabled
   * - The desired allocated_quantity for a quantity-based component
   * - The desired unit_balance for a metered component
   * - The desired metric quantity for an events-based component
   */
  quantity?: number;
  /** Either the component price point's Chargify id or its handle prefixed with `handle:` */
  pricePointId?: PricePointId3;
};

export const renewalPreviewComponentSchema: Schema<RenewalPreviewComponent> =
  s.object<RenewalPreviewComponent>({
    componentId: s.optional(s.lazy(() => componentId2Schema)),
    quantity: s.optional(s.int()),
    pricePointId: s.optional(s.lazy(() => pricePointId3Schema)),
    _keysMap: {
      componentId: "component_id",
      pricePointId: "price_point_id",
    },
  });
