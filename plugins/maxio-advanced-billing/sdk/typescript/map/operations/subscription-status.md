<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionStatus — operations

Accessor: `client.subscriptionStatus` · Source: `src/resources/subscription-status.ts` · 10 operations · Request and error types: namespace `SubscriptionStatus`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### cancelDelayedCancellation

- **Signature**: `cancelDelayedCancellation(request: SubscriptionStatus.CancelDelayedCancellationRequest, options?: RequestOptions): ApiPromise<DelayedCancellationResponse, SubscriptionStatus.CancelDelayedCancellationError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}/delayed_cancel.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `DelayedCancellationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.CancelDelayedCancellationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.CancelDelayedCancellationRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `DelayedCancellationResponse` | `delayedCancellationResponseSchema` | `src/models/delayed-cancellation-response.ts` |

### cancelDunning

- **Provider notes (Maxio)**: `knowledge/operations/subscription-status.md#canceldunning`
- **Signature**: `cancelDunning(request: SubscriptionStatus.CancelDunningRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionStatus.CancelDunningError>`
- **Wire**: `POST /subscriptions/{subscription_id}/cancel_dunning.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.CancelDunningError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.CancelDunningRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### cancelSubscription

- **Provider rules (Maxio)**: To cancel now, send neither `cancel_at_end_of_period` nor `scheduled_cancellation_at` (D11). On prepaid, `refund_prepayment_account_balance` defaults to a refund and needs the Schedule Subscription Cancellation feature. Notes: `knowledge/operations/subscription-status.md#cancelsubscription`
- **Signature**: `cancelSubscription(request: SubscriptionStatus.CancelSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionStatus.CancelSubscriptionError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.CancelSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"cancelSubscriptionErrorResponse"` [422] `CancelSubscriptionErrorResponse` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.CancelSubscriptionRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `CancellationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CancellationRequest` | `cancellationRequestSchema` | `src/models/cancellation-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `CancelSubscriptionErrorResponse` | `cancelSubscriptionErrorResponseSchema` | `src/models/unions/cancel-subscription-error-response.ts` |

### initiateDelayedCancellation

- **Provider rules (Maxio)**: Never call while `past_due` (D11). Send a body-root `uniqueness_token` (R12); a timeout is unknown (R11). The answer is only a message: confirm with `readSubscription` that `cancel_at_end_of_period` is `true`. Notes: `knowledge/operations/subscription-status.md#initiatedelayedcancellation`
- **Signature**: `initiateDelayedCancellation(request: SubscriptionStatus.InitiateDelayedCancellationRequest, options?: RequestOptions): ApiPromise<DelayedCancellationResponse, SubscriptionStatus.InitiateDelayedCancellationError>`
- **Wire**: `POST /subscriptions/{subscription_id}/delayed_cancel.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `DelayedCancellationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.InitiateDelayedCancellationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.InitiateDelayedCancellationRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `CancellationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CancellationRequest` | `cancellationRequestSchema` | `src/models/cancellation-request.ts` |
| `DelayedCancellationResponse` | `delayedCancellationResponseSchema` | `src/models/delayed-cancellation-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### pauseSubscription

- **Provider rules (Maxio)**: Pause only when `current_period_ends_at` is more than 24 hours away. Set any `automatically_resume_at` at least 24 hours ahead; omit it for an open-ended hold. The state becomes `on_hold`, never `paused` (R16). Notes: `knowledge/operations/subscription-status.md#pausesubscription`
- **Signature**: `pauseSubscription(request: SubscriptionStatus.PauseSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionStatus.PauseSubscriptionError>`
- **Wire**: `POST /subscriptions/{subscription_id}/hold.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.PauseSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.PauseSubscriptionRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `PauseRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `PauseRequest` | `pauseRequestSchema` | `src/models/pause-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### previewRenewal

- **Provider notes (Maxio)**: `knowledge/operations/subscription-status.md#previewrenewal`
- **Signature**: `previewRenewal(request: SubscriptionStatus.PreviewRenewalRequest, options?: RequestOptions): ApiPromise<RenewalPreviewResponse, SubscriptionStatus.PreviewRenewalError>`
- **Wire**: `POST /subscriptions/{subscription_id}/renewals/preview.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `RenewalPreviewResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.PreviewRenewalError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.PreviewRenewalRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `RenewalPreviewRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `RenewalPreviewRequest` | `renewalPreviewRequestSchema` | `src/models/renewal-preview-request.ts` |
| `RenewalPreviewResponse` | `renewalPreviewResponseSchema` | `src/models/renewal-preview-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### reactivateSubscription

- **Provider rules (Maxio)**: It can take a payment: turn off the client's automatic retry for it, and settle a timeout by R11. For resume-or-nothing send `resume: {"require_resume": true}`; plain `resume: true` can start a new, charged period (D12). Notes: `knowledge/operations/subscription-status.md#reactivatesubscription`
- **Signature**: `reactivateSubscription(request: SubscriptionStatus.ReactivateSubscriptionRequestParams, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionStatus.ReactivateSubscriptionError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/reactivate.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.ReactivateSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.ReactivateSubscriptionRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `ReactivateSubscriptionRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `ReactivateSubscriptionRequest` | `reactivateSubscriptionRequestSchema` | `src/models/reactivate-subscription-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### resumeSubscription

- **Provider rules (Maxio)**: Call only when the state is `on_hold`. Check first whether the original renewal date has passed: after it, resuming charges the customer at once (D12). Notes: `knowledge/operations/subscription-status.md#resumesubscription`
- **Signature**: `resumeSubscription(request: SubscriptionStatus.ResumeSubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionStatus.ResumeSubscriptionError>`
- **Wire**: `POST /subscriptions/{subscription_id}/resume.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.ResumeSubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.ResumeSubscriptionRequest` (2):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes | — |
| `calendarBillingResumptionCharge` | `query` | `calendar_billing['resumption_charge']` | `ResumptionCharge` | no | `ResumptionCharge.Prorated` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResumptionCharge` | `resumptionChargeSchema` | `src/models/resumption-charge.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### retrySubscription

- **Provider rules (Maxio)**: Call only on a `past_due` subscription. It takes a payment and cannot carry a `uniqueness_token`: never resend it automatically, allow 120 seconds, and after a timeout read the subscription back (R11). Notes: `knowledge/operations/subscription-status.md#retrysubscription`
- **Signature**: `retrySubscription(request: SubscriptionStatus.RetrySubscriptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionStatus.RetrySubscriptionError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/retry.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.RetrySubscriptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.RetrySubscriptionRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updateAutomaticSubscriptionResumption

- **Provider rules (Maxio)**: Call only while the subscription is `on_hold`. Send `automatically_resume_at` at least 24 hours ahead, or `null` to remove the date and leave the hold open-ended. Notes: `knowledge/operations/subscription-status.md#updateautomaticsubscriptionresumption`
- **Signature**: `updateAutomaticSubscriptionResumption(request: SubscriptionStatus.UpdateAutomaticSubscriptionResumptionRequest, options?: RequestOptions): ApiPromise<SubscriptionResponse, SubscriptionStatus.UpdateAutomaticSubscriptionResumptionError>`
- **Wire**: `PUT /subscriptions/{subscription_id}/hold.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionStatus.UpdateAutomaticSubscriptionResumptionError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionStatus.UpdateAutomaticSubscriptionResumptionRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `PauseRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `PauseRequest` | `pauseRequestSchema` | `src/models/pause-request.ts` |
| `SubscriptionResponse` | `subscriptionResponseSchema` | `src/models/subscription-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

