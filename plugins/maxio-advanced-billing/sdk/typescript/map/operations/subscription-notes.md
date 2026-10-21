<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionNotes — operations

Accessor: `client.subscriptionNotes` · Source: `src/resources/subscription-notes.ts` · 5 operations · Request and error types: namespace `SubscriptionNotes`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### createSubscriptionNote

- **Signature**: `createSubscriptionNote(request: SubscriptionNotes.CreateSubscriptionNoteRequest, options?: RequestOptions): ApiPromise<SubscriptionNoteResponse, SubscriptionNotes.CreateSubscriptionNoteError>`
- **Wire**: `POST /subscriptions/{subscription_id}/notes.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionNoteResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionNotes.CreateSubscriptionNoteError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionNotes.CreateSubscriptionNoteRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `UpdateSubscriptionNoteRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateSubscriptionNoteRequest` | `updateSubscriptionNoteRequestSchema` | `src/models/update-subscription-note-request.ts` |
| `SubscriptionNoteResponse` | `subscriptionNoteResponseSchema` | `src/models/subscription-note-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### deleteSubscriptionNote

- **Signature**: `deleteSubscriptionNote(request: SubscriptionNotes.DeleteSubscriptionNoteRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}/notes/{note_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionNotes.DeleteSubscriptionNoteRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `noteId` | `path` | `note_id` | `number` | yes |

### listSubscriptionNotes

- **Signature**: `listSubscriptionNotes(request: SubscriptionNotes.ListSubscriptionNotesRequest, options?: RequestOptions): ApiPromise<SubscriptionNoteResponse[], SubscriptionNotes.ListSubscriptionNotesError>`
- **Wire**: `GET /subscriptions/{subscription_id}/notes.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionNoteResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionNotes.ListSubscriptionNotesError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionNotes.ListSubscriptionNotesRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes | — |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionNoteResponse` | `subscriptionNoteResponseSchema` | `src/models/subscription-note-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readSubscriptionNote

- **Signature**: `readSubscriptionNote(request: SubscriptionNotes.ReadSubscriptionNoteRequest, options?: RequestOptions): ApiPromise<SubscriptionNoteResponse, ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}/notes/{note_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SubscriptionNoteResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionNotes.ReadSubscriptionNoteRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `noteId` | `path` | `note_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionNoteResponse` | `subscriptionNoteResponseSchema` | `src/models/subscription-note-response.ts` |

### updateSubscriptionNote

- **Signature**: `updateSubscriptionNote(request: SubscriptionNotes.UpdateSubscriptionNoteRequestParams, options?: RequestOptions): ApiPromise<SubscriptionNoteResponse, SubscriptionNotes.UpdateSubscriptionNoteError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/notes/{note_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionNoteResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionNotes.UpdateSubscriptionNoteError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionNotes.UpdateSubscriptionNoteRequestParams` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `noteId` | `path` | `note_id` | `number` | yes |
| `body` | `body` | — | `UpdateSubscriptionNoteRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateSubscriptionNoteRequest` | `updateSubscriptionNoteRequestSchema` | `src/models/update-subscription-note-request.ts` |
| `SubscriptionNoteResponse` | `subscriptionNoteResponseSchema` | `src/models/subscription-note-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

