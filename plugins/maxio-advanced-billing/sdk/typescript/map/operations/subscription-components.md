<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionComponents — operations

Accessor: `client.subscriptionComponents` · Source: `src/resources/subscription-components.ts` · 17 operations · Request and error types: namespace `SubscriptionComponents`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### activateEventBasedComponent

- **Signature**: `activateEventBasedComponent(request: SubscriptionComponents.ActivateEventBasedComponentRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `POST /event_based_billing/subscriptions/{subscription_id}/components/{component_id}/activate.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.ActivateEventBasedComponentRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `number` | yes |
| `body` | `body` | — | `ActivateEventBasedComponent` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ActivateEventBasedComponent` | `activateEventBasedComponentSchema` | `src/models/activate-event-based-component.ts` |

### allocateComponent

- **Signature**: `allocateComponent(request: SubscriptionComponents.AllocateComponentRequest, options?: RequestOptions): ApiPromise<AllocationResponse, SubscriptionComponents.AllocateComponentError>`
- **Wire**: `POST /subscriptions/{subscription_id}/components/{component_id}/allocations.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `AllocationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.AllocateComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.AllocateComponentRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `number` | yes |
| `body` | `body` | — | `CreateAllocationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateAllocationRequest` | `createAllocationRequestSchema` | `src/models/create-allocation-request.ts` |
| `AllocationResponse` | `allocationResponseSchema` | `src/models/allocation-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### allocateComponents

