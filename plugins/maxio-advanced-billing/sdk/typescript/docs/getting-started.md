# Getting started with the Maxio Advanced Billing TypeScript SDK

**Read when:** you are about to answer any Maxio Advanced Billing TypeScript SDK contract question or write any SDK code. This is the SDK's identity and lookup layer (TypeScript/JavaScript only) — install, the single import specifier `maxio-advanced-billing`, the server environments and the base-URL knob, the auth pattern, the SDK map that ships inside the installed package (`sdk-map.md` + `map/operations/`) and how to traverse it, and the file table naming the one source file owning each fact the map leaves to the source.

> **Who this doc is for.** This is the **lookup layer** for anyone writing Maxio Advanced Billing TypeScript SDK code — it is yours to follow directly and fully. Ground every contract fact here (in the SDK map, and in the source files it names) rather than in recall, and carry those facts onto a contract sheet before you implement. `docs/integrate.md` is the workflow that sends you here: read it first if you have not.

This is the **SDK-specific** entry point. For general patterns that apply to any APIMatic-generated TypeScript SDK (client construction, auth, calling endpoints, models, error handling, resilience, testing), see the companion API-agnostic docs: `docs/client-initialization.md`, `docs/authentication.md`, `docs/calling-endpoints.md`, `docs/models.md`, `docs/error-handling.md`, `docs/configuration-resilience.md` and `docs/testing.md`.

**This page and those companion pages are complementary.** This page is authoritative for the SDK's *identity and surface* (what to install, what to import, the resources, which file owns which fact). The companion pages are the *usage layer* on top: the best-practice way to call each piece and the gotchas a signature cannot show. Which of them you read, and when, is decided in one place: `docs/integrate.md`, Step 1c. This page only says what each one is for.

## SDK identity

Verified against `package.json` and `sdk-map.md` of the generated package at version `1.0.0`. **Re-verify after a version bump** — this page is a snapshot, not a live read.

| Fact | Value |
| --- | --- |
| API | Maxio Advanced Billing |
| Package name (what you install, and what you import) | `maxio-advanced-billing` — **not on npm**; it installs from this SDK folder (see *Install*) |
| Import specifier | `maxio-advanced-billing` — the package root is the **only** entry; deep imports do not resolve |
| SDK source | this SDK folder, the directory holding `sdk-map.md` and this `docs/` directory — generated with these docs, nothing to clone |
| Version | `1.0.0` (API spec version `1.0`) |
| Client class | `MaxioAdvancedBillingClient` (`src/client.ts`) — one class, no sync/async split |
| Options type | `ClientOptions` (`src/client-options.ts`) — types only, no resolver beside it |
| Client construction | `new MaxioAdvancedBillingClient(options: ClientOptions = {})` — the argument is optional, as is **every** field on it, so `new MaxioAdvancedBillingClient()` compiles. Fields: `serverEnvironment` · `serverOptions` · `retry` · `fetch` · `basicAuth`. `retry` is the `RetryOptions` policy; its defaults retry a GET, HEAD, PUT or OPTIONS call up to `3` times and bound each attempt by `retry.timeout` = `60_000` ms, and every one of them can be changed |
| Auth | **HTTP Basic** — set `ClientOptions.basicAuth` |
| Environments | 2 environments (`ServerEnvironment.Us` *(default)*, `ServerEnvironment.Eu`) × 2 server groups |
| Base-URL config | `serverOptions.<group>.baseUrl` (`src/servers.ts`) |
| Log environment variable | `MAXIO_ADVANCED_BILLING_CLIENT_LOG` |
| Node floor | `>=20.3` (`engines.node`) |
| Runtime dependency | `zod` (`^4.1.0`), imported as `zod/v4-mini` — the only one |
| Module format | dual ESM + CommonJS folder dialects (`dist/esm`, `dist/commonjs`) behind one export |
| Typing | the package ships its own `.d.ts` and is generated under strict TypeScript. Callers get full inference — **a type error against this SDK is a real contract violation, not noise** |
| Surface | 285 operations · 42 resources · 617 models · 121 open enums · 103 unions · 201 per-operation error subclasses |

The table above is **orientation, not a copy-paste recipe** — it gives you the names and facts (install, import specifier, the auth *pattern*, the base-URL knob), while the actual integration code comes from the companion docs. **Integration workflow** below says which page governs which step, and `docs/integrate.md`, Step 1c, says when you read them.

## Install

**A published package.** Install it the ordinary way, `npm install maxio-advanced-billing@<version>`, or from
the tarball your team distributes, `npm install <file>.tgz`. The package carries this SDK's agent files (see
below), so there is nothing more to do.

**Not published yet: from this SDK folder.** Install the package from this SDK folder (the directory holding `package.json`, `sdk-map.md` and this `docs/` directory; `<sdk-folder>` below is its path):

```bash
npm --prefix <sdk-folder>/ install
npm --prefix <sdk-folder>/ run build
npm install <sdk-folder>/
```

**That dependency is local to this machine.** `npm install <directory>` records the package in `package.json` and the lockfile as a `file:` path from your project into this SDK folder, and links it in `node_modules` to that directory, so the project installs only where this SDK folder sits at that path — a teammate needs this SDK folder at that path and all three commands run against their copy, which ships unbuilt and without its dependencies, and a CI runner without this SDK folder cannot install it. Say so when you hand the work over. A copy of this SDK folder reinstalled or updated somewhere else replaces that directory, so run all three commands again against the new copy.

The installed package carries everything its `files` list packs: `dist/`, `src/`, `sdk-map.md`, the pages under `map/operations/`, `api-reference.md`, `AGENTS.md`, `docs/`, `knowledge/` and `recipes/`. So **every lookup on this page works as soon as the install finishes**, and the workflow, Maxio's rules and the recipes are inside `node_modules/maxio-advanced-billing/` beside the map. The copy ships as source, not pre-built, which is why the commands build it where it sits before installing it.

