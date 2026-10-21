import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type SubscriptionGroupCustomer = {
  firstName?: string;
  lastName?: string;
  organization?: string;
  email?: string;
  reference?: string;
};

export const subscriptionGroupCustomerSchema: Schema<SubscriptionGroupCustomer> =
  s.object<SubscriptionGroupCustomer>({
    firstName: s.optional(s.string()),
    lastName: s.optional(s.string()),
    organization: s.optional(s.string()),
    email: s.optional(s.string()),
    reference: s.optional(s.string()),
    _keysMap: {
      firstName: "first_name",
      lastName: "last_name",
    },
  });
