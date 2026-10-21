<!-- Generated file — do not edit; regenerated with the SDK. -->

# Subscriptions — operations

Accessor: `client.subscriptions` · Source: `src/resources/subscriptions.ts` · 12 operations · Request and error types: namespace `Subscriptions`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### activateSubscription

- **Provider rules (Maxio)**: It can take a payment: turn off the client's automatic retry for it (R11). Set `revert_on_failure` explicitly. Only on Relationship Invoicing sites (R3), for an `awaiting_signup` or `trialing` subscription not in a group. Notes: `knowledge/operations/subscriptions.md#activatesubscription`
- **Signature**: `activateSubscription(request: Subscriptions.ActivateSubscriptionRequestParams, options?: RequestOptions): ApiPromise<SubscriptionResponse, Subscriptions.ActivateSubscriptionError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/activate.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.ActivateSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorArrayMapResponse1"` [400] `ErrorArrayMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.ActivateSubscriptionRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `ActivateSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ActivateSubscriptionRequest` | `activateSubscriptionRequestSchema` | `src/models/activate-subscription-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorArrayMapResponse1` | `errorArrayMapResponse1Schema` | `src/models/error-array-map-response1.ts` |

### applyCouponsToSubscription

- **Provider rules (Maxio)**: Send the codes in the request body. Never use the deprecated `code` query parameter: it replaces every coupon already on the subscription (D18). Notes: `knowledge/operations/subscriptions.md#applycouponstosubscription`
- **Signature**: `applyCouponsToSubscription(request: Subscriptions.ApplyCouponsToSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, Subscriptions.ApplyCouponsToSubscriptionError>`
- **Wire**: `POST /subscriptions/{subscription_id}/add_coupon.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.ApplyCouponsToSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"subscriptionAddCouponError1"` [422] `SubscriptionAddCouponError1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.ApplyCouponsToSubscriptionRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `code` | `query` | — | `string` | no |
| `body` | `body` | — | `AddCouponsRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `AddCouponsRequest` | `addCouponsRequestSchema` | `src/models/add-coupons-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `SubscriptionAddCouponError1` | `subscriptionAddCouponError1Schema` | `src/models/subscription-add-coupon-error1.ts` |

### createSubscription

- **Provider rules (Maxio)**: Find the customer (`readCustomerByReference`) and any plan it holds (L2); name it once (D1). Send `payment_collection_method` (R14), `reference`, a body-root `uniqueness_token` kept on resends (R12). Timeout, 409: unknown (R11). Notes: `knowledge/operations/subscriptions.md#createsubscription`
- **Signature**: `createSubscription(request?: Subscriptions.CreateSubscriptionRequestParams, options?: RequestOptions): ApiPromise<SubscriptionResponse, Subscriptions.CreateSubscriptionError>`
- **Wire**: `POST /subscriptions.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.CreateSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.CreateSubscriptionRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateSubscriptionRequest` | `createSubscriptionRequestSchema` | `src/models/create-subscription-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### findSubscription

- **Provider rules (Maxio)**: A 404 is "not there", not proof that a create failed: after a create with an unknown outcome follow R11. That create gets a new `uniqueness_token` only after a corrected 422, or after a 409 once 120 s pass with nothing found. Notes: `knowledge/operations/subscriptions.md#findsubscription`
- **Signature**: `findSubscription(request?: Subscriptions.FindSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, Subscriptions.FindSubscriptionError>`
- **Wire**: `GET /subscriptions/lookup.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.FindSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.FindSubscriptionRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `reference` | `query` | `string` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |

### listSubscriptions

- **Provider rules (Maxio)**: Page until a page comes back empty (R8). The `state` filter cannot name `soft_failure`: to list everyone with access, leave it out and classify each row's `state` (R9, R16). Filter `product` by id or exact name, never a handle. Notes: `knowledge/operations/subscriptions.md#listsubscriptions`
- **Signature**: `listSubscriptions(request?: Subscriptions.ListSubscriptionsRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse[], ApiError>`
- **Wire**: `GET /subscriptions.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Subscriptions.ListSubscriptionsRequest` (25):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `sort` | `query` | — | `SubscriptionSort` | no | `SubscriptionSort.SignupDate` |
| `direction` | `query` | — | `SortingDirection` | no | — |
| `state` | `query` | — | `SubscriptionStateFilter` | no | — |
| `product` | `query` | — | `Product1` | no | — |
| `q` | `query` | — | `string` | no | — |
| `qScope` | `query` | `q_scope` | `QScope` | no | — |
| `customerId` | `query` | `customer_id` | `number` | no | — |
| `productPricePointId` | `query` | `product_price_point_id` | `number` | no | — |
| `coupon` | `query` | — | `number` | no | — |
| `couponCode` | `query` | `coupon_code` | `string` | no | — |
| `collectionMethod` | `query` | `collection_method` | `CollectionMethod1` | no | — |
| `brandingThemeId` | `query` | `branding_theme_id` | `number` | no | — |
| `dateField` | `query` | `date_field` | `SubscriptionDateField` | no | — |
| `startDate` | `query` | `start_date` | `string` (date) | no | — |
| `endDate` | `query` | `end_date` | `string` (date) | no | — |
| `startDatetime` | `query` | `start_datetime` | `Date` (date-time) | no | — |
| `endDatetime` | `query` | `end_datetime` | `Date` (date-time) | no | — |
| `metadata` | `query` | — | `Record<string, string>` | no | — |
| `groupStatus` | `query` | `group_status` | `GroupStatus` | no | — |
| `dunningExemption` | `query` | `dunning_exemption` | `boolean` | no | — |
| `paymentGateways` | `query` | `payment_gateways` | `string` | no | — |
| `currencies` | `query` | — | `string` | no | — |
| `include` | `query` | — | `SubscriptionListInclude[]` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionSort` | `subscriptionSortSchema` | `src/models/subscription-sort.ts` |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `SubscriptionStateFilter` | `subscriptionStateFilterSchema` | `src/models/subscription-state-filter.ts` |
| `Product1` | `product1Schema` | `src/models/unions/product1.ts` |
| `QScope` | `qScopeSchema` | `src/models/qscope.ts` |
| `CollectionMethod1` | `collectionMethod1Schema` | `src/models/collection-method1.ts` |
| `SubscriptionDateField` | `subscriptionDateFieldSchema` | `src/models/subscription-date-field.ts` |
| `GroupStatus` | `groupStatusSchema` | `src/models/group-status.ts` |
| `SubscriptionListInclude` | `subscriptionListIncludeSchema` | `src/models/subscription-list-include.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |

