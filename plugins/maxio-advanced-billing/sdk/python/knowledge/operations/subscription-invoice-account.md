# Subscription Invoice Account: provider notes

Prepayments, service credits and balances. Which money operation fits a need is `../decisions.md` D15.
An operation of this group that has no section here has no provider notes (see `../index.json`).

### createPrepayment
`client.subscription_invoice_account.create_prepayment` · `POST /subscriptions/{subscription_id}/prepayments.json` · contract: `map/operations/subscription_invoice_account.md`
**Always:** Choose `method` on purpose: `credit_card_on_file` charges the default card now (D15). `amount` is in major units: the spec's `amount: 100` comes back as `amount_in_cents: 10000`.

**Rules**
- With `method: credit_card_on_file` the amount "will be collected using the default credit card
  payment profile and applied to the prepayment account balance" [spec]. The spec describes no
  collection for any other `method`, so those record money received elsewhere *(inferred)*.
- `amount` is a decimal in major units, while the answer is in cents: the spec's example sends
  `amount: 100` and gets `amount_in_cents: 10000` (R4). The description says passing `amount_in_cents`
  "is now allowed", but the request body does not declare it *(unconfirmed)*: send `amount`.
- `payment_profile_id` is declared with no description. Whether it selects the profile that
  `credit_card_on_file` charges is not stated *(unconfirmed)*: do not rely on it to pick a card.
- Applying a prepayment returns a `suspended` prepaid subscription to `active` [spec].
- With `credit_card_on_file` this call takes a payment. Send one `uniqueness_token` at the top level of
  the body, beside `prepayment`, and keep it on every resend (R12). After an unknown outcome the
  read-back is `list_prepayments`. It is not by a unique reference, so a prepayment still not found
  after a 409 is settled from webhooks or by hand, never sent again automatically (R11 step 4).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 with an `action_link` | 3-D Secure is required for a `credit_card_on_file` prepayment [spec]. This is not a decline | Send the customer to the link. Do not resend |

**Sources:** [spec] createPrepayment, Create-Prepayment, Create-Prepayment-Method, Subscription-State ·
[docs] about-the-api/duplicate-prevention, error-handling "Timeout Limitation"

### issueServiceCredit
`client.subscription_invoice_account.issue_service_credit` · `POST /subscriptions/{subscription_id}/service_credits.json` · contract: `map/operations/subscription_invoice_account.md`

**Rules**
- A goodwill credit, "applied to the next generated invoice". Not customer-paid money: do not record
  goodwill as a prepayment.

**Sources:** [spec] issueServiceCredit

### refundPrepayment
`client.subscription_invoice_account.refund_prepayment` · `POST /subscriptions/{subscription_id}/prepayments/{prepayment_id}/refunds.json` · contract: `map/operations/subscription_invoice_account.md`
**Always:** `prepayment_id` is the original payment's account transaction id. For a prepayment made through a payment profile send `external` explicitly: `false` refunds to the profile, `true` only records a refund *(inferred)*.

**Rules**
- `prepayment_id` is the **account transaction id** of the original payment, and the prepayment must
  still have some amount remaining [spec].
- `external` must be present when the prepayment was made through a payment profile; it is optional
  when the prepayment itself was external [spec]. Present does not mean `true`.
- What the value does is documented on `refund_invoice`, not here: an external refund means "no money
  is returned to the customer" [spec]. Maxio's signup guide says of an external refund that nothing is
  passed to the gateway and it only changes the balance and adds a transaction record [docs]. So
  `external: true` records a refund you made outside Maxio, and `external: false` asks Maxio to send
  the money back to the payment profile *(inferred for this operation)*.
- Unless `external` is `true`, this sends money back. Send one `uniqueness_token` at the top level of
  the body, beside `refund`, and keep it on every resend (R12). After an unknown outcome the read-back
  is `list_prepayments` (`refunded_amount_in_cents`, `remaining_amount_in_cents` of that prepayment).
  It is not by a unique reference, so a refund still not found after a 409 is settled from webhooks or
  by hand, never sent again automatically (R11 step 4).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Refund amount exceeds prepayment amount" | The amount is larger than what remains of the prepayment. Reported under `refund.amount_in_cents` | Lower the amount |

**Sources:** [spec] refundPrepayment, Refund-Prepayment, Refund-Invoice, listPrepayments, Prepayment ·
[docs] basic-concepts/subscription-signup "Refunds", about-the-api/duplicate-prevention

### readAccountBalances
`client.subscription_invoice_account.read_account_balances` · `GET /subscriptions/{subscription_id}/account_balances.json` · contract: `map/operations/subscription_invoice_account.md`

**Rules**
- Read it before deciding how much a customer owes or holds (D15). The amounts are integer cents (R4).

**Sources:** [spec] readAccountBalances
