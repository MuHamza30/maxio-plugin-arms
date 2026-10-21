import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { reactivationBillingSchema, type ReactivationBilling } from "./reactivation-billing.js";
import { resumeSchema, type Resume } from "./unions/resume.js";

export type ReactivateSubscriptionRequest = {
  /** These values are only applicable to subscriptions using calendar billing. */
  calendarBilling?: ReactivationBilling;
  /**
   * If `true` is sent, the reactivated Subscription will include a trial if one is available. If
   * `false` is sent, the trial period will be ignored.
   */
  includeTrial?: boolean;
  /**
   * If `true` is passed, the existing subscription balance will NOT be cleared/reset before adding
   * the additional reactivation charges.
   */
  preserveBalance?: boolean;
  /** The coupon code to be applied during reactivation. */
  couponCode?: string;
  /**
   * If true is sent, Advanced Billing will use service credits and prepayments upon reactivation.
   * If false is sent, the service credits and prepayments will be ignored.
   */
  useCreditsAndPrepayments?: boolean;
  /**
   * If `true`, Advanced Billing will attempt to resume the subscription's billing period. If not
   * resumable, the subscription will be reactivated with a new billing period. If `false` or
   * omitted, Advanced Billing will only attempt to reactivate the subscription with a new billing
   * period, regardless of whether or not the subscription is resumable.
   */
  resume?: Resume;
};

export const reactivateSubscriptionRequestSchema: Schema<ReactivateSubscriptionRequest> =
  s.object<ReactivateSubscriptionRequest>({
    calendarBilling: s.optional(s.lazy(() => reactivationBillingSchema)),
    includeTrial: s.optional(s.boolean()),
    preserveBalance: s.optional(s.boolean()),
    couponCode: s.optional(s.string()),
    useCreditsAndPrepayments: s.optional(s.boolean()),
    resume: s.optional(s.lazy(() => resumeSchema)),
    _keysMap: {
      calendarBilling: "calendar_billing",
      includeTrial: "include_trial",
      preserveBalance: "preserve_balance",
      couponCode: "coupon_code",
      useCreditsAndPrepayments: "use_credits_and_prepayments",
    },
  });
