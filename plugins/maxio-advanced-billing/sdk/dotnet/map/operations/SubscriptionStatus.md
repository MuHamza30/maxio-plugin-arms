<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionStatus — operations

Accessor: `client.SubscriptionStatus` · Source: `src/MaxioAdvancedBilling/Api/SubscriptionStatus.cs` · 10 operations

**Type sources**: the file declaring each type an operation names (`RawError` excluded — see sdk-map.md).

### CancelDelayedCancellation

- **Auth**: `options.BasicAuth`
- **Signature**: `CancelDelayedCancellation(CancelDelayedCancellationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `DelayedCancellationResponse`
- **Error**: `ApiException<CancelDelayedCancellationError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CancelDelayedCancellationRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/CancelDelayedCancellationRequest.cs` |
| `DelayedCancellationResponse` | `src/MaxioAdvancedBilling/Models/DelayedCancellationResponse.cs` |
| `CancelDelayedCancellationError` | `src/MaxioAdvancedBilling/Errors/CancelDelayedCancellationError.cs` |

### CancelDunning

- **Provider notes (Maxio)**: `knowledge/operations/subscription-status.md#canceldunning`
- **Auth**: `options.BasicAuth`
- **Signature**: `CancelDunning(CancelDunningRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<CancelDunningError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CancelDunningRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/CancelDunningRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `CancelDunningError` | `src/MaxioAdvancedBilling/Errors/CancelDunningError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### CancelSubscription

