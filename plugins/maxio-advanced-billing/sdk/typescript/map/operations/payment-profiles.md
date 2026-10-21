<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentProfiles — operations

Accessor: `client.paymentProfiles` · Source: `src/resources/payment-profiles.ts` · 12 operations · Request and error types: namespace `PaymentProfiles`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### changeSubscriptionDefaultPaymentProfile

- **Signature**: `changeSubscriptionDefaultPaymentProfile(request: PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileRequest, options?: RequestOptions): ApiPromise<PaymentProfileResponse, PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileError>`
- **Wire**: `POST /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_payment_profile.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `PaymentProfileResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.ChangeSubscriptionDefaultPaymentProfileRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `paymentProfileId` | `path` | `payment_profile_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `PaymentProfileResponse` | `paymentProfileResponseSchema` | `src/models/payment-profile-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### changeSubscriptionGroupDefaultPaymentProfile

- **Signature**: `changeSubscriptionGroupDefaultPaymentProfile(request: PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileRequest, options?: RequestOptions): ApiPromise<PaymentProfileResponse, PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileError>`
- **Wire**: `POST /subscription_groups/{uid}/payment_profiles/{payment_profile_id}/change_payment_profile.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `PaymentProfileResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.ChangeSubscriptionGroupDefaultPaymentProfileRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `uid` | `path` | — | `string` | yes |
| `paymentProfileId` | `path` | `payment_profile_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `PaymentProfileResponse` | `paymentProfileResponseSchema` | `src/models/payment-profile-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### createPaymentProfile

