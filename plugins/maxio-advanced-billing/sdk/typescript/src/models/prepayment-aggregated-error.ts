import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type PrepaymentAggregatedError = {
  amountInCents?: string[];
  base?: string[];
  external?: string[];
};

export const prepaymentAggregatedErrorSchema: Schema<PrepaymentAggregatedError> =
  s.object<PrepaymentAggregatedError>({
    amountInCents: s.optional(s.array(s.string())),
    base: s.optional(s.array(s.string())),
    external: s.optional(s.array(s.string())),
    _keysMap: {
      amountInCents: "amount_in_cents",
    },
  });
