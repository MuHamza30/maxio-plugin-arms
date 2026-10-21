import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";

/**
 * (Optional when performing a Subscription Import via vault_token, required otherwise) The 4-digit
 * credit card expiration year, as an integer or string, e.g., 2012
 */
export type ExpirationYear2 = number | string;

export const expirationYear2Schema: Schema<ExpirationYear2> = s.of<ExpirationYear2>(
  s.union([s.int(), s.string()]),
);
