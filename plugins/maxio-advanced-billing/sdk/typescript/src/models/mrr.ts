import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { breakoutsSchema, type Breakouts } from "./breakouts.js";

export type Mrr = {
  amountInCents?: number;
  amountFormatted?: string;
  currency?: string;
  currencySymbol?: string;
  breakouts?: Breakouts;
  /** ISO8601 timestamp */
  atTime?: Date;
};

export const mrrSchema: Schema<Mrr> = s.object<Mrr>({
  amountInCents: s.optional(s.int()),
  amountFormatted: s.optional(s.string()),
  currency: s.optional(s.string()),
  currencySymbol: s.optional(s.string()),
  breakouts: s.optional(s.lazy(() => breakoutsSchema)),
  atTime: s.optional(s.dateTime()),
  _keysMap: {
    amountInCents: "amount_in_cents",
    amountFormatted: "amount_formatted",
    currencySymbol: "currency_symbol",
    atTime: "at_time",
  },
});
