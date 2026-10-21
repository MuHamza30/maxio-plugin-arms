import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * (Optional) For Event Based Components. If the `include=historic_usages` query param is provided,
 * the last ten billing periods will be returned.
 */
export type HistoricUsage = {
  /** Total usage of a component for billing period */
  totalUsageQuantity?: number;
  /** Start date of billing period */
  billingPeriodStartsAt?: Date;
  /** End date of billing period */
  billingPeriodEndsAt?: Date;
};

export const historicUsageSchema: Schema<HistoricUsage> = s.object<HistoricUsage>({
  totalUsageQuantity: s.optional(s.float64()),
  billingPeriodStartsAt: s.optional(s.dateTime()),
  billingPeriodEndsAt: s.optional(s.dateTime()),
  _keysMap: {
    totalUsageQuantity: "total_usage_quantity",
    billingPeriodStartsAt: "billing_period_starts_at",
    billingPeriodEndsAt: "billing_period_ends_at",
  },
});
