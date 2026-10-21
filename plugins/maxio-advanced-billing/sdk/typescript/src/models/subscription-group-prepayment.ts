import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  subscriptionGroupPrepaymentMethodSchema,
  type SubscriptionGroupPrepaymentMethod,
} from "./subscription-group-prepayment-method.js";

export type SubscriptionGroupPrepayment = {
  amount: number;
  details: string;
  memo: string;
  method: SubscriptionGroupPrepaymentMethod;
};

export const subscriptionGroupPrepaymentSchema: Schema<SubscriptionGroupPrepayment> =
  s.object<SubscriptionGroupPrepayment>({
    amount: s.int(),
    details: s.string(),
    memo: s.string(),
    method: subscriptionGroupPrepaymentMethodSchema,
  });
