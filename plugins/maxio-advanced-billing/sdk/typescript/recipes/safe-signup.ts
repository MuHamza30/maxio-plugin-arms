/*
 * safe-signup: create one subscription, and never a second one because an answer was lost.
 *
 * What one call does
 *   1. Looks the subscription up by `reference`. Found: returns `existing` and sends nothing more.
 *      If this lookup fails, its error is thrown and nothing was sent. On a repeat call that leaves
 *      the signup where the previous result left it.
 *   2. Sends the create once, with `uniqueness_token` at the top level of the body beside
 *      `subscription`. The call sets `maxRetries: 0`, so the SDK never sends it again whatever the
 *      client's retry policy. It allows 130 seconds for the answer to start, so that Maxio's own
 *      120 second cut-off answers first, and 150 seconds in all (the SDK's timeout stops at the
 *      response headers and does not cover reading the body).
 *   3. A 2xx with a subscription in the body: returns `created`.
 *   4. A 4xx other than 408 and 409: Maxio rejected the request. The SDK's own error is rethrown
 *      unchanged (docs/error-handling.md, "Maxio: reading a rejection", shows how to read it).
 *      A 429 is rethrown too, but it is not a fault in the request: pause for minutes
 *      (knowledge/rules.md R10), then call again with the same token.
 *   5. A 409: a request with this token arrived before. The 409 does not say how that one ended.
 *   6. A timeout, a dropped connection, a 5xx, a 408, any other status outside 2xx and 4xx, a 2xx
 *      that cannot be read, or a cancellation once the create was sent: the outcome is not known.
 *      Any other error is rethrown as it is: a value the SDK would not encode, a credential it
 *      could not obtain, or a fault in your own code. In the first two nothing was sent.
 *   7. After 5 or 6 it reads back by `reference`. Found: returns `recovered`. Not found, or the
 *      read-back itself failed: returns `unknown`. A failed read-back never replaces the unknown
 *      outcome: the result carries both causes.
 *   It does not send the create a second time. Calling it again with the same input is the resend.
 *
 * What you must supply
 *   - `reference`: the subscription's reference, built from your own data so that the same signup
 *     always gives the same value. Never random: it is how a lost signup is found again.
 *   - `uniquenessToken`: a long random value (a UUID will do). Mint it once for one signup, store
 *     it with your own record of that signup before you call, and pass the same value on every
 *     call for that signup. Mint a new one only after Maxio rejected the request (step 4, not a 429)
 *     and you corrected it, or once the first attempt is known to have failed (see `unknown` below).
 *     This recipe never mints one. A new token on a resend switches the protection off.
 *   - `paymentCollectionMethod`: required here, with no default (knowledge/rules.md R14 and
 *     knowledge/decisions.md D3 say which value). Left out, Maxio applies the site's own default.
 *   - `subscription`: the rest of the create body. It must name the customer in exactly one way
 *     (`customerId`, `customerReference` or `customerAttributes`; knowledge/decisions.md D1) and
 *     the product. The compiler checks the one-customer rule. Nothing checks it at run time.
 *
 * The result is a value you must branch on
 *   - `created`: this call created the subscription.
 *   - `existing`: it was there before this call sent anything. On a repeat call after `unknown`
 *     that means your earlier attempt went through. On a first call it means the reference was
 *     used before, so read `standing`.
 *   - `recovered`: found by the read-back after an outcome that was not known.
 *   - `unknown`: the subscription may or may not exist. Do not report a failure, and do not mint a
 *     new token. Wait until 120 seconds have passed since the first send (Maxio may still be
 *     working on it), then call again with the same input. That call returns `existing` if the
 *     subscription has appeared. Otherwise it sends the create again with the same token:
 *     `created` means no earlier copy had arrived, and a 409 (`recovered`, or `unknown` with
 *     `firstCopyArrived: true`) means one had. Keep the time of every send. The signup has failed
 *     only when a call returns `unknown` with `firstCopyArrived: true` and no `readBackFailure`, and
 *     every earlier send for it is more than 120 seconds old: Maxio has finished with them all and
 *     holds nothing under the reference. Then mint a new token and start again.
 *   `existing` and `recovered` carry `standing` (recipes/subscription-state.ts), because a
 *   subscription found by reference is not always a signup that worked:
 *     live         subscribed, with access. The signup is done.
 *     transient    it exists and Maxio is still working on it. Do not create another. Read it
 *                  again before you confirm anything to the user.
 *     recoverable  it exists, is not billing, and comes back (on hold, suspended, unpaid, awaiting
 *                  signup). Do not sign up again beside it. Resume it or collect on it.
 *     ended        canceled, expired, trial ended or failed to create. This is not a signup. Bring
 *                  it back with a reactivation, or sign up again under a new reference with a new
 *                  token.
 *     unclassified it exists, with no state or one this SDK version does not name. Do not create
 *                  another. Read it again and decide by hand.
 *
 * Cancelling
 *   `options.signal` cancels the first lookup and stops the wait for the create. Once the create
 *   was sent, cancelling cannot undo it, so the call does not reject: it reads back on its own
 *   timer (30 seconds unless you set `readBackTimeoutMs`), which your signal does not stop, and
 *   returns `recovered` or `unknown`. Do not give this call a deadline shorter than 120 seconds:
 *   a shorter one only turns answers Maxio was about to give into `unknown`.
 *
 * What it does not do
 *   - It does not stop two signups for one customer that run at the same time. Two calls with the
 *     same reference and different tokens both find nothing, both create, and the customer has two
 *     subscriptions. Claim the signup in your own store first (one row per reference, holding the
 *     token) so that only one call runs.
 *   - It does not look the customer up by itself. Call `findCustomer` (below) before every signup,
 *     and name the customer by what it answers: `customerAttributes` for a customer who already
 *     exists creates a second customer (knowledge/decisions.md D1). When it finds one, call
 *     `findHeldSubscription` (below) too: this call looks only at its own reference, and a customer
 *     who already holds the plan under another reference gets a second subscription beside it.
 *   - It does not choose the collection method or the payment source (knowledge/decisions.md D2
 *     and D3).
 *   - It does not wait and try again. That is the caller's loop, described under `unknown`.
 *
 * Implements knowledge/rules.md R11 and R12, and steps 6 and 7 of knowledge/lifecycles.md L2.
 * `findCustomer` is step 4, and `findHeldSubscription` the part of step 6 about the customer's other
 * subscriptions.
 *
 * Needs the SDK and recipes/subscription-state.ts: copy that file beside this one. Not part of
 * the SDK's API.
 */
