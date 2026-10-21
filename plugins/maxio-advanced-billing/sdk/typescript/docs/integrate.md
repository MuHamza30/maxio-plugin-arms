# Maxio Advanced Billing TypeScript SDK — Integration workflow (lookup layer + contract sheet)

**Read when:** you are about to write or change code that calls Maxio Advanced Billing through this TypeScript SDK, or a call through it errors, fails to compile, or behaves unexpectedly. Read `AGENTS.md` at the SDK root first, then this page, then only what this page sends you to. This page is the workflow, and it sets five gates: (1) read `docs/getting-started.md`, confirm `maxio-advanced-billing` resolves, and take every contract fact from the SDK map that ships with it; (2) write the plan to `maxio-advanced-billing-plan.md` at the repo root, and create or edit no project file until its contract sheet has no open lookups and you have read it; (3) read every companion page in `docs/` that the sheet names; (4) decide the host once and explicitly, because a client built with no options silently selects `ServerEnvironment.Us`; (5) the memory ban: every signature, request field, channel, header default, error arm and enum member comes from a lookup, never from recall or runtime introspection.

You do the SDK lookups yourself: `docs/getting-started.md` is your **lookup layer** — read it and ground every contract fact in it (and in the source files its table names) before writing code. The companion docs beside it in `docs/` are a different thing: they are API-agnostic *usage* guidance, they are yours to read, and Step 1c below says which of them you read and when.

## Your lookup layer

- **`docs/getting-started.md`** is the entry point for every SDK need. It carries the SDK's identity (package name, version, Node floor, how it installs), the single import specifier and what the root exports, the server environments and the base-URL knob, the auth pattern, the resources, and a **file table** naming the one file that owns each kind of fact. Read it before any lookup.
- **The SDK map is your lookup surface, and you open it yourself.** The SDK ships `sdk-map.md` and `map/operations/` at its package root — and because `package.json`'s `files` list includes them, **installing the package puts the map in `node_modules/maxio-advanced-billing/`**. There is nothing to clone. `docs/getting-started.md` tells you how to traverse it: read `sdk-map.md` once, then the one resource page your operations live on.
- **The installed package is the ground truth; the file table is only the locator.** This page ships in the same package as the map, so the map is always at hand: `sdk-map.md` and `map/operations/`, one directory up from this `docs/` directory. What you confirm is that the project builds against this same copy: run `node -e "console.log(require.resolve('maxio-advanced-billing/package.json'))"`. If it prints a different directory, the project uses another copy of the SDK, so read the map, the docs and the knowledge in that copy. If it fails, the package is not installed in the project yet: `docs/getting-started.md`'s *Install* section carries what to run. This SDK is **not published to a registry**; it installs from this SDK folder. A fact that neither the map nor the file it names settles is `UNVERIFIED`: say what would settle it, and do not fill the hole from memory.
- **Read scoped.** Search for the one symbol and read the lines around it rather than whole files, and never copy a design comment's rationale onto a contract sheet — the sheet carries facts an implementer must obey, not the reasoning behind them.
- **Write a contract sheet with no open lookups** before you implement: exact signatures with the right request type name, every request field with its channel, wire name and default, required-vs-optional-vs-nullable members, the error arms per operation with the status each covers, and enum members for the operations in scope. `docs/getting-started.md` ends with a checklist of what a sheet for this SDK is incomplete without — treat that as the checklist for your own sheet, and collect every in-scope operation in ONE pass rather than re-opening a map page per field.

**Scope guard:** the APIMatic-generated Maxio Advanced Billing **TypeScript SDK** (package and import specifier `maxio-advanced-billing`, client `MaxioAdvancedBillingClient`) in **TypeScript or JavaScript projects only**. Unrelated API, or any language other than TypeScript/JavaScript — do nothing; this doc does not apply.

<!-- maxio:start -->
## Provider knowledge: Maxio's business rules

The map gives you Maxio Advanced Billing's call surface. It cannot give you Maxio's business rules: what
must exist before a call succeeds, which of two overlapping operations to use, which values silently do
nothing, and what each rejection means. Agents get those wrong far more often than signatures. The rules
ship in this SDK folder under `knowledge/`. Never answer a business-rule question from memory.