Do not vendor its `src/` into your project, point `tsconfig` `paths` at a throwaway clone, or import from `dist/` directly. Installing the package properly is what makes the `exports` map, the shipped `.d.ts` chain and the dual-dialect resolution behave the way the SDK expects — **and it is what puts the SDK map inside `node_modules`, which is where every lookup below reads it from**. Requires Node `>=20.3` (`engines.node`).

## Imports — one entry, and only one

**Every** public name is re-exported from the package root — the client, `ClientOptions`, `ServerEnvironment`, 841 model types with the schema value beside each, the error classes, and the runtime types (`ApiPromise`, `Pageable`, `PageableApiResult`, `ApiResult`, `RequestOptions`, `RetryOptions`, `RequestRetryOptions`, `Declared`, `Schema`, `EnumSchema`, `Encoded`).

```ts
import { MaxioAdvancedBillingClient, ServerEnvironment, ApiError, MaxioAdvancedBillingError } from "maxio-advanced-billing";
import type { ClientOptions, AchAgreement } from "maxio-advanced-billing";
```

Things the specifier alone will not tell you:

- **Deep imports do not resolve.** The `exports` map exposes `.` and `./package.json` and nothing else, so `maxio-advanced-billing/models/…` fails (`TS2307`) even though the file exists in the shipped `src/`. Every `Source` path on the SDK map is where to **read** a shape, never what to import.
- **⚠ The SDK exports a model type literally named `Event`** (`src/models/event.ts`, schema `eventSchema`). Import it unaliased and it **shadows the global `Event`** for the rest of the file. Alias it: `import type { Event as SdkEvent } from "maxio-advanced-billing"`.
- **From CommonJS**, the typed spelling is `import sdk = require("maxio-advanced-billing")`. A plain `require` destructure runs but yields `any`.
- **`instanceof` is reliable within one dialect.** A process that loads both (`import` in one file, `require` in another) gets two independent copies of every error class, and `instanceof` across that boundary is `false` — narrow on `err.kind` / `err.payload.kind` / `err.name` there.

Under `verbatimModuleSyntax`, names carrying no runtime value (`ClientOptions`, every model type) must be imported with `import type`. Under `exactOptionalPropertyTypes`, **omit or spread** an absent optional field rather than assigning `undefined` to it.

## Environments

`ClientOptions.serverEnvironment` selects one environment for the whole client (`src/servers.ts`). `ServerEnvironment` is a `const` object with a derived union type — not a TypeScript `enum` — and unlike the model enums it is **closed**, so only its declared members are assignable.

| Group | Environment | Base URL | Override at |
| --- | --- | --- | --- |
| `production` | `us` *(default)* | `https://{site}.chargify.com` | `serverOptions.production.baseUrl` |
| `production` | `eu` | `https://{site}.ebilling.maxio.com` | `serverOptions.production.baseUrl` |
| `ebb` | `us` *(default)* | `https://events.chargify.com/{site}` | `serverOptions.ebb.baseUrl` |
| `ebb` | `eu` | `https://events.chargify.com/{site}` | `serverOptions.ebb.baseUrl` |

Consequences to state on every contract sheet that touches configuration:

- Constructing the client with no options selects **`ServerEnvironment.Us`**, silently.
- An override merges with the built-in default **per group-and-environment pair, key by key**; a `baseUrl` override replaces the template verbatim, template variable values are percent-encoded into it; server variables are filled in once, as the client is built, and only the path parameters expand per request.
- Each operation is bound to one server group at generation time. A map block carries a **Server** bullet only when its group is not `production`.
- An environment value the SDK does not know throws `ConfigurationError` **from the constructor** — every server group is resolved once, as the client is built — so no operation method throws synchronously.

## Auth pattern (1 scheme)

Authentication is **per operation**: every operation declares the requirement it enforces and the SDK sends exactly that. Each block on a map page carries an **Auth** bullet, `none` included. There is no client-global switch and no per-call override. 285 of the 285 operations require a credential and 0 are public.

| `ClientOptions` field | Scheme kind | What the SDK sends |
| --- | --- | --- |
| `basicAuth` | HTTP Basic | `Authorization: Basic <base64 of username:password>` |

<!-- maxio:start -->
The client construction is in **Maxio: site and credentials** below. A sample that sets `basicAuth` alone builds a client with no site.
<!-- maxio:end -->

**Every credential field is optional at the type level and that is a trap worth flagging on every sheet.** Omit one and nothing fails at construction — the request simply goes out without that credential and the server decides. Most APIs then answer `401`; one that serves anonymous traffic answers `200` and hides the omission entirely. So a `401` on a call you believed was authenticated is usually an unset field rather than an SDK failure; verify the field is set rather than waiting for a `401` to tell you, and check the operation's **Auth** bullet against what the client was actually given.

Three more behaviours the type does not show:

- **A credential may be a function.** Every field typed `TokenProvider` is re-read on **every** request with no caching, so a key can rotate without rebuilding the client. An empty string counts as absent; a function counts as present without being invoked.
- **Composition is emitted, not configured.** Where the spec puts two schemes in one requirement the SDK sends **both**; where it lists alternatives it sends the **first configured** one, in the order the **Auth** bullet prints them.
- **A 401 invalidates the cached credential.** On a 401 (401 only, not 403) the SDK clears whatever that operation's scheme had cached, so the *next* call re-acquires; the current request still rejects.

See `docs/authentication.md` for the full picture.

<!-- maxio:start -->
## Maxio: site and credentials

A client needs three values, and all three come from configuration (`knowledge/rules.md` R1, R2):

- **The API key** is the basic-auth username. The password is the letter `x`.
- **The site** is your subdomain: `acme` for `acme.chargify.com`. Set it at `serverOptions.production.site`, and at `serverOptions.ebb.site` as well: the events operations (`recordEvent`, `bulkRecordEvents`) use the `ebb` server group, which has a `site` of its own.
- **The region** is `serverEnvironment`: `ServerEnvironment.Us` (`chargify.com`) or `ServerEnvironment.Eu` (`ebilling.maxio.com`, for EU-hosted accounts only).

