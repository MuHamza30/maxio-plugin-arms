import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type CreditAccountBalanceChanged = {
  reason: string;
  serviceCreditAccountBalanceInCents: number;
  serviceCreditBalanceChangeInCents: number;
  currencyCode: string;
  atTime: Date;
};

export const creditAccountBalanceChangedSchema: Schema<CreditAccountBalanceChanged> =
  s.object<CreditAccountBalanceChanged>({
    reason: s.string(),
    serviceCreditAccountBalanceInCents: s.int(),
    serviceCreditBalanceChangeInCents: s.int(),
    currencyCode: s.string(),
    atTime: s.dateTime(),
    _keysMap: {
      serviceCreditAccountBalanceInCents: "service_credit_account_balance_in_cents",
      serviceCreditBalanceChangeInCents: "service_credit_balance_change_in_cents",
      currencyCode: "currency_code",
      atTime: "at_time",
    },
  });
