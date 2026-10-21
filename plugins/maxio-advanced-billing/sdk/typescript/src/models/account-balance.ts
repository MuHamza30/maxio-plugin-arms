import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type AccountBalance = {
  /** The balance in cents. */
  balanceInCents?: number;
  /** The automatic balance in cents. */
  automaticBalanceInCents?: number | null;
  /** The remittance balance in cents. */
  remittanceBalanceInCents?: number | null;
};

export const accountBalanceSchema: Schema<AccountBalance> = s.object<AccountBalance>({
  balanceInCents: s.optional(s.int()),
  automaticBalanceInCents: s.optionalNullable(s.int()),
  remittanceBalanceInCents: s.optionalNullable(s.int()),
  _keysMap: {
    balanceInCents: "balance_in_cents",
    automaticBalanceInCents: "automatic_balance_in_cents",
    remittanceBalanceInCents: "remittance_balance_in_cents",
  },
});
