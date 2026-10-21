import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { purchaseSchema, type Purchase } from "./purchase.js";

/**
 * Purchases prepaid units for the wallet at a price point, charging the subscription's payment
 * method.
 */
export type CreateWalletPurchaseRequest = {
  purchase: Purchase;
};

export const createWalletPurchaseRequestSchema: Schema<CreateWalletPurchaseRequest> =
  s.object<CreateWalletPurchaseRequest>({
    purchase: purchaseSchema,
  });
