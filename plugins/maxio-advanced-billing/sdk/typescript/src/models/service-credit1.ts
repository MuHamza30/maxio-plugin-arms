import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { serviceCreditTypeSchema, type ServiceCreditType } from "./service-credit-type.js";

export type ServiceCredit1 = {
  id?: number;
  /** The amount in cents of the entry */
  amountInCents?: number;
  /** The new balance for the credit account */
  endingBalanceInCents?: number;
  /** The type of entry */
  entryType?: ServiceCreditType;
  /** The memo attached to the entry */
  memo?: string;
  /** The invoice uid associated with the entry. Only present for debit entries. */
  invoiceUid?: string | null;
  /** The remaining balance for the entry */
  remainingBalanceInCents?: number;
  /** The date and time the entry was created */
  createdAt?: Date;
};

export const serviceCredit1Schema: Schema<ServiceCredit1> = s.object<ServiceCredit1>({
  id: s.optional(s.int()),
  amountInCents: s.optional(s.int()),
  endingBalanceInCents: s.optional(s.int()),
  entryType: s.optional(s.lazy(() => serviceCreditTypeSchema)),
  memo: s.optional(s.string()),
  invoiceUid: s.optionalNullable(s.string()),
  remainingBalanceInCents: s.optional(s.int()),
  createdAt: s.optional(s.dateTime()),
  _keysMap: {
    amountInCents: "amount_in_cents",
    endingBalanceInCents: "ending_balance_in_cents",
    entryType: "entry_type",
    invoiceUid: "invoice_uid",
    remainingBalanceInCents: "remaining_balance_in_cents",
    createdAt: "created_at",
  },
});
