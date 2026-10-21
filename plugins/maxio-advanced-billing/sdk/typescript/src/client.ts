import { buildAuthSchemes, type AuthSchemes } from "./auth-schemes.js";
import type { ClientOptions } from "./client-options.js";
import { buildCoreClientOptions } from "./core/client-options.js";
import { RawClient } from "./core/raw-client.js";
import * as host from "./core/runtime-environment.js";
import * as s from "./core/validation/index.js";
import { AdvanceInvoice } from "./resources/advance-invoice.js";
import { ApiExports } from "./resources/api-exports.js";
import { BillingPortal } from "./resources/billing-portal.js";
import { ComponentFeatures } from "./resources/component-features.js";
import { ComponentPricePoints } from "./resources/component-price-points.js";
import { Components } from "./resources/components.js";
import { Coupons } from "./resources/coupons.js";
import { CustomFields } from "./resources/custom-fields.js";
import { Customers } from "./resources/customers.js";
import { Entitlements } from "./resources/entitlements.js";
import { EventsBasedBillingSegments } from "./resources/events-based-billing-segments.js";
import { Events } from "./resources/events.js";
import { FeatureTemplates } from "./resources/feature-templates.js";
import { Insights } from "./resources/insights.js";
import { Invoices } from "./resources/invoices.js";
import { Offers } from "./resources/offers.js";
import { PaymentProfiles } from "./resources/payment-profiles.js";
import { ProductFamilies } from "./resources/product-families.js";
import { ProductFeatures } from "./resources/product-features.js";
import { ProductPricePoints } from "./resources/product-price-points.js";
import { Products } from "./resources/products.js";
import { ProformaInvoices } from "./resources/proforma-invoices.js";
import { ReasonCodes } from "./resources/reason-codes.js";
import { ReferralCodes } from "./resources/referral-codes.js";
import { SalesCommissions } from "./resources/sales-commissions.js";
import { Sites } from "./resources/sites.js";
import { SubscriptionComponents } from "./resources/subscription-components.js";
import { SubscriptionGroupInvoiceAccount } from "./resources/subscription-group-invoice-account.js";
import { SubscriptionGroupStatus } from "./resources/subscription-group-status.js";
import { SubscriptionGroups } from "./resources/subscription-groups.js";
import { SubscriptionInvoiceAccount } from "./resources/subscription-invoice-account.js";
import { SubscriptionNotes } from "./resources/subscription-notes.js";
import { SubscriptionProducts } from "./resources/subscription-products.js";
import { SubscriptionRenewals } from "./resources/subscription-renewals.js";
import { SubscriptionStatus } from "./resources/subscription-status.js";
import { Subscriptions } from "./resources/subscriptions.js";
import { WalletAdjustments } from "./resources/wallet-adjustments.js";
import { WalletProducts } from "./resources/wallet-products.js";
import { WalletPurchases } from "./resources/wallet-purchases.js";
import { WalletTransactions } from "./resources/wallet-transactions.js";
import { Wallets } from "./resources/wallets.js";
import { Webhooks } from "./resources/webhooks.js";
import { buildServers, type Servers } from "./servers.js";

/**
 *
 * Maxio Advanced Billing (formerly Chargify) provides an HTTP-based API that conforms to the
 * principles of REST. One of the many reasons to use Advanced Billing is the immense feature set
 * and [client libraries](page:development-tools/client-libraries). The Maxio API returns JSON
 * responses as the primary and recommended format, but XML is also provided as a backwards
 * compatible option for merchants who require it.
 *
 * ## Steps to make your first Maxio Advanced Billing API call
 *
 * 1. [Sign-up](https://app.chargify.com/signup/maxio-billing-sandbox) or
 *    [log-in](https://app.chargify.com/login.html) to your [test
 *    site](https://maxio.zendesk.com/hc/en-us/articles/24250712113165-Testing-Overview) account.
 * 2. [Setup authentication](https://maxio.zendesk.com/hc/en-us/articles/24294819360525-API-Keys)
 *    credentials.
 * 3. [Submit an API request and verify the
 *    response](page:development-tools/client-libraries#make-your-first-maxio-advanced-billing-api-request).
 * 5. Test the Advanced Billing [integrations](https://www.maxio.com/integrations).
 *
 * Next, you can explore [authentication methods](page:introduction/authentication), [basic
 * concepts](page:introduction/basic-concepts/connected-sites) for interacting with Advanced Billing
 * via the API, and the entire set of [application-based
 * documentation](https://docs.maxio.com/hc/en-us) to aid in your discovery of the product.
 *
 * ### Request Example
 *
 * The following example uses the curl command-line tool to make an API request.
 *
 * **Request**
 *
 * curl -u <api_key>:x -H Accept:application/json -H Content-Type:application/json
 * https://acme.chargify.com/subscriptions.json
 */
