import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * Billing schedule settings for component allocations or usages on multi-frequency subscriptions.
 * Use this to start a component's billing period on a custom date instead of aligning with the
 * product charge schedule.
 */
export type BillingSchedule = {
  /**
   * Custom start date (ISO 8601 date, YYYY-MM-DD) for the component's first billing period. If
   * omitted or null, billing aligns with the product schedule. If provided, date must be on or
   * after the minimum allowed date for the subscription or component.
   */
  initialBillingAt?: string | null;
};

export const billingScheduleSchema: Schema<BillingSchedule> = s.object<BillingSchedule>({
  initialBillingAt: s.optionalNullable(s.dateOnly()),
  _keysMap: {
    initialBillingAt: "initial_billing_at",
  },
});
