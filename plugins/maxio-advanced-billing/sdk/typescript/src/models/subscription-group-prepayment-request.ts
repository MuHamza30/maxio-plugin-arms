import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionGroupPrepaymentSchema,
  type SubscriptionGroupPrepayment,
} from "./subscription-group-prepayment.js";

export type SubscriptionGroupPrepaymentRequest = {
  prepayment: SubscriptionGroupPrepayment;
};

export const subscriptionGroupPrepaymentRequestSchema: Schema<SubscriptionGroupPrepaymentRequest> =
  s.object<SubscriptionGroupPrepaymentRequest>({
    prepayment: subscriptionGroupPrepaymentSchema,
  });
