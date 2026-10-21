import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { saleRepItemMrrSchema, type SaleRepItemMrr } from "./sale-rep-item-mrr.js";

export type ListSaleRepItem = {
  id?: number;
  fullName?: string;
  subscriptionsCount?: number;
  mrrData?: Record<string, SaleRepItemMrr>;
  testMode?: boolean;
};

export const listSaleRepItemSchema: Schema<ListSaleRepItem> = s.object<ListSaleRepItem>({
  id: s.optional(s.int()),
  fullName: s.optional(s.string()),
  subscriptionsCount: s.optional(s.int()),
  mrrData: s.optional(
    s.record(
      s.string(),
      s.lazy(() => saleRepItemMrrSchema),
    ),
  ),
  testMode: s.optional(s.boolean()),
  _keysMap: {
    fullName: "full_name",
    subscriptionsCount: "subscriptions_count",
    mrrData: "mrr_data",
    testMode: "test_mode",
  },
});
