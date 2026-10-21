import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Price point handle or id. For component. */
export type PricePointId4 = string | number;

export const pricePointId4Schema: Schema<PricePointId4> = s.of<PricePointId4>(s.union([s.string(), s.int()]));
