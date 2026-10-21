import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { adjustmentSchema, type Adjustment } from "./adjustment.js";

/**
 * A signed correction to a specific grant's balance, or to an overdraft entry's usage, intended for
 * support and ops use.
 */
export type CreateWalletAdjustmentRequest = {
  adjustment: Adjustment;
};

export const createWalletAdjustmentRequestSchema: Schema<CreateWalletAdjustmentRequest> =
  s.object<CreateWalletAdjustmentRequest>({
    adjustment: adjustmentSchema,
  });
