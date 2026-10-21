import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The vault that stores the payment profile with the provided vault_token. */
export const PayPalVault = {
  BraintreeBlue: "braintree_blue",
  Paypal: "paypal",
  Moduslink: "moduslink",
  PaypalComplete: "paypal_complete",
} as const;
export type PayPalVault = (typeof PayPalVault)[keyof typeof PayPalVault] | (string & {});

export const payPalVaultSchema: EnumSchema<PayPalVault> = s.enumOf<PayPalVault>(PayPalVault);
