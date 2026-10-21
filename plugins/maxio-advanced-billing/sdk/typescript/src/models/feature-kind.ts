import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The behavior of a feature:
 * - `access_right`: a boolean entitlement. A subscriber either has access or does not.
 * - `usage_limit`: a quantified allowance measured over a recurring period (for example, "10,000
 *   API calls per month").
 * - `service_right`: a free-form value (text, boolean, or number) that isn't a simple access flag
 *   or a metered limit.
 */
export const FeatureKind = {
  AccessRight: "access_right",
  UsageLimit: "usage_limit",
  ServiceRight: "service_right",
} as const;
export type FeatureKind = (typeof FeatureKind)[keyof typeof FeatureKind] | (string & {});

export const featureKindSchema: EnumSchema<FeatureKind> = s.enumOf<FeatureKind>(FeatureKind);