import {
  ConnectionError,
  ResponseError,
  SortingDirection,
  SubscriptionSort,
  TimeoutError,
  type CollectionMethod,
  type CreateSubscription,
  type CreateSubscriptionRequest,
  type Customer,
  type CustomerAttributes,
  type MaxioAdvancedBillingClient,
  type Subscription,
  type SubscriptionResponse,
} from "maxio-advanced-billing";
import { standing, type Standing } from "./subscription-state.js";

/**
 * How long the create may wait for the response to start. Above Maxio's 120 second cut-off, so
 * that Maxio answers first.
 */
export const CREATE_TIMEOUT_MS = 130_000;

/** How long the create may take in all, reading the response body included. */
export const CREATE_DEADLINE_MS = 150_000;

/** How long the read-back after an unknown outcome may take, retries included. */
export const READ_BACK_TIMEOUT_MS = 30_000;

/** Exactly one way to name the customer (knowledge/decisions.md D1). */
export type CustomerSource =
  | { customerId: number; customerReference?: never; customerAttributes?: never }
  | { customerReference: string; customerId?: never; customerAttributes?: never }
  | { customerAttributes: CustomerAttributes; customerId?: never; customerReference?: never };

export type SignupInput = {
  /** The subscription's reference: the same value every time for the same signup, never random. */
  reference: string;
  /** Minted by you, once per signup, stored with your record of it, and reused on every call. */
  uniquenessToken: string;
  /** Sent on every signup. There is no default here. */
  paymentCollectionMethod: CollectionMethod;
  /** The rest of the create body: one customer source, the product, a payment source or none. */
  subscription: Omit<
    CreateSubscription,
    "reference" | "paymentCollectionMethod" | "customerId" | "customerReference" | "customerAttributes"
  > &
    CustomerSource;
};

