<!-- Generated file — do not edit; regenerated with the SDK. -->

# Sites — operations

Accessor: `client.sites` · Source: `src/resources/sites.ts` · 3 operations · Request types: namespace `Sites`

**Type sources**: every type an operation names, with the file that declares it and the schema value exported beside it. Import every name from `maxio-advanced-billing`; the `Source` path is where to **read** the shape, never what to import. `ApiError`, the runtime error family and the file vocabulary are excluded — see sdk-map.md.

### clearSite

- **Provider rules (Maxio)**: Call on test sites only. Choose `cleanup_scope`: `customers` keeps the catalog, `all` also removes products. Afterwards poll until clearing finishes before seeding fixtures. Notes: `knowledge/operations/sites.md#clearsite`
- **Signature**: `clearSite(request: Sites.ClearSiteRequest, options?: RequestOptions): ApiPromise<undefined, ApiError>`
- **Wire**: `POST /sites/clear_data.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **SDK-sent**: `header Idempotency-Key` (minted per call)
- **Returns**: `undefined` — the operation resolves to nothing
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Sites.ClearSiteRequest` (1):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `cleanupScope` | `query` | `cleanup_scope` | `CleanupScope` | no | `CleanupScope.All` |

| Type | Schema value | Source |
| --- | --- | --- |
| `CleanupScope` | `cleanupScopeSchema` | `src/models/cleanup-scope.ts` |

### listChargifyJsPublicKeys

- **Signature**: `listChargifyJsPublicKeys(request: Sites.ListChargifyJsPublicKeysRequest, options?: RequestOptions): ApiPromise<ListPublicKeysResponse, ApiError>`
- **Wire**: `GET /chargify_js_keys.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `ListPublicKeysResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

**Fields** — `Sites.ListChargifyJsPublicKeysRequest` (2):

| Field | Channel | Wire | Type | Req | Default |
| --- | --- | --- | --- | --- | --- |
| `page` | `query` | — | `number` | no | `1` |
| `perPage` | `query` | `per_page` | `number` | no | `20` |

| Type | Schema value | Source |
| --- | --- | --- |
| `ListPublicKeysResponse` | `listPublicKeysResponseSchema` | `src/models/list-public-keys-response.ts` |

### readSite

- **Provider notes (Maxio)**: `knowledge/operations/sites.md#readsite`
- **Signature**: `readSite(options?: RequestOptions): ApiPromise<SiteResponse, ApiError>`
- **Wire**: `GET /site.json`
- **Auth**: `basicAuth`
- **Request body**: none — no `Content-Type` header is sent
- **Returns**: `SiteResponse`
- **Error**: `MaxioAdvancedBillingError` with `kind: "api"` — untyped, `payload.kind` always `"undeclared"`

| Type | Schema value | Source |
| --- | --- | --- |
| `SiteResponse` | `siteResponseSchema` | `src/models/site-response.ts` |