### overrideSubscription

- **Provider rules (Maxio)**: Use it only to align fields Maxio manages with your own history. Other fields do not follow (a new `expires_at` leaves the next assessment date), but `current_period_starts_at` sets how mid-period allocations prorate. Notes: `knowledge/operations/subscriptions.md#overridesubscription`
- **Signature**: `overrideSubscription(request: Subscriptions.OverrideSubscriptionRequestParams, options?: RequestOptions): ApiPromise<undefined, Subscriptions.OverrideSubscriptionError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/override.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.OverrideSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleErrorResponse1"` [422] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.OverrideSubscriptionRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `OverrideSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `OverrideSubscriptionRequest` | `overrideSubscriptionRequestSchema` | `src/models/override-subscription-request.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

### previewSubscription

- **Provider notes (Maxio)**: `knowledge/operations/subscriptions.md#previewsubscription`
- **Signature**: `previewSubscription(request?: Subscriptions.PreviewSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionPreviewResponse, ApiError>`
- **Wire**: `POST /subscriptions/preview.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionPreviewResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Subscriptions.PreviewSubscriptionRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateSubscriptionRequest` | `createSubscriptionRequestSchema` | `src/models/create-subscription-request.ts` |
| `SubscriptionPreviewResponse` | `subscriptionPreviewResponseSchema` | `src/models/subscription-preview-response.ts` |

