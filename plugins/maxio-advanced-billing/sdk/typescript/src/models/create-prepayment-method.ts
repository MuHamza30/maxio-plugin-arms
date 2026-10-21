import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected
 * using the default credit card payment profile and applied to the prepayment account balance. This
 * is especially useful for manual replenishment of prepaid subscriptions.
 */
export const CreatePrepaymentMethod = {
  Check: "check",
  Cash: "cash",
  MoneyOrder: "money_order",
  Ach: "ach",
  PaypalAccount: "paypal_account",
  CreditCard: "credit_card",
  CreditCardOnFile: "credit_card_on_file",
  Other: "other",
} as const;
export type CreatePrepaymentMethod =
  | (typeof CreatePrepaymentMethod)[keyof typeof CreatePrepaymentMethod]
  | (string & {});

export const createPrepaymentMethodSchema: EnumSchema<CreatePrepaymentMethod> =
  s.enumOf<CreatePrepaymentMethod>(CreatePrepaymentMethod);
