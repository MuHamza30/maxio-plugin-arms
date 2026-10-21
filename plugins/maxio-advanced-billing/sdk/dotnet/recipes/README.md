# Recipes

Code to copy for what Maxio requires and this SDK does not do for you. Each file depends only on this
SDK and the .NET base class library, except `SafeSignup.cs`, which also needs `SubscriptionState.cs`.
None of it is part of the SDK's API. Each file's header says exactly what it does, what it does not do,
and what you must set up around it. Read the header of the one you copy, not all five.

Rule ids point at `knowledge/rules.md` (R), `knowledge/decisions.md` (D) and `knowledge/lifecycles.md`
(L). Paths are relative to the SDK folder.

| Recipe | What it does | Rules | What it leaves to you |
|---|---|---|---|
| `recipes/SafeSignup.cs` | Creates a subscription at most once. Looks your reference up first; sends one create with your `uniqueness_token` at the top level of the body and your `payment_collection_method` inside `subscription`; never sends it twice, whatever the client's retry settings; settles a 409, a timeout, a dropped connection, a 5xx, a 408 or an unreadable 2xx by reading back. Returns `Created`, `Existing`, `Recovered` or `Unknown`; the found ones carry their standing, so an ended subscription is not taken for a signup. Your cancellation after the create was sent cannot stop the read-back. `FindCustomer` looks the customer up by your user id: call it before every signup. `FindHeldSubscription` finds a subscription that customer already holds on the plan in a state that allows no second one beside it, skipping one under this signup's own reference, which `SignUp` reports as `Existing` | R11, R12, R13, R14; L2 (find the customer, subscribe and settle), L3 | A lock per customer in your own store (without it, two calls at once both create); a deterministic reference; minting and storing the token; the collection method (D3), calling `FindCustomer` first, then `FindHeldSubscription` when it found one, and naming the customer by the answer (D1), and the payment source (D2); client timeouts of at least 130 seconds; no deadline under 120 seconds on the call; waiting and calling again after `Unknown` |
| `recipes/ListAll.cs` | Walks a paged list: `per_page` 200 or a smaller cap you pass, from page 1 until an empty page. Reaching your page ceiling throws `PageCeilingException`. With a key function, a row already returned is dropped. `ListAll.Subscriptions` is the worked example and asks for ascending order unless the request names a direction | R8 | The ceiling; unwrapping a list that returns a wrapper object; not using it on a list that takes no `page`; filters that fail open (R9); the request limit; export jobs for bulk reads (D19) |
| `recipes/SubscriptionState.cs` | Classifies every state the SDK declares as `Live`, `Transient`, `Recoverable` or `Ended`, and stops compiling when the SDK gains a state it does not classify. `HasAccess` is true for `active`, `trialing`, `past_due` and `soft_failure`. `AccessAfter` keeps your previous decision for `pending`, `assessing` and a state it does not know | R16; L3 | Keeping your copy of the state current (R20, D19); storing the decision you hold. The list filter `state` takes a different, single-valued set (`SubscriptionStateFilter`), so "everyone with access" is a list with no state filter, classified here |
| `recipes/VerifyWebhook.cs` | Checks the hex HMAC-SHA256 of the raw body under the site's shared key in constant time. A missing or malformed signature is `false`; a missing shared key throws. `SignatureFrom` reads the header in any case from ASP.NET Core's `Request.Headers`, `HttpRequestMessage.Headers`, a `NameValueCollection` or a dictionary | R19 (the signature step) | Reading the body as bytes before anything parses it; answering 200 fast; skipping a webhook id you have seen; re-reading the resource before you act (R20); a signature sent in the query string |
| `recipes/RequestLimit.cs` | At most four calls per site in flight in this process, first come first served; a waiting caller can be cancelled; a `Run` nested in a `Run` for the same site takes no second slot. `WithoutUnsafeRetries` turns off the SDK's automatic resend of a 429 and of a `PUT` | R10; R11 (automatic resends) | The pause of minutes after a 429; sharing the limit between processes; one request at a time inside a call. A slot is freed when a call ends, and after a client timeout that can be before Maxio has finished |

## The two client settings for automatic resends

Both are client settings, not per-call switches. They are on `MaxioAdvancedBillingClientOptions.Retry` (a
`RetryOptions` record), are fixed when the client is built, and apply to every call that client makes:
`RequestOptions` carries only `LogLevel` and `Hooks`. So "no automatic resend for this write" means
"send this write through a client built without it". `docs/configuration-resilience.md`, section "Maxio:
retries, timeouts and paging", shows a client built for writes, with both timeouts at 130 seconds.

- **No automatic resend of a 429** (R10): take 429 out of `Retry.StatusCodesToRetry`. By default the SDK
  sends a throttled `GET`, `HEAD`, `PUT` or `OPTIONS` four times within about 7 seconds. Without 429 it
  sends it once and throws an `ApiException` whose status is 429.
- **No automatic resend of a `PUT`** (R11): take `PUT` out of `Retry.HttpMethodsToRetry`. By default the
  SDK resends a `PUT` up to 3 times after a 408, 429, 500, 502, 503 or 504, a timeout or a dropped
  connection, and
  `RetrySubscription`, `ReactivateSubscription` and `ActivateSubscription` are `PUT`s that can take a
  payment. Without `PUT` each is sent once. `POST` and `DELETE` are never resent by default.

`RequestLimit.WithoutUnsafeRetries` does both and leaves only `GET`, `HEAD` and `OPTIONS` to be resent:

```csharp
options.Retry = RequestLimit.WithoutUnsafeRetries(options.Retry);
```

The tests count the requests that reach a fake Maxio with and without each change.

## Copying them in

- **Format.** One C# file per recipe, file-scoped namespace `MaxioRecipes` (rename it), static classes.
  Each file starts with `#nullable enable`, so it compiles the same whether your project has nullable
  reference types on or off. Every public member has an XML documentation comment.
- **Language version.** C# 10 or later (file-scoped namespaces). A project that targets .NET 6 or later
  gets that by default. A `netstandard2.0` or .NET Framework project defaults to C# 7.3 and has to set
  `LangVersion`.
- **Checked under**, on every run of `recipe-tests/dotnet` (see its README), for `netstandard2.0` (the
  framework the SDK targets) and `net10.0`:
  - C# 14, nullable on, implicit usings off, `GenerateDocumentationFile`, `AnalysisLevel`
    `latest-recommended`, warnings as errors;
  - C# 10, nullable off, implicit usings on, `GenerateDocumentationFile`, warnings as errors.
- **Stricter settings.** With `AnalysisMode` `All` the files build with three kinds of warning, which you
  can suppress or fix after you copy: CA1034 for the four result types nested in `SignupResult` (nested
  so that a caller has to name the case), CA1032 because `PageCeilingException` has no parameterless or
  message-only constructor, and CA1031 because `SafeSignup` catches every exception from the read-back on
  purpose: no read-back failure may replace an unknown outcome.
- **What they were tested against.** Every behaviour named in a header runs through the real SDK against a
  fake `HttpMessageHandler`, never against Maxio. The webhook digests were computed with OpenSSL and
  Python, and the RFC 4231 vectors are included.