- **Signature**: `createPaymentProfile(request?: PaymentProfiles.CreatePaymentProfileRequestParams, options?: RequestOptions): ApiPromise<PaymentProfileResponse, PaymentProfiles.CreatePaymentProfileError>`
- **Wire**: `POST /payment_profiles.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `PaymentProfileResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.CreatePaymentProfileError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.CreatePaymentProfileRequestParams` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `body` | `body` | `CreatePaymentProfileRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `CreatePaymentProfileRequest` | `createPaymentProfileRequestSchema` | `src/models/create-payment-profile-request.ts` |
| `PaymentProfileResponse` | `paymentProfileResponseSchema` | `src/models/payment-profile-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### deleteSubscriptionGroupPaymentProfile

- **Signature**: `deleteSubscriptionGroupPaymentProfile(request: PaymentProfiles.DeleteSubscriptionGroupPaymentProfileRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `DELETE /subscription_groups/{uid}/payment_profiles/{payment_profile_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `PaymentProfiles.DeleteSubscriptionGroupPaymentProfileRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `uid` | `path` | — | `string` | yes |
| `paymentProfileId` | `path` | `payment_profile_id` | `number` | yes |

### deleteSubscriptionsPaymentProfile

- **Signature**: `deleteSubscriptionsPaymentProfile(request: PaymentProfiles.DeleteSubscriptionsPaymentProfileRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `DELETE /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `PaymentProfiles.DeleteSubscriptionsPaymentProfileRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |
| `paymentProfileId` | `path` | `payment_profile_id` | `number` | yes |

### deleteUnusedPaymentProfile

- **Signature**: `deleteUnusedPaymentProfile(request: PaymentProfiles.DeleteUnusedPaymentProfileRequest, options?: RequestOptions): ApiPromise<undefined, PaymentProfiles.DeleteUnusedPaymentProfileError>`
- **Wire**: `DELETE /payment_profiles/{payment_profile_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.DeleteUnusedPaymentProfileError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.DeleteUnusedPaymentProfileRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `paymentProfileId` | `path` | `payment_profile_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### listPaymentProfiles

- **Signature**: `listPaymentProfiles(request?: PaymentProfiles.ListPaymentProfilesRequest, options?: RequestOptions): ApiPromise<PaymentProfileResponse[], ApiError>`
- **Wire**: `GET /payment_profiles.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `PaymentProfileResponse[]` — a bare `application/json` array; the success type *is* the array, not a wrapper model
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `PaymentProfiles.ListPaymentProfilesRequest` (3):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |
| `customerId` | `query` | `customer_id` | `number` | no | — |

| Type | Schema value | Source |
| --- | --- | --- |
| `PaymentProfileResponse` | `paymentProfileResponseSchema` | `src/models/payment-profile-response.ts` |

### readOneTimeToken

- **Signature**: `readOneTimeToken(request: PaymentProfiles.ReadOneTimeTokenRequest, options?: RequestOptions): ApiPromise<GetOneTimeTokenRequest, PaymentProfiles.ReadOneTimeTokenError>`
- **Wire**: `GET /one_time_tokens/{chargify_token}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `GetOneTimeTokenRequest`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.ReadOneTimeTokenError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"errorListResponse1"` [404] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.ReadOneTimeTokenRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `chargifyToken` | `path` | `chargify_token` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `GetOneTimeTokenRequest` | `getOneTimeTokenRequestSchema` | `src/models/get-one-time-token-request.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### readPaymentProfile

- **Signature**: `readPaymentProfile(request: PaymentProfiles.ReadPaymentProfileRequest, options?: RequestOptions): ApiPromise<PaymentProfileResponse, PaymentProfiles.ReadPaymentProfileError>`
- **Wire**: `GET /payment_profiles/{payment_profile_id}.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `PaymentProfileResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.ReadPaymentProfileError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.ReadPaymentProfileRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `paymentProfileId` | `path` | `payment_profile_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `PaymentProfileResponse` | `paymentProfileResponseSchema` | `src/models/payment-profile-response.ts` |

### sendRequestUpdatePaymentEmail

- **Signature**: `sendRequestUpdatePaymentEmail(request: PaymentProfiles.SendRequestUpdatePaymentEmailRequest, options?: RequestOptions): ApiPromise<undefined, PaymentProfiles.SendRequestUpdatePaymentEmailError>`
- **Wire**: `POST /subscriptions/{subscription_id}/request_payment_profiles_update.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.SendRequestUpdatePaymentEmailError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.SendRequestUpdatePaymentEmailRequest` (1):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `subscriptionId` | `path` | `subscription_id` | `number` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

### updatePaymentProfile

- **Signature**: `updatePaymentProfile(request: PaymentProfiles.UpdatePaymentProfileRequestParams, options?: RequestOptions): ApiPromise<PaymentProfileResponse, PaymentProfiles.UpdatePaymentProfileError>`
- **Wire**: `PUT /payment_profiles/{payment_profile_id}.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `PaymentProfileResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.UpdatePaymentProfileError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorStringMapResponse1"` [422] `ErrorStringMapResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.UpdatePaymentProfileRequestParams` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `paymentProfileId` | `path` | `payment_profile_id` | `number` | yes |
| `body` | `body` | — | `UpdatePaymentProfileRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `UpdatePaymentProfileRequest` | `updatePaymentProfileRequestSchema` | `src/models/update-payment-profile-request.ts` |
| `PaymentProfileResponse` | `paymentProfileResponseSchema` | `src/models/payment-profile-response.ts` |
| `ErrorStringMapResponse1` | `errorStringMapResponse1Schema` | `src/models/error-string-map-response1.ts` |

### verifyBankAccount

- **Signature**: `verifyBankAccount(request: PaymentProfiles.VerifyBankAccountRequest, options?: RequestOptions): ApiPromise<BankAccountResponse, PaymentProfiles.VerifyBankAccountError>`
- **Wire**: `PUT /bank_accounts/{bank_account_id}/verification.json`
- **Auth**: `basicAuth`
- **Request body**: `application/json` — the `body` field. **Optional**: omit it and the request carries no body and no `Content-Type` header at all
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `BankAccountResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `PaymentProfiles.VerifyBankAccountError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"error404"` [404] no body · `"errorListResponse1"` [422] `ErrorListResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `PaymentProfiles.VerifyBankAccountRequest` (2):

| Field | Channel | Wire | Type | Req |
| --- | --- | --- | --- | --- |
| `bankAccountId` | `path` | `bank_account_id` | `number` | yes |
| `body` | `body` | — | `BankAccountVerificationRequest` | no |

| Type | Schema value | Source |
| --- | --- | --- |
| `BankAccountVerificationRequest` | `bankAccountVerificationRequestSchema` | `src/models/bank-account-verification-request.ts` |
| `BankAccountResponse` | `bankAccountResponseSchema` | `src/models/bank-account-response.ts` |
| `ErrorListResponse1` | `errorListResponse1Schema` | `src/models/error-list-response1.ts` |