export type SignupOptions = {
  /** Cancels the call. Once the create was sent the call still reads back and returns a result. */
  signal?: AbortSignal | undefined;
  /** Milliseconds the read-back may take. Default {@link READ_BACK_TIMEOUT_MS}. */
  readBackTimeoutMs?: number | undefined;
};

export type SignupResult =
  | { status: "created"; subscription: Subscription }
  | { status: "existing"; subscription: Subscription; standing: Standing }
  | {
      status: "recovered";
      subscription: Subscription;
      standing: Standing;
      /** Why the create's outcome was not known. */
      createFailure: unknown;
    }
  | {
      status: "unknown";
      /** True after a 409: Maxio has received a request with this token. */
      firstCopyArrived: boolean;
      /** Why the create's outcome was not known. */
      createFailure: unknown;
      /** Set when the read-back itself failed. Absent when it answered "not found". */
      readBackFailure?: unknown;
    };

/** What a failed create means: `rethrow`, `arrived` (a 409), or `unknown`. */
type CreateFailure = "rethrow" | "arrived" | "unknown";

function classify(err: unknown, sendSignal: AbortSignal): CreateFailure {
  // Maxio answered. Both arms of ResponseError carry the status: an error status, and a body that
  // could not be read.
  if (err instanceof ResponseError) {
    if (err.status === 409) return "arrived";
    if (err.status === 408) return "unknown";
    if (err.status >= 400 && err.status <= 499) return "rethrow"; // a definite rejection
    return "unknown"; // a 5xx, a 2xx whose body could not be read, or a 1xx or 3xx
  }
  if (err instanceof TimeoutError || err instanceof ConnectionError) return "unknown";
  // The caller's cancellation, or this recipe's own deadline. The SDK rejects with the reason.
  if (sendSignal.aborted) return "unknown";
  // Outside the unknown set: an EncodeError or AuthError (nothing was sent), or a bug.
  return "rethrow";
}

/** The subscription that has `reference`, or `undefined` when Maxio says there is none. */
async function findByReference(
  client: MaxioAdvancedBillingClient,
  reference: string,
  signal: AbortSignal | undefined,
): Promise<Subscription | undefined> {
  let answer: SubscriptionResponse;
  try {
    answer = await client.subscriptions.findSubscription({ reference }, { signal });
  } catch (err) {
    // ResponseError and not ApiError: the SDK declares this 404 with no body, so a 404 that carries
    // one arrives as a DecodeError whose `status` is still 404.
    if (err instanceof ResponseError && err.status === 404) return undefined;
    throw err;
  }
  // A 200 with no subscription in it cannot be read. It is not a miss.
  if (answer.subscription === undefined) {
    throw new Error("findSubscription answered without a subscription in the body.");
  }
  return answer.subscription;
}

type ReadBack =
  | { outcome: "found"; subscription: Subscription }
  | { outcome: "missing" }
  | { outcome: "failed"; cause: unknown };

/** Reads back on its own timer. The caller's signal is not used here on purpose. */
async function readBack(
  client: MaxioAdvancedBillingClient,
  reference: string,
  timeoutMs: number,
): Promise<ReadBack> {
  const deadline = new AbortController();
  const timer = setTimeout(
    () => deadline.abort(new Error(`The read-back by reference did not finish within ${timeoutMs} ms.`)),
    timeoutMs,
  );
  try {
    const subscription = await findByReference(client, reference, deadline.signal);
    return subscription === undefined ? { outcome: "missing" } : { outcome: "found", subscription };
  } catch (err) {
    return { outcome: "failed", cause: err };
  } finally {
    clearTimeout(timer);
  }
}

