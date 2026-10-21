# Customers: provider notes

Notes for the Customers operations an integration most often calls. An operation of this group that
has no section here has no provider notes (see `../index.json`).

### readCustomerByReference
`client.customers.read_customer_by_reference` · `GET /customers/lookup.json` · contract: `map/operations/customers.md`

**Before you call**
- You need your own stable user id, stored as the customer's `reference` when you created it.

**Rules**
- This is the exact-match lookup: "It will return a single match." Use it, not the `q` search of
  `list_customers`, to decide whether a customer exists: `q` returns an array of matches, not one exact
  customer.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 404 | No customer has that reference (status not documented: the spec declares only 200; the 404 was seen in sandbox runs [observed]) | This is the lookup's normal "not there" answer: create the customer with that `reference` |

**Sources:** [spec] readCustomerByReference, listCustomers · [observed] the 404 on a miss

### createCustomer
`client.customers.create_customer` · `POST /customers.json` · contract: `map/operations/customers.md`
**Always:** If your app has a user id, send it as `reference`, call `read_customer_by_reference` first and create only on a 404. On the duplicate-reference 422, read the existing customer back (L2).

**Before you call**
- If your app has a stable user id: call `read_customer_by_reference` first, create only on a 404, and
  send that id as `reference`.
- With no id of your own you may leave `reference` out and store the `id` Maxio returns. That `id` is
  then your only key for the customer.

**Rules**
- `reference` must be unique and is "the only validation restriction". Email is not unique, so never
  deduplicate customers by email.
- Lookup-then-create is not atomic: two concurrent requests both see 404 and both try to create.
  Serialize per user in your own store, and on the duplicate-reference 422 read the existing customer
  back [observed].
- Send a `uniqueness_token` for this create, its own and not the one the signup's subscription create
  uses (rules.md R12).
- **Unknown outcome (rules.md R11).** The read-back is `read_customer_by_reference`, a unique reference
  you set, so every step of R11 applies, step 4 included. A second copy that lands anyway answers the
  duplicate-reference 422 below.
- Country is ISO 3166-1 alpha-2 and state ISO 3166-2. Send `entity_identifier_kind` together with any
  tax identifier value; `vat_eu` and `national_tax` also need `vat_country`. `surcharging` defaults to
  true.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 Reference: has already been taken | Another create won the race, or the user already exists. The text was seen in a sandbox and is not documented [observed] | Read the customer with `read_customer_by_reference` and continue with it |
| 422 "First name: cannot be blank." "Last name: cannot be blank." "Email address: cannot be blank." | A name or the email is missing | Send the missing field |
| 422 customer: can't be blank | The body has no `customer` object | Wrap the fields as `{"customer": {...}}` |
| 422 "Entity identifier kind: is not one of the allowed values." | An identifier sent with an unsupported kind | Send a supported `entity_identifier_kind` with the value |

**Sources:** [spec] createCustomer · [observed] duplicate-reference race

### updateCustomer
`client.customers.update_customer` · `PUT /customers/{id}.json` · contract: `map/operations/customers.md`
**Always:** Pass the Maxio customer `id`, not your reference. Never send `entity_identifier_value` without `entity_identifier_kind`. The `vat_eu` and `national_tax` kinds also need `vat_country`; the other kinds do not.

**Before you call**
- You need the Maxio customer `id`, not the reference: resolve it with `read_customer_by_reference` first.

**Rules**
- Changing `reference` is allowed and it must stay unique.
- Send `entity_identifier_kind` and `entity_identifier_value` together: "Always send the kind."
  `vat_eu` and `national_tax` also require `vat_country`. The other kinds do not, so do not invent
  one: a different `vat_country` beside an unchanged pair "is a real edit, so it is validated and can
  return `422`".
- Sending a customer response straight back leaves the tax identifier unchanged. Changing only
  `vat_number` re-derives the kind, turning `gln`/`duns`/`lei` into `company_reg`.
- To clear an identifier, send a supported kind with a blank `entity_identifier_value`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 404 | No customer has that `id` | Resolve the id with `read_customer_by_reference` |
| 422 "Entity identifier kind: is not one of the allowed values." | An unsupported `entity_identifier_kind` | Send a supported kind with the value |
| 422 | A missing or mismatched `vat_country`, a `gln`, `duns` or `lei` value in the wrong format, or a value sent with no kind beside a `vat_country` (messages not documented) | Send kind and value together. Add `vat_country` only for `vat_eu` and `national_tax`, and check the value's format for its kind |

**Sources:** [spec] updateCustomer, Entity-Identifier-Kind

### listCustomers
`client.customers.list_customers` · `GET /customers.json` · contract: `map/operations/customers.md`
**Always:** Never take the first result of a `q` search as the customer; use `read_customer_by_reference` for an exact match. For incremental sync send `date_field` with a start and an end; an unrecognized `date_field` is ignored (R9).

**Rules**
- `q` searches email, id, reference, organization and name and returns an array of matches: never
  take the first one as "the" customer.
- For incremental sync, filter with `date_field` plus a start and an end. An unrecognized `date_field`
  is ignored and the full set comes back (rules.md R9) [announcement].
- Page until a page comes back empty (rules.md R8).

**Sources:** [spec] listCustomers · [announcement] 2020-12-18 date_field validation · [docs]
about-the-api/tips "Synchronizing Your Database"

### listCustomerSubscriptions
`client.customers.list_customer_subscriptions` · `GET /customers/{customer_id}/subscriptions.json` · contract: `map/operations/customers.md`

**Rules**
- The spec declares no paging parameters on this list *(an experiment analysis claims it truncates at
  20; unconfirmed)*. If a customer can hold many subscriptions, reconcile with `list_subscriptions`
  filtered by `customer_id` instead.
- Subscriptions in End of Life (not billing) states are returned too; filter by `state` using
  lifecycles.md L3.
- On new-Catalog sites a subscription can have no product. Then "'product', 'product_price_point_id',
  and 'product_price_point_type' are returned as 'null'": check for null before you read `product`.

**Sources:** [spec] listCustomerSubscriptions, listSubscriptions · [observed]
