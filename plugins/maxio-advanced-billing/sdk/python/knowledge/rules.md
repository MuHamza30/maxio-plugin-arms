# Maxio Advanced Billing: rules for every integration

**Contents.** Read the sections you need, not the whole file.

- R1 · Call Maxio from your server only, with that site's API key
- R2 · The base URL picks the site, so make it configuration
- R3 · Read the site's invoicing architecture before choosing collection settings
- R4 · Money has two shapes: check the field name before you scale
- R5 · Dates are in the site's time zone
- R6 · Reference catalog objects by handle; never hard-code numeric ids
- R7 · Take each shape from the contract; expect nulls and new fields
- R8 · Page every list that takes paging; `per_page` over the cap is clamped silently
- R9 · Some filters fail open: verify what you asked for came back
- R10 · At most 4 requests in flight per subdomain; on 429 back off for minutes
- R11 · A write with no clear answer has an unknown outcome
- R12 · Duplicate prevention is a body token, not a header: one token per write
- R13 · A 4xx never proves that a call "works"
- R14 · Send the collection method on every signup, chosen by how the customer pays
- R15 · Card data reaches Maxio as a Maxio.js token
- R16 · Gate access on the full state model, not on a remembered list
- R17 · Archiving a catalog item does not stop billing it
- R18 · The UI's words are not the API's words
- R19 · Verify the signature over the raw body, answer 200 fast, and deduplicate
- R20 · Webhooks are hints: re-read the resource before acting on state

The API-wide rules. Each of the ten rules on the SDK map is the short form of an item here, in
`decisions.md` or in `lifecycles.md`: read a rule here when a ten-rule, an operation's provider line or
your task points at it. Each rule names what to do, what breaks if you don't, and where it comes from.
Rules that belong to one operation live in `operations/<page>.md`, and rules about order and choice
live in `lifecycles.md` and `decisions.md`.

Source tags: **[docs]** a Maxio documentation page · **[spec]** the OpenAPI spec · **[announcement]**
a dated Maxio announcement · **[observed]** seen in controlled agent runs against a Maxio sandbox.
*(inferred)* marks a consequence the sources imply but do not state. *(unconfirmed)* marks a point the
sources leave open or disagree on.

Rules name wire fields and operations, never SDK code. Where a rule needs something done in code, it
names the page and section of this SDK's `docs/` that says how.

---

## Connecting

### R1 · Call Maxio from your server only, with that site's API key
- **Do:** authenticate with HTTP Basic, the site's API key as the username and `x` as the password.
  Load the key from secret storage. Make every call server-side. `docs/getting-started.md`, section
  "Maxio: site and credentials", says how this SDK takes the key.
- **Exception:** the Sales Commission operations (`list_sales_commission_settings`, `list_sales_reps`,
  `read_sales_rep`) are seller-level. They take `Authorization: Bearer <a user's API key>`, not the
  site key, and the subdomain in their URL is `app`. The user needs financial access and the seller
  needs Advanced Analytics.
- **Breaks if not:** the key grants "full access to all of your Advanced Billing data", and the API has
  no CORS ("CORS cannot be enabled"), so browser calls fail and a shipped key is a full-account leak.
  Web-login credentials are not API credentials.
- **Source:** [docs] introduction/authentication · about-the-api/tips "Secure Applications" · [spec] BasicAuth, listSalesCommissionSettings "Modified Authentication Process", user-authorization

### R2 · The base URL picks the site, so make it configuration
- **Do:** read the subdomain and region from configuration: US `https://{subdomain}.chargify.com`, EU
  `https://{subdomain}.ebilling.maxio.com` (only for EU-hosted accounts). Set both explicitly and fail
  at startup when either is missing: the spec's placeholder for the subdomain is the literal word
  `subdomain`, so a client built without a site calls a site of that name (`docs/getting-started.md`,
  section "Maxio: site and credentials"). Keep test and live sites as separate configurations, and
  confirm `read_site` returns `test: true` before any destructive test.
- **Breaks if not:** calls reach another site's data, or fail auth because the key belongs to a
  different site or region *(inferred)*. Never commit a subdomain or key into tracked files [observed].