/**
 * The customer that has `reference`, your own user id, or `undefined` when Maxio says there is none
 * (knowledge/lifecycles.md L2 step 4). Call it before every signup, one for a "new" customer too: a
 * resend after a lost answer meets the customer the first attempt created.
 *   - Found: pass it, with the signup's reference, to `findHeldSubscription` before you sign it up
 *     again (L2 step 6), then name the customer with `customerReference: reference`.
 *   - `undefined`: send `customerAttributes` with `reference` in it, so the new customer has it.
 * Only a 404 is "not there". Any other failure is thrown: "could not look it up" read as "does not
 * exist" turns an outage into a second customer. It sends no write.
 */
export async function findCustomer(
  client: MaxioAdvancedBillingClient,
  reference: string,
  options: { signal?: AbortSignal | undefined } = {},
): Promise<Customer | undefined> {
  if (typeof reference !== "string" || reference.trim() === "") {
    throw new TypeError("findCustomer: reference must be a non-empty string.");
  }
  try {
    const answer = await client.customers.readCustomerByReference({ reference }, { signal: options.signal });
    return answer.customer;
  } catch (err) {
    // ResponseError covers a 404 whether or not it carries a body the SDK can read.
    if (err instanceof ResponseError && err.status === 404) return undefined;
    throw err;
  }
}

/** The most pages of one customer's subscriptions `findHeldSubscription` reads before it gives up. */
export const HELD_MAX_PAGES = 50;

/**
 * A subscription that `customer` already holds on `productHandle` and that leaves no room for a
 * second one beside it, or `undefined` (knowledge/lifecycles.md L2 step 6 and the fourth column of
 * L3; knowledge/rules.md R16). Call it with what `findCustomer` found, before you sign that customer
 * up again: a customer the task calls "new" can be one who already holds the plan. Pass this signup's
 * own `reference` too. A subscription carrying it is this signup's earlier attempt, not a second plan:
 * it is skipped here, and `safeSignup` finds it by that reference and returns `existing`.
 *   - Found: do not create. Its standing (recipes/subscription-state.ts) says what to tell the user:
 *     `live`, the customer already has the plan; `transient`, Maxio is still working on it, so read it
 *     again; `recoverable`, resume it or collect on it; `unclassified`, decide by hand.
 *   - `undefined`: nothing on this plan blocks a signup. An `ended` one (canceled, expired, trial
 *     ended, failed to create) does not: sign up again, or bring a canceled or trial-ended one back
 *     with a reactivation if that is what the user wants (knowledge/decisions.md D12).
 * It pages `listSubscriptions` filtered by `customer_id`, 200 a page in id order, until a page comes
 * back empty (knowledge/rules.md R8); `listCustomerSubscriptions` declares no paging. It matches the
 * product by `product.handle`, so a subscription with no product (new-Catalog sites) is not matched.
 * Any failure is thrown, never read as "nothing held", and so is a row with no subscription in it.
 * It sends no write.
 */
export async function findHeldSubscription(
  client: MaxioAdvancedBillingClient,
  customer: Pick<Customer, "id">,
  productHandle: string,
  signupReference: string,
  options: { signal?: AbortSignal | undefined } = {},
): Promise<Subscription | undefined> {
  const customerId = customer?.id;
  if (customerId === undefined || !Number.isSafeInteger(customerId) || customerId <= 0) {
    throw new TypeError("findHeldSubscription: the customer has no id; pass what findCustomer returned.");
  }
  if (typeof productHandle !== "string" || productHandle.trim() === "") {
    throw new TypeError("findHeldSubscription: productHandle must be a non-empty string.");
  }
  if (typeof signupReference !== "string" || signupReference.trim() === "") {
    throw new TypeError("findHeldSubscription: signupReference must be this signup's reference.");
  }
  for (let page = 1; page <= HELD_MAX_PAGES; page++) {
    const rows = await client.subscriptions.listSubscriptions(
      { customerId, page, perPage: 200, sort: SubscriptionSort.Id, direction: SortingDirection.Asc },
      { signal: options.signal },
    );
    if (rows.length === 0) return undefined;
    for (const row of rows) {
      const subscription = row.subscription;
      if (subscription === undefined) {
        throw new Error("listSubscriptions answered with a row that has no subscription in it.");
      }
      if (subscription.product?.handle !== productHandle) continue;
      if (subscription.reference === signupReference) continue; // this signup itself: safeSignup's to report
      if (standing(subscription.state) !== "ended") return subscription;
    }
  }
  throw new Error(
    `findHeldSubscription: customer ${customerId} has more than ${HELD_MAX_PAGES} pages of subscriptions; check by hand.`,
  );
}

