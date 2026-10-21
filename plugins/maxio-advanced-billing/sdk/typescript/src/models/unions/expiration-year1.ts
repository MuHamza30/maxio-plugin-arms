import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * (Optional when performing an Import via vault_token, required otherwise) The 4-digit credit card
 * expiration year, as an integer or string, e.g., 2012
 */
export type ExpirationYear1 = number | string;

export const expirationYear1Schema: Schema<ExpirationYear1> = s.of<ExpirationYear1>(
  s.union([s.int(), s.string()]),
);
