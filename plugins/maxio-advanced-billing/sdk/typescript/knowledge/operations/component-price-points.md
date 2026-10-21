# Component Price Points: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### createComponentPricePoint
`client.componentPricePoints.createComponentPricePoint` · `POST /components/{component_id}/price_points.json` · contract: `map/operations/component-price-points.md`
**Always:** For `per_unit`, send `prices` as one open bracket: `[{"starting_quantity": 1, "unit_price": X}]`. Keep brackets contiguous and non-overlapping. Hybrid pricing also needs `overage_pricing_scheme`, or the overage block is ignored.

**Before you call**
- A `per_unit` price point still takes `prices`, as one open bracket:
  `[{"starting_quantity": 1, "unit_price": X}]`.

**Rules**
- Brackets must be contiguous and non-overlapping: each starts at the previous `ending_quantity + 1`;
  the top bracket may be open (`ending_quantity: null`).
- The new price point is not the default until promoted. `interval`/`interval_unit` only on
  Multifrequency sites.
- Hybrid pricing (an included allowance, then overage, on one invoice line) needs site flags only
  Maxio can enable. **Not in the contract:** the spec declares no overage field on a non-prepaid price
  point, so the map does not show one. Maxio's guide sends `overage_pricing_scheme` beside
  `overage_pricing: {"prices": [...]}` here [docs]. Without `overage_pricing_scheme` "the entire
  `overage_pricing` block is silently ignored" and a normal price point is created, with no error
  [docs]. Send both as undeclared fields, then read the price point back with
  `readComponentPricePoint` and tell the user if no overage pricing came back *(the spec documents the
  response's `overage_pricing_scheme` for prepaid components only, so what a hybrid price point
  returns is unconfirmed)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "There cannot be any overlapping bracket ranges" | Two brackets overlap | Fix the ranges |
| 422 "Successive brackets may not have gaps in quantity …" | A gap between two brackets | Start each bracket at the previous `ending_quantity + 1` |
| 422 "Handle: must begin with a letter or a number, have at least one letter in it, and contain only lowercase letters, numbers, dashes and underscores." | Bad `handle` | Lowercase letters, digits, `-`, `_`, at least one letter |
| 422 "Pricing scheme cannot be per_unit for hybrid pricing" | An overage block beside a `per_unit` primary scheme (status not documented) | Use `volume`, `tiered` or `stairstep` as the primary scheme |
| 422 "Prices primary pricing must have a finite included threshold for hybrid pricing" | The top primary bracket has no `ending_quantity` (status not documented) | Set `ending_quantity` on the top bracket |

**Sources:** [spec] createComponentPricePoint, Create-Component-Price-Point, Component-Price-Point ·
[docs] basic-concepts/hybrid-pricing

### updateComponentPricePoint
`client.componentPricePoints.updateComponentPricePoint` · `PUT /components/{component_id}/price_points/{price_point_id}.json` · contract: `map/operations/component-price-points.md`
**Always:** To change `prices`, get the bracket `id`s from `readComponentPricePoint`, then update or `_destroy: true` those; a fresh list is added beside the old one. For new customers only, create and promote a new price point (D9).

**Before you call**
- Call `readComponentPricePoint` to get the bracket `id`s. Custom price points are changed through the
  subscription, not here.

**Rules**
- In `prices`, a bracket without `id` is **added**, one with `id` is updated, and `id` with
  `_destroy: true` is removed. To replace a ladder, update or destroy the existing ids; a fresh list
  is added beside the old one.
- Every subscription on this price point is affected *(inferred: subscriptions reference the price
  point)*, and mid-period proration "uses the current price of the component" (stated on
  `allocateComponent`). For new-customers-only changes, create and promote a new price point.
- Hybrid overage fields work here as on `createComponentPricePoint` [docs] and, as there, are not in
  the contract.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "all prices must belong to the price point" | A bracket `id` from another price point. This was a 404 before 2021-10-01 [announcement] | Use this price point's ids |
| 422 "There cannot be any overlapping bracket ranges" | Brackets overlap. A fresh list sent beside the existing brackets is one way to get here *(inferred)* | Update or `_destroy` the existing ids |

**Sources:** [spec] updateComponentPricePoint, allocateComponent · [announcement] 2021-10-01 price point
error code · [docs] basic-concepts/hybrid-pricing

### promoteComponentPricePointToDefault
`client.componentPricePoints.promoteComponentPricePointToDefault` · `PUT /components/{component_id}/price_points/{price_point_id}/default.json` · contract: `map/operations/component-price-points.md`

**Rules**
- The new default "will apply to all new subscriptions going forward - existing subscriptions will
  remain on their current price point". Move existing subscribers with
  `bulkUpdateSubscriptionComponentsPricePoints` (`"_default"`) or
  `bulkResetSubscriptionComponentsPricePoints`. Usage reported without `price_point_id` goes to the
  current default.

**Sources:** [spec] promoteComponentPricePointToDefault

### archiveComponentPricePoint
`client.componentPricePoints.archiveComponentPricePoint` · `DELETE /components/{component_id}/price_points/{price_point_id}.json` · contract: `map/operations/component-price-points.md`

**Rules**
- Archiving moves nobody: "Subscriptions using a price point that has been archived will continue
  using it until they're moved to another price point" (rules.md R17). To move them, use
  `bulkUpdateSubscriptionComponentsPricePoints` or `bulkResetSubscriptionComponentsPricePoints`.
- Unlike a product or a component, a component price point can be brought back with
  `unarchiveComponentPricePoint`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Price point is already archived." | It is already archived | Nothing to archive. Match this exact message; any other 422 is a rejection (rules.md R13) |

**Sources:** [spec] archiveComponentPricePoint, unarchiveComponentPricePoint

### createCurrencyPrices
`client.componentPricePoints.createCurrencyPrices` · `POST /price_points/{price_point_id}/currency_prices.json` · contract: `map/operations/component-price-points.md`
**Always:** Send one row per price bracket of the price point (`price_id`) for the currency. `price` is in major units of that currency, like `unit_price`, not cents (R4).

**Before you call**
- The currency is already defined on the site, and the price point is not a custom one ("Currency
  Prices are not able to be created for custom price points").
- Call `readComponentPricePoint` for the bracket ids: each row's `price_id` is a bracket `id`.

**Rules**
- Currency prices "need to mirror the structure of your primary pricing": one row for each price level
  (bracket) of the price point.
- `price` is in major units *(inferred from the spec's response example, where `price: "123"` is shown
  as `€123,00`; the field's description gives no unit)*. Sending cents would overprice by 100 with no
  error *(inferred)*.
- The price point's `use_site_exchange_rate` defaults to `true`. Whether it must be `false` before the
  prices you define here are used is not stated *(unconfirmed)*.
- To change a price later use `updateCurrencyPrices` with the currency price `id`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Currency: is not one of the allowed values." | The currency is not defined on the site *(cause inferred from the message)* | Define the currency in the site's settings first (lifecycles.md L1) |
| 422 "Pricing already exists for this currency." | The price point already has prices in that currency (documented on `updateCurrencyPrices`; assumed here) | Change them with `updateCurrencyPrices` |

**Sources:** [spec] createCurrencyPrices, updateCurrencyPrices, Create-Currency-Price
