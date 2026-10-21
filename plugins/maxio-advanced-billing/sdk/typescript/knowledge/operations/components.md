# Components: provider notes

On the new Catalog experience a UI "Product" (an add-on) is an API component (rules.md R18). Choose the
kind with decisions.md D10 before creating: it cannot be changed later. An operation of this group that
has no section here has no provider notes (see `../index.json`).

### createMeteredComponent
`client.components.createMeteredComponent` · `POST /product_families/{product_family_id}/metered_components.json` · contract: `map/operations/components.md`
**Always:** Send `unit_price` in decimal major units, not cents (R4). Send `prices` for any scheme other than `per_unit`, as contiguous, non-overlapping brackets. On new-Catalog sites give taxable components a `tax_code`.

**Before you call**
- Confirm the quantity resets every billing period (API calls, messages, minutes). If it persists
  (seats), use a quantity-based component.

**Rules**
- `unit_price` is decimal major units with up to 8 decimals (`0.0075`), not cents (rules.md R4).
- `prices` is optional only for `per_unit`; bracketed schemes need contiguous, non-overlapping brackets.
- Usage is reported with `createUsage`, one record per component per subscription; send one report per
  customer per day rather than one per event, to stay inside the rate limit.
- On new-Catalog sites a taxable component needs a non-blank `tax_code`; `"tax_code": ""` returns 422.
- Hybrid pricing is available on a metered component that is not event-based. Its overage block is not
  in the contract: see `createQuantityBasedComponent`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "At least 1 price bracket must be defined" | Bracketed scheme without `prices` | Add brackets |
| 422 "Pricing scheme: is not one of the allowed values." | Unknown scheme | Send a `pricing_scheme` value the contract lists |
| 422 "Must set tax type if taxes enabled" | Site taxes on, component taxable | Send tax settings / `tax_code` |

**Sources:** [spec] createMeteredComponent, Metered-Component · [docs] basic-concepts/product-catalog,
about-the-api/tips "Reporting Usage"

### createQuantityBasedComponent
`client.components.createQuantityBasedComponent` · `POST /product_families/{product_family_id}/quantity_based_components.json` · contract: `map/operations/components.md`
**Always:** Send `recurring: false` only for a one-time charge (inferred; D10). In `stairstep`, send each bracket's `unit_price` as the flat charge for the whole band (D17).

**Before you call**
- Decide recurring (seats, the quantity persists) or one-time (the quantity "immediately gets reset
  back to zero after the allocation is made"). `recurring: false` selects one-time *(inferred: the
  spec describes the two types but gives the field no description)*.
- `upgrade_charge` and `downgrade_credit` set this component's proration defaults. Left out, the
  value sent with an allocation applies, then the site setting (resolution order on
  `allocateComponent`).

**Rules**
- Quantities change through `allocateComponent`/`allocateComponents`; `listUsages` does not apply to
  this kind.
- In `stairstep`, a bracket's `unit_price` is the flat charge for the whole band, not a per-unit price
  [docs].
- On new-Catalog sites a taxable component needs a non-blank `tax_code`; `"tax_code": ""` returns 422.
- Hybrid pricing (an included allowance, then overage, on one invoice line) needs site flags only
  Maxio can enable. **Not in the contract:** the spec's prose names an `overage_pricing` parameter but
  the request declares no overage field, so the map does not show one. Maxio's guide sends
  `overage_pricing: {"pricing_scheme": ..., "prices": [...]}` here, and `overage_pricing_scheme` beside
  `overage_pricing.prices` on `createComponentPricePoint` [docs]. The same guide says a missing
  `overage_pricing_scheme` makes the block be ignored with no error; which form this request needs is
  not settled by the sources *(unconfirmed)*. Send the block as undeclared fields, then read the
  default price point back with `readComponentPricePoint` and tell the user if no overage pricing
  came back.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Unit name: cannot be blank." | Missing `unit_name` | Send a singular unit name |
