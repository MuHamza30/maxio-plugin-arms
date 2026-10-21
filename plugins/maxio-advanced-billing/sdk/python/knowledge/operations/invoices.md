# Invoices: provider notes

Relationship Invoicing sites (rules.md R3). Which money operation fits a need is `../decisions.md` D15;
which invoice operation a status allows is D16. An operation of this group that has no section here has
no provider notes (see `../index.json`).

### createInvoice
`client.invoices.create_invoice` · `POST /subscriptions/{subscription_id}/invoices.json` · contract: `map/operations/invoices.md`
**Always:** Decide `status`: send `"draft"` for review; the default `open` issues the invoice now. Make each line item exactly one of `title` + `unit_price`, `product_id` or `component_id`. Keep `issue_date` at today or earlier.

**Before you call**
- This is the one-off charge on Relationship Invoicing. The charge, refund and adjustment examples in
  Maxio's basic-concepts docs point to the **legacy** API, which has no operation in this spec; do not
  hand-roll those endpoints.
- Decide `status`: the default `open` issues the invoice now (due today unless `net_terms`); use
  `"draft"` if someone must review it.

**Rules**
- Each line item is exactly one of: a custom item (`title` + `unit_price`), `product_id`, or
  `component_id`. A price point excludes `unit_price`; prepaid and event-based components need
  `unit_price`.
- `issue_date` is today or earlier, in the site's time zone.
- Whether creating an open invoice attempts payment is not stated *(unconfirmed)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 invoice: can't be blank | The body has no `invoice` object. This is the only 422 the spec documents here | Wrap the payload as `{"invoice": {...}}` |

**Sources:** [spec] createInvoice, Create-Invoice · [docs] basic-concepts/subscription-signup (legacy links)

### updateInvoice
`client.invoices.update_invoice` · `PUT /subscriptions/{subscription_id}/invoices/{uid}.json` · contract: `map/operations/invoices.md`
**Always:** Send `coupons` only to replace every discount on the invoice: the list you send replaces them all, and `[]` removes them. Send each existing line item with its `uid`; a line without `uid` is added as new.

**Before you call**
- Only an ad hoc invoice in `draft` can be updated. An issued invoice, or one with another role
  (`renewal`, `signup`), is rejected with 422.

**Rules**
- Only what you send changes; omitted attributes keep their values. The two arrays behave
  differently:
  - `line_items`: a row without `uid` is **added**, a row with `uid` updates that line, and `uid`
    with `_destroy: true` removes it. Lines you do not mention stay. So sending the invoice's lines
    back without their `uid`s adds them a second time.
  - `coupons`: "When the `coupons` key is present, the submitted coupons replace all discounts
    currently applied to the invoice." Leave the key out to keep the discounts.
- Changing `issue_date` or `net_terms` recalculates the due date; changing an address recalculates
  taxes.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Line item not found." | A `uid` that is not on this invoice | Read the invoice with `read_invoice` and use its line item `uid`s |
| 422 "Billing address must include name." | An address sent without `first_name` | Send `first_name` in every address you send |
| 422 | The invoice is not an ad hoc `draft` (message not documented) | Only a draft can be edited. For an issued invoice pick from decisions.md D16 |
| 404 "Invoice not found" | The invoice does not belong to that subscription | Check the `subscription_id` and `uid` pair |

**Sources:** [spec] updateInvoice, Update-Invoice, Update-Invoice-Item

### deleteInvoice
`client.invoices.delete_invoice` · `DELETE /subscriptions/{subscription_id}/invoices/{uid}.json` · contract: `map/operations/invoices.md`
**Always:** Delete only an ad hoc `draft` invoice, and only when it should be gone for good: the invoice "is permanently removed". Void an issued invoice with `void_invoice` instead.

**Rules**
- Only invoices with the `adhoc` role and `draft` status can be deleted. The delete is permanent;
  this API has no operation that restores one.
- "Issued invoices should be voided instead" (`void_invoice`, decisions.md D16).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Status must be draft." | The invoice is not a draft | Use `void_invoice` if its status allows (decisions.md D16) |
| 422 "Only adhoc invoices can be deleted." | The invoice has another role, such as `renewal` or `signup` | It cannot be deleted. See decisions.md D16 |
| 404 "Invoice not found" | The invoice does not belong to that subscription. An invoice already deleted would answer the same way *(inferred)* | Check the `subscription_id` and `uid` pair |

