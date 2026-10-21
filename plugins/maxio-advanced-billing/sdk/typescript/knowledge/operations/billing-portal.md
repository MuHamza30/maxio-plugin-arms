# Billing Portal: provider notes

An operation of this group that has no section here has no provider notes (see `../index.json`).

### enableBillingPortalForCustomer
`client.billingPortal.enableBillingPortalForCustomer` · `POST /portal/customers/{customer_id}/enable.json` · contract: `map/operations/billing-portal.md`
**Always:** Pass `auto_invite=1` if the customer should get the invitation email. Never enable twice; re-send the invite with `resendBillingPortalInvitation`.

**Rules**
- No invitation email is sent unless you pass `auto_invite=1`.
- Enabling twice is an error; to re-send the invite use `resendBillingPortalInvitation` (at most 5 per
  30 minutes).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Portal is already enabled for this customer." | The portal is already on for this customer | Nothing to enable. Match this exact message before you treat the portal as on: any other 422 is a rejection (rules.md R13). Use `resendBillingPortalInvitation` if the customer needs the email again |

**Sources:** [spec] enableBillingPortalForCustomer, resendBillingPortalInvitation

### readBillingPortalLink
`client.billingPortal.readBillingPortalLink` · `GET /portal/customers/{customer_id}/management_link.json` · contract: `map/operations/billing-portal.md`
**Always:** Cache the URL and reuse it until `new_link_available_at`; more than 15 requests before then are blocked with 429.

**Rules**
- Cache the management URL: it is valid for 65 days and a new one is generated only after 15 days
  (`new_link_available_at`). Do not call this on every page view.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Billing Portal is not enabled for this customer." | Portal not enabled | Call `enableBillingPortalForCustomer` |
| 429 "Too many requests for this customer's management link" | More than 15 requests before `new_link_available_at` | Serve the cached URL and do not retry. The body's `new_link_available_at` says when a new link can be requested |

**Sources:** [spec] readBillingPortalLink, enableBillingPortalForCustomer
