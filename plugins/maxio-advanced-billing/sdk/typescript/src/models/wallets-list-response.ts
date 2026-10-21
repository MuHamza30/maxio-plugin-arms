import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { listPublicKeysMetaSchema, type ListPublicKeysMeta } from "./list-public-keys-meta.js";
import { walletSchema, type Wallet } from "./wallet.js";

export type WalletsListResponse = {
  wallets: Wallet[];
  meta: ListPublicKeysMeta;
};

export const walletsListResponseSchema: Schema<WalletsListResponse> = s.object<WalletsListResponse>({
  wallets: s.array(s.lazy(() => walletSchema)),
  meta: listPublicKeysMetaSchema,
});
