# Recipes

Source files to copy into your own project for what Maxio requires and this SDK does not do for you.
Each needs only `maxio-advanced-billing` and Node's standard library, says in its opening comment
exactly what it does and does not do, and is not part of the SDK's API. Read this page, then only the
recipe you copy.

Rule ids point into `knowledge/`: R in `rules.md`, D in `decisions.md`, L in `lifecycles.md`.

| Recipe | What it does | Rules | What it leaves to you |
|---|---|---|---|
| `safe-signup.ts` | Looks the subscription up by your reference, then sends one create with your `uniqueness_token` at the body root and 130 s to answer. Returns `created`, `existing`, `recovered` or `unknown`: never a bare subscription. A 5xx, a 408, a 409, a timeout, a dropped connection, an unreadable 2xx and a cancellation after the send all lead to a read-back on its own 30 s timer, and a failed read-back still returns `unknown` with both causes. `existing` and `recovered` carry the subscription's standing, so a canceled one is never taken for a signup. Never resends by itself. `findCustomer` looks the customer up by your user id: call it before every signup. `findHeldSubscription` finds a subscription that customer already holds on the plan in a state that allows no second one beside it, skipping one under this signup's own reference, which `safeSignup` reports as `existing`. Needs `subscription-state.ts` beside it | R11, R12, L2 steps 4, 6 and 7. Requires the collection method (R14) and exactly one customer source (D1), both checked by the compiler | Minting the token once per signup and storing it; one signup per reference at a time (two at once both create); waiting and calling again after `unknown`; calling `findCustomer` first, then `findHeldSubscription` when it found one, and naming the customer by the answer; the collection method and payment source (D2, D3); reading a 422 (R13) |
| `list-all.ts` | Reads every page of a list that takes `page` and `perPage` and returns an array, 200 rows a page, until a page comes back empty. Reaching the page ceiling throws. With a key function it drops rows already seen. The header shows how to unwrap a list that returns an object | R8 | The filters (R9), the ceiling, the sort order (a shifting list can still skip a row; sort oldest first on a field that does not change), and never passing a list that has no `page` field |
| `subscription-state.ts` | Classes every state the SDK names as `live`, `transient`, `recoverable` or `ended`, and a missing or unnamed state as `unclassified`, with `hasAccess` and `decideAccess`. Stops compiling when the SDK gains or loses a state | R16, L3 | Storing the last access decision per subscription; listing without a `state` filter, because that filter cannot name `soft_failure`; reading the subscription again before acting on a webhook (R20) |
| `verify-webhook.ts` | Hex HMAC-SHA256 of the raw body with the site's shared key, compared in constant time. `false` for a missing or malformed signature. `signatureFrom(headers)` reads the header in any case from Node's `req.headers` or a fetch `Headers` | R19 (the signature) | Keeping the body bytes as they arrived; answering 200 within about 15 s; skipping webhook ids already processed; reading the resource again (R20) |
| `request-limit.ts` | At most four calls in flight per site in this process, first come first served. A waiter can be cancelled with a signal. Calling the gate from inside a call it is running is refused. Exports `maxioRetryOptions()` and `ONE_SEND`, the two options below | R10, and the options R10 and R11 need | Pausing for minutes after a 429; sharing the limit between processes (each process counts only its own calls); routing every call through the gate |

## The SDK's own resends, and the two options that stop them

By default this SDK sends a `GET`, `HEAD`, `PUT` or `OPTIONS` again up to three times, about 1, 2 and 4
seconds apart, when it answers 408, 429, 500, 502, 503 or 504, times out or loses its connection. A
`POST`, `PATCH` or `DELETE` is sent once.

- **A 429.** Maxio asks for a pause of minutes (R10). Build the client with
  `retry: { statusCodesToRetry: [408, 500, 502, 503, 504] }`. A 429 then reaches you at once.
- **A `PUT` that can take a payment or use up an attempt** (R11): `retrySubscription`,
  `reactivateSubscription`, `activateSubscription`, `updateSubscription` with payment details, and
  `verifyBankAccount`. Pass `ONE_SEND`, `{ retry: { maxRetries: 0, timeout: 130_000 } }`, as that
  call's second argument. Or, to stop it for every `PUT`, build the client with
  `retry: { httpMethodsToRetry: ["GET", "HEAD", "OPTIONS"] }`.

`maxioRetryOptions()` in `request-limit.ts` returns both client options together, and keeps every
other default. Given the retry options you already have, it keeps them and takes out 429 and every
method but `GET`, `HEAD` and `OPTIONS`. The tests count the requests the transport receives for each
option, beside a control that shows the default sending four.

## Copying them in

- **Module format.** The files are ES modules (`import` and `export`). They compile and run unchanged in
  a project whose `package.json` says `"type": "module"`, under `module` and `moduleResolution`
  `NodeNext`. They also compile under `Bundler` resolution with the DOM library.
- **A CommonJS project** (no `"type"`, or `"type": "commonjs"`). With `verbatimModuleSyntax` on, the
  compiler refuses them (TS1287, TS1295). Either turn `verbatimModuleSyntax` off, and they compile and
  run unchanged as CommonJS; or keep it on, rename the files to `.mts`, change the one relative import in
  `safe-signup.ts` from `./subscription-state.js` to `./subscription-state.mjs`, and load them from
  CommonJS code with `await import()`.
- **Relative imports.** `safe-signup.ts` imports `./subscription-state.js`. Copy both into one folder.
  The `.js` ending is what `NodeNext` requires, for a `.ts` file too.
- **Node.** 20.11 or later; the tests ran on Node 20.11, 20.20, 22.23 and 24.19. `safe-signup.ts`
  uses `AbortSignal.any` and `request-limit.ts` uses `AsyncLocalStorage`.
- **Compiler settings they were checked under** (TypeScript 7.0.2, with `@types/node` 20): `strict`,
  `exactOptionalPropertyTypes`, `noUncheckedIndexedAccess`, `noImplicitOverride`, `noImplicitReturns`,
  `noFallthroughCasesInSwitch`, `noPropertyAccessFromIndexSignature`, `noUnusedLocals`,
  `noUnusedParameters`, `isolatedModules`, `verbatimModuleSyntax`, `erasableSyntaxOnly`,
  `skipLibCheck: false`, and separately `isolatedDeclarations`.
- **The token field.** `safe-signup.ts` types its body as
  `CreateSubscriptionRequest & { uniqueness_token: string }`. The SDK declares the token on no model, so a
  plain object literal typed as `CreateSubscriptionRequest` with the token in it does not compile
  (TS2353). Keep the intersection when you adapt the file.

## How they were checked

`recipe-tests/typescript/` at the root of this repository holds the tests. They import these files
where they are, run offline against a fake `fetch` given to the SDK as `ClientOptions.fetch`, and run
twice: as ES modules and as a CommonJS copy. Its `README.md` gives the one command and lists what the
tests prove.
