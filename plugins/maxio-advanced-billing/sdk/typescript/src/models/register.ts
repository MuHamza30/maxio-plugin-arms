import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type Register = {
  id?: number;
  maxioId?: string;
  name?: string;
  /**
   * The ISO 4217 currency code (3 character string) representing the currency of an invoice
   * transaction.
   */
  currencyCode?: string;
};

export const registerSchema: Schema<Register> = s.object<Register>({
  id: s.optional(s.int()),
  maxioId: s.optional(s.string()),
  name: s.optional(s.string()),
  currencyCode: s.optional(s.string()),
  _keysMap: {
    maxioId: "maxio_id",
    currencyCode: "currency_code",
  },
});
