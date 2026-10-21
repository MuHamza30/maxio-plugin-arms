import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { applePayVaultSchema, type ApplePayVault } from "./apple-pay-vault.js";
import { PaymentType, paymentTypeSchema } from "./payment-type.js";

export type ApplePayPaymentProfile = {
  /** The Chargify-assigned ID of the Apple Pay payment profile. */
  id?: number;
  /** The first name of the Apple Pay account holder */
  firstName?: string;
  /** The last name of the Apple Pay account holder */
  lastName?: string;
  /** The Chargify-assigned ID for the customer record to which the Apple Pay account belongs */
  customerId?: number;
  /** The vault that stores the payment profile with the provided vault_token. */
  currentVault?: ApplePayVault;
  /** The “token” provided by your vault storage for an already stored payment profile */
  vaultToken?: string;
  /** The current billing street address for the Apple Pay account */
  billingAddress?: string | null;
  /** The current billing address city for the Apple Pay account */
  billingCity?: string | null;
  /** The current billing address state for the Apple Pay account */
  billingState?: string | null;
  /** The current billing address zip code for the Apple Pay account */
  billingZip?: string | null;
  /** The current billing address country for the Apple Pay account */
  billingCountry?: string | null;
  customerVaultToken?: string | null;
  /** The current billing street address, second line, for the Apple Pay account */
  billingAddress2?: string | null;
  /** @default PaymentType.ApplePay */
  paymentType?: PaymentType;
  siteGatewaySettingId?: number | null;
  gatewayHandle?: string | null;
  /** A timestamp indicating when this payment profile was created */
  createdAt?: Date;
  /** A timestamp indicating when this payment profile was last updated */
  updatedAt?: Date;
};

export const applePayPaymentProfileSchema: Schema<ApplePayPaymentProfile> = s.object<ApplePayPaymentProfile>({
  id: s.optional(s.int()),
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  customerId: s.optional(s.int()),
  currentVault: s.optional(s.lazy(() => applePayVaultSchema)),
  vaultToken: s.optional(s.string()),
  billingAddress: s.optionalNullable(s.string()),
  billingCity: s.optionalNullable(s.string()),
  billingState: s.optionalNullable(s.string()),
  billingZip: s.optionalNullable(s.string()),
  billingCountry: s.optionalNullable(s.string()),
  customerVaultToken: s.optionalNullable(s.string()),
  billingAddress2: s.optionalNullable(s.string()),
  paymentType: s.defaulted(paymentTypeSchema, PaymentType.ApplePay),
  siteGatewaySettingId: s.optionalNullable(s.int()),
  gatewayHandle: s.optionalNullable(s.string()),
  createdAt: s.optional(s.dateTime()),
  updatedAt: s.optional(s.dateTime()),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
    customerId: "customer_id",
    currentVault: "current_vault",
    vaultToken: "vault_token",
    billingAddress: "billing_address",
    billingCity: "billing_city",
    billingState: "billing_state",
    billingZip: "billing_zip",
    billingCountry: "billing_country",
    customerVaultToken: "customer_vault_token",
    billingAddress2: "billing_address_2",
    paymentType: "payment_type",
    siteGatewaySettingId: "site_gateway_setting_id",
    gatewayHandle: "gateway_handle",
    createdAt: "created_at",
    updatedAt: "updated_at",
  },
});
