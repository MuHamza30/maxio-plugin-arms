# Product Features: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### createProductFeature
`client.ProductFeatures.CreateProductFeature` · `POST /products/{product_id}/features.json` · contract: `map/operations/ProductFeatures.md`
**Always:** Send `propagate_to_subscriptions: true` if existing subscribers should get the feature before their next subscription change. Send `value` as `"true"` or `"false"` for an access right, the limit itself for a usage limit.

**Before you call**
- The template exists and is not archived; the product id is numeric.

**Rules**
- `value` is `"true"` or `"false"` for an access right, and the limit itself (e.g. `"100"`) for a usage limit.
- Existing subscribers get the feature only "the next time their subscription changes" unless you send
  `propagate_to_subscriptions: true`.
- To scope to one price point, `price_point_type` is `"ProductPricePoint"` here (the component
  equivalent uses `"PricePoint"`, not "ComponentPricePoint"), plus `price_point_id`.
- Removing the item later keeps existing entitlements unless `destroy_entitlements=true`, which is
  permanent (`RemoveProductFeature`).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 404 | Product or feature template not found. An archived template is a likely cause *(inferred)* | Fix the ids, or restore the template with `RestoreFeatureTemplate` |

**Sources:** [spec] createProductFeature, Create-Feature-Catalog-Item-Request · [docs] basic-concepts/entitlements

### updateProductFeature
`client.ProductFeatures.UpdateProductFeature` · `PUT /products/{product_id}/features/{id}.json` · contract: `map/operations/ProductFeatures.md`
**Always:** Send `propagate_to_subscriptions: true` if existing subscribers must get the new value or periodicity. Left out, this call does not update the entitlements they already hold.

**Rules**
- `propagate_to_subscriptions: true` applies the new `value` or periodicity at once "to every
  existing entitlement created from this feature catalog item". It is off unless you send it, and
  then existing entitlements are not updated by this call. No error says so.
- When they do pick the change up is not stated *(by analogy with `CreateProductFeature`, at the
  subscriber's next subscription change; unconfirmed)*.
- After a change that must reach everyone, read one subscriber back with
  `ReadSubscriptionEntitlements`.

**Sources:** [spec] updateProductFeature, Update-Feature-Catalog-Item-Request

### removeProductFeature
`client.ProductFeatures.RemoveProductFeature` · `DELETE /products/{product_id}/features/{id}.json` · contract: `map/operations/ProductFeatures.md`
**Always:** Send `destroy_entitlements=true` only to revoke access for good: it permanently deletes the catalog item and every entitlement it created. Without it the item is archived and subscribers keep their entitlements.

**Rules**
- Decide which you mean. To stop selling the feature, send no flag: "the feature catalog item is
  archived and existing entitlements are preserved", and `RestoreProductFeature` brings the item
  back.
- To take the feature away from current subscribers, send `destroy_entitlements=true`: it
  "permanently deletes this feature catalog item and every entitlement it created, revoking
  subscriber access immediately". Nothing restores it.

**Sources:** [spec] removeProductFeature, restoreProductFeature · [docs] basic-concepts/entitlements
