# Payment Profiles: provider notes

Notes for the Payment Profiles operations an integration most often calls. An operation of this group
that has no section here has no provider notes (see `../index.json`).

### createPaymentProfile
`client.payment_profiles.create_payment_profile` · `POST /payment_profiles.json` · contract: `map/operations/payment_profiles.md`
**Always:** Send `customer_id` and one payment source; with a `chargify_token`, no card or bank numbers (R15). It is not made a default: follow with `change_subscription_default_payment_profile` if a subscription should charge it (L6).

**Before you call**
- You need `customer_id` and one payment source: a Maxio.js `chargify_token` (rules.md R15), raw card
  data only if the merchant is PCI compliant, or vault-import fields (`vault_token`, `current_vault`).

**Rules**
- A new profile does **not** become the default: "it does not automatically make the profile current
  for any of the customer's subscriptions". If a subscription should charge it, follow with
  `change_subscription_default_payment_profile`. A profile kept for a later signup (sent there as
  `payment_profile_id`, decisions.md D2) needs no such call.
- With a `chargify_token`, the operation's own example sends only `customer_id` and the token, both
  inside `payment_profile`. The token already stands for the card or bank details, so send no card or
  bank numbers beside it *(inferred)*.
- ACH needs `bank_name`, `bank_routing_number` and `bank_account_number`, and `billing_country` must be
  `US`.
- When importing, `current_vault` must name the gateway the site really uses (`stripe_connect`, not
  `stripe`). Maxio enforced this briefly in November 2021, withdrew the check and says it will
  return [announcement].
- Duplicate prevention: send a `uniqueness_token` at the body root, beside `payment_profile`, never
  inside it (rules.md R12). Use one token for this write and the same token on every resend of it;
  mint a new one only after a 422 you corrected. **Not in the contract:** the spec does not declare the
  field on this request. `docs/models.md`, section "Fields the spec does not declare", says how to send
  it.
- **Unknown outcome (rules.md R11).** The read-back is `list_payment_profiles` for the customer. It is
  not by a unique reference, so a profile still not found after a 409
  `DuplicatePrevention::DuplicateSubmissionError` is settled by hand, never sent again automatically
  (R11 step 4).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Advanced Billing token not found" | Maxio does not know the `chargify_token`. An expired or already used token is a likely cause *(inferred)* | Tokenize again in the browser |
| 422 with an `action_link` | 3-D Secure is required. This 422 is a step to complete, not a validation error | Send the customer to the link (rules.md R13). `docs/models.md`, section "Fields the spec does not declare", says how to read it |
| 422 "Credit card expiration month: cannot be blank." "Credit card expiration year: cannot be blank." "Credit card number: cannot be blank." | The raw-card path is missing card fields | Use a token, or send every card field |
| 404 | Not explained: the spec declares the status with no body. An unknown `customer_id` is a likely cause *(inferred)* | Resolve the customer first |

**Sources:** [spec] createPaymentProfile, Create-Payment-Profile · [docs]
about-the-api/duplicate-prevention · [announcement] 2021-12-16 current vault validation

### changeSubscriptionDefaultPaymentProfile
`client.payment_profiles.change_subscription_default_payment_profile` · `POST /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_payment_profile.json` · contract: `map/operations/payment_profiles.md`

**Before you call**
- The profile must exist and belong to this subscription's customer.

**Rules**
- This is how an already stored profile becomes the one renewals charge. `update_subscription` has no
  `payment_profile_id` field: it takes new card details only (decisions.md D6).
- For subscription groups use `change_subscription_group_default_payment_profile`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "This is already the current payment profile" | The profile is already this subscription's default | Nothing to change. Match this exact message before you treat it as done: any other 422 is a rejection (rules.md R13) |
| 404 | Unknown subscription or payment profile | Check both ids |

**Sources:** [spec] changeSubscriptionDefaultPaymentProfile, updateSubscription

### updatePaymentProfile
`client.payment_profiles.update_payment_profile` · `PUT /payment_profiles/{payment_profile_id}.json` · contract: `map/operations/payment_profiles.md`
**Always:** To replace a card use `create_payment_profile`, then `change_subscription_default_payment_profile` (D6). This call never collects: after fixing a past-due subscriber's card here, collect with `retry_subscription` (D12).

**Before you call**
- Decide whether you are fixing details (name, address) or replacing the card (decisions.md D6).

**Rules**
- On Authorize.net, Cybersource, Forte, Braintree Blue and Stripe, the API "will ignore the credit card
  number and CVV … and attempt a partial update": the call succeeds and the old card stays on file
  *(that it answers 200 is inferred)*. No failure tells you, so if you sent a new number, read the
  profile back and compare `masked_card_number`. To replace a card, create a new profile and make it
  the default.
