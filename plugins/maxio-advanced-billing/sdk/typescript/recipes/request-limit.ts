/*
 * request-limit: keep at most four Maxio requests in flight for one site, first come first served.
 *
 * What it does
 *   `gateForSite(site).run(() => client.subscriptions.readSubscription({ subscriptionId }))` starts
 *   the call when one of four slots is free, and frees the slot when the call's promise settles,
 *   resolved or rejected. A caller that finds no free slot waits, and waiters start in the order
 *   they arrived.
 *
 * What the limit covers, exactly
 *   - Slots are counted here, on the client, in this one process. Maxio counts for itself, per
 *     subdomain, across every process and server that calls it. Two workers that each use this
 *     gate can put eight requests in flight. Give each worker a share (`new RequestGate(2)`), or
 *     send every Maxio call through one process.
 *   - Only calls made through `run` are counted.
 *   - A slot is freed when the call returns or fails. After a client timeout or a dropped
 *     connection that can be before Maxio has finished the request, so for a while Maxio may be
 *     working on more than four of yours.
 *   - A resend the SDK makes by itself happens inside the gated call and keeps its slot while it
 *     waits, so it adds no request in flight.
 *   - Nothing here pauses after a 429. That pause is yours to make (see below).
 *
 * Nested use is refused
 *   Calling `run` on a gate from inside a call that same gate is running rejects with
 *   `NestedGateUse`, at once and every time. Allowed, it would hang under load: four outer calls,
 *   each waiting for an inner one, hold every slot and none can finish. So wrap each SDK call, or
 *   wrap as a whole one helper that makes its calls one after another (recipes/list-all.ts,
 *   recipes/safe-signup.ts). Never both.
 *
 * Cancelling a waiter
 *   `run(call, { signal })` rejects with the signal's `reason` if the signal aborts while the call
 *   is still waiting for a slot. The call then never starts and no slot is used. Once the call has
 *   started, the signal no longer stops it here: pass the same signal to the SDK call for that.
 *   Without a signal a waiter waits as long as it takes. `AbortSignal.timeout(ms)` bounds the wait.
 *
 * The SDK's own resends, and the options that stop them
 *   By default the SDK sends a GET, HEAD, PUT or OPTIONS again, up to 3 times, after about 1, 2 and
 *   4 seconds, when it answers 408, 429, 500, 502, 503 or 504, times out, or loses its connection.
 *   A POST, PATCH or DELETE is sent once. Two parts of that are wrong for Maxio:
 *   1. A 429. Maxio asks for a pause of a few minutes (knowledge/rules.md R10). The SDK resends
 *      within seconds. Stop it on the client:
 *        `retry: { statusCodesToRetry: [408, 500, 502, 503, 504] }`  (the default list without 429)
 *      A 429 then rejects at once, as an error whose `status` is 429, and the pause is yours.
 *   2. A PUT that can take a payment or use up an attempt (knowledge/rules.md R11):
 *      retrySubscription, reactivateSubscription, activateSubscription, updateSubscription when it
 *      carries payment details, and verifyBankAccount. A resend can charge twice. Stop it for one
 *      call by passing `ONE_SEND` as the call's second argument:
 *        `client.subscriptionStatus.retrySubscription({ subscriptionId }, ONE_SEND)`
 *      which is `{ retry: { maxRetries: 0, timeout: 130_000 } }`: one send, and 130 seconds so that
 *      Maxio's own 120 second cut-off answers first. A timeout on such a call is an unknown
 *      outcome, never a failure. Or stop it for every PUT, on the client:
 *        `retry: { httpMethodsToRetry: ["GET", "HEAD", "OPTIONS"] }`  (the default list without PUT)
 *   `maxioRetryOptions()` gives both client options together, and keeps every other default:
 *        `new MaxioAdvancedBillingClient({ ...yourOptions, retry: maxioRetryOptions() })`
 *   Pass it the retry options you already have, and it keeps them but takes out 429 and every
 *   method except GET, HEAD and OPTIONS. The SDK's own comment on `httpMethodsToRetry` says its
 *   `Idempotency-Key` header makes a resend of any method safe. Maxio ignores that header, so a
 *   POST, PATCH or DELETE is taken out as well.
 *
 * Implements knowledge/rules.md R10 (the limit of four) and gives the options R10 and R11 need.
 *
 * Leaves to the caller: pausing new work for minutes once a 429 reaches you, sharing the limit
 * between processes, and routing every Maxio call through the gate.
 *
 * Needs the SDK (for two types only) and Node's standard library (`node:async_hooks`). Copy into
 * your project and adapt. Not part of the SDK's API.
 */
import { AsyncLocalStorage } from "node:async_hooks";
import type { HttpMethod, RequestOptions, RetryOptions } from "maxio-advanced-billing";

/** Maxio's limit on concurrent requests per subdomain. */
export const MAX_IN_FLIGHT_PER_SITE = 4;

