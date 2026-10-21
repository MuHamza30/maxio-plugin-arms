import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { itemPricePointDataSchema, type ItemPricePointData } from "./item-price-point-data.js";

export type ItemPricePointChanged = {
  itemId: number;
  itemType: string;
  itemHandle: string;
  itemName: string;
  previousPricePoint: ItemPricePointData;
  currentPricePoint: ItemPricePointData;
};

export const itemPricePointChangedSchema: Schema<ItemPricePointChanged> = s.object<ItemPricePointChanged>({
  itemId: s.int(),
  itemType: s.string(),
  itemHandle: s.string(),
  itemName: s.string(),
  previousPricePoint: itemPricePointDataSchema,
  currentPricePoint: itemPricePointDataSchema,
  _keysMap: {
    itemId: "item_id",
    itemType: "item_type",
    itemHandle: "item_handle",
    itemName: "item_name",
    previousPricePoint: "previous_price_point",
    currentPricePoint: "current_price_point",
  },
});
