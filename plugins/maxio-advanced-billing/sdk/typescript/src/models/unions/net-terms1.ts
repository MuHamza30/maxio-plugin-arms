import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

export type NetTerms1 = string | number;

export const netTerms1Schema: Schema<NetTerms1> = s.of<NetTerms1>(s.union([s.string(), s.int()]));
