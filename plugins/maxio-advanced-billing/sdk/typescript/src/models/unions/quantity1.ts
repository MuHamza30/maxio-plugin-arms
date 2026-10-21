import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type Quantity1 = number | string;

export const quantity1Schema: Schema<Quantity1> = s.of<Quantity1>(s.union([s.int(), s.string()]));
