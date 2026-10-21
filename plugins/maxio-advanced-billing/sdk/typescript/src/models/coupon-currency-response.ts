import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { couponCurrencySchema, type CouponCurrency } from "./coupon-currency.js";

export type CouponCurrencyResponse = {
  currencyPrices?: CouponCurrency[];
};

export const couponCurrencyResponseSchema: Schema<CouponCurrencyResponse> = s.object<CouponCurrencyResponse>({
  currencyPrices: s.optional(s.array(s.lazy(() => couponCurrencySchema))),
  _keysMap: {
    currencyPrices: "currency_prices",
  },
});
