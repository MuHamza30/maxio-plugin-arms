import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";

export type UpdateCouponCurrency = {
  /** ISO code for the site defined currency. */
  currency: string;
  /** Price for the given currency. */
  price: number;
};

export const updateCouponCurrencySchema: Schema<UpdateCouponCurrency> = s.object<UpdateCouponCurrency>({
  currency: s.string(),
  price: s.int(),
});
