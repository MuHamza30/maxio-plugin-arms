import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CancellationOptions = {
  /** An indication as to why the subscription is being canceled. For your internal use. */
  cancellationMessage?: string;
  /**
   * The reason code associated with the cancellation. Use the [List Reason
   * Codes]($e/Reason%20Codes/listReasonCodes) endpoint to retrieve the reason codes associated with
   * your site.
   */
  reasonCode?: string;
  /**
   * When true, the subscription is cancelled at the current period end instead of immediately. To
   * use this option, the Schedule Subscription Cancellation feature must be enabled on your site.
   */
  cancelAtEndOfPeriod?: boolean;
  /**
   * Schedules the cancellation on the provided date. This option is not applicable for prepaid
   * subscriptions. To use this option, the Schedule Subscription Cancellation feature must be
   * enabled on your site.
   */
  scheduledCancellationAt?: Date | null;
  /**
   * Applies to prepaid subscriptions. When true, which is the default, the remaining prepaid
   * balance is refunded as part of cancellation processing. When false, prepaid balance is not
   * refunded as part of cancellation processing. To use this option, the Schedule Subscription
   * Cancellation feature must be enabled on your site.
   */
  refundPrepaymentAccountBalance?: boolean;
};

export const cancellationOptionsSchema: Schema<CancellationOptions> = s.object<CancellationOptions>({
  cancellationMessage: s.optional(s.string()),
  reasonCode: s.optional(s.string()),
  cancelAtEndOfPeriod: s.optional(s.boolean()),
  scheduledCancellationAt: s.optionalNullable(s.dateTime()),
  refundPrepaymentAccountBalance: s.optional(s.boolean()),
  _keysMap: {
    cancellationMessage: "cancellation_message",
    reasonCode: "reason_code",
    cancelAtEndOfPeriod: "cancel_at_end_of_period",
    scheduledCancellationAt: "scheduled_cancellation_at",
    refundPrepaymentAccountBalance: "refund_prepayment_account_balance",
  },
});
