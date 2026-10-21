import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { updateCouponCurrencySchema, type UpdateCouponCurrency } from "./update-coupon-currency.js";

export type CouponCurrencyRequest = {
  currencyPrices: UpdateCouponCurrency[];
};

export const couponCurrencyRequestSchema: Schema<CouponCurrencyRequest> = s.object<CouponCurrencyRequest>({
  currencyPrices: s.array(s.lazy(() => updateCouponCurrencySchema)),
  _keysMap: {
    currencyPrices: "currency_prices",
  },
});
