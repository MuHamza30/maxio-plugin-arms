import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { mrrMovementSchema, type MrrMovement } from "./mrr-movement.js";

export type MovementLineItem = {
  productId?: number;
  /** For Product (or "baseline") line items, this field will have a value of `0`. */
  componentId?: number;
  pricePointId?: number;
  name?: string;
  mrr?: number;
  mrrMovements?: MrrMovement[];
  quantity?: number;
  prevQuantity?: number;
  /**
   * When `true`, the line item's MRR value will contribute to the `plan` breakout. When `false`,
   * the line item contributes to the `usage` breakout.
   */
  recurring?: boolean;
};

export const movementLineItemSchema: Schema<MovementLineItem> = s.object<MovementLineItem>({
  productId: s.optional(s.int()),
  componentId: s.optional(s.int()),
  pricePointId: s.optional(s.int()),
  name: s.optional(s.string()),
  mrr: s.optional(s.int()),
  mrrMovements: s.optional(s.array(s.lazy(() => mrrMovementSchema))),
  quantity: s.optional(s.int()),
  prevQuantity: s.optional(s.int()),
  recurring: s.optional(s.boolean()),
  _keysMap: {
    productId: "product_id",
    componentId: "component_id",
    pricePointId: "price_point_id",
    mrrMovements: "mrr_movements",
    prevQuantity: "prev_quantity",
  },
});
