# Product Price Points: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### createProductPricePoint
`client.product_price_points.create_product_price_point` · `POST /products/{product_id}/price_points.json` · contract: `map/operations/product_price_points.md`
**Always:** Settle `interval`, the trial fields and `initial_charge_in_cents` now: `update_product_price_point` takes only `price_in_cents` and `handle`. Promote the price point if new signups should get it (D9).

**Before you call**
- Settle `interval`, `interval_unit`, the trial fields and `initial_charge_in_cents` now (see Rules).

**Rules**
- A new price point is not the default; promote it explicitly if new signups should get it.
- `update_product_price_point` declares only `price_in_cents` and `handle`, so the interval, the trial
  and `initial_charge_in_cents` cannot be edited later *(inferred from that schema; whether other
  fields are ignored or rejected is not stated)*. Get them right now or create another price point.
- `use_site_exchange_rate` defaults to `true`. Each currency price must mirror the baseline (and trial
  and initial roles, if set); add them with `create_product_currency_prices`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 price_point: can't be blank | The body has no `price_point` object | Wrap the fields as `{"price_point": {...}}` |
| 422 "Recurring Interval: must be greater than or equal to 1." | `interval` below 1 or fractional | Send an integer of 1 or more |
| 422 "Price: must be greater than or equal to 0." | Negative price | Send 0 or more |

**Sources:** [spec] createProductPricePoint, Create-Product-Price-Point, Update-Product-Price-Point ·
[announcement] 2022-05-19 interval validation

### promoteProductPricePointToDefault
`client.product_price_points.promote_product_price_point_to_default` · `PATCH /products/{product_id}/price_points/{price_point_id}/default.json` · contract: `map/operations/product_price_points.md`

**Rules**
- Affects new signups and anything that falls back to the default (offers and migrations without a
  price point). Existing subscribers stay on their current price point until you move them with
  `migrate_subscription_product` *(inferred: the spec states this for component price points only)*.
- Promote before archiving the old default. Custom (per-subscription) price points cannot be promoted.

**Sources:** [spec] promoteProductPricePointToDefault, promoteComponentPricePointToDefault

### updateProductPricePoint
`client.product_price_points.update_product_price_point` · `PUT /products/{product_id}/price_points/{price_point_id}.json` · contract: `map/operations/product_price_points.md`
**Always:** This reprices every subscription on the price point (inferred). For new customers only, create and promote a new price point instead (D9).

**Rules**
- Accepts only `price_in_cents` and `handle`. Changing the price in place reaches **every**
  subscription on this price point *(inferred: subscriptions reference the price point)*. For "new
  customers only", create and promote a new price point instead (decisions.md D9).
- Custom price points cannot be updated here; change them through the subscription.

**Sources:** [spec] updateProductPricePoint, Update-Product-Price-Point

### listProductPricePoints
`client.product_price_points.list_product_price_points` · `GET /products/{product_id}/price_points.json` · contract: `map/operations/product_price_points.md`
**Always:** Never take `[0]` as the default; use `filter[type]=default` or the product's `default_product_price_point_id` (R9). Request at most 200 per page (R8).

**Rules**
- Newest first (DESC `created_at`): the default is **not** `[0]`. Use `filter[type]=default` or the
  product's `default_product_price_point_id`.
- Archived price points appear only with `archived`.

**Sources:** [spec] listProductPricePoints · [announcement] 2020-01-27 price point order

### archiveProductPricePoint
`client.product_price_points.archive_product_price_point` · `DELETE /products/{product_id}/price_points/{price_point_id}.json` · contract: `map/operations/product_price_points.md`

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Cannot archive the default price point." | Target is the default | Promote another price point first |

**Sources:** [spec] archiveProductPricePoint

### createProductCurrencyPrices
`client.product_price_points.create_product_currency_prices` · `POST /product_price_points/{product_price_point_id}/currency_prices.json` · contract: `map/operations/product_price_points.md`
**Always:** Send `price` in major units of the currency, not cents, although the price point itself is in cents (R4). Send a `baseline` row, plus a `trial` and an `initial` row when the price point has a trial or an initial charge.

**Before you call**
- The currency is defined on the site, and the price point is not a custom one ("Currency Prices are
  not able to be created for custom product price points").

**Rules**
- `price` here is in major units *(inferred from the spec's response example, which shows
  `price: 123` as `€123,00`; the field's description gives no unit)*. The price point beside it is in
  cents (`price_in_cents`), so a copied cents value would overprice by 100 with no error
  *(inferred)*.
- The contract types `price` as an integer here, so a price with a fraction cannot be sent through
  it *(whether the API takes a decimal is unconfirmed)*.
- The rows must mirror the price point: "If the product price point defines a trial and/or setup
  fee, each currency must also define a trial and/or setup fee." That is one row per `role`:
  `baseline` always, `trial` and `initial` when the price point has them.
- The price point's `use_site_exchange_rate` defaults to `true`. Whether it must be `false` before
  the prices you define here are used is not stated *(unconfirmed)*.
- Change a price later with `update_product_currency_prices` and the currency price `id`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "This product price point requires that prices are defined for: …" | A role the price point has is missing for the currency. The message lists the missing roles, such as `[baseline]` | Send one row for each role the price point defines |

**Sources:** [spec] createProductCurrencyPrices, Create-Product-Currency-Price, Currency-Price-Role
