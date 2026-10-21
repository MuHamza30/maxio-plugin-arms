import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { walletPurchasePreviewSchema, type WalletPurchasePreview } from "./wallet-purchase-preview.js";

export type WalletPurchasePreviewResponse = {
  walletPurchasePreviews: WalletPurchasePreview[];
};

export const walletPurchasePreviewResponseSchema: Schema<WalletPurchasePreviewResponse> =
  s.object<WalletPurchasePreviewResponse>({
    walletPurchasePreviews: s.array(s.lazy(() => walletPurchasePreviewSchema)),
    _keysMap: {
      walletPurchasePreviews: "wallet_purchase_previews",
    },
  });
