import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PrepaymentAccountBalanceChanged = {
  reason: string;
  prepaymentAccountBalanceInCents: number;
  prepaymentBalanceChangeInCents: number;
  currencyCode: string;
};

export const prepaymentAccountBalanceChangedSchema: Schema<PrepaymentAccountBalanceChanged> =
  s.object<PrepaymentAccountBalanceChanged>({
    reason: s.string(),
    prepaymentAccountBalanceInCents: s.int(),
    prepaymentBalanceChangeInCents: s.int(),
    currencyCode: s.string(),
    _keysMap: {
      prepaymentAccountBalanceInCents: "prepayment_account_balance_in_cents",
      prepaymentBalanceChangeInCents: "prepayment_balance_change_in_cents",
      currencyCode: "currency_code",
    },
  });
