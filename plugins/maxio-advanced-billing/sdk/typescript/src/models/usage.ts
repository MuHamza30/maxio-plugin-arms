import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { quantity1Schema, type Quantity1 } from "./unions/quantity1.js";

export type Usage = {
  id?: number;
  memo?: string | null;
  createdAt?: Date;
  pricePointId?: number;
  quantity?: Quantity1;
  overageQuantity?: number;
  componentId?: number;
  componentHandle?: string;
  subscriptionId?: number;
};

export const usageSchema: Schema<Usage> = s.object<Usage>({
  id: s.optional(s.int()),
  memo: s.optionalNullable(s.string()),
  createdAt: s.optional(s.dateTime()),
  pricePointId: s.optional(s.int()),
  quantity: s.optional(s.lazy(() => quantity1Schema)),
  overageQuantity: s.optional(s.int()),
  componentId: s.optional(s.int()),
  componentHandle: s.optional(s.string()),
  subscriptionId: s.optional(s.int()),
  _keysMap: {
    createdAt: "created_at",
    pricePointId: "price_point_id",
    overageQuantity: "overage_quantity",
    componentId: "component_id",
    componentHandle: "component_handle",
    subscriptionId: "subscription_id",
  },
});
