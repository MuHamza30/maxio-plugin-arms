import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { pricePoint2Schema, type PricePoint2 } from "./unions/price-point2.js";

export type ComponentPricePointAssignment = {
  componentId?: number;
  pricePoint?: PricePoint2;
};

export const componentPricePointAssignmentSchema: Schema<ComponentPricePointAssignment> =
  s.object<ComponentPricePointAssignment>({
    componentId: s.optional(s.int()),
    pricePoint: s.optional(s.lazy(() => pricePoint2Schema)),
    _keysMap: {
      componentId: "component_id",
      pricePoint: "price_point",
    },
  });
