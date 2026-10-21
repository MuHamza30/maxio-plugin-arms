import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/** Either the component price point's Chargify id or its handle prefixed with `handle:` */
export type PricePointId3 = string | number;

export const pricePointId3Schema: Schema<PricePointId3> = s.of<PricePointId3>(s.union([s.string(), s.int()]));
