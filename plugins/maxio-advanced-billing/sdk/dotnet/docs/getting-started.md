# Getting started with the Maxio Advanced Billing .NET SDK

**Read when:** you need a Maxio Advanced Billing .NET SDK contract fact. Read it for every contract fact, never memory; `docs/integrate.md` is the workflow that uses it. This is the Maxio Advanced Billing .NET SDK identity and lookup layer (.NET/C# only): install, root namespace, environments, auth pattern, and the SDK map (shipped in this SDK folder), which gives every operation signature and error case by lookup, plus the source file declaring each model, enum and error type.

> **Who this doc is for.** This is the **map layer**: read it to ground every Maxio Advanced Billing SDK fact. `docs/integrate.md` is the workflow that drives it — you collect the contracts for the work in scope into `maxio-advanced-billing-plan.md`, implement from that sheet, and come back to the one map page a row cites for any fact the sheet is missing. Every contract fact comes from here, never from memory.

This page is **SDK-specific**. For general patterns that apply to any APIMatic-generated .NET SDK (auth, calling endpoints, models, error handling, retries, testing), see the companion API-agnostic docs: `docs/client-initialization.md`, `docs/authentication.md`, `docs/calling-endpoints.md`, `docs/models.md`, `docs/error-handling.md`, `docs/configuration-resilience.md`, `docs/testing.md`.

**The SDK map and these companion docs are complementary — read both.** The map (generated from the SDK source, which remains the ground truth) is authoritative for the SDK's *surface* (signatures, model shapes, enums, which error type an operation throws); the companion docs are the *usage layer* on top — the best-practice way to call each piece and the gotchas a signature cannot show. Reading the map or source does not remove the need to read the doc for that step: the companion governs usage and the map governs names. `docs/integrate.md` says when the companions are read.

> **Ground every signature, model, enum, and error type in the SDK map** (`sdk-map.md` + `map/operations/`, in this SDK folder — see the *SDK source* section for where it sits). The map is **method-first**: operation signatures, error cases with their `TryGet…` accessors, pagination and server/auth wiring are on its pages by lookup — and for every type an operation names, the map names the **file that declares it**, so a shape question (fields, wire names, enum values, union accessors) is one targeted file open, never a search. When a map-sourced name fails to compile, re-read the file its row names; **never fill the gap from memory.** Do **not** decompile or reflect over the installed reference, do **not** fetch SDK files from the web ad hoc, and do **not** grep or run other expensive searches over that source.

## SDK identity

|  |  |
| --- | --- |
| API | Maxio Advanced Billing |
| Package | *not published; reference the project in this SDK folder — see *Install* below* |
| SDK source | this SDK folder, the one holding `sdk-map.md` (generated together with these docs) |
| Root namespace | `MaxioAdvancedBilling` (the `using` namespace) |
| Client class | `MaxioAdvancedBillingClient` |
| Options class | `MaxioAdvancedBillingClientOptions` |
| Auth | HTTP **Basic** — set `BasicAuth` |
| Environments | `ServerEnvironment.Us` *(default)* → `Production` `https://{site}.chargify.com`, `Ebb` `https://events.chargify.com/{site}`<br>`ServerEnvironment.Eu` → `Production` `https://{site}.ebilling.maxio.com`, `Ebb` `https://events.chargify.com/{site}` |
| Log environment variable | `MAXIOADVANCEDBILLINGCLIENT_LOG` |
| Target framework | `netstandard2.0` (C# `LangVersion 14`) |

The table above is **orientation, not a copy-paste recipe** — it gives you the names and facts (install, namespaces, the auth *pattern*, the environments), while the actual integration code comes from the companion docs. Read every one the contract sheet's REQUIRED READING names before you start implementing (`docs/integrate.md` makes that binding); the **Integration workflow** below says which governs which step.

## Namespaces (using-directives)

The SDK splits its public types across **separate child namespaces**. C# does **not** import child namespaces transitively, so `using MaxioAdvancedBilling.Models;` alone does **not** make enums, union types, or error types visible — you get `CS0103`/`CS0246` ("name/type does not exist") on build. Add a separate `using` for each kind of type you reference:

| Type | Namespace |
| --- | --- |
| `MaxioAdvancedBillingClient` | `MaxioAdvancedBilling` |
| `MaxioAdvancedBillingClientOptions` | `MaxioAdvancedBilling` |
| `ServerEnvironment` | `MaxioAdvancedBilling.Servers` |

Models, enums, union types and the generated error types each sit in their own child namespace. The map's **Namespaces by content type** table maps each source directory to its namespace, so read the namespace off the path the map gives for the type; anything left ambiguous is settled by the `namespace` declaration at the top of the type's own file.

## Install

**A published package.** Add it to the project that will call Maxio Advanced Billing,
`dotnet add <your-project>.csproj package MaxioAdvancedBilling --version <version>`, from nuget.org or the
feed your team distributes. The package carries this SDK's agent files at its root in the NuGet package
cache: `AGENTS.md`, `sdk-map.md`, `map/`, `docs/`, `knowledge/`, `recipes/`, and under `src/` the source
the map points at. After a restore the project's `obj/project.assets.json` names that folder, and
`dotnet build` prints it on a line that starts "Maxio Advanced Billing SDK:". Start at its root, not in
`src/`.

**Not published yet: reference the SDK project in this SDK folder.** If the SDK is not on NuGet, it ships as source in this SDK folder (`<sdk-folder>` below: the directory holding `sdk-map.md` and `src/`). Reference the project where it sits, from the project that will call Maxio Advanced Billing:

```bash
dotnet add <your-project>.csproj reference <sdk-folder>/src/MaxioAdvancedBilling/MaxioAdvancedBilling.csproj
```

**That reference is local to this machine.** `dotnet add reference` writes a `<ProjectReference>` whose path runs from your project into this SDK folder, so the project builds only where this SDK folder sits at that path — a teammate needs their own copy of this SDK folder and the reference re-pointed at it (remove it with `dotnet remove reference`, then run the command again), and a CI runner without this SDK folder cannot build it. Say so when you hand the work over. If this SDK folder is moved somewhere else, the reference dangles: re-point it the same way.

> **Build against the project where it sits in this SDK folder, and do not copy the SDK source into your repository.** A copy is a fork: the next time the SDK is regenerated the copy stays behind, and the map then describes code you are not building against. The map is read from that same source, so it is both the build reference and the thing the map reads onto — unlike a published SDK, there is no separate clone.

<!-- maxio:start -->
## Maxio: site and credentials

Three values decide which account a call reaches. All three come from configuration, and the host must
refuse to start when one is missing (`knowledge/rules.md` R1, R2).

| Value | Where it goes | If you leave it out |
| --- | --- | --- |
| API key | `BasicAuth.Username`. The password is the letter `x` | No error from the SDK. The call goes out with no credential |
| Site (the subdomain) | `options.Server.Production.Us.Site` or `.Eu.Site`, and the same under `options.Server.Ebb` for `RecordEvent` and `BulkRecordEvents` | No error from the SDK. The default is the literal `subdomain`, so every call goes to `https://subdomain.chargify.com` |
| Region | `options.Environment`: `ServerEnvironment.Us` or `ServerEnvironment.Eu` | `Us` is used, so calls for an EU-hosted site go to the US host |

Only the selected environment's `Site` is read. A site set under `Us` while `Environment` is `Eu` is ignored
with no error.

```csharp
using MaxioAdvancedBilling;
using MaxioAdvancedBilling.Core.Authentication.Basic;
using MaxioAdvancedBilling.Servers;

public static void ConfigureMaxio(
    MaxioAdvancedBillingClientOptions options, string? apiKey, string? site, string? region)
{
    if (string.IsNullOrWhiteSpace(apiKey))
        throw new InvalidOperationException("Maxio:ApiKey is not configured.");
    if (string.IsNullOrWhiteSpace(site))
        throw new InvalidOperationException("Maxio:Site is not configured.");
    if (!ServerEnvironment.TryGetKnownValue(region, out var environment))   // exactly "US" or "EU"
        throw new InvalidOperationException("Maxio:Region must be US or EU.");

    options.BasicAuth = new BasicAuthCredentials { Username = apiKey, Password = "x" };
    options.Environment = environment;
    // Only the selected environment's Site is read, and each server group has its own. Setting all
    // four leaves no combination that falls back to "subdomain".
    options.Server.Production.Us.Site = options.Server.Production.Eu.Site = site;
    options.Server.Ebb.Us.Site = options.Server.Ebb.Eu.Site = site;
}
```

Build the client from it:

```csharp
var options = new MaxioAdvancedBillingClientOptions();
ConfigureMaxio(options, apiKey, site, region);
var client = new MaxioAdvancedBillingClient(httpClient, options);
```

Under dependency injection, check before you register. The `AddMaxioAdvancedBillingClient` callback runs
when the client is first resolved, which is the first request. A check that lives only inside it is not a
startup check:

```csharp
var maxio = builder.Configuration.GetSection("Maxio");
var (apiKey, site, region) = (maxio["ApiKey"], maxio["Site"], maxio["Region"]);
ConfigureMaxio(new MaxioAdvancedBillingClientOptions(), apiKey, site, region);   // throws here, at startup
builder.Services.AddMaxioAdvancedBillingClient(options => ConfigureMaxio(options, apiKey, site, region));
```

The configuration key names are yours to choose. Keep a test site and a live site as separate
configurations, and confirm `client.Sites.ReadSite()` returns `Site.Test == true` before any test that
writes (R2). `docs/authentication.md` has the rules for the failure message: name the missing key, never
echo a value.
<!-- maxio:end -->

## SDK map — look up first, open the named file second, never grep

The SDK ships a generated map **in this SDK folder**, at its root — the map, the SDK and these docs were generated together in one pass, so they cannot drift apart. The map is **method-first**: operation contracts are on its pages; model, enum and error **shapes are deliberately not duplicated there** — the map names the file declaring each type, and you read the shape in that file. Every path below is relative to this SDK folder — the next section has the layout:

- **`sdk-map.md`** — the index and the read-once pages: SDK identity, client construction and the full options surface, the error-handling model (Case A typed / Case B raw), the **defaults table** for operations, the model/enum/error directory conventions, *Namespaces by content type*, and *Servers & auth*.
- **`map/operations/`** — one page per controller, one block per operation: the exact C# signature with its request record's required members, the return type, the error case (A: typed `{Operation}Error` with its `TryGet…` accessors and their statuses / B: `RawError`), pagination and server-group bullets **only where they differ from the defaults**, and a **Type sources** table naming the file that declares every type the operation mentions.
- **Shapes live in the source, one type per file.** Every file under `src/MaxioAdvancedBilling/Models/`, `src/MaxioAdvancedBilling/Errors/` and `src/MaxioAdvancedBilling/Requests/` declares exactly one public type named after the file, so a type name *is* its path: take it from the operation's Type sources table (or the kind's directory — records `src/MaxioAdvancedBilling/Models/`, enums `src/MaxioAdvancedBilling/Models/Enums/`, typed errors `src/MaxioAdvancedBilling/Errors/`, request records `src/MaxioAdvancedBilling/Requests/`, or `src/MaxioAdvancedBilling/Requests/<Controller>/` for an operation on a controller; an operation with several tags is filed under the first tag it declares) and read the fields, `required` flags, enum values and, on a model, the `[JsonPropertyName]` wire names from that one file (a request record is never serialized and carries none). The compiler is the backstop: a wrong name fails to build.

**This map is how you traverse the SDK.** Do **not** grep, glob, `find`, or otherwise scan that source to locate an operation, model, enum, union, or error type — the map (and the name-is-path convention) is the locator. Instead:

1. Open `sdk-map.md` and follow its controller table to the operations pages in scope; read every contract fact (signature, error accessors, pagination) by lookup.
2. **Silence means the default.** The index's defaults table states what holds for every operation (throw-only, no pagination, the default server group, inputs as one request record); an operation's block states only what differs. A block silent on pagination has none — take the default and move on rather than opening the source to confirm it.
3. For a **shape** (model fields, enum values, union accessors, a typed error's payload), open the one declaring file the map names — that is the normal flow here, not a fallback — and read it scoped.
4. The **HTTP verb/route and the endpoint's behavioural prose** live on the operation method itself — the XML `<remarks>` docs in the `Api/{Controller}.cs` file the page header names; what each input means is in the per-member docs on its request record. Read them there when wire-level detail or call-acceptance semantics matter; never reconstruct a route from memory.

<!-- maxio:start -->
**Silence on pagination is not "this list is complete".** No block on this map has a Pagination bullet,
because the SDK pages nothing for you. Maxio still pages its lists: an operation whose request record has
`Page` and `PerPage` members returns one page per call. Reading a list to its end is your loop
(`knowledge/rules.md` R8; `docs/configuration-resilience.md`, "Maxio: retries, timeouts and paging";
`recipes/ListAll.cs`).
<!-- maxio:end -->

Keep lookups cheap — the rules that keep a session's context small:

- Collect the contracts for **every** in-scope operation in **one** pass — signatures and error accessors from the map pages, then required fields with wire names and enum values from the declaring files those pages name — into the **contract sheet** in `maxio-advanced-billing-plan.md`, then implement from the sheet. Do not re-open a map page or source file per field, and never re-look-up a fact the sheet already carries.
- When you do open a source file, read it **scoped**: with an offset/limit, or a search for the one symbol — never dump a whole file into the conversation.
- The SDK's `api-reference.md` is about 550 KB, and the map supersedes it for contract facts. Search it for one operation when you need the spec's own description of it. Never read it whole.

## SDK source — it is already here; the map lives inside it

The SDK source is where the map lives, and it ships in this SDK folder (the directory holding `sdk-map.md`, `src/` and `docs/`), so **there is nothing to clone**: it already sits beside these docs. It is a read-only reference, never in the project repo, and it is also what your build references. Opening the **one declaring file** a map page names is the normal flow here — that is where model, enum and error shapes live. What stays off-limits is *locating* anything by scanning: every file you open is one the map named, opened scoped, never found by grep.

**Resolve its path once, up front**, as the directory that holds `sdk-map.md` and this `docs/` folder, and reuse that path for the rest of your session.

The source you read is the copy in this SDK folder: the source, the map and these docs were generated together in one pass, so there is no ref to pin and nothing can drift apart. If a name from the map fails to compile, trust the compiler, re-read the source file the map's row names, and report the mismatch; never patch around it from memory.

The source stays in this SDK folder, and `maxio-advanced-billing-plan.md` cites it by paths relative to this SDK folder — those paths stay valid for anyone who has this SDK folder.

Then confirm the SDK shape **only** from that source — not by either of these:

- **Do not decompile or run reflection over the built assembly.** A compiled assembly drops what the source carries and the other docs rely on: the XML `<exception>`/parameter doc-comments, the exact parameter names and order, and each method's internal request-builder list.
- **Do not fetch SDK files from the web one at a time** as your way in — `…/blob/…` pages return HTML (not source) and guessed paths fail, which is exactly how ad-hoc fetching breaks. Read the copy in this SDK folder instead.

Layout — where the SDK map's file references resolve, relative to this SDK folder (open these directly; do not scan for them):

- `src/MaxioAdvancedBilling/Api/` — one file per controller/group; **this is where the operation methods live** (the HTTP verb and route, and the XML `<remarks>` docs carrying the endpoint's behavioural prose). The map's per-controller pages name the exact file.
- `src/MaxioAdvancedBilling/Models/` (+ `src/MaxioAdvancedBilling/Models/Enums/`) — body and response models, unions and enums; one public type per file, named after the file.
- `src/MaxioAdvancedBilling/Requests/` — one request record per operation that takes input, carrying the per-member docs for each input; a controller's records sit in `src/MaxioAdvancedBilling/Requests/<Controller>/` (an operation with several tags is filed under the first tag it declares).
- `src/MaxioAdvancedBilling/Errors/` — per-operation `{Operation}Error` types (only Case-A operations have one; the map's rows say which case each operation is).
- `src/MaxioAdvancedBilling/Core/` — HTTP infrastructure (the `SdkException` family, `RawError`, auth, retries, `SdkHook`).
- `src/MaxioAdvancedBilling/Servers/`, `src/MaxioAdvancedBilling/MaxioAdvancedBillingClient.cs`, `src/MaxioAdvancedBilling/ServiceCollectionExtensions.cs` — environments, the client, DI.

**Leave the source where it sits — do not delete it, copy it or edit it.** It is a read-only reference with nothing of yours in it, and keeping it is what lets every later step in this session reuse it. An edit made in it is lost the next time this SDK is regenerated, so report what needs changing instead of patching it; it is the build reference and the map's source at once, so a copy in your repository forks both.

## Idempotency — the injected header is not a key

The generator injects an `Idempotency-Key: Guid.NewGuid()` header on **every non-GET operation that does not already declare that header itself** — fresh on every call, invisible to you, and **not** an idempotency key in any meaningful sense: a value that changes per call deduplicates nothing, and Maxio Advanced Billing may not document reading that header at all. `docs/configuration-resilience.md` explains why a visible header like this is worse than an absent one.

Whether an operation takes a **real**, caller-supplied key is an API fact, visible on that operation's request record: look for a key-shaped member (an idempotency key, a request id) in the record file its **Type sources** table names. Its semantics — retention windows, when it is mandatory — are provider prose, in that member's XML docs and the method's `<remarks>` in the `Api/` file the page names. Some APIs expose **`If-Match` optimistic concurrency** instead — a different guarantee (reject my write if the resource changed) solving a different problem (lost updates, not duplicates); those members show on the request record too. For every write with no key, the answer is reconciliation — `docs/configuration-resilience.md` — not hope.

<!-- maxio:start -->
**For Maxio, do not conclude "no key" from the request record.** No request record in this SDK has a
key-shaped member, and Maxio does not read the `Idempotency-Key` header. Maxio's duplicate key is
`uniqueness_token`, a top-level body field the spec does not declare, so no request record and no body
model has it and the map's contract does not show it (`knowledge/rules.md` R12). Use one per write, its own
for each write a flow makes, and send the same one on every resend of that write. `docs/models.md`,
"Fields the spec does not declare", shows how to send it. Reconciliation is needed as well, not instead.
<!-- maxio:end -->

## Sensitive data — check the request models before you log anything

Whether this API's **request** models carry fields you must never log — card or bank numbers, personal data, message content — is a shape question: each request model's declaring file (the map's Type sources table names it) lists every field with its `[JsonPropertyName]` wire name. If the scope touches such a field, three generator facts decide your logging posture (all in `docs/configuration-resilience.md`): JSON request bodies are logged **verbatim** when `LogRequestBody` is on, with no redaction; form bodies are masked only by deny-list; and leaving `options.Logging.LoggerFactory` unset arms the `MAXIOADVANCEDBILLINGCLIENT_LOG` environment variable, whose `trace` level forces body logging on with no code change and no deploy. So on any build that can carry such a field: `LogRequestBody` stays off, `LoggerFactory` is set explicitly in production, and your own diagnostics never echo a request body on those paths.

Responses are often safer — many APIs return masked variants of what requests carry raw — but that too is a model-shape fact: check the response model's file before assuming.

## Response metadata — status and headers are not on the return value

On a success the SDK returns only the deserialized body: the HTTP status and headers of a successful call are **not on the return value**, and unless the map's error-handling model notes no-throw `{Operation}Result` siblings for this SDK, there is no non-throwing variant to get them from. On an error, what is reachable depends on the operation's error case — its map row: a Case B `RawError` carries `StatusCode`; a typed Case A body may or may not (see `docs/error-handling.md`).

**Hooks are the SDK's own seam for transport metadata.** `options.Hooks` (client-wide) and `requestOptions.Hooks` (per call, appended after the client-wide list) take `SdkHook` instances; `SdkHook.OnResponse((response, context) => …)` sees every raw `HttpResponseMessage` — status, `Retry-After`, rate-limit budget headers, a request-id echo for correlation — and `SdkHook.OnRequest` the outgoing request. A hook runs **inside the retry pipeline, once per attempt**, so "the" value is the last attempt's; a per-call hook can close over a local, which puts the observed value in scope in the same method's `catch`. `RawClient.ExecuteResult` does return an `ApiResult`, but `RawClient` is `internal sealed`, so hooks — not reflection, and not a `DelegatingHandler` you would otherwise need — are the supported way in.

<!-- maxio:start -->
## API knowledge: Maxio's business rules

Beside the map and `src/`, this SDK folder ships `AGENTS.md`, `docs/`, `knowledge/` and `recipes/`. Contract
facts come from the map. Maxio's business rules come from `knowledge/`. Each operation block in
`map/operations/` opens with a **Provider rules (Maxio)** or **Provider notes (Maxio)** bullet that links
the operation's notes section. A block with neither has no provider notes.
`knowledge/README.md` says what each file holds. `knowledge/index.json` lists every operation by the spec's
operationId, with this SDK's call, its route, its map block and its notes. It is large: search it for one
operationId or call name and never read it whole. `docs/integrate.md` says what to read and when.
<!-- maxio:end -->

## Integration workflow — which companion doc governs each step

`docs/integrate.md` says when the companions are read: once, the ones the sheet names, before implementation starts. This list says which one governs which step, so you know where to go back for the section a trap note cites. Each step calls out the trap the signature hides (in *parens*). A typical integration reaches them in this order:

1. **Client & DI setup** — read **docs/client-initialization.md** before you write `new MaxioAdvancedBillingClient(...)`, build its options, or DI-register it. (*The signature will not tell you:* the `HttpClient`/handler pipeline must be long-lived and reused via `IHttpClientFactory`, not rebuilt per request; the SDK client wrapper over it may be transient.)
2. **Authentication** — read **docs/authentication.md** before you set credentials. The scheme(s) this SDK accepts are the credentials properties on `MaxioAdvancedBillingClientOptions` — the identity table above names them. (*The signature will not tell you:* set credentials before constructing the client or in the DI callback, and load secrets from configuration rather than hardcoding.)
3. **Calling an endpoint / building a request body** — read **docs/calling-endpoints.md** before the first `client.{ApiGroup}.{Operation}(...)` call. (*The signature will not tell you:* every input goes on the operation's request record — `required` members must be set, the rest are optional or already carry the spec's default; and the injected `Idempotency-Key` header is not an idempotency key, see *Idempotency* above.)
4. **Models** — read **docs/models.md** the moment a request/response field is not a plain string or number. (*The signature will not tell you:* unions are built with factory methods and read via `TryGet…` (no `new`), enums are `OpenStringEnum<T>` / `OpenIntEnum<T>` records with a generated `Match` — not C# enums, and with no public factory — and unknown response fields are kept on any model that carries an extension-data bag — conventionally `AdditionalProperties`, but a schema that closes itself with `additionalProperties: false` has none, and one that already declares a member of that name pushes the bag to a deduplicated spelling. Check the model's own map row rather than assuming the property is there.)
5. **Error handling** — read **docs/error-handling.md** before you write any `try/catch`. (*The signature will not tell you:* an operation is either Case B (`ApiException<RawError>`, no typed accessors) or Case A (a typed `{Operation}Error`) — how the API mixes them is its own fact, so confirm each operation's case in its map row; and `TryGetRawError` is not a catch-all on the typed errors. Whether no-throw `…Result` variants exist at all is stated once, in the map's defaults table; never assume one does.)
6. **Configuration & resilience** — read **docs/configuration-resilience.md** when you tune retries, timeouts, the base URL, pagination, or logging. (*The signature will not tell you:* `HttpMethodsToRetry` gates **every** retry trigger, so a `POST` is never resent by default — but a `GET` that hangs costs far more than the `Timeout` value suggests, because the per-attempt timeout is itself retried. `Timeout` is per-attempt not total, `RetryOptions.Disabled()` turns retries off, and there **is** a built-in logger on `options.Logging` — whose `LogRequestBody` does not redact JSON.)
7. **Testing** — read **docs/testing.md** before you stub the SDK. (*The signature will not tell you:* the `HttpClient` constructor argument is the test seam; match the project's existing framework and assertion style.)

