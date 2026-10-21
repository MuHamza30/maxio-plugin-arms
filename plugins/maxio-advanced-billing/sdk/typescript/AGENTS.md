# Maxio Advanced Billing SDK for TypeScript: instructions for coding agents

Everything you need to integrate Maxio with this SDK ships in this folder ("the SDK folder"). Look facts
up here. Your memory is unreliable for this SDK's names and for Maxio's rules, so never answer either
from it.

## Reading order

This is the one reading order. Every other file in this folder defers to it.

1. This file.
2. `docs/integrate.md`. It is the workflow: write a plan first, look every contract fact up, then
   implement. It says when to read each other page under `docs/`; read a page when it tells you to.
3. Contract facts (signatures, models, errors) from `sdk-map.md` and the one page it names under
   `map/operations/`.
4. Maxio's business rules from `knowledge/`, and only the parts your task touches:
   - the ten rules below, once;
   - for each operation in scope, the **Provider rules (Maxio)** or **Provider notes (Maxio)** line in its
     block on the map, and the one notes section that line names. Read the section, not the whole notes
     file;
   - the sections of `knowledge/lifecycles.md` and `knowledge/decisions.md` that those lines cite or the
     flow needs. Each file opens with a contents list;
   - `knowledge/go-live.md`, once, when the code is complete and before you report the work done.
5. `recipes/README.md`, then the one recipe you copy.

Before you construct a client, read `docs/getting-started.md`, section "Maxio: site and credentials": the API key,
the site and the region are set explicitly, and a client built without a site targets a site literally
named `subdomain`.

## The ten rules agents most often get wrong

<!-- ten-rules:start -->
1. Send `payment_collection_method` on every signup; omitted, the site's own default applies. Under
   `automatic`, a signup owing money with no payment source gets 422 "No payment method was on file…".
2. `remittance` (Relationship Invoicing) or `invoice` (legacy Statements): the merchant bills by invoice;
   nothing is charged automatically. Choose by intent, never to clear that 422; `readSite` shows which.
3. No Idempotency-Key header. Send one `uniqueness_token` per write at the body root (events: inside
   `chargify`), the same on every resend, a new one after a corrected 422. Serialize writes per customer.
4. Page every list that takes `page` and `per_page`, with `per_page` ≤ 200, until an empty page; larger
   values are clamped silently.
5. `*_in_cents` fields are integer cents; component `unit_price` and invoice amounts are decimal.
6. Access: `active`, `trialing`, `past_due`, `soft_failure`; `pending`/`assessing` keep the last decision.
   `on_hold`, `suspended`, `unpaid`, `awaiting_signup` come back: no access, no second one on that plan.
7. A plan change via `updateSubscription` is not prorated; `migrateSubscriptionProduct` resets the
   period and charges full price unless `preserve_period: true`.
8. At most 4 requests in flight per subdomain; on 429 back off for minutes. A write that times out or gets
   5xx/409 is unknown: read back, wait out 120 s, resend only with the same token; never call it failed.
9. A 4xx never proves a call works. A 409: outcome unknown. A 422 may be a 3-D Secure `action_link` or an
   account block. A 404 by reference: "not there", but only "not yet" after an unknown outcome.
10. Call Maxio from your server only; cards arrive as Maxio.js tokens.
<!-- ten-rules:end -->

## Where things are

| Path | Holds |
|---|---|
| `sdk-map.md`, `map/operations/` | The contract: every operation's signature, request and response types, error cases, and the source file of each model |
| `knowledge/` | Maxio's business rules: `rules.md`, `decisions.md`, `lifecycles.md`, `go-live.md`, `failures.md`, and `operations/` with a section per operation. `knowledge/README.md` explains them and says how a wire name maps to this SDK's name |
| `docs/integrate.md` | The workflow: plan first, look every contract fact up, then implement. Read it second, right after this file. It says when to read each page below |
| `docs/getting-started.md` | Identity, install, environments, and how to traverse the map. Its section "Maxio: site and credentials" says how to set the key, the site and the region |
| `docs/authentication.md` | Credentials and auth schemes; a 401 or 403 |
| `docs/client-initialization.md` | Constructing and holding the client |
| `docs/calling-endpoints.md` | Finding an operation, request shapes, responses, cancellation |
| `docs/models.md` | Building request models, nullability, enums, unions, wire names. Its section "Fields the spec does not declare" says how to send `uniqueness_token` and read `action_link` |
| `docs/models-reference.md` | Reference tables for `docs/models.md` |
| `docs/error-handling.md` | Error handling and error translation. Its section "Maxio: reading a rejection" shows how to get the status and Maxio's own message out of an SDK error |
| `docs/configuration-resilience.md` | Retries, timeouts, servers, logging. Its section "Maxio: retries, timeouts and paging" says what to change for Maxio |
| `docs/testing.md` | Faking the transport seam; testing error paths |
| `recipes/` | Code to copy and adapt: `list-all.ts`, `request-limit.ts`, `safe-signup.ts`, `subscription-state.ts`, `verify-webhook.ts`. `recipes/README.md` says what each one does, which rules it implements and what it leaves to you |
| `api-reference.md` | The generated reference, with the spec's own descriptions. Large; search it for one operation, never read it whole |

## When Maxio rejects a call

Find the status and message in `knowledge/failures.md` before you change code. `docs/error-handling.md`,
section "Maxio: reading a rejection", shows how to get both out of an SDK error. A 4xx is a rejection, never
evidence that a call works. A 409 on a write means the outcome is unknown: read the resource back. A 422 may
be a 3-D Secure challenge or an account block that no change to the request will fix. A 404 on a lookup by
reference is the normal "not there" answer.

## The project block

`knowledge/AGENTS.block.md` holds the ten rules as a block for the project's own `AGENTS.md`, so that later
sessions and other coding tools have them without opening this folder. It has nothing to fill in.
Adding it changes the project's own instruction files, which is the user's decision. So add it only when
the user asks for it or approves a plan step that adds it. A tool the user installed can carry that request:
when a Maxio plugin or skill asks you to make adding the block a step of your plan, so the user can
approve or decline it, follow it. This section does not override it. Without such a request, leave those
files alone, and if the project's `AGENTS.md` has no block marked `maxio-advanced-billing:rules:start`,
end your report with one line saying that the block exists and where it is.
