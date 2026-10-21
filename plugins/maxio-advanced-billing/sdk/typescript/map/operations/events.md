<!-- Generated file — do not edit; regenerated with the SDK. -->

# Events — operations

Accessor: `client.events` · Source: `src/resources/events.ts` · 3 operations · Request types: namespace `Events`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### listEvents

- **Signature**: `listEvents(request?: Events.ListEventsRequest, options?: RequestOptions): ApiPromise<EventResponse[], ApiError>`
- **Wire**: `GET /events.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `EventResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Events.ListEventsRequest` (11):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `sinceId` | `query` | `since_id` | `number` | no | — |
| `maxId` | `query` | `max_id` | `number` | no | — |
| `direction` | `query` | — | `Direction` | no | `Direction.Desc` |
| `filter` | `query` | — | `EventKey[]` | no | — |
| `dateField` | `query` | `date_field` | `ListEventsDateField` | no | — |
| `startDate` | `query` | `start_date` | `string` | no | — |
| `endDate` | `query` | `end_date` | `string` | no | — |
| `startDatetime` | `query` | `start_datetime` | `string` | no | — |
| `endDatetime` | `query` | `end_datetime` | `string` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `Direction` | `directionSchema` | `src/models/direction.ts` |
| `EventKey` | `eventKeySchema` | `src/models/event-key.ts` |
| `ListEventsDateField` | `listEventsDateFieldSchema` | `src/models/list-events-date-field.ts` |
| `EventResponse` | `eventResponseSchema` | `src/models/event-response.ts` |

### listSubscriptionEvents

- **Signature**: `listSubscriptionEvents(request: Events.ListSubscriptionEventsRequest, options?: RequestOptions): ApiPromise<EventResponse[], ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}/events.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `EventResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Events.ListSubscriptionEventsRequest` (7):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `sinceId` | `query` | `since_id` | `number` | no | — |
| `maxId` | `query` | `max_id` | `number` | no | — |
| `direction` | `query` | — | `Direction` | no | `Direction.Desc` |
| `filter` | `query` | — | `EventKey[]` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `Direction` | `directionSchema` | `src/models/direction.ts` |
| `EventKey` | `eventKeySchema` | `src/models/event-key.ts` |
| `EventResponse` | `eventResponseSchema` | `src/models/event-response.ts` |

### readEventsCount

- **Signature**: `readEventsCount(request?: Events.ReadEventsCountRequest, options?: RequestOptions): ApiPromise<CountResponse, ApiError>`
- **Wire**: `GET /events/count.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `CountResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Events.ReadEventsCountRequest` (6):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `sinceId` | `query` | `since_id` | `number` | no | — |
| `maxId` | `query` | `max_id` | `number` | no | — |
| `direction` | `query` | — | `Direction` | no | `Direction.Desc` |
| `filter` | `query` | — | `EventKey[]` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `Direction` | `directionSchema` | `src/models/direction.ts` |
| `EventKey` | `eventKeySchema` | `src/models/event-key.ts` |
| `CountResponse` | `countResponseSchema` | `src/models/count-response.ts` |

