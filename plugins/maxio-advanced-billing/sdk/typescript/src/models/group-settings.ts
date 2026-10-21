import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { groupBillingSchema, type GroupBilling } from "./group-billing.js";
import { groupTargetSchema, type GroupTarget } from "./group-target.js";

export type GroupSettings = {
  /**
   * Attributes of the target customer who will be the responsible payer of the created
   * subscription. Required.
   */
  target: GroupTarget;
  /**
   * (Optional) Attributes related to billing date and accrual. Note: Only applicable for new
   * subscriptions.
   */
  billing?: GroupBilling;
};

export const groupSettingsSchema: Schema<GroupSettings> = s.object<GroupSettings>({
  target: groupTargetSchema,
  billing: s.optional(s.lazy(() => groupBillingSchema)),
});
