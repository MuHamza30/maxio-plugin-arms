import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type InvoicePrePayment = {
  /** The subscription id for the prepayment account */
  subscriptionId?: number;
  /** The amount in cents of the prepayment that was created as a result of this payment. */
  amountInCents?: number;
  /**
   * The total balance of the prepayment account for this subscription including any prior
   * prepayments
   */
  endingBalanceInCents?: number;
};

export const invoicePrePaymentSchema: Schema<InvoicePrePayment> = s.object<InvoicePrePayment>({
  subscriptionId: s.optional(s.int()),
  amountInCents: s.optional(s.int()),
  endingBalanceInCents: s.optional(s.int()),
  _keysMap: {
    subscriptionId: "subscription_id",
    amountInCents: "amount_in_cents",
    endingBalanceInCents: "ending_balance_in_cents",
  },
});
