import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { meterSchema, type Meter } from "./meter.js";
import { ownerTypeSchema, type OwnerType } from "./owner-type.js";
import { walletGrantSchema, type WalletGrant } from "./wallet-grant.js";
import { walletHardStopOverflowSchema, type WalletHardStopOverflow } from "./wallet-hard-stop-overflow.js";
import { walletOriginSchema, type WalletOrigin } from "./wallet-origin.js";
import { walletRecurringFundingSchema, type WalletRecurringFunding } from "./wallet-recurring-funding.js";
import { walletStatusSchema, type WalletStatus } from "./wallet-status.js";

/**
 * A balance, denominated in the unit of a Wallet Product, owned by a subscription. Grants and
 * recurring funding schedules are embedded so a single read shows the full balance breakdown.
 */
export type Wallet = {
  /** The Advanced Billing id of the wallet. */
  id?: number;
  /** The polymorphic owner type. `subscription` is the only value currently supported. */
  ownerType?: OwnerType;
  /** The id of the owning subscription. */
  ownerId?: number;
  /**
   * (Optional) A merchant-facing label for the wallet, set on create and changeable with [Update
   * Wallet]($e/Wallets/updateWallet). Surrounding spaces are stripped; a blank value is stored as
   * `null`.
   */
  name?: string | null;
  /**
   * The id of the [Wallet Product]($e/Wallet%20Products/createWalletProduct) that denominates the
   * wallet. Immutable for the life of the wallet.
   */
  walletProductId?: number;
  /** The name of the Wallet Product that denominates the wallet. */
  walletProductName?: string;
  /** The billing product's unit name, immutable for the life of the wallet. */
  unit?: string;
  /**
   * The price point that priced this wallet's
   * [purchases]($e/Wallet%20Purchases/createWalletPurchase), set on create and immutable afterward.
   * Defaults to the Wallet Product's default price point; `null` if the Wallet Product has none and
   * none was given on create.
   */
  pricePointId?: number | null;
  /**
   * What the wallet can spend now, encoded as a decimal string to avoid floating-point precision
   * loss. This is the number to enforce against. For a metered wallet, it includes usage not yet
   * posted to the ledger, through `metered_through_at`, but only in the response from [Read
   * Wallet]($e/Wallets/readWallet); every other response (list, create, update, archive) reports
   * the balance as of the last ledger write, equal to `posted_balance`, even for a metered wallet.
   * The grants' `remaining` follow this figure, so they add up to it whenever it is zero or more.
   */
  balance?: string;
  /**
   * The balance from written ledger entries alone: grants funded, minus debits written to the
   * ledger, as a decimal string. Always present, also for a wallet with no meter. It equals
   * `balance` wherever no live metered balance is computed: list, create, update, and archive
   * responses, an unlinked or archived wallet, and a read where `metered_stale` is `true`. Only an
   * active, metered wallet read through [Read Wallet]($e/Wallets/readWallet), with `metered_stale`
   * not `true`, can have a `balance` below its `posted_balance`. It stays exact when
   * `metered_stale` is `true`. Reconcile the transactions list (`balance_after`) against this
   * figure, not against `balance`.
   */
  postedBalance?: string;
  /**
   * The metering meter this wallet is paired with, or `null` for a wallet with no meter. Set on
   * create and immutable afterward.
   */
  meter?: Meter | null;
  /**
   * The point up to which live meter usage has been factored into `balance`. Populated only in the
   * response from [Read Wallet]($e/Wallets/readWallet), for an active, metered wallet on a site
   * with metered consumption enabled; `null` everywhere else, including list, create, update, and
   * archive responses for the same wallet.
   */
  meteredThroughAt?: Date | null;
  /**
   * How many seconds to wait before re-reading `balance` to see usage past `metered_through_at`.
   * Same availability as `metered_through_at`.
   */
  meteredRecheckAfterSeconds?: number | null;
  /**
   * `true` when live usage could not be read fresh and `balance` reflects an earlier snapshot. Same
   * availability as `metered_through_at`.
   */
  meteredStale?: boolean | null;
  status?: WalletStatus;
  /**
   * What happens when a debit would take the wallet below zero. Known values: `hard_stop` (the only
   * value you can set today). More values are expected over time, so treat this as an open string
   * and don't fail on one you don't recognize. At the zero boundary, `hard_stop` behaves as set by
   * `hard_stop_overflow`.
   */
  depletionPolicy?: string;
  /**
   * Behavior at the hard-stop boundary. `discard` drains the wallet to zero and rejects the excess
   * (the default). `allow_negative` deducts the full amount, letting the balance go negative. The
   * excess past the wallet's grants is booked as an overdraft ledger row with `grant_id` set to
   * `null`.
   */
  hardStopOverflow?: WalletHardStopOverflow;
  /**
   * How the wallet came to exist. `manual` for a wallet created directly with [Create
   * Wallet]($e/Wallets/createWallet). `feature` for a wallet auto-provisioned because a
   * subscription resolved a usage-limit entitlement whose Feature has `wallet_behavior` configured.
   */
  origin?: WalletOrigin;
  /**
   * The key of the Feature this wallet was provisioned for, when `origin` is `feature`. `null` for
   * a `manual` wallet.
   */
  featureKey?: string | null;
  /**
   * Every grant on the wallet, including ones already spent or expired, in drain order (the order
   * debits would consume the still-open ones in): the soonest-expiring grant first, evergreen
   * grants last.
   */
  grants?: WalletGrant[];
  /**
   * The wallet's automatic funding schedules, if any. Empty for a `manual` wallet with no funding
   * entitlement. A wallet funds automatically when it's provisioned from a Feature with
   * `wallet_behavior` configured; see [the Wallets concept
   * guide](page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature).
   */
  recurringFunding?: WalletRecurringFunding[];
  createdAt?: Date;
  updatedAt?: Date;
};

