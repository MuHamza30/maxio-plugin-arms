import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  scheduledRenewalComponentCustomPriceSchema,
  type ScheduledRenewalComponentCustomPrice,
} from "./scheduled-renewal-component-custom-price.js";

export type ScheduledRenewalItemRequestBodyComponent = {
  /** Item type to add. Either Product or Component. @default "Component" */
  itemType?: "Component";
  /** Product or component identifier. */
  itemId: number;
  /** Price point identifier. */
  pricePointId?: number;
  /** (Optional) Quantity for the item. */
  quantity?: number;
  /** Custom pricing for a component within a scheduled renewal. */
  customPrice?: ScheduledRenewalComponentCustomPrice;
};

export const scheduledRenewalItemRequestBodyComponentSchema: Schema<ScheduledRenewalItemRequestBodyComponent> =
  s.object<ScheduledRenewalItemRequestBodyComponent>({
    itemType: s.defaulted(s.literal("Component"), "Component"),
    itemId: s.int(),
    pricePointId: s.optional(s.int()),
    quantity: s.optional(s.int()),
    customPrice: s.optional(s.lazy(() => scheduledRenewalComponentCustomPriceSchema)),
    _keysMap: {
      itemType: "item_type",
      itemId: "item_id",
      pricePointId: "price_point_id",
      customPrice: "custom_price",
    },
  });
