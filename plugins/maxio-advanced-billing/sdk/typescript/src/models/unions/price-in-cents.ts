import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Required if using `custom_price` attribute. */
export type PriceInCents = string | number;

export const priceInCentsSchema: Schema<PriceInCents> = s.of<PriceInCents>(s.union([s.string(), s.int()]));
