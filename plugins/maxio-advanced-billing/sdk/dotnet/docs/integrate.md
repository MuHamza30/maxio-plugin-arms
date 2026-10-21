# Maxio Advanced Billing .NET SDK — Workflow (map + docs)

**Read when:** you are asked to add or change Maxio Advanced Billing code in a C#/.NET project, or a Maxio Advanced Billing .NET SDK call errors or behaves unexpectedly. The order is: `AGENTS.md` in this SDK folder, then this page, then what this page names. Read it before you open the SDK map or touch any project file. It sets four binding rules: (1) for implementation work, the plan file `maxio-advanced-billing-plan.md` is written at the project repo root BEFORE any project file is created or edited; (2) `docs/getting-started.md` and the SDK map it describes are read and used for every contract fact, never memory; (3) every doc under `docs/` that the contract sheet's REQUIRED READING names is read before implementation starts; (4) every sheet row carries one of three labels: a map page, `UNVERIFIED`, or `YOUR CALL — not in the map`. Skip it and SDK facts get written from stale memory.

Your scope here is **C#/.NET only**: if a request concerns any other language or SDK, say so and stop. Your source of truth is the **SDK map that ships in this SDK folder** (`sdk-map.md` plus its `map/operations/` pages; model, enum and error shapes live in the source files those pages name), read as `docs/getting-started.md` says, plus the companion docs under `docs/` for usage traps. Your training data on this SDK is stale: every fact you write down must come from a map page or a map-named source file you actually read this session. You never guess. The SDK's `api-reference.md` is about 550 KB: search it for one operation when you need the spec's own description of it, and never read it whole.

**Scope guard:** the APIMatic-generated Maxio Advanced Billing **.NET SDK** (root namespace `MaxioAdvancedBilling`) in **C#/.NET projects only**. Unrelated API, or any language other than C#/.NET — do nothing; this doc does not apply.

## Grounding rules

- **Map for contracts; the map-named file for shapes.** Follow `docs/getting-started.md`'s *SDK map* and *SDK source* sections in full — they define how to obtain the source (the map lives inside it), that reading a model/enum/error shape means opening the one declaring file the map names (routine, scoped), and why locating anything by grep/glob/`find` over the tree is a defect rather than a shortcut. The source stays in this SDK folder, and `maxio-advanced-billing-plan.md` cites it by paths relative to this SDK folder — those paths stay valid for anyone who has this SDK folder.
- **Never grep, glob or `find` the SDK tree to locate something** — the map is the locator, and a type name is its path. Every lookup starts at the map index and ends on the one page (or the one source file) it names.
- **Your contract sheet never leaves a contract fact open for "later."** The map pages and the files they name answer nearly everything — resolve them during planning, not mid-implementation. For the rare in-scope fact even the source cannot settle: if only live traffic could confirm it, convert it into a concrete defensive-coding directive on the sheet and label the uncertainty `UNVERIFIED`. Never leave a row marked for a later source lookup: an open row is how you end up opening source mid-implementation.
- **When you judge how far a contract can be trusted**, the trust judgment may cite ONLY evidence visible in the map or SDK source (e.g. two generated definitions that disagree, a suspicious shared model) — never training-data memory of this API, and never claims about what the live wire "usually" sends.
- **The sheet records Maxio Advanced Billing's call surface; the application's design is decided at implementation time.** Its persistence, its concurrency rules, and the request contract its own callers must satisfy are not SDK facts. Where an SDK fact forces an application decision, record the fact and its consequence on the sheet, mark the decision `YOUR CALL — not in the map`, and decide it at implementation time against the task.
- **Name only what you have read.** Never name a claim, header or route of the application as though you knew it exists — unless you have read that code. Name configuration by its binding key, never by a raw environment variable, and give the default the map documents where there is one: a setting you invent a name for is a setting no deployment will supply.

<!-- maxio:start -->
## Provider knowledge: Maxio's business rules

The map gives you Maxio Advanced Billing's call surface. It cannot give you Maxio's business rules: what
must exist before a call succeeds, which of two overlapping operations to use, which values silently do
nothing, and what each rejection means. Those ship in this SDK folder under `knowledge/`. Never answer a
business-rule question from memory.

