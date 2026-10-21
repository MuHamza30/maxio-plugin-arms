import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type OverrideSubscription = {
  /**
   * Can be used to record an external signup date. Chargify uses this field to record when a
   * subscription first goes active (either at signup or at trial end). Only ISO8601 format is
   * supported.
   */
  activatedAt?: Date;
  /**
   * Can be used to record an external cancellation date. Chargify sets this field automatically
   * when a subscription is canceled, whether by request or via dunning. Only ISO8601 format is
   * supported.
   */
  canceledAt?: Date;
  /** Can be used to record a reason for the original cancellation. */
  cancellationMessage?: string;
  /**
   * Can be used to record an external expiration date. Chargify sets this field automatically when
   * a subscription expires (ceases billing) after a prescribed amount of time. Only ISO8601 format
   * is supported. This field is not supported when Multi-frequency is enabled for the Site. To
   * change the Term End of a Subscription, use the Update Subscription endpoint.
   */
  expiresAt?: Date;
  /**
   * Can only be used when a subscription is unbilled, which happens when a future initial billing
   * date is passed at subscription creation. The value passed must be before the current date and
   * time. Allows you to set when the period started so mid period component allocations have the
   * correct proration. Only ISO8601 format is supported.
   */
  currentPeriodStartsAt?: Date;
};

export const overrideSubscriptionSchema: Schema<OverrideSubscription> = s.object<OverrideSubscription>({
  activatedAt: s.optional(s.dateTime()),
  canceledAt: s.optional(s.dateTime()),
  cancellationMessage: s.optional(s.string()),
  expiresAt: s.optional(s.dateTime()),
  currentPeriodStartsAt: s.optional(s.dateTime()),
  _keysMap: {
    activatedAt: "activated_at",
    canceledAt: "canceled_at",
    cancellationMessage: "cancellation_message",
    expiresAt: "expires_at",
    currentPeriodStartsAt: "current_period_starts_at",
  },
});