- **Source:** [spec] x-server-configuration (environments, `site` default) · [docs] basic-concepts/connected-sites

### R3 · Read the site's invoicing architecture before choosing collection settings
- **Do:** call `read_site` once per process and keep `relationship_invoicing_enabled` and
  `default_payment_collection_method`: at startup, or, where the code has no startup of its own (a
  library module), on first use, keeping the answer for later calls. Not on every signup: that adds a
  request and a point of failure to each one *(inferred)*. Relationship Invoicing sites accept
  `payment_collection_method` = `automatic`, `remittance` or `prepaid`; legacy Statements sites accept
  `automatic` or `invoice`.
  Some operations exist only on Relationship Invoicing sites (`activate_subscription`, proforma
  invoices).
- **Breaks if not:** a value valid on one site fails validation on another, and agents have written
  false claims that the architecture "cannot be known" [observed].
- **Seen live:** on one sandbox both `invoice` and `remittance` were accepted [observed, not reconciled
  with the spec's split]. Follow the split; do not rely on the lenient behaviour.
- **Source:** [spec] Collection-Method, Site, activateSubscription · [announcement] 2021-11-05 payment collection validation

---

## Data on the wire

### R4 · Money has two shapes: check the field name before you scale
- **Do:** `*_in_cents` fields are whole cents and can exceed 32 bits. Component `unit_price`, bracket
  `unit_price`, currency `price` and invoice totals are decimal major units, often strings, with up to
  8 decimals on unit prices. Do money arithmetic in a decimal type, never in binary floating point,
  and round only for display. Where the contract offers the same value as a string or a number, read
  the string; where it offers only a floating-point number, convert it to a decimal once, as you read
  it *(inferred)*.
- **Breaks if not:** 100× mispricing with no error. Agents have typed cents as 32-bit ints and divided
  by 100 twice [observed].
- **Source:** [docs] about-the-api/data-types "Decimal Numbers", "Amount Fields and Currency" · [spec] Product, Price, Invoice

### R5 · Dates are in the site's time zone
- **Do:** send instants with an explicit offset; keep date-only fields (`issue_date`, `due_date`) as
  plain dates. In a request, a date with no time means noon in the site's zone, and a datetime with no
  offset is read in the site's zone.
- **Exceptions:** list filters differ. A `start_date` filter starts at midnight and an `end_date`
  filter runs to 11:59:59 PM in the site's zone. On `list_credit_notes`, `start_datetime` and
  `end_datetime` with no offset are read as UTC; the other lists read them in the site's zone.
- **Breaks if not:** times shift by hours and dates by a day, and fixed offsets break across DST.
- **Source:** [docs] about-the-api/data-types "Dates and Time Zones" · [spec] listSubscriptions `start_date`, `end_date`; listCreditNotes `start_datetime`

### R6 · Reference catalog objects by handle; never hard-code numeric ids
- **Do:** give products, price points, components and families stable handles, and resolve them by
  handle (`product_handle`, or `handle:<handle>` where a path takes "id or handle"). Ids returned at
  runtime are fine to use within a flow. Store ids as 64-bit numbers or strings.
- **Handles are lowercase.** A component handle "Must start with a letter or number and may only
  contain lowercase letters, numbers, or the characters '.', ':', '-', or '_'". A component price
  point handle that is not lowercase letters, numbers, dashes and underscores with "at least one
  letter in it" is rejected with a 422 [spec]. Assume the same for products and families
  *(inferred)*.
- **Breaks if not:** numeric ids differ between sites *(inferred)*, and the test task the runs used
  said they are reassigned when a sandbox is re-seeded *(unconfirmed: stated by that task, not
  observed)*. "Most IDs are currently integers, but you should not assume that this will always be the
  case".
- **Source:** [spec] product-family-id-path, Create-Subscription `product_id`, Metered-Component `handle`, createComponentPricePoint 422 · [docs] about-the-api/versioning

### R7 · Take each shape from the contract; expect nulls and new fields
- **Do:** read each operation's request and response shape from the contract, one operation at a
  time. Most resources are wrapped in their resource name (`{"subscription": {...}}`) and many lists
  are arrays of such wrappers, but not all. `read_invoice`, `issue_invoice`, `void_invoice`,
  `refund_invoice`, `reopen_invoice` and `record_payment_for_invoice` return the invoice with no wrapper,
  while `create_invoice` and `update_invoice` wrap it in `invoice`. `list_invoices` puts its array under
  `invoices`, and some requests have no wrapper
  (`reactivate_subscription`, `record_event`). Treat `null` as a valid value wherever the contract
  allows it, which is many response fields. Accept unknown fields; Maxio adds attributes without
  notice.
- **Breaks if not:** one hand-written shape for every operation fails on the invoice family, and
  treating nulls as "protocol drift" turned valid answers into 502s in 5 of 11 runs [observed].
- **Seen live:** one legacy Statements site returned the invoice list as an array of `invoice`
  wrappers, not the `invoices` object the spec declares [observed, one site].
- **Source:** [spec] Invoice, List-Invoices-Response, Subscription-Response, Reactivate-Subscription-Request · [docs] about-the-api/versioning

---

## Reading lists

### R8 · Page every list that takes paging; `per_page` over the cap is clamped silently
- **Do:** where a list takes `page` and `per_page`, always pass `per_page`, start `page` at 1 and loop
  until a page comes back empty. The cap is 200 on most lists, 50 on `list_mrr_movements` and 10000 on
  the exported-row lists. For this SDK's stop rule see `docs/configuration-resilience.md`,
  section "Maxio: retries, timeouts and paging".
- **Not every list pages.** Nine lists take no `per_page`, among them `list_customer_subscriptions`,
  `list_subscription_components`, `list_product_families` and `list_endpoints`. The contract shows which
  parameters a list takes. Call a list that takes no `page` once: a loop over `page` would read the
  same rows again on every turn *(inferred)*. `list_allocations` takes `page` only: ask for the next
  `page` until one comes back empty *(inferred)*.
- **Breaks if not:** `per_page=500` returns 200 rows; a loop that stops when `count < per_page` ends
  after page one and truncates silently. Agents guessed the cap in 7 of 8 runs [observed].
- **Source:** [spec] page, per-page parameters · [docs] about-the-api/list-operations

### R9 · Some filters fail open: verify what you asked for came back
- **Do:** use only the documented `date_field` values for each list (an unrecognized one is ignored and
  the full set returns). Filter subscriptions by product id or exact name: "Product handle is not
  supported". On invoice-family lists, request each nested array you need (`line_items=true`, ...); they
  default to off. Price-point lists are newest first, so never take `[0]` as the default.
- **The `state` filter is not a state test.** On `list_subscriptions` the spec types it as one value
  per request [spec], while Maxio's tips page says it accepts a comma-separated list [docs]; send one
  value per call *(a comma list is unconfirmed)*. Its values also leave out `soft_failure`, `assessing`
  and `pending` [spec]. To find every subscription with access, list without it and classify each row
  by its own `state` (`lifecycles.md` L3).
- **Breaks if not:** an incremental sync or bulk action silently runs over every record; invoices look
  as if they had no lines or payments; the newest price point is used as the default; subscribers in
  `soft_failure` drop out of a "live" list.
- **Source:** [spec] listCreditNotes, listSubscriptions, Subscription-State-Filter, listInvoices · [docs] about-the-api/tips "Synchronizing Your Database" · [announcement] 2020-12-18 date_field, 2020-01-27 price point order

---

## Writing safely

### R10 · At most 4 requests in flight per subdomain; on 429 back off for minutes
- **Do:** share one concurrency limit of 4 per subdomain across all workers. On `429 Too Many
  Requests`, pause "a few minutes" and resume slower. A resend after a second or two is not that
  back-off: if the client resends a 429 by itself, turn that off and schedule the retry yourself
  (`docs/configuration-resilience.md`, section "Maxio: retries, timeouts and paging"). A write you send
  again after the pause carries its same `uniqueness_token` (R12). Never resend a write blindly (R11).
- **Exception:** a 429 from `read_billing_portal_link` is not this limit. It means the 15 requests allowed
  for that customer's link are used up: wait until `new_link_available_at`.
- **Breaks if not:** adding parallelism while throttled makes the wait longer. Runs that read this
  guidance still shipped no retry, mapped 429 to 400, or retried POSTs with no method guard [observed].
  No `Retry-After` header is documented *(unconfirmed)*.
- **Source:** [docs] about-the-api/error-handling "Rate Limits and Blocks" · [spec] readBillingPortalLink

### R11 · A write with no clear answer has an unknown outcome
- **Do:** Maxio works on a request for up to 120 s (the server cut-off, which includes the payment
  gateway). Give every write at least that long *(inferred from the cut-off)*. After a timeout, a
  dropped connection, a 5xx, a 408, a 2xx you cannot read, or a 409, the write may or may not have
  happened. Settle it in this order:
  1. **Read back:** by your own reference where the write set one; otherwise read the resource the
     write affects (the operation's notes name it). Found: settle from what Maxio holds.
  2. **Not found, and under 120 s since the first send:** wait until 120 s have passed, then read back
     again *(inferred: the first copy may still be running)*. Found: settle.
  3. **Still not found, and the write carried a `uniqueness_token`:** resend it with the **same** token
     (R12). Maxio's answers [docs]: 2xx, the first copy never arrived and this one is done; 422, the
     first never arrived and this one was rejected, so correct it and send it with a new token; 409,
     the first copy arrived, so read back again.
  4. **Still not found after a 409:**
     - The read-back is by a unique reference you set (`find_subscription`, `read_customer_by_reference`):
       the first copy created nothing. Start again with a new token *(inferred)*.
     - Usage (`create_usage`): list the usage already recorded for that component and period
       (`list_usages`, minding its date boundaries) and confirm whether the report landed before
       sending it again [docs].
     - Anything else (a payment, a prepayment, a refund, an invoice payment that may show
       `processing`): never send it again automatically. Settle it from webhooks or by hand [docs].
  5. **A write that cannot carry a token** (an operation with no request body, such as
     `retry_subscription` and `resume_subscription`): never resend it automatically, at any step. Read the
     resource back and settle it from that, from webhooks or by hand.

  Never report an unknown outcome as a failure.
- **Where the wait happens:** steps 2 and 3 can take two minutes. Hold a caller for them only when its
  contract allows a wait that long *(inferred)*. Otherwise answer "unknown" at once, carrying the
  reference and the token, and finish R11 later: from a background job, from the caller's next attempt
  at the same write, or from a webhook. A function that must answer at once answers "unknown", never
  "failed".
- **Writes that take payment:** HTTP calls `PUT` idempotent, but `retry_subscription`,
  `reactivate_subscription` and `activate_subscription` are `PUT`s that can take a payment, and so is
  `update_subscription` when it carries payment details for a past-due subscriber *(inferred from
  their descriptions)*. `verify_bank_account` is a `PUT` capped at 10 attempts. An automatic client-side
  resend of one of these can charge twice or use up the cap. Turn automatic retry off for them and
  allow at least 120 s: `docs/configuration-resilience.md`, section "Maxio: retries, timeouts and
  paging", says how. `uniqueness_token` is accepted on `PUT` as well [docs], so sending one makes a
  resend answer 409 instead of acting twice *(inferred; not probed)*. `retry_subscription` has no body
  and cannot carry one (step 5).
- **Breaks if not:** the card is charged, the client assumes failure and retries, and the customer pays
  twice. A resend while the first copy is still running is the true concurrency under which one run
  saw duplicates (R12). A new token after a 409 on a payment is a second charge that nothing can
  catch *(inferred)*.
- **Source:** [docs] about-the-api/error-handling "Timeout Limitation" · about-the-api/duplicate-prevention "Interpreting the Response to Your Retry", "Recovering When the Outcome Is Unknown" · [spec] retrySubscription, resumeSubscription, reactivateSubscription, activateSubscription, updatePaymentProfile, verifyBankAccount

### R12 · Duplicate prevention is a body token, not a header: one token per write
- **Do:** Maxio has no `Idempotency-Key` header. Its mechanism is `uniqueness_token`, accepted on any
  POST, PUT, PATCH or DELETE at the top level of the body: beside the resource object where there is
  one (`{"subscription": {...}, "uniqueness_token": "..."}`), never inside it. Where a body has no
  resource object, put it among the root fields *(inferred)*. An operation with no request body cannot
  carry it (R11 step 5).
  - **One token per write.** Mint a long random value once for that write, keep it on your own record
    of that write, and send it on every resend of that write. Replace the stored value only when you
    mint a new one: after a 422 you corrected, or at R11 step 4. A flow that makes several writes (a
    signup that creates a customer, then a subscription) gives each write its own token. Tokens are
    scoped to the site and the credentials, not to an endpoint *(inferred: the scope names none)*, so
    a second write sent with the first one's token answers 409.
  - A token is spent when a request is received, even if that request then fails validation. So a
    corrected request needs a new token, and a resend never does. What each answer to a resend means
    is R11 step 3; a 409 `DuplicatePrevention::DuplicateSubmissionError` means the first copy arrived
    and its outcome is unknown (R11).
  - After a 429, send the write again with the same token *(inferred: a 429 is not a rejection you
    corrected)*. If that answers 409, follow R11.
  - Tokens are kept for at least 60 minutes and are scoped to the site and to the API credentials
    that sent them. The window is a site setting, 1 to 12 hours, 1 hour by default [docs]. A replay
    later than that, or through another API key, is not caught. The lasting guard is your own record
    plus a deterministic `reference` you can look up.
  - Also serialize writes per customer in your own store: one run saw duplicates under true
    concurrency [observed, single run].
  - **When the caller's function has no place for a token** (a plan-change function that takes only the
    subscription and the product, which its caller may call again): the token still belongs to the
    write, not to the call. Mint it at the start
    of the call and send it on every resend within that call. Where the app has a store, keep it on a
    record of the request there, so a later call can resend it. Where the app has none, let the change
    itself guard a repeat: read the resource first, and send nothing when it already shows the change
    (the subscription is on the target product, or already has `cancel_at_end_of_period: true`). Never
    compute the token from the change, whether from the arguments or from what you read before the
    write (the current product, the period): a deliberate repeat, such as A to B, back to A, then to B
    again within the token window, computes the same token, answers 409 and never runs *(inferred)*.
    Say in your report that a repeat after an unknown outcome is guarded only by that read.
- **Events are different:** `record_event` and `bulk_record_events` take the token inside the event, as
  `chargify.uniqueness_token`. It is scoped per stream, at most 64 characters and kept 31 days, and a
  duplicate is silently ignored: no 409 [spec].
- **Breaks if not:** a fresh token on every attempt never draws a 409, so a resend after a timeout that
  reached Maxio creates a second subscription or charge. A corrected request sent with the old token
  gets the 409 and never runs, and so does a second write that reuses the first one's token. A 409
  never proves success. A token nested inside `subscription` looked "not honoured", and six concurrent
  subscribes produced three subscriptions [observed].
- **Not in the contract:** apart from events, the spec declares `uniqueness_token` on no request, so
  the contract does not show it. `docs/models.md`, section "Fields the spec does not declare", says how
  to send it at the body root with this SDK. Prove it reaches the wire with a test that captures the
  request.
- **Source:** [docs] about-the-api/duplicate-prevention, tips "Handling Retries Safely" · Maxio help "Configure uniqueness token settings" · [spec] Chargify-Ebb · [observed]

### R13 · A 4xx never proves that a call "works"
- **Do:** read the status and Maxio's own message before changing code, then find them in
  `failures.md` (this folder). `docs/error-handling.md`, section "Maxio: reading a rejection", says how
  to print both from this SDK's error. Error bodies differ between operations, so do not write one
  parser for all of them. What each status can mean:
  - **404** on a lookup by your own reference (`find_subscription` [spec], `read_customer_by_reference`
    [observed]) is the normal "not there" answer. After a write with an unknown outcome it means only
    "not there yet" until R11 has run its course.
  - **409** means a write carrying that `uniqueness_token` already arrived. Its outcome is unknown
    (R11, R12).
  - **422** may be an account block (account canceled, trial ended, site data being cleared, site
    deleted) that no change to the request fixes; a 3-D Secure challenge carrying an `action_link`
    (send the customer there; `docs/models.md`, section "Fields the spec does not declare", says how
    to read it); or a real validation error.

  Map provider errors deliberately: a validation reason about the caller's own data may be returned to
  that caller; raw response bodies, account-level messages and serializer exception text must not
  reach your callers (they did in 10 of 12 builds of one experiment [observed]).
- **Breaks if not:** agents tested with nonexistent data, got a 4xx and reported success [observed];
  repair loops retry account blocks forever; 3DS customers who could pay are turned away.
- **Source:** [docs] about-the-api/error-handling "API Access Limitations" · about-the-api/duplicate-prevention · [spec] createSubscription, createPaymentProfile, findSubscription

---

## Money movement and access

### R14 · Send the collection method on every signup, chosen by how the customer pays
- **Do:** send `payment_collection_method` explicitly on every signup. Omitted, the site's own
  `default_payment_collection_method` applies: the spec declares no default, and it was `automatic` on
  the test site [observed]. Choose by intent, and ask when the task does not say:
  - The customer pays by card or bank: `automatic` plus a payment source (`decisions.md` D2).
  - The merchant bills by invoice: `remittance` on Relationship Invoicing sites, `invoice` on legacy
    Statements sites (R3). The customer is not charged automatically; the payment is recorded when it
    arrives [docs]. That the subscription starts active with an open invoice for any amount due is
    *(inferred)*.
  - Nothing is due at signup (a trial, a free plan): `automatic` with no payment source *(inferred)*.
    What happens when the trial ends is `lifecycles.md` L4.

  "No card required" on the plan does not settle this: it describes the plan, not the signup.
- **Breaks if not:** under `automatic`, a signup that owes money at creation and has no payment source
  fails with `422 "No payment method was on file for the $X balance"` [observed], which never names
  the field. This was the most common failure across every knowledge source tested, including runs
  that had the field's enum in context [observed]. Switching a card-paying plan to an invoice method
  makes the 422 go away and leaves an active subscription that nothing collects: never do it to clear
  the error.
- **Source:** [spec] Collection-Method, Site `default_payment_collection_method` · [docs] basic-concepts/subscription-signup "API", "Payment Methods" · [observed]

### R15 · Card data reaches Maxio as a Maxio.js token
- **Do:** unless the merchant is PCI compliant, tokenize cards and bank details in the browser with
  Maxio.js (formerly Chargify.js) and send only the `chargify_token` (`tok_...`) from your server.
- **Security token:** sellers created since 2023-05-16 have the Maxio.js security token on by default,
  and only Maxio support can change that [announcement]. With it on, the form takes payment details
  only with a valid security token, which your site generates from a secret it shares with Maxio.js
  [docs]. `list_chargify_js_public_keys` shows `requires_security_token` for each key [spec]. How to build
  the token is not in the spec or the portal docs *(unconfirmed)*: take it from Maxio's Maxio.js
  reference and do not guess its format.
- **Breaks if not:** card numbers pass through your servers and logs, which puts the merchant in PCI
  scope. A form that sends no security token on a site that requires one cannot tokenize *(inferred)*.
- **Source:** [docs] basic-concepts/subscription-signup "API" · Maxio help "Prevent card testing abuse with Maxio.js" · [spec] createSubscription, createPaymentProfile, Public-Key · [announcement] 2023-05-16 security token

### R16 · Gate access on the full state model, not on a remembered list
- **Do:** take subscription states from `lifecycles.md` L3.
  - Access is on in `active`, `trialing`, `past_due` and `soft_failure`.
  - `pending` and `assessing` are transient: keep the previous access decision. L3 says how to count
    them where there is no previous decision.
  - Not billing but coming back: `on_hold` (resumes), `suspended` (a prepayment restores it), `unpaid`
    and `awaiting_signup`. No access, and never create a second subscription to the same plan beside
    one of these: use that one (`decisions.md` D12 says how to bring one back). A different plan for
    the same customer is allowed (D1). When it is unclear whether the user wants this one back or
    another plan beside it, ask.
  - Ended, leaving room for a new signup or a reactivation: `canceled`, `expired`, `trial_ended` and
    `failed_to_create`.

  Maxio's schema lists `canceled`, `expired`, `failed_to_create`, `on_hold`, `suspended` and
  `trial_ended` as "End of Life". Read that as End of Life (not billing): two of the six come back. A
  paused subscription is `on_hold`; `paused` is an internal state no API call produces *(inferred)*.
- **Breaks if not:** five runs across two knowledge sources wrote the ended set from memory as
  `canceled`, `expired`, `failed_to_create`, `trial_ended` [observed]. An "already subscribed" check
  built on that set lets a customer who is on hold or suspended sign up again, and bills them twice
  when the first subscription returns *(inferred)*. Code that expects `paused` breaks the resume flow
  [observed].
- **Source:** [spec] Subscription-State · [docs] basic-concepts/entitlements · [observed]

### R17 · Archiving a catalog item does not stop billing it
- **Do:** treat DELETE on a product, component, coupon or price point as "stop selling", not "stop
  charging". Move or migrate existing subscriptions yourself. There is no API unarchive for products,
  components, coupons or families.
- **Breaks if not:** customers keep paying for an item the integration believes is gone.
- **Source:** [spec] archiveProduct, archiveComponent, archiveCoupon, archiveProductPricePoint

### R18 · The UI's words are not the API's words
- **Do:** on the new Catalog experience, a UI **Plan** is an API **product** and a UI **Product** is an
  API **component**. Confirm which one the user means before choosing operations (`decisions.md` D20).
- **Breaks if not:** "add a product to the subscription" is built as a plan migration instead of a
  component allocation, or the reverse.
- **Source:** [announcement] 2026 "NEW Catalog Experience and Terminology"

---

## Webhooks

### R19 · Verify the signature over the raw body, answer 200 fast, and deduplicate
- **Do:** compute hex `HMAC-SHA256(site shared key, raw request body)` and compare it, in constant time,
  with header `X-Chargify-Webhook-Signature-Hmac-Sha-256`, before parsing. Bodies are
  `application/x-www-form-urlencoded` with bracket keys (`payload[subscription][id]=...`), not JSON.
  Return exactly `200 OK` within about 15 s and do the work afterwards, including for events you do not
  handle. Skip any webhook `id` you have already processed. Load the shared key at startup and fail
  there when it is missing *(inferred)*: a receiver that rejects every webhook runs up the failure
  count. Where the code has no startup of its own (a library function), raise a configuration error
  on the call. Never answer "not genuine" for a missing key: that rejects every webhook in silence.
- **Breaks if not:** hashing a re-encoded body never matches; non-200 replies are retried; from a
  failure count of 26 new webhooks are created paused, and from 51 the endpoint is disabled and
  "Webhooks are no longer generated" (`lifecycles.md` L7).
- **Source:** [docs] webhooks "Verifying Events", "Responding to a Webhook", "Inoperative Endpoints"

### R20 · Webhooks are hints: re-read the resource before acting on state
- **Do:** expect several events per action, reordering on retry, and missing values. Re-read the
  subscription (compare `updated_at`) before changing access. For ACH and Direct Debit, `payment_success`
  means "did not fail immediately". Before irreversible fulfilment wait for the event that reports the
  final result: `direct_debit_payment_paid_out` or `direct_debit_payment_rejected` (Stripe and
  GoCardless only), `pending_payment_completed` or `pending_payment_failed` *(which event to wait for
  is inferred)*.
- **Renamed events:** on sites with the new Catalog experience, Maxio's webhook reference lists
  `subscription_product_change` as `subscription_plan_change`, `component_allocation_change` as
  `allocation_change` and `component_billing_date_change` as `product_billing_date_change` [docs]. The
  endpoint's subscription list still holds only the old names [spec]. Accept both spellings in a
  receiver *(unconfirmed which one is sent)*, and subscribe an endpoint only with names from the
  contract.
- **Breaks if not:** a stale event overwrites newer state; goods ship for payments that later bounce;
  handlers keyed on one spelling silently skip events.
- **Source:** [docs] webhooks "Best Practices", webhooks-reference (intro, `payment_success`) · [spec] Webhook-Subscription
