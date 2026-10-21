import * as s from "../core/validation/index.js";
import type { Schema } from "../core/validation/schema.js";
import { allVaultsSchema, type AllVaults } from "./all-vaults.js";
import { cardTypeSchema, type CardType } from "./card-type.js";

export type UpdatePaymentProfile = {
  /** The first name of the card holder. */
  firstName?: string;
  /** The last name of the card holder. */
  lastName?: string;
  /** The full credit card number */
  fullNumber?: string;
  /** The type of card used. */
  cardType?: CardType;
  /**
   * (Optional when performing an Import via vault_token, required otherwise) The 1- or 2-digit
   * credit card expiration month, as an integer or string, e.g., 5
   */
  expirationMonth?: string;
  /**
   * (Optional when performing an Import via vault_token, required otherwise) The 4-digit credit
   * card expiration year, as an integer or string, e.g., 2012
   */
  expirationYear?: string;
  /**
   * The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for
   * testing.
   */
  currentVault?: AllVaults;
  /**
   * The credit card or bank account billing street address (e.g., 123 Main St.). This value is
   * merely passed through to the payment gateway.
   */
  billingAddress?: string;
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
   * The credit card or bank account billing address zip code (e.g., 12345). This value is merely
   * passed through to the payment gateway.
   */
  billingZip?: string;
  /**
   * The credit card or bank account billing address country, required in [ISO_3166-1
   * alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format (e.g., “US”). This value is
   * merely passed through to the payment gateway. Some gateways require country codes in a specific
   * format. Check your gateway’s documentation. If creating an ACH subscription, only US is
   * supported at this time.
   */
  billingCountry?: string;
  /** Second line of the customer’s billing address, e.g., Apt. 100 */
  billingAddress2?: string | null;
};

export const updatePaymentProfileSchema: Schema<UpdatePaymentProfile> = s.object<UpdatePaymentProfile>({
  firstName: s.optional(s.string()),
  lastName: s.optional(s.string()),
  fullNumber: s.optional(s.string()),
  cardType: s.optional(s.lazy(() => cardTypeSchema)),
  expirationMonth: s.optional(s.string()),
  expirationYear: s.optional(s.string()),
  currentVault: s.optional(s.lazy(() => allVaultsSchema)),
  billingAddress: s.optional(s.string()),
  billingCity: s.optional(s.string()),
  billingState: s.optional(s.string()),
  billingZip: s.optional(s.string()),
  billingCountry: s.optional(s.string()),
  billingAddress2: s.optionalNullable(s.string()),
  _keysMap: {
    firstName: "first_name",
    lastName: "last_name",
    fullNumber: "full_number",
    cardType: "card_type",
    expirationMonth: "expiration_month",
    expirationYear: "expiration_year",
    currentVault: "current_vault",
    billingAddress: "billing_address",
    billingCity: "billing_city",
    billingState: "billing_state",
    billingZip: "billing_zip",
    billingCountry: "billing_country",
    billingAddress2: "billing_address_2",
  },
});
