import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { payerErrorSchema, type PayerError } from "./payer-error.js";
import {
  subscriptionGroupSubscriptionErrorSchema,
  type SubscriptionGroupSubscriptionError,
} from "./subscription-group-subscription-error.js";

export type SubscriptionGroupSignupError = {
  /**
   * Object that as key have subscription position in request subscriptions array and as value
   * subscription errors object.
   */
  subscriptions?: Record<string, SubscriptionGroupSubscriptionError>;
  payerReference?: string;
  payer?: PayerError;
  subscriptionGroup?: string[];
  paymentProfileId?: string;
  payerId?: string;
};

export const subscriptionGroupSignupErrorSchema: Schema<SubscriptionGroupSignupError> =
  s.object<SubscriptionGroupSignupError>({
    subscriptions: s.optional(
      s.record(
        s.string(),
        s.lazy(() => subscriptionGroupSubscriptionErrorSchema),
      ),
    ),
    payerReference: s.optional(s.string()),
    payer: s.optional(s.lazy(() => payerErrorSchema)),
    subscriptionGroup: s.optional(s.array(s.string())),
    paymentProfileId: s.optional(s.string()),
    payerId: s.optional(s.string()),
    _keysMap: {
      payerReference: "payer_reference",
      subscriptionGroup: "subscription_group",
      paymentProfileId: "payment_profile_id",
      payerId: "payer_id",
    },
  });
