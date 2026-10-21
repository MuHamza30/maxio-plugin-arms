import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * Set whenever `status` isn't `active`. Accompanying `stopped`: `entitlement_missing` (an ordinary
 * product or component change removed the entitlement), `wallet_archived` (the wallet was
 * archived), `subscription_terminated` (the subscription reached a terminal state),
 * `feature_removed` (the subscription no longer has this Feature), `wallet_behavior_disabled` (the
 * Feature no longer has `wallet_behavior` configured), `superseded_by_replacement` (a later
 * entitlement now funds this wallet instead), or `subscription_prepaid` (the subscription switched
 * to prepaid, which cannot carry an active wallet). Accompanying `erroring`:
 * `allowance_not_representable` (the entitlement's current allowance doesn't fit the wallet's
 * amount encoding) or `balance_at_capacity` (granting it would push the balance past the maximum
 * supported value).
 */
export const Reason = {
  EntitlementMissing: "entitlement_missing",
  WalletArchived: "wallet_archived",
  SubscriptionTerminated: "subscription_terminated",
  FeatureRemoved: "feature_removed",
  WalletBehaviorDisabled: "wallet_behavior_disabled",
  SupersededByReplacement: "superseded_by_replacement",
  SubscriptionPrepaid: "subscription_prepaid",
  AllowanceNotRepresentable: "allowance_not_representable",
  BalanceAtCapacity: "balance_at_capacity",
} as const;
export type Reason = (typeof Reason)[keyof typeof Reason] | (string & {});

export const reasonSchema: EnumSchema<Reason> = s.enumOf<Reason>(Reason);
