# Offers: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### createOffer
`client.Offers.CreateOffer` · `POST /offers.json` · contract: `map/operations/Offers.md`

**Before you call**
- The product, its components and coupons exist.

**Rules**
- An offer bundles a product (optionally a price point), components with a `starting_quantity`, and
  coupons by **code**. Without `product_price_point_id` it uses the product's default.
- There is no update operation for offers: to change one, archive it and create a new offer *(the
  remedy is inferred)*. A coupon in an active offer cannot have its code changed.
- Subscribe with `offer_id` (id or `handle:`) in place of product and component data.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "starting_quantity for an On/Off component can only be '1' or '0': …" | An on/off component with a `starting_quantity` above 1. The message ends with the component id | Send 0 or 1 |

**Sources:** [spec] createOffer, Create-Offer, updateCoupon
