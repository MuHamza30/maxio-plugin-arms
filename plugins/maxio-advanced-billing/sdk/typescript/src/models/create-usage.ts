import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { billingScheduleSchema, type BillingSchedule } from "./billing-schedule.js";
import { componentCustomPriceSchema, type ComponentCustomPrice } from "./component-custom-price.js";

export type CreateUsage = {
  /** integer by default or decimal number if fractional quantities are enabled for the component */
  quantity?: number;
  pricePointId?: string;
  memo?: string;
  /**
   * Billing schedule settings for component allocations or usages on multi-frequency subscriptions.
   * Use this to start a component's billing period on a custom date instead of aligning with the
   * product charge schedule.
   */
  billingSchedule?: BillingSchedule;
  /**
   * Create or update custom pricing unique to the subscription. Used in place of `price_point_id`.
   */
  customPrice?: ComponentCustomPrice;
};

export const createUsageSchema: Schema<CreateUsage> = s.object<CreateUsage>({
  quantity: s.optional(s.float64()),
  pricePointId: s.optional(s.string()),
  memo: s.optional(s.string()),
  billingSchedule: s.optional(s.lazy(() => billingScheduleSchema)),
  customPrice: s.optional(s.lazy(() => componentCustomPriceSchema)),
  _keysMap: {
    pricePointId: "price_point_id",
    billingSchedule: "billing_schedule",
    customPrice: "custom_price",
  },
});