**Sources:** [spec] deleteInvoice

### issueInvoice
`client.invoices.issue_invoice` · `POST /invoices/{uid}/issue.json` · contract: `map/operations/invoices.md`
**Always:** On automatic collection choose `on_failed_payment`. On remittance subscriptions never send `on_failed_payment`. Issue only `draft` or `pending` invoices (D16).

**Before you call**
- The invoice is `draft` or `pending` and not a group member's pending child invoice. On automatic
  collection, choose `on_failed_payment`.

**Rules**
- The default `leave_open_invoice` leaves a failed payment on an open invoice and does **not** start
  dunning. With `initiate_dunning` the subscription "will most likely go into" `past_due` or
  `canceled`, "depending upon net terms and dunning settings". `rollback_to_pending` keeps the invoice
  pending.
- On remittance subscriptions no payment is attempted, and sending `on_failed_payment` is rejected.
- Prepayments may not apply automatically (net terms and a site setting decide); apply them explicitly
  with `record_payment_for_invoice` `type: prepayment` when it matters.

**Sources:** [spec] issueInvoice, Failed-Payment-Action · [announcement] 2022-11-03, 2023-01-18

### recordPaymentForInvoice
`client.invoices.record_payment_for_invoice` · `POST /invoices/{uid}/payments.json` · contract: `map/operations/invoices.md`
**Always:** Choose `type` on purpose: default `external` only records money taken elsewhere; `prepayment`/`service_credit` draw on that balance; `payment` with `payment_profile_id` collects from that profile. Keep `amount` ≤ `due_amount`.

**Rules**
- `type` decides whether money moves:
  - `external` (the default) **records** money received elsewhere and charges nothing *(inferred:
    the spec calls it an external payment, and `received_on` is "when the payment was received from
    a customer")*. `memo`, `details` and `received_on` are each "Applicable only to `external`
    payments", and `received_on` must be in the past.
  - `prepayment` and `service_credit` apply the subscription's own prepayment or service credit
    balance to the invoice.
  - `payment` with `payment_profile_id` names "The ID of the payment profile to be used for the
    payment" [spec]: Maxio collects from that stored profile *(inferred from that wording; not
    probed)*. Never send it to record money already taken elsewhere, or the customer pays twice.
- The amount must not exceed `due_amount`. To overpay on purpose use `record_payment_for_subscription`,
  which turns the excess into a prepayment.
- With `type: payment` a resend can collect twice. Send one `uniqueness_token` at the top level of the
  body and keep it on every resend (rules.md R12). After an unknown outcome the read-back is
  `read_invoice` (`paid_amount`, `due_amount`, and `status`: `processing` is not paid, lifecycles.md
  L8). It is not by a unique reference, so a payment still not found after a 409 is settled from
  webhooks or by hand, never sent again automatically (rules.md R11 step 4).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Invoice must be open or in collections to apply payment" | The invoice is not open: paid, voided, draft or canceled | Use `reopen_invoice` first if it is `canceled`. Otherwise there is nothing to pay |
| 422 "Payment amount … exceeds due amount …" | Overpayment | Cap at `due_amount`; overpay through `record_payment_for_subscription` |
| 422 "Amount: is not a number." | `amount` missing or not numeric | Send a decimal amount |

**Sources:** [spec] recordPaymentForInvoice, Invoice-Payment-Type, Create-Invoice-Payment, Invoice-Status ·
[docs] about-the-api/duplicate-prevention

### recordPaymentForSubscription
`client.invoices.record_payment_for_subscription` · `POST /subscriptions/{subscription_id}/payments.json` · contract: `map/operations/invoices.md`

**Rules**
- Pays the oldest open invoice first and turns any excess into a prepayment. In a group, only the
  primary subscription can take it.

**Sources:** [spec] recordPaymentForSubscription

### recordPaymentForMultipleInvoices
`client.invoices.record_payment_for_multiple_invoices` · `POST /invoices/payments.json` · contract: `map/operations/invoices.md`
**Always:** This records an external payment; it charges nothing (inferred). Give each invoice at most its due amount; to leave a prepayment, raise the total `amount` above the sum of `applications`. Never include a consolidated invoice.

**Rules**
- It records "an external payment against multiple invoices": no card or bank account is charged
  *(inferred from "external")*.
- Send one `applications` row per invoice. A row may not exceed that invoice's due amount, and the
  total `amount` must be at least the sum of the rows. To overpay, put the excess in the total, which
  becomes a prepayment.
