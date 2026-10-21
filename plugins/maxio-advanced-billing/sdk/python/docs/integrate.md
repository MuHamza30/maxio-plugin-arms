# Maxio Advanced Billing Python SDK — Integration workflow (lookup layer + contract sheet)

**Read when:** you are asked to add or change Maxio Advanced Billing code in a Python project with this SDK, or a call through this SDK errors or behaves unexpectedly. Read it before you write any code. There is one reading order: this SDK folder's `AGENTS.md`, then this page, then what this page tells you to read. This page sets five binding gates: (1) read `docs/getting-started.md`, confirm the package is actually installed and read the SDK map that ships with it before any lookup, (2) the exact plan-file path and the no-project-file-edits window until a contract sheet with no open lookups exists there and you have read it, (3) the mandatory read of every `docs/*.md` companion doc the sheet names, (4) sync-vs-async decided once from the host application before the first call, and (5) the memory ban, where every signature, wire alias, error union and enum member comes from a lookup and never from recall or runtime introspection.

You do the SDK lookups yourself: `docs/getting-started.md` is your **lookup layer** — read it and ground every contract fact in it (and in the source modules its table names) before writing code. The `docs/*.md` companion docs are a different thing: they are API-agnostic *usage* guidance, they are yours to read, and Step 1c below makes reading them mandatory. Step 1c is the one place that says when to read them; the other pages defer to it.

## Your lookup layer

- **`docs/getting-started.md`** is the entry point for every SDK need. It carries the SDK's identity (distribution name vs import root, version, Python floor, install-from-source), what the root package exports and the four modules the surface splits across, environments and the base-URL knob, the auth pattern, the controllers, and a **module table** naming the one file that owns each kind of fact. Read it before any lookup, always. Its last section, *Lookup: error bodies by operation*, is a table to search for the operations in scope, not text to read through.
- **The SDK map is your lookup surface, and you open it yourself.** The SDK ships `sdk-map.md` and `map/operations/` at its root. The map is yours to read. `docs/getting-started.md` tells you how to traverse it: read `sdk-map.md` once, then the one controller page your operations live on.
- **The installed package is the ground truth; the module table is only the locator.** Confirm the package is importable before you rely on a lookup — `python -c "import maxio_advanced_billing, pathlib; print(pathlib.Path(maxio_advanced_billing.__file__).parent)"`. **If it is not installed, install it first** — `docs/getting-started.md` carries the command; until then mark the fact `UNVERIFIED`, say what would settle it, and do not fill the hole from memory. (The distribution is not on any package index — it installs from this SDK folder; `docs/getting-started.md` carries the command.)
- **Read scoped.** Those modules carry long design docstrings. `grep -n` for the symbol and read the surrounding lines rather than whole files, and never copy a docstring's design rationale onto a contract sheet — the sheet carries facts an implementer must obey, not the reasoning behind them.
- **Write a contract sheet with no open lookups** before you implement: exact signatures, the keyword-only boundary, wire aliases, required-vs-`UNSET` members, the `ApiError.error` union per operation, and enum members for the operations in scope. `docs/getting-started.md` ends with a checklist of the rows a Python sheet is incomplete without — treat that list as the checklist for your own sheet, and collect every in-scope operation in ONE pass rather than re-opening a module per member.

**Scope guard:** the APIMatic-generated Maxio Advanced Billing **Python SDK** (import root `maxio_advanced_billing`, distribution `maxio-advanced-billing`) in **Python projects only**. Unrelated API, or any language other than Python — do nothing; this doc does not apply.

<!-- maxio:start -->
## Provider knowledge: Maxio's business rules

The map gives you Maxio Advanced Billing's call surface. It cannot give you Maxio's business rules: what
must exist before a call succeeds, which of two overlapping operations to use, which values silently do
nothing, and what each rejection means. Agents get those wrong far more often than signatures. They ship in
this SDK folder under `knowledge/`, and the parts you must not miss are placed on your path:

- `AGENTS.md` carries the ten rules that apply to every call. `sdk-map.md` opens with the same ten. Read
  them once.
- An operation block in `map/operations/` opens with a **Provider rules (Maxio)** line when Maxio has rules
  that change what you send, or with a **Provider notes (Maxio)** line when it has notes only. Either line
  names the operation's notes section. A block with neither has no provider notes.
- `knowledge/failures.md` lists every known rejection by status and message, with its cause and fix.

**What to read, and when.** Read the sections your task touches, not whole files, and never answer a
business-rule question from memory.

