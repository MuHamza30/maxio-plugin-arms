import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { bankAccountHolderTypeSchema, type BankAccountHolderType } from "./bank-account-holder-type.js";
import { bankAccountTypeSchema, type BankAccountType } from "./bank-account-type.js";
import { bankAccountVaultSchema, type BankAccountVault } from "./bank-account-vault.js";
import { PaymentType, paymentTypeSchema } from "./payment-type.js";

export type BankAccountPaymentProfile = {
  /**
   * The Chargify-assigned ID of the stored bank account. This value can be used as an input to
   * payment_profile_id when creating a subscription, in order to re-use a stored payment profile
   * for the same customer.
   */
  id?: number;
  /** The first name of the bank account holder */
  firstName?: string;
  /** The last name of the bank account holder */
  lastName?: string;
  /** The Chargify-assigned ID for the customer record to which the bank account belongs */
  customerId?: number;
  /**
   * The vault that stores the payment profile with the provided vault_token. Use `bogus` for
   * testing.
   */
  currentVault?: BankAccountVault;
  /** The "token" provided by your vault storage for an already stored payment profile */
  vaultToken?: string;
  /** The current billing street address for the bank account */
  billingAddress?: string | null;
  /** The current billing address city for the bank account */
  billingCity?: string | null;
  /** The current billing address state for the bank account */
  billingState?: string | null;
  /** The current billing address zip code for the bank account */
  billingZip?: string | null;
  /** The current billing address country for the bank account */
  billingCountry?: string | null;
  /**
   * (only for Authorize.Net CIM storage): the customerProfileId for the owner of the
   * customerPaymentProfileId provided as the vault_token.
   */
  customerVaultToken?: string | null;
  /** The current billing street address, second line, for the bank account */
  billingAddress2?: string | null;
  /** The bank where the account resides */
  bankName?: string;
  /**
   * A string representation of the stored bank routing number with all but the last 4 digits marked
   * with X's (i.e. 'XXXXXXX1111'). payment_type will be bank_account.
   */
  maskedBankRoutingNumber?: string | null;
  /**
   * A string representation of the stored bank account number with all but the last 4 digits marked
   * with X's (i.e. 'XXXXXXX1111').
   */
  maskedBankAccountNumber?: string | null;
  /** Defaults to checking */
  bankAccountType?: BankAccountType;
  /** Defaults to personal */
  bankAccountHolderType?: BankAccountHolderType;
  /** @default PaymentType.BankAccount */
  paymentType?: PaymentType;
  /**
   * Denotes whether a bank account has been verified by providing the amounts of two small deposits
   * made into the account.
   *
   * @default false
   */
  verified?: boolean;
  siteGatewaySettingId?: number | null;
  gatewayHandle?: string | null;
  /** A timestamp indicating when this payment profile was created */
  createdAt?: Date;
  /** A timestamp indicating when this payment profile was last updated */
  updatedAt?: Date;
};

export const bankAccountPaymentProfileSchema: Schema<BankAccountPaymentProfile> =
  s.object<BankAccountPaymentProfile>({
    id: s.optional(s.int()),
    firstName: s.optional(s.string()),
    lastName: s.optional(s.string()),
    customerId: s.optional(s.int()),
    currentVault: s.optional(s.lazy(() => bankAccountVaultSchema)),
    vaultToken: s.optional(s.string()),
    billingAddress: s.optionalNullable(s.string()),
    billingCity: s.optionalNullable(s.string()),
    billingState: s.optionalNullable(s.string()),
    billingZip: s.optionalNullable(s.string()),
    billingCountry: s.optionalNullable(s.string()),
    customerVaultToken: s.optionalNullable(s.string()),
    billingAddress2: s.optionalNullable(s.string()),
    bankName: s.optional(s.string()),
    maskedBankRoutingNumber: s.optionalNullable(s.string()),
    maskedBankAccountNumber: s.optionalNullable(s.string()),
    bankAccountType: s.optional(s.lazy(() => bankAccountTypeSchema)),
    bankAccountHolderType: s.optional(s.lazy(() => bankAccountHolderTypeSchema)),
    paymentType: s.defaulted(paymentTypeSchema, PaymentType.BankAccount),
    verified: s.defaulted(s.boolean(), false),
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
      bankName: "bank_name",
      maskedBankRoutingNumber: "masked_bank_routing_number",
      maskedBankAccountNumber: "masked_bank_account_number",
      bankAccountType: "bank_account_type",
      bankAccountHolderType: "bank_account_holder_type",
      paymentType: "payment_type",
      siteGatewaySettingId: "site_gateway_setting_id",
      gatewayHandle: "gateway_handle",
      createdAt: "created_at",
      updatedAt: "updated_at",
    },
  });
