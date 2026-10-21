import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PrepaidSubscriptionBalanceChanged = {
  reason: string;
  currentAccountBalanceInCents: number;
  prepaymentAccountBalanceInCents: number;
  currentUsageAmountInCents: number;
};

export const prepaidSubscriptionBalanceChangedSchema: Schema<PrepaidSubscriptionBalanceChanged> =
  s.object<PrepaidSubscriptionBalanceChanged>({
    reason: s.string(),
    currentAccountBalanceInCents: s.int(),
    prepaymentAccountBalanceInCents: s.int(),
    currentUsageAmountInCents: s.int(),
    _keysMap: {
      currentAccountBalanceInCents: "current_account_balance_in_cents",
      prepaymentAccountBalanceInCents: "prepayment_account_balance_in_cents",
      currentUsageAmountInCents: "current_usage_amount_in_cents",
    },
  });
