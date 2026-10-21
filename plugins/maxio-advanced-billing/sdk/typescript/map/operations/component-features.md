<!-- Generated file — do not edit; regenerated with the SDK. -->

# ComponentFeatures — operations

Accessor: `client.componentFeatures` · Source: `src/resources/component-features.ts` · 6 operations · Request and error types: namespace `ComponentFeatures`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createComponentFeature

- **Signature**: `createComponentFeature(request: ComponentFeatures.CreateComponentFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.CreateComponentFeatureError>`
- **Wire**: `POST /components/{component_id}/features.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentFeatures.CreateComponentFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentFeatures.CreateComponentFeatureRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |
| `body` | `body` | — | `CreateFeatureCatalogItemRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateFeatureCatalogItemRequest` | `createFeatureCatalogItemRequestSchema` | `src/models/create-feature-catalog-item-request.ts` |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listComponentFeatures

- **Signature**: `listComponentFeatures(request: ComponentFeatures.ListComponentFeaturesRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemsListResponse, ComponentFeatures.ListComponentFeaturesError>`
- **Wire**: `GET /components/{component_id}/features.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FeatureCatalogItemsListResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentFeatures.ListComponentFeaturesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentFeatures.ListComponentFeaturesRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureCatalogItemsListResponse` | `featureCatalogItemsListResponseSchema` | `src/models/feature-catalog-items-list-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readComponentFeature

- **Signature**: `readComponentFeature(request: ComponentFeatures.ReadComponentFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.ReadComponentFeatureError>`
- **Wire**: `GET /components/{component_id}/features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentFeatures.ReadComponentFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentFeatures.ReadComponentFeatureRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### removeComponentFeature

- **Signature**: `removeComponentFeature(request: ComponentFeatures.RemoveComponentFeatureRequest, options?: RequestOptions): ApiPromise<undefined, ComponentFeatures.RemoveComponentFeatureError>`
- **Wire**: `DELETE /components/{component_id}/features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentFeatures.RemoveComponentFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentFeatures.RemoveComponentFeatureRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes | — |
| `id` | `path` | — | `number` | yes | — |
| `destroyEntitlements` | `query` | `destroy_entitlements` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### restoreComponentFeature

- **Signature**: `restoreComponentFeature(request: ComponentFeatures.RestoreComponentFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.RestoreComponentFeatureError>`
- **Wire**: `POST /components/{component_id}/features/{id}/restore.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentFeatures.RestoreComponentFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentFeatures.RestoreComponentFeatureRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateComponentFeature

- **Signature**: `updateComponentFeature(request: ComponentFeatures.UpdateComponentFeatureRequest, options?: RequestOptions): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.UpdateComponentFeatureError>`
- **Wire**: `PUT /components/{component_id}/features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureCatalogItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ComponentFeatures.UpdateComponentFeatureError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ComponentFeatures.UpdateComponentFeatureRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |
| `body` | `body` | — | `UpdateFeatureCatalogItemRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateFeatureCatalogItemRequest` | `updateFeatureCatalogItemRequestSchema` | `src/models/update-feature-catalog-item-request.ts` |
| `FeatureCatalogItemResponse` | `featureCatalogItemResponseSchema` | `src/models/feature-catalog-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

