<!-- Generated file — do not edit; regenerated with the SDK. -->

# BillingPortal — operations

Accessor: `client.billingPortal` · Source: `src/resources/billing-portal.ts` · 4 operations · Request and error types: namespace `BillingPortal`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### enableBillingPortalForCustomer

- **Provider rules (Maxio)**: Pass `auto_invite=1` if the customer should get the invitation email. Never enable twice; re-send the invite with `resendBillingPortalInvitation`. Notes: `knowledge/operations/billing-portal.md#enablebillingportalforcustomer`
- **Signature**: `enableBillingPortalForCustomer(request: BillingPortal.EnableBillingPortalForCustomerRequest, options?: RequestOptions): ApiPromise<CustomerResponse, BillingPortal.EnableBillingPortalForCustomerError>`
- **Wire**: `POST /portal/customers/{customer_id}/enable.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `CustomerResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `BillingPortal.EnableBillingPortalForCustomerError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `BillingPortal.EnableBillingPortalForCustomerRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `customerId` | `path` | `customer_id` | `number` | yes |
| `autoInvite` | `query` | `auto_invite` | `AutoInvite` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `AutoInvite` | `autoInviteSchema` | `src/models/auto-invite.ts` |
| `CustomerResponse` | `customerResponseSchema` | `src/models/customer-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readBillingPortalLink

- **Provider rules (Maxio)**: Cache the URL and reuse it until `new_link_available_at`; more than 15 requests before then are blocked with 429. Notes: `knowledge/operations/billing-portal.md#readbillingportallink`
- **Signature**: `readBillingPortalLink(request: BillingPortal.ReadBillingPortalLinkRequest, options?: RequestOptions): ApiPromise<PortalManagementLink, BillingPortal.ReadBillingPortalLinkError>`
- **Wire**: `GET /portal/customers/{customer_id}/management_link.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `PortalManagementLink`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `BillingPortal.ReadBillingPortalLinkError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"tooManyManagementLinkRequestsError1"` [429] `TooManyManagementLinkRequestsError1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `BillingPortal.ReadBillingPortalLinkRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `customerId` | `path` | `customer_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `PortalManagementLink` | `portalManagementLinkSchema` | `src/models/portal-management-link.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |
| `TooManyManagementLinkRequestsError1` | `tooManyManagementLinkRequestsError1Schema` | `src/models/too-many-management-link-requests-error1.ts` |

### resendBillingPortalInvitation

- **Signature**: `resendBillingPortalInvitation(request: BillingPortal.ResendBillingPortalInvitationRequest, options?: RequestOptions): ApiPromise<ResentInvitation, BillingPortal.ResendBillingPortalInvitationError>`
- **Wire**: `POST /portal/customers/{customer_id}/invitations/invite.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `ResentInvitation`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `BillingPortal.ResendBillingPortalInvitationError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `BillingPortal.ResendBillingPortalInvitationRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `customerId` | `path` | `customer_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ResentInvitation` | `resentInvitationSchema` | `src/models/resent-invitation.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### revokeBillingPortalAccess

- **Signature**: `revokeBillingPortalAccess(request: BillingPortal.RevokeBillingPortalAccessRequest, options?: RequestOptions): ApiPromise<RevokedInvitation, ApiError>`
- **Wire**: `DELETE /portal/customers/{customer_id}/invitations/revoke.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `RevokedInvitation`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `BillingPortal.RevokeBillingPortalAccessRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `customerId` | `path` | `customer_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `RevokedInvitation` | `revokedInvitationSchema` | `src/models/revoked-invitation.ts` |

