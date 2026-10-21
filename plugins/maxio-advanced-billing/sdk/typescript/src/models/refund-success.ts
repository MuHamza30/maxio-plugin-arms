import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type RefundSuccess = {
  refundId: number;
  gatewayTransactionId: number;
  productId: number;
};

export const refundSuccessSchema: Schema<RefundSuccess> = s.object<RefundSuccess>({
  refundId: s.int(),
  gatewayTransactionId: s.int(),
  productId: s.int(),
  _keysMap: {
    refundId: "refund_id",
    gatewayTransactionId: "gateway_transaction_id",
    productId: "product_id",
  },
});
