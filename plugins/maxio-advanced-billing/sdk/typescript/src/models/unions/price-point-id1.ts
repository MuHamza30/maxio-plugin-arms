import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * Price point that the allocation should be charged at. Accepts either the price point's id
 * (integer) or handle (string). When not specified, the default price point will be used.
 */
export type PricePointId1 = string | number;

export const pricePointId1Schema: Schema<PricePointId1> = s.of<PricePointId1>(s.union([s.string(), s.int()]));
