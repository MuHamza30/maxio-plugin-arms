import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { bankAccountHolderTypeSchema, type BankAccountHolderType } from "./bank-account-holder-type.js";
import { bankAccountTypeSchema, type BankAccountType } from "./bank-account-type.js";
import { bankAccountVaultSchema, type BankAccountVault } from "./bank-account-vault.js";
import { paymentTypeSchema, type PaymentType } from "./payment-type.js";

export type BankAccountAttributes = {
  chargifyToken?: string;
  /**
   * (Required when creating a subscription with ACH or GoCardless) The name of the bank where the
   * customer’s account resides
   */
  bankName?: string;
  /**
   * (Required when creating a subscription with ACH; optional when creating a subscription with
   * GoCardless). The routing number of the bank. It becomes bank_code while passing via GoCardless
   * API.
   */
  bankRoutingNumber?: string;
  /**
   * (Required when creating a subscription with ACH. Required when creating a subscription with
   * GoCardless and bank_iban is blank) The customerʼs bank account number
   */
  bankAccountNumber?: string;
  /** Defaults to checking */
  bankAccountType?: BankAccountType;
  /**
   * (Optional when creating a subscription with GoCardless) Branch code. Alternatively, an IBAN can
   * be provided.
   */
  bankBranchCode?: string;
  /**
   * (Optional when creating a subscription with GoCardless). International Bank Account Number.
   * Alternatively, local bank details can be provided.
   */
  bankIban?: string;
  /** Defaults to personal */
  bankAccountHolderType?: BankAccountHolderType;
  paymentType?: PaymentType;
  /**
   * The vault that stores the payment profile with the provided vault_token. Use `bogus` for
   * testing.
   */
  currentVault?: BankAccountVault;
  vaultToken?: string;
  /**
   * (only for Authorize.Net CIM storage or Square) The customerProfileId for the owner of the
   * customerPaymentProfileId provided as the vault_token
   */
  customerVaultToken?: string;
};

export const bankAccountAttributesSchema: Schema<BankAccountAttributes> = s.object<BankAccountAttributes>({
  chargifyToken: s.optional(s.string()),
  bankName: s.optional(s.string()),
  bankRoutingNumber: s.optional(s.string()),
  bankAccountNumber: s.optional(s.string()),
  bankAccountType: s.optional(s.lazy(() => bankAccountTypeSchema)),
  bankBranchCode: s.optional(s.string()),
  bankIban: s.optional(s.string()),
  bankAccountHolderType: s.optional(s.lazy(() => bankAccountHolderTypeSchema)),
  paymentType: s.optional(s.lazy(() => paymentTypeSchema)),
  currentVault: s.optional(s.lazy(() => bankAccountVaultSchema)),
  vaultToken: s.optional(s.string()),
  customerVaultToken: s.optional(s.string()),
  _keysMap: {
    chargifyToken: "chargify_token",
    bankName: "bank_name",
    bankRoutingNumber: "bank_routing_number",
    bankAccountNumber: "bank_account_number",
    bankAccountType: "bank_account_type",
    bankBranchCode: "bank_branch_code",
    bankIban: "bank_iban",
    bankAccountHolderType: "bank_account_holder_type",
    paymentType: "payment_type",
    currentVault: "current_vault",
    vaultToken: "vault_token",
    customerVaultToken: "customer_vault_token",
  },
});