The type requires none of them, and leaving one out throws nothing. A client built without a site calls a site literally named `subdomain` (`https://subdomain.chargify.com`). One built without a region calls the US host. One built without `basicAuth` sends no credential. So set all three explicitly, and fail at startup when one is missing:

```ts
import { MaxioAdvancedBillingClient, ServerEnvironment } from "maxio-advanced-billing";

const REGIONS: Record<string, ServerEnvironment> = { us: ServerEnvironment.Us, eu: ServerEnvironment.Eu };

export function buildMaxioClient(): MaxioAdvancedBillingClient {
  // The variable names are yours. The site is the subdomain: "acme" for acme.chargify.com.
  const { MAXIO_API_KEY: apiKey, MAXIO_SITE: site, MAXIO_REGION: region } = process.env;
  const serverEnvironment = REGIONS[region ?? ""];

  // Fail at startup. Left out, none of these fails later: the client just calls the wrong host.
  if (!apiKey) throw new Error("MAXIO_API_KEY is not set");
  if (!site) throw new Error("MAXIO_SITE is not set");
  if (!serverEnvironment) throw new Error("MAXIO_REGION must be us or eu");

  return new MaxioAdvancedBillingClient({
    serverEnvironment,
    serverOptions: { production: { site }, ebb: { site } },
    basicAuth: { username: apiKey, password: "x" },
  });
}
```

`serverOptions` has no environment level on this SDK. The keys are `serverOptions.production.site` and `serverOptions.ebb.site`, and `serverEnvironment` picks the region for both.

A client built this way still has the SDK's default retry policy and its 60 second timeout. `docs/configuration-resilience.md`, "Maxio: retries, timeouts and paging", says what to change.

Keep the test site and the live site as separate configurations. Before a smoke or a destructive test, read the site and stop unless it is a test site:

```ts
export async function assertTestSite(client: MaxioAdvancedBillingClient): Promise<void> {
  const { site } = await client.sites.readSite();
  if (site.test !== true) throw new Error("This is not a Maxio test site. Stop.");
}
```

The Sales Commission operations (`listSalesCommissionSettings`, `listSalesReps`, `readSalesRep`) are the exception R1 names: they take a user's API key as a bearer token, on the subdomain `app`. With this SDK that means a second client, built with `serverOptions: { production: { site: "app" } }` and no `basicAuth`, and the token passed on each call in the request's `authorization` field as `"Bearer <key>"`. On a client that has `basicAuth`, the basic header replaces that field.
<!-- maxio:end -->

## Resources

Resources are **memoized lazy getters** on the client (`client.<attr>`). Their classes are exported only for their merged namespaces — the per-operation request and error types — and for `instanceof`; their constructors take engine internals that are not exported, so reach a resource only through its getter.

