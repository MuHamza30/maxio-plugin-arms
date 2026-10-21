import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** A handle for the line item transaction type */
export const LineItemTransactionType = {
  Charge: "charge",
  Credit: "credit",
  Adjustment: "adjustment",
  Payment: "payment",
  Refund: "refund",
  InfoTransaction: "info_transaction",
  PaymentAuthorization: "payment_authorization",
} as const;
export type LineItemTransactionType =
  | (typeof LineItemTransactionType)[keyof typeof LineItemTransactionType]
  | (string & {});

export const lineItemTransactionTypeSchema: EnumSchema<LineItemTransactionType> =
  s.enumOf<LineItemTransactionType>(LineItemTransactionType);
