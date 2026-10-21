<!-- Generated file — do not edit; regenerated with the SDK. -->

# SubscriptionGroups — operations

Accessor: `client.subscriptionGroups` · Source: `src/resources/subscription-groups.ts` · 9 operations · Request and error types: namespace `SubscriptionGroups`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### addSubscriptionToGroup

- **Provider rules (Maxio)**: This decides who pays: the subscription joins the target's group and its payer, or a new group with the target customer as payer (`self`: the subscriber). It must share the target's customer record or hierarchy. Notes: `knowledge/operations/subscription-groups.md#addsubscriptiontogroup`
- **Signature**: `addSubscriptionToGroup(request: SubscriptionGroups.AddSubscriptionToGroupRequest, options?: RequestOptions): ApiPromise<SubscriptionGroupResponse, ApiError>`
- **Wire**: `POST /subscriptions/{subscription_id}/group.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionGroupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionGroups.AddSubscriptionToGroupRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `body` | `body` | — | `AddSubscriptionToAGroup` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `AddSubscriptionToAGroup` | `addSubscriptionToAGroupSchema` | `src/models/add-subscription-to-agroup.ts` |
| `SubscriptionGroupResponse` | `subscriptionGroupResponseSchema` | `src/models/subscription-group-response.ts` |

### createSubscriptionGroup

- **Signature**: `createSubscriptionGroup(request: SubscriptionGroups.CreateSubscriptionGroupRequestParams, options?: RequestOptions): ApiPromise<SubscriptionGroupResponse, SubscriptionGroups.CreateSubscriptionGroupError>`
- **Wire**: `POST /subscription_groups.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionGroupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroups.CreateSubscriptionGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"subscriptionGroupCreateErrorResponse1"` [422] `SubscriptionGroupCreateErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroups.CreateSubscriptionGroupRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreateSubscriptionGroupRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreateSubscriptionGroupRequest` | `createSubscriptionGroupRequestSchema` | `src/models/create-subscription-group-request.ts` |
| `SubscriptionGroupResponse` | `subscriptionGroupResponseSchema` | `src/models/subscription-group-response.ts` |
| `SubscriptionGroupCreateErrorResponse1` | `subscriptionGroupCreateErrorResponse1Schema` | `src/models/subscription-group-create-error-response1.ts` |

### deleteSubscriptionGroup

- **Signature**: `deleteSubscriptionGroup(request: SubscriptionGroups.DeleteSubscriptionGroupRequest, options?: RequestOptions): ApiPromise<DeleteSubscriptionGroupResponse, SubscriptionGroups.DeleteSubscriptionGroupError>`
- **Wire**: `DELETE /subscription_groups/{uid}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `DeleteSubscriptionGroupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroups.DeleteSubscriptionGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroups.DeleteSubscriptionGroupRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `DeleteSubscriptionGroupResponse` | `deleteSubscriptionGroupResponseSchema` | `src/models/delete-subscription-group-response.ts` |

### findSubscriptionGroup

- **Signature**: `findSubscriptionGroup(request: SubscriptionGroups.FindSubscriptionGroupRequest, options?: RequestOptions): ApiPromise<FullSubscriptionGroupResponse, SubscriptionGroups.FindSubscriptionGroupError>`
- **Wire**: `GET /subscription_groups/lookup.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FullSubscriptionGroupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroups.FindSubscriptionGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroups.FindSubscriptionGroupRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `query` | `subscription_id` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `FullSubscriptionGroupResponse` | `fullSubscriptionGroupResponseSchema` | `src/models/full-subscription-group-response.ts` |

### listSubscriptionGroups

- **Signature**: `listSubscriptionGroups(request: SubscriptionGroups.ListSubscriptionGroupsRequest, options?: RequestOptions): ApiPromise<ListSubscriptionGroupsResponse, ApiError>`
- **Wire**: `GET /subscription_groups.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListSubscriptionGroupsResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionGroups.ListSubscriptionGroupsRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `include` | `query` | — | `SubscriptionGroupsListInclude[]` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionGroupsListInclude` | `subscriptionGroupsListIncludeSchema` | `src/models/subscription-groups-list-include.ts` |
| `ListSubscriptionGroupsResponse` | `listSubscriptionGroupsResponseSchema` | `src/models/list-subscription-groups-response.ts` |

