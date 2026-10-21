import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { payerAttributesSchema, type PayerAttributes } from "./payer-attributes.js";
import {
  subscriptionGroupBankAccountSchema,
  type SubscriptionGroupBankAccount,
} from "./subscription-group-bank-account.js";
import {
  subscriptionGroupCreditCardSchema,
  type SubscriptionGroupCreditCard,
} from "./subscription-group-credit-card.js";
import {
  subscriptionGroupSignupItemSchema,
  type SubscriptionGroupSignupItem,
} from "./subscription-group-signup-item.js";

export type SubscriptionGroupSignupFailureData = {
  payerId?: number;
  payerReference?: string;
  paymentProfileId?: number;
  paymentCollectionMethod?: string;
  payerAttributes?: PayerAttributes;
  creditCardAttributes?: SubscriptionGroupCreditCard;
  bankAccountAttributes?: SubscriptionGroupBankAccount;
  subscriptions?: SubscriptionGroupSignupItem[];
};

export const subscriptionGroupSignupFailureDataSchema: Schema<SubscriptionGroupSignupFailureData> =
  s.object<SubscriptionGroupSignupFailureData>({
    payerId: s.optional(s.int()),
    payerReference: s.optional(s.string()),
    paymentProfileId: s.optional(s.int()),
    paymentCollectionMethod: s.optional(s.string()),
    payerAttributes: s.optional(s.lazy(() => payerAttributesSchema)),
    creditCardAttributes: s.optional(s.lazy(() => subscriptionGroupCreditCardSchema)),
    bankAccountAttributes: s.optional(s.lazy(() => subscriptionGroupBankAccountSchema)),
    subscriptions: s.optional(s.array(s.lazy(() => subscriptionGroupSignupItemSchema))),
    _keysMap: {
      payerId: "payer_id",
      payerReference: "payer_reference",
      paymentProfileId: "payment_profile_id",
      paymentCollectionMethod: "payment_collection_method",
      payerAttributes: "payer_attributes",
      creditCardAttributes: "credit_card_attributes",
      bankAccountAttributes: "bank_account_attributes",
    },
  });