| Attribute | Class | Ops | Operations |
| --- | --- | --- | --- |
| `client.apiExports` | `ApiExports` | 9 | `exportInvoices` · `exportProformaInvoices` · `exportSubscriptions` · `listExportedInvoices` · `listExportedProformaInvoices` · `listExportedSubscriptions` · `readInvoicesExport` · `readProformaInvoicesExport` · `readSubscriptionsExport` |
| `client.advanceInvoice` | `AdvanceInvoice` | 3 | `issueAdvanceInvoice` · `readAdvanceInvoice` · `voidAdvanceInvoice` |
| `client.billingPortal` | `BillingPortal` | 4 | `enableBillingPortalForCustomer` · `readBillingPortalLink` · `resendBillingPortalInvitation` · `revokeBillingPortalAccess` |
| `client.coupons` | `Coupons` | 14 | `archiveCoupon` · `createCoupon` · `createCouponSubcodes` · `createOrUpdateCouponCurrencyPrices` · `deleteCouponSubcode` · `findCoupon` · `listCouponSubcodes` · `listCoupons` · `listCouponsForProductFamily` · `readCoupon` · `readCouponUsage` · `updateCoupon` · `updateCouponSubcodes` · `validateCoupon` |
| `client.componentFeatures` | `ComponentFeatures` | 6 | `createComponentFeature` · `listComponentFeatures` · `readComponentFeature` · `removeComponentFeature` · `restoreComponentFeature` · `updateComponentFeature` |
| `client.components` | `Components` | 12 | `archiveComponent` · `createEventBasedComponent` · `createMeteredComponent` · `createOnOffComponent` · `createPrepaidUsageComponent` · `createQuantityBasedComponent` · `findComponent` · `listComponents` · `listComponentsForProductFamily` · `readComponent` · `updateComponent` · `updateProductFamilyComponent` |
| `client.componentPricePoints` | `ComponentPricePoints` | 12 | `archiveComponentPricePoint` · `bulkCreateComponentPricePoints` · `cloneComponentPricePoint` · `createComponentPricePoint` · `createCurrencyPrices` · `listAllComponentPricePoints` · `listComponentPricePoints` · `promoteComponentPricePointToDefault` · `readComponentPricePoint` · `unarchiveComponentPricePoint` · `updateComponentPricePoint` · `updateCurrencyPrices` |
| `client.customers` | `Customers` | 7 | `createCustomer` · `deleteCustomer` · `listCustomerSubscriptions` · `listCustomers` · `readCustomer` · `readCustomerByReference` · `updateCustomer` |
| `client.customFields` | `CustomFields` | 9 | `createMetadata` · `createMetafields` · `deleteMetadata` · `deleteMetafield` · `listMetadata` · `listMetadataForResourceType` · `listMetafields` · `updateMetadata` · `updateMetafield` |
| `client.entitlements` | `Entitlements` | 1 | `readSubscriptionEntitlements` |
| `client.events` | `Events` | 3 | `listEvents` · `listSubscriptionEvents` · `readEventsCount` |
| `client.eventsBasedBillingSegments` | `EventsBasedBillingSegments` | 6 | `bulkCreateSegments` · `bulkUpdateSegments` · `createSegment` · `deleteSegment` · `listSegmentsForPricePoint` · `updateSegment` |
| `client.featureTemplates` | `FeatureTemplates` | 6 | `archiveFeatureTemplate` · `createFeatureTemplate` · `listFeatureTemplates` · `readFeatureTemplate` · `restoreFeatureTemplate` · `updateFeatureTemplate` |
| `client.insights` | `Insights` | 4 | `listMrrMovements` · `listMrrPerSubscription` · `readMrr` · `readSiteStats` |
| `client.invoices` | `Invoices` | 19 | `createInvoice` · `deleteInvoice` · `issueInvoice` · `listConsolidatedInvoiceSegments` · `listCreditNotes` · `listInvoiceEvents` · `listInvoices` · `previewCustomerInformationChanges` · `readCreditNote` · `readInvoice` · `recordPaymentForInvoice` · `recordPaymentForMultipleInvoices` · `recordPaymentForSubscription` · `refundInvoice` · `reopenInvoice` · `sendInvoice` · `updateCustomerInformation` · `updateInvoice` · `voidInvoice` |
| `client.offers` | `Offers` | 5 | `archiveOffer` · `createOffer` · `listOffers` · `readOffer` · `unarchiveOffer` |
| `client.paymentProfiles` | `PaymentProfiles` | 12 | `changeSubscriptionDefaultPaymentProfile` · `changeSubscriptionGroupDefaultPaymentProfile` · `createPaymentProfile` · `deleteSubscriptionGroupPaymentProfile` · `deleteSubscriptionsPaymentProfile` · `deleteUnusedPaymentProfile` · `listPaymentProfiles` · `readOneTimeToken` · `readPaymentProfile` · `sendRequestUpdatePaymentEmail` · `updatePaymentProfile` · `verifyBankAccount` |
| `client.productFamilies` | `ProductFamilies` | 4 | `createProductFamily` · `listProductFamilies` · `listProductsForProductFamily` · `readProductFamily` |
| `client.productFeatures` | `ProductFeatures` | 6 | `createProductFeature` · `listProductFeatures` · `readProductFeature` · `removeProductFeature` · `restoreProductFeature` · `updateProductFeature` |
| `client.products` | `Products` | 6 | `archiveProduct` · `createProduct` · `listProducts` · `readProduct` · `readProductByHandle` · `updateProduct` |
| `client.productPricePoints` | `ProductPricePoints` | 11 | `archiveProductPricePoint` · `bulkCreateProductPricePoints` · `createProductCurrencyPrices` · `createProductPricePoint` · `listAllProductPricePoints` · `listProductPricePoints` · `promoteProductPricePointToDefault` · `readProductPricePoint` · `unarchiveProductPricePoint` · `updateProductCurrencyPrices` · `updateProductPricePoint` |
| `client.proformaInvoices` | `ProformaInvoices` | 10 | `createConsolidatedProformaInvoice` · `createProformaInvoice` · `createSignupProformaInvoice` · `deliverProformaInvoice` · `listProformaInvoices` · `listSubscriptionGroupProformaInvoices` · `previewProformaInvoice` · `previewSignupProformaInvoice` · `readProformaInvoice` · `voidProformaInvoice` |
| `client.reasonCodes` | `ReasonCodes` | 5 | `createReasonCode` · `deleteReasonCode` · `listReasonCodes` · `readReasonCode` · `updateReasonCode` |
| `client.referralCodes` | `ReferralCodes` | 1 | `validateReferralCode` |
| `client.salesCommissions` | `SalesCommissions` | 3 | `listSalesCommissionSettings` · `listSalesReps` · `readSalesRep` |
| `client.sites` | `Sites` | 3 | `clearSite` · `listChargifyJsPublicKeys` · `readSite` |
| `client.subscriptions` | `Subscriptions` | 12 | `activateSubscription` · `applyCouponsToSubscription` · `createSubscription` · `findSubscription` · `listSubscriptions` · `overrideSubscription` · `previewSubscription` · `purgeSubscription` · `readSubscription` · `removeCouponFromSubscription` · `updatePrepaidSubscriptionConfiguration` · `updateSubscription` |
| `client.subscriptionComponents` | `SubscriptionComponents` | 17 | `activateEventBasedComponent` · `allocateComponent` · `allocateComponents` · `bulkRecordEvents` · `bulkResetSubscriptionComponentsPricePoints` · `bulkUpdateSubscriptionComponentsPricePoints` · `createUsage` · `deactivateEventBasedComponent` · `deletePrepaidUsageAllocation` · `listAllocations` · `listSubscriptionComponents` · `listSubscriptionComponentsForSite` · `listUsages` · `previewAllocations` · `readSubscriptionComponent` · `recordEvent` · `updatePrepaidUsageAllocationExpirationDate` |
| `client.subscriptionGroups` | `SubscriptionGroups` | 9 | `addSubscriptionToGroup` · `createSubscriptionGroup` · `deleteSubscriptionGroup` · `findSubscriptionGroup` · `listSubscriptionGroups` · `readSubscriptionGroup` · `removeSubscriptionFromGroup` · `signupWithSubscriptionGroup` · `updateSubscriptionGroupMembers` |
| `client.subscriptionGroupInvoiceAccount` | `SubscriptionGroupInvoiceAccount` | 4 | `createSubscriptionGroupPrepayment` · `deductSubscriptionGroupServiceCredit` · `issueSubscriptionGroupServiceCredit` · `listPrepaymentsForSubscriptionGroup` |
| `client.subscriptionGroupStatus` | `SubscriptionGroupStatus` | 4 | `cancelDelayedCancellationForGroup` · `cancelSubscriptionsInGroup` · `initiateDelayedCancellationForGroup` · `reactivateSubscriptionGroup` |
| `client.subscriptionInvoiceAccount` | `SubscriptionInvoiceAccount` | 7 | `createPrepayment` · `deductServiceCredit` · `issueServiceCredit` · `listPrepayments` · `listServiceCredits` · `readAccountBalances` · `refundPrepayment` |
| `client.subscriptionNotes` | `SubscriptionNotes` | 5 | `createSubscriptionNote` · `deleteSubscriptionNote` · `listSubscriptionNotes` · `readSubscriptionNote` · `updateSubscriptionNote` |
| `client.subscriptionProducts` | `SubscriptionProducts` | 2 | `migrateSubscriptionProduct` · `previewSubscriptionProductMigration` |
| `client.subscriptionRenewals` | `SubscriptionRenewals` | 11 | `cancelScheduledRenewalConfiguration` · `createScheduledRenewalConfiguration` · `createScheduledRenewalConfigurationItem` · `deleteScheduledRenewalConfigurationItem` · `listScheduledRenewalConfigurations` · `lockInScheduledRenewalImmediately` · `readScheduledRenewalConfiguration` · `scheduleScheduledRenewalLockIn` · `unpublishScheduledRenewalConfiguration` · `updateScheduledRenewalConfiguration` · `updateScheduledRenewalConfigurationItem` |
| `client.subscriptionStatus` | `SubscriptionStatus` | 10 | `cancelDelayedCancellation` · `cancelDunning` · `cancelSubscription` · `initiateDelayedCancellation` · `pauseSubscription` · `previewRenewal` · `reactivateSubscription` · `resumeSubscription` · `retrySubscription` · `updateAutomaticSubscriptionResumption` |
| `client.wallets` | `Wallets` | 5 | `archiveWallet` · `createWallet` · `listWallets` · `readWallet` · `updateWallet` |
| `client.walletTransactions` | `WalletTransactions` | 2 | `createWalletTransaction` · `listWalletTransactions` |
| `client.walletAdjustments` | `WalletAdjustments` | 1 | `createWalletAdjustment` |
| `client.walletPurchases` | `WalletPurchases` | 2 | `createWalletPurchase` · `previewWalletPurchase` |
| `client.walletProducts` | `WalletProducts` | 7 | `archiveWalletProduct` · `createWalletProduct` · `listWalletProducts` · `readWalletProduct` · `readWalletProductUsage` · `unarchiveWalletProduct` · `updateWalletProduct` |
| `client.webhooks` | `Webhooks` | 6 | `createEndpoint` · `enableWebhooks` · `listEndpoints` · `listWebhooks` · `replayWebhooks` · `updateEndpoint` |

