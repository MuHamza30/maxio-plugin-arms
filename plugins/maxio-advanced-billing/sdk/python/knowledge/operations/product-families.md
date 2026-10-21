# Product Families: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### createProductFamily
`client.product_families.create_product_family` · `POST /product_families.json` · contract: `map/operations/product_families.md`
**Always:** Set a stable `handle` you will keep (R6). Send `surcharging: false` if the family's products must not carry surcharges.

**Rules**
- The family is the container for products, components and coupons and must exist before them
  (lifecycles.md L1). The API has no archive or delete for families, so choose names and handles you
  will keep.
- Set a stable `handle`. The `handle:<handle>` form works only where the path parameter is a string:
  `create_product`, the component create operations and `list_products_for_product_family`. The coupon
  paths, `read_product_family`, `read_component`, `update_product_family_component`, `archive_component` and
  `list_components_for_product_family` type the family as an integer: pass the numeric id there.
- `surcharging` defaults to `true` when omitted (on sites with surcharging enabled); send `false` if
  the family's products must not carry surcharges.
- The "default product family" is the first non-archived one created; coupon find and validate fall
  back to it.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "API Handle: must be unique - that value has been taken." | A family with that handle exists | Find it with `list_product_families` (match `handle`) and reuse it |

**Sources:** [spec] createProductFamily, Create-Product-Family, listProductFamilies

### listProductsForProductFamily
`client.product_families.list_products_for_product_family` · `GET /product_families/{product_family_id}/products.json` · contract: `map/operations/product_families.md`

**Rules**
- This is how to list a family's plans: the path takes the numeric id or `handle:<family>`. Returns an
  array of `{"product": {...}}` wrappers. Page it (rules.md R8).
- Archived products are hidden unless `include_archived=true`.
- Currency is not a product field; read it from the site (`read_site`).

**Sources:** [spec] listProductsForProductFamily, product-family-id-path · [observed] list envelope, currency

### readProductFamily
`client.product_families.read_product_family` · `GET /product_families/{id}.json` · contract: `map/operations/product_families.md`

**Rules**
- Pass the numeric id. The spec's prose also offers `handle:my-family`, but the contract types `id` as
  an integer, so a handle cannot be sent through it.
- To find a family by its handle, call `list_product_families` and match `handle`.

**Sources:** [spec] readProductFamily, listProductFamilies
