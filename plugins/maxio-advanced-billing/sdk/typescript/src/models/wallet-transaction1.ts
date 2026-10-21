import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { kind1Schema, type Kind1 } from "./kind1.js";
import { amount6Schema, type Amount6 } from "./unions/amount6.js";

export type WalletTransaction1 = {
  /** Determines the direction of the movement. The amount itself is always sent positive. */
  kind: Kind1;
  /**
   * Always positive; `kind` determines the sign written to the ledger. Encoded as a decimal string
   * with at most 8 fractional digits. Send fractional values as strings: a JSON number with a
   * decimal point is rejected with `422`, because a double-precision float may already have lost
   * precision before the request arrives.
   */
  amount: Amount6;
  memo?: string | null;
  /**
   * An expiration for the grant this creates. Only accepted with `kind: grant`; sending it with
   * `kind: debit` is rejected. Omit it for an evergreen grant. Accepts either a bare calendar date
   * (`YYYY-MM-DD`), resolved to the end of that day in the site's time zone, or a full timestamp. A
   * calendar day that doesn't exist, such as `2027-02-30`, is rejected with `422` rather than
   * rolled into the next month.
   */
  expiresAt?: string | null;
};

export const walletTransaction1Schema: Schema<WalletTransaction1> = s.object<WalletTransaction1>({
  kind: kind1Schema,
  amount: amount6Schema,
  memo: s.optionalNullable(s.string()),
  expiresAt: s.optionalNullable(s.string()),
  _keysMap: {
    expiresAt: "expires_at",
  },
});
