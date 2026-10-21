import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { prepaymentMethodSchema, type PrepaymentMethod } from "./prepayment-method.js";

export type ListSubscriptionGroupPrepaymentItem = {
  id?: number;
  subscriptionGroupUid?: string;
  amountInCents?: number;
  remainingAmountInCents?: number;
  details?: string;
  external?: boolean;
  memo?: string;
  paymentType?: PrepaymentMethod;
  createdAt?: Date;
};

export const listSubscriptionGroupPrepaymentItemSchema: Schema<ListSubscriptionGroupPrepaymentItem> =
  s.object<ListSubscriptionGroupPrepaymentItem>({
    id: s.optional(s.int()),
    subscriptionGroupUid: s.optional(s.string()),
    amountInCents: s.optional(s.int()),
    remainingAmountInCents: s.optional(s.int()),
    details: s.optional(s.string()),
    external: s.optional(s.boolean()),
    memo: s.optional(s.string()),
    paymentType: s.optional(s.lazy(() => prepaymentMethodSchema)),
    createdAt: s.optional(s.dateTime()),
    _keysMap: {
      subscriptionGroupUid: "subscription_group_uid",
      amountInCents: "amount_in_cents",
      remainingAmountInCents: "remaining_amount_in_cents",
      paymentType: "payment_type",
      createdAt: "created_at",
    },
  });
