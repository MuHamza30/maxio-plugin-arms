import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * The [Wallet Product]($e/Wallet%20Products/createWalletProduct) that will denominate the wallet:
 * its numeric id, or its handle prefixed with `handle:` (for example `handle:token-pack`). A bare
 * handle with no prefix is looked up as an id and returns `404`. Immutable once the wallet is
 * created.
 */
export type WalletProductId = number | string;

export const walletProductIdSchema: Schema<WalletProductId> = s.of<WalletProductId>(
  s.union([s.int(), s.string()]),
);