Read the part your task touches, at the point it is needed. Do not read `knowledge/rules.md` or an
operation's notes file from top to bottom.

| When | Read | How much |
| --- | --- | --- |
| Before the plan | The ten rules | Once. They are in `AGENTS.md`, which you have already read. A rule id on a line you act on (`R12`) is one heading in `knowledge/rules.md`: open that rule only |
| For each operation in scope, while you fill its contract-sheet row | The first bullet of its map block, then the notes section that bullet links | **Provider rules (Maxio)**: Maxio has rules that change what you send. **Provider notes (Maxio)**: notes only. Neither: Maxio published nothing, so write `no provider notes`. The link ends in `#` and the section's heading: read that one section (**Always**, **Before you call**, **Rules**, **When it fails**), not the file |
| While you order the steps | The sections of `knowledge/lifecycles.md` (L1 to L9) and `knowledge/decisions.md` (D1 to D20) that those lines cite or the flow needs | Each file opens with a contents list. Where a choice depends on the user's intent and the task does not say, ask |
| When the task needs something the SDK does not do for you | `recipes/README.md`, then the one recipe you copy | Paging a list to its end, a safe signup, subscription-state checks, webhook verification, a request limit. Copy and adapt. Do not write your own |
| When Maxio rejects a call | `knowledge/failures.md` | Search it for the status and a distinctive part of the message. Read the row before you change code |
| When the code is complete, before you report | `knowledge/go-live.md` | Once. Its checks go in **GO-LIVE CHECKS** (Step 3) |

The plan format in Step 1 says, at each section, what Maxio adds to it.

`docs/error-handling.md`, "Maxio: reading a rejection", shows how to print the status and Maxio's message
for that lookup. A 4xx is never evidence that a call works. A 409 on a write is not a rejection to
hand your caller as a 4xx: the first copy of the request arrived and its outcome is unknown, so settle it
by reading the resource back (R12, `knowledge/lifecycles.md` L2).

**Test site only.** Any call this work sends to Maxio, a probe or a test, goes to a test site. Prove it
first: `client.Sites.ReadSite()` must return `Site.Test == true` before any write (R2,
`knowledge/go-live.md`). Never send a write to a site you have not checked.

**The project block.** `knowledge/AGENTS.block.md` holds the ten rules as a block for the project's own
`AGENTS.md`. Adding it is the user's decision: `AGENTS.md` in the SDK folder, section *The project block*,
says when to add it and when only to mention it in your report.
<!-- maxio:end -->

## Workflow

**If the user opens with a reported SDK error or unexpected Maxio Advanced Billing behaviour** (not new feature work), go straight to *Step 4 — Fixing SDK errors* below — do not run the plan-first flow for a bug report. Otherwise, for implementation work:

### Step 1 — Plan first: write `maxio-advanced-billing-plan.md` (always, for any implementation work)

Your FIRST deliverable is `maxio-advanced-billing-plan.md` at `<project repo root>/maxio-advanced-billing-plan.md` — that exact path, always; never pick another location. It carries the plan and the contract sheet in the format below, and it is the only project-repo file you write before the HARD GATE further down.

#### How to ground (map-first, one pass)

1. Read `docs/getting-started.md`; open `sdk-map.md` (the index).
2. From the index, open the **operations pages** for every controller in scope — take signatures (the request record each operation takes, and its required members), return types, error case (A: typed `ApiException<{Operation}Error>` with its `TryGet…` accessors and payload type / B: `ApiException<RawError>`), and pagination — remembering that a block silent on a defaults-table point means the default applies. Where an operation's *semantics* decide what you must pass, that prose is the method's XML `<remarks>` in the `Api/` file the page names, and the per-member docs on its request record: read it there.
3. Open, scoped, the **declaring source file** for every request/response model you will reference — the operation's **Type sources** table names it — and take field names WITH their `[JsonPropertyName]` wire names, `required` flags, nullability, and the envelope shape. Enum value lists and union accessors come from their declaring files the same way.
4. Identify which companion doc governs each step in scope. For each, write the trap note as a **named hazard plus a `MUST read` pointer** — *not* as the resolved answer. Naming the hazard ("what `Timeout` actually bounds") is right; resolving it inline ("`Timeout` is per-attempt") is wrong — a resolved trap gives you no reason to read the doc, and the doc carries the parts a one-line note cannot. **Never restate a companion doc's default or semantics in a trap note — not even when you believe it correct.** Write the *consequence*, not the answer. Contract *facts* are the opposite: those you resolve fully and inline.
5. Collect everything in ONE pass — the whole point is that you never have to rediscover a contract mid-coding.