Every operation has the same call shape — `op(request, options?)`, one **flat, channel-blind** request object first and `RequestOptions` (`{ signal, retry, logging }`) second — and returns `ApiPromise<T, E>`.

⚠ **The request type name is not uniformly `<Operation>Request`.** 56 operations take `<Operation>RequestParams` instead: `issueAdvanceInvoice`, `updateComponent`, `cloneComponentPricePoint`, `createComponentPricePoint`, `createCurrencyPrices`, `updateComponentPricePoint`, `updateCurrencyPrices`, `createCustomer`, `updateCustomer`, `createMetadata`, `createMetafields`, `updateMetadata`, `createSegment`, `updateSegment`, `createFeatureTemplate`, `updateFeatureTemplate`, `createInvoice`, `issueInvoice`, `refundInvoice`, `sendInvoice`, `updateInvoice`, `voidInvoice`, `createOffer`, `createPaymentProfile`, `updatePaymentProfile`, `createProductFamily`, `bulkCreateProductPricePoints`, `createProductCurrencyPrices`, `createProductPricePoint`, `updateProductPricePoint`, `deliverProformaInvoice`, `createReasonCode`, `updateReasonCode`, `activateSubscription`, `createSubscription`, `overrideSubscription`, `updateSubscription`, `createUsage`, `previewAllocations`, `createSubscriptionGroup`, `reactivateSubscriptionGroup`, `createPrepayment`, `deductServiceCredit`, `issueServiceCredit`, `refundPrepayment`, `updateSubscriptionNote`, `reactivateSubscription`, `createWallet`, `updateWallet`, `createWalletTransaction`, `createWalletAdjustment`, `createWalletPurchase`, `createWalletProduct`, `updateWalletProduct`, `enableWebhooks`, `replayWebhooks`. Take the name from the operation's **Signature** bullet on its map page; never construct it from the method name.

## SDK map — look up first, open the file second

The SDK ships a generated map, and `package.json`'s `files` list includes it, so **installing the package gives you the map** — no clone is needed. It sits at the package root, the directory holding `package.json` and the `src/` tree:

- **`sdk-map.md`** — the index. It opens with Maxio's ten rules, the same ten `AGENTS.md` carries. Then: client construction with the full `ClientOptions` table, the *Not on this SDK* table, the one error family with `ApiResult` and `.asApiResult()`, wire serialization for every channel, servers and auth, runtime and packaging, and the link table into the operations pages.
- **`map/operations/<resource>.md`** — one page per resource, one `###` block per operation, with bullets in a fixed order. The first is **Provider rules (Maxio)** or **Provider notes (Maxio)**, where Maxio has rules or notes for the operation: it links that operation's section under `knowledge/operations/`, and a block without it has no provider notes. Then come **Server**, **Signature**, **Wire** (verb and route), **Auth**, **Request body**, **SDK-sent**, **Returns**, **Error**, **Error arms** — then a **Fields** table giving every request field its channel, wire name, type, required flag and default, and a **Type sources** table naming the declaring file and schema value of every type the operation mentions.

Locate the installed package before you rely on a lookup:

```bash
node -e "console.log(require.resolve('maxio-advanced-billing/package.json'))"
```

This page ships in the same package as the map: the map is one directory up from this `docs/` directory, so there is always a map to read. What the command settles is whether the project builds against this same copy. If it prints this folder (directly, or through `node_modules/maxio-advanced-billing/`, which links here when the SDK was installed by path), read on. If it prints a different directory, the project uses another copy of the SDK: read the map, the docs and the knowledge in that copy. If it fails, the package is not installed in the project yet: install it (see *Install*). A fact that neither the map nor the file it names settles is `UNVERIFIED`: say what would settle it rather than answering from memory.

