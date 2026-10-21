import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { originSchema, type Origin } from "./origin.js";

/**
 * A funding tranche embedded on the wallet. `original` is the amount the grant was created with;
 * `posted_remaining` is what debits and adjustments written to the ledger have left; `remaining` is
 * what can still be spent. Debits drain grants earliest-expiration-first (grants with no expiration
 * are drained last).
 */
export type WalletGrant = {
  /** The Advanced Billing id of the grant. */
  id?: number;
  /** The memo the grant was created with, or `Grant */
  name?: string;
  /**
   * The amount the grant was created with, encoded as a decimal string. Never changes after
   * creation.
   */
  original?: string;
  /**
   * What the grant can still spend, encoded as a decimal string. On [Read
   * Wallet]($e/Wallets/readWallet) for a metered wallet whose `balance` is the live figure, this is
   * `posted_remaining` less the pending usage drawn from this grant in drain order: usage past a
   * grant spills to the next one, and usage past every grant is an overdraft that belongs to no
   * grant. It never goes below zero, and the grants' `remaining` add up to the wallet's `balance`
   * whenever `balance` is zero or more. Everywhere else it equals `posted_remaining`.
   */
  remaining?: string;
  /**
   * The grant's remainder from written ledger entries alone, encoded as a decimal string. Always
   * present. This is the figure an adjustment checks `expected_remaining` and its bounds against,
   * so send it back, not `remaining`, when correcting a grant.
   */
  postedRemaining?: string;
  /**
   * When this grant's unconsumed remainder is automatically written off. `null` for an evergreen
   * grant.
   */
  expiresAt?: Date | null;
  /** The calendar day `expires_at` falls on, already resolved in the site's time zone. */
  expiresOn?: string | null;
  /**
   * When the expiry sweep actually wrote this grant's remainder off. Usually falls shortly after
   * `expires_at`; use `expires_on` for the date the grant expired, not this field. `null` if the
   * grant was never written off (including a grant simply spent to zero before its `expires_at`).
   */
  expiredAt?: Date | null;
  /** The calendar day `expired_at` falls on, resolved in the site's time zone. */
  expiredOn?: string | null;
  /**
   * How the grant was created. `recurring` comes from the wallet's automatic funding schedule (see
   * the wallet's `recurring_funding` array). `manual` comes from a one-time grant posted to [Create
   * Wallet Transaction]($e/Wallet%20Transactions/createWalletTransaction). `initial_balance` comes
   * from a non-zero `initial_balance` at wallet creation. `allowance_increase` comes from raising a
   * funding entitlement's allowance while it's already funding a wallet. `purchase` comes from
   * [Create Wallet Purchase]($e/Wallet%20Purchases/createWalletPurchase).
   */
  origin?: Origin;
  /**
   * For a `recurring` grant, the start of the funding cadence period this grant covers. `null` for
   * every other origin. After a gap in funding (see `skipped_periods`), this is the period
   * currently in progress, not the oldest period that was missed.
   */
  grantedForPeriodStart?: Date | null;
  /**
   * The uid of the invoice that paid for this grant, for a grant with `origin` of `purchase`.
   * `null` for every other origin.
   */
  invoiceUid?: string | null;
  createdAt?: Date;
};

export const walletGrantSchema: Schema<WalletGrant> = s.object<WalletGrant>({
  id: s.optional(s.int()),
  name: s.optional(s.string()),
  original: s.optional(s.string()),
  remaining: s.optional(s.string()),
  postedRemaining: s.optional(s.string()),
  expiresAt: s.optionalNullable(s.dateTime()),
  expiresOn: s.optionalNullable(s.dateOnly()),
  expiredAt: s.optionalNullable(s.dateTime()),
  expiredOn: s.optionalNullable(s.dateOnly()),
  origin: s.optional(s.lazy(() => originSchema)),
  grantedForPeriodStart: s.optionalNullable(s.dateTime()),
  invoiceUid: s.optionalNullable(s.string()),
  createdAt: s.optional(s.dateTime()),
  _keysMap: {
    postedRemaining: "posted_remaining",
    expiresAt: "expires_at",
    expiresOn: "expires_on",
    expiredAt: "expired_at",
    expiredOn: "expired_on",
    grantedForPeriodStart: "granted_for_period_start",
    invoiceUid: "invoice_uid",
    createdAt: "created_at",
  },
});
