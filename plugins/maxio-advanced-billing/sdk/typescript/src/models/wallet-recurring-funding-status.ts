import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * `active`: refilling normally. `erroring`: the schedule is still due and retrying, but the last
 * attempt couldn't be written (see `reason`); correcting the underlying entitlement resumes funding
 * on the next run with no action needed on the wallet itself. `stopped`: funding has ended for good
 * (see `reason`); units already granted stay on the wallet and remain spendable, but no further
 * automatic grants will be made.
 */
export const WalletRecurringFundingStatus = {
  Active: "active",
  Erroring: "erroring",
  Stopped: "stopped",
} as const;
export type WalletRecurringFundingStatus =
  | (typeof WalletRecurringFundingStatus)[keyof typeof WalletRecurringFundingStatus]
  | (string & {});

export const walletRecurringFundingStatusSchema: EnumSchema<WalletRecurringFundingStatus> =
  s.enumOf<WalletRecurringFundingStatus>(WalletRecurringFundingStatus);
