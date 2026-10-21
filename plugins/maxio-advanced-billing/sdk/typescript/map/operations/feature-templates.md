<!-- Generated file — do not edit; regenerated with the SDK. -->

# FeatureTemplates — operations

Accessor: `client.featureTemplates` · Source: `src/resources/feature-templates.ts` · 6 operations · Request and error types: namespace `FeatureTemplates`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### archiveFeatureTemplate

- **Provider rules (Maxio)**: Send `remove_from_catalog=true` only to revoke access for good: it destroys the template's catalog items and their entitlements at once, and `restoreFeatureTemplate` does not bring them back. Notes: `knowledge/operations/feature-templates.md#archivefeaturetemplate`
- **Signature**: `archiveFeatureTemplate(request: FeatureTemplates.ArchiveFeatureTemplateRequest, options?: RequestOptions): ApiPromise<undefined, FeatureTemplates.ArchiveFeatureTemplateError>`
- **Wire**: `DELETE /features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `FeatureTemplates.ArchiveFeatureTemplateError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `FeatureTemplates.ArchiveFeatureTemplateRequest` (2):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `id` | `path` | — | `number` | yes | — |
| `removeFromCatalog` | `query` | `remove_from_catalog` | `boolean` | no | `false` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createFeatureTemplate

- **Provider rules (Maxio)**: Settle `key` and `kind` before creating: `key` is rejected on every later update, and `kind` once any feature catalog item uses the template. Notes: `knowledge/operations/feature-templates.md#createfeaturetemplate`
- **Signature**: `createFeatureTemplate(request: FeatureTemplates.CreateFeatureTemplateRequestParams, options?: RequestOptions): ApiPromise<FeatureTemplateResponse, FeatureTemplates.CreateFeatureTemplateError>`
- **Wire**: `POST /features.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureTemplateResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `FeatureTemplates.CreateFeatureTemplateError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `FeatureTemplates.CreateFeatureTemplateRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateFeatureTemplateRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateFeatureTemplateRequest` | `createFeatureTemplateRequestSchema` | `src/models/create-feature-template-request.ts` |
| `FeatureTemplateResponse` | `featureTemplateResponseSchema` | `src/models/feature-template-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listFeatureTemplates

- **Signature**: `listFeatureTemplates(request: FeatureTemplates.ListFeatureTemplatesRequest, options?: RequestOptions): ApiPromise<FeatureTemplatesListResponse, FeatureTemplates.ListFeatureTemplatesError>`
- **Wire**: `GET /features.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FeatureTemplatesListResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `FeatureTemplates.ListFeatureTemplatesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `FeatureTemplates.ListFeatureTemplatesRequest` (9):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `status` | `query` | — | `Status1` | no | `Status1.Active` |
| `q` | `query` | — | `string` | no | — |
| `kind` | `query` | — | `Kind` | no | — |
| `updatedFrom` | `query` | `updated_from` | `string` (date) | no | — |
| `updatedTo` | `query` | `updated_to` | `string` (date) | no | — |
| `sortBy` | `query` | `sort_by` | `SortBy` | no | `SortBy.Name` |
| `sortDirection` | `query` | `sort_direction` | `SortDirection` | no | `SortDirection.Asc` |

| Type | Schema value | Source |
| --- | --- | --- |
| `Status1` | `status1Schema` | `src/models/status1.ts` |
| `Kind` | `kindSchema` | `src/models/kind.ts` |
| `SortBy` | `sortBySchema` | `src/models/sort-by.ts` |
| `SortDirection` | `sortDirectionSchema` | `src/models/sort-direction.ts` |
| `FeatureTemplatesListResponse` | `featureTemplatesListResponseSchema` | `src/models/feature-templates-list-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readFeatureTemplate

- **Signature**: `readFeatureTemplate(request: FeatureTemplates.ReadFeatureTemplateRequest, options?: RequestOptions): ApiPromise<FeatureTemplateResponse, FeatureTemplates.ReadFeatureTemplateError>`
- **Wire**: `GET /features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FeatureTemplateResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `FeatureTemplates.ReadFeatureTemplateError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `FeatureTemplates.ReadFeatureTemplateRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureTemplateResponse` | `featureTemplateResponseSchema` | `src/models/feature-template-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### restoreFeatureTemplate

- **Signature**: `restoreFeatureTemplate(request: FeatureTemplates.RestoreFeatureTemplateRequest, options?: RequestOptions): ApiPromise<FeatureTemplateResponse, FeatureTemplates.RestoreFeatureTemplateError>`
- **Wire**: `POST /features/{id}/restore.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureTemplateResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `FeatureTemplates.RestoreFeatureTemplateError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `FeatureTemplates.RestoreFeatureTemplateRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FeatureTemplateResponse` | `featureTemplateResponseSchema` | `src/models/feature-template-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateFeatureTemplate

- **Signature**: `updateFeatureTemplate(request: FeatureTemplates.UpdateFeatureTemplateRequestParams, options?: RequestOptions): ApiPromise<FeatureTemplateResponse, FeatureTemplates.UpdateFeatureTemplateError>`
- **Wire**: `PUT /features/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `FeatureTemplateResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `FeatureTemplates.UpdateFeatureTemplateError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [403] `ErrorListResponse1` · `"error404"` [404] no body · `"errorListResponse12"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `FeatureTemplates.UpdateFeatureTemplateRequestParams` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `id` | `path` | `number` | yes |
| `body` | `body` | `UpdateFeatureTemplateRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateFeatureTemplateRequest` | `updateFeatureTemplateRequestSchema` | `src/models/update-feature-template-request.ts` |
| `FeatureTemplateResponse` | `featureTemplateResponseSchema` | `src/models/feature-template-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

