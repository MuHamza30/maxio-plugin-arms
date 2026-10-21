import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { amount5Schema, type Amount5 } from "./unions/amount5.js";

export type RefundPrepayment = {
  /** `amount` is not required if you pass `amount_in_cents`. */
  amountInCents: number | null;
  /** `amount_in_cents` is not required if you pass `amount`. */
  amount: Amount5;
  memo: string;
  /**
   * Specify the type of refund you wish to initiate. When the prepayment is external, the
   * `external` flag is optional. But if the prepayment was made through a payment profile, the
   * `external` flag is required.
   */
  external?: boolean;
};

export const refundPrepaymentSchema: Schema<RefundPrepayment> = s.object<RefundPrepayment>({
  amountInCents: s.nullable(s.int()),
  amount: amount5Schema,
  memo: s.string(),
  external: s.optional(s.boolean()),
  _keysMap: {
    amountInCents: "amount_in_cents",
  },
});
