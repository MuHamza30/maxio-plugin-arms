import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * Always positive; `kind` determines the sign written to the ledger. Encoded as a decimal string
 * with at most 8 fractional digits. Send fractional values as strings: a JSON number with a decimal
 * point is rejected with `422`, because a double-precision float may already have lost precision
 * before the request arrives.
 */
export type Amount6 = string | number;

export const amount6Schema: Schema<Amount6> = s.of<Amount6>(s.union([s.string(), s.int()]));
