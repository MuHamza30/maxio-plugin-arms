import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { cardTypeSchema, type CardType } from "./card-type.js";
import { creditCardVaultSchema, type CreditCardVault } from "./credit-card-vault.js";
import { PaymentType, paymentTypeSchema } from "./payment-type.js";

export type CreditCardPaymentProfile = {
  /**
   * The Chargify-assigned ID of the stored card. This value can be used as an input to
   * payment_profile_id when creating a subscription, in order to re-use a stored payment profile
   * for the same customer.
   */
  id?: number;
  /** The first name of the card holder. */
  firstName?: string;
  /** The last name of the card holder. */
  lastName?: string;
  /**
   * A string representation of the credit card number with all but the last 4 digits masked with
   * X’s (e.g., ‘XXXX-XXXX-XXXX-1234’).
   */
  maskedCardNumber?: string;
  /** The type of card used. */
  cardType?: CardType | null;
  /** An integer representing the expiration month of the card(1 – 12). */
  expirationMonth?: number;
  /** An integer representing the 4-digit expiration year of the card(e.g., ‘2012’). */
  expirationYear?: number;
  /** The Chargify-assigned id for the customer record to which the card belongs. */
  customerId?: number;
  /**
   * The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for
   * testing.
   */
  currentVault?: CreditCardVault;
  /** The “token” provided by your vault storage for an already stored payment profile. */
  vaultToken?: string | null;
  /** The current billing street address for the card. */
  billingAddress?: string | null;
  /** The current billing address city for the card. */
  billingCity?: string | null;
  /** The current billing address state for the card. */
  billingState?: string | null;
  /** The current billing address zip code for the card. */
  billingZip?: string | null;
  /** The current billing address country for the card. */
  billingCountry?: string | null;
  /**
   * (only for Authorize.Net CIM storage): the customerProfileId for the owner of the
   * customerPaymentProfileId provided as the vault_token.
   */
  customerVaultToken?: string | null;
  /** The current billing street address, second line, for the card. */
  billingAddress2?: string | null;
  /** @default PaymentType.CreditCard */
  paymentType?: PaymentType;
  disabled?: boolean;
  /**
   * Token received after sending billing information using Maxio.js (formerly Chargify.js). This
   * token will only be received if passed as a sole attribute of credit_card_attributes (e.g.,
   * tok_9g6hw85pnpt6knmskpwp4ttt).
   */
  chargifyToken?: string;
  siteGatewaySettingId?: number | null;
  /** An identifier of connected gateway. */
  gatewayHandle?: string | null;
  /** A timestamp indicating when this payment profile was created */
  createdAt?: Date;
  /** A timestamp indicating when this payment profile was last updated */
  updatedAt?: Date;
};

export const creditCardPaymentProfileSchema: Schema<CreditCardPaymentProfile> =
  s.object<CreditCardPaymentProfile>({
    id: s.optional(s.int()),
    firstName: s.optional(s.string()),
    lastName: s.optional(s.string()),
    maskedCardNumber: s.optional(s.string()),
    cardType: s.optionalNullable(s.lazy(() => cardTypeSchema)),
    expirationMonth: s.optional(s.int()),
    expirationYear: s.optional(s.int()),
    customerId: s.optional(s.int()),
    currentVault: s.optional(s.lazy(() => creditCardVaultSchema)),
    vaultToken: s.optionalNullable(s.string()),
    billingAddress: s.optionalNullable(s.string()),
    billingCity: s.optionalNullable(s.string()),
    billingState: s.optionalNullable(s.string()),
    billingZip: s.optionalNullable(s.string()),
    billingCountry: s.optionalNullable(s.string()),
    customerVaultToken: s.optionalNullable(s.string()),
    billingAddress2: s.optionalNullable(s.string()),
    paymentType: s.defaulted(paymentTypeSchema, PaymentType.CreditCard),
    disabled: s.optional(s.boolean()),
    chargifyToken: s.optional(s.string()),
    siteGatewaySettingId: s.optionalNullable(s.int()),
    gatewayHandle: s.optionalNullable(s.string()),
    createdAt: s.optional(s.dateTime()),
    updatedAt: s.optional(s.dateTime()),
    _keysMap: {
      firstName: "first_name",
      lastName: "last_name",
      maskedCardNumber: "masked_card_number",
      cardType: "card_type",
      expirationMonth: "expiration_month",
      expirationYear: "expiration_year",
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
      chargifyToken: "chargify_token",
      siteGatewaySettingId: "site_gateway_setting_id",
      gatewayHandle: "gateway_handle",
      createdAt: "created_at",
      updatedAt: "updated_at",
    },
  });
