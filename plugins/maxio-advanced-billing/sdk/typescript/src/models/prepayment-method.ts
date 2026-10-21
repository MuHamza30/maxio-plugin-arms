import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

export const PrepaymentMethod = {
  Check: "check",
  Cash: "cash",
  MoneyOrder: "money_order",
  Ach: "ach",
  PaypalAccount: "paypal_account",
  CreditCard: "credit_card",
  Other: "other",
} as const;
export type PrepaymentMethod = (typeof PrepaymentMethod)[keyof typeof PrepaymentMethod] | (string & {});

export const prepaymentMethodSchema: EnumSchema<PrepaymentMethod> =
  s.enumOf<PrepaymentMethod>(PrepaymentMethod);
