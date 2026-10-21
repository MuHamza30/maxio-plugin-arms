<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionProducts — operations

Accessor: `client.subscriptionProducts` · Source: `src/resources/subscription-products.ts` · 2 operations · Request and error types: namespace `SubscriptionProducts`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### migrateSubscriptionProduct

- **Signature**: `migrateSubscriptionProduct(request: SubscriptionProducts.MigrateSubscriptionProductRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionProducts.MigrateSubscriptionProductError>`
- **Wire**: `POST /subscriptions/{subscription_id}/migrations.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionProducts.MigrateSubscriptionProductError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionProducts.MigrateSubscriptionProductRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `SubscriptionProductMigrationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionProductMigrationRequest` | `subscriptionProductMigrationRequestSchema` | `src/models/subscription-product-migration-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### previewSubscriptionProductMigration

- **Signature**: `previewSubscriptionProductMigration(request: SubscriptionProducts.PreviewSubscriptionProductMigrationRequest, options?: RequestOptions): ApiPromise<SubscriptionMigrationPreviewResponse, SubscriptionProducts.PreviewSubscriptionProductMigrationError>`
- **Wire**: `POST /subscriptions/{subscription_id}/migrations/preview.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionMigrationPreviewResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionProducts.PreviewSubscriptionProductMigrationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionProducts.PreviewSubscriptionProductMigrationRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `SubscriptionMigrationPreviewRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionMigrationPreviewRequest` | `subscriptionMigrationPreviewRequestSchema` | `src/models/subscription-migration-preview-request.ts` |
| `SubscriptionMigrationPreviewResponse` | `subscriptionMigrationPreviewResponseSchema` | `src/models/subscription-migration-preview-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

