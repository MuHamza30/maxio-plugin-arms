import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { collectionMethodSchema, type CollectionMethod } from "./collection-method.js";
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

export type SubscriptionGroupSignup = {
  paymentProfileId?: number;
  payerId?: number;
  payerReference?: string;
  /**
   * The type of payment collection to be used in the subscription. For legacy Statements
   * Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing
   * Architecture valid options are - `remittance`, `automatic`, `prepaid`.
   */
  paymentCollectionMethod?: CollectionMethod;
  payerAttributes?: PayerAttributes;
  creditCardAttributes?: SubscriptionGroupCreditCard;
  bankAccountAttributes?: SubscriptionGroupBankAccount;
  subscriptions: SubscriptionGroupSignupItem[];
};

export const subscriptionGroupSignupSchema: Schema<SubscriptionGroupSignup> =
  s.object<SubscriptionGroupSignup>({
    paymentProfileId: s.optional(s.int()),
    payerId: s.optional(s.int()),
    payerReference: s.optional(s.string()),
    paymentCollectionMethod: s.optional(s.lazy(() => collectionMethodSchema)),
    payerAttributes: s.optional(s.lazy(() => payerAttributesSchema)),
    creditCardAttributes: s.optional(s.lazy(() => subscriptionGroupCreditCardSchema)),
    bankAccountAttributes: s.optional(s.lazy(() => subscriptionGroupBankAccountSchema)),
    subscriptions: s.array(s.lazy(() => subscriptionGroupSignupItemSchema)),
    _keysMap: {
      paymentProfileId: "payment_profile_id",
      payerId: "payer_id",
      payerReference: "payer_reference",
      paymentCollectionMethod: "payment_collection_method",
      payerAttributes: "payer_attributes",
      creditCardAttributes: "credit_card_attributes",
      bankAccountAttributes: "bank_account_attributes",
    },
  });