// The SDK's defaults (src/core/retry.ts). It does not export them.
const SDK_DEFAULT_STATUSES: readonly number[] = [408, 429, 500, 502, 503, 504];
const SDK_DEFAULT_METHODS: readonly HttpMethod[] = ["GET", "HEAD", "PUT", "OPTIONS"];
const READ_METHODS: readonly HttpMethod[] = ["GET", "HEAD", "OPTIONS"];

/**
 * `ClientOptions.retry` for Maxio: `base` (the SDK's defaults when it is left out) with 429 taken
 * out of the statuses that are retried, and every method but GET, HEAD and OPTIONS taken out of the
 * methods that are retried. Every other setting is kept, so with no `base` a GET is still retried
 * on 408, 500, 502, 503 and 504, on a timeout and on a lost connection.
 */
export function maxioRetryOptions(base: RetryOptions = {}): RetryOptions {
  return {
    ...base,
    statusCodesToRetry: (base.statusCodesToRetry ?? SDK_DEFAULT_STATUSES).filter((status) => status !== 429),
    httpMethodsToRetry: (base.httpMethodsToRetry ?? SDK_DEFAULT_METHODS).filter((method) =>
      READ_METHODS.includes(method),
    ),
  };
}

/**
 * Per-call options for a write that may take a payment: one send, whatever the client's retry
 * policy, and 130 seconds for it. Pass it as the second argument of the call.
 */
export const ONE_SEND: RequestOptions = { retry: { maxRetries: 0, timeout: 130_000 } };

/** `run` was called on a gate from inside a call that gate is already running. */
export class NestedGateUse extends Error {
  constructor() {
    super(
      "RequestGate.run was called from inside a call this gate is already running. " +
        "Wrap each SDK call, or one sequential helper as a whole, never both.",
    );
    this.name = "NestedGateUse";
  }
}

export type RunOptions = {
  /** Stops the wait for a slot. It does not stop a call that has started. */
  signal?: AbortSignal | undefined;
};

type Waiter = { admit: () => void };

export class RequestGate {
  readonly limit: number;
  #inFlight = 0;
  readonly #waiting: Waiter[] = [];
  // Marks the async context of a call this gate is running, so nested use can be told apart.
  readonly #running = new AsyncLocalStorage<{ settled: boolean }>();

  /** @param limit Slots, from 1 to 4. Below 4 when several processes share one site. */
  constructor(limit: number = MAX_IN_FLIGHT_PER_SITE) {
    if (!Number.isInteger(limit) || limit < 1 || limit > MAX_IN_FLIGHT_PER_SITE) {
      throw new RangeError(`limit must be an integer from 1 to ${MAX_IN_FLIGHT_PER_SITE}`);
    }
    this.limit = limit;
  }

  /** Calls started through this gate that have not settled yet. Never above `limit`. */
  get inFlight(): number {
    return this.#inFlight;
  }

  /** Calls waiting for a slot. */
  get waiting(): number {
    return this.#waiting.length;
  }

  /** Runs `call` once a slot is free, and frees the slot when it settles either way. */
  async run<T>(call: () => Promise<T>, options: RunOptions = {}): Promise<T> {
    const outer = this.#running.getStore();
    if (outer !== undefined && !outer.settled) throw new NestedGateUse();

    await this.#acquire(options.signal);
    const mark = { settled: false };
    try {
      return await this.#running.run(mark, call);
    } finally {
      mark.settled = true;
      this.#release();
    }
  }

  #acquire(signal: AbortSignal | undefined): Promise<void> {
    if (signal?.aborted === true) return Promise.reject(signal.reason);
    if (this.#inFlight < this.limit) {
      this.#inFlight++;
      return Promise.resolve();
    }
    return new Promise<void>((resolve, reject) => {
      const onAbort = (): void => {
        const at = this.#waiting.indexOf(waiter);
        if (at < 0) return; // already admitted: the slot is this call's and it will start
        this.#waiting.splice(at, 1);
        reject(signal?.reason);
      };
      const waiter: Waiter = {
        admit: () => {
          signal?.removeEventListener("abort", onAbort);
          resolve();
        },
      };
      this.#waiting.push(waiter);
      signal?.addEventListener("abort", onAbort, { once: true });
    });
  }

  #release(): void {
    // Hand the slot straight to the longest waiter. Freeing it first would let a call that arrives
    // in between take it, and a waiter could wait for ever.
    const next = this.#waiting.shift();
    if (next !== undefined) next.admit();
    else this.#inFlight--;
  }
}

const gates = new Map<string, RequestGate>();

/**
 * The one gate for a site in this process, created on first use. Key it on the subdomain, the
 * value the client was given as `serverOptions.production.site`. Case is ignored.
 */
export function gateForSite(site: string): RequestGate {
  const key = site.trim().toLowerCase();
  if (key === "") throw new RangeError("site must not be empty");
  let gate = gates.get(key);
  if (gate === undefined) {
    gate = new RequestGate();
    gates.set(key, gate);
  }
  return gate;
}
