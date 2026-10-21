import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PaymentRelatedEvents = {
  productId: number;
  accountTransactionId: number;
};

export const paymentRelatedEventsSchema: Schema<PaymentRelatedEvents> = s.object<PaymentRelatedEvents>({
  productId: s.int(),
  accountTransactionId: s.int(),
  _keysMap: {
    productId: "product_id",
    accountTransactionId: "account_transaction_id",
  },
});