- **Provider rules (Maxio)**: To cancel now, send neither `cancel_at_end_of_period` nor `scheduled_cancellation_at` (D11). On prepaid, `refund_prepayment_account_balance` defaults to a refund and needs the Schedule Subscription Cancellation feature. Notes: `knowledge/operations/subscription-status.md#cancelsubscription`
- **Auth**: `options.BasicAuth`
- **Signature**: `CancelSubscription(CancelSubscriptionRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<CancelSubscriptionError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetCancelSubscriptionErrorResponse(out CancelSubscriptionErrorResponse)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CancelSubscriptionRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/CancelSubscriptionRequest.cs` |
| `CancellationRequest` | `src/MaxioAdvancedBilling/Models/CancellationRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `CancelSubscriptionError` | `src/MaxioAdvancedBilling/Errors/CancelSubscriptionError.cs` |
| `CancelSubscriptionErrorResponse` | `src/MaxioAdvancedBilling/Models/AnyOf/CancelSubscriptionErrorResponse.cs` |

### InitiateDelayedCancellation

- **Provider rules (Maxio)**: Never call while `past_due` (D11). Send a body-root `uniqueness_token` (R12); a timeout is unknown (R11). The answer is only a message: confirm with `ReadSubscription` that `cancel_at_end_of_period` is `true`. Notes: `knowledge/operations/subscription-status.md#initiatedelayedcancellation`
- **Auth**: `options.BasicAuth`
- **Signature**: `InitiateDelayedCancellation(InitiateDelayedCancellationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `DelayedCancellationResponse`
- **Error**: `ApiException<InitiateDelayedCancellationError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `InitiateDelayedCancellationRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/InitiateDelayedCancellationRequest.cs` |
| `CancellationRequest` | `src/MaxioAdvancedBilling/Models/CancellationRequest.cs` |
| `DelayedCancellationResponse` | `src/MaxioAdvancedBilling/Models/DelayedCancellationResponse.cs` |
| `InitiateDelayedCancellationError` | `src/MaxioAdvancedBilling/Errors/InitiateDelayedCancellationError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### PauseSubscription

- **Provider rules (Maxio)**: Pause only when `current_period_ends_at` is more than 24 hours away. Set any `automatically_resume_at` at least 24 hours ahead; omit it for an open-ended hold. The state becomes `on_hold`, never `paused` (R16). Notes: `knowledge/operations/subscription-status.md#pausesubscription`
- **Auth**: `options.BasicAuth`
- **Signature**: `PauseSubscription(PauseSubscriptionRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<PauseSubscriptionError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `PauseSubscriptionRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/PauseSubscriptionRequest.cs` |
| `PauseRequest` | `src/MaxioAdvancedBilling/Models/PauseRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `PauseSubscriptionError` | `src/MaxioAdvancedBilling/Errors/PauseSubscriptionError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### PreviewRenewal

- **Provider notes (Maxio)**: `knowledge/operations/subscription-status.md#previewrenewal`
- **Auth**: `options.BasicAuth`
- **Signature**: `PreviewRenewal(PreviewRenewalRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `RenewalPreviewResponse`
- **Error**: `ApiException<PreviewRenewalError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `PreviewRenewalRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/PreviewRenewalRequest.cs` |
| `RenewalPreviewRequest` | `src/MaxioAdvancedBilling/Models/RenewalPreviewRequest.cs` |
| `RenewalPreviewResponse` | `src/MaxioAdvancedBilling/Models/RenewalPreviewResponse.cs` |
| `PreviewRenewalError` | `src/MaxioAdvancedBilling/Errors/PreviewRenewalError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### ReactivateSubscription

- **Provider rules (Maxio)**: It can take a payment: turn off the client's automatic retry for it, and settle a timeout by R11. For resume-or-nothing send `resume: {"require_resume": true}`; plain `resume: true` can start a new, charged period (D12). Notes: `knowledge/operations/subscription-status.md#reactivatesubscription`
- **Auth**: `options.BasicAuth`
- **Signature**: `ReactivateSubscription(ReactivateSubscriptionOperationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<ReactivateSubscriptionError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `ReactivateSubscriptionOperationRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/ReactivateSubscriptionOperationRequest.cs` |
| `ReactivateSubscriptionRequest` | `src/MaxioAdvancedBilling/Models/ReactivateSubscriptionRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `ReactivateSubscriptionError` | `src/MaxioAdvancedBilling/Errors/ReactivateSubscriptionError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### ResumeSubscription

- **Provider rules (Maxio)**: Call only when the state is `on_hold`. Check first whether the original renewal date has passed: after it, resuming charges the customer at once (D12). Notes: `knowledge/operations/subscription-status.md#resumesubscription`
- **Auth**: `options.BasicAuth`
- **Signature**: `ResumeSubscription(ResumeSubscriptionRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Query params (wire ← C#)**: `calendar_billing['resumption_charge']` ← `CalendarBillingResumptionCharge`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<ResumeSubscriptionError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `ResumeSubscriptionRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/ResumeSubscriptionRequest.cs` |
| `ResumptionCharge` | `src/MaxioAdvancedBilling/Models/Enums/ResumptionCharge.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `ResumeSubscriptionError` | `src/MaxioAdvancedBilling/Errors/ResumeSubscriptionError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### RetrySubscription

- **Provider rules (Maxio)**: Call only on a `past_due` subscription. It takes a payment and cannot carry a `uniqueness_token`: never resend it automatically, allow 120 seconds, and after a timeout read the subscription back (R11). Notes: `knowledge/operations/subscription-status.md#retrysubscription`
- **Auth**: `options.BasicAuth`
- **Signature**: `RetrySubscription(RetrySubscriptionRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<RetrySubscriptionError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `RetrySubscriptionRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/RetrySubscriptionRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `RetrySubscriptionError` | `src/MaxioAdvancedBilling/Errors/RetrySubscriptionError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### UpdateAutomaticSubscriptionResumption

- **Provider rules (Maxio)**: Call only while the subscription is `on_hold`. Send `automatically_resume_at` at least 24 hours ahead, or `null` to remove the date and leave the hold open-ended. Notes: `knowledge/operations/subscription-status.md#updateautomaticsubscriptionresumption`
- **Auth**: `options.BasicAuth`
- **Signature**: `UpdateAutomaticSubscriptionResumption(UpdateAutomaticSubscriptionResumptionRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionResponse`
- **Error**: `ApiException<UpdateAutomaticSubscriptionResumptionError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `UpdateAutomaticSubscriptionResumptionRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionStatus/UpdateAutomaticSubscriptionResumptionRequest.cs` |
| `PauseRequest` | `src/MaxioAdvancedBilling/Models/PauseRequest.cs` |
| `SubscriptionResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionResponse.cs` |
| `UpdateAutomaticSubscriptionResumptionError` | `src/MaxioAdvancedBilling/Errors/UpdateAutomaticSubscriptionResumptionError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