1. The ten rules. You have them from `AGENTS.md`. Do not read `knowledge/rules.md` whole: open one rule
   there by its id (`### R12`) when a line cites it and you need the detail.
2. For each operation in scope, while you fill its contract-sheet row: its Provider rules or Provider notes
   line, then the notes **section** that line names. The line's path ends in the operation's name
   (`knowledge/operations/subscriptions.md#createsubscription`) and the section is headed by that name as
   the spec spells it (`### createSubscription`). Read that section, not the file.
3. The lifecycle and decision sections those lines cite or the flow needs: `knowledge/lifecycles.md` for
   the order of calls and the states (L2 for a signup), `knowledge/decisions.md` for which operation or
   value to use. Each file opens with a contents list, so open sections by id. Where a choice depends on
   the user's intent and the task does not say, ask.
4. `recipes/README.md`, when the task needs something the SDK does not do for you: paging every list, a
   safe signup, subscription-state checks, webhook verification, a request limit. Then read only the
   recipe you copy. Copy and adapt it. Do not write your own.
5. `knowledge/go-live.md`, once, when the code is complete and before you report.

**What this changes on the plan.** The plan's steps follow the order the lifecycle section gives, with
every *Before you call* precondition as a step of its own. The contract sheet gains the rows that
`docs/getting-started.md` lists under *What a contract sheet must carry for this SDK* (items 11 to 15),
a Provider rules cell on every operation row among them. Three things decide what goes in:

- A provider rule can require an optional field. A field that a Provider rules line, or a rule in
  `knowledge/`, names is not optional for this task: set it, and cite the rule id in the row.
- A field Maxio needs and the spec does not declare gets a row too. `uniqueness_token` is on no map page
  and on no model, and every write that could be sent twice still carries it (R12). `docs/models.md`,
  *Fields the spec does not declare*, says how to send it. Because it has a row, a test that rejects
  request keys with no row accepts it.
- A provider rule outranks your memory of this API and any default you would otherwise pick. Where a rule
  and the SDK disagree on a contract fact (a name, a type), the map and the module it names win: record
  the conflict. A field the map does not show is not such a conflict, so "the map wins" does not remove
  `uniqueness_token`.

**When Maxio says no**, in a smoke, a test or the running app: print the status and Maxio's own message
(`docs/error-handling.md`, *Maxio: reading a rejection*, has the code) and find them in
`knowledge/failures.md` before you change code. A 4xx is never evidence that a call works. A 409 on a write
is not a rejection to pass on to your caller: the first copy of the write arrived and its outcome is
unknown, so settle it by reading the resource back (R12, `knowledge/lifecycles.md` L2).

**The project block.** `knowledge/AGENTS.block.md` holds the ten rules as a block for the project's own
`AGENTS.md`. Adding it is the user's decision: `AGENTS.md` in the SDK folder, section *The project block*,
says when to add it and when only to mention it in your report.
<!-- maxio:end -->

## Workflow

**If the user opens with a reported SDK error or unexpected Maxio Advanced Billing behaviour** (not new feature work), skip the plan-first flow: read `docs/getting-started.md` and `docs/error-handling.md`, look the failing symbol up in the module the table names, and fix from what you find. Otherwise, for implementation work:

<!-- maxio:start -->
If the error is Maxio answering with a 4xx, it is a rejection to look up, not an SDK fault. Follow *When
Maxio says no* above before you change code.
<!-- maxio:end -->

### Step 1 — Plan first (always, for any implementation work)

Start by reading `docs/getting-started.md` (you have read `AGENTS.md` and this page already) and work through the user's full request (all features in scope — one plan covers the whole implementation). Then write the plan and its contract sheet to `<project repo root>/maxio-advanced-billing-plan.md` — that absolute path, not a location you pick later.

The plan file has three parts: the **steps** in the order they will be built, each naming the operations it calls; the **contract sheet**, whose rows `docs/getting-started.md` lists and which holds the DUPLICATE CLAIMS table and the REQUIRED READING block below; and **Assumptions & Blockers**: what you assumed because the task did not say, and anything that stops the work until the user answers. An empty Assumptions & Blockers section is a valid outcome.

**Do the read-only prerequisites in the same pass — they need no SDK knowledge and touch no project file:**

