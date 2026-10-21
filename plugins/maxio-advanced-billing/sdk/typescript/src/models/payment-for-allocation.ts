import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** Information for captured payment, if applicable */
export type PaymentForAllocation = {
  id?: number;
  amountInCents?: number;
  success?: boolean;
  memo?: string;
};

export const paymentForAllocationSchema: Schema<PaymentForAllocation> = s.object<PaymentForAllocation>({
  id: s.optional(s.int()),
  amountInCents: s.optional(s.int()),
  success: s.optional(s.boolean()),
  memo: s.optional(s.string()),
  _keysMap: {
    amountInCents: "amount_in_cents",
  },
});
