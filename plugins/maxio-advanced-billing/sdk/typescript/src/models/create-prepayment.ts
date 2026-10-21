import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { createPrepaymentMethodSchema, type CreatePrepaymentMethod } from "./create-prepayment-method.js";

export type CreatePrepayment = {
  amount: number;
  details: string;
  memo: string;
  /**
   * When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected
   * using the default credit card payment profile and applied to the prepayment account balance.
   * This is especially useful for manual replenishment of prepaid subscriptions.
   */
  method: CreatePrepaymentMethod;
  paymentProfileId?: number;
};

export const createPrepaymentSchema: Schema<CreatePrepayment> = s.object<CreatePrepayment>({
  amount: s.float64(),
  details: s.string(),
  memo: s.string(),
  method: createPrepaymentMethodSchema,
  paymentProfileId: s.optional(s.int()),
  _keysMap: {
    paymentProfileId: "payment_profile_id",
  },
});
