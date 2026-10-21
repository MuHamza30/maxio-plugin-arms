<!-- Generated file — do not edit; regenerated with the SDK. -->

# Components — operations

Accessor: `client.components` · Source: `src/resources/components.ts` · 12 operations · Request and error types: namespace `Components`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#archivecomponent`
- **Signature**: `archiveComponent(request: Components.ArchiveComponentRequest, options?: RequestOptions): ApiPromise<Component, Components.ArchiveComponentError>`
- **Wire**: `DELETE /product_families/{product_family_id}/components/{component_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `Component`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.ArchiveComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.ArchiveComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `Component` | `componentSchema` | `src/models/component.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createEventBasedComponent

- **Provider rules (Maxio)**: Follow with `activateEventBasedComponent` for each subscription that should be billed; events streamed without it produce no charge and no error. Notes: `knowledge/operations/components.md#createeventbasedcomponent`
- **Signature**: `createEventBasedComponent(request: Components.CreateEventBasedComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, Components.CreateEventBasedComponentError>`
- **Wire**: `POST /product_families/{product_family_id}/event_based_components.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.CreateEventBasedComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.CreateEventBasedComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `string` | yes |
| `body` | `body` | — | `CreateEbbComponent` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateEbbComponent` | `createEbbComponentSchema` | `src/models/create-ebb-component.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createMeteredComponent

- **Provider rules (Maxio)**: Send `unit_price` in decimal major units, not cents (R4). Send `prices` for any scheme other than `per_unit`, as contiguous, non-overlapping brackets. On new-Catalog sites give taxable components a `tax_code`. Notes: `knowledge/operations/components.md#createmeteredcomponent`
- **Signature**: `createMeteredComponent(request: Components.CreateMeteredComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, Components.CreateMeteredComponentError>`
- **Wire**: `POST /product_families/{product_family_id}/metered_components.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.CreateMeteredComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.CreateMeteredComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `string` | yes |
| `body` | `body` | — | `CreateMeteredComponent` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateMeteredComponent` | `createMeteredComponentSchema` | `src/models/create-metered-component.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createOnOffComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#createonoffcomponent`
- **Signature**: `createOnOffComponent(request: Components.CreateOnOffComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, Components.CreateOnOffComponentError>`
- **Wire**: `POST /product_families/{product_family_id}/on_off_components.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.CreateOnOffComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.CreateOnOffComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `string` | yes |
| `body` | `body` | — | `CreateOnOffComponent` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateOnOffComponent` | `createOnOffComponentSchema` | `src/models/create-on-off-component.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createPrepaidUsageComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#createprepaidusagecomponent`
- **Signature**: `createPrepaidUsageComponent(request: Components.CreatePrepaidUsageComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, Components.CreatePrepaidUsageComponentError>`
- **Wire**: `POST /product_families/{product_family_id}/prepaid_usage_components.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.CreatePrepaidUsageComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.CreatePrepaidUsageComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `string` | yes |
| `body` | `body` | — | `CreatePrepaidComponent` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreatePrepaidComponent` | `createPrepaidComponentSchema` | `src/models/create-prepaid-component.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createQuantityBasedComponent

- **Provider rules (Maxio)**: Send `recurring: false` only for a one-time charge (inferred; D10). In `stairstep`, send each bracket's `unit_price` as the flat charge for the whole band (D17). Notes: `knowledge/operations/components.md#createquantitybasedcomponent`
- **Signature**: `createQuantityBasedComponent(request: Components.CreateQuantityBasedComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, Components.CreateQuantityBasedComponentError>`
- **Wire**: `POST /product_families/{product_family_id}/quantity_based_components.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.CreateQuantityBasedComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.CreateQuantityBasedComponentRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `string` | yes |
| `body` | `body` | — | `CreateQuantityBasedComponent` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateQuantityBasedComponent` | `createQuantityBasedComponentSchema` | `src/models/create-quantity-based-component.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### findComponent

- **Signature**: `findComponent(request: Components.FindComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, ApiError>`
- **Wire**: `GET /components/lookup.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Components.FindComponentRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `handle` | `query` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |

### listComponents

- **Signature**: `listComponents(request: Components.ListComponentsRequest, options?: RequestOptions): ApiPromise<ComponentResponse[], ApiError>`
- **Wire**: `GET /components.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ComponentResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Components.ListComponentsRequest` (9):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `dateField` | `query` | `date_field` | `BasicDateField` | no | — |
| `startDate` | `query` | `start_date` | `string` | no | — |
| `endDate` | `query` | `end_date` | `string` | no | — |
| `startDatetime` | `query` | `start_datetime` | `string` | no | — |
| `endDatetime` | `query` | `end_datetime` | `string` | no | — |
| `includeArchived` | `query` | `include_archived` | `boolean` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `filter` | `query` | — | `ListComponentsFilter` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `BasicDateField` | `basicDateFieldSchema` | `src/models/basic-date-field.ts` |
| `ListComponentsFilter` | `listComponentsFilterSchema` | `src/models/list-components-filter.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |

### listComponentsForProductFamily

- **Signature**: `listComponentsForProductFamily(request: Components.ListComponentsForProductFamilyRequest, options?: RequestOptions): ApiPromise<ComponentResponse[], ApiError>`
- **Wire**: `GET /product_families/{product_family_id}/components.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ComponentResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Components.ListComponentsForProductFamilyRequest` (10):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes | — |
| `includeArchived` | `query` | `include_archived` | `boolean` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `filter` | `query` | — | `ListComponentsFilter` | no | — |
| `dateField` | `query` | `date_field` | `BasicDateField` | no | — |
| `endDate` | `query` | `end_date` | `string` | no | — |
| `endDatetime` | `query` | `end_datetime` | `string` | no | — |
| `startDate` | `query` | `start_date` | `string` | no | — |
| `startDatetime` | `query` | `start_datetime` | `string` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListComponentsFilter` | `listComponentsFilterSchema` | `src/models/list-components-filter.ts` |
| `BasicDateField` | `basicDateFieldSchema` | `src/models/basic-date-field.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |

### readComponent

- **Signature**: `readComponent(request: Components.ReadComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, ApiError>`
- **Wire**: `GET /product_families/{product_family_id}/components/{component_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Components.ReadComponentRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes | — |
| `componentId` | `path` | `component_id` | `string` | yes | — |
| `includeFeatures` | `query` | `include_features` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |

### updateComponent

- **Provider notes (Maxio)**: `knowledge/operations/components.md#updatecomponent`
- **Signature**: `updateComponent(request: Components.UpdateComponentRequestParams, options?: RequestOptions): ApiPromise<ComponentResponse, Components.UpdateComponentError>`
- **Wire**: `PUT /components/{component_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.UpdateComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.UpdateComponentRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes |
| `body` | `body` | — | `UpdateComponentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateComponentRequest` | `updateComponentRequestSchema` | `src/models/update-component-request.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateProductFamilyComponent

- **Signature**: `updateProductFamilyComponent(request: Components.UpdateProductFamilyComponentRequest, options?: RequestOptions): ApiPromise<ComponentResponse, Components.UpdateProductFamilyComponentError>`
- **Wire**: `PUT /product_families/{product_family_id}/components/{component_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ComponentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `Components.UpdateProductFamilyComponentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `Components.UpdateProductFamilyComponentRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `productFamilyId` | `path` | `product_family_id` | `number` | yes |
| `componentId` | `path` | `component_id` | `string` | yes |
| `body` | `body` | — | `UpdateComponentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateComponentRequest` | `updateComponentRequestSchema` | `src/models/update-component-request.ts` |
| `ComponentResponse` | `componentResponseSchema` | `src/models/component-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

