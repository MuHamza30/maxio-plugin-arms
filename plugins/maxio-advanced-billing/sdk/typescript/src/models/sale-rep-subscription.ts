import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SaleRepSubscription = {
  id?: number;
  siteName?: string;
  subscriptionUrl?: string;
  customerName?: string;
  createdAt?: string;
  mrr?: string;
  usage?: string;
  recurring?: string;
  lastPayment?: string;
  churnDate?: string | null;
};

export const saleRepSubscriptionSchema: Schema<SaleRepSubscription> = s.object<SaleRepSubscription>({
  id: s.optional(s.int()),
  siteName: s.optional(s.string()),
  subscriptionUrl: s.optional(s.string()),
  customerName: s.optional(s.string()),
  createdAt: s.optional(s.string()),
  mrr: s.optional(s.string()),
  usage: s.optional(s.string()),
  recurring: s.optional(s.string()),
  lastPayment: s.optional(s.string()),
  churnDate: s.optionalNullable(s.string()),
  _keysMap: {
    siteName: "site_name",
    subscriptionUrl: "subscription_url",
    customerName: "customer_name",
    createdAt: "created_at",
    lastPayment: "last_payment",
    churnDate: "churn_date",
  },
});
