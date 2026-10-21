import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** Role for the price. */
export const CurrencyPriceRole = {
  Baseline: "baseline",
  Trial: "trial",
  Initial: "initial",
} as const;
export type CurrencyPriceRole = (typeof CurrencyPriceRole)[keyof typeof CurrencyPriceRole] | (string & {});

export const currencyPriceRoleSchema: EnumSchema<CurrencyPriceRole> =
  s.enumOf<CurrencyPriceRole>(CurrencyPriceRole);
