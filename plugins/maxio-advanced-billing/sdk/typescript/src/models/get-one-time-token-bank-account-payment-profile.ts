import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { bankAccountHolderTypeSchema, type BankAccountHolderType } from "./bank-account-holder-type.js";
import { bankAccountTypeSchema, type BankAccountType } from "./bank-account-type.js";
import { bankAccountVaultSchema, type BankAccountVault } from "./bank-account-vault.js";

export type GetOneTimeTokenBankAccountPaymentProfile = {
  id?: string | null;
  firstName: string;
  lastName: string;
  customerId?: string | null;
  /**
   * The vault that stores the payment profile with the provided vault_token. Use `bogus` for
   * testing.
   */
  currentVault: BankAccountVault;
  vaultToken: string;
  billingAddress: string;
  billingAddress2?: string;
  billingCity: string;
  billingCountry: string;
  billingState: string;
  billingZip: string;
  bankName: string;
  maskedBankRoutingNumber: string;
  maskedBankAccountNumber: string;
  /** Defaults to checking */
  bankAccountType: BankAccountType;
  /** Defaults to personal */
  bankAccountHolderType: BankAccountHolderType;
  paymentType: string;
  disabled: boolean;
  siteGatewaySettingId: number;
  customerVaultToken?: string | null;
  gatewayHandle?: string | null;
  verified?: boolean | null;
};

export const getOneTimeTokenBankAccountPaymentProfileSchema: Schema<GetOneTimeTokenBankAccountPaymentProfile> =
  s.object<GetOneTimeTokenBankAccountPaymentProfile>({
    id: s.optionalNullable(s.string()),
    firstName: s.string(),
    lastName: s.string(),
    customerId: s.optionalNullable(s.string()),
    currentVault: bankAccountVaultSchema,
    vaultToken: s.string(),
    billingAddress: s.string(),
    billingAddress2: s.optional(s.string()),
    billingCity: s.string(),
    billingCountry: s.string(),
    billingState: s.string(),
    billingZip: s.string(),
    bankName: s.string(),
    maskedBankRoutingNumber: s.string(),
    maskedBankAccountNumber: s.string(),
    bankAccountType: bankAccountTypeSchema,
    bankAccountHolderType: bankAccountHolderTypeSchema,
    paymentType: s.string(),
    disabled: s.boolean(),
    siteGatewaySettingId: s.int(),
    customerVaultToken: s.optionalNullable(s.string()),
    gatewayHandle: s.optionalNullable(s.string()),
    verified: s.optionalNullable(s.boolean()),
    _keysMap: {
      firstName: "first_name",
      lastName: "last_name",
      customerId: "customer_id",
      currentVault: "current_vault",
      vaultToken: "vault_token",
      billingAddress: "billing_address",
      billingAddress2: "billing_address_2",
      billingCity: "billing_city",
      billingCountry: "billing_country",
      billingState: "billing_state",
      billingZip: "billing_zip",
      bankName: "bank_name",
      maskedBankRoutingNumber: "masked_bank_routing_number",
      maskedBankAccountNumber: "masked_bank_account_number",
      bankAccountType: "bank_account_type",
      bankAccountHolderType: "bank_account_holder_type",
      paymentType: "payment_type",
      siteGatewaySettingId: "site_gateway_setting_id",
      customerVaultToken: "customer_vault_token",
      gatewayHandle: "gateway_handle",
    },
  });
