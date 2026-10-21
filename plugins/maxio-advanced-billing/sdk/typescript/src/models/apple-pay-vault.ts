import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The vault that stores the payment profile with the provided vault_token. */
export const ApplePayVault = {
  BraintreeBlue: "braintree_blue",
} as const;
export type ApplePayVault = (typeof ApplePayVault)[keyof typeof ApplePayVault] | (string & {});

export const applePayVaultSchema: EnumSchema<ApplePayVault> = s.enumOf<ApplePayVault>(ApplePayVault);
