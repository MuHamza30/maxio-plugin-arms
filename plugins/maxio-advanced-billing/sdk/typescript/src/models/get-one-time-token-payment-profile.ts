import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { cardTypeSchema, type CardType } from "./card-type.js";
import { creditCardVaultSchema, type CreditCardVault } from "./credit-card-vault.js";

export type GetOneTimeTokenPaymentProfile = {
  id?: string | null;
  firstName: string;
  lastName: string;
  maskedCardNumber: string;
  /** The type of card used. */
  cardType: CardType;
  expirationMonth: number;
  expirationYear: number;
  customerId?: string | null;
  /**
   * The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for
   * testing.
   */
  currentVault: CreditCardVault;
  vaultToken: string;
  billingAddress: string;
  billingAddress2?: string;
  billingCity: string;
  billingCountry: string;
  billingState: string;
  billingZip: string;
  paymentType: string;
  disabled: boolean;
  siteGatewaySettingId: number;
  customerVaultToken?: string | null;
  gatewayHandle?: string | null;
};

export const getOneTimeTokenPaymentProfileSchema: Schema<GetOneTimeTokenPaymentProfile> =
  s.object<GetOneTimeTokenPaymentProfile>({
    id: s.optionalNullable(s.string()),
    firstName: s.string(),
    lastName: s.string(),
    maskedCardNumber: s.string(),
    cardType: cardTypeSchema,
    expirationMonth: s.float64(),
    expirationYear: s.float64(),
    customerId: s.optionalNullable(s.string()),
    currentVault: creditCardVaultSchema,
    vaultToken: s.string(),
    billingAddress: s.string(),
    billingAddress2: s.optional(s.string()),
    billingCity: s.string(),
    billingCountry: s.string(),
    billingState: s.string(),
    billingZip: s.string(),
    paymentType: s.string(),
    disabled: s.boolean(),
    siteGatewaySettingId: s.int(),
    customerVaultToken: s.optionalNullable(s.string()),
    gatewayHandle: s.optionalNullable(s.string()),
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
      billingAddress2: "billing_address_2",
      billingCity: "billing_city",
      billingCountry: "billing_country",
      billingState: "billing_state",
      billingZip: "billing_zip",
      paymentType: "payment_type",
      siteGatewaySettingId: "site_gateway_setting_id",
      customerVaultToken: "customer_vault_token",
      gatewayHandle: "gateway_handle",
    },
  });
