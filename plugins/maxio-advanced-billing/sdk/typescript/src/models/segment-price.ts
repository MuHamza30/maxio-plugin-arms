import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SegmentPrice = {
  id?: number;
  componentId?: number;
  startingQuantity?: number;
  endingQuantity?: number | null;
  unitPrice?: string;
  pricePointId?: number;
  formattedUnitPrice?: string;
  segmentId?: number;
};

export const segmentPriceSchema: Schema<SegmentPrice> = s.object<SegmentPrice>({
  id: s.optional(s.int()),
  componentId: s.optional(s.int()),
  startingQuantity: s.optional(s.int()),
  endingQuantity: s.optionalNullable(s.int()),
  unitPrice: s.optional(s.string()),
  pricePointId: s.optional(s.int()),
  formattedUnitPrice: s.optional(s.string()),
  segmentId: s.optional(s.int()),
  _keysMap: {
    componentId: "component_id",
    startingQuantity: "starting_quantity",
    endingQuantity: "ending_quantity",
    unitPrice: "unit_price",
    pricePointId: "price_point_id",
    formattedUnitPrice: "formatted_unit_price",
    segmentId: "segment_id",
  },
});
