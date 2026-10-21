import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/** One active wallet drawing on this Wallet Product. */
export type WalletProductActiveWallet = {
  /** The Advanced Billing id of the wallet. */
  id?: number;
  subscriptionId?: number;
  /**
   * The owning customer's organization name, falling back to their full name, then to `"Customer
   * #<id>"`. `"Customer"` (with no id) when the wallet's subscription has no customer at all.
   */
  companyName?: string;
  /**
   * See the same field on [Wallet Product Usage Template]($m/Wallet%20Product%20Usage%20Template).
   * The same caveats apply.
   */
  purchaseMechanism?: string | null;
  pricePointName?: string | null;
  currency?: string;
  /** `false` when the wallet's Feature is archived. */
  active?: boolean;
};

export const walletProductActiveWalletSchema: Schema<WalletProductActiveWallet> =
  s.object<WalletProductActiveWallet>({
    id: s.optional(s.int()),
    subscriptionId: s.optional(s.int()),
    companyName: s.optional(s.string()),
    purchaseMechanism: s.optionalNullable(s.string()),
    pricePointName: s.optionalNullable(s.string()),
    currency: s.optional(s.string()),
    active: s.optional(s.boolean()),
    _keysMap: {
      subscriptionId: "subscription_id",
      companyName: "company_name",
      purchaseMechanism: "purchase_mechanism",
      pricePointName: "price_point_name",
    },
  });
