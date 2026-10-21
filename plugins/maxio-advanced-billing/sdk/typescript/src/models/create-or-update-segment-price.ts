import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { unitPrice8Schema, type UnitPrice8 } from "./unions/unit-price8.js";

export type CreateOrUpdateSegmentPrice = {
  startingQuantity?: number;
  endingQuantity?: number;
  /** The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065 */
  unitPrice: UnitPrice8;
};

export const createOrUpdateSegmentPriceSchema: Schema<CreateOrUpdateSegmentPrice> =
  s.object<CreateOrUpdateSegmentPrice>({
    startingQuantity: s.optional(s.int()),
    endingQuantity: s.optional(s.int()),
    unitPrice: unitPrice8Schema,
    _keysMap: {
      startingQuantity: "starting_quantity",
      endingQuantity: "ending_quantity",
      unitPrice: "unit_price",
    },
  });
