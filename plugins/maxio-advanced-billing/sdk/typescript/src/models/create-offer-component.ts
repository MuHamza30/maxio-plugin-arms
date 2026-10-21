import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreateOfferComponent = {
  componentId?: number;
  pricePointId?: number;
  startingQuantity?: number;
};

export const createOfferComponentSchema: Schema<CreateOfferComponent> = s.object<CreateOfferComponent>({
  componentId: s.optional(s.int()),
  pricePointId: s.optional(s.int()),
  startingQuantity: s.optional(s.int()),
  _keysMap: {
    componentId: "component_id",
    pricePointId: "price_point_id",
    startingQuantity: "starting_quantity",
  },
});