### readSubscriptionGroup

- **Signature**: `readSubscriptionGroup(request: SubscriptionGroups.ReadSubscriptionGroupRequest, options?: RequestOptions): ApiPromise<FullSubscriptionGroupResponse, ApiError>`
- **Wire**: `GET /subscription_groups/{uid}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `FullSubscriptionGroupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `SubscriptionGroups.ReadSubscriptionGroupRequest` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |
| `include` | `query` | `SubscriptionGroupInclude[]` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionGroupInclude` | `subscriptionGroupIncludeSchema` | `src/models/subscription-group-include.ts` |
| `FullSubscriptionGroupResponse` | `fullSubscriptionGroupResponseSchema` | `src/models/full-subscription-group-response.ts` |

### removeSubscriptionFromGroup

- **Signature**: `removeSubscriptionFromGroup(request: SubscriptionGroups.RemoveSubscriptionFromGroupRequest, options?: RequestOptions): ApiPromise<undefined, SubscriptionGroups.RemoveSubscriptionFromGroupError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}/group.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroups.RemoveSubscriptionFromGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroups.RemoveSubscriptionFromGroupRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### signupWithSubscriptionGroup

- **Provider rules (Maxio)**: Send one payer source, at most one payment source, `payment_collection_method` by intent (R14), exactly one subscription with `"primary": true`, and a top-level `uniqueness_token`, unchanged when you resend the request (R12). Notes: `knowledge/operations/subscription-groups.md#signupwithsubscriptiongroup`
- **Signature**: `signupWithSubscriptionGroup(request: SubscriptionGroups.SignupWithSubscriptionGroupRequest, options?: RequestOptions): ApiPromise<SubscriptionGroupSignupResponse, SubscriptionGroups.SignupWithSubscriptionGroupError>`
- **Wire**: `POST /subscription_groups/signup.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionGroupSignupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroups.SignupWithSubscriptionGroupError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"subscriptionGroupSignupErrorResponse1"` [422] `SubscriptionGroupSignupErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroups.SignupWithSubscriptionGroupRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `SubscriptionGroupSignupRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `SubscriptionGroupSignupRequest` | `subscriptionGroupSignupRequestSchema` | `src/models/subscription-group-signup-request.ts` |
| `SubscriptionGroupSignupResponse` | `subscriptionGroupSignupResponseSchema` | `src/models/subscription-group-signup-response.ts` |
| `SubscriptionGroupSignupErrorResponse1` | `subscriptionGroupSignupErrorResponse1Schema` | `src/models/subscription-group-signup-error-response1.ts` |

### updateSubscriptionGroupMembers

- **Provider rules (Maxio)**: `member_ids` replaces the whole membership: send every subscription that should stay, plus the new ones. An id you leave out is removed from the group, and an empty list removes every member. Notes: `knowledge/operations/subscription-groups.md#updatesubscriptiongroupmembers`
- **Signature**: `updateSubscriptionGroupMembers(request: SubscriptionGroups.UpdateSubscriptionGroupMembersRequest, options?: RequestOptions): ApiPromise<SubscriptionGroupResponse, SubscriptionGroups.UpdateSubscriptionGroupMembersError>`
- **Wire**: `PUT /subscription_groups/{uid}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `SubscriptionGroupResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `SubscriptionGroups.UpdateSubscriptionGroupMembersError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"subscriptionGroupUpdateErrorResponse1"` [422] `SubscriptionGroupUpdateErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `SubscriptionGroups.UpdateSubscriptionGroupMembersRequest` (2):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `uid` | `path` | `string` | yes |
| `body` | `body` | `UpdateSubscriptionGroupRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdateSubscriptionGroupRequest` | `updateSubscriptionGroupRequestSchema` | `src/models/update-subscription-group-request.ts` |
| `SubscriptionGroupResponse` | `subscriptionGroupResponseSchema` | `src/models/subscription-group-response.ts` |
| `SubscriptionGroupUpdateErrorResponse1` | `subscriptionGroupUpdateErrorResponse1Schema` | `src/models/subscription-group-update-error-response1.ts` |