#### Prerequisites you can run alongside

These need no SDK knowledge and touch no project file, so do them before or alongside the map work:

- reaching the SDK source (per `docs/getting-started.md` — the map lives inside it, so this comes before any map work);
- the repo survey (read-only exploration of conventions and layering) — record each convention as *pattern + the ONE exemplar file path to imitate*, NOT inline code snippets: you will read the exemplar at edit time anyway, so a snippet dump gets paid for twice;
- `dotnet restore` and a baseline `dotnet build` / `dotnet test` of the UNTOUCHED solution, so later failures are attributable to your changes;
- locating the SDK reference and its version in the project;
- credentials/environment verification (per the task's secret-handling rules).

Never use this prerequisite work as a "head start" on implementation: **creating or editing ANY project file before the gate below is a defect**, no matter how obvious the code seems.

#### HARD GATE

**No project-file creation or edits until `maxio-advanced-billing-plan.md` exists at that path with every section below filled in.** Starting to code before the sheet exists defeats the plan-first design: the sheet is what keeps SDK facts out of your memory and in the map. The gate bars coding before the sheet exists; it does not bar the read-only prerequisite work above.

<!-- maxio:start -->
**GO-LIVE CHECKS** is the one section the gate does not cover. It is written in Step 3, when the code is
complete.
<!-- maxio:end -->

#### The `maxio-advanced-billing-plan.md` format (keep it tight — tables, not prose)

1. **Scope & sequence** — the implementation steps in order, each naming the operations it uses. A capability the map lacks is a Blocker (§6), never a data path you invent to replace it.
2. **CONTRACT SHEET** — open the section with two literal warning lines: that signatures are generated code, verbatim — each operation that takes input takes ONE request record as its first parameter (an operation with no inputs takes none), built with an object initializer whose property names are the record's own, never flat arguments; and that every SDK type is written fully-qualified with the namespace its source path implies, taken from the path the map gives for THAT type, never from where a neighbouring type sits. Then one table row per operation: controller property · method signature · request record + its members (`Name: type, required?`) · body model + its fields (`Name (wire_name): type, required?`) · response envelope + the inner fields the integration reads · error case A/B + accessors + payload type · pagination · **source** (§7). Below it: the enum value tables actually needed, and the client construction/auth/server-node facts. ⚠ A request model may mark nothing required, and then `required?` selects nothing for you — carry the optional fields the endpoint's own prose ties to whether the call is accepted, and say which doc-named fields you left out.

<!-- maxio:start -->
**What Maxio adds to sections 1 and 2.**

- **Scope & sequence** includes every *Before you call* precondition of an in-scope operation as a step.
- Each operation row carries a **Provider notes** cell: the notes link from the map, or `no provider notes`.
  Copy the **Provider rules** line into the row as directives.
- **A provider rule can require a field.** A field named by a Provider rules line, or by a rule in
  `knowledge/`, is required for this task even where its model marks it optional. Put it on the row, set it,
  and cite the rule id. `payment_collection_method` on a signup is one (R14).
- **A field Maxio needs and the spec does not declare goes on the row too.** `uniqueness_token` is on no
  request record and no body model, so the map's contract does not show it. The row of every write you may
  resend lists it, with `knowledge/rules.md R12` as its source. `docs/models.md`, "Fields the spec does not
  declare", says how to send it.
- A row, or a line of a row, whose source is a rule id or a notes section is grounded. Cite that source.
  For Maxio's rules it is a fourth source beside the three labels of section 7: such a line is neither
  `UNVERIFIED` nor `YOUR CALL — not in the map`.
- A provider rule outranks your memory of this API and any default you would otherwise pick. Where a rule
  and the SDK disagree on a contract fact (a name, a type), the map wins; record the conflict. "The map
  wins" settles names and types. It does not remove a field the map lacks: `uniqueness_token` is still sent.
<!-- maxio:end -->

The CONTRACT SHEET also carries a **CROSS-OPERATION INVARIANTS** table, directly below its per-operation rows: the rules no single row can state, because they relate two operations. One row per value the task lets a caller supply where a *different* operation defines the legal set for it (identifiers, handles, codes, references); `none` if the task has no such value — never leave the table out.

| Invariant | Operations | Enforced where |
| --- | --- | --- |
| a value accepted by X must be one Y returned | `{WriteOperation}` ← `{ListOperation}` | before `{WriteOperation}` is called |

⚠⚠ The map never states these rules; derive them from the task.

<!-- maxio:start -->
For Maxio, start from the sections of `knowledge/lifecycles.md` the flow needs and the *Before you call*
lines of each in-scope operation's notes section. Then derive the rest from the task.
<!-- maxio:end -->

⚠⚠ **Operations** names the operation that *defines* the legal set: the list or search call that returns what this application offers, or the earlier call whose result this application stored. A lookup that confirms a single value exists is not an answer: it proves the value exists at the provider, not that it is one this application offers.

**Enforced where** names the member that checks, before the write, that the caller's value is in that set. If the application never reads that set, say so there and add the read — the check is part of the work. `YOUR CALL — not in the map` is not a legal entry in any cell of this table.

3. **Trap notes** — one line per hazard, attached to the step where it bites, each ending in an inline **`MUST read <doc>`** pointer. Name the hazard and its consequence; do not resolve it. ⚠⚠ **"Do not resolve it" is the load-bearing half of this rule.** A trap note that answers its own question hands you a usable one-liner — and holding one, you do not open the doc. You implement from the sentence, and everything the doc carries beyond it never reaches the code. So: state the hazard, state what it costs, hand over the doc, and stop. No fix, no snippet, not even a partial answer. A trap note from which you could write correct code without reading the named doc is a defect.
4. **REQUIRED READING** — close the sheet with the de-duplicated list of every doc under `docs/` named above, one line each: doc · the step it governs. Write each as its path in this SDK folder. State that these are to be read **before implementation starts**, and that the sheet deliberately does not carry their contents. This block is mandatory even when the trap notes are few — an integration always writes an error boundary, so `docs/error-handling.md` always appears here. Always include, verbatim, this hazard row: a body that does not match its declared type — a drifted or malformed **2xx** response (a missing `required` member) or a **non-2xx** body that does not match its operation's generated `{Operation}Error` shape — surfaces as `ResponseDeserializationException`, an `ApiException` that keeps the HTTP status and names the target type but is **not** an `ApiException<TError>`; a catch ladder that handles only `ApiException<TError>` lets it escape, so it must also catch `ResponseDeserializationException` (or `ApiException`).
5. **PRODUCTION READINESS** — the fixed table below, every row carrying a *decision*. Naming a doc in REQUIRED READING does not address a concern; it defers it. `N/A` is a legitimate answer where it is genuinely true, but it must carry its reason.
6. **Assumptions & Blockers** — anything you had to assume about the user's intent, and anything that blocks planning. An empty section is a valid outcome; an invented fact is not. If you expect the provider to reject a call the plan makes, that is a **Blocker**.
7. Every row's **source** cell cites its map page or the map-named declaring file, so a later lookup is one targeted open, not a search. A row with neither to cite is not a contract fact: write `YOUR CALL — not in the map` there instead. Three labels, one order — a fact the map settles cites that page or file; a fact only live traffic can settle is `UNVERIFIED`; a decision about the application is `YOUR CALL — not in the map`. Something that stops you planning goes in §6.

| # | Concern | The decision the plan must record |
| --- | --- | --- |
| 1 | **Credential fail-fast** | Where credentials are bound, and that the host refuses to start when one is missing or blank — rather than discovering it as a 401 on the first call in production. A multi-part credential needs **every** part checked, because a blank part is not a missing one. |
| 2 | **Secret sourcing & rotation** | Where the secret comes from, and that the DI registration builds the options object **once at registration** and captures it in the singleton — so a rotated secret does not take effect until the process restarts. If rotation without a restart is required, say how. |
| 3 | **Total timeout budget** | The number the caller actually gets, not the knob. `Timeout` is **per attempt**, so a hung retryable call costs a multiple of it. State the budget and where it is enforced — a `CancellationToken` deadline is the only thing that bounds a whole call. |
| 4 | **Write-retry ownership** | Which of the scope's writes the SDK may resend and which it may not. The default `HttpMethodsToRetry` covers `GET, HEAD, PUT, OPTIONS`, so `POST`/`PATCH`/`DELETE` are never resent by the SDK — and `PUT` **is**. |
| 5 | **Idempotency & ambiguous writes** | For each write in scope: the key it uses, where that key is kept, and that a resend carries the same one. For this API the key is on no request record and no model: see *Maxio: what these rows must record* below the table. The generator-injected `Idempotency-Key` header (`Guid.NewGuid()`, fresh on every call) is **not** a key and must not be cited as one. Record the reconciliation path (row 11) beside the key, never in place of it. |
| 6 | **Observability** | What is logged at which level, that **JSON request bodies are logged unredacted** when `LogRequestBody` is on, and which correlation id from the provider's error bodies reaches your own logs. |
| 7 | **Sensitive data** | Whether the scope carries data you would not want in a log — each request model's declaring file lists every field in scope. If it does: `LogRequestBody` stays off **and** `LoggerFactory` is assigned explicitly, so the SDK's log environment variable cannot switch it on from outside the code (see `docs/getting-started.md`). Form bodies are masked only by deny-list, so a key you have not listed prints in the clear. |
| 8 | **Environment selection** | Which base URLs each deployment talks to. Enumerate the server groups and environment members from the map's *Servers & auth* section — there may be more than one group, and each operation resolves through its own. State which groups the scope touches and what each deployment sets; if the SDK declares no sandbox environment, say how test traffic is kept away from the live system. |
| 9 | **Duplicate prevention under concurrency** | For each write a caller can trigger twice: its row in **DUPLICATE CLAIMS** below. If this codebase has nowhere to keep a claim that outlives the process, that is a Blocker in §6, not a row. |
| 10 | **Partial results** | For each paged read that can stop at a cap: the field or return type that tells the caller the result was cut short. |
| 11 | **Unknown outcomes** | For each write whose connection can fail after the provider may have acted: how the code settles the outcome instead of reporting a failure. |

A reviewer grades that table alone: each row either records a decision or records why it does not apply. A row that points at a doc, restates the concern, or sits blank is **not addressed**. Rows 5, 7, 8, 9 and 11 are the ones where "not addressed" costs something that cannot be recovered afterwards — a duplicate charge or duplicate write, sensitive data in a log, or test traffic sent to a live system.

<!-- maxio:start -->
**Maxio: what these rows must record.** The how for rows 3, 4, 10 and 11 is in
`docs/configuration-resilience.md`, "Maxio: retries, timeouts and paging".

- **Row 1.** Three values, not one: the API key, the site and the region. A missing site raises no error.
  It sends every call to a site named `subdomain` (R2; `docs/getting-started.md`, "Maxio: site and
  credentials").
- **Row 3.** Two budgets, not one. Reads: a deadline you choose. Writes: at least 120 s per request,
  because Maxio works on a request for up to 120 s (R11). A shorter deadline on a write does not stop the
  write. It turns its outcome into an unknown one. Name the token each write runs under, and say that it
  is not the web request's own cancellation token.
- **Row 4.** The SDK resends `PUT` by default, and some of Maxio's `PUT`s take a payment or count against
  a cap (R11 names them). Record that `PUT` is out of `HttpMethodsToRetry`, or which no-retry client these
  calls go through, and that 429 is out of `StatusCodesToRetry` (R10).
- **Row 5.** Maxio's key is `uniqueness_token`, a top-level body field the spec does not declare (R12).
  One per write: mint it once for that write, keep it with your own record of the write, and send the
  same value on every resend of it. A signup that creates a customer and then a subscription mints two.
  Mint a new one only after a 422 you corrected, or where `knowledge/rules.md` R11 step 4 allows it. "None
  exists" is not an answer for a Maxio write that has a body. `docs/models.md`, "Fields the spec does not
  declare", says how to send it and which writes cannot carry it.
- **Row 8.** The SDK declares no sandbox environment: `Us` and `Eu` are both live hosts. Test traffic is
  kept apart by using a test site. Say which configuration is the test site and where `Site.Test` is
  checked before a test writes (R2).
- **Row 10.** No operation in this SDK is paged for you, so every list you read to its end is a row in
  **PAGED READS**. Page until an empty page, never until a short one (R8). `recipes/ListAll.cs` does it.
- **Row 11.** The unknown outcomes are wider than a failed connection: a timeout, a dropped connection, a
  5xx, a 408, a 2xx that cannot be read, a 409, and your own cancellation or deadline firing after the
  request was sent. Each is settled in R11's order: read the resource back; if it is not there, wait
  until 120 s have passed since the first send and read again; then resend with the same
  `uniqueness_token`. A write that cannot carry one is never resent automatically (R11, R12,
  `knowledge/lifecycles.md` L2). For a signup, copy `recipes/SafeSignup.cs`.
<!-- maxio:end -->

**DUPLICATE CLAIMS** — one row per write a caller can trigger twice; `none` if the task has no such write.

| Write | Where the claim is stored | What rejects the second one | Where that rejection is caught | Where in the code |
| --- | --- | --- | --- | --- |

Every row follows one order: **claim → SDK call → record the result**. The claim is a write of its own, made before the SDK call, so a second caller is stopped before it reaches the provider; release it when the provider refuses the call.

⚠⚠ **Where the claim is stored**: a store this application owns — the one the codebase already keeps its records in — never the provider. A provider idempotency key goes beside the claim, never in place of it.

⚠⚠ **What rejects the second one**: the store refusing the second caller's claim, the way this codebase already refuses a duplicate. A conflict on the save *after* the SDK call is too late — both callers have already reached the provider. A read before the write — a status check, a lookup by key — is not a refusal either: it lets both callers through. Pick a refusal the store you run against enforces: a primary key is refused even by in-memory test stores; a unique index may not be.

**Where that rejection is caught**: the `catch` for what the store raises on the second claim — a lookup that returns the earlier result is not a catch.

Write `TBD` in **Where in the code** while you plan — every row. Once the code compiles, replace each `TBD` individually with two members, in order: the claim write, then the SDK call it precedes. Only this column changes after coding starts. ⚠⚠ A `TBD` left behind, a member that is not in the code, or one note covering several rows is **not addressed**; if the code does not do what the row says, fix the code, then the cell.

**PAGED READS** — one row per read that walks pages; `none` if the scope reads no paged list.

| Read | What caps it | How the caller learns the answer was cut short | Where in the code |
| --- | --- | --- | --- |

⚠⚠ A log line is not a legal entry in the third column: whoever reads the result never reads your logs. Name the field or return type that changes. Write `TBD` in **Where in the code** while you plan; once the code compiles, replace it with the member that sets that field or return type. A `TBD` left behind is not addressed.

**UNKNOWN OUTCOMES** — one row per write whose connection can fail after the provider may already have acted; `none` if the scope makes no writes.

| Write | The operation you re-read with | The reference you search by | Where in the code | The test that fails the connection |
| --- | --- | --- | --- | --- |

⚠⚠ Reporting a failure is not a legal entry, and neither is leaving the caller to retry. Settle the outcome in the failing write's own `catch`, before it returns, or record it as unknown for code that settles it later — a report someone reads is not that code. With no reference, the third column names what the match uses; if the provider offers no way to find the write, that is a Blocker in §6, not a row.

**Where in the code**: that `catch`, or the unknown state and the code that settles it — a re-read helper nothing calls is not addressed. **The test that fails the connection** asserts what follows. Both are `TBD` while you plan, replaced once the code compiles. A `TBD` left behind is not addressed.

<!-- maxio:start -->
**GO-LIVE CHECKS**: not part of the gate. Leave this section out while you plan. When the code is complete,
read `knowledge/go-live.md` once and add one row per check that applies to the scope.

| Check | How it was proved against a test site, or `not run` and why |
| --- | --- |

The first column is the check's id (`G3`) and its subject. "I believe it works" is not a legal entry in the
second.
<!-- maxio:end -->

Keep the file lean: no copied map pages, no full model dumps, and no path beyond those relative to the SDK folder — only the operations and fields the scope actually touches.

### Step 2 — Required reading (do this before you write any code)

The contract sheet ends with a **REQUIRED READING** block, and its rows carry inline `MUST read <doc>` pointers. **Read every doc under `docs/` the sheet names, now, before you start implementing** — not lazily at the step that needs it. The sheet deliberately does *not* carry the how-to: it names the hazard and hands you the doc that resolves it, so an unread pointer is a gap in what you know, not a formality. If the sheet names none, read `docs/error-handling.md` anyway — every integration writes an error boundary.

<!-- maxio:start -->
This is the one rule for when companion pages are read: once, after the plan is written and before the
first project file changes, and only the pages the sheet names. `AGENTS.md` and `docs/getting-started.md`
list which page governs which step. Neither asks for a second reading: go back to a page only for the
section a trap note cites.

Four pages carry a section written for Maxio. In a page the sheet names, read that section first:
`docs/getting-started.md` "Maxio: site and credentials", `docs/models.md` "Fields the spec does not
declare", `docs/configuration-resilience.md` "Maxio: retries, timeouts and paging", and
`docs/error-handling.md` "Maxio: reading a rejection".

Skip the sections that describe features this SDK does not have: in `docs/configuration-resilience.md`,
the opening of *Pagination*, before *Never leave a page loop unbounded* (no operation returns `Pageable`),
and *Streaming (Server-Sent Events)*; in `docs/error-handling.md` and `docs/testing.md`, the `ApiResult`
sections (no operation has a `…Result` variant); in `docs/testing.md`, *Test a client with OAuth
credentials*; in `docs/calling-endpoints.md`, *Files*.
<!-- maxio:end -->

These are API-agnostic usage docs; reading them is not the same as reading the map. Contract *facts* still come only from the sheet or a map lookup.

Before implementing, check the plan's **Assumptions & Blockers** section:

- Blocker or major assumption → surface it to the user in plain language, get their answer, then revise `maxio-advanced-billing-plan.md` in place with targeted edits — edit the changed rows, append the new section. Rewriting the whole file to change a few rows is a defect.
- Minor assumptions only → proceed.

Full re-planning only on genuine scope change; for a single missing fact mid-implementation, look it up in the map — never guess.

### Step 3 — Implement from the contract sheet

1. Read `maxio-advanced-billing-plan.md` once. Treat its contracts as authoritative — do not re-derive or "double-check" them from memory. A row whose source column says `YOUR CALL — not in the map` is the one exception: that row is a planning-time judgment about YOUR application, so weigh it against the task and follow the task.
2. Implement sequentially, following the repo's own conventions and layering. You read the companion docs the sheet named in Step 2 — implement each step in line with the one that governs it. Take every contract *fact* (signatures, wire names, error accessors, enum values) from the contract sheet or a map lookup — never re-derive one from a companion.
3. After every change: `dotnet build`; fix non-SDK errors yourself.
4. **Any compile or runtime error involving an SDK type or member** (`CS1061`, `CS0117`, `CS0234`, `CS0104`, `CS1503`, `CS7036`, … on `MaxioAdvancedBilling.*`, or a provider error at runtime) → *Step 4* below. Do not attempt more than one self-fix of an SDK-name error before switching to that procedure — rewriting from the same knowledge that produced the error is guessing.
5. Once the code is complete, open each member the **DUPLICATE CLAIMS** and **UNKNOWN OUTCOMES** rows name and confirm it runs when that write runs. Where the code falls short of a row, fix the code, not the row.
6. Run the project's tests (`dotnet test`); verify the integration end to end the way the task demands.

<!-- maxio:start -->
7. When the code is complete and before you report: read `knowledge/go-live.md` once and add the
   **GO-LIVE CHECKS** section to the plan. A check that reaches Maxio runs against a test site only,
   confirmed by `client.Sites.ReadSite()` returning `Site.Test == true` (R2). Report each check as run or
   not run.
<!-- maxio:end -->

### Step 4 — Fixing SDK errors (map-first, in place)

A compile or runtime error involving an SDK type or member (`CS1061`, `CS0117`, `CS0234`, `CS0104`, `CS1503`, `CS7036`, … on `MaxioAdvancedBilling.*`, or a provider error). Resolve it map-first — never patch it by guessing. Read `docs/getting-started.md` first if you have not already — the map is where every fix below comes from.

1. **Map lookup first.** For an operation symbol, find its block on the controller's operations page; for a model, enum, error or request-record symbol, open the declaring file — its name is its path (`src/MaxioAdvancedBilling/Models/{Type}.cs`, `src/MaxioAdvancedBilling/Models/Enums/{Type}.cs`, `src/MaxioAdvancedBilling/Errors/{Type}.cs`, `src/MaxioAdvancedBilling/Requests/{Type}.cs`, or `src/MaxioAdvancedBilling/Requests/{Controller}/{Type}.cs` for an operation on a controller — an operation with several tags is filed under the first tag it declares), or take it from the operation's Type sources table. If the code contradicts what you read (wrong field name, missed response envelope, wrong param order, wrong namespace), that is the fix. Response envelopes are the classic case: response types often wrap their payload in one field — reads go one level down.
2. **Go one level deeper on a real gap.** If what you read matches the code, or ambiguity remains, open the operation's own method in the `Api/{Controller}.cs` file the page header names — its `<remarks>` docs and the request it builds — and the per-member docs on its request record, in the SDK source in this SDK folder, scoped. Never scan the tree.
3. **Never re-guess.** Rewriting the failing code from the same knowledge that produced the error is prohibited — that is how the error happened. Each failing symbol gets a map/source-grounded answer before its line changes; never mutate payloads, field names, or status handling speculatively to "see if it works".
4. **Fix in place** — edit only the project files involved in the error, grounded in the map row (or the named source file).
5. **Build to verify, and classify the outcome:** compiles clean → run `dotnet test` on the touched tests when they exist; compile error → the fix is not done, resolve it the same map-first way and rebuild; build blocked (output locked) → the solution is running, so stop it if you started it, or ask the user to rather than killing their process.
6. **Runtime / provider errors** — read the provider's error payload through the documented path: the operation's error case and `TryGet…` accessors from its map row; `docs/error-handling.md` for the Case A/B mechanics. Config-shaped failures (401, wrong host, timeouts): check auth, the server-node/base-URL configuration, and retry semantics before touching call sites.

<!-- maxio:start -->
For a Maxio rejection, print the status and Maxio's own message (`docs/error-handling.md`, "Maxio: reading
a rejection") and match them in `knowledge/failures.md` before you touch the call. A 422 can be a 3-D
Secure `action_link` or an account-level block, which no change to the request fixes. A 409 on a write
means the outcome is unknown: read the resource back before anything else (R12). A request that went to
a host starting `subdomain.` was sent by a client built without a site (`docs/getting-started.md`, "Maxio:
site and credentials").
<!-- maxio:end -->

If a fix corrects a row in `maxio-advanced-billing-plan.md`, correct the row in the file too — the sheet stays the record of what was verified.

### Step 5 — Pure questions

A standalone Maxio Advanced Billing question with no code change: read `docs/getting-started.md`, look it up in the map (open the one source file the map names only on a real gap), and answer with the map page (or source file) it came from. No plan file — just the grounded answers; when several questions arrive batched, answer them all in one pass. Never answer from memory, even for "easy" questions.

## Anti-patterns — never do these

- **Never write a Maxio Advanced Billing/SDK fact from memory** — every signature, field name, enum value, and error type in your code must come from the contract sheet or a map lookup. And **never write a call from memory "to fix later".**
- **Do not re-derive or double-check a sheet row from memory** — re-open the one map page it cites.
- **Do not re-derive a contract fact from a companion doc under `docs/`** — they are usage guidance; facts come from the map.
- **Do not grep, glob or `find` the SDK tree, and do not read its `api-reference.md` whole** — the map is the locator; `docs/getting-started.md` says why. Search `api-reference.md` for one operation when you need the spec's own description of it.
- **Do not web-search Maxio Advanced Billing for an implementation detail** — the map and the SDK source it lives in are the ground truth for THIS SDK version, and `MaxioAdvancedBilling` is what the generated source declares, not what public docs describe.
- **Do not resolve a trap note inline on the sheet** — name the hazard and the doc.

