import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { saleRepSubscriptionSchema, type SaleRepSubscription } from "./sale-rep-subscription.js";

export type SaleRep = {
  id?: number;
  fullName?: string;
  subscriptionsCount?: number;
  testMode?: boolean;
  subscriptions?: SaleRepSubscription[];
};

export const saleRepSchema: Schema<SaleRep> = s.object<SaleRep>({
  id: s.optional(s.int()),
  fullName: s.optional(s.string()),
  subscriptionsCount: s.optional(s.int()),
  testMode: s.optional(s.boolean()),
  subscriptions: s.optional(s.array(s.lazy(() => saleRepSubscriptionSchema))),
  _keysMap: {
    fullName: "full_name",
    subscriptionsCount: "subscriptions_count",
    testMode: "test_mode",
  },
});
