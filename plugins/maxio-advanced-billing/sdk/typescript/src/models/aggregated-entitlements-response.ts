import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { aggregatedEntitlementSchema, type AggregatedEntitlement } from "./aggregated-entitlement.js";

export type AggregatedEntitlementsResponse = {
  subscriptionId: number;
  customerId: number;
  /** The subscription's current state, e.g. `active`, `trialing`, `canceled`. */
  status: string;
  entitlements: AggregatedEntitlement[];
};

export const aggregatedEntitlementsResponseSchema: Schema<AggregatedEntitlementsResponse> =
  s.object<AggregatedEntitlementsResponse>({
    subscriptionId: s.int(),
    customerId: s.int(),
    status: s.string(),
    entitlements: s.array(s.lazy(() => aggregatedEntitlementSchema)),
    _keysMap: {
      subscriptionId: "subscription_id",
      customerId: "customer_id",
    },
  });
