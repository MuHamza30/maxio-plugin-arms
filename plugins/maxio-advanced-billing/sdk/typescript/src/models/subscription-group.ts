import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { collectionMethodSchema, type CollectionMethod } from "./collection-method.js";
import {
  subscriptionGroupPaymentProfileSchema,
  type SubscriptionGroupPaymentProfile,
} from "./subscription-group-payment-profile.js";

export type SubscriptionGroup = {
  uid?: string;
  customerId?: number;
  paymentProfile?: SubscriptionGroupPaymentProfile;
  /**
   * The type of payment collection to be used in the subscription. For legacy Statements
   * Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing
   * Architecture valid options are - `remittance`, `automatic`, `prepaid`.
   */
  paymentCollectionMethod?: CollectionMethod;
  subscriptionIds?: number[];
  createdAt?: Date;
};

export const subscriptionGroupSchema: Schema<SubscriptionGroup> = s.object<SubscriptionGroup>({
  uid: s.optional(s.string()),
  customerId: s.optional(s.int()),
  paymentProfile: s.optional(s.lazy(() => subscriptionGroupPaymentProfileSchema)),
  paymentCollectionMethod: s.optional(s.lazy(() => collectionMethodSchema)),
  subscriptionIds: s.optional(s.array(s.int())),
  createdAt: s.optional(s.dateTime()),
  _keysMap: {
    customerId: "customer_id",
    paymentProfile: "payment_profile",
    paymentCollectionMethod: "payment_collection_method",
    subscriptionIds: "subscription_ids",
    createdAt: "created_at",
  },
});
