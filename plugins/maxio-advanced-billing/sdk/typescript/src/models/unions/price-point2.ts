import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type PricePoint2 = string | number;

export const pricePoint2Schema: Schema<PricePoint2> = s.of<PricePoint2>(s.union([s.string(), s.int()]));
