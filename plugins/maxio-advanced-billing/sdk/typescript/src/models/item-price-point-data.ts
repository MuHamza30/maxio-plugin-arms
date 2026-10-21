import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type ItemPricePointData = {
  id?: number;
  handle?: string;
  name?: string;
};

export const itemPricePointDataSchema: Schema<ItemPricePointData> = s.object<ItemPricePointData>({
  id: s.optional(s.int()),
  handle: s.optional(s.string()),
  name: s.optional(s.string()),
});
