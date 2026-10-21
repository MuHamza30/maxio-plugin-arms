import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { allVaultsSchema, type AllVaults } from "./all-vaults.js";
import { bankAccountHolderTypeSchema, type BankAccountHolderType } from "./bank-account-holder-type.js";
import { bankAccountTypeSchema, type BankAccountType } from "./bank-account-type.js";
import { cardTypeSchema, type CardType } from "./card-type.js";
import { paymentTypeSchema, type PaymentType } from "./payment-type.js";
import { expirationMonth1Schema, type ExpirationMonth1 } from "./unions/expiration-month1.js";
import { expirationYear1Schema, type ExpirationYear1 } from "./unions/expiration-year1.js";

export type CreatePaymentProfile = {
  /** Token received after sending billing information using Maxio.js (formerly Chargify.js). */
  chargifyToken?: string;
  id?: number;
  paymentType?: PaymentType;
  /**
   * First name on card or bank account. If omitted, the first_name from customer attributes will be
   * used.
   */
  firstName?: string;
  /**
   * Last name on card or bank account. If omitted, the last_name from customer attributes will be
   * used.
   */
  lastName?: string;
  maskedCardNumber?: string;
  /** The full credit card number */
  fullNumber?: string;
  /** The type of card used. */
  cardType?: CardType;
  /**
   * (Optional when performing an Import via vault_token, required otherwise) The 1- or 2-digit
   * credit card expiration month, as an integer or string, e.g., 5
   */
  expirationMonth?: ExpirationMonth1;
  /**
   * (Optional when performing an Import via vault_token, required otherwise) The 4-digit credit
   * card expiration year, as an integer or string, e.g., 2012
   */
  expirationYear?: ExpirationYear1;
  /**
   * The credit card or bank account billing street address (e.g., 123 Main St.). This value is
   * merely passed through to the payment gateway.
   */
  billingAddress?: string;
  /** Second line of the customer’s billing address e.g., Apt. 100 */
  billingAddress2?: string | null;
  /**
   * The credit card or bank account billing address city (e.g., “Boston”). This value is merely
   * passed through to the payment gateway.
   */
  billingCity?: string;
  /**
   * The credit card or bank account billing address state (e.g., MA). This value is merely passed
   * through to the payment gateway. This must conform to the
   * [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) in order to be valid for
   * tax locale purposes.
   */
  billingState?: string;
  /**
   * “The credit card or bank account billing address country, required in [ISO_3166-1
   * alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format (e.g., “US”). This value is
   * merely passed through to the payment gateway. Some gateways require country codes in a specific
   * format. Check your gateway’s documentation. If creating an ACH subscription, only US is
   * supported at this time.”
   */
  billingCountry?: string;
  /**
   * The credit card or bank account billing address zip code (e.g., 12345). This value is merely
   * passed through to the payment gateway.
   */
  billingZip?: string;
  /**
   * The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for
   * testing.
   */
  currentVault?: AllVaults;
  /** The “token” provided by your vault storage for an already stored payment profile */
  vaultToken?: string;
  /**
   * (only for Authorize.Net CIM storage or Square) The customerProfileId for the owner of the
   * customerPaymentProfileId provided as the vault_token
   */
  customerVaultToken?: string;
  /** (Required when creating a new payment profile) The Chargify customer id. */
  customerId?: number;
  /**
   * used by merchants that implemented BraintreeBlue javaScript libraries on their own. We
   * recommend using Maxio.js (formerly Chargify.js) instead.
   *
   * @deprecated
   */
  paypalEmail?: string;
  /**
   * used by merchants that implemented BraintreeBlue javaScript libraries on their own. We
   * recommend using Maxio.js (formerly Chargify.js) instead.
   *
   * @deprecated
   */
  paymentMethodNonce?: string;
  /**
   * This attribute is only available if MultiGateway feature is enabled for your Site. This feature
   * is in the Private Beta currently. gateway_handle is used to directly select a gateway where a
   * payment profile will be stored in. Every connected gateway must have a unique gateway handle
   * specified. Read [Multigateway
   * description](https://chargify.zendesk.com/hc/en-us/articles/4407761759643#connecting-with-multiple-gateways)
   * to learn more about new concepts that MultiGateway introduces and the default behavior when
   * this attribute is not passed.
   */
  gatewayHandle?: string;
  /**
   * The 3- or 4-digit Card Verification Value. This value is merely passed through to the payment
   * gateway.
   */
  cvv?: string;
  /**
   * (Required when creating with ACH or GoCardless, optional with Stripe Direct Debit). The name of
   * the bank where the customerʼs account resides
   */
  bankName?: string;
  /**
   * (Optional when creating with GoCardless, required with Stripe Direct Debit). International Bank
   * Account Number. Alternatively, local bank details can be provided.
   */
  bankIban?: string;
  /**
   * (Required when creating with ACH. Optional when creating a subscription with GoCardless). The
   * routing number of the bank. It becomes bank_code while passing via GoCardless API.
   */
  bankRoutingNumber?: string;
  /**
   * (Required when creating with ACH, GoCardless, Stripe BECS or BACS Direct Debit, and bank_iban
   * is blank) The customerʼs bank account number
   */
  bankAccountNumber?: string;
  /**
   * (Optional when creating with GoCardless, required with Stripe BECS or BACS Direct Debit)
   * Branch/Sort code. Alternatively, an IBAN can be provided.
   */
  bankBranchCode?: string;
  /** Defaults to checking */
  bankAccountType?: BankAccountType;
  /** Defaults to personal */
  bankAccountHolderType?: BankAccountHolderType;
  /**
   * (Optional) Used for creating subscription with payment profile imported using vault_token, for
   * proper display in Advanced Billing UI
   */
  lastFour?: string;
};

