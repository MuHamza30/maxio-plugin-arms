<!-- Generated file — do not edit; regenerated with the SDK. -->

# CustomFields — operations

Accessor: `client.customFields` · Source: `src/resources/custom-fields.ts` · 9 operations · Request and error types: namespace `CustomFields`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createMetadata

- **Signature**: `createMetadata(request: CustomFields.CreateMetadataRequestParams, options?: RequestOptions): ApiPromise<Metadata[], CustomFields.CreateMetadataError>`
- **Wire**: `POST /{resource_type}/{resource_id}/metadata.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `Metadata[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `CustomFields.CreateMetadataError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleErrorResponse1"` [422] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `CustomFields.CreateMetadataRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes |
| `resourceId` | `path` | `resource_id` | `number` | yes |
| `body` | `body` | — | `CreateMetadataRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |
| `CreateMetadataRequest` | `createMetadataRequestSchema` | `src/models/create-metadata-request.ts` |
| `Metadata` | `metadataSchema` | `src/models/metadata.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

### createMetafields

- **Signature**: `createMetafields(request: CustomFields.CreateMetafieldsRequestParams, options?: RequestOptions): ApiPromise<Metafield[], CustomFields.CreateMetafieldsError>`
- **Wire**: `POST /{resource_type}/metafields.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `Metafield[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `CustomFields.CreateMetafieldsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleErrorResponse1"` [422] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `CustomFields.CreateMetafieldsRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes |
| `body` | `body` | — | `CreateMetafieldsRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |
| `CreateMetafieldsRequest` | `createMetafieldsRequestSchema` | `src/models/create-metafields-request.ts` |
| `Metafield` | `metafieldSchema` | `src/models/metafield.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

### deleteMetadata

- **Signature**: `deleteMetadata(request: CustomFields.DeleteMetadataRequest, options?: RequestOptions): ApiPromise<undefined, CustomFields.DeleteMetadataError>`
- **Wire**: `DELETE /{resource_type}/{resource_id}/metadata.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `CustomFields.DeleteMetadataError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `CustomFields.DeleteMetadataRequest` (4):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes |
| `resourceId` | `path` | `resource_id` | `number` | yes |
| `name` | `query` | — | `string` | no |
| `names` | `query` | — | `string[]` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |

### deleteMetafield

- **Signature**: `deleteMetafield(request: CustomFields.DeleteMetafieldRequest, options?: RequestOptions): ApiPromise<undefined, CustomFields.DeleteMetafieldError>`
- **Wire**: `DELETE /{resource_type}/metafields.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `CustomFields.DeleteMetafieldError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `CustomFields.DeleteMetafieldRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes |
| `name` | `query` | — | `string` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |

### listMetadata

- **Signature**: `listMetadata(request: CustomFields.ListMetadataRequest, options?: RequestOptions): ApiPromise<PaginatedMetadata, ApiError>`
- **Wire**: `GET /{resource_type}/{resource_id}/metadata.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `PaginatedMetadata`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `CustomFields.ListMetadataRequest` (4):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes | — |
| `resourceId` | `path` | `resource_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |
| `PaginatedMetadata` | `paginatedMetadataSchema` | `src/models/paginated-metadata.ts` |

### listMetadataForResourceType

- **Signature**: `listMetadataForResourceType(request: CustomFields.ListMetadataForResourceTypeRequest, options?: RequestOptions): ApiPromise<PaginatedMetadata, ApiError>`
- **Wire**: `GET /{resource_type}/metadata.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `PaginatedMetadata`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `CustomFields.ListMetadataForResourceTypeRequest` (11):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `dateField` | `query` | `date_field` | `BasicDateField` | no | — |
| `startDate` | `query` | `start_date` | `string` (date) | no | — |
| `endDate` | `query` | `end_date` | `string` (date) | no | — |
| `startDatetime` | `query` | `start_datetime` | `Date` (date-time) | no | — |
| `endDatetime` | `query` | `end_datetime` | `Date` (date-time) | no | — |
| `withDeleted` | `query` | `with_deleted` | `boolean` | no | — |
| `resourceIds` | `query` | `resource_ids` | `number[]` | no | — |
| `direction` | `query` | — | `SortingDirection` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |
| `BasicDateField` | `basicDateFieldSchema` | `src/models/basic-date-field.ts` |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `PaginatedMetadata` | `paginatedMetadataSchema` | `src/models/paginated-metadata.ts` |

### listMetafields

- **Signature**: `listMetafields(request: CustomFields.ListMetafieldsRequest, options?: RequestOptions): ApiPromise<ListMetafieldsResponse, ApiError>`
- **Wire**: `GET /{resource_type}/metafields.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListMetafieldsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `CustomFields.ListMetafieldsRequest` (5):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes | — |
| `name` | `query` | — | `string` | no | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `direction` | `query` | — | `SortingDirection` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |
| `SortingDirection` | `sortingDirectionSchema` | `src/models/sorting-direction.ts` |
| `ListMetafieldsResponse` | `listMetafieldsResponseSchema` | `src/models/list-metafields-response.ts` |

### updateMetadata

- **Signature**: `updateMetadata(request: CustomFields.UpdateMetadataRequestParams, options?: RequestOptions): ApiPromise<Metadata[], CustomFields.UpdateMetadataError>`
- **Wire**: `PUT /{resource_type}/{resource_id}/metadata.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `Metadata[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `CustomFields.UpdateMetadataError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleErrorResponse1"` [422] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `CustomFields.UpdateMetadataRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes |
| `resourceId` | `path` | `resource_id` | `number` | yes |
| `body` | `body` | — | `UpdateMetadataRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |
| `UpdateMetadataRequest` | `updateMetadataRequestSchema` | `src/models/update-metadata-request.ts` |
| `Metadata` | `metadataSchema` | `src/models/metadata.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

### updateMetafield

- **Signature**: `updateMetafield(request: CustomFields.UpdateMetafieldRequest, options?: RequestOptions): ApiPromise<Metafield[], CustomFields.UpdateMetafieldError>`
- **Wire**: `PUT /{resource_type}/metafields.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `Metafield[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `CustomFields.UpdateMetafieldError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleErrorResponse1"` [422] `SingleErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `CustomFields.UpdateMetafieldRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `resourceType` | `path` | `resource_type` | `ResourceType` | yes |
| `body` | `body` | — | `UpdateMetafieldsRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResourceType` | `resourceTypeSchema` | `src/models/resource-type.ts` |
| `UpdateMetafieldsRequest` | `updateMetafieldsRequestSchema` | `src/models/update-metafields-request.ts` |
| `Metafield` | `metafieldSchema` | `src/models/metafield.ts` |
| `SingleErrorResponse1` | `singleErrorResponse1Schema` | `src/models/single-error-response1.ts` |

