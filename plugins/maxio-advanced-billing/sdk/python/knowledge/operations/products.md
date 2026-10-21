# Products: provider notes

On the new Catalog experience a UI "Plan" is an API product (rules.md R18). An operation of this group
that has no section here has no provider notes (see `../index.json`).

### createProduct
`client.products.create_product` · `POST /product_families/{product_family_id}/products.json` · contract: `map/operations/products.md`
**Always:** Set a `handle` (R6). For yearly billing send `interval: 12` with `interval_unit: "month"`. With a trial, set `trial_type` on purpose (L4). On new-Catalog sites never send `auto_create_signup_page`.

**Before you call**
- The family exists (id or `handle:<family>` in the path).
- Set a `handle` (R6).

**Rules**
- Prices are in cents (R4). There is no yearly unit: bill yearly as `interval: 12, interval_unit: "month"`.
- If the product has a trial, set `trial_type` on purpose: with no card at trial end, `no_obligation`
  goes quietly to `trial_ended`, `payment_expected` goes to `past_due` and starts dunning.
- On new-Catalog sites never send `auto_create_signup_page` (Maxio's own docs sample does): "If
  `auto_create_signup_page` is included (with any value) an error is returned."
- `require_credit_card` is a "Deprecated value that can be ignored unless you have legacy hosted
  pages" and does not make a signup cardless (rules.md R14). `request_credit_card` is response-only:
  the request does not declare it.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Auto Create Signup Page: is not allowed" | `auto_create_signup_page` sent on a new-Catalog site | Remove the field |
| 422 "Interval unit: must be 'month' or 'day'." | Another unit, such as `year` (documented on `create_product_price_point`; assumed here) | For yearly billing send `interval: 12` with `interval_unit: "month"` |
| 422 "Recurring Interval: must be greater than or equal to 1." | `interval` of 0 or a fraction (documented on `create_product_price_point`; assumed here) | Send an integer of 1 or more |
| 422 "Name: cannot be blank." | Missing `name` | Send it |

**Sources:** [spec] createProduct, createProductPricePoint, Create-or-Update-Product · [announcement]
2022-05-19 interval validation, 2026 new Catalog

### updateProduct
`client.products.update_product` · `PUT /products/{product_id}.json` · contract: `map/operations/products.md`
**Always:** Treat every call as creating a new price point and making it the product's default; never use it to change a price (D9). The body requires the price and interval fields: send the current values unchanged.

**Rules**
- Every update "will create a new price point and set it as the default price point for this
  product". The spec states this without a condition. Whether an update that changes only the name
  or the description also does so is unconfirmed: assume it does, and read
  `default_product_price_point_id` back afterwards.
- The request is the create model and requires `name`, `description`, `price_in_cents`, `interval`
  and `interval_unit`. To rename a plan you must still send them: read the product first and send its
  current price and interval unchanged. A guessed or zero price becomes the default price for every
  new signup.
- Do not use this to change a price. That is decisions.md D9: a new price point, then promote it.
- The path takes the product id only. To update by handle, resolve the id with `read_product_by_handle`
  first.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Name: cannot be blank." | `name` missing or empty | Send the product's current `name` |

**Sources:** [spec] updateProduct, Create-or-Update-Product

### readProductByHandle
`client.products.read_product_by_handle` · `GET /products/handle/{api_handle}.json` · contract: `map/operations/products.md`
**Always:** Pass the bare handle; never a `handle:` prefix in this path.

**Rules**
- Use this to read a product by handle: `read_product` takes a numeric id only. No `handle:` prefix in
  this path.

**Sources:** [spec] readProductByHandle

### archiveProduct
`client.products.archive_product` · `DELETE /products/{product_id}.json` · contract: `map/operations/products.md`

**Rules**
- Archives; it does not stop billing: "All current subscribers will be unaffected" (rules.md R17). No
  API unarchive exists for products.

**Sources:** [spec] archiveProduct