- When the total exceeds what the invoices owe, all the invoices must belong to one subscription. All
  invoices must be in one currency.
- Consolidated invoices cannot be paid here. `received_on` must be in the past.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Individual invoices may not be overpaid. To create a prepayment, add overage to the total amount." | One application is larger than its invoice's due amount | Cap each application at the due amount and put the excess in the total `amount` |
| 422 "Total amount must be higher or equal to invoices payment amount sum" | The total `amount` is smaller than the sum of the applications | Raise the total or lower the applications |
| 422 "Paying consolidated invoices is forbidden" | An `invoice_uid` names a consolidated invoice | Take it out of `applications` |
| 422 "Invoices belong to different subscriptions. Only invoices from same subscriptions are allowed when total amount exceeds invoices due amount." | An overpayment across subscriptions | Send one request per subscription, or do not overpay |
| 422 "Multiple applications associated to a single invoice, please aggregate and send as a single application per invoice." | Two rows for one invoice | Merge them into one row |
| 422 "Invoice must have an open balance" | An invoice in the list owes nothing | Take it out of `applications` |

**Sources:** [spec] recordPaymentForMultipleInvoices, Create-Multi-Invoice-Payment

### refundInvoice
`client.invoices.refund_invoice` · `POST /invoices/{uid}/refunds.json` · contract: `map/operations/invoices.md`
**Always:** Send `external: true` only to record a refund made elsewhere (D15). Send `void_invoice: true` only with `apply_credit: false` and a full refund. On consolidated invoices send `segment_uids`.

**Before you call**
- You need the `payment_id` and its remaining refundable amount. A paid invoice cannot be voided; this
  is how money goes back.

**Rules**
- `amount` is a decimal string. `external: true` records a refund made elsewhere: no money moves.
- `void_invoice: true` takes effect only with `apply_credit: false` and a full refund.
- On consolidated invoices `segment_uids` is required; partial refunds split proportionally.
- `refund_success`/`refund_failure` webhooks on newer sites carry `subscription[id]`, not
  `subscription_id`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Amount: must be greater than 0." | Zero or missing amount | Send a positive decimal string |

**Sources:** [spec] refundInvoice, Refund-Invoice · [announcement] 2023-05-18

### voidInvoice
`client.invoices.void_invoice` · `POST /invoices/{uid}/void.json` · contract: `map/operations/invoices.md`
**Always:** Void only `open`, `canceled` or non-consolidated `pending` invoices (D16). No operation reverses a void. Refund a `paid` invoice with `refund_invoice` instead.

**Rules**
- Allowed on `open`, `canceled`, or non-consolidated `pending` invoices.
- A voided invoice has no way back: this API has no operation that reopens one (`reopen_invoice` takes
  `canceled` invoices only).
- A `paid` invoice is refunded, not voided (`refund_invoice`). An ad hoc `draft` is deleted
  (`delete_invoice`).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Invoice status must be 'open', 'canceled', or 'pending' and non-consolidated to be voided." | Wrong status, or a consolidated `pending` invoice | Pick the operation the status allows (decisions.md D16) |

**Sources:** [spec] voidInvoice, reopenInvoice

### reopenInvoice
`client.invoices.reopen_invoice` · `POST /invoices/{uid}/reopen.json` · contract: `map/operations/invoices.md`

**Rules**
- Only `canceled` invoices; makes them `open` (due) again. Reopen older periods' invoices **before**
  reactivating a subscription if you intend to collect them.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "The invoice must be in canceled status to be reopened." | The invoice is not `canceled` | Nothing to reopen. For another status pick from decisions.md D16 |

**Sources:** [spec] reopenInvoice

### listInvoices
`client.invoices.list_invoices` · `GET /invoices.json` · contract: `map/operations/invoices.md`
**Always:** Request each nested array you need (`line_items=true`, ...) (R9). Use datetime filters only with `date_field` set to `created_at` or `updated_at`.

**Rules**
- Nested arrays (`line_items`, `payments`, `refunds`, ...) are omitted unless requested
  (`line_items=true`, ...). Datetime filters work only with `date_field=created_at|updated_at`.
- Legacy Statements sites returned `[{"invoice": {...}}]` live where Relationship Invoicing and the
  spec have `{"invoices": [...]}`, so the response fails to deserialize there [observed].

**Sources:** [spec] listInvoices · [observed]