| 422 "Pricing scheme cannot be per_unit for hybrid pricing" | An overage block beside a `per_unit` primary scheme (status not documented) | Use `volume`, `tiered` or `stairstep` as the primary scheme |
| 422 "Prices primary pricing must have a finite included threshold for hybrid pricing" | The top primary bracket has no `ending_quantity` (status not documented) | Set `ending_quantity` on the top bracket |

**Sources:** [spec] createQuantityBasedComponent, Quantity-Based-Component, allocateComponent · [docs]
basic-concepts/hybrid-pricing

### createOnOffComponent
`client.components.createOnOffComponent` · `POST /product_families/{product_family_id}/on_off_components.json` · contract: `map/operations/components.md`

**Rules**
- For a flat recurring add-on. Allocate only `1` or `0`.
- On new-Catalog sites a taxable component needs a non-blank `tax_code`; `"tax_code": ""` returns 422.

**Sources:** [spec] createOnOffComponent, createOffer

### createPrepaidUsageComponent
`client.components.createPrepaidUsageComponent` · `POST /product_families/{product_family_id}/prepaid_usage_components.json` · contract: `map/operations/components.md`

**Rules**
- Units are charged at purchase, with no proration. At allocation, `upgrade_charge`,
  `downgrade_credit` and `accrue_charge` "are ignored for Prepaid Components" (stated on
  `allocateComponent`).
- `expiration_interval` applies only with `rollover_prepaid_remainder: true`.
- On new-Catalog sites a taxable component needs a non-blank `tax_code`; a blank value is a
  validation error.

**Sources:** [spec] createPrepaidUsageComponent, Prepaid-Component, allocateComponent

### createEventBasedComponent
`client.components.createEventBasedComponent` · `POST /product_families/{product_family_id}/event_based_components.json` · contract: `map/operations/components.md`
**Always:** Follow with `activateEventBasedComponent` for each subscription that should be billed; events streamed without it produce no charge and no error.

**Rules**
- Events are billed only after `activateEventBasedComponent` for each subscription. Activation "only
  determines if the subscription should be billed for event-based component usage at renewal", and
  events can be streamed "at any time, regardless of component activation status". So events for a
  subscription that is not activated produce no charge and no error.
- Events go to a separate host (`https://events.chargify.com/{subdomain}/events/{api_handle}`), at
  most 1000 per bulk request.
- Duplicate prevention for events is not the body-root `uniqueness_token` of other writes (rules.md
  R12). It is `chargify.uniqueness_token`, nested inside each event: scoped per stream, at most 64
  characters, kept 31 days. A duplicate is "silently ignored", so a resend with the same token is
  safe and no 409 tells you it was a duplicate *(the missing 409 is inferred)*.
- On new-Catalog sites a taxable component needs a non-blank `tax_code`; a blank value is a
  validation error.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Metric: cannot be blank." | No metric attached | Send `event_based_billing_metric_id` |

**Sources:** [spec] createEventBasedComponent, activateEventBasedComponent, recordEvent,
bulkRecordEvents, Chargify-Ebb

### updateComponent
`client.components.updateComponent` · `PUT /components/{component_id}.json` · contract: `map/operations/components.md`

**Rules**
- Accepts descriptive, tax and accounting fields plus `handle` and `upgrade_charge` only. It cannot
  change kind or pricing: change pricing through component price points; change kind by creating a new
  component and moving subscribers.
- On new-Catalog sites a taxable component needs a non-blank `tax_code`; `"tax_code": ""` returns 422.

**Sources:** [spec] updateComponent, Update-Component

### archiveComponent
`client.components.archiveComponent` · `DELETE /product_families/{product_family_id}/components/{component_id}.json` · contract: `map/operations/components.md`

**Rules**
- Archives; subscribers "will continue to be charged as usual" (rules.md R17). No unarchive.
  `listSubscriptionComponents` still returns archived components on existing subscriptions, so keep
  them in any local catalog cache.

**Sources:** [spec] archiveComponent, listSubscriptionComponents
