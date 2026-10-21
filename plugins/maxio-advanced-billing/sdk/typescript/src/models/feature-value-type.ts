import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The data type of a feature's value. For `access_right` features this is always `boolean`, and for
 * `usage_limit` features this is always `numeric`. For `service_right` features, you choose the
 * value type explicitly.
 */
export const FeatureValueType = {
  Text: "text",
  Boolean: "boolean",
  Numeric: "numeric",
} as const;
export type FeatureValueType = (typeof FeatureValueType)[keyof typeof FeatureValueType] | (string & {});

export const featureValueTypeSchema: EnumSchema<FeatureValueType> =
  s.enumOf<FeatureValueType>(FeatureValueType);
