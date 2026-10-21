/*
 * subscription-state: what a Maxio subscription state means for access and for signing up again.
 *
 * What it does
 *   `standing(state)` puts every state the SDK's `SubscriptionState` names into one of four groups,
 *   and anything else into a fifth:
 *     live         active, trialing, past_due, soft_failure. The subscriber has access. past_due is
 *                  here on purpose: access stays on while Maxio retries the payment.
 *     transient    pending, assessing. Maxio is in the middle of creating or renewing. Decide
 *                  nothing: keep the access decision you made last.
 *     recoverable  on_hold, suspended, unpaid, awaiting_signup, paused. Not billing, no access, and
 *                  it comes back. Never create a second subscription beside one of these.
 *     ended        canceled, expired, trial_ended, failed_to_create. No access. A new signup or a
 *                  reactivation is possible.
 *     unclassified a missing state (the SDK types `state` as optional) or one this SDK version does
 *                  not name. Nothing is known about it: it grants nothing, takes nothing away, and
 *                  never lets a second signup through. Update the SDK and this file.
 *   `hasAccess(state)` is true for the four live states and false for everything else.
 *   `decideAccess(state, previous)` is `hasAccess`, except that a transient or unclassified state
 *   returns `previous`.
 *
 * Two things the names do not tell you
 *   - Maxio's schema lists six states as End of Life (not billing): canceled, expired,
 *     failed_to_create, on_hold, suspended, trial_ended. Two of those, on_hold and suspended, come
 *     back, so they are `recoverable` here and not `ended`.
 *   - A subscription you paused is `on_hold`. No API call produces `paused`: it means the
 *     merchant's own Maxio account is in arrears.
 *
 * Listing everyone with access
 *   The `state` filter of `listSubscriptions` takes `SubscriptionStateFilter`, a different and
 *   smaller set of values than `SubscriptionState`. It has no value for soft_failure, assessing,
 *   pending, failed_to_create or paused. So list with no `state` filter (recipes/list-all.ts) and
 *   keep the rows where `hasAccess(row.subscription?.state)` is true. A transient or unclassified
 *   row cannot be decided from a list alone: use the decision you stored for it, or read it again.
 *   With no stored decision, count assessing in (a renewal in progress; its entitlements stay on)
 *   and pending out (knowledge/lifecycles.md L3).
 *
 * Guard
 *   `STANDING_BY_STATE` is typed as a record over every state the SDK names. When a regenerated
 *   SDK adds a state, this file stops compiling until the new state is classified here.
 *
 * Implements knowledge/rules.md R16 and knowledge/lifecycles.md L3.
 *
 * Leaves to the caller: storing the last access decision for each subscription, and reading the
 * subscription again before acting on a webhook (knowledge/rules.md R20).
 *
 * Needs only the SDK. Copy into your project and adapt. Not part of the SDK's API.
 */
import { SubscriptionState } from "maxio-advanced-billing";

export type Standing = "live" | "transient" | "recoverable" | "ended" | "unclassified";

/** The states this SDK version names, without the open `string` arm of `SubscriptionState`. */
export type KnownSubscriptionState = (typeof SubscriptionState)[keyof typeof SubscriptionState];

/** The four groups a state the SDK names can be in. */
export type ClassifiedStanding = Exclude<Standing, "unclassified">;

/**
 * Every state the SDK names, classified. The annotation is the guard: a state the SDK gains is a
 * missing property here, and a state it drops is an unknown one. Both are compile errors.
 */
export const STANDING_BY_STATE: Readonly<Record<KnownSubscriptionState, ClassifiedStanding>> = {
  active: "live",
  trialing: "live",
  past_due: "live",
  soft_failure: "live",

  pending: "transient",
  assessing: "transient",

  on_hold: "recoverable",
  suspended: "recoverable",
  unpaid: "recoverable",
  awaiting_signup: "recoverable",
  // No API call produces it: the merchant's own Maxio account is in arrears.
  paused: "recoverable",

  canceled: "ended",
  expired: "ended",
  trial_ended: "ended",
  failed_to_create: "ended",
};

// A Map, so that a state named "constructor" or "toString" finds nothing.
const standings: ReadonlyMap<string, Standing> = new Map(Object.entries(STANDING_BY_STATE));

/**
 * The group a state belongs to. A state this SDK version does not name, and a missing state, are
 * `unclassified`.
 */
export function standing(state: SubscriptionState | null | undefined): Standing {
  if (typeof state !== "string") return "unclassified";
  return standings.get(state) ?? "unclassified";
}

/**
 * True for active, trialing, past_due and soft_failure. False for a transient or unclassified state
 * too, so use {@link decideAccess} where you have a stored decision to keep.
 */
export function hasAccess(state: SubscriptionState | null | undefined): boolean {
  return standing(state) === "live";
}

/**
 * The access decision for a subscription now in `state`.
 *
 * @param previous The decision you last stored for this subscription, or `false` when you have none.
 */
export function decideAccess(state: SubscriptionState | null | undefined, previous: boolean): boolean {
  const group = standing(state);
  return group === "transient" || group === "unclassified" ? previous : group === "live";
}