- **Signature**: `allocateComponents(request: SubscriptionComponents.AllocateComponentsRequest, options?: RequestOptions): ApiPromise<AllocationResponse[], SubscriptionComponents.AllocateComponentsError>`
- **Wire**: `POST /subscriptions/{subscription_id}/allocations.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `AllocationResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.AllocateComponentsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.AllocateComponentsRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `AllocateComponents` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `AllocateComponents` | `allocateComponentsSchema` | `src/models/allocate-components.ts` |
| `AllocationResponse` | `allocationResponseSchema` | `src/models/allocation-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### bulkRecordEvents

- **Server**: `ebb` — not the `production` group; see Servers & auth in sdk-map.md
- **Signature**: `bulkRecordEvents(request: SubscriptionComponents.BulkRecordEventsRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `POST /events/{api_handle}/bulk.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field, a bare top-level JSON array. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.BulkRecordEventsRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `apiHandle` | `path` | `api_handle` | `string` | yes |
| `storeUid` | `query` | `store_uid` | `string` | no |
| `body` | `body` | — | `EbbEvent[]` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `EbbEvent` | `ebbEventSchema` | `src/models/ebb-event.ts` |

### bulkResetSubscriptionComponentsPricePoints

- **Signature**: `bulkResetSubscriptionComponentsPricePoints(request: SubscriptionComponents.BulkResetSubscriptionComponentsPricePointsRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, ApiError>`
- **Wire**: `POST /subscriptions/{subscription_id}/price_points/reset.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.BulkResetSubscriptionComponentsPricePointsRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |

### bulkUpdateSubscriptionComponentsPricePoints

- **Signature**: `bulkUpdateSubscriptionComponentsPricePoints(request: SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsRequest, options?: RequestOptions): ApiPromise<BulkComponentsPricePointAssignment, SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsError>`
- **Wire**: `POST /subscriptions/{subscription_id}/price_points.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `BulkComponentsPricePointAssignment`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"componentPricePointError1"` [422] `ComponentPricePointError1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `BulkComponentsPricePointAssignment` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `BulkComponentsPricePointAssignment` | `bulkComponentsPricePointAssignmentSchema` | `src/models/bulk-components-price-point-assignment.ts` |
| `ComponentPricePointError1` | `componentPricePointError1Schema` | `src/models/component-price-point-error1.ts` |

### createUsage

- **Signature**: `createUsage(request: SubscriptionComponents.CreateUsageRequestParams, options?: RequestOptions): ApiPromise<UsageResponse, SubscriptionComponents.CreateUsageError>`
- **Wire**: `POST /subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `UsageResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.CreateUsageError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.CreateUsageRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionIdOrReference` | `path` | `subscription_id_or_reference` | `SubscriptionIdOrReference` | yes |
| `componentId` | `path` | `component_id` | `ComponentIdModel` | yes |
| `body` | `body` | — | `CreateUsageRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionIdOrReference` | `subscriptionIdOrReferenceSchema` | `src/models/unions/subscription-id-or-reference.ts` |
| `ComponentIdModel` | `componentIdModelSchema` | `src/models/unions/component-id-model.ts` |
| `CreateUsageRequest` | `createUsageRequestSchema` | `src/models/create-usage-request.ts` |
| `UsageResponse` | `usageResponseSchema` | `src/models/usage-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### deactivateEventBasedComponent

- **Signature**: `deactivateEventBasedComponent(request: SubscriptionComponents.DeactivateEventBasedComponentRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `POST /event_based_billing/subscriptions/{subscription_id}/components/{component_id}/deactivate.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.DeactivateEventBasedComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `number` | yes |

### deletePrepaidUsageAllocation

- **Signature**: `deletePrepaidUsageAllocation(request: SubscriptionComponents.DeletePrepaidUsageAllocationRequest, options?: RequestOptions): ApiPromise<undefined, SubscriptionComponents.DeletePrepaidUsageAllocationError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.DeletePrepaidUsageAllocationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"subscriptionComponentAllocationError1"` [422] `SubscriptionComponentAllocationError1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.DeletePrepaidUsageAllocationRequest` (4):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `number` | yes |
| `allocationId` | `path` | `allocation_id` | `number` | yes |
| `body` | `body` | — | `CreditSchemeRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreditSchemeRequest` | `creditSchemeRequestSchema` | `src/models/credit-scheme-request.ts` |
| `SubscriptionComponentAllocationError1` | `subscriptionComponentAllocationError1Schema` | `src/models/subscription-component-allocation-error1.ts` |

### listAllocations

- **Signature**: `listAllocations(request: SubscriptionComponents.ListAllocationsRequest, options?: RequestOptions): ApiPromise<AllocationResponse[], SubscriptionComponents.ListAllocationsError>`
- **Wire**: `GET /subscriptions/{subscription_id}/components/{component_id}/allocations.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `AllocationResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.ListAllocationsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.ListAllocationsRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes | — |
| `componentId` | `path` | `component_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |

| Type | Schema value | Source |
| --- | --- | --- |
| `AllocationResponse` | `allocationResponseSchema` | `src/models/allocation-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listSubscriptionComponents

- **Signature**: `listSubscriptionComponents(request: SubscriptionComponents.ListSubscriptionComponentsRequest, options?: RequestOptions): ApiPromise<SubscriptionComponentResponse[], ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}/components.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionComponentResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.ListSubscriptionComponentsRequest` (13):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `dateField` | `query` | `date_field` | `SubscriptionListDateField` | no |
| `direction` | `query` | — | `SortingDirection` | no |
| `filter` | `query` | — | `ListSubscriptionComponentsFilter` | no |
| `endDate` | `query` | `end_date` | `string` | no |
| `endDatetime` | `query` | `end_datetime` | `string` | no |
| `pricePointIds` | `query` | `price_point_ids` | `IncludeNotNull` | no |
| `productFamilyIds` | `query` | `product_family_ids` | `number[]` | no |
| `sort` | `query` | — | `ListSubscriptionComponentsSort` | no |
| `startDate` | `query` | `start_date` | `string` | no |
| `startDatetime` | `query` | `start_datetime` | `string` | no |
| `include` | `query` | — | `ListSubscriptionComponentsInclude[]` | no |
| `inUse` | `query` | `in_use` | `boolean` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionListDateField` | `subscriptionListDateFieldSchema` | `src/models/subscription-list-date-field.ts` |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `ListSubscriptionComponentsFilter` | `listSubscriptionComponentsFilterSchema` | `src/models/list-subscription-components-filter.ts` |
| `IncludeNotNull` | `includeNotNullSchema` | `src/models/include-not-null.ts` |
| `ListSubscriptionComponentsSort` | `listSubscriptionComponentsSortSchema` | `src/models/list-subscription-components-sort.ts` |
| `ListSubscriptionComponentsInclude` | `listSubscriptionComponentsIncludeSchema` | `src/models/list-subscription-components-include.ts` |
| `SubscriptionComponentResponse` | `subscriptionComponentResponseSchema` | `src/models/subscription-component-response.ts` |

### listSubscriptionComponentsForSite

- **Signature**: `listSubscriptionComponentsForSite(request: SubscriptionComponents.ListSubscriptionComponentsForSiteRequest, options?: RequestOptions): ApiPromise<ListSubscriptionComponentsResponse, ApiError>`
- **Wire**: `GET /subscriptions_components.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListSubscriptionComponentsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.ListSubscriptionComponentsForSiteRequest` (14):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `sort` | `query` | — | `ListSubscriptionComponentsSort` | no | — |
| `direction` | `query` | — | `SortingDirection` | no | — |
| `filter` | `query` | — | `ListSubscriptionComponentsForSiteFilter` | no | — |
| `dateField` | `query` | `date_field` | `SubscriptionListDateField` | no | — |
| `startDate` | `query` | `start_date` | `string` | no | — |
| `startDatetime` | `query` | `start_datetime` | `string` | no | — |
| `endDate` | `query` | `end_date` | `string` | no | — |
| `endDatetime` | `query` | `end_datetime` | `string` | no | — |
| `subscriptionIds` | `query` | `subscription_ids` | `number[]` | no | — |
| `pricePointIds` | `query` | `price_point_ids` | `IncludeNotNull` | no | — |
| `productFamilyIds` | `query` | `product_family_ids` | `number[]` | no | — |
| `include` | `query` | — | `ListSubscriptionComponentsInclude` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListSubscriptionComponentsSort` | `listSubscriptionComponentsSortSchema` | `src/models/list-subscription-components-sort.ts` |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `ListSubscriptionComponentsForSiteFilter` | `listSubscriptionComponentsForSiteFilterSchema` | `src/models/list-subscription-components-for-site-filter.ts` |
| `SubscriptionListDateField` | `subscriptionListDateFieldSchema` | `src/models/subscription-list-date-field.ts` |
| `IncludeNotNull` | `includeNotNullSchema` | `src/models/include-not-null.ts` |
| `ListSubscriptionComponentsInclude` | `listSubscriptionComponentsIncludeSchema` | `src/models/list-subscription-components-include.ts` |
| `ListSubscriptionComponentsResponse` | `listSubscriptionComponentsResponseSchema` | `src/models/list-subscription-components-response.ts` |

### listUsages

- **Signature**: `listUsages(request: SubscriptionComponents.ListUsagesRequest, options?: RequestOptions): ApiPromise<UsageResponse[], ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `UsageResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.ListUsagesRequest` (8):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionIdOrReference` | `path` | `subscription_id_or_reference` | `SubscriptionIdOrReference` | yes | — |
| `componentId` | `path` | `component_id` | `ComponentIdModel` | yes | — |
| `sinceId` | `query` | `since_id` | `number` | no | — |
| `maxId` | `query` | `max_id` | `number` | no | — |
| `sinceDate` | `query` | `since_date` | `string` (date) | no | — |
| `untilDate` | `query` | `until_date` | `string` (date) | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionIdOrReference` | `subscriptionIdOrReferenceSchema` | `src/models/unions/subscription-id-or-reference.ts` |
| `ComponentIdModel` | `componentIdModelSchema` | `src/models/unions/component-id-model.ts` |
| `UsageResponse` | `usageResponseSchema` | `src/models/usage-response.ts` |

### previewAllocations

- **Signature**: `previewAllocations(request: SubscriptionComponents.PreviewAllocationsRequestParams, options?: RequestOptions): ApiPromise<AllocationPreviewResponse, SubscriptionComponents.PreviewAllocationsError>`
- **Wire**: `POST /subscriptions/{subscription_id}/allocations/preview.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `AllocationPreviewResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.PreviewAllocationsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"componentAllocationError1"` [422] `ComponentAllocationError1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.PreviewAllocationsRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `PreviewAllocationsRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `PreviewAllocationsRequest` | `previewAllocationsRequestSchema` | `src/models/preview-allocations-request.ts` |
| `AllocationPreviewResponse` | `allocationPreviewResponseSchema` | `src/models/allocation-preview-response.ts` |
| `ComponentAllocationError1` | `componentAllocationError1Schema` | `src/models/component-allocation-error1.ts` |

### readSubscriptionComponent

- **Signature**: `readSubscriptionComponent(request: SubscriptionComponents.ReadSubscriptionComponentRequest, options?: RequestOptions): ApiPromise<SubscriptionComponentResponse, SubscriptionComponents.ReadSubscriptionComponentError>`
- **Wire**: `GET /subscriptions/{subscription_id}/components/{component_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.ReadSubscriptionComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.ReadSubscriptionComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionComponentResponse` | `subscriptionComponentResponseSchema` | `src/models/subscription-component-response.ts` |

### recordEvent

- **Server**: `ebb` — not the `production` group; see Servers & auth in sdk-map.md
- **Signature**: `recordEvent(request: SubscriptionComponents.RecordEventRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `POST /events/{api_handle}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionComponents.RecordEventRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `apiHandle` | `path` | `api_handle` | `string` | yes |
| `storeUid` | `query` | `store_uid` | `string` | no |
| `body` | `body` | — | `EbbEvent` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `EbbEvent` | `ebbEventSchema` | `src/models/ebb-event.ts` |

### updatePrepaidUsageAllocationExpirationDate

- **Signature**: `updatePrepaidUsageAllocationExpirationDate(request: SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateRequest, options?: RequestOptions): ApiPromise<undefined, SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"subscriptionComponentAllocationError1"` [422] `SubscriptionComponentAllocationError1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateRequest` (4):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `number` | yes |
| `allocationId` | `path` | `allocation_id` | `number` | yes |
| `body` | `body` | — | `UpdateAllocationExpirationDate` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateAllocationExpirationDate` | `updateAllocationExpirationDateSchema` | `src/models/update-allocation-expiration-date.ts` |
| `SubscriptionComponentAllocationError1` | `subscriptionComponentAllocationError1Schema` | `src/models/subscription-component-allocation-error1.ts` |

