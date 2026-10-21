import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type PricePointId = string | number;

export const pricePointIdSchema: Schema<PricePointId> = s.of<PricePointId>(s.union([s.string(), s.int()]));
