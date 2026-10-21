import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { conversionRateSchema, type ConversionRate } from "./unions/conversion-rate.js";
import { initialBalanceSchema, type InitialBalance } from "./unions/initial-balance.js";
import { walletProductIdSchema, type WalletProductId } from "./unions/wallet-product-id.js";
import { walletHardStopOverflowSchema, type WalletHardStopOverflow } from "./wallet-hard-stop-overflow.js";

export type Wallet1 = {
  /** The subscription that will own the wallet. */
  subscriptionId: number;
  /**
   * The [Wallet Product]($e/Wallet%20Products/createWalletProduct) that will denominate the wallet:
   * its numeric id, or its handle prefixed with `handle:` (for example `handle:token-pack`). A bare
   * handle with no prefix is looked up as an id and returns `404`. Immutable once the wallet is
   * created.
   */
  walletProductId: WalletProductId;
  /**
   * (Optional) A merchant-facing label for the wallet. Surrounding spaces are stripped; a blank
   * value is stored as `null`.
   */
  name?: string | null;
  /** Defaults to `hard_stop`, currently the only supported value. */
  depletionPolicy?: string;
  /** Defaults to `discard`. */
  hardStopOverflow?: WalletHardStopOverflow;
  /**
   * Pairs the wallet with a merchant-owned metering meter, so its balance factors in live usage
   * (see the wallet resource's `meter` and `metered_through_at` fields). Only a `sum` or `count`
   * meter can be paired. Requires metered wallet consumption to be enabled for the site, checked
   * whenever this or `conversion_rate` is sent: `403` (plain text, not JSON) if it isn't. A meter
   * id that doesn't resolve to a merchant-owned meter on this site, including a system-maintained
   * shadow meter, is `404`. Immutable once the wallet is created.
   */
  meterId?: number;
  /**
   * How many wallet units one meter unit is worth, as a decimal string with at most 8 fractional
   * digits, greater than `0` and below 10^16. Send fractional values as strings: a JSON number with
   * a decimal point is rejected with `422`, because a double-precision float may already have lost
   * precision before the request arrives. Only meaningful with `meter_id`. Defaults to `"1.0"`.
   * Immutable once the wallet is created.
   */
  conversionRate?: ConversionRate;
  /**
   * The price point used to price [Create Wallet
   * Purchase]($e/Wallet%20Purchases/createWalletPurchase) calls against this wallet. Must belong to
   * the Wallet Product, and can't be archived or a subscription-specific custom price point.
   * Defaults to the Wallet Product's default price point. Immutable once the wallet is created.
   */
  pricePointId?: number;
  /**
   * (Optional) A free opening balance, not a purchase and not reflected on any invoice. When
   * non-zero, wallet creation also writes an initial-balance grant and a matching `initial_balance`
   * ledger row. Omitted or exactly `0` creates a zero-balance wallet, not an error. Encoded as a
   * decimal string with at most 8 fractional digits, and must be non-negative and below 10^16. Send
   * fractional values as strings: a JSON number with a decimal point is rejected with `422`,
   * because a double-precision float may already have lost precision before the request arrives.
   */
  initialBalance?: InitialBalance;
  /**
   * An expiration for the initial-balance grant. Only accepted together with a non-zero
   * `initial_balance`, and must be in the future. Accepts either a bare calendar date
   * (`YYYY-MM-DD`), resolved to the end of that day in the site's time zone, or a full timestamp. A
   * calendar day that doesn't exist, such as `2027-02-30`, is rejected with `422` rather than
   * rolled into the next month.
   */
  initialBalanceExpiresAt?: string | null;
};

export const wallet1Schema: Schema<Wallet1> = s.object<Wallet1>({
  subscriptionId: s.int(),
  walletProductId: walletProductIdSchema,
  name: s.optionalNullable(s.string()),
  depletionPolicy: s.optional(s.string()),
  hardStopOverflow: s.optional(s.lazy(() => walletHardStopOverflowSchema)),
  meterId: s.optional(s.int()),
  conversionRate: s.optional(s.lazy(() => conversionRateSchema)),
  pricePointId: s.optional(s.int()),
  initialBalance: s.optional(s.lazy(() => initialBalanceSchema)),
  initialBalanceExpiresAt: s.optionalNullable(s.string()),
  _keysMap: {
    subscriptionId: "subscription_id",
    walletProductId: "wallet_product_id",
    depletionPolicy: "depletion_policy",
    hardStopOverflow: "hard_stop_overflow",
    meterId: "meter_id",
    conversionRate: "conversion_rate",
    pricePointId: "price_point_id",
    initialBalance: "initial_balance",
    initialBalanceExpiresAt: "initial_balance_expires_at",
  },
});
