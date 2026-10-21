<!-- Generated file — do not edit; regenerated with the SDK. -->

# ReferralCodes — operations

Accessor: `client.referralCodes` · Source: `src/resources/referral-codes.ts` · 1 operation · Request and error types: namespace `ReferralCodes`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### validateReferralCode

- **Signature**: `validateReferralCode(request: ReferralCodes.ValidateReferralCodeRequest, options?: RequestOptions): ApiPromise<ReferralValidationResponse, ReferralCodes.ValidateReferralCodeError>`
- **Wire**: `GET /referral_codes/validate.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ReferralValidationResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"`, an instance of `ReferralCodes.ValidateReferralCodeError` — **typed arms**, narrowed on `err.payload.kind`
- **Error arms**: `"singleStringErrorResponse1"` [404] `SingleStringErrorResponse1` · `"undeclared"` [any other] `rawBody: ArrayBuffer`

**Fields** — `ReferralCodes.ValidateReferralCodeRequest` (1):

| Field | Channel | Type | Req |
| --- | --- | --- | --- |
| `code` | `query` | `string` | yes |

| Type | Schema value | Source |
| --- | --- | --- |
| `ReferralValidationResponse` | `referralValidationResponseSchema` | `src/models/referral-validation-response.ts` |
| `SingleStringErrorResponse1` | `singleStringErrorResponse1Schema` | `src/models/single-string-error-response1.ts` |