export class MaxioAdvancedBillingClient {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;
  #apiExports?: ApiExports;
  #advanceInvoice?: AdvanceInvoice;
  #billingPortal?: BillingPortal;
  #coupons?: Coupons;
  #componentFeatures?: ComponentFeatures;
  #components?: Components;
  #componentPricePoints?: ComponentPricePoints;
  #customers?: Customers;
  #customFields?: CustomFields;
  #entitlements?: Entitlements;
  #events?: Events;
  #eventsBasedBillingSegments?: EventsBasedBillingSegments;
  #featureTemplates?: FeatureTemplates;
  #insights?: Insights;
  #invoices?: Invoices;
  #offers?: Offers;
  #paymentProfiles?: PaymentProfiles;
  #productFamilies?: ProductFamilies;
  #productFeatures?: ProductFeatures;
  #products?: Products;
  #productPricePoints?: ProductPricePoints;
  #proformaInvoices?: ProformaInvoices;
  #reasonCodes?: ReasonCodes;
  #referralCodes?: ReferralCodes;
  #salesCommissions?: SalesCommissions;
  #sites?: Sites;
  #subscriptions?: Subscriptions;
  #subscriptionComponents?: SubscriptionComponents;
  #subscriptionGroups?: SubscriptionGroups;
  #subscriptionGroupInvoiceAccount?: SubscriptionGroupInvoiceAccount;
  #subscriptionGroupStatus?: SubscriptionGroupStatus;
  #subscriptionInvoiceAccount?: SubscriptionInvoiceAccount;
  #subscriptionNotes?: SubscriptionNotes;
  #subscriptionProducts?: SubscriptionProducts;
  #subscriptionRenewals?: SubscriptionRenewals;
  #subscriptionStatus?: SubscriptionStatus;
  #wallets?: Wallets;
  #walletTransactions?: WalletTransactions;
  #walletAdjustments?: WalletAdjustments;
  #walletPurchases?: WalletPurchases;
  #walletProducts?: WalletProducts;
  #webhooks?: Webhooks;

