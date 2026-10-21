# Maxio Advanced Billing: Maxio's business rules

The SDK map tells you **how to call** Maxio with this Python SDK: signatures, models, errors. This
folder tells you **what Maxio requires**: what must exist first, which of two operations to use, which
values silently do nothing, and what each rejection means. It is rendered for this SDK from one
language-neutral source, so the rules are the same in every language; only call names differ.

| | |
|---|---|
| API spec version | 1.0 (the version this SDK and its map were generated from) |
| Rules curated | 2026-10-13 |
| Generated with | APIMatic CLI 2.0.0-beta.5 |
| Operations with notes | 114 of 285 |

## What is here

Read the part your task touches, not the whole folder. `AGENTS.md` in the SDK folder gives the reading order.

| File | Holds | Read |
|---|---|---|
| `operations/<group>.md` | One section per operation: **Always**, **Before you call**, **Rules**, **When it fails** | The one section for each operation in scope, before you call it. The operation's block on the map names the section |
| `rules.md` | API-wide rules, R1 to R20 | A rule when one of the ten rules, a provider line, a notes section or your task points at it. Never the whole file |
| `decisions.md` | Where Maxio offers several ways to do one thing, D1 to D20 | A decision when something points at it, or when your flow has that choice to make |
| `lifecycles.md` | Call order and the subscription and invoice state models, L1 to L9 | A lifecycle when something points at it, or when your flow follows it |
| `go-live.md` | Sandbox proof and the pre-delivery checklist, G1 to G15 | Once, when the code is complete and before you report the work done |
| `failures.md` | Every known rejection by status and message, with cause and fix | On any rejection, before changing code |
| `index.json` | One entry per operation, keyed by the spec's operationId: this SDK's call, the route, the map block, and the notes section or `null` | To go from an operationId to the call and the notes. To start from a call name, search the file for it |
| `AGENTS.block.md` | The ten rules as a block for the project's own `AGENTS.md`, to add as it is | Only when the user wants it (`AGENTS.md` in the SDK folder, section "The project block") |

`rules.md`, `decisions.md`, `lifecycles.md` and `go-live.md` each open with a contents list: find the id there and
read that section.
An operation with no section has no provider notes: record "no provider notes", which is an answer, not a gap.

## How a reference to a notes section reads

The map and `failures.json` name a section like this: `knowledge/operations/subscriptions.md#createsubscription`. That is the
file's path from the SDK folder, then `#`, then the section heading in lower case. A section is headed by the
API's own name for the operation (its operationId), and the line under the heading gives this SDK's call
(`client.subscriptions.create_subscription`).

## How to read an entry

Every rule states what to do, what breaks if you don't, and where it comes from:

- **[docs]** a Maxio documentation page · **[spec]** the OpenAPI spec · **[announcement]** a dated Maxio
  announcement · **[observed]** behaviour seen in controlled agent runs against a sandbox.
- *(inferred)* a consequence the sources imply but do not state · *(unconfirmed)* the sources conflict
  or are silent.

A provider rule outranks your memory of this API. Where a rule here and the SDK disagree about a contract
fact (a name, a type), the SDK and its map win; report the conflict. A field the rules name that the spec
does not declare (`uniqueness_token`, `action_link`) is not such a conflict: it is on no model, and
`docs/models.md`, section "Fields the spec does not declare", says how to send or read it.

## From a wire name to this SDK's name

Fields are named here by their wire names, as the API spells them.
In this SDK a name is the wire name unchanged: `payment_collection_method` is `payment_collection_method`.
The exceptions keep clear of Python's own names or are not valid names. On models, `type` is `type_` and
`_destroy` is `destroy`; `id` stays `id`. On operation parameters, `id` is `id_`, `filter` is `filter_`,
`credits` is `credits_`, `filter[type]` is `filter_type`, `calendar_billing['resumption_charge']` is
`calendar_billing_resumption_charge` and the `Authorization` header is `authorization`. A list parameter
written with `[]` on the wire (`cascade[]`, `include[]`) is the plain name (`cascade`, `include`). When in
doubt, read the name off the contract: an operation block's **Params** bullet shows the wire name wherever
it differs, and a model field carries its wire name as `Field(alias=...)` in the module the map names.

## What is not here

Only what the contract cannot say is here. Signatures and error types are on the map. Fields, their types,
required members and enum members are on the map and in the module it names. How this SDK sends or
reads something is in `docs/`, and working code for what the SDK does not do for you is in `recipes/`.
