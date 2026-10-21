<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionGroupStatus — operations

Accessor: `client.SubscriptionGroupStatus` · Source: `src/MaxioAdvancedBilling/Api/SubscriptionGroupStatus.cs` · 4 operations

**Type sources**: the file declaring each type an operation names (`RawError` excluded — see sdk-map.md).

### CancelDelayedCancellationForGroup

- **Provider notes (Maxio)**: `knowledge/operations/subscription-group-status.md#canceldelayedcancellationforgroup`
- **Auth**: `options.BasicAuth`
- **Signature**: `CancelDelayedCancellationForGroup(CancelDelayedCancellationForGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Uid`
- **Returns**: `void` (Task)
- **Error**: `ApiException<CancelDelayedCancellationForGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CancelDelayedCancellationForGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroupStatus/CancelDelayedCancellationForGroupRequest.cs` |
| `CancelDelayedCancellationForGroupError` | `src/MaxioAdvancedBilling/Errors/CancelDelayedCancellationForGroupError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### CancelSubscriptionsInGroup

- **Provider rules (Maxio)**: This cancels every subscription in the group at once. Unbilled metered and prepaid usage is charged only when you send `charge_unbilled_usage: true`: decide it. Notes: `knowledge/operations/subscription-group-status.md#cancelsubscriptionsingroup`
- **Auth**: `options.BasicAuth`
- **Signature**: `CancelSubscriptionsInGroup(CancelSubscriptionsInGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Uid`
- **Returns**: `void` (Task)
- **Error**: `ApiException<CancelSubscriptionsInGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CancelSubscriptionsInGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroupStatus/CancelSubscriptionsInGroupRequest.cs` |
| `CancelGroupedSubscriptionsRequest` | `src/MaxioAdvancedBilling/Models/CancelGroupedSubscriptionsRequest.cs` |
| `CancelSubscriptionsInGroupError` | `src/MaxioAdvancedBilling/Errors/CancelSubscriptionsInGroupError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### InitiateDelayedCancellationForGroup

- **Provider rules (Maxio)**: Call only when every subscription in the group is on automatic billing and the group is not `past_due`. Notes: `knowledge/operations/subscription-group-status.md#initiatedelayedcancellationforgroup`
- **Auth**: `options.BasicAuth`
- **Signature**: `InitiateDelayedCancellationForGroup(InitiateDelayedCancellationForGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Uid`
- **Returns**: `void` (Task)
- **Error**: `ApiException<InitiateDelayedCancellationForGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `InitiateDelayedCancellationForGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroupStatus/InitiateDelayedCancellationForGroupRequest.cs` |
| `InitiateDelayedCancellationForGroupError` | `src/MaxioAdvancedBilling/Errors/InitiateDelayedCancellationForGroupError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### ReactivateSubscriptionGroup

- **Provider rules (Maxio)**: It attempts payment: canceled invoices from the primary's current period are reopened and charged, and a new period adds new charges. Decide `resume` and `resume_members`. After a timeout read the group back first (R11). Notes: `knowledge/operations/subscription-group-status.md#reactivatesubscriptiongroup`
- **Auth**: `options.BasicAuth`
- **Signature**: `ReactivateSubscriptionGroup(ReactivateSubscriptionGroupOperationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Uid`
- **Returns**: `ReactivateSubscriptionGroupResponse`
- **Error**: `ApiException<ReactivateSubscriptionGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `ReactivateSubscriptionGroupOperationRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroupStatus/ReactivateSubscriptionGroupOperationRequest.cs` |
| `ReactivateSubscriptionGroupRequest` | `src/MaxioAdvancedBilling/Models/ReactivateSubscriptionGroupRequest.cs` |
| `ReactivateSubscriptionGroupResponse` | `src/MaxioAdvancedBilling/Models/ReactivateSubscriptionGroupResponse.cs` |
| `ReactivateSubscriptionGroupError` | `src/MaxioAdvancedBilling/Errors/ReactivateSubscriptionGroupError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

