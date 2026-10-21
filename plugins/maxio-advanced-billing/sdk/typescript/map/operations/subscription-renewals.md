<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionRenewals — operations

Accessor: `client.subscriptionRenewals` · Source: `src/resources/subscription-renewals.ts` · 11 operations · Request and error types: namespace `SubscriptionRenewals`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### cancelScheduledRenewalConfiguration

- **Signature**: `cancelScheduledRenewalConfiguration(request: SubscriptionRenewals.CancelScheduledRenewalConfigurationRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationResponse, SubscriptionRenewals.CancelScheduledRenewalConfigurationError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/scheduled_renewals/{id}/cancel.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.CancelScheduledRenewalConfigurationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.CancelScheduledRenewalConfigurationRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalConfigurationResponse` | `scheduledRenewalConfigurationResponseSchema` | `src/models/scheduled-renewal-configuration-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createScheduledRenewalConfiguration

- **Signature**: `createScheduledRenewalConfiguration(request: SubscriptionRenewals.CreateScheduledRenewalConfigurationRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationResponse, SubscriptionRenewals.CreateScheduledRenewalConfigurationError>`
- **Wire**: `POST /subscriptions/{subscription_id}/scheduled_renewals.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.CreateScheduledRenewalConfigurationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.CreateScheduledRenewalConfigurationRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `ScheduledRenewalConfigurationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalConfigurationRequest` | `scheduledRenewalConfigurationRequestSchema` | `src/models/scheduled-renewal-configuration-request.ts` |
| `ScheduledRenewalConfigurationResponse` | `scheduledRenewalConfigurationResponseSchema` | `src/models/scheduled-renewal-configuration-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createScheduledRenewalConfigurationItem

- **Signature**: `createScheduledRenewalConfigurationItem(request: SubscriptionRenewals.CreateScheduledRenewalConfigurationItemRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationItemResponse, SubscriptionRenewals.CreateScheduledRenewalConfigurationItemError>`
- **Wire**: `POST /subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.CreateScheduledRenewalConfigurationItemError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.CreateScheduledRenewalConfigurationItemRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `scheduledRenewalsConfigurationId` | `path` | `scheduled_renewals_configuration_id` | `number` | yes |
| `body` | `body` | — | `ScheduledRenewalConfigurationItemRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalConfigurationItemRequest` | `scheduledRenewalConfigurationItemRequestSchema` | `src/models/scheduled-renewal-configuration-item-request.ts` |
| `ScheduledRenewalConfigurationItemResponse` | `scheduledRenewalConfigurationItemResponseSchema` | `src/models/scheduled-renewal-configuration-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### deleteScheduledRenewalConfigurationItem

- **Signature**: `deleteScheduledRenewalConfigurationItem(request: SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemRequest, options?: RequestOptions): ApiPromise<undefined, SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `scheduledRenewalsConfigurationId` | `path` | `scheduled_renewals_configuration_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listScheduledRenewalConfigurations

- **Signature**: `listScheduledRenewalConfigurations(request: SubscriptionRenewals.ListScheduledRenewalConfigurationsRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationsResponse, ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}/scheduled_renewals.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ScheduledRenewalConfigurationsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionRenewals.ListScheduledRenewalConfigurationsRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `status` | `query` | — | `Status` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `Status` | `statusSchema` | `src/models/status.ts` |
| `ScheduledRenewalConfigurationsResponse` | `scheduledRenewalConfigurationsResponseSchema` | `src/models/scheduled-renewal-configurations-response.ts` |

### lockInScheduledRenewalImmediately

- **Signature**: `lockInScheduledRenewalImmediately(request: SubscriptionRenewals.LockInScheduledRenewalImmediatelyRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationResponse, SubscriptionRenewals.LockInScheduledRenewalImmediatelyError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/scheduled_renewals/{id}/immediate_lock_in.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.LockInScheduledRenewalImmediatelyError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.LockInScheduledRenewalImmediatelyRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalConfigurationResponse` | `scheduledRenewalConfigurationResponseSchema` | `src/models/scheduled-renewal-configuration-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readScheduledRenewalConfiguration

- **Signature**: `readScheduledRenewalConfiguration(request: SubscriptionRenewals.ReadScheduledRenewalConfigurationRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationResponse, ApiError>`
- **Wire**: `GET /subscriptions/{subscription_id}/scheduled_renewals/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ScheduledRenewalConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionRenewals.ReadScheduledRenewalConfigurationRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalConfigurationResponse` | `scheduledRenewalConfigurationResponseSchema` | `src/models/scheduled-renewal-configuration-response.ts` |

### scheduleScheduledRenewalLockIn

- **Signature**: `scheduleScheduledRenewalLockIn(request: SubscriptionRenewals.ScheduleScheduledRenewalLockInRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationResponse, SubscriptionRenewals.ScheduleScheduledRenewalLockInError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/scheduled_renewals/{id}/schedule_lock_in.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.ScheduleScheduledRenewalLockInError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.ScheduleScheduledRenewalLockInRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |
| `body` | `body` | — | `ScheduledRenewalLockInRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalLockInRequest` | `scheduledRenewalLockInRequestSchema` | `src/models/scheduled-renewal-lock-in-request.ts` |
| `ScheduledRenewalConfigurationResponse` | `scheduledRenewalConfigurationResponseSchema` | `src/models/scheduled-renewal-configuration-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### unpublishScheduledRenewalConfiguration

- **Signature**: `unpublishScheduledRenewalConfiguration(request: SubscriptionRenewals.UnpublishScheduledRenewalConfigurationRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationResponse, SubscriptionRenewals.UnpublishScheduledRenewalConfigurationError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/scheduled_renewals/{id}/unpublish.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.UnpublishScheduledRenewalConfigurationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.UnpublishScheduledRenewalConfigurationRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalConfigurationResponse` | `scheduledRenewalConfigurationResponseSchema` | `src/models/scheduled-renewal-configuration-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateScheduledRenewalConfiguration

- **Signature**: `updateScheduledRenewalConfiguration(request: SubscriptionRenewals.UpdateScheduledRenewalConfigurationRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationResponse, SubscriptionRenewals.UpdateScheduledRenewalConfigurationError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/scheduled_renewals/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.UpdateScheduledRenewalConfigurationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.UpdateScheduledRenewalConfigurationRequest` (3):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |
| `body` | `body` | — | `ScheduledRenewalConfigurationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalConfigurationRequest` | `scheduledRenewalConfigurationRequestSchema` | `src/models/scheduled-renewal-configuration-request.ts` |
| `ScheduledRenewalConfigurationResponse` | `scheduledRenewalConfigurationResponseSchema` | `src/models/scheduled-renewal-configuration-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateScheduledRenewalConfigurationItem

- **Signature**: `updateScheduledRenewalConfigurationItem(request: SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemRequest, options?: RequestOptions): ApiPromise<ScheduledRenewalConfigurationItemResponse, SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ScheduledRenewalConfigurationItemResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemRequest` (4):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `scheduledRenewalsConfigurationId` | `path` | `scheduled_renewals_configuration_id` | `number` | yes |
| `id` | `path` | — | `number` | yes |
| `body` | `body` | — | `ScheduledRenewalUpdateRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ScheduledRenewalUpdateRequest` | `scheduledRenewalUpdateRequestSchema` | `src/models/scheduled-renewal-update-request.ts` |
| `ScheduledRenewalConfigurationItemResponse` | `scheduledRenewalConfigurationItemResponseSchema` | `src/models/scheduled-renewal-configuration-item-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

