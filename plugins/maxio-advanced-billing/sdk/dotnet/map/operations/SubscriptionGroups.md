<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionGroups — operations

Accessor: `client.SubscriptionGroups` · Source: `src/MaxioAdvancedBilling/Api/SubscriptionGroups.cs` · 9 operations

**Type sources**: the file declaring each type an operation names (`RawError` excluded — see sdk-map.md).

### AddSubscriptionToGroup

- **Provider rules (Maxio)**: This decides who pays: the subscription joins the target's group and its payer, or a new group with the target customer as payer (`self`: the subscriber). It must share the target's customer record or hierarchy. Notes: `knowledge/operations/subscription-groups.md#addsubscriptiontogroup`
- **Auth**: `options.BasicAuth`
- **Signature**: `AddSubscriptionToGroup(AddSubscriptionToGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `SubscriptionGroupResponse`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `AddSubscriptionToGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/AddSubscriptionToGroupRequest.cs` |
| `AddSubscriptionToAGroup` | `src/MaxioAdvancedBilling/Models/AddSubscriptionToAGroup.cs` |
| `SubscriptionGroupResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupResponse.cs` |

### CreateSubscriptionGroup

- **Auth**: `options.BasicAuth`
- **Signature**: `CreateSubscriptionGroup(CreateSubscriptionGroupOperationRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
- **Returns**: `SubscriptionGroupResponse`
- **Error**: `ApiException<CreateSubscriptionGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetSubscriptionGroupCreateErrorResponse1(out SubscriptionGroupCreateErrorResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `CreateSubscriptionGroupOperationRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/CreateSubscriptionGroupOperationRequest.cs` |
| `CreateSubscriptionGroupRequest` | `src/MaxioAdvancedBilling/Models/CreateSubscriptionGroupRequest.cs` |
| `SubscriptionGroupResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupResponse.cs` |
| `CreateSubscriptionGroupError` | `src/MaxioAdvancedBilling/Errors/CreateSubscriptionGroupError.cs` |
| `SubscriptionGroupCreateErrorResponse1` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupCreateErrorResponse1.cs` |

### DeleteSubscriptionGroup

- **Auth**: `options.BasicAuth`
- **Signature**: `DeleteSubscriptionGroup(DeleteSubscriptionGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Uid`
- **Returns**: `DeleteSubscriptionGroupResponse`
- **Error**: `ApiException<DeleteSubscriptionGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `DeleteSubscriptionGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/DeleteSubscriptionGroupRequest.cs` |
| `DeleteSubscriptionGroupResponse` | `src/MaxioAdvancedBilling/Models/DeleteSubscriptionGroupResponse.cs` |
| `DeleteSubscriptionGroupError` | `src/MaxioAdvancedBilling/Errors/DeleteSubscriptionGroupError.cs` |

### FindSubscriptionGroup

- **Auth**: `options.BasicAuth`
- **Signature**: `FindSubscriptionGroup(FindSubscriptionGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Query params (wire ← C#)**: `subscription_id` ← `SubscriptionId`
- **Returns**: `FullSubscriptionGroupResponse`
- **Error**: `ApiException<FindSubscriptionGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `FindSubscriptionGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/FindSubscriptionGroupRequest.cs` |
| `FullSubscriptionGroupResponse` | `src/MaxioAdvancedBilling/Models/FullSubscriptionGroupResponse.cs` |
| `FindSubscriptionGroupError` | `src/MaxioAdvancedBilling/Errors/FindSubscriptionGroupError.cs` |

### ListSubscriptionGroups

- **Auth**: `options.BasicAuth`
- **Signature**: `ListSubscriptionGroups(ListSubscriptionGroupsRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
- **Query params (wire ← C#)**: `page` ← `Page`, `per_page` ← `PerPage`, `include` ← `Include`
- **Returns**: `ListSubscriptionGroupsResponse`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ListSubscriptionGroupsRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/ListSubscriptionGroupsRequest.cs` |
| `SubscriptionGroupsListInclude` | `src/MaxioAdvancedBilling/Models/Enums/SubscriptionGroupsListInclude.cs` |
| `ListSubscriptionGroupsResponse` | `src/MaxioAdvancedBilling/Models/ListSubscriptionGroupsResponse.cs` |

### ReadSubscriptionGroup

- **Auth**: `options.BasicAuth`
- **Signature**: `ReadSubscriptionGroup(ReadSubscriptionGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Uid`
- **Query params (wire ← C#)**: `include` ← `Include`
- **Returns**: `FullSubscriptionGroupResponse`
- **Error**: `ApiException<RawError>` — **Case B**

| Type | Source |
| --- | --- |
| `ReadSubscriptionGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/ReadSubscriptionGroupRequest.cs` |
| `SubscriptionGroupInclude` | `src/MaxioAdvancedBilling/Models/Enums/SubscriptionGroupInclude.cs` |
| `FullSubscriptionGroupResponse` | `src/MaxioAdvancedBilling/Models/FullSubscriptionGroupResponse.cs` |

### RemoveSubscriptionFromGroup

- **Auth**: `options.BasicAuth`
- **Signature**: `RemoveSubscriptionFromGroup(RemoveSubscriptionFromGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `SubscriptionId`
- **Returns**: `void` (Task)
- **Error**: `ApiException<RemoveSubscriptionFromGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetNoContent(out RawError)` [404] · `TryGetErrorListResponse1(out ErrorListResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `RemoveSubscriptionFromGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/RemoveSubscriptionFromGroupRequest.cs` |
| `RemoveSubscriptionFromGroupError` | `src/MaxioAdvancedBilling/Errors/RemoveSubscriptionFromGroupError.cs` |
| `ErrorListResponse1` | `src/MaxioAdvancedBilling/Models/ErrorListResponse1.cs` |

### SignupWithSubscriptionGroup

- **Provider rules (Maxio)**: Send one payer source, at most one payment source, `payment_collection_method` by intent (R14), exactly one subscription with `"primary": true`, and a top-level `uniqueness_token`, unchanged when you resend the request (R12). Notes: `knowledge/operations/subscription-groups.md#signupwithsubscriptiongroup`
- **Auth**: `options.BasicAuth`
- **Signature**: `SignupWithSubscriptionGroup(SignupWithSubscriptionGroupRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
- **Returns**: `SubscriptionGroupSignupResponse`
- **Error**: `ApiException<SignupWithSubscriptionGroupError>` — **Case A (typed)**
- **Error accessors**: `TryGetSubscriptionGroupSignupErrorResponse1(out SubscriptionGroupSignupErrorResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `SignupWithSubscriptionGroupRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/SignupWithSubscriptionGroupRequest.cs` |
| `SubscriptionGroupSignupRequest` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupSignupRequest.cs` |
| `SubscriptionGroupSignupResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupSignupResponse.cs` |
| `SignupWithSubscriptionGroupError` | `src/MaxioAdvancedBilling/Errors/SignupWithSubscriptionGroupError.cs` |
| `SubscriptionGroupSignupErrorResponse1` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupSignupErrorResponse1.cs` |

### UpdateSubscriptionGroupMembers

- **Provider rules (Maxio)**: `member_ids` replaces the whole membership: send every subscription that should stay, plus the new ones. An id you leave out is removed from the group, and an empty list removes every member. Notes: `knowledge/operations/subscription-groups.md#updatesubscriptiongroupmembers`
- **Auth**: `options.BasicAuth`
- **Signature**: `UpdateSubscriptionGroupMembers(UpdateSubscriptionGroupMembersRequest request, RequestOptions? requestOptions = null, CancellationToken cancellationToken = default)`
  - required: `Uid`
- **Returns**: `SubscriptionGroupResponse`
- **Error**: `ApiException<UpdateSubscriptionGroupMembersError>` — **Case A (typed)**
- **Error accessors**: `TryGetSubscriptionGroupUpdateErrorResponse1(out SubscriptionGroupUpdateErrorResponse1)` [422] · `TryGetRawError(out RawError)` [fallback]

| Type | Source |
| --- | --- |
| `UpdateSubscriptionGroupMembersRequest` | `src/MaxioAdvancedBilling/Requests/SubscriptionGroups/UpdateSubscriptionGroupMembersRequest.cs` |
| `UpdateSubscriptionGroupRequest` | `src/MaxioAdvancedBilling/Models/UpdateSubscriptionGroupRequest.cs` |
| `SubscriptionGroupResponse` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupResponse.cs` |
| `UpdateSubscriptionGroupMembersError` | `src/MaxioAdvancedBilling/Errors/UpdateSubscriptionGroupMembersError.cs` |
| `SubscriptionGroupUpdateErrorResponse1` | `src/MaxioAdvancedBilling/Models/SubscriptionGroupUpdateErrorResponse1.cs` |

