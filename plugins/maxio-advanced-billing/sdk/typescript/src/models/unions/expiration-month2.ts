import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * (Optional when performing a Subscription Import via vault_token, required otherwise) The 1- or
 * 2-digit credit card expiration month, as an integer or string, e.g., 5
 */
export type ExpirationMonth2 = number | string;

export const expirationMonth2Schema: Schema<ExpirationMonth2> = s.of<ExpirationMonth2>(
  s.union([s.int(), s.string()]),
);
