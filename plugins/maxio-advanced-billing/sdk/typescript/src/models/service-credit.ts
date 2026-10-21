import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { serviceCreditTypeSchema, type ServiceCreditType } from "./service-credit-type.js";

export type ServiceCredit = {
  id?: number;
  /** The amount in cents of the entry */
  amountInCents?: number;
  /** The new balance for the credit account */
  endingBalanceInCents?: number;
  /** The type of entry */
  entryType?: ServiceCreditType;
  /** The memo attached to the entry */
  memo?: string;
};

export const serviceCreditSchema: Schema<ServiceCredit> = s.object<ServiceCredit>({
  id: s.optional(s.int()),
  amountInCents: s.optional(s.int()),
  endingBalanceInCents: s.optional(s.int()),
  entryType: s.optional(s.lazy(() => serviceCreditTypeSchema)),
  memo: s.optional(s.string()),
  _keysMap: {
    amountInCents: "amount_in_cents",
    endingBalanceInCents: "ending_balance_in_cents",
    entryType: "entry_type",
  },
});
