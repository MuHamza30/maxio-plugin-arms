import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * A summary of the Wallet Product's default price point, for rendering a catalog listing without a
 * separate price points call.
 */
export type WalletProductPricePointSummary = {
  /** Number of archived price points on this Wallet Product. */
  archivedCount?: number;
  /**
   * The default price point's pricing scheme. `null` if the Wallet Product has no default price
   * point.
   */
  pricingScheme?: string | null;
  /**
   * Number of price brackets on the default price point. A `per_unit` scheme always stores exactly
   * one synthesized bracket, so this is `1` for `per_unit`, not `0`.
   */
  tierCount?: number;
  /**
   * The unit price of the default price point's first bracket, as a decimal string. `null` if there
   * are no brackets.
   */
  entryPrice?: string | null;
  /**
   * The unit price of the default price point's last bracket, as a decimal string. `null` if there
   * are no brackets.
   */
  finalPrice?: string | null;
};

export const walletProductPricePointSummarySchema: Schema<WalletProductPricePointSummary> =
  s.object<WalletProductPricePointSummary>({
    archivedCount: s.optional(s.int()),
    pricingScheme: s.optionalNullable(s.string()),
    tierCount: s.optional(s.int()),
    entryPrice: s.optionalNullable(s.string()),
    finalPrice: s.optionalNullable(s.string()),
    _keysMap: {
      archivedCount: "archived_count",
      pricingScheme: "pricing_scheme",
      tierCount: "tier_count",
      entryPrice: "entry_price",
      finalPrice: "final_price",
    },
  });
