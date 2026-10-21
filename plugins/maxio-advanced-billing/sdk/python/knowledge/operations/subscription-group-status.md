# Subscription Group Status: provider notes

Cancel, delay a cancel and reactivate for a whole subscription group. The same choices for a single
subscription are on `subscription-status.md`; `../decisions.md` D11 and D12 name them. An operation of
this group that has no section here has no provider notes (see `../index.json`).

### cancelSubscriptionsInGroup
`client.subscription_group_status.cancel_subscriptions_in_group` · `POST /subscription_groups/{uid}/cancel.json` · contract: `map/operations/subscription_group_status.md`
**Always:** This cancels every subscription in the group at once. Unbilled metered and prepaid usage is charged only when you send `charge_unbilled_usage: true`: decide it.

**Before you call**
- The primary subscription must be on automatic billing, and every member on automatic or prepaid
  billing [spec].

**Rules**
- All subscriptions in the group are canceled immediately [spec]. There is no per-member choice here:
  to cancel one member, use `cancel_subscription`.
- Usage on metered or prepaid components that has not been billed yet is charged only with
  `charge_unbilled_usage: true` [spec]. Without it that usage goes unbilled *(inferred)*.
- The 200 answer has no body. Confirm from `read_subscription_group` or from each member's `state`
  *(inferred)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "One or more subscriptions are not on automatic billing" | A member's collection method does not allow a group cancel | Cancel the members one by one with `cancel_subscription` |

**Sources:** [spec] cancelSubscriptionsInGroup

### initiateDelayedCancellationForGroup
`client.subscription_group_status.initiate_delayed_cancellation_for_group` · `POST /subscription_groups/{uid}/delayed_cancel.json` · contract: `map/operations/subscription_group_status.md`
**Always:** Call only when every subscription in the group is on automatic billing and the group is not `past_due`.

**Rules**
- Schedules every subscription in the group to cancel at the end of its billing period [spec].
- The 200 answer has no body. Confirm from the members: each should show
  `cancel_at_end_of_period: true`, the flag `cancel_delayed_cancellation_for_group` resets *(inferred from
  that operation's description)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Subscriptions group is in a past due state" | The group is `past_due` | Recover payment first (D12), or cancel now with `cancel_subscriptions_in_group` |

**Sources:** [spec] initiateDelayedCancellationForGroup, cancelDelayedCancellationForGroup

### cancelDelayedCancellationForGroup
`client.subscription_group_status.cancel_delayed_cancellation_for_group` · `DELETE /subscription_groups/{uid}/delayed_cancel.json` · contract: `map/operations/subscription_group_status.md`

**Rules**
- Resets `cancel_at_end_of_period` to `false` on each member of the group [spec].
- Unlike `cancel_delayed_cancellation` for a single subscription, which is idempotent, this call answers
  422 when nothing is scheduled [spec]. Treat that answer as "already undone".

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Subscriptions group does not have a pending delayed cancellation" | No delayed cancellation is scheduled for the group | Nothing to undo; treat as done |

**Sources:** [spec] cancelDelayedCancellationForGroup, cancelDelayedCancellation

### reactivateSubscriptionGroup
`client.subscription_group_status.reactivate_subscription_group` · `POST /subscription_groups/{uid}/reactivate.json` · contract: `map/operations/subscription_group_status.md`
**Always:** It attempts payment: canceled invoices from the primary's current period are reopened and charged, and a new period adds new charges. Decide `resume` and `resume_members`. After a timeout read the group back first (R11).

**Before you call**
- Know whether the primary subscription's billing period has ended: that decides whether a resume is
  possible at all [spec].
- Decide `resume` (keep the current period) and `resume_members` (let members with longer periods keep
  theirs).

**Rules**
- **Payment.** On reactivation, "any canceled invoices created after the beginning of the primary
  subscription's billing period will be reopened and payment will be attempted on them". A
  reactivation that is not a resume also assesses new charges for the new billing period [spec].
- Inside the primary's current period: `resume: true` keeps the existing billing period; without it a
  new period starts. `resume_members` is ignored in this case, and all eligible members resume [spec].
- Subscriptions on calendar billing cannot be reactivated inside the current period: without
  `resume: true` the request returns an error [spec].
- After the primary's period has ended: only a new billing period is possible. The description says
  `resume: true` is then ignored, while the documented 422 below says the request is rejected; expect
  either *(the spec gives both)*. `resume_members: true` lets members whose own, longer period is
  still running keep it, while the primary starts a new one [spec].
- This call collects money. Send one `uniqueness_token` at the top level of the body, kept on every
  resend (R12). After an unknown outcome the read-back is `read_subscription_group` and each member's
  `state`. It is not by a unique reference, so a reactivation still not settled after a 409 is settled
  from webhooks or by hand, never sent again automatically (R11 step 4).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Must be inside the current billing period to resume this subscription group" | `resume` was asked for after the primary's billing period had ended | Decide with the user whether a new, charged period is acceptable. If so, send again without `resume` |
| 422 with an `action_link` | 3-D Secure is required [spec]. This is not a decline | Send the customer to the link. Do not resend |

**Sources:** [spec] reactivateSubscriptionGroup, Reactivate-Subscription-Group-Request · [docs]
about-the-api/duplicate-prevention, error-handling "Timeout Limitation"
