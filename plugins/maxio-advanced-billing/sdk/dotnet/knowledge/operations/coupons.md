# Coupons: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### createCoupon
`client.Coupons.CreateCoupon` · `POST /product_families/{product_family_id}/coupons.json` · contract: `map/operations/Coupons.md`
**Always:** Send exactly one of `percentage` or `amount_in_cents`. Never send a past `end_date`. Put `restricted_products` / `restricted_components` beside `coupon`, not inside it, and never with `allow_negative_balance: true`.

**Before you call**
- Choose the family: coupon lookups are scoped to a family. Decide percentage or amount, recurring or
  not, stackable or not.

**Rules**
- Send exactly one of `percentage` or `amount_in_cents` (integer cents, never negative).
- `end_date` stops only **new** uses: "Recurring discounts started before this date will continue to
  recur even after this date." It cannot be in the past (Maxio's own docs sample uses 2012 and fails).
- Only `stackable: true` coupons combine. `compounding_strategy` applies to stackable percentage coupons:
  `compound` applies after earlier discounts, `full-price` to the original price.
- `restricted_products` / `restricted_components` go beside `coupon`, not inside it, and cannot be
  combined with `allow_negative_balance: true`. Sending `allow_negative_balance: false` with
  restrictions is fine: the spec's own example does.
- Codes: up to 255 uppercase letters, digits and `% @ + - _ .`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Expiration Date cannot be in the past" | Past `end_date` | Send a future date, or leave `end_date` out |
| 422 "Code: must be unique - that value has been taken." | Duplicate code (documented on `UpdateCoupon`; assumed here) | Reuse the existing coupon or pick another code |
| 422 "Amount: must be greater than or equal to $0.00." | Negative amount (documented on `UpdateCoupon`; assumed here) | Send 0 or more |

**Sources:** [spec] createCoupon, updateCoupon, Coupon-Payload · [announcement] 2020-01-16 coupon
validation

### validateCoupon
`client.Coupons.ValidateCoupon` · `GET /coupons/validate.json` · contract: `map/operations/Coupons.md`
**Always:** Pass `product_family_id` unless the coupon is in the default product family (D18).

**Rules**
- Searches the **default** product family unless you pass `product_family_id`; the same code can exist
  in several families. Read the coupon's restrictions and `end_date` before showing a discount.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 404 "Coupon code could not be found." | Unknown code, or the coupon lives in another product family | Pass `product_family_id`. The code is not proven invalid until the right family was searched |

**Sources:** [spec] validateCoupon, findCoupon

### findCoupon
`client.Coupons.FindCoupon` · `GET /coupons/find.json` · contract: `map/operations/Coupons.md`
**Always:** Pass `product_family_id` unless the coupon is in the default product family.

**Rules**
- Same family scoping as `ValidateCoupon`.

**Sources:** [spec] findCoupon

### updateCouponSubcodes
`client.Coupons.UpdateCouponSubcodes` · `PUT /coupons/{coupon_id}/codes.json` · contract: `map/operations/Coupons.md`
**Always:** Use only to replace every subcode, and send the complete list. To add codes use `CreateCouponSubcodes` (D18).

**Rules**
- **Deletes every existing subcode** and then adds the list. To add codes use `CreateCouponSubcodes`.
  Responses list created, already-existing and invalid codes separately instead of failing.
- Send the codes in the body as plain strings, not percent-encoded. The encoding rule is for a subcode
  in a URL path only (`DeleteCouponSubcode`) *(inferred: the spec states it "for use in the URL")*.

**Sources:** [spec] updateCouponSubcodes, createCouponSubcodes

### createCouponSubcodes
`client.Coupons.CreateCouponSubcodes` · `POST /coupons/{coupon_id}/codes.json` · contract: `map/operations/Coupons.md`

**Rules**
- Adds codes; subcodes are uppercased automatically. Check the response for codes reported invalid.

**Sources:** [spec] createCouponSubcodes

### deleteCouponSubcode
`client.Coupons.DeleteCouponSubcode` · `DELETE /coupons/{coupon_id}/codes/{subcode}.json` · contract: `map/operations/Coupons.md`

**Rules**
- The subcode travels in the URL path, so its special characters must reach Maxio percent-encoded:
  `%` as `%25`, `@` as `%40`, `+` as `%2B`, `-` as `%2D`, `_` as `%5F`, `.` as `%2E`. The subcode
  `20%OFF` is deleted at `/coupons/567/codes/20%25OFF.json`.
- Look at what your HTTP client puts on the wire before encoding by hand. Encoding twice sends
  `%2525`, and common URL encoders leave `-`, `_` and `.` alone *(inferred)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 404 | No such subcode on this coupon. A wrongly encoded subcode would give the same answer *(inferred)* | Compare with the coupon's subcodes from `ListCouponSubcodes` |

**Sources:** [spec] deleteCouponSubcode, createCouponSubcodes

### archiveCoupon
`client.Coupons.ArchiveCoupon` · `DELETE /product_families/{product_family_id}/coupons/{coupon_id}.json` · contract: `map/operations/Coupons.md`

**Rules**
- Coupons already on subscriptions "remain attached and functional" (rules.md R17). To end a running
  recurring discount, call `RemoveCouponFromSubscription` for each of those subscriptions. No
  unarchive.

**Sources:** [spec] archiveCoupon, removeCouponFromSubscription
