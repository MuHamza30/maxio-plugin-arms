import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import {
  aggregatedEntitlementPeriodicitySchema,
  type AggregatedEntitlementPeriodicity,
} from "./aggregated-entitlement-periodicity.js";
import { featureKindSchema, type FeatureKind } from "./feature-kind.js";
import { valueSchema, type Value } from "./unions/value.js";

/**
 * One entitlement in a subscriber's aggregated entitlements list. Entries are aggregated per
 * feature key and periodicity window, not per feature key alone. A `usage_limit` feature granted
 * with two different periodicities yields two entries sharing one `feature_key`. Use
 * `periodicity_key` to identify an entry uniquely.
 */
export type AggregatedEntitlement = {
  /**
   * The feature's key, prefixed by kind: `feature.*` for `access_right`, `usage.*` for
   * `usage_limit`, `service.*` for `service_right`.
   */
  featureKey?: string;
  /**
   * Uniquely identifies this aggregated entry: the prefixed feature key, suffixed with
   * `:{interval}:{unit}` when the entitlement has a periodicity window. Equal to `feature_key` when
   * `periodicity` is `null`.
   */
  periodicityKey?: string;
  name?: string;
  /**
   * The behavior of a feature:
   * - `access_right`: a boolean entitlement. A subscriber either has access or does not.
   * - `usage_limit`: a quantified allowance measured over a recurring period (for example, "10,000
   *   API calls per month").
   * - `service_right`: a free-form value (text, boolean, or number) that isn't a simple access flag
   *   or a metered limit.
   */
  type?: FeatureKind;
  /**
   * The aggregated value, coerced according to `type`: a boolean for `access_right` (and boolean
   * `service_right`), a number for `usage_limit` (and numeric `service_right`), or a string for
   * text `service_right`.
   */
  value?: Value;
  /**
   * `true` only when the aggregated value is truthy for this feature's kind, and the subscription
   * is in a live state (`active`, `trialing`, `assessing`, `past_due`, or `soft_failure`). `false`
   * otherwise, including for `awaiting_signup`, canceled, expired, and on-hold subscriptions.
   * Entitlements deliberately stay enabled through dunning.
   */
  enabled?: boolean;
  periodicity?: AggregatedEntitlementPeriodicity | null;
  /**
   * The names of the products/components contributing to this entitlement. For `access_right`
   * features, only contributors that granted `true` are listed.
   */
  sourceProducts?: string[];
};

export const aggregatedEntitlementSchema: Schema<AggregatedEntitlement> = s.object<AggregatedEntitlement>({
  featureKey: s.optional(s.string()),
  periodicityKey: s.optional(s.string()),
  name: s.optional(s.string()),
  type: s.optional(s.lazy(() => featureKindSchema)),
  value: s.optional(s.lazy(() => valueSchema)),
  enabled: s.optional(s.boolean()),
  periodicity: s.optionalNullable(s.lazy(() => aggregatedEntitlementPeriodicitySchema)),
  sourceProducts: s.optional(s.array(s.string())),
  _keysMap: {
    featureKey: "feature_key",
    periodicityKey: "periodicity_key",
    sourceProducts: "source_products",
  },
});
