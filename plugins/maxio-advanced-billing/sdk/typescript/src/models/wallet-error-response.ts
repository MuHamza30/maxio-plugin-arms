import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

/**
 * The JSON error body returned by every wallet, transaction, adjustment, purchase, and Wallet
 * Product endpoint for `404`, `409`, `422`, `500`, and `503` responses. A `403` is not JSON; it is
 * the plain text `403 Forbidden`.
 */
export type WalletErrorResponse = {
  /** Human-readable messages. These may be reworded, so match on `code` instead. */
  errors: string[];
  /**
   * A stable, machine-readable reason, for example `wallet_depleted`, `wallet_not_found`,
   * `wallet_product_not_found`, `price_point_archived`, `kind_invalid`, or `parameter_missing`.
   * Failures that come from record validation, such as a field that fails a model rule, report
   * `validation_failed`.
   */
  code: string;
};

export const walletErrorResponseSchema: Schema<WalletErrorResponse> = s.object<WalletErrorResponse>({
  errors: s.array(s.string()),
  code: s.string(),
});