Every `Source` path on the map is relative to that package root, so `src/models/<file>.ts` opens as written from there — the package ships its `src/` tree, so the path resolves inside `node_modules/maxio-advanced-billing/` exactly as the map writes it. An import specifier ending `.js` inside that source is the NodeNext spelling of the sibling `.ts` file.

**The map is the locator; the source files are the shapes.** Read the map first — signatures, routes, request fields with their channels and defaults, return types, error arms, and which file declares a type are all answered there without opening a single `.ts` file. Then open the one file the map names for what it deliberately does not carry: a model's members, whether each is required, optional or nullable, and an enum's members with their wire values — the `as const` object in the enum's own file (for an enum inside a model, the file the model imports it from). The map says so itself — *"Shapes live only in the source … Do not derive the path from the type name."*

**`sdk-map.md` carries the invariants every operation block assumes, so read it before any `map/operations/` page**; the pages are written to be read beside it. And **silence means the default**: the index states what holds for every operation — the call shape, the flat channel-blind request object, the `ApiPromise<T, E>` return, the default server group, no pagination and no streaming — and a block departs from one only by saying so. Take the default and move on rather than opening the source to confirm it.

**The map carries shapes; what an operation *means* lives elsewhere.** When *what* to pass depends on meaning — which values a field accepts beyond its type, a rule that couples two fields, what a defaulted header actually selects — the map will not settle it. Read the operation's provider notes first: the **Provider rules** or **Provider notes** bullet on its block links one section under `knowledge/operations/`. Where that does not settle it, look the operation up in `api-reference.md` at the package root, keyed by the same signature. That file is close to a megabyte: search it for the one operation and never read it whole. Do this *before* writing the sheet row, and record what you found. A value you already "know" for a field the map types as a plain `string` is a lookup, not a recall — the memory ban applies to it.

## Contract facts — the map first, then the source file

**Six of these are map lookups — don't open a source file for them:** an operation's signature; its request fields with channel, wire name, required flag and default; its return type; its error subclass and the arms with the status each covers; the `ClientOptions` fields and their defaults; and the environments, base URLs and auth wiring.

The table below covers everything else, and the full body behind a map row. Paths are relative to `node_modules/maxio-advanced-billing/`:

| Question | File |
| --- | --- |
| A model's members, required (`f: T`) vs optional (`f?: T`) vs required-nullable (`f: T \| null`) | `src/models/<file the Type sources table names>.ts` |
| The operation method body and the request it builds | `src/resources/<resource>.ts` |
| The per-operation request and error types (merged namespace) | the `export namespace <Resource>` block at the foot of the same file |
| Client construction, resource getters | `src/client.ts` |
| `ClientOptions` fields | `src/client-options.ts` |
| Environments, base URLs, override merging | `src/servers.ts` |
| Auth scheme wiring, token endpoint, credential placement | `src/auth-schemes.ts`, `src/core/auth/credentials.ts`, `src/core/auth/oauth2-strategies.ts` |
| The transport: the attempt loop, `fetch` resolution, 401 invalidation, 2xx-vs-error split | `src/core/raw-client.ts` |
| Error classes and `ErrorKind` | `src/core/errors.ts`, `src/core/api-error.ts` |
| `ApiPromise`, `ApiResult`, `.asApiResult()`, the `Symbol.species` behaviour | `src/core/api-promise.ts` |
| `RequestOptions` (it is `{ signal, retry, logging }` and nothing else) | `src/core/api-request.ts` |
| `RetryOptions` and its defaults, `RequestRetryOptions`, backoff, `Retry-After`, `RetryAttempt` | `src/core/retry.ts` |
| `LoggingOptions` and its defaults (`defaultLoggingOptions`), `RequestLoggingOptions`, `Logger`, `LogDetails` | `src/core/logging.ts` |
| Schema decode/encode, `SchemaError`, `Encoded<T>` | `src/core/validation/schema-error.ts` and its directory |
| Wire serialization per channel | `src/core/param-value.ts`, `src/core/url.ts`, `src/core/headers.ts`, `src/core/params.ts` |
| What an operation *means* — field semantics, coupling rules | the operation's section under `knowledge/operations/`, linked from its map block. Then `api-reference.md` at the package root: search it for the one operation, never read it whole |

**Read scoped.** Search for the one symbol and read the lines around it rather than whole files, and never copy a design comment's rationale onto a contract sheet — the sheet carries facts an implementer must obey, not the reasoning behind them.

Keep lookups cheap — the rules that keep a session's context small:

- Collect the contracts for **every** in-scope operation in **one** pass — signature, request fields with channels and defaults, required members, the error arms, enum values — into a short **contract sheet** in your plan, then implement from the sheet. Don't re-open a map page per field, and never re-look-up a fact the sheet already carries.
- Recurse into a model's members only where the task actually sets them — a full transitive expansion is hundreds of rows nobody needs.
- **Never grep, glob or `find` the package to *locate* a type** — the map is the locator, and it says so. Grep only *inside* the file its **Type sources** table names, for the symbol. A sweep for a cross-cutting *shape* is a different question and is fine: "every field typed `unknown`", "every required-nullable member" are things nothing indexes, and one targeted `grep -rn` over `src/models/` is the right tool — record what it found on the sheet.
- Trust the compiler over this page: if a name here ever fails to type-check, re-read the file the table above names and report the drift; never patch around it from memory.

## Sensitive data — check the request models before you log anything