function requireText(name: string, value: unknown): void {
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(`safeSignup: ${name} must be a non-empty string.`);
  }
}

export async function safeSignup(
  client: MaxioAdvancedBillingClient,
  input: SignupInput,
  options: SignupOptions = {},
): Promise<SignupResult> {
  requireText("reference", input.reference);
  requireText("uniquenessToken", input.uniquenessToken);
  requireText("paymentCollectionMethod", input.paymentCollectionMethod);
  const readBackTimeoutMs = options.readBackTimeoutMs ?? READ_BACK_TIMEOUT_MS;
  if (!Number.isInteger(readBackTimeoutMs) || readBackTimeoutMs < 1) {
    throw new RangeError("safeSignup: readBackTimeoutMs must be an integer of 1 or more.");
  }
  const { signal } = options;

  // 1. Nothing has been sent yet, so a failure here is a plain failure.
  const before = await findByReference(client, input.reference, signal);
  if (before !== undefined) {
    return { status: "existing", subscription: before, standing: standing(before.state) };
  }

  // The spec declares `uniqueness_token` on no model, so it is spelled as the wire key. The SDK
  // sends keys a model does not declare, and it must sit beside `subscription`, never inside it.
  // The header the SDK adds by itself, `Idempotency-Key`, means nothing to Maxio.
  const body: CreateSubscriptionRequest & { uniqueness_token: string } = {
    subscription: {
      ...input.subscription,
      reference: input.reference,
      paymentCollectionMethod: input.paymentCollectionMethod,
    },
    uniqueness_token: input.uniquenessToken,
  };

  // Last point at which cancelling means "not sent".
  signal?.throwIfAborted();

  // The SDK's timeout ends when the response headers arrive. This deadline also covers the body.
  const deadline = new AbortController();
  const timer = setTimeout(
    () => deadline.abort(new Error(`createSubscription did not finish within ${CREATE_DEADLINE_MS} ms.`)),
    CREATE_DEADLINE_MS,
  );
  const sendSignal = signal === undefined ? deadline.signal : AbortSignal.any([signal, deadline.signal]);

  let firstCopyArrived = false;
  let createFailure: unknown;
  try {
    // 2. One send, whatever retry policy the client was built with.
    const answer = await client.subscriptions.createSubscription(
      { body },
      { retry: { maxRetries: 0, timeout: CREATE_TIMEOUT_MS }, signal: sendSignal },
    );
    // 3.
    if (answer.subscription !== undefined) return { status: "created", subscription: answer.subscription };
    createFailure = new Error("createSubscription answered 2xx without a subscription in the body.");
  } catch (err) {
    const failure = classify(err, sendSignal);
    if (failure === "rethrow") throw err; // 4.
    firstCopyArrived = failure === "arrived"; // 5.
    createFailure = err; // 6.
  } finally {
    clearTimeout(timer);
  }

  // 7. Never resend here. What Maxio holds under the reference decides.
  const back = await readBack(client, input.reference, readBackTimeoutMs);
  switch (back.outcome) {
    case "found":
      return {
        status: "recovered",
        subscription: back.subscription,
        standing: standing(back.subscription.state),
        createFailure,
      };
    case "missing":
      return { status: "unknown", firstCopyArrived, createFailure };
    case "failed":
      return { status: "unknown", firstCopyArrived, createFailure, readBackFailure: back.cause };
  }
}
