import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { cardTypeSchema, type CardType } from "./card-type.js";
import { creditCardVaultSchema, type CreditCardVault } from "./credit-card-vault.js";
import { expirationMonthSchema, type ExpirationMonth } from "./unions/expiration-month.js";
import { expirationYearSchema, type ExpirationYear } from "./unions/expiration-year.js";
import { fullNumberSchema, type FullNumber } from "./unions/full-number.js";

export type SubscriptionGroupCreditCard = {
  chargifyToken?: string;
  vaultToken?: string;
  /**
   * The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for
   * testing.
   */
  currentVault?: CreditCardVault;
  gatewayHandle?: string;
  firstName?: string;
  lastName?: string;
  billingAddress?: string;
  billingAddress2?: string;
  billingCity?: string;
  billingState?: string;
  billingZip?: string;
  billingCountry?: string;
  fullNumber?: FullNumber;
  expirationMonth?: ExpirationMonth;
  expirationYear?: ExpirationYear;
  lastFour?: string;
  /** The type of card used. */
  cardType?: CardType;
  customerVaultToken?: string;
  cvv?: string;
  paymentType?: string;
};

export const subscriptionGroupCreditCardSchema: Schema<SubscriptionGroupCreditCard> =
  s.object<SubscriptionGroupCreditCard>({
    chargifyToken: s.optional(s.string()),
    vaultToken: s.optional(s.string()),
    currentVault: s.optional(s.lazy(() => creditCardVaultSchema)),
    gatewayHandle: s.optional(s.string()),
    firstName: s.optional(s.string()),
    lastName: s.optional(s.string()),
    billingAddress: s.optional(s.string()),
    billingAddress2: s.optional(s.string()),
    billingCity: s.optional(s.string()),
    billingState: s.optional(s.string()),
    billingZip: s.optional(s.string()),
    billingCountry: s.optional(s.string()),
    fullNumber: s.optional(s.lazy(() => fullNumberSchema)),
    expirationMonth: s.optional(s.lazy(() => expirationMonthSchema)),
    expirationYear: s.optional(s.lazy(() => expirationYearSchema)),
    lastFour: s.optional(s.string()),
    cardType: s.optional(s.lazy(() => cardTypeSchema)),
    customerVaultToken: s.optional(s.string()),
    cvv: s.optional(s.string()),
    paymentType: s.optional(s.string()),
    _keysMap: {
      chargifyToken: "chargify_token",
      vaultToken: "vault_token",
      currentVault: "current_vault",
      gatewayHandle: "gateway_handle",
      firstName: "first_name",
      lastName: "last_name",
      billingAddress: "billing_address",
      billingAddress2: "billing_address_2",
      billingCity: "billing_city",
      billingState: "billing_state",
      billingZip: "billing_zip",
      billingCountry: "billing_country",
      fullNumber: "full_number",
      expirationMonth: "expiration_month",
      expirationYear: "expiration_year",
      lastFour: "last_four",
      cardType: "card_type",
      customerVaultToken: "customer_vault_token",
      paymentType: "payment_type",
    },
  });