Read the ten rules, then only the sections your task touches. `knowledge/` is never read whole, and
neither is any file in it: find the item by its id (`R12`, `D3`, `L2`) or its heading and read that item.

| When | Read |
| --- | --- |
| Once, before anything else | The ten rules. They are in `AGENTS.md`, which you read before this page, and at the top of `sdk-map.md`. Do not read `knowledge/rules.md` whole |
| For each operation in scope, as you write its contract-sheet row | The first bullet of its block on the map, **Provider rules (Maxio)** or **Provider notes (Maxio)**, and the one section under `knowledge/operations/` that the bullet links. A block with neither bullet has no provider notes: record that and move on |
| When one of those lines or sections cites an id, or the flow needs an order of calls or a choice between operations | That one item in `knowledge/rules.md`, `knowledge/decisions.md` or `knowledge/lifecycles.md`. Each item is a `###` heading that starts with its id (`### L2 · Signup, end to end`), so search for the id |
| When a rule sends you to a named section of a `docs/` page | That section, not the page. The four are listed in `docs/getting-started.md`, "API knowledge" |
| When the task needs something this SDK does not do: paging every list, a safe signup, subscription-state checks, webhook verification, a request limit | `recipes/README.md`, then only the recipe you copy. Copy and adapt; do not re-invent |
| When Maxio rejects a call, in a smoke, a test or the running app | The row for that status and message in `knowledge/failures.md`, before you change code |
| Once, when the code is complete and before you report | `knowledge/go-live.md` |

Where a choice depends on the user's intent and the task does not say, ask.

What this changes on the plan:
- The plan lists every *Before you call* precondition of an in-scope operation as a step before that call.
- Each contract-sheet operation row carries a **Provider notes** cell: the notes link from the map, or
  `no provider notes`. Copy the **Provider rules** line into the row as directives. A field that line
  names is required for this task even where the type marks it optional: it gets a row in OPTIONAL FIELDS
  (1b.3) that cites the rule.
- **CROSS-OPERATION INVARIANTS** (1b.2) start from the `knowledge/lifecycles.md` items you read, then add
  what the task implies.
- **DUPLICATE CLAIMS** and **UNKNOWN OUTCOMES** (1b.1) follow R12 and R11 on every write. 1b.1 says how.
- A provider rule outranks your memory of this API and any default you would otherwise pick. Where a rule
  and the SDK disagree on a contract fact (a name, a type), the map wins; record the conflict. That never
  removes a field the spec does not declare: `uniqueness_token` is in no **Fields** table and on no model,
  and R12 still requires it.

A 4xx never proves that a call works. A 409 on a write means its outcome is unknown, a 422 may be a
3-D Secure `action_link` or an account block that no change to the request fixes, and a 404 on a lookup
by your own reference is the normal "not there" answer (`knowledge/rules.md` R13).

**The project block.** `knowledge/AGENTS.block.md` holds the ten rules as a block for the project's own
`AGENTS.md`. Adding it is the user's decision: `AGENTS.md` in the SDK folder, section *The project block*,
says when to add it and when only to mention it in your report.
<!-- maxio:end -->

## Workflow

**If the user opens with a reported SDK error, a compile failure, or unexpected Maxio Advanced Billing behaviour** (not new feature work), skip the plan-first flow: read `docs/getting-started.md` and `docs/error-handling.md`, look the failing symbol up on the map page or in the file the table names, and fix from what you find.

<!-- maxio:start -->
If what failed is a call that Maxio answered with a 4xx, the fix is rarely in the SDK. Print the status
and Maxio's own message (`docs/error-handling.md`, "Maxio: reading a rejection"), then find them in
`knowledge/failures.md` before you change code.
<!-- maxio:end -->

Otherwise, for implementation work:

### Step 1 — Plan first (always, for any implementation work)

Your FIRST action in this step is to read `docs/getting-started.md` and work through the user's full request (all features in scope — one plan covers the whole implementation). Read `docs/error-handling.md` before you write the plan too: table 1b.4 is decided from it. Then write the plan and its contract sheet to `<project repo root>/maxio-advanced-billing-plan.md` — that absolute path, not a location you pick later.

