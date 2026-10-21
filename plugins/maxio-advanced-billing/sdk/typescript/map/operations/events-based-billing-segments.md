<!-- Generated file — do not edit; regenerated with the SDK. -->

# EventsBasedBillingSegments — operations

Accessor: `client.eventsBasedBillingSegments` · Source: `src/resources/events-based-billing-segments.ts` · 6 operations · Request and error types: namespace `EventsBasedBillingSegments`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### bulkCreateSegments

- **Signature**: `bulkCreateSegments(request: EventsBasedBillingSegments.BulkCreateSegmentsRequest, options?: RequestOptions): ApiPromise<ListSegmentsResponse, EventsBasedBillingSegments.BulkCreateSegmentsError>`
- **Wire**: `POST /components/{component_id}/price_points/{price_point_id}/segments/bulk.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ListSegmentsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `EventsBasedBillingSegments.BulkCreateSegmentsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"eventBasedBillingSegment1"` [422] `EventBasedBillingSegment1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `EventsBasedBillingSegments.BulkCreateSegmentsRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes |
| `pricePointId` | `path` | `price_point_id` | `string` | yes |
| `body` | `body` | — | `BulkCreateSegments` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `BulkCreateSegments` | `bulkCreateSegmentsSchema` | `src/models/bulk-create-segments.ts` |
| `ListSegmentsResponse` | `listSegmentsResponseSchema` | `src/models/list-segments-response.ts` |
| `EventBasedBillingSegment1` | `eventBasedBillingSegment1Schema` | `src/models/event-based-billing-segment1.ts` |

### bulkUpdateSegments

- **Signature**: `bulkUpdateSegments(request: EventsBasedBillingSegments.BulkUpdateSegmentsRequest, options?: RequestOptions): ApiPromise<ListSegmentsResponse, EventsBasedBillingSegments.BulkUpdateSegmentsError>`
- **Wire**: `PUT /components/{component_id}/price_points/{price_point_id}/segments/bulk.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ListSegmentsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `EventsBasedBillingSegments.BulkUpdateSegmentsError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"eventBasedBillingSegment1"` [422] `EventBasedBillingSegment1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `EventsBasedBillingSegments.BulkUpdateSegmentsRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes |
| `pricePointId` | `path` | `price_point_id` | `string` | yes |
| `body` | `body` | — | `BulkUpdateSegments` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `BulkUpdateSegments` | `bulkUpdateSegmentsSchema` | `src/models/bulk-update-segments.ts` |
| `ListSegmentsResponse` | `listSegmentsResponseSchema` | `src/models/list-segments-response.ts` |
| `EventBasedBillingSegment1` | `eventBasedBillingSegment1Schema` | `src/models/event-based-billing-segment1.ts` |

### createSegment

- **Signature**: `createSegment(request: EventsBasedBillingSegments.CreateSegmentRequestParams, options?: RequestOptions): ApiPromise<SegmentResponse, EventsBasedBillingSegments.CreateSegmentError>`
- **Wire**: `POST /components/{component_id}/price_points/{price_point_id}/segments.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SegmentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `EventsBasedBillingSegments.CreateSegmentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"eventBasedBillingSegmentErrors1"` [422] `EventBasedBillingSegmentErrors1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `EventsBasedBillingSegments.CreateSegmentRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes |
| `pricePointId` | `path` | `price_point_id` | `string` | yes |
| `body` | `body` | — | `CreateSegmentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateSegmentRequest` | `createSegmentRequestSchema` | `src/models/create-segment-request.ts` |
| `SegmentResponse` | `segmentResponseSchema` | `src/models/segment-response.ts` |
| `EventBasedBillingSegmentErrors1` | `eventBasedBillingSegmentErrors1Schema` | `src/models/event-based-billing-segment-errors1.ts` |

### deleteSegment

- **Signature**: `deleteSegment(request: EventsBasedBillingSegments.DeleteSegmentRequest, options?: RequestOptions): ApiPromise<undefined, EventsBasedBillingSegments.DeleteSegmentError>`
- **Wire**: `DELETE /components/{component_id}/price_points/{price_point_id}/segments/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `EventsBasedBillingSegments.DeleteSegmentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"error422"` [422] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `EventsBasedBillingSegments.DeleteSegmentRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes |
| `pricePointId` | `path` | `price_point_id` | `string` | yes |
| `id` | `path` | — | `number` | yes |

### listSegmentsForPricePoint

- **Signature**: `listSegmentsForPricePoint(request: EventsBasedBillingSegments.ListSegmentsForPricePointRequest, options?: RequestOptions): ApiPromise<ListSegmentsResponse, EventsBasedBillingSegments.ListSegmentsForPricePointError>`
- **Wire**: `GET /components/{component_id}/price_points/{price_point_id}/segments.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListSegmentsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `EventsBasedBillingSegments.ListSegmentsForPricePointError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"eventBasedBillingListSegmentsErrors1"` [422] `EventBasedBillingListSegmentsErrors1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `EventsBasedBillingSegments.ListSegmentsForPricePointRequest` (5):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes | — |
| `pricePointId` | `path` | `price_point_id` | `string` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `30` |
| `filter` | `query` | — | `ListSegmentsFilter` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListSegmentsFilter` | `listSegmentsFilterSchema` | `src/models/list-segments-filter.ts` |
| `ListSegmentsResponse` | `listSegmentsResponseSchema` | `src/models/list-segments-response.ts` |
| `EventBasedBillingListSegmentsErrors1` | `eventBasedBillingListSegmentsErrors1Schema` | `src/models/event-based-billing-list-segments-errors1.ts` |

### updateSegment

- **Signature**: `updateSegment(request: EventsBasedBillingSegments.UpdateSegmentRequestParams, options?: RequestOptions): ApiPromise<SegmentResponse, EventsBasedBillingSegments.UpdateSegmentError>`
- **Wire**: `PUT /components/{component_id}/price_points/{price_point_id}/segments/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SegmentResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `EventsBasedBillingSegments.UpdateSegmentError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"eventBasedBillingSegmentErrors1"` [422] `EventBasedBillingSegmentErrors1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `EventsBasedBillingSegments.UpdateSegmentRequestParams` (4):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `componentId` | `path` | `component_id` | `string` | yes |
| `pricePointId` | `path` | `price_point_id` | `string` | yes |
| `id` | `path` | — | `number` | yes |
| `body` | `body` | — | `UpdateSegmentRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateSegmentRequest` | `updateSegmentRequestSchema` | `src/models/update-segment-request.ts` |
| `SegmentResponse` | `segmentResponseSchema` | `src/models/segment-response.ts` |
| `EventBasedBillingSegmentErrors1` | `eventBasedBillingSegmentErrors1Schema` | `src/models/event-based-billing-segment-errors1.ts` |

