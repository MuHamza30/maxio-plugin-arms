import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type Product1 = number | string;

export const product1Schema: Schema<Product1> = s.of<Product1>(s.union([s.int(), s.string()]));