**Do the read-only prerequisites in the same pass — they need no SDK knowledge and touch no project file:**

- the repo survey (read-only exploration of conventions, layering, **module format — ESM or CJS, which changes how the SDK is imported and whether `instanceof` on its error classes is trustworthy**, and the runtime: Node, a bundled browser app, or an edge runtime) — capture each convention as *pattern + the ONE exemplar file path to imitate*, NOT inline code snippets: you will read the exemplar at edit time anyway, so a snippet dump gets paid for twice;
- **establish the toolchain before you need it**: the package manager, whether `maxio-advanced-billing` is already a dependency and at what version, the `tsconfig` flags that change what compiles here (`exactOptionalPropertyTypes`, `verbatimModuleSyntax`, `strict`), and the exact commands that run the project's build, type check, lint and tests. Getting this wrong later costs a broken install mid-implementation;
- a baseline run of the project's checks (`tsc --noEmit`, the test runner, the linter — whatever it has) on the UNTOUCHED tree, so later failures are attributable to your changes;
- credentials/environment verification (per the task's secret-handling rules) — **including which host this deployment will actually talk to**, since constructing the client with no options silently selects `ServerEnvironment.Us`, and the other environment is reached only by setting it;
- **a read-only smoke of each in-scope operation against the real credential**, run from a scratch directory outside the project, once the map has given you the signatures and before you finalise the sheet. A plan-, region- or entitlement-gated endpoint answers `403` here — the map presents every operation uniformly and cannot know which ones your credential may call — and learning that now reorders the plan rather than the build. Skip only operations whose side effects you cannot reverse.

<!-- maxio:start -->
For Maxio, two of those bullets mean more:

- **Credentials and host.** The site (subdomain) and the region are configuration too, and both are set
  explicitly. A client built without them calls a site literally named `subdomain`. The construction is in
  `docs/getting-started.md`, "Maxio: site and credentials" (`knowledge/rules.md` R1, R2).
- **The smoke.** Run it against a test site only. Read the site first (`client.sites.readSite()`) and go on
  only when its `test` flag is `true` (R2, `knowledge/go-live.md`). If the only credential you have is for
  a live site, smoke reads only, never a write, and say in your report that writes were not exercised.
<!-- maxio:end -->

Never use the planning phase to get a "head start" on implementation: **creating or editing ANY project file before the gate below is a defect**, no matter how obvious the code seems.

**HARD GATE — no project-file creation or edits until:** `maxio-advanced-billing-plan.md` EXISTS at the repo root, its contract sheet has **no open lookups**, and you have read it. The gate bars coding "meanwhile"; it does not bar the read-only prerequisite work above. Starting to code before the sheet exists defeats the entire plan-first design.

**What the gate does not cover:** installing `maxio-advanced-billing` into the project, installing the toolchain, and the files those writes produce (`node_modules/`, a lockfile the installer updates) are **prerequisites, not project-file edits**. The type check and the smoke need the package installed, and these are the only writes permitted before the gate. Nothing you author by hand may change.

### Step 1b — The tables the contract sheet must carry (fill these in before you write any code)

The per-operation rows describe **what each operation is**. The tables below carry what those rows cannot: a write that may reach the provider twice or whose outcome you may not learn, a rule that spans two operations, and a field nobody asked for. Fill in every one that applies before any code exists.

#### 1b.1 — DURABLE WRITES

One row in each table below per operation in scope that creates, sends or changes something on the provider's side; `none` if the scope has no such write. Every row follows one order: **claim → SDK call → record the result**. The claim is a row of its own, committed to a store this application owns *before* the call — not a field filled in afterwards on the record the write is about — so a second caller is stopped before it reaches the provider, and a lost answer leaves something to settle. A test that reads the store from inside the faked `fetch` shows the claim was there when the request left.

**DUPLICATE CLAIMS** — what stops the same operation reaching the provider twice.

| Write | Where the claim is stored | What rejects the second one | Where that rejection is caught | Where in the code |
| --- | --- | --- | --- | --- |

⚠⚠ **What rejects the second one**: the store refusing the second claim — a unique constraint or a conditional write on a value every caller doing the same operation computes the same (the order being paid, the signup being welcomed), never on a value minted per attempt, which is unique by construction and refuses nothing. A read before the write, an in-process lock, or an assumption that one process runs lets both callers through. Release the claim when the provider refuses the call, so a later attempt is not blocked.

**Where that rejection is caught**: the `catch` for what the store raises on the second claim, recognised by the driver's error code rather than its message; the losing caller then uses the record the winner wrote.

The SDK sends an `Idempotency-Key` minted once per call, and its own retries resend that key — but a second click or a retry of your own is a new call with a new key, so the provider cannot join the two. The key goes beside the claim, never in place of it; where the operation declares its own key, send the reference stored on the claim (see `docs/configuration-resilience.md`).

<!-- maxio:start -->
**For Maxio the paragraph above needs a correction.** Maxio has no `Idempotency-Key` header and ignores
the one this SDK sends, and no operation on the map declares a key. Maxio's duplicate guard is
`uniqueness_token`, a field the spec does not declare, sent at the top level of the body beside the
resource object (`knowledge/rules.md` R12). `docs/models.md`, "Fields the spec does not declare", shows how
to send it with this SDK.

- Mint one token per write (a signup that creates a customer and then a subscription mints two), store
  it on the claim, and send the same token on every resend of that write. Mint a new one only after a
  422 you corrected, or where `knowledge/rules.md` R11 step 4 allows it.
- "The map wins" does not remove this field. No **Fields** table or model shows it, because the spec does
  not declare it. Where Maxio requires it, the operation's Provider rules line names it.
- The token does not replace the claim. It does not stop two requests that arrive at the same moment, and
  Maxio keeps a token for a limited time. The lasting guard is your own record plus a deterministic
  `reference` you can look the write up by.
<!-- maxio:end -->

**UNKNOWN OUTCOMES** — what settles a write the provider may have acted on without your code learning the answer.

| Write | The operation you re-read with | The reference you search by | Where in the code | The test that fails the connection |
| --- | --- | --- | --- | --- |

⚠⚠ A `ConnectionError` or `TimeoutError` on a write is *unknown*, not *failed*: the provider may already have acted. Reporting a failure is not a legal entry, and neither is leaving the caller to check or retry. Settle it in that write's own `catch`: re-read by the reference you sent — found, settle from what the provider holds; not found, or the re-read itself fails, still unknown, never failed. Telling the caller the outcome is unknown comes after the re-read, never instead of it. If the provider offers no way to find the write, that is a **Blocker** in Assumptions & Blockers, not a row.

A write that never left has nothing to re-read — a credential that could not be obtained (`AuthError`) or a value that would not encode (`EncodeError`) — and must reach a different outcome. Re-reading after every error is not the safe default: "any error might mean it went through" is false for a request that never left, so a refused credential gets its own outcome and no re-read. **The test that fails the connection** asserts the re-read request was made; a second test, a never-sent failure on the same write, asserts it was not.

<!-- maxio:start -->
**Maxio widens "unknown".** Besides a `ConnectionError` and a `TimeoutError`, a write's outcome is unknown
after a 5xx, a 408, a 409, a 2xx whose body would not decode (a `DecodeError` with a 2xx `status`), and an
abort of your own `signal` once the request has left. Maxio works on a request for up to 120 seconds, so
"not found" on the first read-back does not mean the write failed. `knowledge/rules.md` R11 gives the
order: read back; if it is not there, wait until 120 seconds have passed since the first send and read
again; then resend with the **same** `uniqueness_token`. A write that cannot carry a token is never resent
automatically, and after a 409 a write starts again with a new token only where R11 step 4 allows it.
Never report an unknown outcome as a failure, and never mint a new token for a resend.

`recipes/safe-signup.ts` implements this for a signup. The SDK settings it needs (no automatic resend, an
attempt that outlasts 120 seconds) are in `docs/configuration-resilience.md`, "Maxio: retries, timeouts and
paging", and the code that tells a rejection from an unknown outcome is in `docs/error-handling.md`,
"Maxio: reading a rejection".
<!-- maxio:end -->

Write `TBD` in **Where in the code** and **The test that fails the connection** while you plan — every row. Once the code compiles, replace each `TBD` individually: the claim write, then the SDK call it precedes; the `catch`, then the re-read it makes. ⚠⚠ A `TBD` left behind, a name that is not in the code, or one note covering several rows is **not addressed**; if the code does not do what the row says, fix the code, then the cell.

#### 1b.2 — CROSS-OPERATION INVARIANTS

**CROSS-OPERATION INVARIANTS** — copy this header into the contract sheet and add one row per value a caller supplies (an identifier, a code, a reference) whose legal set something other than that call defines: a list the provider returns, or records this application keeps. `none` if the task restricts no such value. ⚠⚠ The map never states these rules; derive them from the task.

| Invariant | Where the legal set comes from | Enforced where | The test that proves it |
| --- | --- | --- | --- |

<!-- maxio:start -->
Seed this table from the `knowledge/lifecycles.md` items you read and the *Before you call* lines of each
in-scope operation's notes. Maxio's ordering rules are invariants too: a customer before its subscription,
and a collection method chosen and sent explicitly on every signup (`knowledge/rules.md` R14,
`knowledge/decisions.md` D3).
<!-- maxio:end -->

⚠⚠ **The legal set is the one this task offers, not everything the account holds.** Asking the provider whether a value exists is not this check: the provider already rejects what exists nowhere, so a lookup of one record by its id enforces nothing new — internal records, test records and records meant for something else all exist, and all pass it. Check membership of the offered set itself, read in full (every page). If neither the provider nor this application can name that set, that is a **Blocker** in Assumptions & Blockers, not a row.

The check runs before the write is attempted and before its **DUPLICATE CLAIMS** claim is inserted — a value rejected after the claim exists leaves the claim behind to block a later, legitimate attempt. **The test that proves it** asserts a value outside the set is rejected **and** the write is never called.

#### 1b.3 — OPTIONAL REQUEST FIELDS

For every write operation in scope, the contract sheet carries an **OPTIONAL FIELDS** table: one row per optional field on the request, and what **requires** it.

| Field | What requires it | Set it? |
| --- | --- | --- |
| `{optionalField}` | nothing | ❌ leave it out |
| `{optionalField}` | the words in the task that supply it | ✅ set it from those words |
| `{optionalField}` | a named row of this sheet — e.g. the idempotency key a DUPLICATE CLAIMS row sends, or the reference an UNKNOWN OUTCOMES row searches by | ✅ set it, and name that row here |

<!-- maxio:start -->
Maxio adds a fourth thing that requires a field. Put this row in the table too:

| Field | What requires it | Set it? |
| --- | --- | --- |
| `{optionalField}` | a provider rule: the operation's **Provider rules (Maxio)** line on the map, or a rule in `knowledge/` | ✅ set it, and cite the rule id here |

`payment_collection_method` on a signup is the usual case: optional in the type, required by R14.

A field Maxio needs but the spec does not declare gets a row as well, although the request type does not
list it. `uniqueness_token` is the one that matters: R12 and the DUPLICATE CLAIMS row require it on every
write that may be resent. Because it has a row, the test at the end of this section must not flag it. That
test asserts the opposite: the key is there, at the top level of the body.
<!-- maxio:end -->

⚠⚠ **A field nothing requires is not yours to choose.** "Something requires it" means the task's own words, a provider rule or a row of this sheet, never your own sense that it looks sensible. Leaving it out *is* the decision: the provider's own default then applies, whether that is the account's configuration or the API's documented behaviour, and neither is yours to replace with a value you invented.

⚠⚠ **This rule never removes a field another row requires.** An idempotency key, and the reference you look an unknown outcome up by, are required by the DUPLICATE CLAIMS and UNKNOWN OUTCOMES rows rather than by the task — the task will never mention either. Dropping one to satisfy this table is a defect, not compliance. And because a header, a query parameter and a body field all look alike on this SDK's flat request object, "it is only a header" is not a reason to leave a field off the table.

⚠⚠ **The map does not state defaults, and its silence is not permission to pick one.** A member typed `field?: T` tells you the field may be omitted. It tells you nothing about what omitting it does. If you cannot state what the provider will apply when the field is absent, that is a reason to leave it absent, not a reason to fill it.

**The test that proves it:** assert the request the SDK sent carries **no key your own code set without a row that requires it** — headers and query parameters included, not only the body. The SDK adds its own (authorization, content type, its defaults); those are not yours and need no row. A test that only checks the fields you meant to send cannot see an invented one.

#### 1b.4 — WHEN THE API SAYS NO

Add one table per operation that uses the caller's data — what they typed, IDs they supply, and data your app stores for them (their email, their name). An empty request body does not make a refusal yours: when the API refuses the data you sent for them, only its reason tells them what to change. An operation with no typed arms still gets one.

| status | your app answers | the caller reads | test |
| --- | --- | --- | --- |
| a `4xx` other than 401 / 403 / 429, and not one of the Maxio rows below | the same `4xx` | the API's reason text from `err.payload` | fake it with a reason; assert the reason is in your response |
| 401 / 403 | 502 | a fixed message — our credentials | fake a 401; assert 502 and the fixed message |
| 429 | 503 | a fixed message — our quota | — |
| 5xx | 502 | a fixed message | — |
| no response, on a write | per UNKNOWN OUTCOMES | unknown — never "failed" | — |
| no response, on a read | 502 | a fixed message | — |

Logging the reason is not returning it: log it **and** put it in the response.

<!-- maxio:start -->
Maxio adds these rows, and where one applies it replaces the generic row above. Read the operation's
**When it fails** table in its notes section before you fill any row (`knowledge/rules.md` R13).

| status | your app answers | the caller reads | test |
| --- | --- | --- | --- |
| 408, 409 or 5xx, on a write | per UNKNOWN OUTCOMES | unknown, never "failed" | fake a 409; assert the read-back request was made |
| 422 carrying an `action_link` | your own "authentication needed" answer | the link, so the customer can complete 3-D Secure | fake it; assert the link is in your response |
| 422 that is an account block | 502 | a fixed message | fake it; assert Maxio's text is not in your response |

A 409 on a write is never relayed as "the same `4xx`". It means Maxio received a request with that
`uniqueness_token` and its outcome is unknown, so it is settled by a read-back (R12,
`knowledge/lifecycles.md` L2). A 404 on a lookup by your own reference is not a failure at all: it is the
normal "not there" answer. `docs/error-handling.md`, "Maxio: reading a rejection", has the code that reads
the status and Maxio's message, and `docs/models.md`, "Fields the spec does not declare", the code that
reads `action_link`.
<!-- maxio:end -->

### Step 1c — Required reading (do this before you write any code)

End the contract sheet with a **REQUIRED READING** block whose rows carry inline `MUST read <doc>` pointers. **Read every doc in `docs/` the sheet names, now, before you start implementing** — not lazily at the step that needs it. The sheet deliberately does *not* carry the how-to: it names the hazard and hands you the doc that resolves it, so an unread pointer is a gap in what you know, not a formality.

This step is the one place that decides when the companion pages are read. `docs/getting-started.md`
says what each page is for and defers to this step. A row may name one section of a page instead of the
page. Then read that section.

**A fixed floor applies regardless of what the sheet says** — the sheet can add to it, never remove from it: `docs/error-handling.md` always (every integration writes an error boundary, and this SDK's one error family is narrowed on its closed `kind`, with four throwables outside it that a family test has to rethrow); `docs/client-initialization.md` before the client is constructed; `docs/testing.md` before the first test file you create or edit, *including* a throwaway verification script that fakes `fetch`. A sheet row that excuses one of these ("out of scope", "no test suite requested") is not a substitute for reading it.

These are API-agnostic usage docs; reading them is not a substitute for the lookup layer, and reading a file in the installed package does not remove the need to read the doc for that step. Contract *facts* still come only from your sheet or a fresh lookup.

Before implementing, check the plan's **Assumptions & Blockers** section:

- Blocker or major assumption → surface it to the user in plain language, get their answer, and revise `maxio-advanced-billing-plan.md` in place.
- Minor assumptions only → proceed.

Full re-planning only on genuine scope change; for a single missing fact mid-implementation, do the lookup, never guess.

### Step 2 — Implement from the contract sheet

1. Read `maxio-advanced-billing-plan.md` once. Treat its contracts as authoritative — do not re-derive or "double-check" them from memory. When a lookup revises a row, update the file so the sheet and the code never disagree.
2. **Decide which environment this deployment talks to, explicitly, before the first call.** Constructing the client with no options selects `ServerEnvironment.Us` **silently**, so an unset field is indistinguishable from a deliberate choice of the default. Bind it to configuration and fail startup if the (environment, credential) pair is not the one this deployment intends — a credential pointed at the wrong host is not a defect any call site can correct.
3. **Build the client once and hold it.** Resources are memoized lazy getters on it, so rebuilding one per request throws that state away. There is no `close()` — it owns a `fetch`, not a pool.
4. **Pick the response mode per call, deliberately.** Every operation returns `ApiPromise<T, E>`: `await` it and an error status rejects, or call `.asApiResult()` **on the value the operation returned** for the non-throwing `ApiResult<T, E>` — the only way to see the status and headers of a *success*, and therefore the only way to observe anything at all from the **32 operations that resolve to `undefined`** (every operation whose success declares no body — the map's **Returns** bullet names them). `ApiPromise` overrides `Symbol.species`, so `.then()`/`.catch()`/`.finally()` hand back a plain `Promise` with the method gone — the mode is chosen at write time, never retrofitted.
5. Implement sequentially, following the repo's own conventions and layering. You read the companion docs the sheet named in Step 1c — implement each step in line with the one that governs it. Take every contract *fact* (signatures, field names, channels, error arms, enum members) from the contract sheet or a fresh lookup — never re-derive one from a companion.
6. After every change: run the project's **type checker** (`tsc --noEmit`) as well as its tests. The package ships its own types and is generated under strict TypeScript, so a type error against it is a real contract violation, not noise — it is the compile-time backstop the whole map-first discipline leans on. **Treat a clean type check as the gate you do not skip.** If the project has no type check configured, run `tsc --noEmit` over the files you touched; if you genuinely cannot, say so in your final report rather than silently substituting a smoke run. Fix non-SDK errors yourself.
7. **Any error involving an SDK type or member** — `TS2339` (property does not exist), `TS2345`/`TS2322` (argument or assignment mismatch), `TS2551` (did you mean), `TS2307` (cannot find module — usually a deep import), `TS2739`/`TS2741` (missing required members), or an unexpected rejection at runtime — → go back to `docs/getting-started.md`'s map section and file table, and read the one page or file that owns the fact. Do not attempt more than one self-fix of an SDK-name error before doing that lookup: rewriting from the same knowledge that produced the error is guessing. Remember which failures are **not** `ApiError`: a malformed body is `DecodeError`, a value that would not encode `EncodeError`, a dropped connection `ConnectionError`, an attempt's timeout `TimeoutError` (both only after any retries are spent), a credential that could not be **obtained** `AuthError` — every one of them in the `MaxioAdvancedBillingError` family, told apart by `err.kind` — and an unknown `serverEnvironment` throws `ConfigurationError` out of the client constructor, before any call exists. So an exception that does not look like an API error may still be one of the SDK's failure kinds.
8. Once the code is complete, open each member the **DUPLICATE CLAIMS** and **UNKNOWN OUTCOMES** rows name and confirm it runs when that write runs. Where the code falls short of a row, fix the code, not the row.
9. **Observability and sensitive data.** Logging is **off by default** and is configured through `ClientOptions.logging`: say whether the integration turns it on, at what level, and which correlation id from the provider's error bodies reaches your own logs. A JSON request body is logged **verbatim** when `logRequestBody` is on, and a form body is masked only by deny-list, so a key you have not listed prints in the clear. If the scope carries data you would not want in a log — each request model's declaring file lists every field in scope — `logRequestBody` stays off, no call on those paths passes a per-call level, which turns the body on, **and** `ClientOptions.logging.level` is set explicitly, so the `MAXIO_ADVANCED_BILLING_CLIENT_LOG` environment variable cannot switch logging on from outside the code (see `docs/getting-started.md`).
10. Run the project's tests; verify the integration end to end the way the task demands. Retrying is **on by default**, so if the task needs a different policy, tune it through `ClientOptions.retry` rather than wrapping the call. The SDK has no hooks or middleware, so anything the task needs there is yours to build on the `ClientOptions.fetch` seam or to deliberately omit — say which you did for both.

<!-- maxio:start -->
For Maxio, three of the steps above carry more:

- **Step 2, item 2.** The site is part of the host. Set the site and the region from configuration and fail
  startup when either is missing: `docs/getting-started.md`, "Maxio: site and credentials".
- **Step 2, item 10.** The retry defaults do not fit Maxio's writes, and the SDK's `Idempotency-Key` does
  nothing here: `docs/configuration-resilience.md`, "Maxio: retries, timeouts and paging". Paging and the
  request limit are recipes to copy, not code to write.
- **Before you report.** Go through `knowledge/go-live.md` once, and do the pin step from the plan unless
  the user declined it.
<!-- maxio:end -->

### Step 3 — Answering pure questions

A standalone Maxio Advanced Billing question with no code change: look it up in `docs/getting-started.md` (and the map page or file its table names), then give the grounded answer, citing where it came from. When several questions arrive batched, answer them in one pass. Never answer from memory, even for "easy" questions.

<!-- maxio:start -->
A question about what Maxio requires, not about this SDK's surface, is answered from `knowledge/` the same
way: the operation's notes section, or the one rule, decision or lifecycle item it cites.
<!-- maxio:end -->

## Anti-patterns — never do these

- **Read `docs/getting-started.md` before any lookup.** It is your lookup layer, not optional background. (The companion docs in `docs/` are the complement: read the ones the sheet names, per Step 1c.) Don't re-derive a contract *fact* from a companion — exact signatures, request fields, channels, error arms and enum members come from the sheet or a fresh lookup.
- **Never write any Maxio Advanced Billing or SDK fact from memory** — every signature, field name, wire header, enum member, and error arm in your code must come from the contract sheet or a lookup. And **never write a call from memory "to fix later".**
- **Never switch on an error arm tag across operations.** A tag is derived from the arm's **body schema**, never from its status: an arm whose body is a direct model reference is named after that model in lower camel (`"validationError"`), and every other body — a primitive, an array, a map, or no content — is named `"error{Status}"` (`"error400"`, `"error4XX"`, `"errorDefault"`), with a numeric suffix on the second of two arms that would otherwise land on the same name. Tags are resolved **per operation**, so the same tag covers different statuses on different operations — a shared handler keyed on `err.payload.kind` is a bug. Read the status from `err.status`, and narrow on `kind` only against the arm table of that one operation.
- **Don't web-search Maxio Advanced Billing topics to find an implementation detail** — the installed package's own map and source are the ground truth, and the file table tells you where to look. Public Maxio Advanced Billing docs describe the HTTP API, not this SDK's generated surface, and the two disagree on names, on which fields are required, and on what the SDK sends by default.
- **Never introspect the SDK at run time to discover its shape.** `Object.keys`, logging a client instance, or a REPL poke is the TypeScript-flavoured version of decompiling the package: it answers what exists, never what is *supported*, and it invites `#`-private fields and unexported engine types into your code. Read the map, then the file it names.
- **Don't grep the package to *locate* a type** — the SDK map is the locator (and says so: *"Do not derive the path from the type name"*); grep only *inside* the file its **Type sources** table names, for the symbol. A sweep for a *shape* is a different thing, and is fine: "every field typed `unknown`", "every required-nullable member" are cross-cutting questions nothing indexes, and one targeted `grep -rn` over `src/models/` is the right tool for them — record what it found on the sheet.
- **Don't deep-import from the package** (`maxio-advanced-billing/models/…`). The package root is the only entry and deep specifiers do not resolve; the map's `Source` paths are for reading, not importing.
- **Don't import `Event` unaliased.** This SDK exports a type named after a TypeScript/DOM global, so importing it plain shadows the global for the whole file. Alias on import from `maxio-advanced-billing`.
- **Don't vendor the SDK's `src/` into the project, point `tsconfig` `paths` at a throwaway clone, or import from `dist/` directly** to make a lookup possible. Install it properly (see `docs/getting-started.md`); a clone-based shortcut breaks every import the moment the clone is deleted, and it does not put the map where the lookups expect it.
- **Don't create or edit project files before the HARD GATE** in Step 1 — plan and contract sheet first, code second.

