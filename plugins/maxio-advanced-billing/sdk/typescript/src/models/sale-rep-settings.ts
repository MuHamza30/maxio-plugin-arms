import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SaleRepSettings = {
  customerName?: string;
  subscriptionId?: number;
  siteLink?: string;
  siteName?: string;
  subscriptionMrr?: string;
  salesRepId?: number;
  salesRepName?: string;
};

export const saleRepSettingsSchema: Schema<SaleRepSettings> = s.object<SaleRepSettings>({
  customerName: s.optional(s.string()),
  subscriptionId: s.optional(s.int()),
  siteLink: s.optional(s.string()),
  siteName: s.optional(s.string()),
  subscriptionMrr: s.optional(s.string()),
  salesRepId: s.optional(s.int()),
  salesRepName: s.optional(s.string()),
  _keysMap: {
    customerName: "customer_name",
    subscriptionId: "subscription_id",
    siteLink: "site_link",
    siteName: "site_name",
    subscriptionMrr: "subscription_mrr",
    salesRepId: "sales_rep_id",
    salesRepName: "sales_rep_name",
  },
});
