# Sites: provider notes

Site facts every integration reads once, and clearing a test site. An operation of this group that has
no section here has no provider notes (see `../index.json`).

### readSite
`client.Sites.ReadSite` · `GET /site.json` · contract: `map/operations/Sites.md`

**Rules**
- Call once at startup and keep three facts: `relationship_invoicing_enabled` (it decides which
  invoice-billing value of `payment_collection_method` is valid, `remittance` or `invoice`, and which
  operations exist, rules.md R3), the site's `currency` (currency is on the site and the
  subscription, not on the product), and `test` (refuse destructive test code unless it is `true`).
- `default_payment_collection_method` is what Maxio applies to a signup that sends no
  `payment_collection_method` *(inferred from the field's name: the spec gives it no description)*. It
  was `automatic` on the test site [observed]. Read it to explain a rejected signup, not to choose a
  method: every signup sends its own `payment_collection_method`, chosen by how the customer will pay
  (R14).
- Two more switches that other calls depend on: `schedule_subscription_cancellation_enabled`
  (`CancelSubscription`) and `allocation_settings` (`AllocateComponent`).

**Sources:** [spec] readSite, Site, Collection-Method · [observed] currency hard-coded as USD in
several runs; the site default on the test site

### clearSite
`client.Sites.ClearSite` · `POST /sites/clear_data.json` · contract: `map/operations/Sites.md`
**Always:** Call on test sites only. Choose `cleanup_scope`: `customers` keeps the catalog, `all` also removes products. Afterwards poll until clearing finishes before seeding fixtures.

**Rules**
- Test sites only: on a live site the answer is 403 [spec].
- It runs asynchronously. Until it finishes, every call to the site is rejected with the 422 below
  [docs]. That 422 is an account block, not a fault in the request (R13): wait, do not "fix" the call.
- `cleanup_scope=customers` keeps the catalog; `all` also removes products [spec].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 403 | The site is in live mode [spec] | Never clear a live site |
| 422 "Site data clearing is in progress. Please try later." | Clearing has not finished. Every call to the site answers this until it has [docs] | Wait, then poll a cheap read until it succeeds and the cleared lists are empty. Change nothing in the request |

**Sources:** [spec] clearSite · [docs] about-the-api/error-handling "API Access Limitations"