- the repo survey (read-only exploration of conventions, layering, and **whether the project is sync or `async`**) — capture each convention as *pattern + the ONE exemplar file path to imitate*, NOT inline code snippets: you will read the exemplar at edit time anyway, so a snippet dump gets paid for twice;
- **establish the toolchain before you need it**: which environment manager the repo uses (`uv`, `poetry`, `pip` + venv, `pdm`), whether `maxio-advanced-billing` is already a dependency and at what version, and the exact commands that run the project's tests and type checker. Getting this wrong later costs a broken install mid-implementation — and an uninstalled package cannot be type-checked or run against;
- a baseline run of the project's checks (`pytest`, `mypy`, `ruff` — whatever it has) on the UNTOUCHED tree, so later failures are attributable to your changes;
- credentials/environment verification (per the task's secret-handling rules) — including which host `environment` will select, since omitting it is silent;
- **a read-only smoke of each in-scope operation against a test site**, run from a scratch directory outside the project, once the map has given you the signatures and before you finalise the sheet. A plan-, region- or entitlement-gated endpoint answers `403` here — the map presents every operation uniformly and cannot know which ones your key may call — and learning that now reorders the plan rather than the build. Smoke reads only; the passage below says how to confirm the site is a test site.

<!-- maxio:start -->
For Maxio, two of these prerequisites need more than the list says:

- **Credentials and environment are three values, not one:** the API key, the site and the region. A
  client built without a site calls a site literally named `subdomain`, and nothing fails at construction
  (`docs/getting-started.md`, *Maxio: site and credentials*).
- **The smoke runs against a test site only, and it only reads.** Call `client.sites.read_site()` first
  and go on only if the returned site has `test` set to true (`knowledge/rules.md` R2,
  `knowledge/go-live.md`). If it is false, or you cannot tell, do not smoke: say so and ask. Never smoke a
  write on a live site, and never smoke a write that can take a payment (R11), whether or not you could
  reverse it. A 4xx from the smoke is a rejection to look up, never proof that the call works.
<!-- maxio:end -->

Never use the planning phase to get a "head start" on implementation: **creating or editing ANY project file before the gate below is a defect**, no matter how obvious the code seems.

**HARD GATE — no project-file creation or edits until:** `maxio-advanced-billing-plan.md` EXISTS at the repo root, its contract sheet has **no open lookups**, and you have read it. The gate bars coding "meanwhile"; it does not bar the read-only prerequisite work above. Starting to code before the sheet exists defeats the entire plan-first design.

**What the gate does not cover:** creating or activating a virtual environment, installing `maxio-advanced-billing` and the toolchain into it, and the files those writes produce (`.venv/`, a lockfile the installer updates) are **prerequisites, not project-file edits**. On a greenfield repo they are what makes the type check and the tests possible, and they are the only writes permitted before the gate. Nothing you author by hand may change.

**DUPLICATE CLAIMS** — one row per write a caller can trigger twice; `none` if the task has no such write (`docs/configuration-resilience.md`, *The same operation arriving twice*).

| Write | Where the claim is stored | What rejects the second one | Where that rejection is caught | Where in the code |
| --- | --- | --- | --- | --- |

Every row follows one order: **claim → SDK call → record the result**. The claim is a write of its own, made before the SDK call, so a second caller is stopped before it reaches the provider; release it when the provider refuses the call.

⚠⚠ **Where the claim is stored**: a store this application owns — the one the codebase already keeps its records in — never the provider. A provider idempotency key goes beside the claim, never in place of it; the SDK's own `Idempotency-Key` header is not one — it is new on every call. If this codebase has nowhere to keep a claim that outlives the process, that is a Blocker in the plan's **Assumptions & Blockers**, not a row.

<!-- maxio:start -->
**For Maxio:** no operation on the map takes an idempotency key, and Maxio does not read the SDK's
`Idempotency-Key` header. Maxio's key is `uniqueness_token`, a body field the spec does not declare
(`knowledge/rules.md` R12; `docs/models.md`, *Fields the spec does not declare*). One token per write:
mint a long random value for each write when you take the claim, store it with the claim, and send that
same value on every resend of that write. A signup that creates a customer and then a subscription mints
two. Mint a new one only after a 422 you corrected, or where `knowledge/rules.md` R11 step 4 allows it.
The row's **Where the claim is stored** cell names where the token is kept too. The claim itself is
keyed by your own deterministic `reference`, which is also how you read the resource back.
`recipes/safe_signup.py` is the signup case.
<!-- maxio:end -->

⚠⚠ **What rejects the second one**: the store refusing the second caller's claim, the way this codebase already refuses a duplicate. A conflict on the save *after* the SDK call is too late — both callers have already reached the provider. A read before the write — a status check, a lookup by key — is not a refusal either: it lets both callers through. Pick a refusal the store you run against enforces.

**Where that rejection is caught**: the `except` for what the store raises on the second claim — a lookup that returns the earlier result is not an `except`.

Write `TBD` in **Where in the code** while you plan — every row; it names code not yet written, not a contract fact, so it is not an open lookup. Once the code type-checks, replace each `TBD` individually with two functions, in order: the claim write, then the SDK call it precedes. Only this column changes after coding starts. ⚠⚠ A `TBD` left behind, a function that is not in the code, or one note covering several rows is **not addressed**; if the code does not do what the row says, fix the code, then the cell.

### Step 1c — Required reading (do this before you write any code)

End the contract sheet with a **REQUIRED READING** block whose rows carry inline `MUST read <doc>` pointers. **Read every `docs/*.md` doc the sheet names, now, before you start implementing** — not lazily at the step that needs it. The sheet deliberately does *not* carry the how-to: it names the hazard and hands you the doc that resolves it, so an unread pointer is a gap in what you know, not a formality.

**A fixed floor applies regardless of what the sheet says** — the sheet can add to it, never remove from it: `docs/error-handling.md` always (every integration writes an error boundary); `docs/client-initialization.md` before the client is constructed; `docs/testing.md` before the first test file you create or edit, *including* a throwaway verification script that fakes the transport. A sheet row that excuses one of these ("out of scope", "no test suite requested") is not a substitute for reading it.

<!-- maxio:start -->
**For Maxio, a REQUIRED READING row may name one section of a page**, and then that section is what you
must read. The fixed-floor pages above are still read whole. Four sections carry what Maxio needs from
this SDK, and other files point at them by these names:

- `docs/getting-started.md`, *Maxio: site and credentials*: every task that builds a client.
- `docs/configuration-resilience.md`, *Maxio: retries, timeouts and paging*: every task with a write, a
  list or a 429 to handle.
- `docs/error-handling.md`, *Maxio: reading a rejection*: every task.
- `docs/models.md`, *Fields the spec does not declare*: every write that carries `uniqueness_token`, and
  every call whose 422 can carry an `action_link`.

Never name `docs/event-streams.md` or `docs/file-handling.md`: no operation of this API streams events or
handles files. Name `docs/authentication.md` only for what its opening passage lists: this API has basic
auth only.
<!-- maxio:end -->

These are API-agnostic usage docs; reading them is not a substitute for the lookup layer, and reading a module in the installed package does not remove the need to read the doc for that step. Contract *facts* still come only from your sheet or a fresh lookup.

Before implementing, check the plan's **Assumptions & Blockers** section:

- Blocker or major assumption → surface it to the user in plain language, get their answer, and revise `maxio-advanced-billing-plan.md` in place.
- Minor assumptions only → proceed.

Full re-planning only on genuine scope change; for a single missing fact mid-implementation, do the lookup, never guess.

### Step 2 — Implement from the contract sheet

1. Read `maxio-advanced-billing-plan.md` once. Treat its contracts as authoritative — do not re-derive or "double-check" them from memory. When a lookup revises a row, update the file so the sheet and the code never disagree.
2. **Decide sync vs async once, from the host application, before the first call** — and take the decision from the repo survey, not from preference. This SDK ships two complete client classes (`Client` / `AsyncClient`) and there is no bridge between them: a sync client in an `async def` blocks the event loop, and an async client in sync code is a coroutine nobody awaits. Getting this wrong is not a local fix later; it is every call site. The choice also changes the transport-override keyword (`custom_http_client` vs `custom_async_http_client`) and the teardown obligation (`close()` vs `await aclose()`).
3. **Pick the response mode per call, deliberately.** Each operation exists twice: the plain call raises `ApiError` on failure, and its `with_raw_response` peer returns `ApiResult` instead. For the operations that return `None`, the raw peer is the only way to observe the status code — so a call whose outcome you must inspect needs the mode chosen at write time, not retrofitted.
4. Implement sequentially, following the repo's own conventions and layering. You read the companion docs the sheet named in Step 1c — implement each step in line with the one that governs it. Take every contract *fact* (signatures, wire aliases, error unions, enum members) from the contract sheet or a fresh lookup — never re-derive one from a companion.
5. After every change: run the project's **type checker** (`mypy`/`pyright`) as well as its tests. The package ships `py.typed` and is generated under `mypy --strict`, so a type error against it is a real contract violation, not noise — it is the closest thing Python gives you to the compile step. **Treat a clean type check as the gate you do not skip.** If the project has no type checker configured, install `mypy` into the environment and run `mypy --strict` on the files you touched — the SDK is generated under that setting, so it checks cleanly against it. If you genuinely cannot install one, say so in your final report rather than silently substituting a smoke run. Fix non-SDK errors yourself.
6. **Any error involving an SDK type or member** — an `AttributeError`/`TypeError` on a `maxio_advanced_billing.*` object, a `pydantic.ValidationError` you cannot place, a mypy error naming an SDK type, an unexpected `ApiError` — → go back to `docs/getting-started.md`'s module table and read the one module that owns the fact. Do not attempt more than one self-fix of an SDK-name error before doing that lookup: rewriting from the same knowledge that produced the error is guessing. Remember that a **decode failure raises `ValidationError`/`ValueError`, not `ApiError`, and bypasses both response modes**, and that `httpx2` transport exceptions arrive unwrapped — so an exception that does not look like an API error may still be one of the SDK's failure kinds.
   <!-- maxio:start -->
   An `ApiError` with a 4xx status is first of all Maxio rejecting the request. Print it and look it up
   (`docs/error-handling.md`, *Maxio: reading a rejection*) before you treat it as an SDK-name error.
   <!-- maxio:end -->
7. Once the code is complete, open each function the **DUPLICATE CLAIMS** rows name and confirm it runs when that write runs. Where the code falls short of a row, fix the code, not the row.
8. Run the project's tests; verify the integration end to end the way the task demands. Retrying is **on by default**, so decide whether the task keeps it, tunes it through `retry_options`, or turns it off with `max_retries` set to `0`, rather than wrapping the call in a retry of your own — and say which you did.
   <!-- maxio:start -->
   For Maxio the decision is made in `docs/configuration-resilience.md`, *Maxio: retries, timeouts and
   paging*: no automatic retry of a 429 or of a write that can take a payment, and at least 120 seconds
   for a write. Then go through `knowledge/go-live.md` once, before you report.
   <!-- maxio:end -->

### Step 3 — Answering pure questions

A standalone Maxio Advanced Billing question with no code change: look it up in `docs/getting-started.md` (and the module its table names), then give the grounded answer. Never answer from memory, even for "easy" questions.

<!-- maxio:start -->
A question about what Maxio requires or does, not about this SDK's names, is answered from `knowledge/`:
the operation's notes section, or the rule, decision or lifecycle section by id. `knowledge/README.md`
says which file holds what.
<!-- maxio:end -->

## Anti-patterns — never do these

- **Never skip `docs/getting-started.md`.** It is your lookup layer, not optional background. (The `docs/*.md` companions are the complement: read the ones the sheet names, per Step 1c.) Don't re-derive a contract *fact* from a companion — exact signatures, wire aliases, error unions and enum members come from the sheet or a fresh lookup.
- **Never write a Maxio Advanced Billing/SDK fact from memory** — every signature, field name, enum member, and error union in your code must come from the contract sheet or a lookup. And **never write a call from memory "to fix later".**
- **Don't web-search Maxio Advanced Billing topics to find an implementation detail** — the installed package's own source is the ground truth, and the module table tells you where to look. Public Maxio Advanced Billing docs describe the REST API, not this SDK's generated surface, and the two disagree on names.
  <!-- maxio:start -->
  Maxio's rules for the operations an integration most often calls are in `knowledge/`, in this SDK's
  call names. Look there before any search.
  <!-- maxio:end -->
- **Never introspect the SDK at runtime to discover its shape.** `dir()`, `model_fields`, `inspect.signature`, or a REPL poke is the Python-flavoured version of decompiling the package: it answers what exists, never what is *supported*, and it silently invites private attributes into your code. Read the source module instead.
- **Don't grep the package to *locate* a type** — the SDK map is the locator (and says so: *"Never grep for a type"*); grep only *inside* the module its **Type sources** table names, for the symbol. A sweep for a *shape* is a different thing, and is fine: "every member typed `Optional[Any]`", "every discriminator field" are cross-cutting questions nothing indexes, and one targeted `grep -rn` over `models/` is the right tool for them — record what it found on the sheet.
- **Don't vendor, `sys.path`-hack, or editable-install the SDK from a throwaway clone** to make a lookup possible. Install the distribution properly into the project's environment (see `docs/getting-started.md`); an editable install pointed at a clone breaks every import the moment the clone is deleted.
- **Don't create or edit project files before the HARD GATE** in Step 1 — plan and contract sheet first, code second.

