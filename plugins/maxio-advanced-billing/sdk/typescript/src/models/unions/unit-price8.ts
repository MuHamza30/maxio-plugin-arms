import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065 */
export type UnitPrice8 = string | number;

export const unitPrice8Schema: Schema<UnitPrice8> = s.of<UnitPrice8>(s.union([s.string(), s.float64()]));