### purgeSubscription

- **Provider rules (Maxio)**: Set `ack` to the subscription's customer id. Call on test sites only. Send `cascade[]=customer` or `cascade[]=payment_profile` only to delete those records too. Notes: `knowledge/operations/subscriptions.md#purgesubscription`
- **Signature**: `purgeSubscription(request: Subscriptions.PurgeSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, Subscriptions.PurgeSubscriptionError>`
- **Wire**: `POST /subscriptions/{subscription_id}/purge.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.PurgeSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"subscriptionResponse"` [400] `SubscriptionResponse` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.PurgeSubscriptionRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `ack` | `query` | — | `number` | yes |
| `cascade` | `query` | — | `SubscriptionPurgeType[]` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionPurgeType` | `subscriptionPurgeTypeSchema` | `src/models/subscription-purge-type.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |

### readSubscription

- **Provider notes (Maxio)**: `knowledge/operations/subscriptions.md#readsubscription`
- **Signature**: `readSubscription(request: Subscriptions.ReadSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Subscriptions.ReadSubscriptionRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `include` | `query` | — | `SubscriptionInclude[]` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionInclude` | `subscriptionIncludeSchema` | `src/models/subscription-include.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |

### removeCouponFromSubscription

- **Signature**: `removeCouponFromSubscription(request: Subscriptions.RemoveCouponFromSubscriptionRequest, options?: RequestOptions): ApiPromise<string, Subscriptions.RemoveCouponFromSubscriptionError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}/remove_coupon.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `string` — a bare `application/json` string; the success type *is* the string
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.RemoveCouponFromSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"subscriptionRemoveCouponErrors1"` [422] `SubscriptionRemoveCouponErrors1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.RemoveCouponFromSubscriptionRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `couponCode` | `query` | `coupon_code` | `string` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionRemoveCouponErrors1` | `subscriptionRemoveCouponErrors1Schema` | `src/models/subscription-remove-coupon-errors1.ts` |

### updatePrepaidSubscriptionConfiguration

- **Signature**: `updatePrepaidSubscriptionConfiguration(request: Subscriptions.UpdatePrepaidSubscriptionConfigurationRequest, options?: RequestOptions): ApiPromise<PrepaidConfigurationResponse, Subscriptions.UpdatePrepaidSubscriptionConfigurationError>`
- **Wire**: `POST /subscriptions/{subscription_id}/prepaid_configurations.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `PrepaidConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.UpdatePrepaidSubscriptionConfigurationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"prepaidConfigurationErrorResponse"` [422] `PrepaidConfigurationErrorResponse` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.UpdatePrepaidSubscriptionConfigurationRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `UpsertPrepaidConfigurationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpsertPrepaidConfigurationRequest` | `upsertPrepaidConfigurationRequestSchema` | `src/models/upsert-prepaid-configuration-request.ts` |
| `PrepaidConfigurationResponse` | `prepaidConfigurationResponseSchema` | `src/models/prepaid-configuration-response.ts` |
| `PrepaidConfigurationErrorResponse` | `prepaidConfigurationErrorResponseSchema` | `src/models/unions/prepaid-configuration-error-response.ts` |

### updateSubscription

- **Provider rules (Maxio)**: A product sent here switches the plan now, with no proration; add `product_change_delayed: true` to switch at renewal (D13). With card details this call can take a payment: turn off the client's automatic retry for it (R11). Notes: `knowledge/operations/subscriptions.md#updatesubscription`
- **Signature**: `updateSubscription(request: Subscriptions.UpdateSubscriptionRequestParams, options?: RequestOptions): ApiPromise<SubscriptionResponse, Subscriptions.UpdateSubscriptionError>`
- **Wire**: `PUT /subscriptions/{subscription_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Subscriptions.UpdateSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Subscriptions.UpdateSubscriptionRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `UpdateSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateSubscriptionRequest` | `updateSubscriptionRequestSchema` | `src/models/update-subscription-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

