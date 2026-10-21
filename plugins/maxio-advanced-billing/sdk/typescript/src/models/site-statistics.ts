import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SiteStatistics = {
  totalSubscriptions?: number;
  subscriptionsToday?: number;
  totalRevenue?: string;
  revenueToday?: string;
  revenueThisMonth?: string;
  revenueThisYear?: string;
  totalCanceledSubscriptions?: number;
  totalActiveSubscriptions?: number;
  totalPastDueSubscriptions?: number;
  totalUnpaidSubscriptions?: number;
  totalDunningSubscriptions?: number;
};

export const siteStatisticsSchema: Schema<SiteStatistics> = s.object<SiteStatistics>({
  totalSubscriptions: s.optional(s.int()),
  subscriptionsToday: s.optional(s.int()),
  totalRevenue: s.optional(s.string()),
  revenueToday: s.optional(s.string()),
  revenueThisMonth: s.optional(s.string()),
  revenueThisYear: s.optional(s.string()),
  totalCanceledSubscriptions: s.optional(s.int()),
  totalActiveSubscriptions: s.optional(s.int()),
  totalPastDueSubscriptions: s.optional(s.int()),
  totalUnpaidSubscriptions: s.optional(s.int()),
  totalDunningSubscriptions: s.optional(s.int()),
  _keysMap: {
    totalSubscriptions: "total_subscriptions",
    subscriptionsToday: "subscriptions_today",
    totalRevenue: "total_revenue",
    revenueToday: "revenue_today",
    revenueThisMonth: "revenue_this_month",
    revenueThisYear: "revenue_this_year",
    totalCanceledSubscriptions: "total_canceled_subscriptions",
    totalActiveSubscriptions: "total_active_subscriptions",
    totalPastDueSubscriptions: "total_past_due_subscriptions",
    totalUnpaidSubscriptions: "total_unpaid_subscriptions",
    totalDunningSubscriptions: "total_dunning_subscriptions",
  },
});
