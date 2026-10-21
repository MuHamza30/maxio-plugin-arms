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

  /**
   * API Exports allow you to generate and download bulk exports of subscriptions, invoices, and
   * proforma invoices as asynchronous batch jobs, useful for reporting or migrating data outside
   * the standard paginated list endpoints. For more information, see [Billing Export Fields
   * Reference](https://docs.maxio.com/insights/data-export/field-references/billing-export-fields-reference#invoice-line-items-fields).
   */
  get apiExports(): ApiExports {
    return (this.#apiExports ??= new ApiExports(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Use the Advance Invoice feature to issue, retrieve, or void an invoice for a subscription ahead
   * of its normal billing schedule, collecting an outstanding balance before the next scheduled
   * renewal. For more information, see [Issue Advance Invoices for Subscription
   * Renewals](https://docs.maxio.com/billing/invoicing/advance-invoices/issue-advance-invoices-for-subscription-renewals).
   */
  get advanceInvoice(): AdvanceInvoice {
    return (this.#advanceInvoice ??= new AdvanceInvoice(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Billing Portal object allows you to enable, disable, and manage customer access to the
   * self-service Billing Portal, where customers can view invoices and manage their own payment
   * details. For more information, see [Understand the Billing
   * Portal](https://docs.maxio.com/billing/billing-portal/overview/understand-the-billing-portal).
   */
  get billingPortal(): BillingPortal {
    return (this.#billingPortal ??= new BillingPortal(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Coupon object defines a discount, either a percentage or a fixed amount, that can be
   * applied to a subscription to reduce the subscription's billing amount.
   *
   * Coupons can be restricted to a specific Product Family, limited to a date range, and configured
   * to apply once or recur over a set duration. For more information, see [Understand
   * Coupons](https://docs.maxio.com/billing/catalog/coupons/understand-coupons).
   */
  get coupons(): Coupons {
    return (this.#coupons ??= new Coupons(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Component Feature object attaches a Feature Template to a Component as a feature catalog
   * item with a concrete value, granting that feature to subscribers through the component.
   *
   * A component feature applies to the whole component by default, or can be scoped to a single
   * component price point as an override. For more information, see [Configure
   * Entitlements](https://docs.maxio.com/billing/catalog/entitlements/configure-entitlements).
   */
  get componentFeatures(): ComponentFeatures {
    return (this.#componentFeatures ??= new ComponentFeatures(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Component object represents an add-on item, such as a metered usage charge, quantity-based
   * feature, or on/off toggle, that can be added to a subscription alongside the subscription's
   * base Product. With the new catalog experience, the UI labels components as Products, while the
   * API keeps the component name. See [Catalog
   * terminology](https://docs.maxio.com/billing/catalog/overview/using-the-new-product-catalog#catalog-terminology).
   *
   * Components belong to a Product Family and are billed according to their pricing scheme and
   * kind. Components can also grant features to subscribers. See the **Create Component Feature
   * Catalog Item** endpoint for details. For more information, see [Understand
   * Products](https://docs.maxio.com/billing/catalog/products/understand-products) and [Hybrid
   * pricing](https://docs.maxio.com/billing/catalog/products/use-product-pricing-schemes#hybrid-pricing).
   */
  get components(): Components {
    return (this.#components ??= new Components(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Component Price Point object defines a specific pricing configuration for a Component,
   * including the price point's rate structure and billing interval.
   *
   * A single Component can have multiple price points, allowing different subscriptions to be
   * billed for the same component under different terms.
   */
  get componentPricePoints(): ComponentPricePoints {
    return (this.#componentPricePoints ??= new ComponentPricePoints(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * The Customer object represents the person or organization being billed and is the anchor that
   * subscriptions, payment profiles, and invoices are all attached to.
   *
   * A customer record stores contact and billing details (name, address, tax exemption status,
   * locale) along with references to related records, such as the customer's default subscription
   * group. For more information, see [Understand Customers for Subscription
   * Management](https://docs.maxio.com/billing/subscriptions/customers/understand-customers-for-subscription-management).
   */
  get customers(): Customers {
    return (this.#customers ??= new Customers(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Custom Fields let you define Metafields for a resource type and manage the Metadata values
   * attached to individual records, so you can capture and store additional data beyond built-in
   * system fields. For more information, see [Understand Custom
   * Fields](https://docs.maxio.com/configuration/advanced-billing/custom-fields/understand-custom-fields).
   */
  get customFields(): CustomFields {
    return (this.#customFields ??= new CustomFields(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Entitlements report what a subscription is allowed to do, and how much of it, based on the
   * features granted by the subscription's products and components.
   *
   * When more than one product or component grants the same feature, the values are aggregated into
   * one entry per feature key and periodicity. For more information, see [Read Subscription
   * Entitlements with the
   * API](https://docs.maxio.com/billing/catalog/entitlements/read-subscription-entitlements-with-the-api).
   */
  get entitlements(): Entitlements {
    return (this.#entitlements ??= new Entitlements(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Event object records a discrete occurrence within your account, such as a payment, renewal,
   * or subscription state change.
   *
   * The key identifies which type of event occurred, and event_specific_data carries a payload
   * whose shape depends on that key.
   */
  get events(): Events {
    return (this.#events ??= new Events(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Segment object defines a distinct pricing variation within an event-based billing metric,
   * based on one or more property values, such as a specific country or usage category.
   *
   * Each segment carries its own set of prices, letting a single metric charge different rates
   * depending on which segment an event falls into.
   */
  get eventsBasedBillingSegments(): EventsBasedBillingSegments {
    return (this.#eventsBasedBillingSegments ??= new EventsBasedBillingSegments(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * The Feature Template object defines a feature once at the site level, such as Single Sign-On, a
   * monthly API call limit, or a support tier.
   *
   * A feature template is not billable on its own. Attach the template to products or components to
   * grant the feature to subscribers. The kind (access_right, usage_limit, or service_right)
   * determines how the feature's value behaves. For more information, see [Configure
   * Entitlements](https://docs.maxio.com/billing/catalog/entitlements/configure-entitlements).
   */
  get featureTemplates(): FeatureTemplates {
    return (this.#featureTemplates ??= new FeatureTemplates(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Insights endpoints provide aggregate site-level statistics, such as customer and
   * subscription counts, giving a high-level snapshot of account activity.
   */
  get insights(): Insights {
    return (this.#insights ??= new Insights(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Invoice object is the billing document generated for a subscription, itemizing charges,
   * taxes, and payments, and tracking amounts owed.
   *
   * The role indicates what triggered the invoice (signup, renewal, usage, proration, etc.), and
   * the status and due_date reflect where an invoice stands in the payment lifecycle. For more
   * information, see [Get Started with
   * Invoicing](https://docs.maxio.com/billing/invoicing/overview/get-started-with-invoicing).
   */
  get invoices(): Invoices {
    return (this.#invoices ??= new Invoices(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Offer object bundles a specific Product, Price Point, and any associated discounts into a
   * single pre-configured signup option that customers can subscribe to directly.
   *
   * Offers are commonly used to power self-service signup pages without requiring each pricing
   * combination to be built manually. For more information, see [Understand
   * Offers](https://docs.maxio.com/billing/catalog/offers/understand-offers).
   */
  get offers(): Offers {
    return (this.#offers ??= new Offers(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Payment Profile object represents a stored payment method on a customer's account. For more
   * information, see [Managing Payment
   * Methods](https://docs.maxio.com/getting-started/maxio-platform-basics/advanced-billing-overview-and-resources/subscription-summary-tabs/managing-payment-methods).
   */
  get paymentProfiles(): PaymentProfiles {
    return (this.#paymentProfiles ??= new PaymentProfiles(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Product Family object groups related Products together for organizational purposes, such as
   * products belonging to a single line of business, each sharing a family-level handle and
   * accounting code. For more information, see [Organize Product
   * Families](https://docs.maxio.com/billing/catalog/plans/organize-product-families).
   */
  get productFamilies(): ProductFamilies {
    return (this.#productFamilies ??= new ProductFamilies(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Product Feature object attaches a Feature Template to a Product as a feature catalog item
   * with a concrete value, granting that feature to subscribers through the product.
   *
   * A product feature applies to the whole product by default, or can be scoped to a single product
   * price point as an override. For more information, see [Configure
   * Entitlements](https://docs.maxio.com/billing/catalog/entitlements/configure-entitlements).
   */
  get productFeatures(): ProductFeatures {
    return (this.#productFeatures ??= new ProductFeatures(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Product object defines what you sell, including default pricing, billing interval, and
   * trial configuration. With the new catalog experience, the UI labels products as Plans, while
   * the API keeps the product name. See [Catalog
   * terminology](https://docs.maxio.com/billing/catalog/overview/using-the-new-product-catalog#catalog-terminology).
   *
   * Products are grouped under a Product Family and are the base type a customer subscribes to.
   * Products can also grant features to subscribers. See the **Create Product Feature Catalog
   * Item** endpoint for details. For more information, see [Understand
   * Plans](https://docs.maxio.com/billing/catalog/plans/understand-plans).
   */
  get products(): Products {
    return (this.#products ??= new Products(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Product Price Point object defines a specific pricing configuration for a Product,
   * including price, billing interval, and trial terms.
   *
   * A single Product can have multiple price points, letting you offer different rates or terms for
   * the same product without creating separate products. For more information, see [Setting Up Plan
   * Price Points](https://docs.maxio.com/billing/catalog/plans/setting-up-plan-price-points).
   */
  get productPricePoints(): ProductPricePoints {
    return (this.#productPricePoints ??= new ProductPricePoints(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Proforma Invoice object is a preview of an upcoming invoice, showing the charges a customer
   * will be billed before the actual invoice is issued. A proforma invoice is not a finalized
   * billing document and is commonly used to give customers advance visibility into what they owe.
   * For more information, see [Understand Proforma
   * Invoices](https://docs.maxio.com/billing/invoicing/proforma-invoices/understand-proforma-invoices).
   */
  get proformaInvoices(): ProformaInvoices {
    return (this.#proformaInvoices ??= new ProformaInvoices(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Reason Code object defines a churn reason that can be presented to customers when they
   * cancel a subscription, such as "too expensive" or "switching providers."
   *
   * Reason codes give merchants visibility into why subscribers are canceling. For more
   * information, see [Configure Churn Reason
   * Codes](https://docs.maxio.com/configuration/advanced-billing/settings/churn-reason-codes).
   */
  get reasonCodes(): ReasonCodes {
    return (this.#reasonCodes ??= new ReasonCodes(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Referral Code object represents a code attached to a subscription, used to track and
   * validate referrals as part of a referral program. For more information, see [Understand
   * Referrals](https://docs.maxio.com/configuration/advanced-billing/understand-referrals).
   */
  get referralCodes(): ReferralCodes {
    return (this.#referralCodes ??= new ReferralCodes(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Sales Commissions allow sellers with financial access to retrieve commission data for a site
   * with Advanced Analytics enabled.
   *
   * These endpoints use a different, user-level authentication method than the rest of the API,
   * since commission data is tied to the seller rather than an individual site.
   */
  get salesCommissions(): SalesCommissions {
    return (this.#salesCommissions ??= new SalesCommissions(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Site object represents a single billing account and holds site-wide configuration, such as
   * default currency, tax settings, net terms, and which billing features are enabled. For more
   * information, see [Understand Advanced Billing
   * Sites](https://docs.maxio.com/configuration/advanced-billing/sites/sites-overview).
   */
  get sites(): Sites {
    return (this.#sites ??= new Sites(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Subscriptions connect a customer to a product and drive all recurring billing for that
   * relationship, including invoice generation, billing start dates, and pricing structure across
   * plan-based and planless configurations. For more information, see [Understand
   * Subscriptions](https://docs.maxio.com/billing/subscriptions/overview/understand-subscriptions).
   */
  get subscriptions(): Subscriptions {
    return (this.#subscriptions ??= new Subscriptions(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Use the Subscription Components object to allocate, adjust, and report usage for the components
   * attached to a subscription, including quantity-based, metered, and event-based components. For
   * more information, see [Managing Components and
   * Usage](https://docs.maxio.com/getting-started/maxio-platform-basics/advanced-billing-overview-and-resources/subscription-summary-tabs/managing-components-and-usage).
   */
  get subscriptionComponents(): SubscriptionComponents {
    return (this.#subscriptionComponents ??= new SubscriptionComponents(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * The Subscription Group object links multiple subscriptions for a single customer under one
   * shared payment profile and collection method, so you can consolidate billing instead of
   * managing payment details separately for each subscription. For more information, see
   * [Understand Subscription
   * Groups](https://docs.maxio.com/billing/subscriptions/configuration/subscription-groups/understand-subscription-groups).
   */
  get subscriptionGroups(): SubscriptionGroups {
    return (this.#subscriptionGroups ??= new SubscriptionGroups(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Subscription Group Invoice Account object lets you manage prepayments and service credits
   * for the shared invoice account of a Subscription Group, applying at the group level rather than
   * to an individual subscription.
   */
  get subscriptionGroupInvoiceAccount(): SubscriptionGroupInvoiceAccount {
    return (this.#subscriptionGroupInvoiceAccount ??= new SubscriptionGroupInvoiceAccount(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * Use the Subscription Group Status object to manage the lifecycle of a Subscription Group as a
   * whole, such as canceling every subscription within the group together.
   */
  get subscriptionGroupStatus(): SubscriptionGroupStatus {
    return (this.#subscriptionGroupStatus ??= new SubscriptionGroupStatus(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * The Subscription Invoice Account object lets you manage a subscription's account balance,
   * including prepayments, service credits, and refunds. For more information, see [Recording
   * Prepayments](https://docs.maxio.com/getting-started/maxio-platform-basics/advanced-billing-overview-and-resources/subscription-summary-tabs/recording-prepayments)
   * and [Give, Deduct, and Apply Service
   * Credits](https://docs.maxio.com/billing/subscriptions/management/subscription-actions/give-deduct-and-apply-service-credits).
   */
  get subscriptionInvoiceAccount(): SubscriptionInvoiceAccount {
    return (this.#subscriptionInvoiceAccount ??= new SubscriptionInvoiceAccount(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * The Subscription Note object stores an internal note attached to a subscription, used to record
   * context, decisions, or history for your team.
   *
   * Notes are never exposed to the customer; they exist purely for internal reference.
   */
  get subscriptionNotes(): SubscriptionNotes {
    return (this.#subscriptionNotes ??= new SubscriptionNotes(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Use the Subscription Products object to migrate a subscription from one product or price point
   * to another, including previewing the effects of a migration before committing to it. For more
   * information, see [Upgrade or Downgrade a
   * Subscription](https://docs.maxio.com/billing/subscriptions/management/subscription-actions/upgrade-or-downgrade-a-subscription).
   */
  get subscriptionProducts(): SubscriptionProducts {
    return (this.#subscriptionProducts ??= new SubscriptionProducts(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * The Subscription Renewals object lets you schedule, preview, and manage a subscription's
   * upcoming renewal, including locking in specific pricing or canceling a scheduled renewal before
   * it takes effect. For more information, see [Understand Scheduled
   * Renewal](https://docs.maxio.com/billing/subscriptions/configuration/term-renewal/scheduled-renewal).
   */
  get subscriptionRenewals(): SubscriptionRenewals {
    return (this.#subscriptionRenewals ??= new SubscriptionRenewals(
      this.#rawClient,
      this.#servers,
      this.#auth,
    ));
  }

  /**
   * Subscription Status allows you to manage a subscription's lifecycle, including retrying a
   * failed payment, canceling, pausing, resuming, and reactivating a subscription. For more
   * information, see [Understand Subscription
   * States](https://docs.maxio.com/billing/subscriptions/management/subscription-states/understand-subscription-states).
   */
  get subscriptionStatus(): SubscriptionStatus {
    return (this.#subscriptionStatus ??= new SubscriptionStatus(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Wallet object is a balance, owned by a subscription and denominated in the unit of a Wallet
   * Product, that you can create, fund, drain, and read through the API.
   *
   * Wallets suit prepaid allowances, credits, and consumption pools that don't map cleanly onto the
   * regular usage-billing cycle. Every balance change is recorded on the wallet's append-only
   * ledger. For more information, see [Understand
   * Wallets](https://docs.maxio.com/billing/catalog/wallets/understand-wallets).
   */
  get wallets(): Wallets {
    return (this.#wallets ??= new Wallets(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Use Wallet Transactions to fund a wallet with a one-time grant, consume units with a direct
   * debit, and read the wallet's append-only ledger. For more information, see [Understand
   * Wallets](https://docs.maxio.com/billing/catalog/wallets/understand-wallets).
   */
  get walletTransactions(): WalletTransactions {
    return (this.#walletTransactions ??= new WalletTransactions(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Wallet Adjustments post a signed correction against a specific grant, or against an overdraft,
   * on a wallet's ledger. Adjustments are intended for support and operations corrections, and each
   * adjustment requires a reason that is recorded on the ledger. For more information, see
   * [Understand Wallets](https://docs.maxio.com/billing/catalog/wallets/understand-wallets).
   */
  get walletAdjustments(): WalletAdjustments {
    return (this.#walletAdjustments ??= new WalletAdjustments(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * Wallet Purchases let a subscription buy additional prepaid units for a wallet, charged
   * according to the subscription's collection method. A purchase can be previewed to quote the
   * price before anything is charged. For more information, see [Understand
   * Wallets](https://docs.maxio.com/billing/catalog/wallets/understand-wallets).
   */
  get walletPurchases(): WalletPurchases {
    return (this.#walletPurchases ??= new WalletPurchases(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Wallet Product object is a billing product created specifically to denominate wallets and
   * to price wallet purchases. A Wallet Product does not belong to a product family, and the Wallet
   * Product behind a wallet cannot be changed after the wallet is created. For more information,
   * see [Create and Manage Wallet
   * Products](https://docs.maxio.com/billing/catalog/wallets/create-and-manage-wallet-products).
   */
  get walletProducts(): WalletProducts {
    return (this.#walletProducts ??= new WalletProducts(this.#rawClient, this.#servers, this.#auth));
  }

  /**
   * The Webhook object represents a single notification sent to your configured endpoint when an
   * event occurs.
   *
   * A webhook tracks delivery status, including when it was last sent, whether the merchant
   * endpoint accepted it, and any error from a failed attempt. For more information, see
   * [Understand Webhooks in Advanced
   * Billing](https://docs.maxio.com/configuration/advanced-billing/webhooks/understand-webhooks-in-advanced-billing).
   */
  get webhooks(): Webhooks {
    return (this.#webhooks ??= new Webhooks(this.#rawClient, this.#servers, this.#auth));
  }
}
