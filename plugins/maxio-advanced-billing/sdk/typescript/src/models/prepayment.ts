import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { prepaymentMethodSchema, type PrepaymentMethod } from "./prepayment-method.js";

export type Prepayment = {
  id: number;
  subscriptionId: number;
  amountInCents: number;
  remainingAmountInCents: number;
  refundedAmountInCents?: number;
  details?: string;
  external: boolean;
  memo: string;
  /** The payment type of the prepayment. */
  paymentType?: PrepaymentMethod;
  createdAt: Date;
};

export const prepaymentSchema: Schema<Prepayment> = s.object<Prepayment>({
  id: s.int(),
  subscriptionId: s.int(),
  amountInCents: s.int(),
  remainingAmountInCents: s.int(),
  refundedAmountInCents: s.optional(s.int()),
  details: s.optional(s.string()),
  external: s.boolean(),
  memo: s.string(),
  paymentType: s.optional(s.lazy(() => prepaymentMethodSchema)),
  createdAt: s.dateTime(),
  _keysMap: {
    subscriptionId: "subscription_id",
    amountInCents: "amount_in_cents",
    remainingAmountInCents: "remaining_amount_in_cents",
    refundedAmountInCents: "refunded_amount_in_cents",
    paymentType: "payment_type",
    createdAt: "created_at",
  },
});
