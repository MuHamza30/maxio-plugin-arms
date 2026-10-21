# Entitlements: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### readSubscriptionEntitlements
`client.Entitlements.ReadSubscriptionEntitlements` · `GET /subscriptions/{subscription_id}/entitlements.json` · contract: `map/operations/Entitlements.md`
**Always:** Match on the prefixed key (`feature.<key>`, `usage.<key>`, `service.<key>`), key entries on `periodicity_key`, and grant access only when `enabled` is true.

**Rules**
- `feature_key` carries a kind prefix: template key `sso` comes back as `feature.sso`; usage limits are
  `usage.*`, service rights `service.*`. Comparing with the raw template key never matches.
- One entry per feature key **and** periodicity: key lookups on `periodicity_key`.
- Gate access on `enabled`. It is false for non-live states and deliberately **stays true through
  dunning** (`past_due`, `soft_failure`); it turns off at `on_hold`, `unpaid`, `canceled`.
- Combined values: `access_right` is OR, `usage_limit` sums within one periodicity, and for
  `service_right` one contributor wins (which one is undefined).
- New features reach existing subscribers only at their next subscription change unless they were
  attached with `propagate_to_subscriptions: true` (product-features.md).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 403 | Not stated: the spec declares the status with no body example. Possibly the feature is not available on the site *(unconfirmed)* | Check the site's feature access |

**Sources:** [spec] readSubscriptionEntitlements, Aggregated-Entitlement · [docs] basic-concepts/entitlements