Whether this API's **request** models carry fields you must never log — card or bank numbers, personal data, message content — is a shape question: each request model's declaring file (the map's **Type sources** table names it) lists every field. If the scope touches such a field, four generator facts decide your logging posture (all in `docs/configuration-resilience.md`): a JSON request body is logged **verbatim** when `logRequestBody` is on, with no redaction; a form body is masked only by deny-list; a per-call `RequestOptions.logging` level turns the request body on for that call, whatever the client set; and leaving `ClientOptions.logging` without a `logger` or a `level` arms the `MAXIO_ADVANCED_BILLING_CLIENT_LOG` environment variable, which turns logging and both header switches on with no code change and no deploy — though never the body. So on any build that can carry such a field: `logRequestBody` stays off, no call on those paths passes a per-call level, `ClientOptions.logging.level` is set explicitly in production, and your own diagnostics never echo a request body on those paths.

The SDK never logs a response body, but your own code may. Responses are often safer — many APIs return masked variants of what requests carry raw — but that too is a model-shape fact: check the response model's file before assuming.

<!-- maxio:start -->
## API knowledge: Maxio's business rules

Contract facts come from the map; Maxio's business rules come from `knowledge/` in this SDK folder.
`knowledge/README.md` says what each file holds, `knowledge/index.json` maps every operation, by its call
name in this SDK and by the spec's operationId, to its notes, and each operation block in
`map/operations/` links its own notes section. `docs/integrate.md`, "Provider knowledge", says which
sections to read and when. It is a short list: never read `knowledge/` whole.

The rules name wire fields and leave the SDK-specific "how" to four sections of these pages. The headings
are fixed, so a rule can point at one by name. Read the section a rule sends you to, not the whole page:

| Section | Says how to | Rules |
| --- | --- | --- |
| this page, **Maxio: site and credentials** | set the API key, the site and the region, and fail at startup when one is missing | R1, R2 |
| `docs/models.md`, **Fields the spec does not declare** | send `uniqueness_token` at the body root, and read `action_link` from a 422 | R12, R13 |
| `docs/configuration-resilience.md`, **Maxio: retries, timeouts and paging** | turn off automatic retry for one call, raise a write's timeout above 120 seconds, stop the automatic retry of a 429, stop a paging loop | R8, R10, R11, R12 |
| `docs/error-handling.md`, **Maxio: reading a rejection** | print the status and Maxio's own message from an SDK error, and tell a rejection from an unknown outcome | R13 |
<!-- maxio:end -->

## Integration workflow: the companion page for each step

Each step below names the companion page that governs it and the trap the signature hides (in *parens*). When you read those pages is decided in `docs/integrate.md`, Step 1c, and this list adds nothing to that. A typical integration reaches the steps in this order:

1. **Client construction & lifetime** — read **`docs/client-initialization.md`** before you write `new MaxioAdvancedBillingClient(…)`. (*The signature won't tell you:* every option is optional, so a client built with no arguments compiles and talks to the default environment with no credential; the client must be **long-lived and app-scoped**, never rebuilt per request, because the resource getters live on it; there is no `close()` or `dispose()` — it owns no pool, only a `fetch`; and when no `fetch` is reachable the **constructor** throws `ConfigurationError`, not the first call.)
2. **Authentication** — read **`docs/authentication.md`** before you set credentials. The scheme is `basicAuth` on `ClientOptions`. (*The signature won't tell you:* the field is optional — omit it and every request goes out unauthenticated with no failure at construction; and a 401 invalidates the cache without retrying the current call. Load secrets from the environment or a secret store, never hardcode.)
3. **Calling an endpoint** — read **`docs/calling-endpoints.md`** before the first `client.<resource>.<operation>(…)` call. (*The signature won't tell you:* the request object is **flat and channel-blind** — a field named `body` *is* the whole request body and every other field is fanned out to path, query or header by the SDK, so nothing is nested by channel; **an omitted field that has a default is still sent, with that default**; **32 operations resolve to `undefined`**; and `.asApiResult()` must be called on the value the operation returned, because `ApiPromise` overrides `Symbol.species` and `.then()`/`.catch()` hand back a plain `Promise` with the method gone.)
4. **Models** — read **`docs/models.md`** the moment a request/response member is not a plain string or number. (*The signature won't tell you:* models are plain `type`s built from object literals — no constructor, no builder; `f?: T` means omit the key, while `f: T | null` is **required and nullable** and `null` is a distinct value; enums are **open** (`const` companion plus a union admitting `(string & {})`), so the schema validates the base type only and an unknown server value round-trips instead of throwing — use `.values` to test membership yourself; and every type has a schema companion usable in both directions.)
5. **Error handling** — read **`docs/error-handling.md`** before you write any `try/catch`. (*The signature won't tell you:* every operational failure is **one family**, `MaxioAdvancedBillingError`, narrowed on `err.kind` — `"api"` is an API error status, carried by `ApiError` and its per-operation subclasses — while four throwables sit outside it (`ConfigurationError` from the constructor, `SchemaError` from a codec called directly, a `TypeError` for a bug, and a caller abort's own `reason`), so a `catch` that tests the family has to rethrow the rest; **arm tags are schema-derived, not statuses** (see the sheet checklist below); a malformed 2xx body rejects with `DecodeError`, not `ApiError`, and `.asApiResult()` does not convert it; and a missing response field the schema permits is silently `undefined` rather than any error at all.)
6. **Configuration & resilience** — read **`docs/configuration-resilience.md`** when you set the base URL, timeouts, retries, proxies, TLS, or logging. (*The signature won't tell you:* **retrying is on by default** — the default policy retries a GET, HEAD, PUT or OPTIONS call on `408`, `429`, `500`, `502`, `503` and `504` and on a dropped connection or timeout, and every one of those is a `RetryOptions` field you can change; a write is repeated only when `httpMethodsToRetry` names its method; `retry: { maxRetries: 0 }` turns it off, one call overrides it through `RequestOptions.retry`, and a `401` is not retried by default; `retry.timeout` bounds **one attempt**, up to its response headers, not the whole call, and `0` is a zero-length deadline while a value `setTimeout` cannot honour falls back to the default; **logging is off by default** — `ClientOptions.logging` turns it on with a `logger` or a `level`, and so does the `MAXIO_ADVANCED_BILLING_CLIENT_LOG` environment variable when code sets neither, but a request body is logged only when code sets `logRequestBody`, and then a JSON body **verbatim**, with no redaction; **there are no hooks, middleware or interceptors** — `ClientOptions.fetch` is the one transport extension point, `onRetry` being the only built-in callback; and a `fetch` replacement is called with the attempt's `Request` and no `init`, so one that does not forward that `Request`, or its `signal`, makes both each attempt's timeout and every `RequestOptions.signal` inert.)
7. **Testing** — read **`docs/testing.md`** before you stub the SDK. (*The signature won't tell you:* the seam is **`ClientOptions.fetch`**, not the client class and not the resource classes — whose constructors take unexported engine internals, so they cannot be instantiated in a test; stub bodies in **wire shape** and let the SDK decode them; assert on the request the SDK actually built, headers included; and cover the failure kinds an `ApiError`-only test misses, `DecodeError` above all.)

## What a contract sheet must carry for this SDK

Beyond the usual signatures and model members, a contract sheet for the Maxio Advanced Billing TypeScript SDK is incomplete without these, because each one is a decision the implementer cannot make correctly from the signature alone.

1. **Which host each deployment talks to**, and where that is set. The members are `ServerEnvironment.Us`, `ServerEnvironment.Eu`, defaulting to `ServerEnvironment.Us` when the field is unset.
2. **32 operations resolve to `undefined`** — `await` gives you nothing to inspect, so **`.asApiResult()` is the only way to observe their status and headers** — decide the mode at write time, not by retrofit.
3. **The exact request type name per operation**, taken from the **Signature** bullet — 56 operations take `<Operation>RequestParams`, not `<Operation>Request`.
4. **Every request field with its channel, wire name and default**, because the request object is flat and channel-blind and the SDK fans fields out. An omitted field that has a default is still sent with that default, so a defaulted header shapes the response whether or not the sheet mentions it. The generator injects an `Idempotency-Key` on every non-GET operation that does not declare that header itself — minted once per call and invisible to you. Every retry of that call re-sends the **same** key, which is what makes naming a write in `httpMethodsToRetry` safe where the provider deduplicates on it; but the next call mints a new one, so a call your own code repeats is two submissions. Any caller-supplied idempotency or request-id field is the only idempotency that spans calls, and `RequestOptions` is `{ signal, retry, logging }` only.
5. **Required vs optional vs required-nullable** for every model member the task sets — `f: T` required, `f?: T` omit the key, `f: T | null` required and nullable. And that under `exactOptionalPropertyTypes` an absent optional is **omitted or spread**, never assigned `undefined`.
6. **The error arms for each operation in scope, with the status each covers — and the warning that arm tags are schema-derived, not status codes.** Every operation rejects with its own `ApiError` subclass narrowed on `err.payload.kind`, and a tag comes from the arm's **body schema**: an arm whose body is a direct model reference is named after that model in lower camel (`"validationError"`), and every other body — a primitive, an array, a map, or no content — is named `"error{Status}"` (`"error400"`, `"error4XX"`, `"errorDefault"`), with a numeric suffix on the second of two arms that would otherwise land on the same name. The same tag means different statuses on different operations, and the same status carries different tags — so a tag is only meaningful beside the arm table it came from, and a shared helper that switches on `kind` across operations is a bug. 201 of 285 operations declare typed error bodies; the rest reject with the base `ApiError`. Every operation also carries an always-present `"undeclared"` arm holding `rawBody: ArrayBuffer`, for which **matcher precedence** matters: an exact numeric status is looked up across the whole table first, then the first covering range, and last a `"default"` arm where the spec declared one — whose body, if it does not fit, falls to `"undeclared"` rather than throwing.
7. **That a malformed or drifted 2xx body rejects with `DecodeError`, not `ApiError`, in both response modes** — `.asApiResult()` converts an HTTP error status, never any other failure. Any sheet row for a call whose result is used must name the members the implementer has to assert on, because a thin or truncated body decodes without complaint and the hole surfaces later.
8. **The retry policy this integration needs.** Retrying is on by default — `ClientOptions.retry` sets it for the client and `RequestOptions.retry` overrides it per call — so the sheet says whether the defaults fit, which writes (if any) join `httpMethodsToRetry`, since a write is repeated only when the policy names its method, and the per-attempt timeout.
9. **The logging this integration needs.** Logging is off by default — `ClientOptions.logging` sets it for the client and `RequestOptions.logging` sets one call's level — so the sheet says whether it stays off and, where it is on, the level, the logger, and whether headers and the request body are logged: a JSON request body is logged verbatim, with no redaction.
10. **That the SDK performs no pagination and no streaming at all**, and that `ClientOptions.fetch` is the one seam where either can be added — so whatever the task needs there is yours to build or deliberately omit. Say which.
11. **That `Event` imported from this package is a model type, not the global of that name** — every sheet that references one should carry the alias it will be imported under. The error base is re-exported as `MaxioAdvancedBillingError` for the same reason.
12. A **REQUIRED READING** block naming the companion docs in `docs/` that govern the steps, with inline `MUST read` pointers.

<!-- maxio:start -->
For Maxio, four of these items carry more than the generic text says. The sections named are listed under **API knowledge** above.

- **Item 1.** The host has two parts, the region and the site, and both are set explicitly: **Maxio: site and credentials** (R2).
- **Item 4.** Maxio has no `Idempotency-Key` header and ignores the one this SDK sends, so that key makes no resend safe. The sheet names `uniqueness_token` for every write that may be resent: **Fields the spec does not declare** (R12).
- **Item 8.** The defaults do not fit Maxio's writes: a `PUT` is resent, a 429 is resent after about a second, and an attempt times out at 60 seconds. **Maxio: retries, timeouts and paging** has what to set (R10, R11).
- **Item 10.** Paging is written for you to copy: `recipes/list-all.ts` (R8).
<!-- maxio:end -->

