import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { restrictionTypeSchema, type RestrictionType } from "./restriction-type.js";

export type CouponRestriction = {
  id?: number;
  itemType?: RestrictionType;
  itemId?: number;
  name?: string;
  handle?: string | null;
};

export const couponRestrictionSchema: Schema<CouponRestriction> = s.object<CouponRestriction>({
  id: s.optional(s.int()),
  itemType: s.optional(s.lazy(() => restrictionTypeSchema)),
  itemId: s.optional(s.int()),
  name: s.optional(s.string()),
  handle: s.optionalNullable(s.string()),
  _keysMap: {
    itemType: "item_type",
    itemId: "item_id",
  },
});
