import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * The aggregated value, coerced according to `type`: a boolean for `access_right` (and boolean
 * `service_right`), a number for `usage_limit` (and numeric `service_right`), or a string for text
 * `service_right`.
 */
export type Value = boolean | number | string;

export const valueSchema: Schema<Value> = s.of<Value>(s.union([s.boolean(), s.float64(), s.string()]));
