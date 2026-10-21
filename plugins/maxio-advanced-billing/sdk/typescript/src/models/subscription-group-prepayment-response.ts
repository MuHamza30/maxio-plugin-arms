import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { serviceCreditTypeSchema, type ServiceCreditType } from "./service-credit-type.js";

export type SubscriptionGroupPrepaymentResponse = {
  id?: number;
  /** The amount in cents of the entry. */
  amountInCents?: number;
  /** The ending balance in cents of the account. */
  endingBalanceInCents?: number;
  /** The type of entry */
  entryType?: ServiceCreditType;
  /** A memo attached to the entry. */
  memo?: string | null;
};

export const subscriptionGroupPrepaymentResponseSchema: Schema<SubscriptionGroupPrepaymentResponse> =
  s.object<SubscriptionGroupPrepaymentResponse>({
    id: s.optional(s.int()),
    amountInCents: s.optional(s.int()),
    endingBalanceInCents: s.optional(s.int()),
    entryType: s.optional(s.lazy(() => serviceCreditTypeSchema)),
    memo: s.optionalNullable(s.string()),
    _keysMap: {
      amountInCents: "amount_in_cents",
      endingBalanceInCents: "ending_balance_in_cents",
      entryType: "entry_type",
    },
  });
