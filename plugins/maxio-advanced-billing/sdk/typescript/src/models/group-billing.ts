import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * (Optional) Attributes related to billing date and accrual. Note: Only applicable for new
 * subscriptions.
 */
export type GroupBilling = {
  /** A flag indicating whether or not to accrue charges on the new subscription. @default false */
  accrue?: boolean;
  /**
   * A flag indicating whether or not to align the billing date of the new subscription with the
   * billing date of the primary subscription of the hierarchy's default subscription group.
   * Required to be true if prorate is also true.
   *
   * @default false
   */
  alignDate?: boolean;
  /**
   * A flag indicating whether or not to prorate billing of the new subscription for the current
   * period. A value of true is ignored unless align_date is also true.
   *
   * @default false
   */
  prorate?: boolean;
};

export const groupBillingSchema: Schema<GroupBilling> = s.object<GroupBilling>({
  accrue: s.defaulted(s.boolean(), false),
  alignDate: s.defaulted(s.boolean(), false),
  prorate: s.defaulted(s.boolean(), false),
  _keysMap: {
    alignDate: "align_date",
  },
});