export const createPaymentProfileSchema: Schema<CreatePaymentProfile> = s.object<CreatePaymentProfile>({
  chargifyToken: s.optional(s.string()),
  id: s.optional(s.int()),
  paymentType: s.optional(s.lazy(() => paymentTypeSchema)),
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  maskedCardNumber: s.optional(s.string()),
  fullNumber: s.optional(s.string()),
  cardType: s.optional(s.lazy(() => cardTypeSchema)),
  expirationMonth: s.optional(s.lazy(() => expirationMonth1Schema)),
  expirationYear: s.optional(s.lazy(() => expirationYear1Schema)),
  billingAddress: s.optional(s.string()),
  billingAddress2: s.optionalNullable(s.string()),
  billingCity: s.optional(s.string()),
  billingState: s.optional(s.string()),
  billingCountry: s.optional(s.string()),
  billingZip: s.optional(s.string()),
  currentVault: s.optional(s.lazy(() => allVaultsSchema)),
  vaultToken: s.optional(s.string()),
  customerVaultToken: s.optional(s.string()),
  customerId: s.optional(s.int()),
  paypalEmail: s.optional(s.string()),
  paymentMethodNonce: s.optional(s.string()),
  gatewayHandle: s.optional(s.string()),
  cvv: s.optional(s.string()),
  bankName: s.optional(s.string()),
  bankIban: s.optional(s.string()),
  bankRoutingNumber: s.optional(s.string()),
  bankAccountNumber: s.optional(s.string()),
  bankBranchCode: s.optional(s.string()),
  bankAccountType: s.optional(s.lazy(() => bankAccountTypeSchema)),
  bankAccountHolderType: s.optional(s.lazy(() => bankAccountHolderTypeSchema)),
  lastFour: s.optional(s.string()),
  _keysMap: {
    chargifyToken: "chargify_token",
    paymentType: "payment_type",
    firstName: "first_name",
    lastName: "last_name",
    maskedCardNumber: "masked_card_number",
    fullNumber: "full_number",
    cardType: "card_type",
    expirationMonth: "expiration_month",
    expirationYear: "expiration_year",
    billingAddress: "billing_address",
    billingAddress2: "billing_address_2",
    billingCity: "billing_city",
    billingState: "billing_state",
    billingCountry: "billing_country",
    billingZip: "billing_zip",
    currentVault: "current_vault",
    vaultToken: "vault_token",
    customerVaultToken: "customer_vault_token",
    customerId: "customer_id",
    paypalEmail: "paypal_email",
    paymentMethodNonce: "payment_method_nonce",
    gatewayHandle: "gateway_handle",
    bankName: "bank_name",
    bankIban: "bank_iban",
    bankRoutingNumber: "bank_routing_number",
    bankAccountNumber: "bank_account_number",
    bankBranchCode: "bank_branch_code",
    bankAccountType: "bank_account_type",
    bankAccountHolderType: "bank_account_holder_type",
    lastFour: "last_four",
  },
});
