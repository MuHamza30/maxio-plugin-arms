import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { payPalVaultSchema, type PayPalVault } from "./pay-pal-vault.js";
import { PaymentType, paymentTypeSchema } from "./payment-type.js";

export type PaypalPaymentProfile = {
  /** The Chargify-assigned ID of the stored PayPal payment profile. */
  id?: number;
  /** The first name of the PayPal account holder */
  firstName?: string;
  /** The last name of the PayPal account holder */
  lastName?: string;
  /** The Chargify-assigned id for the customer record to which the PayPal account belongs */
  customerId?: number;
  /** The vault that stores the payment profile with the provided vault_token. */
  currentVault?: PayPalVault;
  /** The “token” provided by your vault storage for an already stored payment profile */
  vaultToken?: string;
  /** The current billing street address for the PayPal account */
  billingAddress?: string | null;
  /** The current billing address city for the PayPal account */
  billingCity?: string | null;
  /** The current billing address state for the PayPal account */
  billingState?: string | null;
  /** The current billing address zip code for the PayPal account */
  billingZip?: string | null;
  /** The current billing address country for the PayPal account */
  billingCountry?: string | null;
  customerVaultToken?: string | null;
  /** The current billing street address, second line, for the PayPal account */
  billingAddress2?: string | null;
  /** @default PaymentType.PaypalAccount */
  paymentType?: PaymentType;
  siteGatewaySettingId?: number | null;
  gatewayHandle?: string | null;
  paypalEmail?: string;
  /** A timestamp indicating when this payment profile was created */
  createdAt?: Date;
  /** A timestamp indicating when this payment profile was last updated */
  updatedAt?: Date;
};

export const paypalPaymentProfileSchema: Schema<PaypalPaymentProfile> = s.object<PaypalPaymentProfile>({
  id: s.optional(s.int()),
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  customerId: s.optional(s.int()),
  currentVault: s.optional(s.lazy(() => payPalVaultSchema)),
  vaultToken: s.optional(s.string()),
  billingAddress: s.optionalNullable(s.string()),
  billingCity: s.optionalNullable(s.string()),
  billingState: s.optionalNullable(s.string()),
  billingZip: s.optionalNullable(s.string()),
  billingCountry: s.optionalNullable(s.string()),
  customerVaultToken: s.optionalNullable(s.string()),
  billingAddress2: s.optionalNullable(s.string()),
  paymentType: s.defaulted(paymentTypeSchema, PaymentType.PaypalAccount),
  siteGatewaySettingId: s.optionalNullable(s.int()),
  gatewayHandle: s.optionalNullable(s.string()),
  paypalEmail: s.optional(s.string()),
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
    paypalEmail: "paypal_email",
    createdAt: "created_at",
    updatedAt: "updated_at",
  },
});
