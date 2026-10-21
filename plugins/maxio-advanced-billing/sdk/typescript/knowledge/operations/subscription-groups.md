# Subscription Groups: provider notes

Signing up several subscriptions for one payer, and changing who is in a group. Cancelling and
reactivating a whole group is on `subscription-group-status.md`. An operation of this group that has no
section here has no provider notes (see `../index.json`).

### signupWithSubscriptionGroup
`client.subscriptionGroups.signupWithSubscriptionGroup` · `POST /subscription_groups/signup.json` · contract: `map/operations/subscription-groups.md`
**Always:** Send one payer source, at most one payment source, `payment_collection_method` by intent (R14), exactly one subscription with `"primary": true`, and a top-level `uniqueness_token`, unchanged when you resend the request (R12).

**Before you call**
- Payer: exactly one of `payer_id`, `payer_reference`, `payer_attributes` [spec].
- Collection method: send the group's `payment_collection_method` on every signup, chosen by how the
  payer will pay (R14, D3). Ask when the task does not say.
  - The payer pays by card or bank account: `automatic`, with a payment source.
  - The merchant bills by invoice: `remittance` on a Relationship Invoicing site, `invoice` on a legacy
    Statements site (`readSite`, R3). The payer is not charged automatically [docs].
  - Nothing is due at signup (trials, free plans): `automatic` with no payment source *(inferred)*.
- Payment source: at most one of `payment_profile_id`, `credit_card_attributes`,
  `bank_account_attributes`. The description asks for "one and only one", but the spec's own example
  for an invoiced group (`payer_attributes` with `payment_collection_method: remittance`) sends none
  [spec]. So: one when the payer pays by card or bank, none when the group is billed by invoice.
- Exactly one subscription carries `"primary": true` [spec].
- Duplicate safety (R12): before the first send, save a `uniqueness_token` for this request and give
  every subscription in the request its own `reference`, derived from your own record of the signup.
  The token goes at the top level of the body, beside `subscription_group` [docs].

**Rules**
- Use this to sign up several new subscriptions for one payer in one call. To add one subscription to
  an existing group or customer hierarchy, use `createSubscription` with `group` (decisions.md D8).
- Omitted, `payment_collection_method` falls to the site's default *(inferred: the spec states no
  default here either)*. Never switch a card-paying group to an invoice method to make the "No payment
  method" rejection go away.
- **Unknown outcome (R11).** Settle it in R11's order. The read-back is `findSubscription` by each
  subscription's `reference`, unique references you set, and the request carries a token.
  `findSubscriptionGroup` shows the group and its members. Whether a group signup can land in part is
  not stated *(unconfirmed)*, so at R11 step 4 start again with a new token only when none of the
  request's subscriptions is found; if some are, settle by hand. A second copy under a new token
  creates every subscription twice.
- Errors are keyed by the subscription's position in the request: `errors.subscriptions` holds one
  entry per failing item, named by its index as a string, and inside it one key per problem (`base`,
  `product`, `product_price_point_id`, `payment_profile.chargify_token`) [spec].
- Maxio emits `subscription_group_signup_success` and `subscription_group_signup_failure` [docs].
  Neither key is among the values the contract lists for an endpoint's `webhook_subscriptions`, so
  whether an endpoint created through the API can subscribe to them is not stated *(unconfirmed)*.
  Settle the signup from the response and the read-back.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "No payment method was on file for the …" | Reported under the failing item's `base` key: collection is `automatic` (sent, or the site default), money is due at signup and there is no payment source | Decide by intent (R14). A payer who pays by card or bank needs a payment source. A group billed by invoice needs `remittance` or `invoice`. Never switch a card-paying group to an invoice method to clear this |
| 422 "Chargify token not found" | Reported under the item's `payment_profile.chargify_token` key: the Maxio.js token is unknown or already used *(second cause inferred)* | Tokenize again in the browser (R15), then send with a new `uniqueness_token` |
| 422 "Product must be among the Products for this Site" | Reported under the item's `product` key: the product is not on this site | Correct that item, then send with a new `uniqueness_token` |
| 422 "Product price point must belong to product." | Reported under the item's `product_price_point_id` key: the price point belongs to another product | Correct that item, then send with a new `uniqueness_token` |
| 409 `DuplicatePrevention::DuplicateSubmissionError` | A request with this `uniqueness_token` already reached Maxio [docs]. Its outcome is unknown: a 409 never proves success | Follow R11 with `findSubscription` by each subscription's `reference`. Found: settle from what Maxio holds. None found once 120 seconds have passed since the first send: start again with a new token (R11 step 4) |

**Sources:** [spec] signupWithSubscriptionGroup, Subscription-Group-Signup,
Subscription-Group-Signup-Item, Subscription-Group-Signup-Error-Response, Webhook-Subscription · [docs]
about-the-api/duplicate-prevention, error-handling "Timeout Limitation", basic-concepts/subscription-signup
"Payment Methods", webhooks-reference (subscription_group_signup_success, subscription_group_signup_failure)

### updateSubscriptionGroupMembers
`client.subscriptionGroups.updateSubscriptionGroupMembers` · `PUT /subscription_groups/{uid}.json` · contract: `map/operations/subscription-groups.md`
**Always:** `member_ids` replaces the whole membership: send every subscription that should stay, plus the new ones. An id you leave out is removed from the group, and an empty list removes every member.

**Rules**
- Read the current members first (`readSubscriptionGroup`), then send the complete list. The spec:
  "Not including them will result in removing them from the subscription group. To clean up members,
  just leave the array empty."

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 `not_found` | Reported under `errors.members`: an id in `member_ids` is not a subscription the group can take *(inferred)* | Check every id against the site before sending |

**Sources:** [spec] updateSubscriptionGroupMembers

### addSubscriptionToGroup
`client.subscriptionGroups.addSubscriptionToGroup` · `POST /subscriptions/{subscription_id}/group.json` · contract: `map/operations/subscription-groups.md`
**Always:** This decides who pays: the subscription joins the target's group and its payer, or a new group with the target customer as payer (`self`: the subscriber). It must share the target's customer record or hierarchy.

**Rules**
- When the target customer or subscription is not yet in a group, a new group is created with the
  target customer "as the responsible payer for the group's subscriptions" [spec]. When the target is
  already in one, the subscription joins that group.
- A `target` of type `self`, `parent` or `eldest` names the payer by position: the subscribing
  customer, its parent in the customer hierarchy, or the root-level customer [spec].
- The `billing` options (`accrue`, `align_date`, `prorate`) are described as "Only applicable for new
  subscriptions", although this operation's own example sends them [spec]. Do not rely on them to
  change the billing of an existing subscription *(unconfirmed)*.
- Needs the Relationship Invoicing architecture and the Customer Hierarchy feature [spec]. To create
  a new subscription straight into a group, use `createSubscription` with `group` (D8).

**Sources:** [spec] addSubscriptionToGroup, Group-Target, Group-Billing