- A profile cannot switch between card and bank account.
- Updating a profile does not retry a past-due balance [spec]. To collect after a fix made here, call
  `retry_subscription` (D12); the spec names that path for Authorize.net and Stripe. Sending the new
  card through `update_subscription` instead does collect, but that call refuses partial card updates
  on Authorize.Net [spec].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 payment_profile: can't be blank | The body has no `payment_profile` object. This is the only 422 the spec documents here | Wrap the fields as `{"payment_profile": {...}}` |
| 422 | Bank account fields sent to a card profile, or the reverse *(inferred: the spec forbids the mix and documents no message for it)* | Create a new profile of the other type |

**Sources:** [spec] updatePaymentProfile, updateSubscription "Update Subscription Payment Method",
retrySubscription

### listPaymentProfiles
`client.payment_profiles.list_payment_profiles` · `GET /payment_profiles.json` · contract: `map/operations/payment_profiles.md`
**Always:** Pass `customer_id` in anything customer-facing.

**Rules**
- Always pass `customer_id` in anything customer-facing. Without it the endpoint "lists all active
  payment profiles for a site", which would show one customer the masked cards of others.

**Sources:** [spec] listPaymentProfiles

### deleteUnusedPaymentProfile
`client.payment_profiles.delete_unused_payment_profile` · `DELETE /payment_profiles/{payment_profile_id}.json` · contract: `map/operations/payment_profiles.md`

**Rules**
- Only for profiles no subscription uses. To remove a profile a subscription uses, call
  `delete_subscriptions_payment_profile`, which removes it "from all of them" if the customer has several
  subscriptions. Set another default afterwards, or the next automatic charge has nothing to use
  *(inferred)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "The payment profile is in use by one or more subscriptions and cannot be deleted" | In use | Use `delete_subscriptions_payment_profile`, or change the default first |

**Sources:** [spec] deleteUnusedPaymentProfile, deleteSubscriptionsPaymentProfile

### deleteSubscriptionsPaymentProfile
`client.payment_profiles.delete_subscriptions_payment_profile` · `DELETE /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json` · contract: `map/operations/payment_profiles.md`
**Always:** This removes the profile from every subscription the customer has, not only the one in the path. Each one that charged it then needs a new default: set it with `change_subscription_default_payment_profile` (D7).

**Before you call**
- The path names one subscription, but if the customer has several, "the payment profile is removed
  from all of them". List them with `list_customer_subscriptions` and see which ones charge this
  profile.

**Rules**
- After the default profile of a subscription is deleted "you need to specify another payment profile
  to be the default". Through the API that is `change_subscription_default_payment_profile`; the other
  ways are the customer adding a card in the Billing Portal or on the self-service page.
- Until then an automatic renewal has nothing to charge *(inferred)*.
- For a profile no subscription uses, call `delete_unused_payment_profile` instead (decisions.md D7).

**Sources:** [spec] deleteSubscriptionsPaymentProfile, deleteUnusedPaymentProfile

### verifyBankAccount
`client.payment_profiles.verify_bank_account` · `PUT /bank_accounts/{bank_account_id}/verification.json` · contract: `map/operations/payment_profiles.md`
**Always:** Turn off the client's automatic retry for this `PUT`: tries are capped at 10, then verification is blocked until the merchant contacts Maxio. Treat a timeout as an unknown outcome: check `verified` before sending again (R11).

**Rules**
- Stripe only. Send the two micro-deposit amounts in cents.
- Tries are capped: after 10, verification is blocked until the merchant contacts Maxio. A wrong pair
  of amounts costs a try, so take the amounts from the customer and never loop over guesses.
- This is a `PUT`, and an HTTP client may resend a `PUT` on its own after a timeout or a 5xx. Each
  resend can cost a try *(inferred)*. Turn automatic retry off for this call and allow at least 120
  seconds *(inferred from the 120 second cut-off, rules.md R11)*. `docs/configuration-resilience.md`,
  section "Maxio: retries, timeouts and paging", says how.
- After a timeout the outcome is unknown: check the profile's `verified` flag (`list_payment_profiles`
  for the customer) before you send the amounts again.
- `uniqueness_token` is accepted on `PUT` as well [docs], so sending one should make a resend answer
  409 instead of counting twice *(inferred; not probed)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "You have tried to verify this bank account 10 times. …" | Tries exhausted | Stop. No request unblocks it: tell the merchant to contact Maxio |

**Sources:** [spec] verifyBankAccount, Bank-Account-Payment-Profile · [docs]
about-the-api/duplicate-prevention, error-handling "Timeout Limitation"
