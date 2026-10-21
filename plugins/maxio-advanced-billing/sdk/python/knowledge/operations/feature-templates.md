# Feature Templates: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### createFeatureTemplate
`client.feature_templates.create_feature_template` · `POST /features.json` · contract: `map/operations/feature_templates.md`
**Always:** Settle `key` and `kind` before creating: `key` is rejected on every later update, and `kind` once any feature catalog item uses the template.

**Before you call**
- Settle `key` and `kind`: `key` can never change, and `kind` cannot change once any catalog item
  uses the template. A wrong `kind` then means a new template.

**Rules**
- `usage_limit` needs `unit`; only it takes `default_periodicity_interval` and
  `default_periodicity_unit`, which are set together. `service_right` needs `value_type`.
- A template grants nothing until it is attached to a product or component (product-features.md).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Key can't be blank" | Missing `key` | Send it |
| 403 | Not stated: the spec declares the status with no body example *(unconfirmed)* | Check the site's feature access |

**Sources:** [spec] createFeatureTemplate, updateFeatureTemplate · [docs] basic-concepts/entitlements

### archiveFeatureTemplate
`client.feature_templates.archive_feature_template` · `DELETE /features/{id}.json` · contract: `map/operations/feature_templates.md`
**Always:** Send `remove_from_catalog=true` only to revoke access for good: it destroys the template's catalog items and their entitlements at once, and `restore_feature_template` does not bring them back.

**Rules**
- Without `remove_from_catalog`, the template and its feature catalog items are archived and
  "existing entitlements are preserved": subscribers keep their access.
- With `remove_from_catalog=true`, every feature catalog item made from the template is destroyed,
  and its entitlements with it, "revoking subscriber access immediately". That part is permanent:
  "restoring the template will not bring subscriber access back".
- An archived template answers 404 on `read_feature_template` and `update_feature_template` until
  `restore_feature_template`. Restoring the template does not restore its catalog items: restore each
  one afterwards (`restore_product_feature`, `restore_component_feature`).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 404 | No template has that `id`. An already archived template is a likely cause too *(inferred)* | Check the id |
| 403 | Not stated: the spec declares the status with no body example *(unconfirmed)* | Check the site's feature access |

**Sources:** [spec] archiveFeatureTemplate, restoreFeatureTemplate, restoreProductFeature · [docs]
basic-concepts/entitlements
