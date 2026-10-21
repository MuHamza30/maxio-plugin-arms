import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065 */
export type UnitPrice = number | string;

export const unitPriceSchema: Schema<UnitPrice> = s.of<UnitPrice>(s.union([s.float64(), s.string()]));