  constructor(options: ClientOptions = {}) {
    this.#rawClient = new RawClient({
      ...buildCoreClientOptions(options, "MAXIO_ADVANCED_BILLING_CLIENT_LOG"),
      defaultHeaders: [
        { name: "User-Agent", value: "MaxioAdvancedBillingClient/1.0.0 TypeScript", schema: s.string() },
        { name: "X-APIMatic-Lang", value: "TypeScript", schema: s.string() },
        { name: "X-APIMatic-Package-Version", value: "1.0.0", schema: s.string() },
        { name: "X-APIMatic-Gen-Version", value: "4.0.0", schema: s.string() },
        { name: "X-APIMatic-OS", value: host.operatingSystem(), schema: s.optional(s.string()) },
        { name: "X-APIMatic-Runtime", value: host.runtimeDescription(), schema: s.optional(s.string()) },
      ],
      defaultQuery: [],
      defaultPathParams: [],
    });

    this.#servers = buildServers(options);

    this.#auth = buildAuthSchemes(options);
  }

  get apiExports(): ApiExports {
    return (this.#apiExports ??= new ApiExports(this.#rawClient, this.#servers, this.#auth));
  }

  get advanceInvoice(): AdvanceInvoice {
    return (this.#advanceInvoice ??= new AdvanceInvoice(this.#rawClient, this.#servers, this.#auth));
  }

  get billingPortal(): BillingPortal {
    return (this.#billingPortal ??= new BillingPortal(this.#rawClient, this.#servers, this.#auth));
  }

  get coupons(): Coupons {
    return (this.#coupons ??= new Coupons(this.#rawClient, this.#servers, this.#auth));
  }

  get componentFeatures(): ComponentFeatures {
    return (this.#componentFeatures ??= new ComponentFeatures(this.#rawClient, this.#servers, this.#auth));
  }

  get components(): Components {
    return (this.#components ??= new Components(this.#rawClient, this.#servers, this.#auth));
  }

  get componentPricePoints(): ComponentPricePoints {
    return (this.#componentPricePoints ??= new ComponentPricePoints(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get customers(): Customers {
    return (this.#customers ??= new Customers(this.#rawClient, this.#servers, this.#auth));
  }

  get customFields(): CustomFields {
    return (this.#customFields ??= new CustomFields(this.#rawClient, this.#servers, this.#auth));
  }

  get entitlements(): Entitlements {
    return (this.#entitlements ??= new Entitlements(this.#rawClient, this.#servers, this.#auth));
  }

  get events(): Events {
    return (this.#events ??= new Events(this.#rawClient, this.#servers, this.#auth));
  }

  get eventsBasedBillingSegments(): EventsBasedBillingSegments {
    return (this.#eventsBasedBillingSegments ??= new EventsBasedBillingSegments(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get featureTemplates(): FeatureTemplates {
    return (this.#featureTemplates ??= new FeatureTemplates(this.#rawClient, this.#servers, this.#auth));
  }

  get insights(): Insights {
    return (this.#insights ??= new Insights(this.#rawClient, this.#servers, this.#auth));
  }

  get invoices(): Invoices {
    return (this.#invoices ??= new Invoices(this.#rawClient, this.#servers, this.#auth));
  }

  get offers(): Offers {
    return (this.#offers ??= new Offers(this.#rawClient, this.#servers, this.#auth));
  }

  get paymentProfiles(): PaymentProfiles {
    return (this.#paymentProfiles ??= new PaymentProfiles(this.#rawClient, this.#servers, this.#auth));
  }

  get productFamilies(): ProductFamilies {
    return (this.#productFamilies ??= new ProductFamilies(this.#rawClient, this.#servers, this.#auth));
  }

  get productFeatures(): ProductFeatures {
    return (this.#productFeatures ??= new ProductFeatures(this.#rawClient, this.#servers, this.#auth));
  }

  get products(): Products {
    return (this.#products ??= new Products(this.#rawClient, this.#servers, this.#auth));
  }

  get productPricePoints(): ProductPricePoints {
    return (this.#productPricePoints ??= new ProductPricePoints(this.#rawClient, this.#servers, this.#auth));
  }

  get proformaInvoices(): ProformaInvoices {
    return (this.#proformaInvoices ??= new ProformaInvoices(this.#rawClient, this.#servers, this.#auth));
  }

  get reasonCodes(): ReasonCodes {
    return (this.#reasonCodes ??= new ReasonCodes(this.#rawClient, this.#servers, this.#auth));
  }

  get referralCodes(): ReferralCodes {
    return (this.#referralCodes ??= new ReferralCodes(this.#rawClient, this.#servers, this.#auth));
  }

  get salesCommissions(): SalesCommissions {
    return (this.#salesCommissions ??= new SalesCommissions(this.#rawClient, this.#servers, this.#auth));
  }

  get sites(): Sites {
    return (this.#sites ??= new Sites(this.#rawClient, this.#servers, this.#auth));
  }

  get subscriptions(): Subscriptions {
    return (this.#subscriptions ??= new Subscriptions(this.#rawClient, this.#servers, this.#auth));
  }

  get subscriptionComponents(): SubscriptionComponents {
    return (this.#subscriptionComponents ??= new SubscriptionComponents(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get subscriptionGroups(): SubscriptionGroups {
    return (this.#subscriptionGroups ??= new SubscriptionGroups(this.#rawClient, this.#servers, this.#auth));
  }

  get subscriptionGroupInvoiceAccount(): SubscriptionGroupInvoiceAccount {
    return (this.#subscriptionGroupInvoiceAccount ??= new SubscriptionGroupInvoiceAccount(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get subscriptionGroupStatus(): SubscriptionGroupStatus {
    return (this.#subscriptionGroupStatus ??= new SubscriptionGroupStatus(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get subscriptionInvoiceAccount(): SubscriptionInvoiceAccount {
    return (this.#subscriptionInvoiceAccount ??= new SubscriptionInvoiceAccount(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get subscriptionNotes(): SubscriptionNotes {
    return (this.#subscriptionNotes ??= new SubscriptionNotes(this.#rawClient, this.#servers, this.#auth));
  }

  get subscriptionProducts(): SubscriptionProducts {
    return (this.#subscriptionProducts ??= new SubscriptionProducts(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get subscriptionRenewals(): SubscriptionRenewals {
    return (this.#subscriptionRenewals ??= new SubscriptionRenewals(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  get subscriptionStatus(): SubscriptionStatus {
    return (this.#subscriptionStatus ??= new SubscriptionStatus(this.#rawClient, this.#servers, this.#auth));
  }

  get wallets(): Wallets {
    return (this.#wallets ??= new Wallets(this.#rawClient, this.#servers, this.#auth));
  }

  get walletTransactions(): WalletTransactions {
    return (this.#walletTransactions ??= new WalletTransactions(this.#rawClient, this.#servers, this.#auth));
  }

  get walletAdjustments(): WalletAdjustments {
    return (this.#walletAdjustments ??= new WalletAdjustments(this.#rawClient, this.#servers, this.#auth));
  }

  get walletPurchases(): WalletPurchases {
    return (this.#walletPurchases ??= new WalletPurchases(this.#rawClient, this.#servers, this.#auth));
  }

  get walletProducts(): WalletProducts {
    return (this.#walletProducts ??= new WalletProducts(this.#rawClient, this.#servers, this.#auth));
  }

  get webhooks(): Webhooks {
    return (this.#webhooks ??= new Webhooks(this.#rawClient, this.#servers, this.#auth));
  }
}
