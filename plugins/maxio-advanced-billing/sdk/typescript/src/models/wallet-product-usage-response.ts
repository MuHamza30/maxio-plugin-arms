import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { activeWalletsSchema, type ActiveWallets } from "./active-wallets.js";
import {
  walletProductUsageTemplateSchema,
  type WalletProductUsageTemplate,
} from "./wallet-product-usage-template.js";

export type WalletProductUsageResponse = {
  /** Wallet templates billing through this product at its default price point. */
  walletTemplates: WalletProductUsageTemplate[];
  /** Wallet templates billing through this product at a price point other than the default. */
  pricePointOverrides: WalletProductUsageTemplate[];
  activeWallets: ActiveWallets;
};

export const walletProductUsageResponseSchema: Schema<WalletProductUsageResponse> =
  s.object<WalletProductUsageResponse>({
    walletTemplates: s.array(s.lazy(() => walletProductUsageTemplateSchema)),
    pricePointOverrides: s.array(s.lazy(() => walletProductUsageTemplateSchema)),
    activeWallets: activeWalletsSchema,
    _keysMap: {
      walletTemplates: "wallet_templates",
      pricePointOverrides: "price_point_overrides",
      activeWallets: "active_wallets",
    },
  });
