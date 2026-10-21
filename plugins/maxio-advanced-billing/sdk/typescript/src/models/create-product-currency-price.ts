import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { currencyPriceRoleSchema, type CurrencyPriceRole } from "./currency-price-role.js";

export type CreateProductCurrencyPrice = {
  /** ISO code for one of the site level currencies. */
  currency: string;
  /** Price for the given role. */
  price: number;
  /** Role for the price. */
  role: CurrencyPriceRole;
};

export const createProductCurrencyPriceSchema: Schema<CreateProductCurrencyPrice> =
  s.object<CreateProductCurrencyPrice>({
    currency: s.string(),
    price: s.int(),
    role: currencyPriceRoleSchema,
  });
