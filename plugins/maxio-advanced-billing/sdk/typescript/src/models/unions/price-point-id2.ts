import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type PricePointId2 = number | string;

export const pricePointId2Schema: Schema<PricePointId2> = s.of<PricePointId2>(s.union([s.int(), s.string()]));
