import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { siteStatisticsSchema, type SiteStatistics } from "./site-statistics.js";

export type SiteSummary = {
  sellerName?: string;
  siteName?: string;
  siteId?: number;
  siteCurrency?: string;
  stats?: SiteStatistics;
};

export const siteSummarySchema: Schema<SiteSummary> = s.object<SiteSummary>({
  sellerName: s.optional(s.string()),
  siteName: s.optional(s.string()),
  siteId: s.optional(s.int()),
  siteCurrency: s.optional(s.string()),
  stats: s.optional(s.lazy(() => siteStatisticsSchema)),
  _keysMap: {
    sellerName: "seller_name",
    siteName: "site_name",
    siteId: "site_id",
    siteCurrency: "site_currency",
  },
});