export const walletSchema: Schema<Wallet> = s.object<Wallet>({
  id: s.optional(s.int()),
  ownerType: s.optional(s.lazy(() => ownerTypeSchema)),
  ownerId: s.optional(s.int()),
  name: s.optionalNullable(s.string()),
  walletProductId: s.optional(s.int()),
  walletProductName: s.optional(s.string()),
  unit: s.optional(s.string()),
  pricePointId: s.optionalNullable(s.int()),
  balance: s.optional(s.string()),
  postedBalance: s.optional(s.string()),
  meter: s.optionalNullable(s.lazy(() => meterSchema)),
  meteredThroughAt: s.optionalNullable(s.dateTime()),
  meteredRecheckAfterSeconds: s.optionalNullable(s.int()),
  meteredStale: s.optionalNullable(s.boolean()),
  status: s.optional(s.lazy(() => walletStatusSchema)),
  depletionPolicy: s.optional(s.string()),
  hardStopOverflow: s.optional(s.lazy(() => walletHardStopOverflowSchema)),
  origin: s.optional(s.lazy(() => walletOriginSchema)),
  featureKey: s.optionalNullable(s.string()),
  grants: s.optional(s.array(s.lazy(() => walletGrantSchema))),
  recurringFunding: s.optional(s.array(s.lazy(() => walletRecurringFundingSchema))),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  _keysMap: {
    ownerType: "owner_type",
    ownerId: "owner_id",
    walletProductId: "wallet_product_id",
    walletProductName: "wallet_product_name",
    pricePointId: "price_point_id",
    postedBalance: "posted_balance",
    meteredThroughAt: "metered_through_at",
    meteredRecheckAfterSeconds: "metered_recheck_after_seconds",
    meteredStale: "metered_stale",
    depletionPolicy: "depletion_policy",
    hardStopOverflow: "hard_stop_overflow",
    featureKey: "feature_key",
    recurringFunding: "recurring_funding",
    createdAt: "created_at",
    updatedAt: "updated_at",
  },
});
