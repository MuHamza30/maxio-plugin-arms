import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * (Optional when performing an Import via vault_token, required otherwise) The 1- or 2-digit credit
 * card expiration month, as an integer or string, e.g., 5
 */
export type ExpirationMonth1 = number | string;

export const expirationMonth1Schema: Schema<ExpirationMonth1> = s.of<ExpirationMonth1>(
  s.union([s.int(), s.string()]),
);
