import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletProductListItemSchema, type WalletProductListItem } from "./wallet-product-list-item.js";

export type WalletProductsListResponse = {
  walletProducts: WalletProductListItem[];
  /** Total number of Wallet Products matching the filters, across all pages. */
  totalCount: number;
  /**
   * Not a simple count of archived products matching the filters. With `status=archived`, equals
   * `total_count` (there's nothing else to report). With any other `status`, it's `0` whenever
   * `total_count` is non-zero, and only when `total_count` is `0` does it become the number of
   * archived Wallet Products matching the same `q` search term (ignoring `status`): an empty-state
   * hint, not a running total.
   */
  archivedCount: number;
};

export const walletProductsListResponseSchema: Schema<WalletProductsListResponse> =
  s.object<WalletProductsListResponse>({
    walletProducts: s.array(s.lazy(() => walletProductListItemSchema)),
    totalCount: s.int(),
    archivedCount: s.int(),
    _keysMap: {
      walletProducts: "wallet_products",
      totalCount: "total_count",
      archivedCount: "archived_count",
    },
  });
