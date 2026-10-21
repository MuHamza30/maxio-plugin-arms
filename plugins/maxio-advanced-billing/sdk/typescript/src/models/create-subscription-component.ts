import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { componentCustomPriceSchema, type ComponentCustomPrice } from "./component-custom-price.js";
import { allocatedQuantity3Schema, type AllocatedQuantity3 } from "./unions/allocated-quantity3.js";
import { componentId1Schema, type ComponentId1 } from "./unions/component-id1.js";
import { pricePointId2Schema, type PricePointId2 } from "./unions/price-point-id2.js";
import { unitBalance2Schema, type UnitBalance2 } from "./unions/unit-balance2.js";

export type CreateSubscriptionComponent = {
  componentId?: ComponentId1;
  /** Used for on/off components only. */
  enabled?: boolean;
  /** Used for metered and events based components. */
  unitBalance?: UnitBalance2;
  /** Used for quantity based components. */
  allocatedQuantity?: AllocatedQuantity3;
  /**
   * Deprecated. Use `allocated_quantity` instead.
   *
   * @deprecated
   */
  quantity?: number;
  pricePointId?: PricePointId2;
  /**
   * Create or update custom pricing unique to the subscription. Used in place of `price_point_id`.
   */
  customPrice?: ComponentCustomPrice;
};

export const createSubscriptionComponentSchema: Schema<CreateSubscriptionComponent> =
  s.object<CreateSubscriptionComponent>({
    componentId: s.optional(s.lazy(() => componentId1Schema)),
    enabled: s.optional(s.boolean()),
    unitBalance: s.optional(s.lazy(() => unitBalance2Schema)),
    allocatedQuantity: s.optional(s.lazy(() => allocatedQuantity3Schema)),
    quantity: s.optional(s.int()),
    pricePointId: s.optional(s.lazy(() => pricePointId2Schema)),
    customPrice: s.optional(s.lazy(() => componentCustomPriceSchema)),
    _keysMap: {
      componentId: "component_id",
      unitBalance: "unit_balance",
      allocatedQuantity: "allocated_quantity",
      pricePointId: "price_point_id",
      customPrice: "custom_price",
    },
  });
