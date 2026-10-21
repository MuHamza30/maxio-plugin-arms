import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/**
 * The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for
 * testing.
 */
export const CreditCardVault = {
  Adyen: "adyen",
  Authorizenet: "authorizenet",
  Beanstream: "beanstream",
  BlueSnap: "blue_snap",
  Bogus: "bogus",
  Braintree1: "braintree1",
  BraintreeBlue: "braintree_blue",
  Checkout: "checkout",
  Cybersource: "cybersource",
  Elavon: "elavon",
  Eway: "eway",
  EwayRapid: "eway_rapid",
  EwayRapidStd: "eway_rapid_std",
  Firstdata: "firstdata",
  Forte: "forte",
  Litle: "litle",
  MaxioPayments: "maxio_payments",
  Maxp: "maxp",
  Moduslink: "moduslink",
  Moneris: "moneris",
  Nmi: "nmi",
  Orbital: "orbital",
  PaymentExpress: "payment_express",
  Paymill: "paymill",
  Paypal: "paypal",
  PaypalComplete: "paypal_complete",
  Pin: "pin",
  Square: "square",
  Stripe: "stripe",
  StripeConnect: "stripe_connect",
  TrustCommerce: "trust_commerce",
  Unipaas: "unipaas",
  Wirecard: "wirecard",
} as const;
export type CreditCardVault = (typeof CreditCardVault)[keyof typeof CreditCardVault] | (string & {});

export const creditCardVaultSchema: EnumSchema<CreditCardVault> = s.enumOf<CreditCardVault>(CreditCardVault);
