# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [MaxioAdvancedBillingClient](maxio_advanced_billing/client.py)

## ApiExports

> Source: [ApiExports](maxio_advanced_billing/apis/api_exports.py)

<details>
<summary><code>def export_invoices(*, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an invoices export and returns a batch job object.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.export_invoices()
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExportInvoicesErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.export_invoices()
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExportInvoicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchJobResponse](maxio_advanced_billing/models/batch_job_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ExportInvoicesErrorBody](maxio_advanced_billing/errors/export_invoices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 409 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def export_proforma_invoices(*, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a proforma invoices export and returns a batch job object. Proforma invoices are only available on Relationship Invoicing sites.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.export_proforma_invoices()
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExportProformaInvoicesErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.export_proforma_invoices()
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExportProformaInvoicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchJobResponse](maxio_advanced_billing/models/batch_job_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ExportProformaInvoicesErrorBody](maxio_advanced_billing/errors/export_proforma_invoices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 409 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def export_subscriptions(*, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a subscriptions export and returns a batch job object.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.export_subscriptions()
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExportSubscriptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.export_subscriptions()
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExportSubscriptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchJobResponse](maxio_advanced_billing/models/batch_job_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ExportSubscriptionsErrorBody](maxio_advanced_billing/errors/export_subscriptions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 409 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_exported_invoices(batch_id: str, *, per_page: int | None = 100, page: int | None = 1, request_options: RequestOptionsOrDict | None = None) -> list[Invoice]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists exported invoices for a provided `batch_id`. Use pagination to control responses returned from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.list_exported_invoices("some example string", page=1)
    # TODO: Handle 'response' of type list[Invoice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExportedInvoicesErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.list_exported_invoices("some example string", page=1)
    # TODO: Handle 'response' of type list[Invoice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExportedInvoicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>batch_id</code> | <code>str</code> | Id of a Batch Job. |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. <br>Default value is 100. <br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br>**Default**: <code>100</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Invoice](maxio_advanced_billing/models/invoice.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListExportedInvoicesErrorBody](maxio_advanced_billing/errors/list_exported_invoices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_exported_proforma_invoices(batch_id: str, *, per_page: int | None = 100, page: int | None = 1, request_options: RequestOptionsOrDict | None = None) -> list[ProformaInvoice]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists exported proforma invoices for a provided `batch_id`. Use pagination to control responses returned from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.list_exported_proforma_invoices("some example string", page=1)
    # TODO: Handle 'response' of type list[ProformaInvoice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExportedProformaInvoicesErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.list_exported_proforma_invoices("some example string", page=1)
    # TODO: Handle 'response' of type list[ProformaInvoice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExportedProformaInvoicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>batch_id</code> | <code>str</code> | Id of a Batch Job. |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. <br>Default value is 100. <br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br>**Default**: <code>100</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ProformaInvoice](maxio_advanced_billing/models/proforma_invoice.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListExportedProformaInvoicesErrorBody](maxio_advanced_billing/errors/list_exported_proforma_invoices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_exported_subscriptions(batch_id: str, *, per_page: int | None = 100, page: int | None = 1, request_options: RequestOptionsOrDict | None = None) -> list[Subscription]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists exported subscriptions for a provided `batch_id`. Use pagination to control responses returned from the server.

Example: `GET https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.list_exported_subscriptions("some example string", page=1)
    # TODO: Handle 'response' of type list[Subscription]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExportedSubscriptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.list_exported_subscriptions("some example string", page=1)
    # TODO: Handle 'response' of type list[Subscription]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExportedSubscriptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>batch_id</code> | <code>str</code> | Id of a Batch Job. |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. <br>Default value is 100. <br>The maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.<br>**Default**: <code>100</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Subscription](maxio_advanced_billing/models/subscription.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListExportedSubscriptionsErrorBody](maxio_advanced_billing/errors/list_exported_subscriptions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_invoices_export(batch_id: str, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a batch job object for an invoices export.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.read_invoices_export("some example string")
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadInvoicesExportErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.read_invoices_export("some example string")
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadInvoicesExportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>batch_id</code> | <code>str</code> | Id of a Batch Job. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchJobResponse](maxio_advanced_billing/models/batch_job_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadInvoicesExportErrorBody](maxio_advanced_billing/errors/read_invoices_export_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_proforma_invoices_export(batch_id: str, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a batch job object for a proforma invoices export. Proforma invoices are only available on Relationship Invoicing sites.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.read_proforma_invoices_export("some example string")
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadProformaInvoicesExportErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.read_proforma_invoices_export("some example string")
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadProformaInvoicesExportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>batch_id</code> | <code>str</code> | Id of a Batch Job. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchJobResponse](maxio_advanced_billing/models/batch_job_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadProformaInvoicesExportErrorBody](maxio_advanced_billing/errors/read_proforma_invoices_export_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_subscriptions_export(batch_id: str, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a batch job object for a subscriptions export.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api_exports.read_subscriptions_export("some example string")
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadSubscriptionsExportErrorBody
```

**Async**

```python
try:
    response = await async_client.api_exports.read_subscriptions_export("some example string")
    # TODO: Handle 'response' of type BatchJobResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadSubscriptionsExportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>batch_id</code> | <code>str</code> | Id of a Batch Job. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchJobResponse](maxio_advanced_billing/models/batch_job_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadSubscriptionsExportErrorBody](maxio_advanced_billing/errors/read_subscriptions_export_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## AdvanceInvoice

> Source: [AdvanceInvoice](maxio_advanced_billing/apis/advance_invoice.py)

<details>
<summary><code>def issue_advance_invoice(subscription_id: int, *, body: IssueAdvanceInvoiceRequest | IssueAdvanceInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Issues an invoice in advance for a subscription's next renewal date. For the most part, advance invoices function like any other invoice, except they are issued early and have special behavior upon being voided. For more information on advance invoices, including eligibility for generating one, see [Issue Invoice In Advance](https://maxio.zendesk.com/hc/en-us/articles/24252026404749-Issue-Invoice-In-Advance).

A subscription can only have one advance invoice per billing period. Attempting to issue an advance invoice when one already exists returns an error.

Regeneration of the invoice can be forced with the params `force: true`, which voids an advance invoice if one exists and generates a new one. If no advance invoice exists, a new one is generated.

Consider using either the create or preview endpoints for proforma invoices to preview this advance invoice before using this endpoint to generate it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.advance_invoice.issue_advance_invoice(1, body=IssueAdvanceInvoiceRequest(force=True))
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueAdvanceInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.advance_invoice.issue_advance_invoice(1, body=IssueAdvanceInvoiceRequest(force=True))
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueAdvanceInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[IssueAdvanceInvoiceRequest](maxio_advanced_billing/models/issue_advance_invoice_request.py) \| [IssueAdvanceInvoiceRequestDict](maxio_advanced_billing/models/issue_advance_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[IssueAdvanceInvoiceErrorBody](maxio_advanced_billing/errors/issue_advance_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_advance_invoice(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the advance invoice generated for a subscription's upcoming renewal. There can only be one advance invoice per subscription per billing cycle.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.advance_invoice.read_advance_invoice(1)
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadAdvanceInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.advance_invoice.read_advance_invoice(1)
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadAdvanceInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadAdvanceInvoiceErrorBody](maxio_advanced_billing/errors/read_advance_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def void_advance_invoice(subscription_id: int, *, body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Voids a subscription's existing advance invoice. Once voided, it can later be regenerated if desired.

A `reason` is required to void, and the invoice must have an open status. Voiding causes any prepayments and credits that were applied to the invoice to be returned to the subscription.

For a full overview of the impact of voiding, see [Invoice]($m/Invoice).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.advance_invoice.void_advance_invoice(1)
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidAdvanceInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.advance_invoice.void_advance_invoice(1)
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidAdvanceInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[VoidInvoiceRequest](maxio_advanced_billing/models/void_invoice_request.py) \| [VoidInvoiceRequestDict](maxio_advanced_billing/models/void_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[VoidAdvanceInvoiceErrorBody](maxio_advanced_billing/errors/void_advance_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## BillingPortal

> Source: [BillingPortal](maxio_advanced_billing/apis/billing_portal.py)

<details>
<summary><code>def enable_billing_portal_for_customer(customer_id: int, *, auto_invite: AutoInviteOrInt | None = None, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables Billing Portal access for a customer, with an option to send an invitation email at the same time.

## Billing Portal Security

If your customer has been invited to the Billing Portal, they receive a link to manage their subscription (the “Management URL”) automatically at the bottom of their statements, invoices, and receipts. **This link changes periodically for security and is only valid for 65 days.**

If you need to provide your customer their Management URL through other means, you can retrieve it [via the API]($e/Billing%20Portal/readBillingPortalLink). Because the URL is cryptographically signed with a timestamp, merchants cannot generate the URL without requesting it through the API.

To prevent abuse and overuse, request a new URL only when absolutely necessary. Management URLs are good for 65 days, so you should re-use a previously generated one as much as possible. If you use the URL frequently (such as to display on your website), **do not** make an API request every time.

For more information configuring the Billing Portal, see [Billing Portal Overview](https://maxio.zendesk.com/hc/en-us/articles/24252412965133-Billing-Portal-Overview).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing_portal.enable_billing_portal_for_customer(1)
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableBillingPortalForCustomerErrorBody
```

**Async**

```python
try:
    response = await async_client.billing_portal.enable_billing_portal_for_customer(1)
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableBillingPortalForCustomerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>int</code> | The Chargify id of the customer |
| <code>auto_invite</code> | <code>[AutoInviteOrInt](maxio_advanced_billing/models/enums/auto_invite.py) \| None</code> | When set to 1, an Invitation email will be sent to the Customer.<br>When set to 0, or not sent, an email will not be sent.<br>Use in query: `auto_invite=1`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CustomerResponse](maxio_advanced_billing/models/customer_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[EnableBillingPortalForCustomerErrorBody](maxio_advanced_billing/errors/enable_billing_portal_for_customer_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_billing_portal_link(customer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> PortalManagementLink</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the exact URL required for a subscriber to access the Billing Portal.

## Management Link Request Rules

+ When retrieving a management URL, multiple requests for the same customer in a short period return the **same** URL
+ A new URL is not generated for 15 days
+ You must cache and remember this URL if you are going to need it again within 15 days
+ Only request a new URL after the `new_link_available_at` date
+ You are limited to 15 requests for the same URL. If you make more than 15 requests before `new_link_available_at`, you are blocked from further Management URL requests (with a response code `429`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing_portal.read_billing_portal_link(1)
    # TODO: Handle 'response' of type PortalManagementLink
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadBillingPortalLinkErrorBody
```

**Async**

```python
try:
    response = await async_client.billing_portal.read_billing_portal_link(1)
    # TODO: Handle 'response' of type PortalManagementLink
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadBillingPortalLinkErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>int</code> | The Chargify id of the customer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PortalManagementLink](maxio_advanced_billing/models/portal_management_link.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadBillingPortalLinkErrorBody](maxio_advanced_billing/errors/read_billing_portal_link_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 429 | <code>[TooManyManagementLinkRequestsError1](maxio_advanced_billing/models/too_many_management_link_requests_error1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def resend_billing_portal_invitation(customer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ResentInvitation</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Resends a customer's Billing Portal invitation.

If you attempt to resend an invitation 5 times within 30 minutes, you will receive a `422` response with an `error` message in the body.

If you attempt to resend an invitation when the Billing Portal is already disabled for a Customer, you will receive a `422` error response.

If you attempt to resend an invitation when the Customer does not exist, you will receive a `404` error response.

## Limitations

This endpoint will only return a JSON response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing_portal.resend_billing_portal_invitation(1)
    # TODO: Handle 'response' of type ResentInvitation
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResendBillingPortalInvitationErrorBody
```

**Async**

```python
try:
    response = await async_client.billing_portal.resend_billing_portal_invitation(1)
    # TODO: Handle 'response' of type ResentInvitation
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResendBillingPortalInvitationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>int</code> | The Chargify id of the customer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ResentInvitation](maxio_advanced_billing/models/resent_invitation.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ResendBillingPortalInvitationErrorBody](maxio_advanced_billing/errors/resend_billing_portal_invitation_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def revoke_billing_portal_access(customer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> RevokedInvitation</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Revokes a customer's Billing Portal invitation.

If you attempt to revoke an invitation when the Billing Portal is already disabled for a Customer, you will receive a 422 error response.

## Limitations

This endpoint will only return a JSON response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing_portal.revoke_billing_portal_access(1)
    # TODO: Handle 'response' of type RevokedInvitation
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.billing_portal.revoke_billing_portal_access(1)
    # TODO: Handle 'response' of type RevokedInvitation
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>int</code> | The Chargify id of the customer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RevokedInvitation](maxio_advanced_billing/models/revoked_invitation.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ComponentFeatures

> Source: [ComponentFeatures](maxio_advanced_billing/apis/component_features.py)

<details>
<summary><code>def create_component_feature(component_id: int, *, body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Attaches a feature template to this component with a concrete value. Pass `price_point_type: "PricePoint"` and `price_point_id` to create an override scoped to a single component price point instead of the whole component.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_features.create_component_feature(1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateComponentFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.component_features.create_component_feature(1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateComponentFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component. |
| <code>body</code> | <code>[CreateFeatureCatalogItemRequest](maxio_advanced_billing/models/create_feature_catalog_item_request.py) \| [CreateFeatureCatalogItemRequestDict](maxio_advanced_billing/models/create_feature_catalog_item_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateComponentFeatureErrorBody](maxio_advanced_billing/errors/create_component_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_component_features(component_id: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemsListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the feature catalog items attached to this component, including price-point-specific overrides.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_features.list_component_features(1)
    # TODO: Handle 'response' of type FeatureCatalogItemsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListComponentFeaturesErrorBody
```

**Async**

```python
try:
    response = await async_client.component_features.list_component_features(1)
    # TODO: Handle 'response' of type FeatureCatalogItemsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListComponentFeaturesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemsListResponse](maxio_advanced_billing/models/feature_catalog_items_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListComponentFeaturesErrorBody](maxio_advanced_billing/errors/list_component_features_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_component_feature(component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single feature catalog item attached to this component.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_features.read_component_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadComponentFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.component_features.read_component_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadComponentFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadComponentFeatureErrorBody](maxio_advanced_billing/errors/read_component_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_component_feature(component_id: int, id_: int, *, destroy_entitlements: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a feature catalog item from this component.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.component_features.remove_component_feature(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveComponentFeatureErrorBody
```

**Async**

```python
try:
    await async_client.component_features.remove_component_feature(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveComponentFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>destroy_entitlements</code> | <code>bool \| None</code> | When `true`, permanently deletes this feature catalog item and every entitlement it created, revoking subscriber access immediately. When `false` (default), the feature catalog item is archived and existing entitlements are preserved.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RemoveComponentFeatureErrorBody](maxio_advanced_billing/errors/remove_component_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def restore_component_feature(component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Clears the archived state of a feature catalog item attached to this component. Returns `422` if the parent feature template is still archived. Restore the feature template first.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_features.restore_component_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreComponentFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.component_features.restore_component_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreComponentFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RestoreComponentFeatureErrorBody](maxio_advanced_billing/errors/restore_component_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_component_feature(component_id: int, id_: int, *, body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the value or periodicity of a feature catalog item attached to this component.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_features.update_component_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateComponentFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.component_features.update_component_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateComponentFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>body</code> | <code>[UpdateFeatureCatalogItemRequest](maxio_advanced_billing/models/update_feature_catalog_item_request.py) \| [UpdateFeatureCatalogItemRequestDict](maxio_advanced_billing/models/update_feature_catalog_item_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateComponentFeatureErrorBody](maxio_advanced_billing/errors/update_component_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ComponentPricePoints

> Source: [ComponentPricePoints](maxio_advanced_billing/apis/component_price_points.py)

<details>
<summary><code>def archive_component_price_point(component_id: ComponentIdModel | ComponentIdModelDict, price_point_id: PricePointIdModel | PricePointIdModelDict, *, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives a component price point. Subscriptions using a price point that has been archived will continue using it until they're moved to another price point.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.archive_component_price_point(1, 1)
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveComponentPricePointErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.archive_component_price_point(1, 1)
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveComponentPricePointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>[ComponentIdModel](maxio_advanced_billing/models/unions/component_id_model.py) \| [ComponentIdModelDict](maxio_advanced_billing/models/unions/component_id_model.py)</code> | The id or handle of the component. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle. |
| <code>price_point_id</code> | <code>[PricePointIdModel](maxio_advanced_billing/models/unions/price_point_id_model.py) \| [PricePointIdModelDict](maxio_advanced_billing/models/unions/price_point_id_model.py)</code> | The id or handle of the price point. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a string handle. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointResponse](maxio_advanced_billing/models/component_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ArchiveComponentPricePointErrorBody](maxio_advanced_billing/errors/archive_component_price_point_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_create_component_price_points(component_id: str, *, body: CreateComponentPricePointsRequest | CreateComponentPricePointsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates multiple component price points in one request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.bulk_create_component_price_points(
        "some example string",
        body=CreateComponentPricePointsRequest(
            price_points=[
                CreateComponentPricePoint(
                    name="Wholesale",
                    handle="wholesale",
                    pricing_scheme=PricingScheme.PER_UNIT,
                    prices=[Price(starting_quantity=1, unit_price=5)],
                ),
                CreateComponentPricePoint(
                    name="MSRP",
                    handle="msrp",
                    pricing_scheme=PricingScheme.PER_UNIT,
                    prices=[Price(starting_quantity=1, unit_price=4)],
                ),
                CreateComponentPricePoint(
                    name="Special Pricing",
                    handle="special",
                    pricing_scheme=PricingScheme.PER_UNIT,
                    prices=[Price(starting_quantity=1, unit_price=5)],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type ComponentPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkCreateComponentPricePointsErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.bulk_create_component_price_points(
        "some example string",
        body=CreateComponentPricePointsRequest(
            price_points=[
                CreateComponentPricePoint(
                    name="Wholesale",
                    handle="wholesale",
                    pricing_scheme=PricingScheme.PER_UNIT,
                    prices=[Price(starting_quantity=1, unit_price=5)],
                ),
                CreateComponentPricePoint(
                    name="MSRP",
                    handle="msrp",
                    pricing_scheme=PricingScheme.PER_UNIT,
                    prices=[Price(starting_quantity=1, unit_price=4)],
                ),
                CreateComponentPricePoint(
                    name="Special Pricing",
                    handle="special",
                    pricing_scheme=PricingScheme.PER_UNIT,
                    prices=[Price(starting_quantity=1, unit_price=5)],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type ComponentPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkCreateComponentPricePointsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | The Advanced Billing id of the component for which you want to fetch price points. |
| <code>body</code> | <code>[CreateComponentPricePointsRequest](maxio_advanced_billing/models/create_component_price_points_request.py) \| [CreateComponentPricePointsRequestDict](maxio_advanced_billing/models/create_component_price_points_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointsResponse](maxio_advanced_billing/models/component_price_points_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[BulkCreateComponentPricePointsErrorBody](maxio_advanced_billing/errors/bulk_create_component_price_points_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def clone_component_price_point(component_id: ComponentIdModel | ComponentIdModelDict, price_point_id: PricePointIdModel | PricePointIdModelDict, *, body: CloneComponentPricePointRequest | CloneComponentPricePointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointCurrencyOverageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Clones a component price point. Custom price points (tied to a specific subscription) cannot be cloned. The following attributes are copied from the source price point:
- Pricing scheme
- All price tiers (with starting/ending quantities and unit prices)
- Tax included setting
- Currency prices (if definitive pricing is set)
- Overage pricing (for prepaid usage components)
- Interval settings (if multi-frequency is enabled)
- Event-based billing segments (if applicable)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.clone_component_price_point(
        1, 1, body=CloneComponentPricePointRequest(price_point=CloneComponentPricePoint(name="Pro Usage Tiered Clone"))
    )
    # TODO: Handle 'response' of type ComponentPricePointCurrencyOverageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloneComponentPricePointErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.clone_component_price_point(
        1, 1, body=CloneComponentPricePointRequest(price_point=CloneComponentPricePoint(name="Pro Usage Tiered Clone"))
    )
    # TODO: Handle 'response' of type ComponentPricePointCurrencyOverageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CloneComponentPricePointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>[ComponentIdModel](maxio_advanced_billing/models/unions/component_id_model.py) \| [ComponentIdModelDict](maxio_advanced_billing/models/unions/component_id_model.py)</code> | The id or handle of the component. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle. |
| <code>price_point_id</code> | <code>[PricePointIdModel](maxio_advanced_billing/models/unions/price_point_id_model.py) \| [PricePointIdModelDict](maxio_advanced_billing/models/unions/price_point_id_model.py)</code> | The id or handle of the price point. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a string handle. |
| <code>body</code> | <code>[CloneComponentPricePointRequest](maxio_advanced_billing/models/clone_component_price_point_request.py) \| [CloneComponentPricePointRequestDict](maxio_advanced_billing/models/clone_component_price_point_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointCurrencyOverageResponse](maxio_advanced_billing/models/component_price_point_currency_overage_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CloneComponentPricePointErrorBody](maxio_advanced_billing/errors/clone_component_price_point_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_component_price_point(component_id: int, *, body: CreateComponentPricePointRequest | CreateComponentPricePointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a price point for an existing component.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.create_component_price_point(
        1,
        body=CreateComponentPricePointRequest(
            price_point=CreateComponentPricePoint(
                name="Wholesale",
                handle="wholesale-handle",
                pricing_scheme=PricingScheme.STAIRSTEP,
                prices=[
                    Price(starting_quantity="1", ending_quantity="100", unit_price="5.00"),
                    Price(starting_quantity="101", ending_quantity="200", unit_price="4.00"),
                ],
                use_site_exchange_rate=False,
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateComponentPricePointErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.create_component_price_point(
        1,
        body=CreateComponentPricePointRequest(
            price_point=CreateComponentPricePoint(
                name="Wholesale",
                handle="wholesale-handle",
                pricing_scheme=PricingScheme.STAIRSTEP,
                prices=[
                    Price(starting_quantity="1", ending_quantity="100", unit_price="5.00"),
                    Price(starting_quantity="101", ending_quantity="200", unit_price="4.00"),
                ],
                use_site_exchange_rate=False,
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateComponentPricePointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>body</code> | <code>[CreateComponentPricePointRequest](maxio_advanced_billing/models/create_component_price_point_request.py) \| [CreateComponentPricePointRequestDict](maxio_advanced_billing/models/create_component_price_point_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointResponse](maxio_advanced_billing/models/component_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateComponentPricePointErrorBody](maxio_advanced_billing/errors/create_component_price_point_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_currency_prices(price_point_id: int, *, body: CreateCurrencyPricesRequest | CreateCurrencyPricesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentCurrencyPricesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates currency prices for a given currency defined at the site level.

When creating currency prices, they need to mirror the structure of your primary pricing. For each price level defined on the component price point, there should be a matching price level created in the given currency.

Note: Currency Prices are not able to be created for custom price points.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.create_currency_prices(
        1,
        body=CreateCurrencyPricesRequest(
            currency_prices=[
                CreateCurrencyPrice(currency="EUR", price=50, price_id=20),
                CreateCurrencyPrice(currency="EUR", price=40, price_id=21),
            ],
        ),
    )
    # TODO: Handle 'response' of type ComponentCurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateCurrencyPricesErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.create_currency_prices(
        1,
        body=CreateCurrencyPricesRequest(
            currency_prices=[
                CreateCurrencyPrice(currency="EUR", price=50, price_id=20),
                CreateCurrencyPrice(currency="EUR", price=40, price_id=21),
            ],
        ),
    )
    # TODO: Handle 'response' of type ComponentCurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateCurrencyPricesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>price_point_id</code> | <code>int</code> | The Advanced Billing id of the price point |
| <code>body</code> | <code>[CreateCurrencyPricesRequest](maxio_advanced_billing/models/create_currency_prices_request.py) \| [CreateCurrencyPricesRequestDict](maxio_advanced_billing/models/create_currency_prices_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentCurrencyPricesResponse](maxio_advanced_billing/models/component_currency_prices_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateCurrencyPricesErrorBody](maxio_advanced_billing/errors/create_currency_prices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_all_component_price_points(*, include: ListComponentsPricePointsIncludeOrStr | None = None, page: int | None = 1, per_page: int | None = 20, direction: SortingDirectionOrStr | None = None, filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ListComponentsPricePointsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all component price points belonging to a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.list_all_component_price_points(
        include=ListComponentsPricePointsInclude.CURRENCY_PRICES, page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListComponentsPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllComponentPricePointsErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.list_all_component_price_points(
        include=ListComponentsPricePointsInclude.CURRENCY_PRICES, page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListComponentsPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllComponentPricePointsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include</code> | <code>[ListComponentsPricePointsIncludeOrStr](maxio_advanced_billing/models/enums/list_components_price_points_include.py) \| None</code> | Allows including additional data in the response. Use in query: `include=currency_prices`.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>filter_</code> | <code>[ListPricePointsFilter](maxio_advanced_billing/models/list_price_points_filter.py) \| [ListPricePointsFilterDict](maxio_advanced_billing/models/list_price_points_filter.py) \| None</code> | Filter to use for List PricePoints operations<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListComponentsPricePointsResponse](maxio_advanced_billing/models/list_components_price_points_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListAllComponentPricePointsErrorBody](maxio_advanced_billing/errors/list_all_component_price_points_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_component_price_points(component_id: int, *, currency_prices: bool | None = None, page: int | None = 1, per_page: int | None = 20, filter_type: list[PricePointTypeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the price points associated with a component.

You may specify the component by using either the numeric id or the `handle:gold` syntax.

If the price point is set to `use_site_exchange_rate: true`, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.list_component_price_points(
        1, page=1, per_page=50, filter_type=[PricePointType.CATALOG, PricePointType.DEFAULT]
    )
    # TODO: Handle 'response' of type ComponentPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.component_price_points.list_component_price_points(
        1, page=1, per_page=50, filter_type=[PricePointType.CATALOG, PricePointType.DEFAULT]
    )
    # TODO: Handle 'response' of type ComponentPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>currency_prices</code> | <code>bool \| None</code> | Include an array of currency price data.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>filter_type</code> | <code>list&#91;[PricePointTypeOrStr](maxio_advanced_billing/models/enums/price_point_type.py)&#93; \| None</code> | Use in query: `filter[type]=catalog,default`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointsResponse](maxio_advanced_billing/models/component_price_points_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def promote_component_price_point_to_default(component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets a new default price point for the component. This new default will apply to all new subscriptions going forward - existing subscriptions will remain on their current price point.

See [Price Points Documentation](https://maxio.zendesk.com/hc/en-us/articles/24261191737101-Price-Points-Components) for more information on price points and moving subscriptions between price points.

Note: Custom price points are not able to be set as the default for a component.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.promote_component_price_point_to_default(1, 1)
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.component_price_points.promote_component_price_point_to_default(1, 1)
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component to which the price point belongs |
| <code>price_point_id</code> | <code>int</code> | The Advanced Billing id of the price point |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_component_price_point(component_id: ComponentIdModel | ComponentIdModelDict, price_point_id: PricePointIdModel | PricePointIdModelDict, *, currency_prices: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointCurrencyOverageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details for a specific component price point. You can achieve this by using either the component price point ID or handle.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.read_component_price_point(1, 1)
    # TODO: Handle 'response' of type ComponentPricePointCurrencyOverageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.component_price_points.read_component_price_point(1, 1)
    # TODO: Handle 'response' of type ComponentPricePointCurrencyOverageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>[ComponentIdModel](maxio_advanced_billing/models/unions/component_id_model.py) \| [ComponentIdModelDict](maxio_advanced_billing/models/unions/component_id_model.py)</code> | The id or handle of the component. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle. |
| <code>price_point_id</code> | <code>[PricePointIdModel](maxio_advanced_billing/models/unions/price_point_id_model.py) \| [PricePointIdModelDict](maxio_advanced_billing/models/unions/price_point_id_model.py)</code> | The id or handle of the price point. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a string handle. |
| <code>currency_prices</code> | <code>bool \| None</code> | Include an array of currency price data.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointCurrencyOverageResponse](maxio_advanced_billing/models/component_price_point_currency_overage_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unarchive_component_price_point(component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unarchives a component price point.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.unarchive_component_price_point(1, 1)
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.component_price_points.unarchive_component_price_point(1, 1)
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component to which the price point belongs |
| <code>price_point_id</code> | <code>int</code> | The Advanced Billing id of the price point |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointResponse](maxio_advanced_billing/models/component_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_component_price_point(component_id: ComponentIdModel | ComponentIdModelDict, price_point_id: PricePointIdModel | PricePointIdModelDict, *, body: UpdateComponentPricePointRequest | UpdateComponentPricePointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a component price point and its associated prices.

Passing in a price bracket without an `id` will attempt to create a new price.

Including an `id` will update the corresponding price, and including the `_destroy` flag set to true along with the `id` will remove that price.

Note: Custom price points cannot be updated directly. They must be edited through the Subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.update_component_price_point(
        1,
        1,
        body=UpdateComponentPricePointRequest(
            price_point=UpdateComponentPricePoint(
                name="Default",
                prices=[
                    UpdatePrice(id=1, ending_quantity=100, unit_price=5),
                    UpdatePrice(id=2, destroy=True),
                    UpdatePrice(unit_price=4, starting_quantity=101),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateComponentPricePointErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.update_component_price_point(
        1,
        1,
        body=UpdateComponentPricePointRequest(
            price_point=UpdateComponentPricePoint(
                name="Default",
                prices=[
                    UpdatePrice(id=1, ending_quantity=100, unit_price=5),
                    UpdatePrice(id=2, destroy=True),
                    UpdatePrice(unit_price=4, starting_quantity=101),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateComponentPricePointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>[ComponentIdModel](maxio_advanced_billing/models/unions/component_id_model.py) \| [ComponentIdModelDict](maxio_advanced_billing/models/unions/component_id_model.py)</code> | The id or handle of the component. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle. |
| <code>price_point_id</code> | <code>[PricePointIdModel](maxio_advanced_billing/models/unions/price_point_id_model.py) \| [PricePointIdModelDict](maxio_advanced_billing/models/unions/price_point_id_model.py)</code> | The id or handle of the price point. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a string handle. |
| <code>body</code> | <code>[UpdateComponentPricePointRequest](maxio_advanced_billing/models/update_component_price_point_request.py) \| [UpdateComponentPricePointRequestDict](maxio_advanced_billing/models/update_component_price_point_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentPricePointResponse](maxio_advanced_billing/models/component_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateComponentPricePointErrorBody](maxio_advanced_billing/errors/update_component_price_point_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_currency_prices(price_point_id: int, *, body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentCurrencyPricesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates currency prices for a given currency defined at the site level.

Note: Currency Prices are not able to be updated for custom price points.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.component_price_points.update_currency_prices(
        1,
        body=UpdateCurrencyPricesRequest(
            currency_prices=[UpdateCurrencyPrice(id=100, price=51), UpdateCurrencyPrice(id=101, price=41)]
        ),
    )
    # TODO: Handle 'response' of type ComponentCurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCurrencyPricesErrorBody
```

**Async**

```python
try:
    response = await async_client.component_price_points.update_currency_prices(
        1,
        body=UpdateCurrencyPricesRequest(
            currency_prices=[UpdateCurrencyPrice(id=100, price=51), UpdateCurrencyPrice(id=101, price=41)]
        ),
    )
    # TODO: Handle 'response' of type ComponentCurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCurrencyPricesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>price_point_id</code> | <code>int</code> | The Advanced Billing id of the price point |
| <code>body</code> | <code>[UpdateCurrencyPricesRequest](maxio_advanced_billing/models/update_currency_prices_request.py) \| [UpdateCurrencyPricesRequestDict](maxio_advanced_billing/models/update_currency_prices_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentCurrencyPricesResponse](maxio_advanced_billing/models/component_currency_prices_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateCurrencyPricesErrorBody](maxio_advanced_billing/errors/update_currency_prices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Components

> Source: [Components](maxio_advanced_billing/apis/components.py)

<details>
<summary><code>def archive_component(product_family_id: int, component_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Component</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives the component; all current subscribers will continue to be charged as usual.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.archive_component(1, "some example string")
    # TODO: Handle 'response' of type Component
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.archive_component(1, "some example string")
    # TODO: Handle 'response' of type Component
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the component belongs |
| <code>component_id</code> | <code>str</code> | Either the Advanced Billing id of the component or the handle for the component prefixed with `handle:` |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Component](maxio_advanced_billing/models/component.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ArchiveComponentErrorBody](maxio_advanced_billing/errors/archive_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_event_based_component(product_family_id: str, *, body: CreateEbbComponent | CreateEbbComponentDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an event-based component definition under the specified product family. An event-based component can then be added and “allocated” for a subscription.

Event-based components are similar to other component types, in that you define the component parameters (such as name and taxability) and the pricing. A key difference for the event-based component is that it must be attached to a metric. This is because the metric provides the component with the actual quantity used in computing what and how much will be billed each period for each subscription.

So, instead of reporting usage directly for each component (as you would with metered components), the usage is derived from analysis of your events.

For more information, see [Components Overview](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, taxable components must include a non-blank `tax_code`; sending a blank value results in a validation error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.create_event_based_component(
        "some example string",
        body=CreateEbbComponent(
            event_based_component=EbbComponent(
                name="Component Name",
                unit_name="string",
                description="string",
                handle="some_handle",
                taxable=True,
                pricing_scheme=PricingScheme.PER_UNIT,
                prices=[Price(starting_quantity=1, unit_price="0.49")],
                event_based_billing_metric_id=123,
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateEventBasedComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.create_event_based_component(
        "some example string",
        body=CreateEbbComponent(
            event_based_component=EbbComponent(
                name="Component Name",
                unit_name="string",
                description="string",
                handle="some_handle",
                taxable=True,
                pricing_scheme=PricingScheme.PER_UNIT,
                prices=[Price(starting_quantity=1, unit_price="0.49")],
                event_based_billing_metric_id=123,
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateEventBasedComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>str</code> | Either the product family's id or its handle prefixed with `handle:` |
| <code>body</code> | <code>[CreateEbbComponent](maxio_advanced_billing/models/create_ebb_component.py) \| [CreateEbbComponentDict](maxio_advanced_billing/models/create_ebb_component.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateEventBasedComponentErrorBody](maxio_advanced_billing/errors/create_event_based_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_metered_component(product_family_id: str, *, body: CreateMeteredComponent | CreateMeteredComponentDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a metered component definition under the specified product family. A metered component can then be added and “allocated” for a subscription.

Metered components are used to bill for any type of unit that resets to 0 at the end of the billing period (think daily Google Ads clicks or monthly cell phone minutes). This is most commonly associated with usage-based billing and many other pricing schemes.

Note that this is different from recurring quantity-based components, which DO NOT reset to zero at the start of every billing period. If you want to bill for a quantity of something that does not change unless you change it, then you want quantity components, instead.

#### Hybrid Pricing
A `volume`, `tiered`, or `stairstep` metered component can combine its primary pricing with a secondary pricing model (the `overage_pricing` parameter) so both bill as a single invoice line item instead of two. This does not apply to metered components configured for event-based billing (metric, meter, or formula). See [Hybrid Pricing](page:introduction/basic-concepts/hybrid-pricing) for requirements and configuration details.

For more information on components, see our documentation [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""` returns `422`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.create_metered_component(
        "some example string",
        body=CreateMeteredComponent(
            metered_component=MeteredComponent(
                name="Text messages",
                unit_name="text message",
                taxable=False,
                pricing_scheme=PricingScheme.PER_UNIT,
                prices=[Price(starting_quantity=1, unit_price=1)],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMeteredComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.create_metered_component(
        "some example string",
        body=CreateMeteredComponent(
            metered_component=MeteredComponent(
                name="Text messages",
                unit_name="text message",
                taxable=False,
                pricing_scheme=PricingScheme.PER_UNIT,
                prices=[Price(starting_quantity=1, unit_price=1)],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMeteredComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>str</code> | Either the product family's id or its handle prefixed with `handle:` |
| <code>body</code> | <code>[CreateMeteredComponent](maxio_advanced_billing/models/create_metered_component.py) \| [CreateMeteredComponentDict](maxio_advanced_billing/models/create_metered_component.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateMeteredComponentErrorBody](maxio_advanced_billing/errors/create_metered_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_on_off_component(product_family_id: str, *, body: CreateOnOffComponent | CreateOnOffComponentDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an On/Off component definition under the specified product family. An On/Off component can then be added and “allocated” for a subscription.

On/off components are used for any flat fee, recurring add on (think $99/month for tech support or a flat add on shipping fee).

For more information on components, see our documentation [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""` returns `422`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.create_on_off_component(
        "some example string",
        body=CreateOnOffComponent(
            on_off_component=OnOffComponent(
                name="Annual Support Services",
                description="Prepay for support services",
                taxable=True,
                unit_price="100.00",
                display_on_hosted_page=True,
                public_signup_page_ids=[320495],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOnOffComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.create_on_off_component(
        "some example string",
        body=CreateOnOffComponent(
            on_off_component=OnOffComponent(
                name="Annual Support Services",
                description="Prepay for support services",
                taxable=True,
                unit_price="100.00",
                display_on_hosted_page=True,
                public_signup_page_ids=[320495],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOnOffComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>str</code> | Either the product family's id or its handle prefixed with `handle:` |
| <code>body</code> | <code>[CreateOnOffComponent](maxio_advanced_billing/models/create_on_off_component.py) \| [CreateOnOffComponentDict](maxio_advanced_billing/models/create_on_off_component.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateOnOffComponentErrorBody](maxio_advanced_billing/errors/create_on_off_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_prepaid_usage_component(product_family_id: str, *, body: CreatePrepaidComponent | CreatePrepaidComponentDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a prepaid usage component definition under the specified product family. A prepaid component can then be added and “allocated” for a subscription.

Prepaid components allow customers to pre-purchase units that can be used up over time on their subscription. In a sense, they are the mirror image of metered components; while metered components charge at the end of the period for the amount of units used, prepaid components are charged for at the time of purchase, and usage is subsequently tracked against the amount purchased.

For more information, see [Components Overview](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, taxable components must include a non-blank `tax_code`; sending a blank value results in a validation error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.create_prepaid_usage_component(
        "some example string",
        body=CreatePrepaidComponent(
            prepaid_usage_component=PrepaidUsageComponent(
                name="Minutes",
                unit_name="minutes",
                pricing_scheme=PricingScheme.PER_UNIT,
                unit_price=2,
                overage_pricing=OveragePricing(pricing_scheme=PricingScheme.STAIRSTEP, prices=[Price(), Price()]),
                rollover_prepaid_remainder=True,
                renew_prepaid_allocation=True,
                expiration_interval=15,
                expiration_interval_unit=ExpirationIntervalUnit.DAY,
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePrepaidUsageComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.create_prepaid_usage_component(
        "some example string",
        body=CreatePrepaidComponent(
            prepaid_usage_component=PrepaidUsageComponent(
                name="Minutes",
                unit_name="minutes",
                pricing_scheme=PricingScheme.PER_UNIT,
                unit_price=2,
                overage_pricing=OveragePricing(pricing_scheme=PricingScheme.STAIRSTEP, prices=[Price(), Price()]),
                rollover_prepaid_remainder=True,
                renew_prepaid_allocation=True,
                expiration_interval=15,
                expiration_interval_unit=ExpirationIntervalUnit.DAY,
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePrepaidUsageComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>str</code> | Either the product family's id or its handle prefixed with `handle:` |
| <code>body</code> | <code>[CreatePrepaidComponent](maxio_advanced_billing/models/create_prepaid_component.py) \| [CreatePrepaidComponentDict](maxio_advanced_billing/models/create_prepaid_component.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreatePrepaidUsageComponentErrorBody](maxio_advanced_billing/errors/create_prepaid_usage_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_quantity_based_component(product_family_id: str, *, body: CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Quantity Based component definition under the specified product family. A Quantity Based component can then be added and “allocated” for a subscription.

When defining a Quantity Based component, you can choose one of two types:
#### Recurring
Recurring quantity-based components are used to bill for the number of some unit (think monthly software user licenses or the number of pairs of socks in a box-a-month club). This is most commonly associated with billing for user licenses, number of users, number of employees, etc.

#### One-time
One-time quantity-based components are used to create ad hoc usage charges that do not recur. For example, at the time of signup, you might want to charge your customer a one-time fee for onboarding or other services.

The allocated quantity for one-time quantity-based components immediately gets reset back to zero after the allocation is made.

For more information, see [Components Overview](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).
#### Hybrid Pricing
A `volume`, `tiered`, or `stairstep` component can combine its primary pricing with a secondary pricing model (the `overage_pricing` parameter) so both bill as a single invoice line item instead of two. See [Hybrid Pricing](page:introduction/basic-concepts/hybrid-pricing) for requirements and configuration details.

For more information on components, see our documentation [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""` returns `422`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.create_quantity_based_component(
        "some example string",
        body=CreateQuantityBasedComponent(
            quantity_based_component=QuantityBasedComponent(
                name="Quantity Based Component",
                unit_name="Component",
                description="Example of JSON per-unit component example",
                taxable=True,
                pricing_scheme=PricingScheme.PER_UNIT,
                unit_price="10",
                display_on_hosted_page=True,
                allow_fractional_quantities=True,
                public_signup_page_ids=[323397],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateQuantityBasedComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.create_quantity_based_component(
        "some example string",
        body=CreateQuantityBasedComponent(
            quantity_based_component=QuantityBasedComponent(
                name="Quantity Based Component",
                unit_name="Component",
                description="Example of JSON per-unit component example",
                taxable=True,
                pricing_scheme=PricingScheme.PER_UNIT,
                unit_price="10",
                display_on_hosted_page=True,
                allow_fractional_quantities=True,
                public_signup_page_ids=[323397],
            ),
        ),
    )
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateQuantityBasedComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>str</code> | Either the product family's id or its handle prefixed with `handle:` |
| <code>body</code> | <code>[CreateQuantityBasedComponent](maxio_advanced_billing/models/create_quantity_based_component.py) \| [CreateQuantityBasedComponentDict](maxio_advanced_billing/models/create_quantity_based_component.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateQuantityBasedComponentErrorBody](maxio_advanced_billing/errors/create_quantity_based_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_component(handle: str, *, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information for a component matching the provided handle. You can identify your components with a handle so you don't have to save or reference the IDs we generate.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.find_component("some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.components.find_component("some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>handle</code> | <code>str</code> | The handle of the component to find |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_components(*, date_field: BasicDateFieldOrStr | None = None, start_date: str | None = None, end_date: str | None = None, start_datetime: str | None = None, end_datetime: str | None = None, include_archived: bool | None = None, page: int | None = 1, per_page: int | None = 20, filter_: ListComponentsFilter | ListComponentsFilterDict | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ComponentResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists components for a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.list_components(date_field=BasicDateField.UPDATED_AT, page=1, per_page=50)
    # TODO: Handle 'response' of type list[ComponentResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.components.list_components(date_field=BasicDateField.UPDATED_AT, page=1, per_page=50)
    # TODO: Handle 'response' of type list[ComponentResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>date_field</code> | <code>[BasicDateFieldOrStr](maxio_advanced_billing/models/enums/basic_date_field.py) \| None</code> | The type of filter you would like to apply to your search.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>include_archived</code> | <code>bool \| None</code> | Include archived items.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>filter_</code> | <code>[ListComponentsFilter](maxio_advanced_billing/models/list_components_filter.py) \| [ListComponentsFilterDict](maxio_advanced_billing/models/list_components_filter.py) \| None</code> | Filter to use for List Components operations<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ComponentResponse](maxio_advanced_billing/models/component_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_components_for_product_family(product_family_id: int, *, include_archived: bool | None = None, page: int | None = 1, per_page: int | None = 20, filter_: ListComponentsFilter | ListComponentsFilterDict | None = None, date_field: BasicDateFieldOrStr | None = None, end_date: str | None = None, end_datetime: str | None = None, start_date: str | None = None, start_datetime: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ComponentResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists components for a particular product family.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.list_components_for_product_family(
        1, page=1, per_page=50, date_field=BasicDateField.UPDATED_AT
    )
    # TODO: Handle 'response' of type list[ComponentResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.components.list_components_for_product_family(
        1, page=1, per_page=50, date_field=BasicDateField.UPDATED_AT
    )
    # TODO: Handle 'response' of type list[ComponentResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family |
| <code>include_archived</code> | <code>bool \| None</code> | Include archived items.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>filter_</code> | <code>[ListComponentsFilter](maxio_advanced_billing/models/list_components_filter.py) \| [ListComponentsFilterDict](maxio_advanced_billing/models/list_components_filter.py) \| None</code> | Filter to use for List Components operations<br>**Default**: <code>None</code> |
| <code>date_field</code> | <code>[BasicDateFieldOrStr](maxio_advanced_billing/models/enums/basic_date_field.py) \| None</code> | The type of filter you would like to apply to your search. Use in query `date_field=created_at`.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ComponentResponse](maxio_advanced_billing/models/component_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_component(product_family_id: int, component_id: str, *, include_features: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information regarding a component from a specific product family.

You can read the component by either the component's id or handle. When using the handle, it must be prefixed with `handle:`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.read_component(1, "some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.components.read_component(1, "some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the component belongs |
| <code>component_id</code> | <code>str</code> | Either the Advanced Billing id of the component or the handle for the component prefixed with `handle:` |
| <code>include_features</code> | <code>bool \| None</code> | When `true`, embeds the active feature catalog items for each result in a `features` array. Default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_component(component_id: str, *, body: UpdateComponentRequest | UpdateComponentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a component.

You may read the component by either the component's id or handle. When using the handle, it must be prefixed with `handle:`.

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""` returns `422`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.update_component("some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.update_component("some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | The id or handle of the component |
| <code>body</code> | <code>[UpdateComponentRequest](maxio_advanced_billing/models/update_component_request.py) \| [UpdateComponentRequestDict](maxio_advanced_billing/models/update_component_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateComponentErrorBody](maxio_advanced_billing/errors/update_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_product_family_component(product_family_id: int, component_id: str, *, body: UpdateComponentRequest | UpdateComponentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a component from a specific product family.

You may read the component by either the component's id or handle. When using the handle, it must be prefixed with `handle:`.

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""` returns `422`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.components.update_product_family_component(1, "some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductFamilyComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.components.update_product_family_component(1, "some example string")
    # TODO: Handle 'response' of type ComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductFamilyComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the component belongs |
| <code>component_id</code> | <code>str</code> | Either the Advanced Billing id of the component or the handle for the component prefixed with `handle:` |
| <code>body</code> | <code>[UpdateComponentRequest](maxio_advanced_billing/models/update_component_request.py) \| [UpdateComponentRequestDict](maxio_advanced_billing/models/update_component_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ComponentResponse](maxio_advanced_billing/models/component_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateProductFamilyComponentErrorBody](maxio_advanced_billing/errors/update_product_family_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Coupons

> Source: [Coupons](maxio_advanced_billing/apis/coupons.py)

<details>
<summary><code>def archive_coupon(product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None) -> CouponResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives a coupon, making it unavailable for future use while remaining active on existing subscriptions.
Archiving makes that Coupon unavailable for future use, but allows it to remain attached and functional on existing Subscriptions that are using it.
The `archived_at` date and time will be assigned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.archive_coupon(1, 1)
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.archive_coupon(1, 1)
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the coupon belongs |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponResponse](maxio_advanced_billing/models/coupon_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_coupon(product_family_id: int, *, body: CouponRequest | CouponRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a coupon under the specified product family.

You can create either a flat amount coupon, by specifying `amount_in_cents`, or percentage coupon by specifying `percentage`.

See [Apply Coupons to Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions) for information on applying a coupon to a subscription in the Advanced Billing UI.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.create_coupon(
        1,
        body=CouponRequest(
            coupon=CouponPayload(
                name="15% off",
                code="15OFF",
                description="15% off for life",
                percentage=15,
                allow_negative_balance=False,
                recurring=False,
                end_date=date(2012, 8, 29),
                product_family_id="2",
                stackable=True,
                compounding_strategy=CompoundingStrategy.COMPOUND,
                exclude_mid_period_allocations=True,
                apply_on_cancel_at_end_of_period=True,
            ),
            restricted_products={"1": True},
            restricted_components={"1": True, "2": False},
        ),
    )
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateCouponErrorBody
```

**Async**

```python
try:
    response = await async_client.coupons.create_coupon(
        1,
        body=CouponRequest(
            coupon=CouponPayload(
                name="15% off",
                code="15OFF",
                description="15% off for life",
                percentage=15,
                allow_negative_balance=False,
                recurring=False,
                end_date=date(2012, 8, 29),
                product_family_id="2",
                stackable=True,
                compounding_strategy=CompoundingStrategy.COMPOUND,
                exclude_mid_period_allocations=True,
                apply_on_cancel_at_end_of_period=True,
            ),
            restricted_products={"1": True},
            restricted_components={"1": True, "2": False},
        ),
    )
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateCouponErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the coupon belongs |
| <code>body</code> | <code>[CouponRequest](maxio_advanced_billing/models/coupon_request.py) \| [CouponRequestDict](maxio_advanced_billing/models/coupon_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponResponse](maxio_advanced_billing/models/coupon_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateCouponErrorBody](maxio_advanced_billing/errors/create_coupon_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_coupon_subcodes(coupon_id: int, *, body: CouponSubcodes | CouponSubcodesDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponSubcodesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates subcodes for an existing coupon.

Coupon Subcodes allow you to create a set of unique codes that allow you to expand the use of one coupon.

For example:

Master Coupon Code:

+ SPRING2020

Coupon Subcodes:

+ SPRING90210
+ DP80302
+ SPRINGBALTIMORE

When creating a coupon subcode, you must specify a coupon to attach it to using the coupon_id. Valid coupon subcodes are all capital letters, contain only letters and numbers, and do not have any spaces. Lowercase letters are capitalized before the subcode is created.

Note: If you are using any of the allowed special characters ("%", "@", "+", "-", "_", and "."), you must encode them for use in the URL.

    % to %25
    @ to %40
    + to %2B
    - to %2D
    _ to %5F
    . to %2E

So, if the coupon subcode is `20%OFF`, the URL to delete this coupon subcode would be: `https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>`.

For more information on coupon codes and applying coupons to subscriptions, see [Coupon Codes](https://maxio.zendesk.com/hc/en-us/articles/24261208729229-Coupon-Codes) and [Coupons and Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.create_coupon_subcodes(
        1, body=CouponSubcodes(codes=["BALTIMOREFALL", "ORLANDOFALL", "DETROITFALL"])
    )
    # TODO: Handle 'response' of type CouponSubcodesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.create_coupon_subcodes(
        1, body=CouponSubcodes(codes=["BALTIMOREFALL", "ORLANDOFALL", "DETROITFALL"])
    )
    # TODO: Handle 'response' of type CouponSubcodesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon |
| <code>body</code> | <code>[CouponSubcodes](maxio_advanced_billing/models/coupon_subcodes.py) \| [CouponSubcodesDict](maxio_advanced_billing/models/coupon_subcodes.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponSubcodesResponse](maxio_advanced_billing/models/coupon_subcodes_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_or_update_coupon_currency_prices(coupon_id: int, *, body: CouponCurrencyRequest | CouponCurrencyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponCurrencyResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates and/or updates currency prices for an existing coupon. Multiple prices can be created or updated in a single request but each of the currencies must be defined on the site level already and the coupon must be an amount-based coupon, not percentage.

Currency pricing for coupons must mirror the setup of the primary coupon pricing - if the primary coupon is percentage based, you will not be able to define pricing in non-primary currencies.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.create_or_update_coupon_currency_prices(
        1,
        body=CouponCurrencyRequest(
            currency_prices=[
                UpdateCouponCurrency(currency="EUR", price=10), UpdateCouponCurrency(currency="GBP", price=9)
            ],
        ),
    )
    # TODO: Handle 'response' of type CouponCurrencyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOrUpdateCouponCurrencyPricesErrorBody
```

**Async**

```python
try:
    response = await async_client.coupons.create_or_update_coupon_currency_prices(
        1,
        body=CouponCurrencyRequest(
            currency_prices=[
                UpdateCouponCurrency(currency="EUR", price=10), UpdateCouponCurrency(currency="GBP", price=9)
            ],
        ),
    )
    # TODO: Handle 'response' of type CouponCurrencyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOrUpdateCouponCurrencyPricesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon |
| <code>body</code> | <code>[CouponCurrencyRequest](maxio_advanced_billing/models/coupon_currency_request.py) \| [CouponCurrencyRequestDict](maxio_advanced_billing/models/coupon_currency_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponCurrencyResponse](maxio_advanced_billing/models/coupon_currency_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateOrUpdateCouponCurrencyPricesErrorBody](maxio_advanced_billing/errors/create_or_update_coupon_currency_prices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorStringMapResponse1](maxio_advanced_billing/models/error_string_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_coupon_subcode(coupon_id: int, subcode: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a specific subcode from a coupon.

## Example

Given a coupon with an ID of 567, and a coupon subcode of 20OFF, the URL to `DELETE` this coupon subcode would be:

``
http://subdomain.chargify.com/coupons/567/codes/20OFF.<format>
``

Note: If you are using any of the allowed special characters (“%”, “@”, “+”, “-”, “_”, and “.”), you must encode them for use in the URL.

| Special character | Encoding |
|-------------------|----------|
| %                 | %25      |
| @                 | %40      |
| +                 | %2B      |
| –                 | %2D      |
| _                 | %5F      |
| .                 | %2E      |

## Percent Encoding Example

Or if the coupon subcode is 20%OFF, the URL to delete this coupon subcode would be: @https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.coupons.delete_coupon_subcode(1, "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteCouponSubcodeErrorBody
```

**Async**

```python
try:
    await async_client.coupons.delete_coupon_subcode(1, "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteCouponSubcodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon to which the subcode belongs |
| <code>subcode</code> | <code>str</code> | The subcode of the coupon |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteCouponSubcodeErrorBody](maxio_advanced_billing/errors/delete_coupon_subcode_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_coupon(*, product_family_id: int | None = None, code: str | None = None, currency_prices: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for a coupon by code.

If you have more than one product family and if the coupon you are trying to find does not belong to the default product family in your site, you need to specify (either in the URL or as a query string param) the `product_family_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.find_coupon(currency_prices=True)
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.find_coupon(currency_prices=True)
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int \| None</code> | The Advanced Billing id of the product family to which the coupon belongs<br>**Default**: <code>None</code> |
| <code>code</code> | <code>str \| None</code> | The code of the coupon<br>**Default**: <code>None</code> |
| <code>currency_prices</code> | <code>bool \| None</code> | (Optional) If you have defined multiple currencies at the site level, you can pass `?currency_prices=true` to include an array of currency price data in the response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponResponse](maxio_advanced_billing/models/coupon_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_coupon_subcodes(coupon_id: int, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> CouponSubcodes</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the subcodes attached to a coupon.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.list_coupon_subcodes(1, page=1, per_page=50)
    # TODO: Handle 'response' of type CouponSubcodes
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.list_coupon_subcodes(1, page=1, per_page=50)
    # TODO: Handle 'response' of type CouponSubcodes
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponSubcodes](maxio_advanced_billing/models/coupon_subcodes.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_coupons(*, page: int | None = 1, per_page: int | None = 30, filter_: ListCouponsFilter | ListCouponsFilterDict | None = None, currency_prices: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> list[CouponResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists coupons for a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.list_coupons(page=1, per_page=50, currency_prices=True)
    # TODO: Handle 'response' of type list[CouponResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.list_coupons(page=1, per_page=50, currency_prices=True)
    # TODO: Handle 'response' of type list[CouponResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 30. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>30</code> |
| <code>filter_</code> | <code>[ListCouponsFilter](maxio_advanced_billing/models/list_coupons_filter.py) \| [ListCouponsFilterDict](maxio_advanced_billing/models/list_coupons_filter.py) \| None</code> | Filter to use for List Coupons operations<br>**Default**: <code>None</code> |
| <code>currency_prices</code> | <code>bool \| None</code> | (Optional) If you have defined multiple currencies at the site level, you can pass `?currency_prices=true` to include an array of currency price data in the response. Use in query `currency_prices=true`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[CouponResponse](maxio_advanced_billing/models/coupon_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_coupons_for_product_family(product_family_id: int, *, page: int | None = 1, per_page: int | None = 30, filter_: ListCouponsFilter | ListCouponsFilterDict | None = None, currency_prices: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> list[CouponResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists coupons for a specific product family in a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.list_coupons_for_product_family(1, page=1, per_page=50, currency_prices=True)
    # TODO: Handle 'response' of type list[CouponResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.list_coupons_for_product_family(1, page=1, per_page=50, currency_prices=True)
    # TODO: Handle 'response' of type list[CouponResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the coupon belongs |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 30. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>30</code> |
| <code>filter_</code> | <code>[ListCouponsFilter](maxio_advanced_billing/models/list_coupons_filter.py) \| [ListCouponsFilterDict](maxio_advanced_billing/models/list_coupons_filter.py) \| None</code> | Filter to use for List Coupons operations<br>**Default**: <code>None</code> |
| <code>currency_prices</code> | <code>bool \| None</code> | (Optional) If you have defined multiple currencies at the site level, you can pass `?currency_prices=true` to include an array of currency price data in the response. Use in query `currency_prices=true`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[CouponResponse](maxio_advanced_billing/models/coupon_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_coupon(product_family_id: int, coupon_id: int, *, currency_prices: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a coupon by its system-assigned ID. You must identify the Coupon in this call by the ID parameter assigned to it.

If instead you would like to find a Coupon using a Coupon code, use the [Find Coupon]($e/Coupons/findCoupon) endpoint.

If the coupon is set to `use_site_exchange_rate: true`, it returns pricing based on the current exchange rate. If the flag is set to false, it returns all of the defined prices for each currency.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.read_coupon(1, 1, currency_prices=True)
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.read_coupon(1, 1, currency_prices=True)
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the coupon belongs |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon |
| <code>currency_prices</code> | <code>bool \| None</code> | (Optional) If you have defined multiple currencies at the site level, you can pass `?currency_prices=true` to include an array of currency price data in the response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponResponse](maxio_advanced_billing/models/coupon_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_coupon_usage(product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None) -> list[CouponUsage]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists coupon usage details, one entry per product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.read_coupon_usage(1, 1)
    # TODO: Handle 'response' of type list[CouponUsage]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.read_coupon_usage(1, 1)
    # TODO: Handle 'response' of type list[CouponUsage]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the coupon belongs. |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[CouponUsage](maxio_advanced_billing/models/coupon_usage.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_coupon(product_family_id: int, coupon_id: int, *, body: CouponRequest | CouponRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a coupon. 

You can restrict a coupon to only apply to specific products / components by optionally passing in hashes of `restricted_products` and/or `restricted_components` in the format:
`{ "<product/component_id>": boolean_value }`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.update_coupon(
        1,
        1,
        body=CouponRequest(
            coupon=CouponPayload(
                name="15% off",
                code="15OFF",
                description="15% off for life",
                percentage=15,
                allow_negative_balance=False,
                recurring=False,
                end_date=date(2012, 8, 29),
                product_family_id="2",
                stackable=True,
                compounding_strategy=CompoundingStrategy.COMPOUND,
            ),
            restricted_products={"1": True},
            restricted_components={"1": True, "2": False},
        ),
    )
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCouponErrorBody
```

**Async**

```python
try:
    response = await async_client.coupons.update_coupon(
        1,
        1,
        body=CouponRequest(
            coupon=CouponPayload(
                name="15% off",
                code="15OFF",
                description="15% off for life",
                percentage=15,
                allow_negative_balance=False,
                recurring=False,
                end_date=date(2012, 8, 29),
                product_family_id="2",
                stackable=True,
                compounding_strategy=CompoundingStrategy.COMPOUND,
            ),
            restricted_products={"1": True},
            restricted_components={"1": True, "2": False},
        ),
    )
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCouponErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>int</code> | The Advanced Billing id of the product family to which the coupon belongs |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon |
| <code>body</code> | <code>[CouponRequest](maxio_advanced_billing/models/coupon_request.py) \| [CouponRequestDict](maxio_advanced_billing/models/coupon_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponResponse](maxio_advanced_billing/models/coupon_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateCouponErrorBody](maxio_advanced_billing/errors/update_coupon_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_coupon_subcodes(coupon_id: int, *, body: CouponSubcodes | CouponSubcodesDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponSubcodesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the subcodes for a coupon, replacing all existing subcodes with the new list.
Send an array of new coupon subcodes.

**Note**: All current subcodes for that Coupon will be deleted first, and replaced with the list of subcodes sent to this endpoint.
The response will contain:

+ The created subcodes,

+ Subcodes that were not created because they already exist,

+ Any subcodes not created because they are invalid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.update_coupon_subcodes(1, body=CouponSubcodes(codes=["AAAA", "BBBB", "CCCC"]))
    # TODO: Handle 'response' of type CouponSubcodesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.coupons.update_coupon_subcodes(1, body=CouponSubcodes(codes=["AAAA", "BBBB", "CCCC"]))
    # TODO: Handle 'response' of type CouponSubcodesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>coupon_id</code> | <code>int</code> | The Advanced Billing id of the coupon |
| <code>body</code> | <code>[CouponSubcodes](maxio_advanced_billing/models/coupon_subcodes.py) \| [CouponSubcodesDict](maxio_advanced_billing/models/coupon_subcodes.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponSubcodesResponse](maxio_advanced_billing/models/coupon_subcodes_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def validate_coupon(code: str, *, product_family_id: int | None = None, request_options: RequestOptionsOrDict | None = None) -> CouponResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Verifies whether a specific coupon code is valid. This method is useful for validating coupon codes that are entered by a customer.

If you have more than one product family and if the coupon you are validating does not belong to the first product family in your site, you need to specify the product family, either in the URL or as a query string param. This can be done by supplying the id or the handle in the `handle:my-family` format.

Supplying the `product_family_handle` in the URL:

``
https://<subdomain>.chargify.com/product_families/handle:<product_family_handle>/coupons/validate.<format>?code=<coupon_code>
``

Supplying the `product_family_id` as a query parameter:

``
https://<subdomain>.chargify.com/coupons/validate.<format>?code=<coupon_code>&product_family_id=<id>
``

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.coupons.validate_coupon("some example string")
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ValidateCouponErrorBody
```

**Async**

```python
try:
    response = await async_client.coupons.validate_coupon("some example string")
    # TODO: Handle 'response' of type CouponResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ValidateCouponErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | The code of the coupon |
| <code>product_family_id</code> | <code>int \| None</code> | The Advanced Billing id of the product family to which the coupon belongs<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CouponResponse](maxio_advanced_billing/models/coupon_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ValidateCouponErrorBody](maxio_advanced_billing/errors/validate_coupon_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[SingleStringErrorResponse1](maxio_advanced_billing/models/single_string_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CustomFields

> Source: [CustomFields](maxio_advanced_billing/apis/custom_fields.py)

<details>
<summary><code>def create_metadata(resource_type: ResourceTypeOrStr, resource_id: int, *, body: CreateMetadataRequest | CreateMetadataRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Metadata]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates metadata and metafields for a specific subscription or customer, or updates metadata values of existing metafields for a subscription or customer. Metadata values are limited to 2 KB in size.

If you create metadata on a subscription or customer with a metafield that does not already exist, the metafield is created with the metadata you specify and it is always added as a text field. You can update the input_type for the metafield with the [Update Metafield]($e/Custom%20Fields/updateMetafield) endpoint. 

>Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for Subscriptions and another 100 for Customers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.custom_fields.create_metadata(
        ResourceType.SUBSCRIPTIONS,
        1,
        body=CreateMetadataRequest(
            metadata=[CreateMetadata(name="Color", value="Blue"), CreateMetadata(name="Something", value="Useful")]
        ),
    )
    # TODO: Handle 'response' of type list[Metadata]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMetadataErrorBody
```

**Async**

```python
try:
    response = await async_client.custom_fields.create_metadata(
        ResourceType.SUBSCRIPTIONS,
        1,
        body=CreateMetadataRequest(
            metadata=[CreateMetadata(name="Color", value="Blue"), CreateMetadata(name="Something", value="Useful")]
        ),
    )
    # TODO: Handle 'response' of type list[Metadata]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMetadataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>resource_id</code> | <code>int</code> | The Advanced Billing id of the customer or the subscription for which the metadata applies |
| <code>body</code> | <code>[CreateMetadataRequest](maxio_advanced_billing/models/create_metadata_request.py) \| [CreateMetadataRequestDict](maxio_advanced_billing/models/create_metadata_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Metadata](maxio_advanced_billing/models/metadata.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateMetadataErrorBody](maxio_advanced_billing/errors/create_metadata_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_metafields(resource_type: ResourceTypeOrStr, *, body: CreateMetafieldsRequest | CreateMetafieldsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Metafield]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates metafields on a Site for either the Subscriptions or Customers resource. 

Metafields and their metadata are created in the Custom Fields configuration page on your Site. Metafields can be populated with metadata when you create them or later with the [Update Metafield]($e/Custom%20Fields/updateMetafield), [Create Metadata]($e/Custom%20Fields/createMetadata), or [Update Metadata]($e/Custom%20Fields/updateMetadata) endpoints. The Create Metadata and Update Metadata endpoints allow you to add metafields and metadata values to a specific subscription or customer.

Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for Subscriptions and another 100 for Customers.

> Note: After creating a metafield, the resource type cannot be modified.

In the UI and product documentation, metafields and metadata are called Custom Fields. 

- Metafield is the custom field
- Metadata is the data populating the custom field.

See [Custom Fields Reference](https://docs.maxio.com/hc/en-us/articles/24266140850573-Custom-Fields-Reference) and [Custom Fields Tab](https://maxio.zendesk.com/hc/en-us/articles/24251701302925-Subscription-Summary-Custom-Fields-Tab) for information on using Custom Fields in the Advanced Billing UI.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.custom_fields.create_metafields(
        ResourceType.SUBSCRIPTIONS,
        body=CreateMetafieldsRequest(
            metafields=CreateMetafield(
                name="Dropdown field",
                scope=MetafieldScope(
                    csv=IncludeOption._0,
                    invoices=IncludeOption._0,
                    statements=IncludeOption._0,
                    portal=IncludeOption._1,
                ),
                input_type=MetafieldInput.DROPDOWN,
                enum=["option 1", "option 2"],
            ),
        ),
    )
    # TODO: Handle 'response' of type list[Metafield]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMetafieldsErrorBody
```

**Async**

```python
try:
    response = await async_client.custom_fields.create_metafields(
        ResourceType.SUBSCRIPTIONS,
        body=CreateMetafieldsRequest(
            metafields=CreateMetafield(
                name="Dropdown field",
                scope=MetafieldScope(
                    csv=IncludeOption._0,
                    invoices=IncludeOption._0,
                    statements=IncludeOption._0,
                    portal=IncludeOption._1,
                ),
                input_type=MetafieldInput.DROPDOWN,
                enum=["option 1", "option 2"],
            ),
        ),
    )
    # TODO: Handle 'response' of type list[Metafield]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMetafieldsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>body</code> | <code>[CreateMetafieldsRequest](maxio_advanced_billing/models/create_metafields_request.py) \| [CreateMetafieldsRequestDict](maxio_advanced_billing/models/create_metafields_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Metafield](maxio_advanced_billing/models/metafield.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateMetafieldsErrorBody](maxio_advanced_billing/errors/create_metafields_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_metadata(resource_type: ResourceTypeOrStr, resource_id: int, *, name: str | None = None, names: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes one or more metafields (and associated metadata) from the specified subscription or customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.custom_fields.delete_metadata(ResourceType.SUBSCRIPTIONS, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMetadataErrorBody
```

**Async**

```python
try:
    await async_client.custom_fields.delete_metadata(ResourceType.SUBSCRIPTIONS, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMetadataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>resource_id</code> | <code>int</code> | The Advanced Billing id of the customer or the subscription for which the metadata applies |
| <code>name</code> | <code>str \| None</code> | Name of field to be removed.<br>**Default**: <code>None</code> |
| <code>names</code> | <code>list&#91;str&#93; \| None</code> | Names of fields to be removed. Use in query: `names[]=field1&names[]=my-field&names[]=another-field`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteMetadataErrorBody](maxio_advanced_billing/errors/delete_metadata_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_metafield(resource_type: ResourceTypeOrStr, *, name: str | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a metafield from your Site. Removes the metafield and associated metadata from all Subscriptions or Customers resources on the Site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.custom_fields.delete_metafield(ResourceType.SUBSCRIPTIONS)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMetafieldErrorBody
```

**Async**

```python
try:
    await async_client.custom_fields.delete_metafield(ResourceType.SUBSCRIPTIONS)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMetafieldErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>name</code> | <code>str \| None</code> | The name of the metafield to be deleted<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteMetafieldErrorBody](maxio_advanced_billing/errors/delete_metafield_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_metadata(resource_type: ResourceTypeOrStr, resource_id: int, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> PaginatedMetadata</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists metadata and metafields for a specific customer or subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.custom_fields.list_metadata(ResourceType.SUBSCRIPTIONS, 1, page=1, per_page=50)
    # TODO: Handle 'response' of type PaginatedMetadata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.custom_fields.list_metadata(ResourceType.SUBSCRIPTIONS, 1, page=1, per_page=50)
    # TODO: Handle 'response' of type PaginatedMetadata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>resource_id</code> | <code>int</code> | The Advanced Billing id of the customer or the subscription for which the metadata applies |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaginatedMetadata](maxio_advanced_billing/models/paginated_metadata.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_metadata_for_resource_type(resource_type: ResourceTypeOrStr, *, page: int | None = 1, per_page: int | None = 20, date_field: BasicDateFieldOrStr | None = None, start_date: Date | None = None, end_date: Date | None = None, start_datetime: RFC3339DateTime | None = None, end_datetime: RFC3339DateTime | None = None, with_deleted: bool | None = None, resource_ids: list[int] | None = None, direction: SortingDirectionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> PaginatedMetadata</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists metadata for a specified array of subscriptions or customers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.custom_fields.list_metadata_for_resource_type(
        ResourceType.SUBSCRIPTIONS, page=1, per_page=50, date_field=BasicDateField.UPDATED_AT
    )
    # TODO: Handle 'response' of type PaginatedMetadata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.custom_fields.list_metadata_for_resource_type(
        ResourceType.SUBSCRIPTIONS, page=1, per_page=50, date_field=BasicDateField.UPDATED_AT
    )
    # TODO: Handle 'response' of type PaginatedMetadata
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>date_field</code> | <code>[BasicDateFieldOrStr](maxio_advanced_billing/models/enums/basic_date_field.py) \| None</code> | The type of filter you would like to apply to your search.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>Date \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>Date \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>RFC3339DateTime \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns metadata with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>RFC3339DateTime \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns metadata with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>with_deleted</code> | <code>bool \| None</code> | Allow to fetch deleted metadata.<br>**Default**: <code>None</code> |
| <code>resource_ids</code> | <code>list&#91;int&#93; \| None</code> | Allow to fetch metadata for multiple records based on provided ids. Use in query: `resource_ids[]=122&resource_ids[]=123&resource_ids[]=124`.<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaginatedMetadata](maxio_advanced_billing/models/paginated_metadata.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_metafields(resource_type: ResourceTypeOrStr, *, name: str | None = None, page: int | None = 1, per_page: int | None = 20, direction: SortingDirectionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ListMetafieldsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the metafields and their associated details for a Site and resource type. You can filter the request to a specific metafield.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.custom_fields.list_metafields(ResourceType.SUBSCRIPTIONS, page=1, per_page=50)
    # TODO: Handle 'response' of type ListMetafieldsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.custom_fields.list_metafields(ResourceType.SUBSCRIPTIONS, page=1, per_page=50)
    # TODO: Handle 'response' of type ListMetafieldsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>name</code> | <code>str \| None</code> | Filter by the name of the metafield.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListMetafieldsResponse](maxio_advanced_billing/models/list_metafields_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_metadata(resource_type: ResourceTypeOrStr, resource_id: int, *, body: UpdateMetadataRequest | UpdateMetadataRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Metadata]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates metadata and metafields on the Site and the customer or subscription specified, and updates the metadata value on a subscription or customer.

If you update metadata on a subscription or customer with a metafield that does not already exist, the metafield is created with the metadata you specify and it is always added as a text field to the Site and to the subscription or customer you specify. You can update the input_type for the metafield with the Update Metafield endpoint. 

Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for the Subscription resource and another 100 for the Customer resource.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.custom_fields.update_metadata(ResourceType.SUBSCRIPTIONS, 1)
    # TODO: Handle 'response' of type list[Metadata]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMetadataErrorBody
```

**Async**

```python
try:
    response = await async_client.custom_fields.update_metadata(ResourceType.SUBSCRIPTIONS, 1)
    # TODO: Handle 'response' of type list[Metadata]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMetadataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>resource_id</code> | <code>int</code> | The Advanced Billing id of the customer or the subscription for which the metadata applies |
| <code>body</code> | <code>[UpdateMetadataRequest](maxio_advanced_billing/models/update_metadata_request.py) \| [UpdateMetadataRequestDict](maxio_advanced_billing/models/update_metadata_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Metadata](maxio_advanced_billing/models/metadata.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateMetadataErrorBody](maxio_advanced_billing/errors/update_metadata_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_metafield(resource_type: ResourceTypeOrStr, *, body: UpdateMetafieldsRequest | UpdateMetafieldsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> list[Metafield]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates metafields on your Site for a resource type.  Depending on the request structure, you can update or add metafields and metadata to the Subscriptions or Customers resource.

With this endpoint, you can: 

- Add metafields. If the metafield specified in current_name does not exist, a new metafield is added. 
  >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for Subscriptions and another 100 for Customers.

- Change the name of a metafield. 
  >Note: To keep the metafield name the same and only update the metadata for the metafield, you must use the current metafield name in both the `current_name` and `name` parameters.

- Change the input type for the metafield. For example, you can change a metafield input type from text to a dropdown. If you change the input type from text to a dropdown or radio, you must update the specific subscriptions or customers where the metafield was used to reflect the updated metafield and metadata. 

- Add metadata values to the existing metadata for a dropdown or radio metafield. 
  >Note: Updates to metadata overwrite. To add one or more values, you must specify all metadata values including the new value you want to add.

- Add new metadata to a dropdown or radio for a metafield that was created without metadata.

- Remove metadata for a dropdown or radio for a metafield.
  >Note: Updates to metadata overwrite existing values. To remove one or more values, specify all metadata values except those you want to remove.

- Add or update scope settings for a metafield.
  >Note: Scope changes overwrite existing settings. You must specify the complete scope, including the changes you want to make.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.custom_fields.update_metafield(ResourceType.SUBSCRIPTIONS)
    # TODO: Handle 'response' of type list[Metafield]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMetafieldErrorBody
```

**Async**

```python
try:
    response = await async_client.custom_fields.update_metafield(ResourceType.SUBSCRIPTIONS)
    # TODO: Handle 'response' of type list[Metafield]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMetafieldErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource_type</code> | <code>[ResourceTypeOrStr](maxio_advanced_billing/models/enums/resource_type.py)</code> | The resource type to which the metafields belong. |
| <code>body</code> | <code>[UpdateMetafieldsRequest](maxio_advanced_billing/models/update_metafields_request.py) \| [UpdateMetafieldsRequestDict](maxio_advanced_billing/models/update_metafields_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Metafield](maxio_advanced_billing/models/metafield.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateMetafieldErrorBody](maxio_advanced_billing/errors/update_metafield_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Customers

> Source: [Customers](maxio_advanced_billing/apis/customers.py)

<details>
<summary><code>def create_customer(*, body: CreateCustomerRequest | CreateCustomerRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new customer; can also be created alongside a new subscription. The only validation restriction is that you can only create one customer for a given reference value.

If provided, the `reference` value must be unique. It represents a unique identifier for the customer from your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared information. Alternatively, you can choose to leave `reference` blank, and store the system-assigned unique ID for the customer, which is in the `id` attribute.

For more information, see [Customer Details](https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details).

## Required Country Format

Format the country attribute of the customer using the ISO Standard Country codes.

Countries should be formatted as two characters. For more information, see [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes).

## Required State Format

Format the state attribute of the customer using the ISO Standard State codes.

+ US States (two characters): see [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:US).

+ States Outside the US (two to three characters): To find the correct state codes outside the US, go to [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) and click on the link in the “ISO 3166-2 codes” column next to the country you wish to populate.

## Locale

You can attribute a language/region to the customer to deliver invoices in any required language. For more information, see [Customer Locale](https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale).

## Tax and Business Identifiers

Send `entity_identifier_kind` and `entity_identifier_value` together to store the customer's tax or business identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time.

The `vat_eu` and `national_tax` kinds also require `vat_country`. An unsupported kind, a missing or mismatched `vat_country`, or a `gln`, `duns`, or `lei` value in the wrong format returns `422`.

Always send the kind. `entity_identifier_value` on its own is stored as a `company_reg` when no `vat_country` is present, and returns `422` naming `entity_identifier_kind` when one is.

A blank pair is ignored rather than rejected, so a `vat_number` sent alongside it still takes effect.

The legacy `vat_number` and `vat_country` pair still works on its own. When neither entity identifier field is sent, Advanced Billing derives the kind from `vat_country`: an EU member state code or `GB` gives `vat_eu`, one of the national tax country codes gives `national_tax`, and a blank or unrecognized country gives `company_reg`.

The response reports the stored identifier in `entity_identifier_kind` and `entity_identifier_value`, and repeats its value in `vat_number`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.customers.create_customer(
        body=CreateCustomerRequest(
            customer=CreateCustomer(
                first_name="Martha",
                last_name="Washington",
                email="martha@example.com",
                cc_emails="george@example.com",
                organization="ABC, Inc.",
                reference="1234567890",
                address="123 Main Street",
                address_2="Unit 10",
                city="Anytown",
                state="MA",
                zip="02120",
                country="US",
                phone="555-555-1212",
                locale="es-MX",
            ),
        ),
    )
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateCustomerErrorBody
```

**Async**

```python
try:
    response = await async_client.customers.create_customer(
        body=CreateCustomerRequest(
            customer=CreateCustomer(
                first_name="Martha",
                last_name="Washington",
                email="martha@example.com",
                cc_emails="george@example.com",
                organization="ABC, Inc.",
                reference="1234567890",
                address="123 Main Street",
                address_2="Unit 10",
                city="Anytown",
                state="MA",
                zip="02120",
                country="US",
                phone="555-555-1212",
                locale="es-MX",
            ),
        ),
    )
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateCustomerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateCustomerRequest](maxio_advanced_billing/models/create_customer_request.py) \| [CreateCustomerRequestDict](maxio_advanced_billing/models/create_customer_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CustomerResponse](maxio_advanced_billing/models/customer_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateCustomerErrorBody](maxio_advanced_billing/errors/create_customer_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[CustomerErrorResponse1](maxio_advanced_billing/models/customer_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_customer(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.customers.delete_customer(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.customers.delete_customer(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the customer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_customer_subscriptions(customer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> list[SubscriptionResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all subscriptions that belong to a customer.

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, subscriptions no longer require an associated product. For subscriptions without an associated product, 'product', 'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.customers.list_customer_subscriptions(1)
    # TODO: Handle 'response' of type list[SubscriptionResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.customers.list_customer_subscriptions(1)
    # TODO: Handle 'response' of type list[SubscriptionResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>int</code> | The Chargify id of the customer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_customers(*, direction: SortingDirectionOrStr | None = None, page: int | None = 1, per_page: int | None = 50, date_field: BasicDateFieldOrStr | None = None, start_date: str | None = None, end_date: str | None = None, start_datetime: str | None = None, end_datetime: str | None = None, q: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[CustomerResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all customers associated with your site, or filters results using the search parameter.

## Find Customer

Use the search feature with the `q` query parameter to retrieve an array of customers that matches the search query.

Common use cases are:

+ Search by an email
+ Search by an Advanced Billing ID
+ Search by an organization
+ Search by a reference value from your application
+ Search by a first or last name

To retrieve a single, exact match by reference, use the [lookup endpoint](https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.customers.list_customers(page=1, per_page=30, date_field=BasicDateField.UPDATED_AT)
    # TODO: Handle 'response' of type list[CustomerResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.customers.list_customers(page=1, per_page=30, date_field=BasicDateField.UPDATED_AT)
    # TODO: Handle 'response' of type list[CustomerResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Direction to sort customers by time of creation<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 50. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>50</code> |
| <code>date_field</code> | <code>[BasicDateFieldOrStr](maxio_advanced_billing/models/enums/basic_date_field.py) \| None</code> | The type of filter you would like to apply to your search.<br>Use in query: `date_field=created_at`.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns subscriptions with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns subscriptions with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>q</code> | <code>str \| None</code> | A search query by which to filter customers (can be an email, an ID, a reference, organization)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[CustomerResponse](maxio_advanced_billing/models/customer_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_customer(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the Customer properties by Advanced Billing-generated Customer ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.customers.read_customer(1)
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.customers.read_customer(1)
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the customer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CustomerResponse](maxio_advanced_billing/models/customer_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_customer_by_reference(reference: str, *, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a customer by their unique reference ID. It will return a single match.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.customers.read_customer_by_reference("some example string")
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.customers.read_customer_by_reference("some example string")
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reference</code> | <code>str</code> | Customer reference |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CustomerResponse](maxio_advanced_billing/models/customer_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_customer(id_: int, *, body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the customer.

## Tax and Business Identifiers

Send `entity_identifier_kind` and `entity_identifier_value` together to store the customer's tax or business identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time, so saving an identifier of a different kind replaces the existing one.

The `vat_eu` and `national_tax` kinds also require `vat_country`. An unsupported kind, a missing or mismatched `vat_country`, or a `gln`, `duns`, or `lei` value in the wrong format returns `422`.

Always send the kind. `entity_identifier_value` on its own is stored as a `company_reg` when no `vat_country` is present, and returns `422` naming `entity_identifier_kind` when one is.

To clear an identifier, send a supported `entity_identifier_kind` with a blank `entity_identifier_value`, or send a blank `vat_number` on its own. The first form also clears `vat_number` and `vat_country`, and it removes whichever identifier the customer holds, whatever kind you send with it.

The legacy `vat_number` and `vat_country` pair still works on its own. When neither entity identifier field is sent, Advanced Billing derives the kind from `vat_country`: an EU member state code or `GB` gives `vat_eu`, one of the national tax country codes gives `national_tax`, and a blank or unrecognized country gives `company_reg`.

Sending a customer response straight back leaves the tax ID alone. A blank pair, and a pair that still matches the stored identifier with `vat_country` unchanged, are read as nothing to change rather than as a request to clear. For `gln`, `duns`, and `lei` that also covers the `vat_number` the response mirrors back, so the kind survives the round trip.

What you do change is applied, and the entity identifier fields take precedence over `vat_number`. A different kind or value writes that identifier, and `vat_number` and `vat_country` follow from it. A different `vat_country` next to an unchanged pair is a real edit, so it is validated and can return `422`. Changing only `vat_number` leaves the pair unchanged, so the derivation above decides the kind, which turns a `gln`, `duns`, or `lei` customer into a `company_reg`. Setting `vat_number` to `null` or a blank string still clears the identifier.

The response reports the stored identifier in `entity_identifier_kind` and `entity_identifier_value`, and repeats its value in `vat_number`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.customers.update_customer(
        1,
        body=UpdateCustomerRequest(
            customer=UpdateCustomer(first_name="Martha", last_name="Washington", email="martha.washington@example.com")
        ),
    )
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCustomerErrorBody
```

**Async**

```python
try:
    response = await async_client.customers.update_customer(
        1,
        body=UpdateCustomerRequest(
            customer=UpdateCustomer(first_name="Martha", last_name="Washington", email="martha.washington@example.com")
        ),
    )
    # TODO: Handle 'response' of type CustomerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCustomerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the customer |
| <code>body</code> | <code>[UpdateCustomerRequest](maxio_advanced_billing/models/update_customer_request.py) \| [UpdateCustomerRequestDict](maxio_advanced_billing/models/update_customer_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CustomerResponse](maxio_advanced_billing/models/customer_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateCustomerErrorBody](maxio_advanced_billing/errors/update_customer_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[CustomerErrorResponse1](maxio_advanced_billing/models/customer_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Entitlements

> Source: [Entitlements](maxio_advanced_billing/apis/entitlements.py)

<details>
<summary><code>def read_subscription_entitlements(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> AggregatedEntitlementsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns every feature a subscription is entitled to, collapsed into one entry per feature key and periodicity window across all products and components on the subscription. A `usage_limit` feature granted with two different periodicities comes back as two entries sharing one `feature_key`, each identified by its own `periodicity_key`.

When more than one product or component grants the same feature key and periodicity, the values are combined:
- **`access_right`** features are combined with a boolean OR. If any contributor grants access, the aggregate is `true`. `source_products` only lists the contributors that granted `true`.
- **`usage_limit`** features are summed across every contributor sharing the same periodicity window. `source_products` lists every contributor. Grants with different periodicities are not summed together. Each periodicity is returned as a separate entry.
- **`service_right`** features are not combined: one contributor's value wins. Do not rely on which one when several grant the same feature key.

`enabled` reflects both the aggregated value and the subscription's state. The field is `false` whenever the subscription is not in a live state (`active`, `trialing`, `assessing`, `past_due`, `soft_failure`), regardless of the aggregated value. Entitlements deliberately stay enabled through dunning.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.entitlements.read_subscription_entitlements(1)
    # TODO: Handle 'response' of type AggregatedEntitlementsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadSubscriptionEntitlementsErrorBody
```

**Async**

```python
try:
    response = await async_client.entitlements.read_subscription_entitlements(1)
    # TODO: Handle 'response' of type AggregatedEntitlementsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadSubscriptionEntitlementsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AggregatedEntitlementsResponse](maxio_advanced_billing/models/aggregated_entitlements_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadSubscriptionEntitlementsErrorBody](maxio_advanced_billing/errors/read_subscription_entitlements_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Events

> Source: [Events](maxio_advanced_billing/apis/events.py)

<details>
<summary><code>def list_events(*, page: int | None = 1, per_page: int | None = 20, since_id: int | None = None, max_id: int | None = None, direction: DirectionOrStr | None = Direction.DESC, filter_: list[EventKeyOrStr] | None = None, date_field: ListEventsDateFieldOrStr | None = None, start_date: str | None = None, end_date: str | None = None, start_datetime: str | None = None, end_datetime: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[EventResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists events for a site.

Events include various activity that happens around a Site. This information is **especially** useful to track down issues that arise when subscriptions are not created due to errors.

Within the UI, Events are referred to as Site Activity. For more information, see [Site Activity](https://maxio.zendesk.com/hc/en-us/articles/24250671733517-Site-Activity).

Use query string filters to narrow down results. You can use the `filter` parameter to filter by event key.

### Legacy Filters

The following keys are no longer supported.

+ `payment_failure_recreated`
+ `payment_success_recreated`
+ `renewal_failure_recreated`
+ `renewal_success_recreated`
+ `zferral_revenue_post_failure` - (Specific to the deprecated Zferral integration)
+ `zferral_revenue_post_success` - (Specific to the deprecated Zferral integration)

## Event Key
The event type is identified by the key property. See [Event Key]($m/Event%20Key) for a complete list of supported keys.

## Event Specific Data

Different event types may include additional data in `event_specific_data` property.
While some events share the same schema for `event_specific_data`, others may not include it at all.
For precise mappings from key to event_specific_data, refer to [Event]($m/Event).

### Example
Here’s an example event for the `subscription_product_change` event:

``
{
    "event": {
        "id": 351,
        "key": "subscription_product_change",
        "message": "Product changed on Mark Alan's subscription from 'Basic' to 'Pro'",
        "subscription_id": 205,
        "event_specific_data": {
            "new_product_id": 3,
            "previous_product_id": 2
        },
        "created_at": "2012-01-30T10:43:31-05:00"
    }
}
``

Here’s an example event for the `subscription_state_change` event:

``
 {
     "event": {
         "id": 353,
         "key": "subscription_state_change",
         "message": "State changed on Mark Alan's subscription to Pro from trialing to active",
         "subscription_id": 205,
         "event_specific_data": {
             "new_subscription_state": "active",
             "previous_subscription_state": "trialing"
         },
         "created_at": "2012-01-30T10:43:33-05:00"
     }
 }
``

## Enhanced Catalog Experience

If you’re using the [enhanced Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology), you’ll see updated naming in webhook events and messages.

Event name changes:

- subscription_product_change → subscription_plan_change
- component_allocation_change → allocation_change
- component_billing_date_change → product_billing_date_change

Message updates:

- “Plan changed on Subscription from previous plan to new plan”
- “Successful payment for allocation changes to Product on Subscription”
- “Failed payment for allocation changes to Product on Subscription”

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events.list_events(
        page=1,
        per_page=50,
        filter_=[EventKey.CUSTOM_FIELD_VALUE_CHANGE, EventKey.PAYMENT_SUCCESS],
        date_field=ListEventsDateField.CREATED_AT,
    )
    # TODO: Handle 'response' of type list[EventResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.events.list_events(
        page=1,
        per_page=50,
        filter_=[EventKey.CUSTOM_FIELD_VALUE_CHANGE, EventKey.PAYMENT_SUCCESS],
        date_field=ListEventsDateField.CREATED_AT,
    )
    # TODO: Handle 'response' of type list[EventResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>since_id</code> | <code>int \| None</code> | Returns events with an id greater than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>max_id</code> | <code>int \| None</code> | Returns events with an id less than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | The sort direction of the returned events.<br>**Default**: <code>Direction.DESC</code> |
| <code>filter_</code> | <code>list&#91;[EventKeyOrStr](maxio_advanced_billing/models/enums/event_key.py)&#93; \| None</code> | You can pass multiple event keys after comma.<br>Use in query `filter=signup_success,payment_success`.<br>**Default**: <code>None</code> |
| <code>date_field</code> | <code>[ListEventsDateFieldOrStr](maxio_advanced_billing/models/enums/list_events_date_field.py) \| None</code> | The type of filter you would like to apply to your search.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[EventResponse](maxio_advanced_billing/models/event_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_events(subscription_id: int, *, page: int | None = 1, per_page: int | None = 20, since_id: int | None = None, max_id: int | None = None, direction: DirectionOrStr | None = Direction.DESC, filter_: list[EventKeyOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> list[EventResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists events for a subscription.

## Event Key
The event type is identified by the key property. See [Event Key]($m/Event%20Key) for a complete list of supported keys.

## Event Specific Data

Different event types may include additional data in `event_specific_data` property.
While some events share the same schema for `event_specific_data`, others may not include it at all.
For precise mappings from key to event_specific_data, refer to [Event]($m/Event).

## Enhanced Catalog Experience

If you’re using the [enhanced Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology), you’ll see updated naming in webhook events and messages.

Event name changes:

- subscription_product_change → subscription_plan_change
- component_allocation_change → allocation_change
- component_billing_date_change → product_billing_date_change

Message updates:

- “Successful payment for allocation changes to Product on Subscription”
- “Failed payment for allocation changes to Product on Subscription”
- “Plan changed on Subscription from previous plan to new plan”

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events.list_subscription_events(
        1, page=1, per_page=50, filter_=[EventKey.CUSTOM_FIELD_VALUE_CHANGE, EventKey.PAYMENT_SUCCESS]
    )
    # TODO: Handle 'response' of type list[EventResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.events.list_subscription_events(
        1, page=1, per_page=50, filter_=[EventKey.CUSTOM_FIELD_VALUE_CHANGE, EventKey.PAYMENT_SUCCESS]
    )
    # TODO: Handle 'response' of type list[EventResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>since_id</code> | <code>int \| None</code> | Returns events with an id greater than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>max_id</code> | <code>int \| None</code> | Returns events with an id less than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | The sort direction of the returned events.<br>**Default**: <code>Direction.DESC</code> |
| <code>filter_</code> | <code>list&#91;[EventKeyOrStr](maxio_advanced_billing/models/enums/event_key.py)&#93; \| None</code> | You can pass multiple event keys after comma.<br>Use in query `filter=signup_success,payment_success`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[EventResponse](maxio_advanced_billing/models/event_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_events_count(*, page: int | None = 1, per_page: int | None = 20, since_id: int | None = None, max_id: int | None = None, direction: DirectionOrStr | None = Direction.DESC, filter_: list[EventKeyOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> CountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the total count of events for a given site.

If you’re using the [enhanced Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology), you’ll see updated naming in webhook events and messages.

Event name changes:

- subscription_product_change → subscription_plan_change
- component_allocation_change → allocation_change
- component_billing_date_change → product_billing_date_change

Message updates:

- “Successful payment for allocation changes to Product on Subscription”
- “Failed payment for allocation changes to Product on Subscription”
- “Plan changed on Subscription from previous plan to new plan”

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events.read_events_count(
        page=1, per_page=50, filter_=[EventKey.CUSTOM_FIELD_VALUE_CHANGE, EventKey.PAYMENT_SUCCESS]
    )
    # TODO: Handle 'response' of type CountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.events.read_events_count(
        page=1, per_page=50, filter_=[EventKey.CUSTOM_FIELD_VALUE_CHANGE, EventKey.PAYMENT_SUCCESS]
    )
    # TODO: Handle 'response' of type CountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>since_id</code> | <code>int \| None</code> | Returns events with an id greater than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>max_id</code> | <code>int \| None</code> | Returns events with an id less than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | The sort direction of the returned events.<br>**Default**: <code>Direction.DESC</code> |
| <code>filter_</code> | <code>list&#91;[EventKeyOrStr](maxio_advanced_billing/models/enums/event_key.py)&#93; \| None</code> | You can pass multiple event keys after comma.<br>Use in query `filter=signup_success,payment_success`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CountResponse](maxio_advanced_billing/models/count_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## EventsBasedBillingSegments

> Source: [EventsBasedBillingSegments](maxio_advanced_billing/apis/events_based_billing_segments.py)

<details>
<summary><code>def bulk_create_segments(component_id: str, price_point_id: str, *, body: BulkCreateSegments | BulkCreateSegmentsDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ListSegmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates multiple segments in one request. The array of segments can contain up to `2000` records.

If any of the records contain an error the whole request would fail and none of the requested segments get created. The error response contains a message for only the one segment that failed validation, with the corresponding index in the array.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events_based_billing_segments.bulk_create_segments("some example string", "some example string")
    # TODO: Handle 'response' of type ListSegmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkCreateSegmentsErrorBody
```

**Async**

```python
try:
    response = await async_client.events_based_billing_segments.bulk_create_segments(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type ListSegmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkCreateSegmentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | ID or Handle for the Component |
| <code>price_point_id</code> | <code>str</code> | ID or Handle for the Price Point belonging to the Component |
| <code>body</code> | <code>[BulkCreateSegments](maxio_advanced_billing/models/bulk_create_segments.py) \| [BulkCreateSegmentsDict](maxio_advanced_billing/models/bulk_create_segments.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListSegmentsResponse](maxio_advanced_billing/models/list_segments_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[BulkCreateSegmentsErrorBody](maxio_advanced_billing/errors/bulk_create_segments_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[EventBasedBillingSegment1](maxio_advanced_billing/models/event_based_billing_segment1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_update_segments(component_id: str, price_point_id: str, *, body: BulkUpdateSegments | BulkUpdateSegmentsDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ListSegmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates multiple segments in one request. The array of segments can contain up to `1000` records.

If any of the records contain an error the whole request would fail and none of the requested segments get updated. The error response contains a message for only the one segment that failed validation, with the corresponding index in the array.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events_based_billing_segments.bulk_update_segments("some example string", "some example string")
    # TODO: Handle 'response' of type ListSegmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkUpdateSegmentsErrorBody
```

**Async**

```python
try:
    response = await async_client.events_based_billing_segments.bulk_update_segments(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type ListSegmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkUpdateSegmentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | ID or Handle for the Component |
| <code>price_point_id</code> | <code>str</code> | ID or Handle for the Price Point belonging to the Component |
| <code>body</code> | <code>[BulkUpdateSegments](maxio_advanced_billing/models/bulk_update_segments.py) \| [BulkUpdateSegmentsDict](maxio_advanced_billing/models/bulk_update_segments.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListSegmentsResponse](maxio_advanced_billing/models/list_segments_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[BulkUpdateSegmentsErrorBody](maxio_advanced_billing/errors/bulk_update_segments_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[EventBasedBillingSegment1](maxio_advanced_billing/models/event_based_billing_segment1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_segment(component_id: str, price_point_id: str, *, body: CreateSegmentRequest | CreateSegmentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SegmentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new segment for a component with a segmented metric. It allows you to specify properties to bill upon and prices for each Segment. You can only pass as many "property_values" as the related Metric has segmenting properties defined.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events_based_billing_segments.create_segment(
        "some example string",
        "some example string",
        body=CreateSegmentRequest(
            segment=CreateSegment(
                segment_property_1_value="France",
                segment_property_2_value="Spain",
                pricing_scheme=PricingScheme.VOLUME,
                prices=[
                    CreateOrUpdateSegmentPrice(starting_quantity=1, ending_quantity=10000, unit_price=0.19),
                    CreateOrUpdateSegmentPrice(starting_quantity=10001, unit_price=0.09),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type SegmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSegmentErrorBody
```

**Async**

```python
try:
    response = await async_client.events_based_billing_segments.create_segment(
        "some example string",
        "some example string",
        body=CreateSegmentRequest(
            segment=CreateSegment(
                segment_property_1_value="France",
                segment_property_2_value="Spain",
                pricing_scheme=PricingScheme.VOLUME,
                prices=[
                    CreateOrUpdateSegmentPrice(starting_quantity=1, ending_quantity=10000, unit_price=0.19),
                    CreateOrUpdateSegmentPrice(starting_quantity=10001, unit_price=0.09),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type SegmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSegmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | ID or Handle for the Component |
| <code>price_point_id</code> | <code>str</code> | ID or Handle for the Price Point belonging to the Component |
| <code>body</code> | <code>[CreateSegmentRequest](maxio_advanced_billing/models/create_segment_request.py) \| [CreateSegmentRequestDict](maxio_advanced_billing/models/create_segment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SegmentResponse](maxio_advanced_billing/models/segment_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateSegmentErrorBody](maxio_advanced_billing/errors/create_segment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[EventBasedBillingSegmentErrors1](maxio_advanced_billing/models/event_based_billing_segment_errors1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_segment(component_id: str, price_point_id: str, id_: float, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a segment with the specified ID.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.events_based_billing_segments.delete_segment("some example string", "some example string", 1.5)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteSegmentErrorBody
```

**Async**

```python
try:
    await async_client.events_based_billing_segments.delete_segment("some example string", "some example string", 1.5)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteSegmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | ID or Handle of the Component |
| <code>price_point_id</code> | <code>str</code> | ID or Handle of the Price Point belonging to the Component |
| <code>id_</code> | <code>float</code> | The ID of the Segment |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteSegmentErrorBody](maxio_advanced_billing/errors/delete_segment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404, 422 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_segments_for_price_point(component_id: str, price_point_id: str, *, page: int | None = 1, per_page: int | None = 30, filter_: ListSegmentsFilter | ListSegmentsFilterDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ListSegmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists segments created for a given price point, in order of creation.

You can pass `page` and `per_page` parameters in order to access all of the segments. By default it will return `30` records. You can set `per_page` to `200` at most.

You may specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events_based_billing_segments.list_segments_for_price_point(
        "some example string", "some example string", page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListSegmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSegmentsForPricePointErrorBody
```

**Async**

```python
try:
    response = await async_client.events_based_billing_segments.list_segments_for_price_point(
        "some example string", "some example string", page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListSegmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSegmentsForPricePointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | ID or Handle for the Component |
| <code>price_point_id</code> | <code>str</code> | ID or Handle for the Price Point belonging to the Component |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 30. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>30</code> |
| <code>filter_</code> | <code>[ListSegmentsFilter](maxio_advanced_billing/models/list_segments_filter.py) \| [ListSegmentsFilterDict](maxio_advanced_billing/models/list_segments_filter.py) \| None</code> | Filter to use for List Segments for a Price Point operation<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListSegmentsResponse](maxio_advanced_billing/models/list_segments_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListSegmentsForPricePointErrorBody](maxio_advanced_billing/errors/list_segments_for_price_point_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[EventBasedBillingListSegmentsErrors1](maxio_advanced_billing/models/event_based_billing_list_segments_errors1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_segment(component_id: str, price_point_id: str, id_: float, *, body: UpdateSegmentRequest | UpdateSegmentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SegmentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a single segment for a component with a segmented metric. You can also update the pricing for the segment.

You can specify component and/or price point by using either the numeric ID or the `handle:gold` syntax.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.events_based_billing_segments.update_segment("some example string", "some example string", 1.5)
    # TODO: Handle 'response' of type SegmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSegmentErrorBody
```

**Async**

```python
try:
    response = await async_client.events_based_billing_segments.update_segment(
        "some example string", "some example string", 1.5
    )
    # TODO: Handle 'response' of type SegmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSegmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>component_id</code> | <code>str</code> | ID or Handle of the Component |
| <code>price_point_id</code> | <code>str</code> | ID or Handle of the Price Point belonging to the Component |
| <code>id_</code> | <code>float</code> | The ID of the Segment |
| <code>body</code> | <code>[UpdateSegmentRequest](maxio_advanced_billing/models/update_segment_request.py) \| [UpdateSegmentRequestDict](maxio_advanced_billing/models/update_segment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SegmentResponse](maxio_advanced_billing/models/segment_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateSegmentErrorBody](maxio_advanced_billing/errors/update_segment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[EventBasedBillingSegmentErrors1](maxio_advanced_billing/models/event_based_billing_segment_errors1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FeatureTemplates

> Source: [FeatureTemplates](maxio_advanced_billing/apis/feature_templates.py)

<details>
<summary><code>def archive_feature_template(id_: int, *, remove_from_catalog: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives a feature template. Archived feature templates are not addressable via [Read Feature Template]($e/Feature%20Templates/readFeatureTemplate) or [Update Feature Template]($e/Feature%20Templates/updateFeatureTemplate). Both endpoints return `404` until the template is restored.

The feature template record itself is never hard-deleted, and can always be restored with [Restore Feature Template]($e/Feature%20Templates/restoreFeatureTemplate). Reversibility does not extend to `remove_from_catalog=true`: the feature catalog items and entitlements that parameter destroys are gone permanently, and restoring the template will not bring subscriber access back.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.feature_templates.archive_feature_template(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveFeatureTemplateErrorBody
```

**Async**

```python
try:
    await async_client.feature_templates.archive_feature_template(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveFeatureTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature template. |
| <code>remove_from_catalog</code> | <code>bool \| None</code> | When `true`, also destroys every feature catalog item created from this template and cascades to their entitlements, revoking subscriber access immediately. When `false` (default), the feature template and its feature catalog items are archived, and existing entitlements are preserved.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ArchiveFeatureTemplateErrorBody](maxio_advanced_billing/errors/archive_feature_template_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_feature_template(*, body: CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> FeatureTemplateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Defines a new feature at the site level. Feature templates aren't billable on their own. Attach a template to products or components to grant the feature to subscribers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feature_templates.create_feature_template(
        body=CreateFeatureTemplateRequest(
            feature=Feature(key="sso", name="Single Sign-On", kind=FeatureKind.ACCESS_RIGHT)
        ),
    )
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateFeatureTemplateErrorBody
```

**Async**

```python
try:
    response = await async_client.feature_templates.create_feature_template(
        body=CreateFeatureTemplateRequest(
            feature=Feature(key="sso", name="Single Sign-On", kind=FeatureKind.ACCESS_RIGHT)
        ),
    )
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateFeatureTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateFeatureTemplateRequest](maxio_advanced_billing/models/create_feature_template_request.py) \| [CreateFeatureTemplateRequestDict](maxio_advanced_billing/models/create_feature_template_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureTemplateResponse](maxio_advanced_billing/models/feature_template_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateFeatureTemplateErrorBody](maxio_advanced_billing/errors/create_feature_template_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_feature_templates(*, page: int | None = 1, per_page: int | None = 20, status: Status1OrStr | None = Status1.ACTIVE, q: str | None = None, kind: KindOrStr | None = None, updated_from: Date | None = None, updated_to: Date | None = None, sort_by: SortByOrStr | None = SortBy.NAME, sort_direction: SortDirectionOrStr | None = SortDirection.ASC, request_options: RequestOptionsOrDict | None = None) -> FeatureTemplatesListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the feature templates defined for your site, active (non-archived) ones by default. Pass `status=archived` or `status=all` to widen the result set.

Supply `page` or `per_page` to paginate. Without either parameter, the response includes the full result set.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feature_templates.list_feature_templates(page=1, per_page=50)
    # TODO: Handle 'response' of type FeatureTemplatesListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFeatureTemplatesErrorBody
```

**Async**

```python
try:
    response = await async_client.feature_templates.list_feature_templates(page=1, per_page=50)
    # TODO: Handle 'response' of type FeatureTemplatesListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFeatureTemplatesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>status</code> | <code>[Status1OrStr](maxio_advanced_billing/models/enums/status1.py) \| None</code> | Filters by archived state. Defaults to `active` (non-archived templates only).<br>**Default**: <code>Status1.ACTIVE</code> |
| <code>q</code> | <code>str \| None</code> | Filters to feature templates whose name contains this substring (case-insensitive).<br>**Default**: <code>None</code> |
| <code>kind</code> | <code>[KindOrStr](maxio_advanced_billing/models/enums/kind.py) \| None</code> | Filters by feature kind.<br>**Default**: <code>None</code> |
| <code>updated_from</code> | <code>Date \| None</code> | Returns feature templates updated on or after this date.<br>**Default**: <code>None</code> |
| <code>updated_to</code> | <code>Date \| None</code> | Returns feature templates updated on or before this date.<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>[SortByOrStr](maxio_advanced_billing/models/enums/sort_by.py) \| None</code> | The field to sort results by.<br>**Default**: <code>SortBy.NAME</code> |
| <code>sort_direction</code> | <code>[SortDirectionOrStr](maxio_advanced_billing/models/enums/sort_direction.py) \| None</code> | The sort direction of the returned feature templates.<br>**Default**: <code>SortDirection.ASC</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureTemplatesListResponse](maxio_advanced_billing/models/feature_templates_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListFeatureTemplatesErrorBody](maxio_advanced_billing/errors/list_feature_templates_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_feature_template(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureTemplateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single feature template. Archived feature templates are not addressable here and return `404`. Restore a template first to read or update it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feature_templates.read_feature_template(1)
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadFeatureTemplateErrorBody
```

**Async**

```python
try:
    response = await async_client.feature_templates.read_feature_template(1)
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadFeatureTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature template. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureTemplateResponse](maxio_advanced_billing/models/feature_template_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadFeatureTemplateErrorBody](maxio_advanced_billing/errors/read_feature_template_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def restore_feature_template(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureTemplateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Clears the feature template's archived state. Feature catalog items created from this template are not automatically restored. Restore each one individually.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feature_templates.restore_feature_template(1)
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreFeatureTemplateErrorBody
```

**Async**

```python
try:
    response = await async_client.feature_templates.restore_feature_template(1)
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreFeatureTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature template. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureTemplateResponse](maxio_advanced_billing/models/feature_template_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RestoreFeatureTemplateErrorBody](maxio_advanced_billing/errors/restore_feature_template_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_feature_template(id_: int, *, body: UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> FeatureTemplateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the name, description, unit, value type, default value, or default periodicity of a feature template. `key` is rejected on every update. `kind` is rejected once any feature catalog item has been created from this template.

Archived feature templates are not addressable here and return `404`. Restore a template first to update it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feature_templates.update_feature_template(1)
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFeatureTemplateErrorBody
```

**Async**

```python
try:
    response = await async_client.feature_templates.update_feature_template(1)
    # TODO: Handle 'response' of type FeatureTemplateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFeatureTemplateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature template. |
| <code>body</code> | <code>[UpdateFeatureTemplateRequest](maxio_advanced_billing/models/update_feature_template_request.py) \| [UpdateFeatureTemplateRequestDict](maxio_advanced_billing/models/update_feature_template_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureTemplateResponse](maxio_advanced_billing/models/feature_template_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateFeatureTemplateErrorBody](maxio_advanced_billing/errors/update_feature_template_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Insights

> Source: [Insights](maxio_advanced_billing/apis/insights.py)

<details>
<summary><code>def list_mrr_movements(*, subscription_id: int | None = None, page: int | None = 1, per_page: int | None = 10, direction: SortingDirectionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ListMrrResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists your site's MRR movements.

## Understanding MRR movements

This endpoint will aid in accessing your site's [MRR Report](https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics) data.

Whenever a subscription event occurs that causes your site's MRR to change (such as a signup or upgrade), we record an MRR movement. These records are accessible via the MRR Movements endpoint.

Each MRR Movement belongs to a subscription and contains a timestamp, category, and an amount. `line_items` represent the subscription's product configuration at the time of the movement.

### Plan & Usage Breakouts

In the MRR Report UI, we support a setting to [include or exclude](https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics#displaying-component-based-metered-usage-in-mrr) usage revenue. In the MRR APIs, responses include `plan` and `usage` breakouts.

Plan includes revenue from:
* Products
* Quantity-Based Components
* On/Off Components

Usage includes revenue from:
* Metered Components
* Prepaid Usage Components

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.insights.list_mrr_movements(page=1, per_page=20)
    # TODO: Handle 'response' of type ListMrrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.insights.list_mrr_movements(page=1, per_page=20)
    # TODO: Handle 'response' of type ListMrrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int \| None</code> | (Optional) Filter results by subscription.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 10. The maximum allowed values is 50; any per_page value over 50 will be changed to 50.<br>Use in query `per_page=20`.<br>**Default**: <code>10</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListMrrResponse](maxio_advanced_billing/models/list_mrr_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_mrr_per_subscription(*, filter_: ListMrrFilter | ListMrrFilterDict | None = None, at_time: str | None = None, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionMrrResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists your site's current MRR, including plan and usage breakouts split per subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.insights.list_mrr_per_subscription(
        at_time="at_time=2022-01-10T10:00:00-05:00", page=1, per_page=50, direction=Direction.DESC
    )
    # TODO: Handle 'response' of type SubscriptionMrrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListMrrPerSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.insights.list_mrr_per_subscription(
        at_time="at_time=2022-01-10T10:00:00-05:00", page=1, per_page=50, direction=Direction.DESC
    )
    # TODO: Handle 'response' of type SubscriptionMrrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListMrrPerSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>filter_</code> | <code>[ListMrrFilter](maxio_advanced_billing/models/list_mrr_filter.py) \| [ListMrrFilterDict](maxio_advanced_billing/models/list_mrr_filter.py) \| None</code> | Filter to use for List MRR per subscription operation<br>**Default**: <code>None</code> |
| <code>at_time</code> | <code>str \| None</code> | Submit a timestamp in ISO8601 format to request MRR for a historic time. Use in query: `at_time=2022-01-10T10:00:00-05:00`.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | Controls the order in which results are returned. Records are ordered by subscription_id in ascending order by default. Use in query `direction=desc`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionMrrResponse](maxio_advanced_billing/models/subscription_mrr_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListMrrPerSubscriptionErrorBody](maxio_advanced_billing/errors/list_mrr_per_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[SubscriptionsMrrErrorResponse1](maxio_advanced_billing/models/subscriptions_mrr_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_mrr(*, at_time: RFC3339DateTime | None = None, subscription_id: int | None = None, request_options: RequestOptionsOrDict | None = None) -> MrrResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns your site's current MRR, including plan and usage breakouts.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.insights.read_mrr()
    # TODO: Handle 'response' of type MrrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.insights.read_mrr()
    # TODO: Handle 'response' of type MrrResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>at_time</code> | <code>RFC3339DateTime \| None</code> | submit a timestamp in ISO8601 format to request MRR for a historic time.<br>**Default**: <code>None</code> |
| <code>subscription_id</code> | <code>int \| None</code> | submit the id of a subscription in order to limit results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MrrResponse](maxio_advanced_billing/models/mrr_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_site_stats(*, request_options: RequestOptionsOrDict | None = None) -> SiteSummary</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns basic site-level stats. This API call only answers with JSON responses. An XML version is not provided.

## Stats Documentation

There currently is not a complimentary matching set of documentation that compliments this endpoint. However, each Site's dashboard will reflect the summary of information provided in the Stats response.

``
https://subdomain.chargify.com/dashboard
``

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.insights.read_site_stats()
    # TODO: Handle 'response' of type SiteSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.insights.read_site_stats()
    # TODO: Handle 'response' of type SiteSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteSummary](maxio_advanced_billing/models/site_summary.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Invoices

> Source: [Invoices](maxio_advanced_billing/apis/invoices.py)

<details>
<summary><code>def create_invoice(subscription_id: int, *, body: CreateInvoiceRequest | CreateInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> InvoiceResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an ad hoc invoice.

### Basic Behavior

You can create a basic invoice by sending an array of line items to this endpoint. Each line item, at a minimum, must include a title, a quantity and a unit price. Example:

``json
{
  "invoice": {
    "line_items": [
      {
        "title": "A Product",
        "quantity": 12,
        "unit_price": "150.00"
      }
    ]
  }
}
``

### Catalog items
Instead of creating custom products like in above example, You can pass existing items like products, components.

``json
{
  "invoice": {
    "line_items": [
      {
        "product_id": "handle:gold-product",
        "quantity": 2,
      }
    ]
  }
}
``


The price for each line item will be calculated as well as a total due amount for the invoice. Multiple line items can be sent.

### Line item types
When defining a line item, You can choose one of 3 types for a line item:
#### Custom item
As shown in the basic behavior example, You can pass `title` and `unit_price` for custom item.
#### Product id
Product handle (with handle: prefix) or id from the scope of current subscription's site can be provided with `product_id`. By default `unit_price` is taken from product's default price point, but can be overwritten by passing `unit_price` or `product_price_point_id`. If `product_id` is used, following fields cannot be used: `title`, `component_id`.
#### Component id
Component handle (with handle: prefix) or id from the scope of current subscription's site can be provided with `component_id`. If `component_id` is used, following fields cannot be used: `title`, `product_id`. By default `unit_price` is taken from product's default price point, but can be overwritten by passing `unit_price` or `price_point_id`. At this moment price points are supported only for quantity based, on/off and metered components. For prepaid and event based billing components `unit_price` is required.

### Coupons
When creating ad hoc invoice, new discounts can be applied in following way:

``json
{
  "invoice": {
    "line_items": [
      {
        "product_id": "handle:gold-product",
        "quantity": 1
      }
    ],
    "coupons": [
      {
        "code": "COUPONCODE",
        "percentage": 50.0
      }
    ]
  }
}
``
If You want to use existing coupon for discount creation, only `code` and optional `product_family_id` is needed

``json
...
 "coupons": [
      {
        "code": "FREESETUP",
        "product_family_id": 1
      }
  ]
...
``

#### Using Coupon Subcodes
You can also use coupon subcodes to apply existing coupons with specific subcodes:

``json
...
 "coupons": [
      {
        "subcode": "SUB1",
        "product_family_id": 1
      }
  ]
...
``
**Important:** You cannot specify both `code` and `subcode` for the same coupon. Use either:
- `code` to apply a main coupon
- `subcode` to apply a specific coupon subcode

The API response will include both the main coupon code and the subcode used:

``json
...
 "coupons": [
      {
        "code": "MAIN123",
        "subcode": "SUB1",
        "product_family_id": 1,
        "percentage": 10,
        "description": "Special discount"
      }
  ]
...
``

### Coupon options
#### Code
Coupon `code` will be displayed on invoice discount section.
Coupon code can only contain uppercase letters, numbers, and allowed special characters.
Lowercase letters will be converted to uppercase. It can be used to select an existing coupon from the catalog, or as an ad hoc coupon when passed with `percentage` or `amount`.
#### Subcode
Coupon `subcode` allows you to apply existing coupons using their subcodes. When a subcode is used, the API response will include both the main coupon code and the specific subcode that was applied. Subcodes are case-insensitive and will be converted to uppercase automatically.
#### Percentage
Coupon `percentage` can take values from 0 to 100 and up to 4 decimal places. It cannot be used with `amount`. Only for ad hoc coupons, will be ignored if `code` is used to select an existing coupon from the catalog.
#### Amount
Coupon `amount` takes number value. It cannot be used with `percentage`. Used only when not matching existing coupon by `code`.
#### Description
Optional `description` will be displayed with coupon `code`. Used only when not matching existing coupon by `code`.
#### Product Family id
Optional `product_family_id` handle (with handle: prefix) or id is used to match existing coupon within site, when codes are not unique.
#### Compounding Strategy
Optional `compounding_strategy` for percentage coupons, can take values `compound` or `full-price`.

For amount coupons, discounts will be always calculated against the original item price, before other discounts are applied.

`compound` strategy:
Percentage-based discounts will be calculated against the remaining price, after prior discounts have been calculated. It is set by default.

`full-price` strategy:
Percentage-based discounts will always be calculated against the original item price, before other discounts are applied.

### Line Item Options

#### Period Date Range

A custom period date range can be defined for each line item with the `period_range_start` and `period_range_end` parameters. Dates must be sent in the `YYYY-MM-DD` format.
`period_range_end` must be greater or equal `period_range_start`.

#### Taxes

The `taxable` parameter can be sent as `true` if taxes should be calculated for a specific line item. For this to work, the site should be configured to use and calculate taxes. Further, if the site uses Avalara for tax calculations, a `tax_code` parameter should also be sent. For existing catalog items: products/components taxes cannot be overwritten.

#### Price Point
Price point handle (with handle: prefix) or id from the scope of current subscription's site can be provided with `price_point_id` for components with `component_id` or `product_price_point_id` for products with `product_id` parameter. If price point is passed `unit_price` cannot be used. It can be used only with catalog items products and components.

#### Description
Optional `description` parameter, it will overwrite default generated description for line item.

### Invoice Options

#### Issue Date

By default, invoices will be created with a issue date set to today in your site's time zone. The `issue_date` parameter can be sent to alter the default. Only today or dates in the past are accepted. This date is interpreted and validated in your site's time zone. The format for `issue_date` is `YYYY-MM-DD`.

#### Net Terms

By default, invoices will be created with a due date matching the date of invoice creation. If a different due date is desired, the `net_terms` parameter can be sent indicating the number of days in advance the due date should be.

#### Addresses

The seller, shipping and billing addresses can be sent to override the site's defaults. Each address requires to send a `first_name` at a minimum in order to work. See below for the details on which parameters can be sent for each address object.

#### Memo and Payment Instructions

A custom memo can be sent with the `memo` parameter to override the site's default. Likewise, custom payment instructions can be sent with the `payment_instructions` parameter.

#### Status

By default, invoices will be created with open status. Possible alternative is `draft`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.create_invoice(
        1,
        body=CreateInvoiceRequest(
            invoice=CreateInvoice(line_items=[CreateInvoiceItem(title="A Product", quantity=12, unit_price="150.00")])
        ),
    )
    # TODO: Handle 'response' of type InvoiceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.create_invoice(
        1,
        body=CreateInvoiceRequest(
            invoice=CreateInvoice(line_items=[CreateInvoiceItem(title="A Product", quantity=12, unit_price="150.00")])
        ),
    )
    # TODO: Handle 'response' of type InvoiceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[CreateInvoiceRequest](maxio_advanced_billing/models/create_invoice_request.py) \| [CreateInvoiceRequestDict](maxio_advanced_billing/models/create_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InvoiceResponse](maxio_advanced_billing/models/invoice_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateInvoiceErrorBody](maxio_advanced_billing/errors/create_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_invoice(subscription_id: int, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an ad hoc invoice while it is in the `draft` state.

**Important: only invoices with the `adhoc` role and `draft` status can be deleted.** Any other invoice — issued, or with a different role (e.g. `renewal`, `signup`) — cannot be deleted through this endpoint and the request returns a `422` error. Issued invoices should be voided instead. If the invoice does not belong to the provided subscription, a `404` error is returned.

A successful deletion returns a `204 No Content` response and the invoice is permanently removed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.invoices.delete_invoice(1, "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteInvoiceErrorBody
```

**Async**

```python
try:
    await async_client.invoices.delete_invoice(1, "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteInvoiceErrorBody](maxio_advanced_billing/errors/delete_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issue_invoice(uid: str, *, body: IssueInvoiceRequest | IssueInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Issues an invoice that is in "pending" or "draft" status. For example, you can issue an invoice that was created when allocating new quantity on a component and using "accrue charges" option.

You cannot issue a pending child invoice that was created for a member subscription in a group.

For Remittance subscriptions, the invoice will go into "open" status and payment won't be attempted. The value for `on_failed_payment` would be rejected if sent. Any prepayments or service credits that exist on the subscription will be automatically applied. Additionally, if the setting is enabled, an email will be sent for the issued invoice.

For Automatic subscriptions, prepayments and service credits will apply to the invoice before payment is attempted. On successful payment, the invoice will go into "paid" status and email will be sent to the customer (if setting applies). When payment fails, the next event depends on the `on_failed_payment` value:
- `leave_open_invoice` - prepayments and credits applied to invoice; invoice status set to "open"; email sent to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice history. This is the default option.
- `rollback_to_pending` - prepayments and credits not applied; invoice remains in "pending" status; no email sent to the customer; payment failure recorded in the invoice history.
- `initiate_dunning` - prepayments and credits applied to the invoice; invoice status set to "open"; email sent to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice history; subscription will  most likely go into "past_due" or "canceled" state (depending upon net terms and dunning settings).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.issue_invoice("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.issue_invoice("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>body</code> | <code>[IssueInvoiceRequest](maxio_advanced_billing/models/issue_invoice_request.py) \| [IssueInvoiceRequestDict](maxio_advanced_billing/models/issue_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[IssueInvoiceErrorBody](maxio_advanced_billing/errors/issue_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_consolidated_invoice_segments(invoice_uid: str, *, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = Direction.ASC, request_options: RequestOptionsOrDict | None = None) -> ConsolidatedInvoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists segments for a consolidated invoice. Invoice segments returned on the index will only include totals, not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, or `custom_fields`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.list_consolidated_invoice_segments("some example string", page=1, per_page=50)
    # TODO: Handle 'response' of type ConsolidatedInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invoices.list_consolidated_invoice_segments(
        "some example string", page=1, per_page=50
    )
    # TODO: Handle 'response' of type ConsolidatedInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_uid</code> | <code>str</code> | The unique identifier of the consolidated invoice |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | Sort direction of the returned segments.<br>**Default**: <code>Direction.ASC</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConsolidatedInvoice](maxio_advanced_billing/models/consolidated_invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_credit_notes(*, subscription_id: int | None = None, date_field: CreditNoteDateFieldOrStr | None = CreditNoteDateField.ISSUE_DATE, start_date: str | None = None, end_date: str | None = None, start_datetime: str | None = None, end_datetime: str | None = None, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = Direction.DESC, line_items: bool | None = False, discounts: bool | None = False, taxes: bool | None = False, refunds: bool | None = False, applications: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ListCreditNotesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists credit notes for a site. Credit Notes are like inverse invoices. They reduce the amount a customer owes.

By default, the credit notes returned by this endpoint will exclude the arrays of `line_items`, `discounts`, `taxes`, `applications`, or `refunds`. To include these arrays, pass the specific field as a key in the query with a value set to `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.list_credit_notes(date_field=CreditNoteDateField.ISSUE_DATE, page=1, per_page=50)
    # TODO: Handle 'response' of type ListCreditNotesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invoices.list_credit_notes(
        date_field=CreditNoteDateField.ISSUE_DATE, page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListCreditNotesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int \| None</code> | The subscription's Advanced Billing id<br>**Default**: <code>None</code> |
| <code>date_field</code> | <code>[CreditNoteDateFieldOrStr](maxio_advanced_billing/models/enums/credit_note_date_field.py) \| None</code> | The type of filter you would like to apply to your search. Use in query `date_field=issue_date`. If a date range is provided without an explicit `date_field`, it defaults to `issue_date`. If only `start_datetime`/`end_datetime` are provided without an explicit `date_field`, it defaults to `created_at` instead. An unrecognized `date_field` is ignored rather than raising an error.<br>**Default**: <code>CreditNoteDateField.ISSUE_DATE</code> |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns credit notes with a timestamp at or after exact time provided in query. If provided, this parameter will be used instead of start_date. If no timezone offset is included in the value, it is interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns credit notes with a timestamp at or before exact time provided in query. If provided, this parameter will be used instead of end_date. If no timezone offset is included in the value, it is interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | The sort direction of the returned credit notes, sorted by sequence_number.<br>**Default**: <code>Direction.DESC</code> |
| <code>line_items</code> | <code>bool \| None</code> | Include line items data.<br>**Default**: <code>False</code> |
| <code>discounts</code> | <code>bool \| None</code> | Include discounts data.<br>**Default**: <code>False</code> |
| <code>taxes</code> | <code>bool \| None</code> | Include taxes data.<br>**Default**: <code>False</code> |
| <code>refunds</code> | <code>bool \| None</code> | Include refunds data.<br>**Default**: <code>False</code> |
| <code>applications</code> | <code>bool \| None</code> | Include applications data.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListCreditNotesResponse](maxio_advanced_billing/models/list_credit_notes_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_invoice_events(*, since_date: str | None = None, since_id: int | None = None, page: int | None = 1, per_page: int | None = 100, invoice_uid: str | None = None, with_change_invoice_status: str | None = None, event_types: list[InvoiceEventTypeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInvoiceEventsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists invoice events for a site. Each event contains event "data" (such as an applied payment) as well as a snapshot of the `invoice` at the time of event completion.

Exposed event types are:

+ issue_invoice
+ apply_credit_note
+ apply_payment
+ refund_invoice
+ void_invoice
+ void_remainder
+ backport_invoice
+ change_invoice_status
+ change_invoice_collection_method
+ remove_payment
+ failed_payment
+ apply_debit_note
+ create_debit_note
+ change_chargeback_status

Invoice events are returned in ascending order.

If both a `since_date` and `since_id` are provided in request parameters, the `since_date` will be used.

Note - invoice events that occurred prior to 09/05/2018 __will not__ contain an `invoice` snapshot.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.list_invoice_events(page=1)
    # TODO: Handle 'response' of type ListInvoiceEventsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invoices.list_invoice_events(page=1)
    # TODO: Handle 'response' of type ListInvoiceEventsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>since_date</code> | <code>str \| None</code> | The timestamp in a format `YYYY-MM-DD T HH:MM:SS Z`, or `YYYY-MM-DD`(in this case, it returns data from the beginning of the day). of the event from which you want to start the search. All the events before the `since_date` timestamp are not returned in the response.<br>**Default**: <code>None</code> |
| <code>since_id</code> | <code>int \| None</code> | The ID of the event from which you want to start the search(ID is not included. e.g. if ID is set to 2, then all events with ID 3 and more will be shown) This parameter is not used if since_date is defined.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 100. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>**Default**: <code>100</code> |
| <code>invoice_uid</code> | <code>str \| None</code> | Providing an invoice_uid allows for scoping of the invoice events to a single invoice or credit note.<br>**Default**: <code>None</code> |
| <code>with_change_invoice_status</code> | <code>str \| None</code> | Use this parameter if you want to fetch also invoice events with change_invoice_status type.<br>**Default**: <code>None</code> |
| <code>event_types</code> | <code>list&#91;[InvoiceEventTypeOrStr](maxio_advanced_billing/models/enums/invoice_event_type.py)&#93; \| None</code> | Filter results by event_type. Supply a comma separated list of event types (listed above). Use in query: `event_types=void_invoice,void_remainder`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInvoiceEventsResponse](maxio_advanced_billing/models/list_invoice_events_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_invoices(*, start_date: str | None = None, end_date: str | None = None, status: InvoiceStatusOrStr | None = None, subscription_id: int | None = None, subscription_group_uid: str | None = None, consolidation_level: str | None = None, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = Direction.DESC, line_items: bool | None = False, discounts: bool | None = False, taxes: bool | None = False, credits_: bool | None = False, payments: bool | None = False, custom_fields: bool | None = False, refunds: bool | None = False, date_field: InvoiceDateFieldOrStr | None = InvoiceDateField.DUE_DATE, start_datetime: str | None = None, end_datetime: str | None = None, customer_ids: list[int] | None = None, number: list[str] | None = None, product_ids: list[int] | None = None, sort: InvoiceSortFieldOrStr | None = InvoiceSortField.NUMBER, request_options: RequestOptionsOrDict | None = None) -> ListInvoicesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists invoices for a site. By default, invoices returned on the index will only include totals, not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, `custom_fields`, or `refunds`. To include breakdowns, pass the specific field as a key in the query with a value set to `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.list_invoices(
        page=1,
        per_page=50,
        date_field=InvoiceDateField.ISSUE_DATE,
        customer_ids=[1, 2, 3],
        number=["1234", "1235"],
        product_ids=[23, 34],
        sort=InvoiceSortField.TOTAL_AMOUNT,
    )
    # TODO: Handle 'response' of type ListInvoicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invoices.list_invoices(
        page=1,
        per_page=50,
        date_field=InvoiceDateField.ISSUE_DATE,
        customer_ids=[1, 2, 3],
        number=["1234", "1235"],
        product_ids=[23, 34],
        sort=InvoiceSortField.TOTAL_AMOUNT,
    )
    # TODO: Handle 'response' of type ListInvoicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[InvoiceStatusOrStr](maxio_advanced_billing/models/enums/invoice_status.py) \| None</code> | The current status of the invoice.  Allowed Values: draft, open, paid, pending, voided<br>**Default**: <code>None</code> |
| <code>subscription_id</code> | <code>int \| None</code> | The subscription's ID.<br>**Default**: <code>None</code> |
| <code>subscription_group_uid</code> | <code>str \| None</code> | The UID of the subscription group you want to fetch consolidated invoices for. This will return a paginated list of consolidated invoices for the specified group.<br>**Default**: <code>None</code> |
| <code>consolidation_level</code> | <code>str \| None</code> | The consolidation level of the invoice. Allowed Values: none, parent, child or comma-separated lists of thereof, e.g. none,parent.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | The sort direction of the returned invoices.<br>**Default**: <code>Direction.DESC</code> |
| <code>line_items</code> | <code>bool \| None</code> | Include line items data.<br>**Default**: <code>False</code> |
| <code>discounts</code> | <code>bool \| None</code> | Include discounts data.<br>**Default**: <code>False</code> |
| <code>taxes</code> | <code>bool \| None</code> | Include taxes data.<br>**Default**: <code>False</code> |
| <code>credits_</code> | <code>bool \| None</code> | Include credits data.<br>**Default**: <code>False</code> |
| <code>payments</code> | <code>bool \| None</code> | Include payments data.<br>**Default**: <code>False</code> |
| <code>custom_fields</code> | <code>bool \| None</code> | Include custom fields data.<br>**Default**: <code>False</code> |
| <code>refunds</code> | <code>bool \| None</code> | Include refunds data.<br>**Default**: <code>False</code> |
| <code>date_field</code> | <code>[InvoiceDateFieldOrStr](maxio_advanced_billing/models/enums/invoice_date_field.py) \| None</code> | The type of filter you would like to apply to your search. Use in query `date_field=issue_date`.<br>**Default**: <code>InvoiceDateField.DUE_DATE</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns invoices with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. Allowed to be used only along with date_field set to created_at or updated_at.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns invoices with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. Allowed to be used only along with date_field set to created_at or updated_at.<br>**Default**: <code>None</code> |
| <code>customer_ids</code> | <code>list&#91;int&#93; \| None</code> | Allows fetching invoices with matching customer id based on provided values. Use in query `customer_ids=1,2,3`.<br>**Default**: <code>None</code> |
| <code>number</code> | <code>list&#91;str&#93; \| None</code> | Allows fetching invoices with matching invoice number based on provided values. Use in query `number=1234,1235`.<br>**Default**: <code>None</code> |
| <code>product_ids</code> | <code>list&#91;int&#93; \| None</code> | Allows fetching invoices with matching line items product ids based on provided values. Use in query `product_ids=23,34`.<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[InvoiceSortFieldOrStr](maxio_advanced_billing/models/enums/invoice_sort_field.py) \| None</code> | Allows specification of the order of the returned list. Use in query `sort=total_amount`.<br>**Default**: <code>InvoiceSortField.NUMBER</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInvoicesResponse](maxio_advanced_billing/models/list_invoices_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_customer_information_changes(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> CustomerChangesPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Previews the effect of customer information changes on an open invoice. Customer information may change after an invoice is issued, which may lead to a mismatch between customer information that is present on an open invoice and actual customer information. This endpoint allows you to preview these differences, if any.

The endpoint doesn't accept a request body. Customer information differences are calculated on the application side.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.preview_customer_information_changes("some example string")
    # TODO: Handle 'response' of type CustomerChangesPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewCustomerInformationChangesErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.preview_customer_information_changes("some example string")
    # TODO: Handle 'response' of type CustomerChangesPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewCustomerInformationChangesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CustomerChangesPreviewResponse](maxio_advanced_billing/models/customer_changes_preview_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PreviewCustomerInformationChangesErrorBody](maxio_advanced_billing/errors/preview_customer_information_changes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_credit_note(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> CreditNote</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the details for a credit note.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.read_credit_note("some example string")
    # TODO: Handle 'response' of type CreditNote
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invoices.read_credit_note("some example string")
    # TODO: Handle 'response' of type CreditNote
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier of the credit note |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreditNote](maxio_advanced_billing/models/credit_note.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_invoice(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the details for an invoice.

## PDF Invoice retrieval

Individual PDF Invoices can be retrieved by using the "Accept" header application/pdf or appending .pdf as the format portion of the URL:
``curl -u <api_key>:x -H
Accept:application/pdf -H
https://acme.chargify.com/invoices/inv_8gd8tdhtd3hgr.pdf > output_file.pdf
URL: `https://<subdomain>.chargify.com/invoices/<uid>.<format>`
Method: GET
Required parameters: `uid`
Response: A single Invoice.
``

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.read_invoice("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invoices.read_invoice("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def record_payment_for_invoice(uid: str, *, body: CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Applies a payment of a given type against a specific invoice. If you would like to apply a payment across multiple invoices, you can use the [Record Payment for Multiple Invoices]($e/Invoices/recordPaymentForMultipleInvoices) endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.record_payment_for_invoice(
        "some example string",
        body=CreateInvoicePaymentRequest(
            payment=CreateInvoicePayment(
                amount=124.33, memo="for John Smith", method=InvoicePaymentMethodType.CHECK, details="#0102"
            ),
        ),
    )
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecordPaymentForInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.record_payment_for_invoice(
        "some example string",
        body=CreateInvoicePaymentRequest(
            payment=CreateInvoicePayment(
                amount=124.33, memo="for John Smith", method=InvoicePaymentMethodType.CHECK, details="#0102"
            ),
        ),
    )
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecordPaymentForInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>body</code> | <code>[CreateInvoicePaymentRequest](maxio_advanced_billing/models/create_invoice_payment_request.py) \| [CreateInvoicePaymentRequestDict](maxio_advanced_billing/models/create_invoice_payment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RecordPaymentForInvoiceErrorBody](maxio_advanced_billing/errors/record_payment_for_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def record_payment_for_multiple_invoices(*, body: CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> MultiInvoicePaymentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records an external payment against multiple invoices.

To apply a payment to multiple invoices, at minimum, specify the `amount` and `applications` (i.e., `invoice_uid` and `amount`) details.

Note that the invoice payment amounts must be greater than 0. Total amount must be greater or equal to invoices payment amount sum.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.record_payment_for_multiple_invoices(
        body=CreateMultiInvoicePaymentRequest(
            payment=CreateMultiInvoicePayment(
                memo="to pay the bills",
                details="check number 8675309",
                method=InvoicePaymentMethodType.CHECK,
                amount="100.00",
                applications=[
                    CreateInvoicePaymentApplication(invoice_uid="inv_8gk5bwkct3gqt", amount="50.00"),
                    CreateInvoicePaymentApplication(invoice_uid="inv_7bc6bwkct3lyt", amount="50.00"),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type MultiInvoicePaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecordPaymentForMultipleInvoicesErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.record_payment_for_multiple_invoices(
        body=CreateMultiInvoicePaymentRequest(
            payment=CreateMultiInvoicePayment(
                memo="to pay the bills",
                details="check number 8675309",
                method=InvoicePaymentMethodType.CHECK,
                amount="100.00",
                applications=[
                    CreateInvoicePaymentApplication(invoice_uid="inv_8gk5bwkct3gqt", amount="50.00"),
                    CreateInvoicePaymentApplication(invoice_uid="inv_7bc6bwkct3lyt", amount="50.00"),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type MultiInvoicePaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecordPaymentForMultipleInvoicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateMultiInvoicePaymentRequest](maxio_advanced_billing/models/create_multi_invoice_payment_request.py) \| [CreateMultiInvoicePaymentRequestDict](maxio_advanced_billing/models/create_multi_invoice_payment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MultiInvoicePaymentResponse](maxio_advanced_billing/models/multi_invoice_payment_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RecordPaymentForMultipleInvoicesErrorBody](maxio_advanced_billing/errors/record_payment_for_multiple_invoices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def record_payment_for_subscription(subscription_id: int, *, body: RecordPaymentRequest | RecordPaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> RecordPaymentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records an external payment made against a subscription that will pay partially or in full one or more invoices.

Payment will be applied starting with the oldest open invoice and then next oldest, and so on until the amount of the payment is fully consumed.

Excess payment will result in the creation of a prepayment on the Invoice Account.

Only ungrouped or primary subscriptions may be paid using the "bulk" payment request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.record_payment_for_subscription(
        1,
        body=RecordPaymentRequest(
            payment=CreatePayment(
                amount="10.0",
                memo="to pay the bills",
                payment_details="check number 8675309",
                payment_method=InvoicePaymentMethodType.CHECK,
            ),
        ),
    )
    # TODO: Handle 'response' of type RecordPaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecordPaymentForSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.record_payment_for_subscription(
        1,
        body=RecordPaymentRequest(
            payment=CreatePayment(
                amount="10.0",
                memo="to pay the bills",
                payment_details="check number 8675309",
                payment_method=InvoicePaymentMethodType.CHECK,
            ),
        ),
    )
    # TODO: Handle 'response' of type RecordPaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RecordPaymentForSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[RecordPaymentRequest](maxio_advanced_billing/models/record_payment_request.py) \| [RecordPaymentRequestDict](maxio_advanced_billing/models/record_payment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RecordPaymentResponse](maxio_advanced_billing/models/record_payment_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RecordPaymentForSubscriptionErrorBody](maxio_advanced_billing/errors/record_payment_for_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refund_invoice(uid: str, *, body: RefundInvoiceRequest | RefundInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Refunds an invoice, segment, or consolidated invoice.

## Partial Refund for Consolidated Invoice

A refund less than the total of a consolidated invoice will be split across its segments.

For a $50.00 refund on a $100.00 consolidated invoice with one $60.00 segment and one $40.00 segment, the refunded amount will be applied as 50% of each ($30.00 and $20.00, respectively).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.refund_invoice(
        "some example string",
        body=RefundInvoiceRequest(
            refund=RefundInvoice(
                amount="100.00",
                memo="Refund for Basic Plan renewal",
                payment_id=12345,
                external=False,
                apply_credit=False,
                void_invoice=True,
            ),
        ),
    )
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.refund_invoice(
        "some example string",
        body=RefundInvoiceRequest(
            refund=RefundInvoice(
                amount="100.00",
                memo="Refund for Basic Plan renewal",
                payment_id=12345,
                external=False,
                apply_credit=False,
                void_invoice=True,
            ),
        ),
    )
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>body</code> | <code>[RefundInvoiceRequest](maxio_advanced_billing/models/refund_invoice_request.py) \| [RefundInvoiceRequestDict](maxio_advanced_billing/models/refund_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RefundInvoiceErrorBody](maxio_advanced_billing/errors/refund_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reopen_invoice(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reopens any invoice with the "canceled" status. Invoices enter "canceled" status if they were open at the time the subscription was canceled (whether through dunning or an intentional cancellation).

Invoices with "canceled" status are no longer considered to be due. Once reopened, they are considered due for payment. Payment may then be captured in one of the following ways:

- Reactivating the subscription, which will capture all open invoices (See note below about automatic reopening of invoices.)
- Recording a payment directly against the invoice

A note about reactivations: any canceled invoices from the most recent active period are automatically opened as a part of the reactivation process. Reactivating via this endpoint prior to reactivation is only necessary when you wish to capture older invoices from previous periods during the reactivation.

### Reopening Consolidated Invoices

When reopening a consolidated invoice, all of its canceled segments will also be reopened.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.reopen_invoice("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReopenInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.reopen_invoice("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReopenInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReopenInvoiceErrorBody](maxio_advanced_billing/errors/reopen_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>Any \| None</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_invoice(uid: str, *, body: SendInvoiceRequest | SendInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends an invoice to the customer via email. This endpoint supports the delivery of both ad-hoc and automatically generated invoices. Additionally, this endpoint supports email delivery to direct recipients, carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

**File Attachments**: You can attach files to invoice emails using `attachment_urls[]` parameter by providing URLs to the files you want to attach. When using attachments, the request must use `multipart/form-data` content type. Max 10 files, 10MB per file.

If no recipient email addresses are specified in the request, then the subscription's default email configuration will be used. For example, if `recipient_emails` is left blank, then the invoice will be delivered to the subscription's customer email address.

On success, a 204 no-content response will be returned. The response does not indicate that email(s) have been delivered, but instead indicates that emails have been successfully queued for delivery. If _any_ invalid or malformed email address is found in the request body, the entire request will be rejected and a 422 response will be returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.invoices.send_invoice(
        "some example string",
        body=SendInvoiceRequest(
            recipient_emails=["user0@example.com"],
            cc_recipient_emails=["user1@example.com"],
            bcc_recipient_emails=["user2@example.com"],
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendInvoiceErrorBody
```

**Async**

```python
try:
    await async_client.invoices.send_invoice(
        "some example string",
        body=SendInvoiceRequest(
            recipient_emails=["user0@example.com"],
            cc_recipient_emails=["user1@example.com"],
            bcc_recipient_emails=["user2@example.com"],
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>body</code> | <code>[SendInvoiceRequest](maxio_advanced_billing/models/send_invoice_request.py) \| [SendInvoiceRequestDict](maxio_advanced_billing/models/send_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[SendInvoiceErrorBody](maxio_advanced_billing/errors/send_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_customer_information(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates customer information on an open invoice and returns the updated invoice. If you would like to preview changes that will be applied, use the `/invoices/{uid}/customer_information/preview.json` endpoint first.

The endpoint doesn't accept a request body. Customer information differences are calculated on the application side.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.update_customer_information("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCustomerInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.update_customer_information("some example string")
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCustomerInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateCustomerInformationErrorBody](maxio_advanced_billing/errors/update_customer_information_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_invoice(subscription_id: int, uid: str, *, body: UpdateInvoiceRequest | UpdateInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> InvoiceResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an ad hoc invoice while it is in the `draft` state.

**Important: only invoices with the `adhoc` role and `draft` status can be updated.** Any other invoice — issued, or with a different role (e.g. `renewal`, `signup`) — cannot be updated through this endpoint and the request returns a `422` error. If the invoice does not belong to the provided subscription, a `404` error is returned.

Only the attributes submitted in the request are changed — omitted attributes keep their current values.

### Line Items

The `line_items` array describes changes to the invoice's line items. Line items not referenced in the array remain unchanged.

#### Adding a line item

A line item without a `uid` is added to the invoice. The same line item types and options as on invoice creation are supported (custom items, `product_id`, `component_id`, price points, period date ranges, taxes).

#### Updating a line item

A line item with the `uid` of an existing line item updates that line item with the submitted attributes. Amounts and taxes are recalculated.

#### Removing a line item

A line item with a `uid` and `"_destroy": true` is removed from the invoice. Other line items remain unchanged.

Referencing a `uid` which does not exist on the invoice returns a `422` error.

### Coupons

When the `coupons` key is present, the submitted coupons replace all discounts currently applied to the invoice. Send an empty array to remove all discounts. Coupon options are the same as on invoice creation.

### Invoice Options

#### Issue Date and Net Terms

The `issue_date` parameter can be sent to change the invoice's issue date. Only today or dates in the past are accepted. The date is interpreted and validated in your site's time zone, using the `YYYY-MM-DD` format. The `net_terms` parameter indicates the number of days after the issue date on which the invoice is due. The due date is recalculated whenever the issue date or net terms change.

#### Addresses

The seller, shipping and billing addresses can be sent to replace the addresses on the invoice. Each address requires to send a `first_name` at a minimum in order to work. Taxes are recalculated after an address change.

#### Memo and Payment Instructions

A custom memo can be sent with the `memo` parameter. Likewise, custom payment instructions can be sent with the `payment_instructions` parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.update_invoice(
        1, "some example string", body=UpdateInvoiceRequest(invoice=UpdateInvoice(net_terms=30, memo="Updated memo"))
    )
    # TODO: Handle 'response' of type InvoiceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.update_invoice(
        1, "some example string", body=UpdateInvoiceRequest(invoice=UpdateInvoice(net_terms=30, memo="Updated memo"))
    )
    # TODO: Handle 'response' of type InvoiceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>body</code> | <code>[UpdateInvoiceRequest](maxio_advanced_billing/models/update_invoice_request.py) \| [UpdateInvoiceRequestDict](maxio_advanced_billing/models/update_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InvoiceResponse](maxio_advanced_billing/models/invoice_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateInvoiceErrorBody](maxio_advanced_billing/errors/update_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def void_invoice(uid: str, *, body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> Invoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Voids any invoice with the "open" or "canceled" status.  It will also allow voiding of an invoice with the "pending" status if it is not a consolidated invoice.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invoices.void_invoice(
        "some example string", body=VoidInvoiceRequest(void=VoidInvoice(reason="Duplicate invoice"))
    )
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.invoices.void_invoice(
        "some example string", body=VoidInvoiceRequest(void=VoidInvoice(reason="Duplicate invoice"))
    )
    # TODO: Handle 'response' of type Invoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The unique identifier for the invoice, this does not refer to the public facing invoice number. |
| <code>body</code> | <code>[VoidInvoiceRequest](maxio_advanced_billing/models/void_invoice_request.py) \| [VoidInvoiceRequestDict](maxio_advanced_billing/models/void_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Invoice](maxio_advanced_billing/models/invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[VoidInvoiceErrorBody](maxio_advanced_billing/errors/void_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>Any \| None</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Offers

> Source: [Offers](maxio_advanced_billing/apis/offers.py)

<details>
<summary><code>def archive_offer(offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives an existing offer. Please provide an `offer_id` in order to archive the correct item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.offers.archive_offer(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.offers.archive_offer(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>offer_id</code> | <code>int</code> | The Chargify id of the offer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_offer(*, body: CreateOfferRequest | CreateOfferRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> OfferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an offer within your site.

Offers allow you to package complicated combinations of products, components and coupons into a convenient package which can then be subscribed to just like products.

Once an offer is defined it can be used as an alternative to the product when creating subscriptions.

For more information, see [Offers](https://maxio.zendesk.com/hc/en-us/articles/24261295098637-Offers-Overview) in the product documentation.

## Using a Product Price Point

You can optionally pass in a `product_price_point_id` that corresponds with the `product_id` and the offer will use that price point. If a `product_price_point_id` is not passed in, the product's default price point will be used.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.offers.create_offer(
        body=CreateOfferRequest(
            offer=CreateOffer(
                name="Solo",
                handle="han_shot_first",
                description="A Star Wars Story",
                product_id=31,
                product_price_point_id=102,
                components=[CreateOfferComponent(component_id=24, starting_quantity=1)],
                coupons=["DEF456"],
            ),
        ),
    )
    # TODO: Handle 'response' of type OfferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOfferErrorBody
```

**Async**

```python
try:
    response = await async_client.offers.create_offer(
        body=CreateOfferRequest(
            offer=CreateOffer(
                name="Solo",
                handle="han_shot_first",
                description="A Star Wars Story",
                product_id=31,
                product_price_point_id=102,
                components=[CreateOfferComponent(component_id=24, starting_quantity=1)],
                coupons=["DEF456"],
            ),
        ),
    )
    # TODO: Handle 'response' of type OfferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateOfferErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateOfferRequest](maxio_advanced_billing/models/create_offer_request.py) \| [CreateOfferRequestDict](maxio_advanced_billing/models/create_offer_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OfferResponse](maxio_advanced_billing/models/offer_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateOfferErrorBody](maxio_advanced_billing/errors/create_offer_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_offers(*, page: int | None = 1, per_page: int | None = 20, include_archived: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ListOffersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists offers for a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.offers.list_offers(page=1, per_page=50, include_archived=True)
    # TODO: Handle 'response' of type ListOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListOffersErrorBody
```

**Async**

```python
try:
    response = await async_client.offers.list_offers(page=1, per_page=50, include_archived=True)
    # TODO: Handle 'response' of type ListOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListOffersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>include_archived</code> | <code>bool \| None</code> | Include archived products. Use in query: `include_archived=true`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListOffersResponse](maxio_advanced_billing/models/list_offers_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListOffersErrorBody](maxio_advanced_billing/errors/list_offers_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_offer(offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> OfferResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a specific offer's attributes. This is different from listing all offers for a site, as it requires an `offer_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.offers.read_offer(1)
    # TODO: Handle 'response' of type OfferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.offers.read_offer(1)
    # TODO: Handle 'response' of type OfferResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>offer_id</code> | <code>int</code> | The Chargify id of the offer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OfferResponse](maxio_advanced_billing/models/offer_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unarchive_offer(offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unarchives a previously archived offer. Please provide an `offer_id` in order to unarchive the correct item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.offers.unarchive_offer(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.offers.unarchive_offer(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>offer_id</code> | <code>int</code> | The Chargify id of the offer |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## PaymentProfiles

> Source: [PaymentProfiles](maxio_advanced_billing/apis/payment_profiles.py)

<details>
<summary><code>def change_subscription_default_payment_profile(subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes the default payment profile on the subscription to the existing payment profile with the specified ID.

You must elect to change the existing payment profile to a new payment profile ID in order to receive a satisfactory response from this endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.change_subscription_default_payment_profile(1, 1)
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeSubscriptionDefaultPaymentProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.payment_profiles.change_subscription_default_payment_profile(1, 1)
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeSubscriptionDefaultPaymentProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>payment_profile_id</code> | <code>int</code> | The Chargify id of the payment profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentProfileResponse](maxio_advanced_billing/models/payment_profile_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ChangeSubscriptionDefaultPaymentProfileErrorBody](maxio_advanced_billing/errors/change_subscription_default_payment_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_subscription_group_default_payment_profile(uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes the default payment profile on the subscription group to the existing payment profile with the specified ID.

You must elect to change the existing payment profile to a new payment profile ID in order to receive a satisfactory response from this endpoint.

The new payment profile must belong to the subscription group's customer, otherwise you will receive an error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.change_subscription_group_default_payment_profile("some example string", 1)
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeSubscriptionGroupDefaultPaymentProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.payment_profiles.change_subscription_group_default_payment_profile(
        "some example string", 1
    )
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeSubscriptionGroupDefaultPaymentProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>payment_profile_id</code> | <code>int</code> | The Chargify id of the payment profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentProfileResponse](maxio_advanced_billing/models/payment_profile_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ChangeSubscriptionGroupDefaultPaymentProfileErrorBody](maxio_advanced_billing/errors/change_subscription_group_default_payment_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_payment_profile(*, body: CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a payment profile for a customer.

When you create a new payment profile for a customer via the API, it does not automatically make the profile current for any of the customer’s subscriptions. To use the payment profile as the default, you must set it explicitly for the subscription or subscription group.

Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of common scenarios for creating payment profiles. 

Do not use real card information for testing. See the Sites articles that cover [testing your site setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0) for more details on testing in your sandbox.

Note that collecting and sending raw card details in production requires [PCI compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0) on your end. If your business is not PCI compliant, use [Maxio.js (formerly Chargify.js)](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0) to collect credit card or bank account information.

See the following articles to learn more about subscriptions and payments:

+ [Subscriber Payment Details](https://maxio.zendesk.com/hc/en-us/articles/24251599929613-Subscription-Summary-Payment-Details-Tab)
+ [Self Service Pages](https://maxio.zendesk.com/hc/en-us/articles/24261425318541-Self-Service-Pages) (Allows credit card updates by Subscriber)
+ [Public Signup Pages payment settings](https://maxio.zendesk.com/hc/en-us/articles/24261368332557-Individual-Page-Settings)
+ [Taxes](https://developers.chargify.com/docs/developer-docs/d2e9e34db740e-signups#taxes)
+ [Maxio.js (formerly Chargify.js)](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview)
    + [Maxio.js with GoCardless - minimal example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQZKCER8CFK40MR6XJ)
    + [Maxio.js with GoCardless - full example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QR09JVHWW0MCA7HVJV)
    + [Maxio.js with Stripe Direct Debit - minimal example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQFKKN8Z7B7DZ9AJS5)
    + [Maxio.js with Stripe Direct Debit - full example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QRECQQ4ECS3ZA55GY7)
    + [Maxio.js with Stripe BECS Direct Debit - minimal example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-gateway)
    + [Maxio.js with Stripe BECS Direct Debit - full example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#full-example-with-sepa-direct-debit-stripe-gateway)
+ [Full documentation on GoCardless](https://maxio.zendesk.com/hc/en-us/articles/24176159136909-GoCardless)
+ [Full documentation on Stripe SEPA Direct Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit)
+ [Full documentation on Stripe BECS Direct Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit)
+ [Full documentation on Stripe BACS Direct Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit)

## 3D Secure (3DS) Authentication post-authentication flow

When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will direct the customer through 3DS Authentication. 

See the [3D Secure Post-Authentication Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow) article in the product documentation to learn how to manage the redirect flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.create_payment_profile(
        body=CreatePaymentProfileRequest(
            payment_profile=CreatePaymentProfile(chargify_token="tok_w68qcpnftyv53jk33jv6wk3w", customer_id=1036)
        ),
    )
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePaymentProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.payment_profiles.create_payment_profile(
        body=CreatePaymentProfileRequest(
            payment_profile=CreatePaymentProfile(chargify_token="tok_w68qcpnftyv53jk33jv6wk3w", customer_id=1036)
        ),
    )
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePaymentProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreatePaymentProfileRequest](maxio_advanced_billing/models/create_payment_profile_request.py) \| [CreatePaymentProfileRequestDict](maxio_advanced_billing/models/create_payment_profile_request.py) \| None</code> | When following the IBAN or the Local Bank details examples, a customer, bank account and mandate will be created in your current vault. If the customer, bank account, and mandate already exist in your vault, follow the Import example to link the payment profile into Advanced Billing.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentProfileResponse](maxio_advanced_billing/models/payment_profile_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreatePaymentProfileErrorBody](maxio_advanced_billing/errors/create_payment_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription_group_payment_profile(uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a Payment Profile belonging to a Subscription Group.

**Note**: If the Payment Profile belongs to multiple Subscription Groups and/or Subscriptions, it will be removed from all of them.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.payment_profiles.delete_subscription_group_payment_profile("some example string", 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.payment_profiles.delete_subscription_group_payment_profile("some example string", 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>payment_profile_id</code> | <code>int</code> | The Chargify id of the payment profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscriptions_payment_profile(subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a payment profile belonging to the customer on the subscription.

If the customer has multiple subscriptions, the payment profile is removed from all of them.

If you delete the default payment profile for a subscription, you need to specify another payment profile to be the default through the API, or either prompt the user to enter a card in the billing portal or on the self-service page, or visit the Payment Details tab on the subscription in the Admin UI and use the “Add New Credit Card” or “Make Active Payment Method” link, (depending on whether there are other cards present).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.payment_profiles.delete_subscriptions_payment_profile(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.payment_profiles.delete_subscriptions_payment_profile(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>payment_profile_id</code> | <code>int</code> | The Chargify id of the payment profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_unused_payment_profile(payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an unused payment profile.

If the payment profile is in use by one or more subscriptions or groups, an error message is returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.payment_profiles.delete_unused_payment_profile(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteUnusedPaymentProfileErrorBody
```

**Async**

```python
try:
    await async_client.payment_profiles.delete_unused_payment_profile(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteUnusedPaymentProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payment_profile_id</code> | <code>int</code> | The Chargify id of the payment profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteUnusedPaymentProfileErrorBody](maxio_advanced_billing/errors/delete_unused_payment_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_payment_profiles(*, page: int | None = 1, per_page: int | None = 20, customer_id: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[PaymentProfileResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all active payment profiles for a site, or for one customer within a site. If no payment profiles are found, this endpoint returns an empty array.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.list_payment_profiles(page=1, per_page=50)
    # TODO: Handle 'response' of type list[PaymentProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_profiles.list_payment_profiles(page=1, per_page=50)
    # TODO: Handle 'response' of type list[PaymentProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>customer_id</code> | <code>int \| None</code> | The ID of the customer for which you wish to list payment profiles<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[PaymentProfileResponse](maxio_advanced_billing/models/payment_profile_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_one_time_token(chargify_token: str, *, request_options: RequestOptionsOrDict | None = None) -> GetOneTimeTokenRequest</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the one-time token data, including credit card or ACH details, associated with the provided token ID. One Time Tokens aka Advanced Billing Tokens house the credit card or ACH (Authorize.Net or Stripe only) data for a customer.

You can use One Time Tokens while creating a subscription or payment profile instead of passing all bank account or credit card data directly to a given API endpoint.

To obtain a One Time Token you have to use [Chargify.js](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.read_one_time_token("some example string")
    # TODO: Handle 'response' of type GetOneTimeTokenRequest
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadOneTimeTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.payment_profiles.read_one_time_token("some example string")
    # TODO: Handle 'response' of type GetOneTimeTokenRequest
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadOneTimeTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>chargify_token</code> | <code>str</code> | Advanced Billing Token |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOneTimeTokenRequest](maxio_advanced_billing/models/get_one_time_token_request.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadOneTimeTokenErrorBody](maxio_advanced_billing/errors/read_one_time_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_payment_profile(payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a payment profile identified by its unique ID.

Note that a different JSON object will be returned if the card method on file is a bank account.

### Response for Bank Account

Example response for Bank Account:

``
{
  "payment_profile": {
    "id": 10089892,
    "first_name": "Chester",
    "last_name": "Tester",
    "created_at": "2025-01-01T00:00:00-05:00",
    "updated_at": "2025-01-01T00:00:00-05:00",
    "customer_id": 14543792,
    "current_vault": "bogus",
    "vault_token": "0011223344",
    "billing_address": "456 Juniper Court",
    "billing_city": "Boulder",
    "billing_state": "CO",
    "billing_zip": "80302",
    "billing_country": "US",
    "customer_vault_token": null,
    "billing_address_2": "",
    "bank_name": "Bank of Kansas City",
    "masked_bank_routing_number": "XXXX6789",
    "masked_bank_account_number": "XXXX3344",
    "bank_account_type": "checking",
    "bank_account_holder_type": "personal",
    "payment_type": "bank_account",
    "site_gateway_setting_id": 1,
    "gateway_handle": null
  }
}
``

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.read_payment_profile(1)
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadPaymentProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.payment_profiles.read_payment_profile(1)
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadPaymentProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payment_profile_id</code> | <code>int</code> | The Chargify id of the payment profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentProfileResponse](maxio_advanced_billing/models/payment_profile_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadPaymentProfileErrorBody](maxio_advanced_billing/errors/read_payment_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_request_update_payment_email(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends a "request payment update" email to the customer associated with the subscription.

If you attempt to send a "request payment update" email more than five times within a 30-minute period, you will receive a `422` response with an error message in the body. This error message will indicate that the request has been rejected due to excessive attempts, and will provide instructions on how to resubmit the request.

Additionally, if you attempt to send a "request payment update" email for a subscription that does not exist, you will receive a `404` error response. This error message will indicate that the subscription could not be found, and will provide instructions on how to correct the error and resubmit the request.

These error responses are designed to prevent excessive or invalid requests, and to provide clear and helpful information to users who encounter errors during the request process.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.payment_profiles.send_request_update_payment_email(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendRequestUpdatePaymentEmailErrorBody
```

**Async**

```python
try:
    await async_client.payment_profiles.send_request_update_payment_email(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendRequestUpdatePaymentEmailErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[SendRequestUpdatePaymentEmailErrorBody](maxio_advanced_billing/errors/send_request_update_payment_email_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_payment_profile(payment_profile_id: int, *, body: UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PaymentProfileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a payment profile.

## Partial Card Updates

In the event that you are using the Authorize.net, Stripe, Cybersource, Forte or Braintree Blue payment gateways, you can update just the billing and contact information for a payment method. Note the lack of credit-card related data contained in the JSON payload.

In this case, the following JSON is acceptable:

``
{
  "payment_profile": {
    "first_name": "Kelly",
    "last_name": "Test",
    "billing_address": "789 Juniper Court",
    "billing_city": "Boulder",
    "billing_state": "CO",
    "billing_zip": "80302",
    "billing_country": "US",
    "billing_address_2": null
  }
}
``

The result will be that you have updated the billing information for the card, yet retained the original card number data.

## Specific notes on updating payment profiles

- Merchants with **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe** as their payment gateway can update their Customer’s credit cards without passing in the full credit card number and CVV.

- If you are using **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe**, Advanced Billing will ignore the credit card number and CVV when processing an update via the API, and attempt a partial update instead. If you wish to change the card number on a payment profile, you will need to create a new payment profile for the given customer.

- A Payment Profile cannot be updated with the attributes of another type of Payment Profile. For example, if the payment profile you are attempting to update is a credit card, you cannot pass in bank account attributes (like `bank_account_number`), and vice versa.

- Updating a payment profile directly will not trigger an attempt to capture a past-due balance. If this is the intent, update the card details via the Subscription instead.

- If you are using Authorize.net or Stripe, you may elect to manually trigger a retry for a past due subscription after a partial update.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.update_payment_profile(
        1,
        body=UpdatePaymentProfileRequest(
            payment_profile=UpdatePaymentProfile(
                first_name="Graham",
                last_name="Test",
                billing_address="456 Juniper Court",
                billing_city="Boulder",
                billing_state="CO",
                billing_zip="80302",
                billing_country="US",
                billing_address_2="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdatePaymentProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.payment_profiles.update_payment_profile(
        1,
        body=UpdatePaymentProfileRequest(
            payment_profile=UpdatePaymentProfile(
                first_name="Graham",
                last_name="Test",
                billing_address="456 Juniper Court",
                billing_city="Boulder",
                billing_state="CO",
                billing_zip="80302",
                billing_country="US",
                billing_address_2="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type PaymentProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdatePaymentProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payment_profile_id</code> | <code>int</code> | The Chargify id of the payment profile |
| <code>body</code> | <code>[UpdatePaymentProfileRequest](maxio_advanced_billing/models/update_payment_profile_request.py) \| [UpdatePaymentProfileRequestDict](maxio_advanced_billing/models/update_payment_profile_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentProfileResponse](maxio_advanced_billing/models/payment_profile_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdatePaymentProfileErrorBody](maxio_advanced_billing/errors/update_payment_profile_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorStringMapResponse1](maxio_advanced_billing/models/error_string_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def verify_bank_account(bank_account_id: int, *, body: BankAccountVerificationRequest | BankAccountVerificationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> BankAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Verifies a bank account. Submit the two small deposit amounts the customer received in their bank account to verify the bank account. (Stripe only)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_profiles.verify_bank_account(
        1,
        body=BankAccountVerificationRequest(
            bank_account_verification=BankAccountVerification(deposit_1_in_cents=32, deposit_2_in_cents=45)
        ),
    )
    # TODO: Handle 'response' of type BankAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VerifyBankAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.payment_profiles.verify_bank_account(
        1,
        body=BankAccountVerificationRequest(
            bank_account_verification=BankAccountVerification(deposit_1_in_cents=32, deposit_2_in_cents=45)
        ),
    )
    # TODO: Handle 'response' of type BankAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VerifyBankAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>bank_account_id</code> | <code>int</code> | Identifier of the bank account in the system. |
| <code>body</code> | <code>[BankAccountVerificationRequest](maxio_advanced_billing/models/bank_account_verification_request.py) \| [BankAccountVerificationRequestDict](maxio_advanced_billing/models/bank_account_verification_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankAccountResponse](maxio_advanced_billing/models/bank_account_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[VerifyBankAccountErrorBody](maxio_advanced_billing/errors/verify_bank_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ProductFamilies

> Source: [ProductFamilies](maxio_advanced_billing/apis/product_families.py)

<details>
<summary><code>def create_product_family(*, body: CreateProductFamilyRequest | CreateProductFamilyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProductFamilyResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Product Family within your site. Create a Product Family to act as a container for your products, components, and coupons.

Full documentation on how Product Families operate within the Advanced Billing UI can be located [here](https://maxio.zendesk.com/hc/en-us/articles/24261098936205-Product-Families).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_families.create_product_family(
        body=CreateProductFamilyRequest(
            product_family=CreateProductFamily(
                name="Acme Projects", description="Amazing project management tool", surcharging=False
            ),
        ),
    )
    # TODO: Handle 'response' of type ProductFamilyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductFamilyErrorBody
```

**Async**

```python
try:
    response = await async_client.product_families.create_product_family(
        body=CreateProductFamilyRequest(
            product_family=CreateProductFamily(
                name="Acme Projects", description="Amazing project management tool", surcharging=False
            ),
        ),
    )
    # TODO: Handle 'response' of type ProductFamilyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductFamilyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateProductFamilyRequest](maxio_advanced_billing/models/create_product_family_request.py) \| [CreateProductFamilyRequestDict](maxio_advanced_billing/models/create_product_family_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductFamilyResponse](maxio_advanced_billing/models/product_family_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateProductFamilyErrorBody](maxio_advanced_billing/errors/create_product_family_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_product_families(*, date_field: BasicDateFieldOrStr | None = None, start_date: Date | None = None, end_date: Date | None = None, start_datetime: RFC3339DateTime | None = None, end_datetime: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ProductFamilyResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists Product Families for a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_families.list_product_families(date_field=BasicDateField.UPDATED_AT)
    # TODO: Handle 'response' of type list[ProductFamilyResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.product_families.list_product_families(date_field=BasicDateField.UPDATED_AT)
    # TODO: Handle 'response' of type list[ProductFamilyResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>date_field</code> | <code>[BasicDateFieldOrStr](maxio_advanced_billing/models/enums/basic_date_field.py) \| None</code> | The type of filter you would like to apply to your search.<br>Use in query: `date_field=created_at`.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>Date \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>Date \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>RFC3339DateTime \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>RFC3339DateTime \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ProductFamilyResponse](maxio_advanced_billing/models/product_family_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_products_for_product_family(product_family_id: str, *, page: int | None = 1, per_page: int | None = 20, date_field: BasicDateFieldOrStr | None = None, filter_: ListProductsFilter | ListProductsFilterDict | None = None, start_date: Date | None = None, end_date: Date | None = None, start_datetime: RFC3339DateTime | None = None, end_datetime: RFC3339DateTime | None = None, include_archived: bool | None = None, include: ListProductsIncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> list[ProductResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of Products belonging to a Product Family.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_families.list_products_for_product_family(
        "some example string",
        page=1,
        per_page=50,
        date_field=BasicDateField.UPDATED_AT,
        include=ListProductsInclude.PREPAID_PRODUCT_PRICE_POINT,
    )
    # TODO: Handle 'response' of type list[ProductResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListProductsForProductFamilyErrorBody
```

**Async**

```python
try:
    response = await async_client.product_families.list_products_for_product_family(
        "some example string",
        page=1,
        per_page=50,
        date_field=BasicDateField.UPDATED_AT,
        include=ListProductsInclude.PREPAID_PRODUCT_PRICE_POINT,
    )
    # TODO: Handle 'response' of type list[ProductResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListProductsForProductFamilyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>str</code> | Either the product family's id or its handle prefixed with `handle:` |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>date_field</code> | <code>[BasicDateFieldOrStr](maxio_advanced_billing/models/enums/basic_date_field.py) \| None</code> | The type of filter you would like to apply to your search.<br>Use in query: `date_field=created_at`.<br>**Default**: <code>None</code> |
| <code>filter_</code> | <code>[ListProductsFilter](maxio_advanced_billing/models/list_products_filter.py) \| [ListProductsFilterDict](maxio_advanced_billing/models/list_products_filter.py) \| None</code> | Filter to use for List Products operations<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>Date \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>Date \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>RFC3339DateTime \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>RFC3339DateTime \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>include_archived</code> | <code>bool \| None</code> | Include archived products.<br>**Default**: <code>None</code> |
| <code>include</code> | <code>[ListProductsIncludeOrStr](maxio_advanced_billing/models/enums/list_products_include.py) \| None</code> | Allows including additional data in the response. Use in query `include=prepaid_product_price_point`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ProductResponse](maxio_advanced_billing/models/product_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListProductsForProductFamilyErrorBody](maxio_advanced_billing/errors/list_products_for_product_family_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>str</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_product_family(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> ProductFamilyResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a Product Family via the `product_family_id`. The response will contain a Product Family object.

The product family can be specified either with the id number, or with the `handle:my-family` format.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_families.read_product_family(1)
    # TODO: Handle 'response' of type ProductFamilyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.product_families.read_product_family(1)
    # TODO: Handle 'response' of type ProductFamilyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the product family |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductFamilyResponse](maxio_advanced_billing/models/product_family_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ProductFeatures

> Source: [ProductFeatures](maxio_advanced_billing/apis/product_features.py)

<details>
<summary><code>def create_product_feature(product_id: int, *, body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Attaches a feature template to this product with a concrete value. Pass `price_point_type: "ProductPricePoint"` and `price_point_id` to create an override scoped to a single product price point instead of the whole product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_features.create_product_feature(1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.product_features.create_product_feature(1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product. |
| <code>body</code> | <code>[CreateFeatureCatalogItemRequest](maxio_advanced_billing/models/create_feature_catalog_item_request.py) \| [CreateFeatureCatalogItemRequestDict](maxio_advanced_billing/models/create_feature_catalog_item_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateProductFeatureErrorBody](maxio_advanced_billing/errors/create_product_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_product_features(product_id: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemsListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the feature catalog items attached to this product, including price-point-specific overrides.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_features.list_product_features(1)
    # TODO: Handle 'response' of type FeatureCatalogItemsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListProductFeaturesErrorBody
```

**Async**

```python
try:
    response = await async_client.product_features.list_product_features(1)
    # TODO: Handle 'response' of type FeatureCatalogItemsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListProductFeaturesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemsListResponse](maxio_advanced_billing/models/feature_catalog_items_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListProductFeaturesErrorBody](maxio_advanced_billing/errors/list_product_features_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_product_feature(product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single feature catalog item attached to this product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_features.read_product_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadProductFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.product_features.read_product_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadProductFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadProductFeatureErrorBody](maxio_advanced_billing/errors/read_product_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_product_feature(product_id: int, id_: int, *, destroy_entitlements: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a feature catalog item from this product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.product_features.remove_product_feature(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveProductFeatureErrorBody
```

**Async**

```python
try:
    await async_client.product_features.remove_product_feature(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveProductFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>destroy_entitlements</code> | <code>bool \| None</code> | When `true`, permanently deletes this feature catalog item and every entitlement it created, revoking subscriber access immediately. When `false` (default), the feature catalog item is archived and existing entitlements are preserved.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RemoveProductFeatureErrorBody](maxio_advanced_billing/errors/remove_product_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def restore_product_feature(product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Clears the archived state of a feature catalog item attached to this product. Returns `422` if the parent feature template is still archived. Restore the feature template first.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_features.restore_product_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreProductFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.product_features.restore_product_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreProductFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RestoreProductFeatureErrorBody](maxio_advanced_billing/errors/restore_product_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_product_feature(product_id: int, id_: int, *, body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> FeatureCatalogItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the value or periodicity of a feature catalog item attached to this product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_features.update_product_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductFeatureErrorBody
```

**Async**

```python
try:
    response = await async_client.product_features.update_product_feature(1, 1)
    # TODO: Handle 'response' of type FeatureCatalogItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductFeatureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product. |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the feature catalog item. |
| <code>body</code> | <code>[UpdateFeatureCatalogItemRequest](maxio_advanced_billing/models/update_feature_catalog_item_request.py) \| [UpdateFeatureCatalogItemRequestDict](maxio_advanced_billing/models/update_feature_catalog_item_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeatureCatalogItemResponse](maxio_advanced_billing/models/feature_catalog_item_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateProductFeatureErrorBody](maxio_advanced_billing/errors/update_product_feature_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ProductPricePoints

> Source: [ProductPricePoints](maxio_advanced_billing/apis/product_price_points.py)

<details>
<summary><code>def archive_product_price_point(product_id: ProductIdModel | ProductIdModelDict, price_point_id: PricePointIdModel | PricePointIdModelDict, *, request_options: RequestOptionsOrDict | None = None) -> ProductPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives a product price point.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.archive_product_price_point(1, 1)
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveProductPricePointErrorBody
```

**Async**

```python
try:
    response = await async_client.product_price_points.archive_product_price_point(1, 1)
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveProductPricePointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>[ProductIdModel](maxio_advanced_billing/models/unions/product_id_model.py) \| [ProductIdModelDict](maxio_advanced_billing/models/unions/product_id_model.py)</code> | The id or handle of the product. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle. |
| <code>price_point_id</code> | <code>[PricePointIdModel](maxio_advanced_billing/models/unions/price_point_id_model.py) \| [PricePointIdModelDict](maxio_advanced_billing/models/unions/price_point_id_model.py)</code> | The id or handle of the price point. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-price-point-handle` for a string handle. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductPricePointResponse](maxio_advanced_billing/models/product_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ArchiveProductPricePointErrorBody](maxio_advanced_billing/errors/archive_product_price_point_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_create_product_price_points(product_id: int, *, body: BulkCreateProductPricePointsRequest | BulkCreateProductPricePointsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> BulkCreateProductPricePointsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates multiple product price points in one request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.bulk_create_product_price_points(
        1,
        body=BulkCreateProductPricePointsRequest(
            price_points=[
                CreateProductPricePoint(
                    name="Educational",
                    handle="educational",
                    price_in_cents=1000,
                    interval=1,
                    interval_unit=IntervalUnit.MONTH,
                    trial_price_in_cents=4900,
                    trial_interval=1,
                    trial_interval_unit=IntervalUnit.MONTH,
                    trial_type=TrialType.PAYMENT_EXPECTED,
                    initial_charge_in_cents=120000,
                    initial_charge_after_trial=False,
                    expiration_interval=12,
                    expiration_interval_unit=ExpirationIntervalUnit.MONTH,
                ),
                CreateProductPricePoint(
                    name="More Educational",
                    handle="more-educational",
                    price_in_cents=2000,
                    interval=1,
                    interval_unit=IntervalUnit.MONTH,
                    trial_price_in_cents=4900,
                    trial_interval=1,
                    trial_interval_unit=IntervalUnit.MONTH,
                    trial_type=TrialType.PAYMENT_EXPECTED,
                    initial_charge_in_cents=120000,
                    initial_charge_after_trial=False,
                    expiration_interval=12,
                    expiration_interval_unit=ExpirationIntervalUnit.MONTH,
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type BulkCreateProductPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkCreateProductPricePointsErrorBody
```

**Async**

```python
try:
    response = await async_client.product_price_points.bulk_create_product_price_points(
        1,
        body=BulkCreateProductPricePointsRequest(
            price_points=[
                CreateProductPricePoint(
                    name="Educational",
                    handle="educational",
                    price_in_cents=1000,
                    interval=1,
                    interval_unit=IntervalUnit.MONTH,
                    trial_price_in_cents=4900,
                    trial_interval=1,
                    trial_interval_unit=IntervalUnit.MONTH,
                    trial_type=TrialType.PAYMENT_EXPECTED,
                    initial_charge_in_cents=120000,
                    initial_charge_after_trial=False,
                    expiration_interval=12,
                    expiration_interval_unit=ExpirationIntervalUnit.MONTH,
                ),
                CreateProductPricePoint(
                    name="More Educational",
                    handle="more-educational",
                    price_in_cents=2000,
                    interval=1,
                    interval_unit=IntervalUnit.MONTH,
                    trial_price_in_cents=4900,
                    trial_interval=1,
                    trial_interval_unit=IntervalUnit.MONTH,
                    trial_type=TrialType.PAYMENT_EXPECTED,
                    initial_charge_in_cents=120000,
                    initial_charge_after_trial=False,
                    expiration_interval=12,
                    expiration_interval_unit=ExpirationIntervalUnit.MONTH,
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type BulkCreateProductPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkCreateProductPricePointsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product to which the price points belong |
| <code>body</code> | <code>[BulkCreateProductPricePointsRequest](maxio_advanced_billing/models/bulk_create_product_price_points_request.py) \| [BulkCreateProductPricePointsRequestDict](maxio_advanced_billing/models/bulk_create_product_price_points_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BulkCreateProductPricePointsResponse](maxio_advanced_billing/models/bulk_create_product_price_points_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[BulkCreateProductPricePointsErrorBody](maxio_advanced_billing/errors/bulk_create_product_price_points_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>dict&#91;str, Any&#93;</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_product_currency_prices(product_price_point_id: int, *, body: CreateProductCurrencyPricesRequest | CreateProductCurrencyPricesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CurrencyPricesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates currency prices for a given currency that has been defined on the site level in your settings.

When creating currency prices, they need to mirror the structure of your primary pricing. If the product price point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

Note: Currency Prices are not able to be created for custom product price points.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.create_product_currency_prices(
        1,
        body=CreateProductCurrencyPricesRequest(
            currency_prices=[
                CreateProductCurrencyPrice(currency="EUR", price=60, role=CurrencyPriceRole.BASELINE),
                CreateProductCurrencyPrice(currency="EUR", price=30, role=CurrencyPriceRole.TRIAL),
                CreateProductCurrencyPrice(currency="EUR", price=100, role=CurrencyPriceRole.INITIAL),
            ],
        ),
    )
    # TODO: Handle 'response' of type CurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductCurrencyPricesErrorBody
```

**Async**

```python
try:
    response = await async_client.product_price_points.create_product_currency_prices(
        1,
        body=CreateProductCurrencyPricesRequest(
            currency_prices=[
                CreateProductCurrencyPrice(currency="EUR", price=60, role=CurrencyPriceRole.BASELINE),
                CreateProductCurrencyPrice(currency="EUR", price=30, role=CurrencyPriceRole.TRIAL),
                CreateProductCurrencyPrice(currency="EUR", price=100, role=CurrencyPriceRole.INITIAL),
            ],
        ),
    )
    # TODO: Handle 'response' of type CurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductCurrencyPricesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_price_point_id</code> | <code>int</code> | The Advanced Billing id of the product price point |
| <code>body</code> | <code>[CreateProductCurrencyPricesRequest](maxio_advanced_billing/models/create_product_currency_prices_request.py) \| [CreateProductCurrencyPricesRequestDict](maxio_advanced_billing/models/create_product_currency_prices_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CurrencyPricesResponse](maxio_advanced_billing/models/currency_prices_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateProductCurrencyPricesErrorBody](maxio_advanced_billing/errors/create_product_currency_prices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_product_price_point(product_id: ProductIdModel | ProductIdModelDict, *, body: CreateProductPricePointRequest | CreateProductPricePointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProductPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Product Price Point. See the [Product Price Point](https://maxio.zendesk.com/hc/en-us/articles/24261111947789-Product-Price-Points) documentation for details.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.create_product_price_point(
        1,
        body=CreateProductPricePointRequest(
            price_point=CreateProductPricePoint(
                name="Educational",
                handle="educational",
                price_in_cents=1000,
                interval=1,
                interval_unit=IntervalUnit.MONTH,
                trial_price_in_cents=4900,
                trial_interval=1,
                trial_interval_unit=IntervalUnit.MONTH,
                trial_type=TrialType.PAYMENT_EXPECTED,
                initial_charge_in_cents=120000,
                initial_charge_after_trial=False,
                expiration_interval=12,
                expiration_interval_unit=ExpirationIntervalUnit.MONTH,
            ),
        ),
    )
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductPricePointErrorBody
```

**Async**

```python
try:
    response = await async_client.product_price_points.create_product_price_point(
        1,
        body=CreateProductPricePointRequest(
            price_point=CreateProductPricePoint(
                name="Educational",
                handle="educational",
                price_in_cents=1000,
                interval=1,
                interval_unit=IntervalUnit.MONTH,
                trial_price_in_cents=4900,
                trial_interval=1,
                trial_interval_unit=IntervalUnit.MONTH,
                trial_type=TrialType.PAYMENT_EXPECTED,
                initial_charge_in_cents=120000,
                initial_charge_after_trial=False,
                expiration_interval=12,
                expiration_interval_unit=ExpirationIntervalUnit.MONTH,
            ),
        ),
    )
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductPricePointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>[ProductIdModel](maxio_advanced_billing/models/unions/product_id_model.py) \| [ProductIdModelDict](maxio_advanced_billing/models/unions/product_id_model.py)</code> | The id or handle of the product. When using the handle, it must be prefixed with `handle:` |
| <code>body</code> | <code>[CreateProductPricePointRequest](maxio_advanced_billing/models/create_product_price_point_request.py) \| [CreateProductPricePointRequestDict](maxio_advanced_billing/models/create_product_price_point_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductPricePointResponse](maxio_advanced_billing/models/product_price_point_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateProductPricePointErrorBody](maxio_advanced_billing/errors/create_product_price_point_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ProductPricePointErrorResponse1](maxio_advanced_billing/models/product_price_point_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_all_product_price_points(*, direction: SortingDirectionOrStr | None = None, filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None, include: ListProductsPricePointsIncludeOrStr | None = None, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ListProductPricePointsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists Product Price Points belonging to a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.list_all_product_price_points(
        include=ListProductsPricePointsInclude.CURRENCY_PRICES, page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListProductPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllProductPricePointsErrorBody
```

**Async**

```python
try:
    response = await async_client.product_price_points.list_all_product_price_points(
        include=ListProductsPricePointsInclude.CURRENCY_PRICES, page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListProductPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllProductPricePointsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>filter_</code> | <code>[ListPricePointsFilter](maxio_advanced_billing/models/list_price_points_filter.py) \| [ListPricePointsFilterDict](maxio_advanced_billing/models/list_price_points_filter.py) \| None</code> | Filter to use for List PricePoints operations<br>**Default**: <code>None</code> |
| <code>include</code> | <code>[ListProductsPricePointsIncludeOrStr](maxio_advanced_billing/models/enums/list_products_price_points_include.py) \| None</code> | Allows including additional data in the response. Use in query: `include=currency_prices`.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListProductPricePointsResponse](maxio_advanced_billing/models/list_product_price_points_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListAllProductPricePointsErrorBody](maxio_advanced_billing/errors/list_all_product_price_points_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_product_price_points(product_id: ProductIdModel | ProductIdModelDict, *, page: int | None = 1, per_page: int | None = 10, currency_prices: bool | None = None, filter_type: list[PricePointTypeOrStr] | None = None, archived: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ListProductPricePointsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of product price points.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.list_product_price_points(
        1, page=1, filter_type=[PricePointType.CATALOG, PricePointType.DEFAULT]
    )
    # TODO: Handle 'response' of type ListProductPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.product_price_points.list_product_price_points(
        1, page=1, filter_type=[PricePointType.CATALOG, PricePointType.DEFAULT]
    )
    # TODO: Handle 'response' of type ListProductPricePointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>[ProductIdModel](maxio_advanced_billing/models/unions/product_id_model.py) \| [ProductIdModelDict](maxio_advanced_billing/models/unions/product_id_model.py)</code> | The id or handle of the product. When using the handle, it must be prefixed with `handle:` |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 10. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>**Default**: <code>10</code> |
| <code>currency_prices</code> | <code>bool \| None</code> | (Optional) If you have defined multiple currencies at the site level, you can pass ?currency_prices=true to include an array of currency price data in the response. If the product price point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.<br>**Default**: <code>None</code> |
| <code>filter_type</code> | <code>list&#91;[PricePointTypeOrStr](maxio_advanced_billing/models/enums/price_point_type.py)&#93; \| None</code> | Use in query: `filter[type]=catalog,default`.<br>**Default**: <code>None</code> |
| <code>archived</code> | <code>bool \| None</code> | Set to include archived price points in the response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListProductPricePointsResponse](maxio_advanced_billing/models/list_product_price_points_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def promote_product_price_point_to_default(product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets a product price point as the default for the product.

Note: Custom product price points cannot be set as the default for a product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.promote_product_price_point_to_default(1, 1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.product_price_points.promote_product_price_point_to_default(1, 1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product to which the price point belongs |
| <code>price_point_id</code> | <code>int</code> | The Advanced Billing id of the product price point |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductResponse](maxio_advanced_billing/models/product_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_product_price_point(product_id: ProductIdModel | ProductIdModelDict, price_point_id: PricePointIdModel | PricePointIdModelDict, *, currency_prices: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ProductPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details for a specific product price point. You can achieve this by using either the product price point ID or handle.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.read_product_price_point(1, 1)
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.product_price_points.read_product_price_point(1, 1)
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>[ProductIdModel](maxio_advanced_billing/models/unions/product_id_model.py) \| [ProductIdModelDict](maxio_advanced_billing/models/unions/product_id_model.py)</code> | The id or handle of the product. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle. |
| <code>price_point_id</code> | <code>[PricePointIdModel](maxio_advanced_billing/models/unions/price_point_id_model.py) \| [PricePointIdModelDict](maxio_advanced_billing/models/unions/price_point_id_model.py)</code> | The id or handle of the price point. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-price-point-handle` for a string handle. |
| <code>currency_prices</code> | <code>bool \| None</code> | (Optional) If you have defined multiple currencies at the site level, you can pass ?currency_prices=true to include an array of currency price data in the response. If the product price point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductPricePointResponse](maxio_advanced_billing/models/product_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unarchive_product_price_point(product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ProductPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unarchives an archived product price point.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.unarchive_product_price_point(1, 1)
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.product_price_points.unarchive_product_price_point(1, 1)
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product to which the price point belongs |
| <code>price_point_id</code> | <code>int</code> | The Advanced Billing id of the product price point |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductPricePointResponse](maxio_advanced_billing/models/product_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_product_currency_prices(product_price_point_id: int, *, body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CurrencyPricesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the `price`s of currency prices for a given currency that exists on the product price point.

When updating the pricing, it needs to mirror the structure of your primary pricing. If the product price point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

Note: Currency Prices cannot be updated for custom product price points.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.update_product_currency_prices(
        1,
        body=UpdateCurrencyPricesRequest(
            currency_prices=[UpdateCurrencyPrice(id=200, price=15), UpdateCurrencyPrice(id=201, price=5)]
        ),
    )
    # TODO: Handle 'response' of type CurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductCurrencyPricesErrorBody
```

**Async**

```python
try:
    response = await async_client.product_price_points.update_product_currency_prices(
        1,
        body=UpdateCurrencyPricesRequest(
            currency_prices=[UpdateCurrencyPrice(id=200, price=15), UpdateCurrencyPrice(id=201, price=5)]
        ),
    )
    # TODO: Handle 'response' of type CurrencyPricesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductCurrencyPricesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_price_point_id</code> | <code>int</code> | The Advanced Billing id of the product price point |
| <code>body</code> | <code>[UpdateCurrencyPricesRequest](maxio_advanced_billing/models/update_currency_prices_request.py) \| [UpdateCurrencyPricesRequestDict](maxio_advanced_billing/models/update_currency_prices_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CurrencyPricesResponse](maxio_advanced_billing/models/currency_prices_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateProductCurrencyPricesErrorBody](maxio_advanced_billing/errors/update_product_currency_prices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_product_price_point(product_id: ProductIdModel | ProductIdModelDict, price_point_id: PricePointIdModel | PricePointIdModelDict, *, body: UpdateProductPricePointRequest | UpdateProductPricePointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProductPricePointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a product price point.

Note: Custom product price points cannot be updated.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_price_points.update_product_price_point(
        1,
        1,
        body=UpdateProductPricePointRequest(
            price_point=UpdateProductPricePoint(handle="educational", price_in_cents=1250)
        ),
    )
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.product_price_points.update_product_price_point(
        1,
        1,
        body=UpdateProductPricePointRequest(
            price_point=UpdateProductPricePoint(handle="educational", price_in_cents=1250)
        ),
    )
    # TODO: Handle 'response' of type ProductPricePointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>[ProductIdModel](maxio_advanced_billing/models/unions/product_id_model.py) \| [ProductIdModelDict](maxio_advanced_billing/models/unions/product_id_model.py)</code> | The id or handle of the product. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle. |
| <code>price_point_id</code> | <code>[PricePointIdModel](maxio_advanced_billing/models/unions/price_point_id_model.py) \| [PricePointIdModelDict](maxio_advanced_billing/models/unions/price_point_id_model.py)</code> | The id or handle of the price point. When using the handle, it must be prefixed with `handle:`. Example: `123` for an integer ID, or `handle:example-product-price-point-handle` for a string handle. |
| <code>body</code> | <code>[UpdateProductPricePointRequest](maxio_advanced_billing/models/update_product_price_point_request.py) \| [UpdateProductPricePointRequestDict](maxio_advanced_billing/models/update_product_price_point_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductPricePointResponse](maxio_advanced_billing/models/product_price_point_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Products

> Source: [Products](maxio_advanced_billing/apis/products.py)

<details>
<summary><code>def archive_product(product_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives the product. All current subscribers will be unaffected; their subscription/purchase will continue to be charged monthly.

This will restrict the option to chose the product for purchase via the Billing Portal, as well as disable Public Signup Pages for the product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.products.archive_product(1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveProductErrorBody
```

**Async**

```python
try:
    response = await async_client.products.archive_product(1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductResponse](maxio_advanced_billing/models/product_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ArchiveProductErrorBody](maxio_advanced_billing/errors/archive_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_product(product_family_id: str, *, body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a product in your site.

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, the `auto_create_signup_page` parameter is not supported. If `auto_create_signup_page` is included (with any value) an error is returned.

For more information, see:

+ [Products Overview](https://maxio.zendesk.com/hc/en-us/articles/24261090117645-Products-Overview)
+ [Changing a Subscription's Product](https://maxio.zendesk.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.products.create_product(
        "some example string",
        body=CreateOrUpdateProductRequest(
            product=CreateOrUpdateProduct(
                name="Gold Plan",
                handle="gold",
                description="This is our gold plan.",
                accounting_code="123",
                require_credit_card=True,
                price_in_cents=1000,
                interval=1,
                interval_unit=IntervalUnit.MONTH,
                auto_create_signup_page=True,
                tax_code="D0000000",
            ),
        ),
    )
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductErrorBody
```

**Async**

```python
try:
    response = await async_client.products.create_product(
        "some example string",
        body=CreateOrUpdateProductRequest(
            product=CreateOrUpdateProduct(
                name="Gold Plan",
                handle="gold",
                description="This is our gold plan.",
                accounting_code="123",
                require_credit_card=True,
                price_in_cents=1000,
                interval=1,
                interval_unit=IntervalUnit.MONTH,
                auto_create_signup_page=True,
                tax_code="D0000000",
            ),
        ),
    )
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_family_id</code> | <code>str</code> | Either the product family's id or its handle prefixed with `handle:` |
| <code>body</code> | <code>[CreateOrUpdateProductRequest](maxio_advanced_billing/models/create_or_update_product_request.py) \| [CreateOrUpdateProductRequestDict](maxio_advanced_billing/models/create_or_update_product_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductResponse](maxio_advanced_billing/models/product_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateProductErrorBody](maxio_advanced_billing/errors/create_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_products(*, date_field: BasicDateFieldOrStr | None = None, filter_: ListProductsFilter | ListProductsFilterDict | None = None, end_date: Date | None = None, end_datetime: RFC3339DateTime | None = None, start_date: Date | None = None, start_datetime: RFC3339DateTime | None = None, page: int | None = 1, per_page: int | None = 20, include_archived: bool | None = None, include: ListProductsIncludeOrStr | None = None, include_features: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> list[ProductResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists products belonging to a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.products.list_products(
        date_field=BasicDateField.UPDATED_AT,
        page=1,
        per_page=50,
        include_archived=True,
        include=ListProductsInclude.PREPAID_PRODUCT_PRICE_POINT,
    )
    # TODO: Handle 'response' of type list[ProductResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.products.list_products(
        date_field=BasicDateField.UPDATED_AT,
        page=1,
        per_page=50,
        include_archived=True,
        include=ListProductsInclude.PREPAID_PRODUCT_PRICE_POINT,
    )
    # TODO: Handle 'response' of type list[ProductResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>date_field</code> | <code>[BasicDateFieldOrStr](maxio_advanced_billing/models/enums/basic_date_field.py) \| None</code> | The type of filter you would like to apply to your search.<br>Use in query: `date_field=created_at`.<br>**Default**: <code>None</code> |
| <code>filter_</code> | <code>[ListProductsFilter](maxio_advanced_billing/models/list_products_filter.py) \| [ListProductsFilterDict](maxio_advanced_billing/models/list_products_filter.py) \| None</code> | Filter to use for List Products operations<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>Date \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>RFC3339DateTime \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>Date \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>RFC3339DateTime \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns products with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>include_archived</code> | <code>bool \| None</code> | Include archived products. Use in query: `include_archived=true`.<br>**Default**: <code>None</code> |
| <code>include</code> | <code>[ListProductsIncludeOrStr](maxio_advanced_billing/models/enums/list_products_include.py) \| None</code> | Allows including additional data in the response. Use in query `include=prepaid_product_price_point`.<br>**Default**: <code>None</code> |
| <code>include_features</code> | <code>bool \| None</code> | When `true`, embeds the active feature catalog items for each result in a `features` array. Default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ProductResponse](maxio_advanced_billing/models/product_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_product(product_id: int, *, include_features: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reads the current details of a product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.products.read_product(1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.products.read_product(1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product |
| <code>include_features</code> | <code>bool \| None</code> | When `true`, embeds the active feature catalog items for each result in a `features` array. Default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductResponse](maxio_advanced_billing/models/product_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_product_by_handle(api_handle: str, *, request_options: RequestOptionsOrDict | None = None) -> ProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a Product object by its `api_handle`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.products.read_product_by_handle("some example string")
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.products.read_product_by_handle("some example string")
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_handle</code> | <code>str</code> | The handle of the product |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductResponse](maxio_advanced_billing/models/product_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_product(product_id: int, *, body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates aspects of an existing product.

### Input Attributes Update Notes

+ `update_return_params` The parameters we will append to your `update_return_url`. See Return URLs and Parameters

### Product Price Point

Updating a product using this endpoint will create a new price point and set it as the default price point for this product. If you should like to update an existing product price point, that must be done separately.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.products.update_product(1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductErrorBody
```

**Async**

```python
try:
    response = await async_client.products.update_product(1)
    # TODO: Handle 'response' of type ProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_id</code> | <code>int</code> | The Advanced Billing id of the product |
| <code>body</code> | <code>[CreateOrUpdateProductRequest](maxio_advanced_billing/models/create_or_update_product_request.py) \| [CreateOrUpdateProductRequestDict](maxio_advanced_billing/models/create_or_update_product_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductResponse](maxio_advanced_billing/models/product_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateProductErrorBody](maxio_advanced_billing/errors/update_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ProformaInvoices

> Source: [ProformaInvoices](maxio_advanced_billing/apis/proforma_invoices.py)

<details>
<summary><code>def create_consolidated_proforma_invoice(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a consolidated proforma invoice asynchronously. To find and view the new consolidated proforma invoice, you can poll the subscription group listing for proforma invoices; only one consolidated proforma invoice can be created per group at a time.

If the information becomes outdated, simply void the old consolidated proforma invoice and generate a new one.

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the subscription must not be prepaid, and must be in a live state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.proforma_invoices.create_consolidated_proforma_invoice("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConsolidatedProformaInvoiceErrorBody
```

**Async**

```python
try:
    await async_client.proforma_invoices.create_consolidated_proforma_invoice("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConsolidatedProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateConsolidatedProformaInvoiceErrorBody](maxio_advanced_billing/errors/create_consolidated_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_proforma_invoice(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ProformaInvoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a proforma invoice and returns it as a response. If the information becomes outdated, simply void the old proforma invoice and generate a new one.

If you would like to preview the next billing amounts without generating a full proforma invoice, use the renewal preview endpoint.

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the subscription must not be in a group, must not be prepaid, and must be in a live state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.create_proforma_invoice(1)
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProformaInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.create_proforma_invoice(1)
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProformaInvoice](maxio_advanced_billing/models/proforma_invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateProformaInvoiceErrorBody](maxio_advanced_billing/errors/create_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_signup_proforma_invoice(*, body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProformaInvoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a proforma invoice to preview costs before a subscription's signup. This endpoint is only available for Relationship Invoicing sites and cannot be used to create consolidated proforma invoices or preview prepaid subscriptions. Like other proforma invoices, it can be emailed to the customer, voided, and publicly viewed on the chargifypay domain.

Pass a payload that resembles a subscription create or signup preview request. For example, you can specify components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate a shipping or billing address.

A product and customer first name, last name, and email are the minimum requirements. We recommend associating the proforma invoice with a customer_id to easily find their proforma invoices, since the subscription_id will always be blank.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.create_signup_proforma_invoice(
        body=CreateSubscriptionRequest(
            subscription=CreateSubscription(
                product_handle="gold-product",
                customer_attributes=CustomerAttributes(
                    first_name="Myra", last_name="Maisel", email="mmaisel@example.com"
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSignupProformaInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.create_signup_proforma_invoice(
        body=CreateSubscriptionRequest(
            subscription=CreateSubscription(
                product_handle="gold-product",
                customer_attributes=CustomerAttributes(
                    first_name="Myra", last_name="Maisel", email="mmaisel@example.com"
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSignupProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateSubscriptionRequest](maxio_advanced_billing/models/create_subscription_request.py) \| [CreateSubscriptionRequestDict](maxio_advanced_billing/models/create_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProformaInvoice](maxio_advanced_billing/models/proforma_invoice.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateSignupProformaInvoiceErrorBody](maxio_advanced_billing/errors/create_signup_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProformaBadRequestErrorResponse1](maxio_advanced_billing/models/proforma_bad_request_error_response1.py)</code> |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deliver_proforma_invoice(proforma_invoice_uid: str, *, body: DeliverProformaInvoiceRequest | DeliverProformaInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProformaInvoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delivers a proforma invoice programmatically via email. Supports email
delivery to direct recipients, carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

If `recipient_emails` is omitted, the system will fall back to the primary recipient derived from the invoice or
subscription. At least one recipient must be present, either via the request body or via this default behavior, so an
empty body may still succeed when defaults are available.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.deliver_proforma_invoice(
        "some example string",
        body=DeliverProformaInvoiceRequest(
            recipient_emails=["user0@example.com"],
            cc_recipient_emails=["user1@example.com"],
            bcc_recipient_emails=["user2@example.com"],
        ),
    )
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeliverProformaInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.deliver_proforma_invoice(
        "some example string",
        body=DeliverProformaInvoiceRequest(
            recipient_emails=["user0@example.com"],
            cc_recipient_emails=["user1@example.com"],
            bcc_recipient_emails=["user2@example.com"],
        ),
    )
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeliverProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>proforma_invoice_uid</code> | <code>str</code> | The uid of the proforma invoice |
| <code>body</code> | <code>[DeliverProformaInvoiceRequest](maxio_advanced_billing/models/deliver_proforma_invoice_request.py) \| [DeliverProformaInvoiceRequestDict](maxio_advanced_billing/models/deliver_proforma_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProformaInvoice](maxio_advanced_billing/models/proforma_invoice.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeliverProformaInvoiceErrorBody](maxio_advanced_billing/errors/deliver_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_proforma_invoices(subscription_id: int, *, start_date: str | None = None, end_date: str | None = None, status: ProformaInvoiceStatusOrStr | None = None, page: int | None = 1, per_page: int | None = 20, direction: DirectionOrStr | None = Direction.DESC, line_items: bool | None = False, discounts: bool | None = False, taxes: bool | None = False, credits_: bool | None = False, payments: bool | None = False, custom_fields: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ListProformaInvoicesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists proforma invoices for a subscription. By default, results only include totals, not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, or `custom_fields`. To include breakdowns, pass the specific field as a key in the query with a value set to `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.list_proforma_invoices(1, page=1, per_page=50)
    # TODO: Handle 'response' of type ListProformaInvoicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.list_proforma_invoices(1, page=1, per_page=50)
    # TODO: Handle 'response' of type ListProformaInvoicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>start_date</code> | <code>str \| None</code> | The beginning date range for the invoice's Due Date, in the YYYY-MM-DD format.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The ending date range for the invoice's Due Date, in the YYYY-MM-DD format.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[ProformaInvoiceStatusOrStr](maxio_advanced_billing/models/enums/proforma_invoice_status.py) \| None</code> | The current status of the invoice.  Allowed Values: draft, open, paid, pending, voided<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[DirectionOrStr](maxio_advanced_billing/models/enums/direction.py) \| None</code> | The sort direction of the returned invoices.<br>**Default**: <code>Direction.DESC</code> |
| <code>line_items</code> | <code>bool \| None</code> | Include line items data.<br>**Default**: <code>False</code> |
| <code>discounts</code> | <code>bool \| None</code> | Include discounts data.<br>**Default**: <code>False</code> |
| <code>taxes</code> | <code>bool \| None</code> | Include taxes data.<br>**Default**: <code>False</code> |
| <code>credits_</code> | <code>bool \| None</code> | Include credits data.<br>**Default**: <code>False</code> |
| <code>payments</code> | <code>bool \| None</code> | Include payments data.<br>**Default**: <code>False</code> |
| <code>custom_fields</code> | <code>bool \| None</code> | Include custom fields data.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListProformaInvoicesResponse](maxio_advanced_billing/models/list_proforma_invoices_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_group_proforma_invoices(uid: str, *, line_items: bool | None = False, discounts: bool | None = False, taxes: bool | None = False, credits_: bool | None = False, payments: bool | None = False, custom_fields: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ListProformaInvoicesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists proforma invoices with a `consolidation_level` of parent for the subscription group.

By default, proforma invoices returned on the index will only include totals, not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, `custom_fields`. To include breakdowns, pass the specific field as a key in the query with a value set to true.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.list_subscription_group_proforma_invoices("some example string")
    # TODO: Handle 'response' of type ListProformaInvoicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionGroupProformaInvoicesErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.list_subscription_group_proforma_invoices("some example string")
    # TODO: Handle 'response' of type ListProformaInvoicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionGroupProformaInvoicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>line_items</code> | <code>bool \| None</code> | Include line items data.<br>**Default**: <code>False</code> |
| <code>discounts</code> | <code>bool \| None</code> | Include discounts data.<br>**Default**: <code>False</code> |
| <code>taxes</code> | <code>bool \| None</code> | Include taxes data.<br>**Default**: <code>False</code> |
| <code>credits_</code> | <code>bool \| None</code> | Include credits data.<br>**Default**: <code>False</code> |
| <code>payments</code> | <code>bool \| None</code> | Include payments data.<br>**Default**: <code>False</code> |
| <code>custom_fields</code> | <code>bool \| None</code> | Include custom fields data.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListProformaInvoicesResponse](maxio_advanced_billing/models/list_proforma_invoices_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListSubscriptionGroupProformaInvoicesErrorBody](maxio_advanced_billing/errors/list_subscription_group_proforma_invoices_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_proforma_invoice(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ProformaInvoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Previews the data that will be included on a given subscription's proforma invoice if one were to be generated. It will have similar line items and totals as a renewal preview, but the response will be presented in the format of a proforma invoice. Consequently it will include additional information such as the name and addresses that will appear on the proforma invoice.

The preview endpoint is subject to all the same conditions as the proforma invoice endpoint. For example, previews are only available on the Relationship Invoicing architecture, and previews cannot be made for end-of-life subscriptions.

If all the data returned in the preview is as expected, you may then create a static proforma invoice and send it to your customer. The data within a preview will not be saved and will not be accessible after the call is made.

Alternatively, if you have some proforma invoices already, you may make a preview call to determine whether any billing information for the subscription's upcoming renewal has changed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.preview_proforma_invoice(1)
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewProformaInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.preview_proforma_invoice(1)
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProformaInvoice](maxio_advanced_billing/models/proforma_invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PreviewProformaInvoiceErrorBody](maxio_advanced_billing/errors/preview_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_signup_proforma_invoice(*, include: CreateSignupProformaPreviewIncludeOrStr | None = None, body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SignupProformaPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a signup preview in the format of a proforma invoice to preview costs before a subscription's signup. This endpoint is only available for Relationship Invoicing sites and cannot be used to create consolidated proforma invoice previews or preview prepaid subscriptions. You have the option of previewing the first renewal's costs as well. The proforma invoice preview will not be persisted.

Pass a payload that resembles a subscription create or signup preview request. For example, you can specify components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate a shipping or billing address.

A product and customer first name, last name, and email are the minimum requirements.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.preview_signup_proforma_invoice(
        include=CreateSignupProformaPreviewInclude.NEXT_PROFORMA_INVOICE,
        body=CreateSubscriptionRequest(
            subscription=CreateSubscription(
                product_handle="gold-plan",
                customer_attributes=CustomerAttributes(first_name="first", last_name="last", email="flast@example.com"),
            ),
        ),
    )
    # TODO: Handle 'response' of type SignupProformaPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewSignupProformaInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.preview_signup_proforma_invoice(
        include=CreateSignupProformaPreviewInclude.NEXT_PROFORMA_INVOICE,
        body=CreateSubscriptionRequest(
            subscription=CreateSubscription(
                product_handle="gold-plan",
                customer_attributes=CustomerAttributes(first_name="first", last_name="last", email="flast@example.com"),
            ),
        ),
    )
    # TODO: Handle 'response' of type SignupProformaPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewSignupProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include</code> | <code>[CreateSignupProformaPreviewIncludeOrStr](maxio_advanced_billing/models/enums/create_signup_proforma_preview_include.py) \| None</code> | Choose to include a proforma invoice preview for the first renewal. Use in query `include=next_proforma_invoice`.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[CreateSubscriptionRequest](maxio_advanced_billing/models/create_subscription_request.py) \| [CreateSubscriptionRequestDict](maxio_advanced_billing/models/create_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SignupProformaPreviewResponse](maxio_advanced_billing/models/signup_proforma_preview_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PreviewSignupProformaInvoiceErrorBody](maxio_advanced_billing/errors/preview_signup_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProformaBadRequestErrorResponse1](maxio_advanced_billing/models/proforma_bad_request_error_response1.py)</code> |
| 422 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_proforma_invoice(proforma_invoice_uid: str, *, request_options: RequestOptionsOrDict | None = None) -> ProformaInvoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the details of an existing proforma invoice.

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.read_proforma_invoice("some example string")
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadProformaInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.read_proforma_invoice("some example string")
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>proforma_invoice_uid</code> | <code>str</code> | The uid of the proforma invoice |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProformaInvoice](maxio_advanced_billing/models/proforma_invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadProformaInvoiceErrorBody](maxio_advanced_billing/errors/read_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def void_proforma_invoice(proforma_invoice_uid: str, *, body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ProformaInvoice</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Voids a proforma invoice that has the status "draft".

## Restrictions

Proforma invoices are only available on Relationship Invoicing sites.

Only proforma invoices that have the appropriate status may be reopened. If the invoice identified by {uid} does not have the appropriate status, the response will have HTTP status code 422 and an error message.

A reason for the void operation is required to be included in the request body. If one is not provided, the response will have HTTP status code 422 and an error message.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.proforma_invoices.void_proforma_invoice("some example string")
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidProformaInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.proforma_invoices.void_proforma_invoice("some example string")
    # TODO: Handle 'response' of type ProformaInvoice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type VoidProformaInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>proforma_invoice_uid</code> | <code>str</code> | The uid of the proforma invoice |
| <code>body</code> | <code>[VoidInvoiceRequest](maxio_advanced_billing/models/void_invoice_request.py) \| [VoidInvoiceRequestDict](maxio_advanced_billing/models/void_invoice_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProformaInvoice](maxio_advanced_billing/models/proforma_invoice.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[VoidProformaInvoiceErrorBody](maxio_advanced_billing/errors/void_proforma_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ReasonCodes

> Source: [ReasonCodes](maxio_advanced_billing/apis/reason_codes.py)

<details>
<summary><code>def create_reason_code(*, body: CreateReasonCodeRequest | CreateReasonCodeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ReasonCodeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a reason code for a given site.

Reason Codes are a way to gain a high-level view of why your customers are cancelling the subscription to your product or service.

Add a set of churn reason codes to be displayed in-app and/or the Maxio Billing Portal. As your subscribers decide to cancel their subscription, learn why they decided to cancel.

For more information, see [Churn Reason Codes](https://maxio.zendesk.com/hc/en-us/articles/24286647554701-Churn-Reason-Codes).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reason_codes.create_reason_code(
        body=CreateReasonCodeRequest(
            reason_code=CreateReasonCode(code="NOTHANKYOU", description="No thank you!", position=5)
        ),
    )
    # TODO: Handle 'response' of type ReasonCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateReasonCodeErrorBody
```

**Async**

```python
try:
    response = await async_client.reason_codes.create_reason_code(
        body=CreateReasonCodeRequest(
            reason_code=CreateReasonCode(code="NOTHANKYOU", description="No thank you!", position=5)
        ),
    )
    # TODO: Handle 'response' of type ReasonCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateReasonCodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateReasonCodeRequest](maxio_advanced_billing/models/create_reason_code_request.py) \| [CreateReasonCodeRequestDict](maxio_advanced_billing/models/create_reason_code_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReasonCodeResponse](maxio_advanced_billing/models/reason_code_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateReasonCodeErrorBody](maxio_advanced_billing/errors/create_reason_code_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_reason_code(reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None) -> OkResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a reason code from the Churn Reason Codes. This code will be immediately removed. This action is not reversible.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reason_codes.delete_reason_code(1)
    # TODO: Handle 'response' of type OkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteReasonCodeErrorBody
```

**Async**

```python
try:
    response = await async_client.reason_codes.delete_reason_code(1)
    # TODO: Handle 'response' of type OkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteReasonCodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reason_code_id</code> | <code>int</code> | The Advanced Billing id of the reason code |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OkResponse](maxio_advanced_billing/models/ok_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteReasonCodeErrorBody](maxio_advanced_billing/errors/delete_reason_code_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_reason_codes(*, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> list[ReasonCodeResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all current churn codes for a given site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reason_codes.list_reason_codes(page=1, per_page=50)
    # TODO: Handle 'response' of type list[ReasonCodeResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListReasonCodesErrorBody
```

**Async**

```python
try:
    response = await async_client.reason_codes.list_reason_codes(page=1, per_page=50)
    # TODO: Handle 'response' of type list[ReasonCodeResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListReasonCodesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ReasonCodeResponse](maxio_advanced_billing/models/reason_code_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListReasonCodesErrorBody](maxio_advanced_billing/errors/list_reason_codes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_reason_code(reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None) -> ReasonCodeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a particular churn reason code for a given site by its unique ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reason_codes.read_reason_code(1)
    # TODO: Handle 'response' of type ReasonCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadReasonCodeErrorBody
```

**Async**

```python
try:
    response = await async_client.reason_codes.read_reason_code(1)
    # TODO: Handle 'response' of type ReasonCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadReasonCodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reason_code_id</code> | <code>int</code> | The Advanced Billing id of the reason code |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReasonCodeResponse](maxio_advanced_billing/models/reason_code_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadReasonCodeErrorBody](maxio_advanced_billing/errors/read_reason_code_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_reason_code(reason_code_id: int, *, body: UpdateReasonCodeRequest | UpdateReasonCodeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ReasonCodeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing reason code for a given site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reason_codes.update_reason_code(1)
    # TODO: Handle 'response' of type ReasonCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateReasonCodeErrorBody
```

**Async**

```python
try:
    response = await async_client.reason_codes.update_reason_code(1)
    # TODO: Handle 'response' of type ReasonCodeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateReasonCodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reason_code_id</code> | <code>int</code> | The Advanced Billing id of the reason code |
| <code>body</code> | <code>[UpdateReasonCodeRequest](maxio_advanced_billing/models/update_reason_code_request.py) \| [UpdateReasonCodeRequestDict](maxio_advanced_billing/models/update_reason_code_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReasonCodeResponse](maxio_advanced_billing/models/reason_code_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateReasonCodeErrorBody](maxio_advanced_billing/errors/update_reason_code_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ReferralCodes

> Source: [ReferralCodes](maxio_advanced_billing/apis/referral_codes.py)

<details>
<summary><code>def validate_referral_code(code: str, *, request_options: RequestOptionsOrDict | None = None) -> ReferralValidationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Validates whether a referral code is valid and applicable within your site. This method is useful for validating referral codes that are entered by a customer.

For more information, see [Understanding Referrals](https://docs.maxio.com/hc/en-us/articles/24286981223693-Understanding-Referrals) in the product documentation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.referral_codes.validate_referral_code("some example string")
    # TODO: Handle 'response' of type ReferralValidationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ValidateReferralCodeErrorBody
```

**Async**

```python
try:
    response = await async_client.referral_codes.validate_referral_code("some example string")
    # TODO: Handle 'response' of type ReferralValidationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ValidateReferralCodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | The referral code you are trying to validate |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReferralValidationResponse](maxio_advanced_billing/models/referral_validation_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ValidateReferralCodeErrorBody](maxio_advanced_billing/errors/validate_referral_code_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[SingleStringErrorResponse1](maxio_advanced_billing/models/single_string_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SalesCommissions

> Source: [SalesCommissions](maxio_advanced_billing/apis/sales_commissions.py)

<details>
<summary><code>def list_sales_commission_settings(seller_id: str, *, live_mode: bool | None = None, page: int | None = 1, per_page: int | None = 100, authorization: str | None = "Bearer <<apiKey>>", request_options: RequestOptionsOrDict | None = None) -> list[SaleRepSettings]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists subscriptions with associated sales reps.

## Modified Authentication Process

The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site was a sufficient solution. To share resources at the seller level, a new authentication method was introduced, which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales Commission API, more details [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).

Access to the Sales Commission API endpoints is available to users with financial access, where the seller has the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics contact Maxio support.

> Note: The request is at seller level, it means `<<subdomain>>` variable will be replaced by `app`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sales_commissions.list_sales_commission_settings("some example string", page=1)
    # TODO: Handle 'response' of type list[SaleRepSettings]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sales_commissions.list_sales_commission_settings("some example string", page=1)
    # TODO: Handle 'response' of type list[SaleRepSettings]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | The Chargify id of your seller account |
| <code>live_mode</code> | <code>bool \| None</code> | This parameter indicates if records should be fetched from live mode sites. Default value is true.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 100.<br>**Default**: <code>100</code> |
| <code>authorization</code> | <code>str \| None</code> | For authorization use user API key. See details [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).<br>**Default**: <code>"Bearer <<apiKey>>"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SaleRepSettings](maxio_advanced_billing/models/sale_rep_settings.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_sales_reps(seller_id: str, *, live_mode: bool | None = None, page: int | None = 1, per_page: int | None = 100, authorization: str | None = "Bearer <<apiKey>>", request_options: RequestOptionsOrDict | None = None) -> list[ListSaleRepItem]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists sales reps with details.

## Modified Authentication Process

The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site was a sufficient solution. To share resources at the seller level, a new authentication method was introduced, which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales Commission API, more details [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).

Access to the Sales Commission API endpoints is available to users with financial access, where the seller has the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics contact Maxio support.

> Note: The request is at seller level, it means `<<subdomain>>` variable will be replaced by `app`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sales_commissions.list_sales_reps("some example string", page=1)
    # TODO: Handle 'response' of type list[ListSaleRepItem]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sales_commissions.list_sales_reps("some example string", page=1)
    # TODO: Handle 'response' of type list[ListSaleRepItem]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | The Chargify id of your seller account |
| <code>live_mode</code> | <code>bool \| None</code> | This parameter indicates if records should be fetched from live mode sites. Default value is true.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 100.<br>**Default**: <code>100</code> |
| <code>authorization</code> | <code>str \| None</code> | For authorization use user API key. See details [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).<br>**Default**: <code>"Bearer <<apiKey>>"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[ListSaleRepItem](maxio_advanced_billing/models/list_sale_rep_item.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_sales_rep(seller_id: str, sales_rep_id: str, *, live_mode: bool | None = None, page: int | None = 1, per_page: int | None = 100, authorization: str | None = "Bearer <<apiKey>>", request_options: RequestOptionsOrDict | None = None) -> SaleRep</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a sales rep and attached subscription details.

## Modified Authentication Process

The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site was a sufficient solution. To share resources at the seller level, a new authentication method was introduced, which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales Commission API, more details [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).

Access to the Sales Commission API endpoints is available to users with financial access, where the seller has the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics contact Maxio support.

> Note: The request is at seller level, it means `<<subdomain>>` variable will be replaced by `app`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sales_commissions.read_sales_rep("some example string", "some example string", page=1)
    # TODO: Handle 'response' of type SaleRep
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sales_commissions.read_sales_rep("some example string", "some example string", page=1)
    # TODO: Handle 'response' of type SaleRep
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | The Chargify id of your seller account |
| <code>sales_rep_id</code> | <code>str</code> | The Advanced Billing id of sales rep. |
| <code>live_mode</code> | <code>bool \| None</code> | This parameter indicates if records should be fetched from live mode sites. Default value is true.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 100.<br>**Default**: <code>100</code> |
| <code>authorization</code> | <code>str \| None</code> | For authorization use user API key. See details [here](https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication).<br>**Default**: <code>"Bearer <<apiKey>>"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SaleRep](maxio_advanced_billing/models/sale_rep.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Sites

> Source: [Sites](maxio_advanced_billing/apis/sites.py)

<details>
<summary><code>def clear_site(*, cleanup_scope: CleanupScopeOrStr | None = CleanupScope.ALL, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Clears all data from a test site asynchronously. This call is asynchronous and there may be a delay before the site data is fully deleted. If you are clearing site data for an automated test, you will need to build in a delay and/or check that there are no products, etc., in the site before proceeding.

**This functionality will only work on sites in TEST mode. Attempts to perform this on sites in “live” mode will result in a response of 403 FORBIDDEN.**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.sites.clear_site()
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.sites.clear_site()
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cleanup_scope</code> | <code>[CleanupScopeOrStr](maxio_advanced_billing/models/enums/cleanup_scope.py) \| None</code> | `all`: Will clear all products, customers, and related subscriptions from the site. <br>`customers`: Will clear only customers and related subscriptions (leaving the products untouched) for the site. <br>Revenue will also be reset to 0.<br>Use in query `cleanup_scope=all`.<br>**Default**: <code>CleanupScope.ALL</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_chargify_js_public_keys(*, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> ListPublicKeysResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists public keys used for Maxio.js (formerly Chargify.js).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sites.list_chargify_js_public_keys(page=1, per_page=50)
    # TODO: Handle 'response' of type ListPublicKeysResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sites.list_chargify_js_public_keys(page=1, per_page=50)
    # TODO: Handle 'response' of type ListPublicKeysResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListPublicKeysResponse](maxio_advanced_billing/models/list_public_keys_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_site(*, request_options: RequestOptionsOrDict | None = None) -> SiteResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves site data.

For more information, see [Sites](https://maxio.zendesk.com/hc/en-us/sections/24250550707085-Sites) in the product documentation. Specifically, the [Clearing Site Data](https://maxio.zendesk.com/hc/en-us/articles/24250617028365-Clearing-Site-Data) section is relevant to this endpoint.

#### Relationship invoicing enabled
If the site has Relationship invoicing enabled, additional properties are returned in the response:

``
"customer_hierarchy_enabled": true,
"whopays_enabled": true,
"whopays_default_payer": "self"
``

For more information, see [Who Pays & Customer Hierarchy](https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sites.read_site()
    # TODO: Handle 'response' of type SiteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sites.read_site()
    # TODO: Handle 'response' of type SiteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteResponse](maxio_advanced_billing/models/site_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionComponents

> Source: [SubscriptionComponents](maxio_advanced_billing/apis/subscription_components.py)

<details>
<summary><code>def activate_event_based_component(subscription_id: int, component_id: int, *, body: ActivateEventBasedComponent | ActivateEventBasedComponentDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Activates an event-based component for a single subscription.

To bill your subscribers on your Events data under the Events-Based Billing feature, the components must be activated for the subscriber.

For more information, see [Design Your Catalog](https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes).

Use this endpoint to activate an event-based component for a single subscription. Activating an event-based component causes billing for events when the subscription is renewed.

Note: it is possible to stream events for a subscription at any time, regardless of component activation status. The activation status only determines if the subscription should be billed for event-based component usage at renewal.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_components.activate_event_based_component(
        1,
        1,
        body=ActivateEventBasedComponent(
            price_point_id=1,
            billing_schedule=BillingSchedule(initial_billing_at=date(2022, 1, 1)),
            custom_price=ComponentCustomPrice(
                tax_included=False,
                pricing_scheme=PricingScheme.PER_UNIT,
                interval=30,
                interval_unit=IntervalUnit.DAY,
                prices=[Price(starting_quantity=1, ending_quantity=1, unit_price="5.0")],
            ),
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.subscription_components.activate_event_based_component(
        1,
        1,
        body=ActivateEventBasedComponent(
            price_point_id=1,
            billing_schedule=BillingSchedule(initial_billing_at=date(2022, 1, 1)),
            custom_price=ComponentCustomPrice(
                tax_included=False,
                pricing_scheme=PricingScheme.PER_UNIT,
                interval=30,
                interval_unit=IntervalUnit.DAY,
                prices=[Price(starting_quantity=1, ending_quantity=1, unit_price="5.0")],
            ),
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Advanced Billing id of the subscription |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>body</code> | <code>[ActivateEventBasedComponent](maxio_advanced_billing/models/activate_event_based_component.py) \| [ActivateEventBasedComponentDict](maxio_advanced_billing/models/activate_event_based_component.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def allocate_component(subscription_id: int, component_id: int, *, body: CreateAllocationRequest | CreateAllocationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AllocationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an allocation, sets the current allocated quantity for the component, and records a memo. Allocations can only be updated for Quantity, On/Off, and Prepaid Components.

When creating an allocation via the API, you can pass the `upgrade_charge`, `downgrade_credit`, and `accrue_charge` to be applied.

> **Note:** These proration and accrual fields are ignored for Prepaid Components since this component type always generates charges immediately without proration.

For information on prorated components and upgrade/downgrade schemes, see [Setting Component Allocations.](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration)

### Order of Resolution for upgrade_charge and downgrade_credit

1. Per allocation in API call (within a single allocation of the `allocations` array)
2. [Component-level default value](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview)
3. Allocation API call top level (outside of the `allocations` array)
4. [Site-level default value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)

### Order of Resolution for accrue charge

1. Allocation API call top level (outside of the `allocations` array)
2. [Site-level default value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)

> **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to either may cause the prorated charge/credit to be wrong.

For more information, see the [Component Allocations](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview) product Documentation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.allocate_component(
        1,
        1,
        body=CreateAllocationRequest(
            allocation=CreateAllocation(
                quantity=10,
                decimal_quantity="10.0",
                previous_quantity=5,
                decimal_previous_quantity="5.0",
                memo="Increase seats to 10",
                proration_downgrade_scheme="prorate",
                proration_upgrade_scheme="full-price-attempt-capture",
                downgrade_credit=DowngradeCreditCreditType.PRORATED,
                upgrade_charge=UpgradeChargeCreditType.FULL,
                accrue_charge=False,
                price_point_id=789,
                billing_schedule=BillingSchedule(initial_billing_at=date(2025, 2, 28)),
                custom_price=ComponentCustomPrice(
                    tax_included=False,
                    pricing_scheme=PricingScheme.PER_UNIT,
                    interval=1,
                    interval_unit=IntervalUnit.MONTH,
                    list_price_point_id=4321,
                    use_default_list_price=False,
                    prices=[Price(), Price()],
                    renew_prepaid_allocation=False,
                    rollover_prepaid_remainder=False,
                    expiration_interval=1,
                    expiration_interval_unit=ExpirationIntervalUnit.NEVER,
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type AllocationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllocateComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_components.allocate_component(
        1,
        1,
        body=CreateAllocationRequest(
            allocation=CreateAllocation(
                quantity=10,
                decimal_quantity="10.0",
                previous_quantity=5,
                decimal_previous_quantity="5.0",
                memo="Increase seats to 10",
                proration_downgrade_scheme="prorate",
                proration_upgrade_scheme="full-price-attempt-capture",
                downgrade_credit=DowngradeCreditCreditType.PRORATED,
                upgrade_charge=UpgradeChargeCreditType.FULL,
                accrue_charge=False,
                price_point_id=789,
                billing_schedule=BillingSchedule(initial_billing_at=date(2025, 2, 28)),
                custom_price=ComponentCustomPrice(
                    tax_included=False,
                    pricing_scheme=PricingScheme.PER_UNIT,
                    interval=1,
                    interval_unit=IntervalUnit.MONTH,
                    list_price_point_id=4321,
                    use_default_list_price=False,
                    prices=[Price(), Price()],
                    renew_prepaid_allocation=False,
                    rollover_prepaid_remainder=False,
                    expiration_interval=1,
                    expiration_interval_unit=ExpirationIntervalUnit.NEVER,
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type AllocationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllocateComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>body</code> | <code>[CreateAllocationRequest](maxio_advanced_billing/models/create_allocation_request.py) \| [CreateAllocationRequestDict](maxio_advanced_billing/models/create_allocation_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AllocationResponse](maxio_advanced_billing/models/allocation_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[AllocateComponentErrorBody](maxio_advanced_billing/errors/allocate_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def allocate_components(subscription_id: int, *, body: AllocateComponents | AllocateComponentsDict | None = None, request_options: RequestOptionsOrDict | None = None) -> list[AllocationResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates multiple allocations, sets the current allocated quantity for each of the components, and records a memo.   A `component_id` is required for each allocation.

The charges and/or credits that are created will be rolled up into a single total which is used to determine whether this is an upgrade or a downgrade.

### Order of Resolution for upgrade_charge and downgrade_credit

1. Per allocation in API call (within a single allocation of the `allocations` array)
2. [Component-level default value](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview)
3. Allocation API call top level (outside of the `allocations` array)
4. [Site-level default value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)

### Order of Resolution for accrue charge

1. Allocation API call top level (outside of the `allocations` array)
2. [Site-level default value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)

> **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to either may cause the prorated charge/credit to be wrong.

For more information, see the [Component Allocations](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview) product documentation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.allocate_components(
        1,
        body=AllocateComponents(
            proration_upgrade_scheme="prorate-attempt-capture",
            proration_downgrade_scheme="no-prorate",
            allocations=[
                CreateAllocation(quantity=10, component_id=123, memo="foo"),
                CreateAllocation(quantity=5, component_id=456, memo="bar"),
            ],
        ),
    )
    # TODO: Handle 'response' of type list[AllocationResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllocateComponentsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_components.allocate_components(
        1,
        body=AllocateComponents(
            proration_upgrade_scheme="prorate-attempt-capture",
            proration_downgrade_scheme="no-prorate",
            allocations=[
                CreateAllocation(quantity=10, component_id=123, memo="foo"),
                CreateAllocation(quantity=5, component_id=456, memo="bar"),
            ],
        ),
    )
    # TODO: Handle 'response' of type list[AllocationResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AllocateComponentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[AllocateComponents](maxio_advanced_billing/models/allocate_components.py) \| [AllocateComponentsDict](maxio_advanced_billing/models/allocate_components.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AllocationResponse](maxio_advanced_billing/models/allocation_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[AllocateComponentsErrorBody](maxio_advanced_billing/errors/allocate_components_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_record_events(api_handle: str, *, store_uid: str | None = None, body: list[EbbEvent | EbbEventDict] | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records a collection of events.

Note: this endpoint differs from the standard URL for this API in that `events` and your site subdomain are included in the path.

A maximum of 1000 events can be published in a single request. A 422 will be returned if this limit is exceeded.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_components.bulk_record_events("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.subscription_components.bulk_record_events("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_handle</code> | <code>str</code> | Identifies the Stream for which the events should be published. |
| <code>store_uid</code> | <code>str \| None</code> | If you've attached your own Keen project as an Advanced Billing event data-store, use this parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on Maxio Metering sites.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>list&#91;[EbbEvent](maxio_advanced_billing/models/ebb_event.py) \| [EbbEventDict](maxio_advanced_billing/models/ebb_event.py)&#93; \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_reset_subscription_components_price_points(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Resets all of a subscription's components to use the current default.

**Note**: this will update the price point for all of the subscription's components, even ones that have not been allocated yet.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.bulk_reset_subscription_components_price_points(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_components.bulk_reset_subscription_components_price_points(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_update_subscription_components_price_points(subscription_id: int, *, body: BulkComponentsPricePointAssignment | BulkComponentsPricePointAssignmentDict | None = None, request_options: RequestOptionsOrDict | None = None) -> BulkComponentsPricePointAssignment</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the price points on one or more of a subscription's components.

The `price_point` key can take either a:
1. Price point id (integer)
2. Price point handle (string)
3. `"_default"` string, which will reset the price point to the component's current default price point.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.bulk_update_subscription_components_price_points(
        1,
        body=BulkComponentsPricePointAssignment(
            components=[
                ComponentPricePointAssignment(component_id=997, price_point=1022),
                ComponentPricePointAssignment(component_id=998, price_point="wholesale-handle"),
                ComponentPricePointAssignment(component_id=999, price_point="_default"),
            ],
        ),
    )
    # TODO: Handle 'response' of type BulkComponentsPricePointAssignment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkUpdateSubscriptionComponentsPricePointsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_components.bulk_update_subscription_components_price_points(
        1,
        body=BulkComponentsPricePointAssignment(
            components=[
                ComponentPricePointAssignment(component_id=997, price_point=1022),
                ComponentPricePointAssignment(component_id=998, price_point="wholesale-handle"),
                ComponentPricePointAssignment(component_id=999, price_point="_default"),
            ],
        ),
    )
    # TODO: Handle 'response' of type BulkComponentsPricePointAssignment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkUpdateSubscriptionComponentsPricePointsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[BulkComponentsPricePointAssignment](maxio_advanced_billing/models/bulk_components_price_point_assignment.py) \| [BulkComponentsPricePointAssignmentDict](maxio_advanced_billing/models/bulk_components_price_point_assignment.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BulkComponentsPricePointAssignment](maxio_advanced_billing/models/bulk_components_price_point_assignment.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[BulkUpdateSubscriptionComponentsPricePointsErrorBody](maxio_advanced_billing/errors/bulk_update_subscription_components_price_points_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ComponentPricePointError1](maxio_advanced_billing/models/component_price_point_error1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_usage(subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict, component_id: ComponentIdModel | ComponentIdModelDict, *, body: CreateUsageRequest | CreateUsageRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UsageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records an instance of metered or prepaid usage for a subscription.

You can report metered or prepaid usage to Advanced Billing as often as you wish. You can report usage as it happens or periodically, such as each night or once per billing period. 

Full documentation on how to create Components in the Advanced Billing UI can be located [here](https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components). Additionally, for information on how to record component usage against a subscription, see the following resources:

It is not possible to record metered usage for more than one component at a time. Usage should be reported as one API call per component on a single subscription. For example, to record that a subscriber has sent both an SMS Message and an Email, send an API call for each.        

See the following product documentation articles for more information:

- [Create and Manage Components](https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components)
- [Recording Metered Component Usage](https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-metered-component-usage)
- [Reporting Prepaid Component Status](https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-prepaid-component-status)

The `quantity` from usage for each component is accumulated to the `unit_balance` on the [Component Line Item]($e/Subscription%20Components/readSubscriptionComponent) for the subscription.

## Price Point ID usage

If you are using price points, for metered and prepaid usage components Advanced Billing gives you the option to specify a price point in your request.

You do not need to specify a price point ID. If a price point is not included, the default price point for the component will be used when the usage is recorded.

## Deducting Usage

If you need to reverse a previous usage report or otherwise deduct from the current usage balance, you can provide a negative quantity.

Example:

Previously recorded quantity was 5000:

``json
{
  "usage": {
    "quantity": 5000,
    "memo": "Recording 5000 units"
  }
}
``

To reduce the quantity to `0`, POST the following payload:

``json
{
  "usage": {
    "quantity": -5000,
    "memo": "Deducting 5000 units"
  }
}
``
The `unit_balance` has a floor of `0`; negative unit balances are never allowed. For example, if the usage balance is 100 and you deduct 200 units, the unit balance would then be `0`, not `-100`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.create_usage(
        1, 1, body=CreateUsageRequest(usage=CreateUsage(quantity=1000, price_point_id="149416", memo="My memo"))
    )
    # TODO: Handle 'response' of type UsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateUsageErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_components.create_usage(
        1, 1, body=CreateUsageRequest(usage=CreateUsage(quantity=1000, price_point_id="149416", memo="My memo"))
    )
    # TODO: Handle 'response' of type UsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateUsageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id_or_reference</code> | <code>[SubscriptionIdOrReference](maxio_advanced_billing/models/unions/subscription_id_or_reference.py) \| [SubscriptionIdOrReferenceDict](maxio_advanced_billing/models/unions/subscription_id_or_reference.py)</code> | Either the Advanced Billing subscription ID (integer) or the subscription reference (string). Important: In cases where a numeric string value matches both an existing subscription ID and an existing subscription reference, the system will prioritize the subscription ID lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123" will return the subscription with ID 123. |
| <code>component_id</code> | <code>[ComponentIdModel](maxio_advanced_billing/models/unions/component_id_model.py) \| [ComponentIdModelDict](maxio_advanced_billing/models/unions/component_id_model.py)</code> | Either the Advanced Billing id for the component or the component's handle prefixed by `handle:` |
| <code>body</code> | <code>[CreateUsageRequest](maxio_advanced_billing/models/create_usage_request.py) \| [CreateUsageRequestDict](maxio_advanced_billing/models/create_usage_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsageResponse](maxio_advanced_billing/models/usage_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateUsageErrorBody](maxio_advanced_billing/errors/create_usage_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deactivate_event_based_component(subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deactivates an event-based component for a single subscription. Deactivating the event-based component causes Advanced Billing to ignore related events at subscription renewal.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_components.deactivate_event_based_component(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.subscription_components.deactivate_event_based_component(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Advanced Billing id of the subscription |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_prepaid_usage_allocation(subscription_id: int, component_id: int, allocation_id: int, *, body: CreditSchemeRequest | CreditSchemeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a prepaid usage allocation.

Prepaid Usage components are unique in that their allocations are always additive. In order to reduce a subscription's allocated quantity for a prepaid usage component, each allocation must be destroyed individually via this endpoint.

## Credit Scheme

By default, destroying an allocation will generate a service credit on the subscription. This behavior can be modified with the optional `credit_scheme` parameter on this endpoint. The accepted values are:

1. `none`: The allocation will be destroyed and the balances will be updated but no service credit or refund will be created.
2. `credit`: The allocation will be destroyed and the balances will be updated and a service credit will be generated. This is also the default behavior if the `credit_scheme` param is not passed.
3. `refund`: The allocation will be destroyed and the balances will be updated and a refund will be issued along with a Credit Note.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_components.delete_prepaid_usage_allocation(
        1, 1, 1, body=CreditSchemeRequest(credit_scheme=CreditScheme.NONE)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeletePrepaidUsageAllocationErrorBody
```

**Async**

```python
try:
    await async_client.subscription_components.delete_prepaid_usage_allocation(
        1, 1, 1, body=CreditSchemeRequest(credit_scheme=CreditScheme.NONE)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeletePrepaidUsageAllocationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>allocation_id</code> | <code>int</code> | The Advanced Billing id of the allocation |
| <code>body</code> | <code>[CreditSchemeRequest](maxio_advanced_billing/models/credit_scheme_request.py) \| [CreditSchemeRequestDict](maxio_advanced_billing/models/credit_scheme_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeletePrepaidUsageAllocationErrorBody](maxio_advanced_billing/errors/delete_prepaid_usage_allocation_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[SubscriptionComponentAllocationError1](maxio_advanced_billing/models/subscription_component_allocation_error1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_allocations(subscription_id: int, component_id: int, *, page: int | None = 1, request_options: RequestOptionsOrDict | None = None) -> list[AllocationResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the 50 most recent Allocations, ordered by most recent first.

## On/Off Components

When a subscription's on/off component has been toggled to on (`1`) or off (`0`), usage will be logged in this response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.list_allocations(1, 1, page=1)
    # TODO: Handle 'response' of type list[AllocationResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllocationsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_components.list_allocations(1, 1, page=1)
    # TODO: Handle 'response' of type list[AllocationResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllocationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AllocationResponse](maxio_advanced_billing/models/allocation_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListAllocationsErrorBody](maxio_advanced_billing/errors/list_allocations_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_components(subscription_id: int, *, date_field: SubscriptionListDateFieldOrStr | None = None, direction: SortingDirectionOrStr | None = None, filter_: ListSubscriptionComponentsFilter | ListSubscriptionComponentsFilterDict | None = None, end_date: str | None = None, end_datetime: str | None = None, price_point_ids: IncludeNotNullOrStr | None = None, product_family_ids: list[int] | None = None, sort: ListSubscriptionComponentsSortOrStr | None = None, start_date: str | None = None, start_datetime: str | None = None, include: list[ListSubscriptionComponentsIncludeOrStr] | None = None, in_use: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SubscriptionComponentResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists a subscription's applied components.

## Archived Components

When requesting to list components for a given subscription, if the subscription contains **archived** components they will be listed in the server response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.list_subscription_components(
        1,
        date_field=SubscriptionListDateField.UPDATED_AT,
        price_point_ids=IncludeNotNull.NOT_NULL,
        product_family_ids=[1, 2, 3],
        sort=ListSubscriptionComponentsSort.UPDATED_AT,
        include=[ListSubscriptionComponentsInclude.SUBSCRIPTION, ListSubscriptionComponentsInclude.HISTORIC_USAGES],
        in_use=True,
    )
    # TODO: Handle 'response' of type list[SubscriptionComponentResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_components.list_subscription_components(
        1,
        date_field=SubscriptionListDateField.UPDATED_AT,
        price_point_ids=IncludeNotNull.NOT_NULL,
        product_family_ids=[1, 2, 3],
        sort=ListSubscriptionComponentsSort.UPDATED_AT,
        include=[ListSubscriptionComponentsInclude.SUBSCRIPTION, ListSubscriptionComponentsInclude.HISTORIC_USAGES],
        in_use=True,
    )
    # TODO: Handle 'response' of type list[SubscriptionComponentResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>date_field</code> | <code>[SubscriptionListDateFieldOrStr](maxio_advanced_billing/models/enums/subscription_list_date_field.py) \| None</code> | The type of filter you'd like to apply to your search. Use in query `date_field=updated_at`.<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>filter_</code> | <code>[ListSubscriptionComponentsFilter](maxio_advanced_billing/models/list_subscription_components_filter.py) \| [ListSubscriptionComponentsFilterDict](maxio_advanced_billing/models/list_subscription_components_filter.py) \| None</code> | Filter to use for List Subscription Components operation<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of end_date.<br>**Default**: <code>None</code> |
| <code>price_point_ids</code> | <code>[IncludeNotNullOrStr](maxio_advanced_billing/models/enums/include_not_null.py) \| None</code> | Allows fetching components allocation only if price point id is present. Use in query `price_point_ids=not_null`.<br>**Default**: <code>None</code> |
| <code>product_family_ids</code> | <code>list&#91;int&#93; \| None</code> | Allows fetching components allocation with matching product family id based on provided ids. Use in query `product_family_ids=1,2,3`.<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[ListSubscriptionComponentsSortOrStr](maxio_advanced_billing/models/enums/list_subscription_components_sort.py) \| None</code> | The attribute by which to sort. Use in query `sort=updated_at`.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of start_date.<br>**Default**: <code>None</code> |
| <code>include</code> | <code>list&#91;[ListSubscriptionComponentsIncludeOrStr](maxio_advanced_billing/models/enums/list_subscription_components_include.py)&#93; \| None</code> | Allows including additional data in the response. Use in query `include=subscription,historic_usages`.<br>**Default**: <code>None</code> |
| <code>in_use</code> | <code>bool \| None</code> | If in_use is set to true, it returns only components that are currently in use. However, if it's set to false or not provided, it returns all components connected with the subscription.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SubscriptionComponentResponse](maxio_advanced_billing/models/subscription_component_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_components_for_site(*, page: int | None = 1, per_page: int | None = 20, sort: ListSubscriptionComponentsSortOrStr | None = None, direction: SortingDirectionOrStr | None = None, filter_: ListSubscriptionComponentsForSiteFilter | ListSubscriptionComponentsForSiteFilterDict | None = None, date_field: SubscriptionListDateFieldOrStr | None = None, start_date: str | None = None, start_datetime: str | None = None, end_date: str | None = None, end_datetime: str | None = None, subscription_ids: list[int] | None = None, price_point_ids: IncludeNotNullOrStr | None = None, product_family_ids: list[int] | None = None, include: ListSubscriptionComponentsIncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ListSubscriptionComponentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists components applied to each subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.list_subscription_components_for_site(
        page=1,
        per_page=50,
        sort=ListSubscriptionComponentsSort.UPDATED_AT,
        date_field=SubscriptionListDateField.UPDATED_AT,
        subscription_ids=[1, 2, 3],
        price_point_ids=IncludeNotNull.NOT_NULL,
        product_family_ids=[1, 2, 3],
        include=ListSubscriptionComponentsInclude.SUBSCRIPTION,
    )
    # TODO: Handle 'response' of type ListSubscriptionComponentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_components.list_subscription_components_for_site(
        page=1,
        per_page=50,
        sort=ListSubscriptionComponentsSort.UPDATED_AT,
        date_field=SubscriptionListDateField.UPDATED_AT,
        subscription_ids=[1, 2, 3],
        price_point_ids=IncludeNotNull.NOT_NULL,
        product_family_ids=[1, 2, 3],
        include=ListSubscriptionComponentsInclude.SUBSCRIPTION,
    )
    # TODO: Handle 'response' of type ListSubscriptionComponentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[ListSubscriptionComponentsSortOrStr](maxio_advanced_billing/models/enums/list_subscription_components_sort.py) \| None</code> | The attribute by which to sort. Use in query: `sort=updated_at`.<br>**Default**: <code>None</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>filter_</code> | <code>[ListSubscriptionComponentsForSiteFilter](maxio_advanced_billing/models/list_subscription_components_for_site_filter.py) \| [ListSubscriptionComponentsForSiteFilterDict](maxio_advanced_billing/models/list_subscription_components_for_site_filter.py) \| None</code> | Filter to use for List Subscription Components For Site operation<br>**Default**: <code>None</code> |
| <code>date_field</code> | <code>[SubscriptionListDateFieldOrStr](maxio_advanced_billing/models/enums/subscription_list_date_field.py) \| None</code> | The type of filter you'd like to apply to your search. Use in query: `date_field=updated_at`.<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>str \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in query `start_date=2011-12-15`.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>str \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of start_date. Use in query `start_datetime=2022-07-01 09:00:05`.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query `end_date=2011-12-16`.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>str \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns components with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead of end_date. Use in query `end_datetime=2022-07-01 09:00:05`.<br>**Default**: <code>None</code> |
| <code>subscription_ids</code> | <code>list&#91;int&#93; \| None</code> | Allows fetching components allocation with matching subscription id based on provided ids. Use in query `subscription_ids=1,2,3`.<br>**Default**: <code>None</code> |
| <code>price_point_ids</code> | <code>[IncludeNotNullOrStr](maxio_advanced_billing/models/enums/include_not_null.py) \| None</code> | Allows fetching components allocation only if price point id is present. Use in query `price_point_ids=not_null`.<br>**Default**: <code>None</code> |
| <code>product_family_ids</code> | <code>list&#91;int&#93; \| None</code> | Allows fetching components allocation with matching product family id based on provided ids. Use in query `product_family_ids=1,2,3`.<br>**Default**: <code>None</code> |
| <code>include</code> | <code>[ListSubscriptionComponentsIncludeOrStr](maxio_advanced_billing/models/enums/list_subscription_components_include.py) \| None</code> | Allows including additional data in the response. Use in query `include=subscription,historic_usages`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListSubscriptionComponentsResponse](maxio_advanced_billing/models/list_subscription_components_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_usages(subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict, component_id: ComponentIdModel | ComponentIdModelDict, *, since_id: int | None = None, max_id: int | None = None, since_date: Date | None = None, until_date: Date | None = None, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> list[UsageResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists usages associated with a subscription for a particular metered component. This will display the previously recorded components for a subscription.

This endpoint is not compatible with quantity-based components.

## Since Date and Until Date Usage

Note: The `since_date` and `until_date` attributes each default to midnight on the date specified. For example, in order to list usages for January 20th, you would need to append the following to the URL.

``
?since_date=2016-01-20&until_date=2016-01-21
``

## Read Usage by Handle

Use this endpoint to read the previously recorded components for a subscription.  You can now specify either the component id (integer) or the component handle prefixed by "handle:" to specify the unique identifier for the component you are working with.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.list_usages(1, 1, page=1, per_page=50)
    # TODO: Handle 'response' of type list[UsageResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_components.list_usages(1, 1, page=1, per_page=50)
    # TODO: Handle 'response' of type list[UsageResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id_or_reference</code> | <code>[SubscriptionIdOrReference](maxio_advanced_billing/models/unions/subscription_id_or_reference.py) \| [SubscriptionIdOrReferenceDict](maxio_advanced_billing/models/unions/subscription_id_or_reference.py)</code> | Either the Advanced Billing subscription ID (integer) or the subscription reference (string). Important: In cases where a numeric string value matches both an existing subscription ID and an existing subscription reference, the system will prioritize the subscription ID lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123" will return the subscription with ID 123. |
| <code>component_id</code> | <code>[ComponentIdModel](maxio_advanced_billing/models/unions/component_id_model.py) \| [ComponentIdModelDict](maxio_advanced_billing/models/unions/component_id_model.py)</code> | Either the Advanced Billing id for the component or the component's handle prefixed by `handle:` |
| <code>since_id</code> | <code>int \| None</code> | Returns usages with an id greater than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>max_id</code> | <code>int \| None</code> | Returns usages with an id less than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>since_date</code> | <code>Date \| None</code> | Returns usages with a created_at date greater than or equal to midnight (12:00 AM) on the date specified.<br>**Default**: <code>None</code> |
| <code>until_date</code> | <code>Date \| None</code> | Returns usages with a created_at date less than or equal to midnight (12:00 AM) on the date specified.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[UsageResponse](maxio_advanced_billing/models/usage_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_allocations(subscription_id: int, *, body: PreviewAllocationsRequest | PreviewAllocationsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AllocationPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Previews a potential subscription's **quantity-based** or **on/off** component allocation in the middle of the current billing period.  This is useful if you want users to be able to see the effect of a component operation before actually doing it.

## Fine-grained Component Control: Use with multiple `upgrade_charge`s or `downgrade_credits`

When the allocation uses multiple different types of `upgrade_charge`s or `downgrade_credit`s, the Allocation is viewed as an Allocation which uses "Fine-Grained Component Control". As a result, the response will not include `direction` and `proration` within the `allocation_preview`, but at the `line_items` and `allocations` level respectfully.

See example below for Fine-Grained Component Control response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.preview_allocations(
        1,
        body=PreviewAllocationsRequest(
            allocations=[
                CreateAllocation(
                    quantity=10,
                    component_id=554108,
                    memo="NOW",
                    proration_downgrade_scheme="prorate",
                    proration_upgrade_scheme="prorate-attempt-capture",
                    price_point_id=325826,
                ),
            ],
            effective_proration_date=date(2023, 11, 1),
        ),
    )
    # TODO: Handle 'response' of type AllocationPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewAllocationsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_components.preview_allocations(
        1,
        body=PreviewAllocationsRequest(
            allocations=[
                CreateAllocation(
                    quantity=10,
                    component_id=554108,
                    memo="NOW",
                    proration_downgrade_scheme="prorate",
                    proration_upgrade_scheme="prorate-attempt-capture",
                    price_point_id=325826,
                ),
            ],
            effective_proration_date=date(2023, 11, 1),
        ),
    )
    # TODO: Handle 'response' of type AllocationPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewAllocationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[PreviewAllocationsRequest](maxio_advanced_billing/models/preview_allocations_request.py) \| [PreviewAllocationsRequestDict](maxio_advanced_billing/models/preview_allocations_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AllocationPreviewResponse](maxio_advanced_billing/models/allocation_preview_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PreviewAllocationsErrorBody](maxio_advanced_billing/errors/preview_allocations_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ComponentAllocationError1](maxio_advanced_billing/models/component_allocation_error1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_subscription_component(subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None) -> SubscriptionComponentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information for a specific component on a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_components.read_subscription_component(1, 1)
    # TODO: Handle 'response' of type SubscriptionComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadSubscriptionComponentErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_components.read_subscription_component(1, 1)
    # TODO: Handle 'response' of type SubscriptionComponentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadSubscriptionComponentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component. Alternatively, the component's handle prefixed by `handle:` |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionComponentResponse](maxio_advanced_billing/models/subscription_component_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadSubscriptionComponentErrorBody](maxio_advanced_billing/errors/read_subscription_component_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def record_event(api_handle: str, *, store_uid: str | None = None, body: EbbEvent | EbbEventDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records a single event for Events-Based Billing.

Events-Based Billing is an evolved form of metered billing that is based on data-rich events streamed in real-time from your system to Advanced Billing.

These events can then be transformed, enriched, or analyzed to form the computed totals of usage charges billed to your customers.

This API allows you to stream events into the Advanced Billing data ingestion engine.

For more information, see [Design Your Catalog](https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes).

Note: this endpoint differs from the standard URL for this API in that `events` and your site subdomain are included in the path. For example:

``
https://events.chargify.com/my-site-subdomain/events/my-stream-api-handle
``

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_components.record_event(
        "some example string",
        body=EbbEvent(
            chargify=ChargifyEbb(timestamp=datetime(2020, 2, 27, 22, 45, 50, tzinfo=timezone.utc), subscription_id=1)
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.subscription_components.record_event(
        "some example string",
        body=EbbEvent(
            chargify=ChargifyEbb(timestamp=datetime(2020, 2, 27, 22, 45, 50, tzinfo=timezone.utc), subscription_id=1)
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_handle</code> | <code>str</code> | Identifies the Stream for which the event should be published. |
| <code>store_uid</code> | <code>str \| None</code> | If you've attached your own Keen project as an Advanced Billing event data-store, use this parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on Maxio Metering sites.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[EbbEvent](maxio_advanced_billing/models/ebb_event.py) \| [EbbEventDict](maxio_advanced_billing/models/ebb_event.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_prepaid_usage_allocation_expiration_date(subscription_id: int, component_id: int, allocation_id: int, *, body: UpdateAllocationExpirationDate | UpdateAllocationExpirationDateDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the expiration date for a prepaid usage allocation. This expiration date can be changed after the fact to allow for extending or shortening the allocation's active window.

In order to change a prepaid usage allocation's expiration date, a PUT call must be made to the allocation's endpoint with a new expiration date.

## Limitations

A few limitations exist when changing an allocation's expiration date:

- An expiration date can only be changed for an allocation that belongs to a price point with expiration interval options explicitly set.
- An expiration date can be changed towards the future with no limitations.
- An expiration date can be changed towards the past (essentially expiring it) up to the subscription's current period beginning date.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_components.update_prepaid_usage_allocation_expiration_date(
        1,
        1,
        1,
        body=UpdateAllocationExpirationDate(
            allocation=AllocationExpirationDate(expires_at=datetime(2021, 5, 5, 16, 0, 0, tzinfo=timezone.utc))
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdatePrepaidUsageAllocationExpirationDateErrorBody
```

**Async**

```python
try:
    await async_client.subscription_components.update_prepaid_usage_allocation_expiration_date(
        1,
        1,
        1,
        body=UpdateAllocationExpirationDate(
            allocation=AllocationExpirationDate(expires_at=datetime(2021, 5, 5, 16, 0, 0, tzinfo=timezone.utc))
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdatePrepaidUsageAllocationExpirationDateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>component_id</code> | <code>int</code> | The Advanced Billing id of the component |
| <code>allocation_id</code> | <code>int</code> | The Advanced Billing id of the allocation |
| <code>body</code> | <code>[UpdateAllocationExpirationDate](maxio_advanced_billing/models/update_allocation_expiration_date.py) \| [UpdateAllocationExpirationDateDict](maxio_advanced_billing/models/update_allocation_expiration_date.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdatePrepaidUsageAllocationExpirationDateErrorBody](maxio_advanced_billing/errors/update_prepaid_usage_allocation_expiration_date_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[SubscriptionComponentAllocationError1](maxio_advanced_billing/models/subscription_component_allocation_error1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionGroupInvoiceAccount

> Source: [SubscriptionGroupInvoiceAccount](maxio_advanced_billing/apis/subscription_group_invoice_account.py)

<details>
<summary><code>def create_subscription_group_prepayment(uid: str, *, body: SubscriptionGroupPrepaymentRequest | SubscriptionGroupPrepaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionGroupPrepaymentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a prepayment for a subscription group. This endpoint requires an `amount`, `details`, `method`, and `memo`. On success, the prepayment will be added to the group's prepayment balance.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_group_invoice_account.create_subscription_group_prepayment("some example string")
    # TODO: Handle 'response' of type SubscriptionGroupPrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionGroupPrepaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_group_invoice_account.create_subscription_group_prepayment(
        "some example string"
    )
    # TODO: Handle 'response' of type SubscriptionGroupPrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionGroupPrepaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>body</code> | <code>[SubscriptionGroupPrepaymentRequest](maxio_advanced_billing/models/subscription_group_prepayment_request.py) \| [SubscriptionGroupPrepaymentRequestDict](maxio_advanced_billing/models/subscription_group_prepayment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionGroupPrepaymentResponse](maxio_advanced_billing/models/subscription_group_prepayment_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateSubscriptionGroupPrepaymentErrorBody](maxio_advanced_billing/errors/create_subscription_group_prepayment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deduct_subscription_group_service_credit(uid: str, *, body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ServiceCredit</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deducts service credit for a subscription group. Credit will be deducted from the group in the amount specified in the request body.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_group_invoice_account.deduct_subscription_group_service_credit(
        "some example string",
        body=DeductServiceCreditRequest(deduction=DeductServiceCredit(amount=10, memo="Deduct from group account")),
    )
    # TODO: Handle 'response' of type ServiceCredit
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeductSubscriptionGroupServiceCreditErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_group_invoice_account.deduct_subscription_group_service_credit(
        "some example string",
        body=DeductServiceCreditRequest(deduction=DeductServiceCredit(amount=10, memo="Deduct from group account")),
    )
    # TODO: Handle 'response' of type ServiceCredit
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeductSubscriptionGroupServiceCreditErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>body</code> | <code>[DeductServiceCreditRequest](maxio_advanced_billing/models/deduct_service_credit_request.py) \| [DeductServiceCreditRequestDict](maxio_advanced_billing/models/deduct_service_credit_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ServiceCredit](maxio_advanced_billing/models/service_credit.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeductSubscriptionGroupServiceCreditErrorBody](maxio_advanced_billing/errors/deduct_subscription_group_service_credit_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issue_subscription_group_service_credit(uid: str, *, body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ServiceCreditResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Issues service credit for a subscription group. Credit will be added to the group in the amount specified in the request body. The credit will be applied to group member invoices as they are generated.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_group_invoice_account.issue_subscription_group_service_credit(
        "some example string",
        body=IssueServiceCreditRequest(service_credit=IssueServiceCredit(amount=10, memo="Credit the group account")),
    )
    # TODO: Handle 'response' of type ServiceCreditResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueSubscriptionGroupServiceCreditErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_group_invoice_account.issue_subscription_group_service_credit(
        "some example string",
        body=IssueServiceCreditRequest(service_credit=IssueServiceCredit(amount=10, memo="Credit the group account")),
    )
    # TODO: Handle 'response' of type ServiceCreditResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueSubscriptionGroupServiceCreditErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>body</code> | <code>[IssueServiceCreditRequest](maxio_advanced_billing/models/issue_service_credit_request.py) \| [IssueServiceCreditRequestDict](maxio_advanced_billing/models/issue_service_credit_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ServiceCreditResponse](maxio_advanced_billing/models/service_credit_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[IssueSubscriptionGroupServiceCreditErrorBody](maxio_advanced_billing/errors/issue_subscription_group_service_credit_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_prepayments_for_subscription_group(uid: str, *, page: int | None = 1, per_page: int | None = 20, filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ListSubscriptionGroupPrepaymentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists a subscription group's prepayments.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_group_invoice_account.list_prepayments_for_subscription_group(
        "some example string", page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListSubscriptionGroupPrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPrepaymentsForSubscriptionGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_group_invoice_account.list_prepayments_for_subscription_group(
        "some example string", page=1, per_page=50
    )
    # TODO: Handle 'response' of type ListSubscriptionGroupPrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPrepaymentsForSubscriptionGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>filter_</code> | <code>[ListPrepaymentsFilter](maxio_advanced_billing/models/list_prepayments_filter.py) \| [ListPrepaymentsFilterDict](maxio_advanced_billing/models/list_prepayments_filter.py) \| None</code> | Filter to use for List Prepayments operations<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListSubscriptionGroupPrepaymentResponse](maxio_advanced_billing/models/list_subscription_group_prepayment_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListPrepaymentsForSubscriptionGroupErrorBody](maxio_advanced_billing/errors/list_prepayments_for_subscription_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionGroupStatus

> Source: [SubscriptionGroupStatus](maxio_advanced_billing/apis/subscription_group_status.py)

<details>
<summary><code>def cancel_delayed_cancellation_for_group(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes the delayed cancellation on a subscription group.

Removing the delayed cancellation on a subscription group will ensure that the subscriptions do not get canceled at the end of the period. The request will reset the `cancel_at_end_of_period` flag to false on each member in the group.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_group_status.cancel_delayed_cancellation_for_group("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelDelayedCancellationForGroupErrorBody
```

**Async**

```python
try:
    await async_client.subscription_group_status.cancel_delayed_cancellation_for_group("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelDelayedCancellationForGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CancelDelayedCancellationForGroupErrorBody](maxio_advanced_billing/errors/cancel_delayed_cancellation_for_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_subscriptions_in_group(uid: str, *, body: CancelGroupedSubscriptionsRequest | CancelGroupedSubscriptionsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels all subscriptions within the specified group immediately. The group is identified by the `uid` that is passed in the URL. To successfully cancel the group, the primary subscription must be on automatic billing. The group members must be on automatic billing or prepaid.

To cancel a subscription group while also charging for any unbilled usage on metered or prepaid components, the `charge_unbilled_usage=true` parameter must be included in the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_group_status.cancel_subscriptions_in_group(
        "some example string", body=CancelGroupedSubscriptionsRequest(charge_unbilled_usage=True)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSubscriptionsInGroupErrorBody
```

**Async**

```python
try:
    await async_client.subscription_group_status.cancel_subscriptions_in_group(
        "some example string", body=CancelGroupedSubscriptionsRequest(charge_unbilled_usage=True)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSubscriptionsInGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>body</code> | <code>[CancelGroupedSubscriptionsRequest](maxio_advanced_billing/models/cancel_grouped_subscriptions_request.py) \| [CancelGroupedSubscriptionsRequestDict](maxio_advanced_billing/models/cancel_grouped_subscriptions_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CancelSubscriptionsInGroupErrorBody](maxio_advanced_billing/errors/cancel_subscriptions_in_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def initiate_delayed_cancellation_for_group(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules all subscriptions within the specified group to be canceled at the end of their billing period. The group is identified by its uid passed in the URL.

All subscriptions in the group must be on automatic billing in order to successfully cancel them, and the group must not be in a "past_due" state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_group_status.initiate_delayed_cancellation_for_group("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InitiateDelayedCancellationForGroupErrorBody
```

**Async**

```python
try:
    await async_client.subscription_group_status.initiate_delayed_cancellation_for_group("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InitiateDelayedCancellationForGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[InitiateDelayedCancellationForGroupErrorBody](maxio_advanced_billing/errors/initiate_delayed_cancellation_for_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reactivate_subscription_group(uid: str, *, body: ReactivateSubscriptionGroupRequest | ReactivateSubscriptionGroupRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ReactivateSubscriptionGroupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reactivates or resumes a cancelled subscription group. Upon reactivation, any canceled invoices created after the beginning of the primary subscription's billing period will be reopened and payment will be attempted on them. If the subscription group is being reactivated (as opposed to resumed), new charges will also be assessed for the new billing period.

Whether a subscription group is reactivated (a new billing period is created) or resumed (the current billing period is respected) will depend on the parameters that are sent with the request as well as the date of the request relative to the primary subscription's period.

## Reactivating within the current period

If a subscription group is cancelled and reactivated within the primary subscription's current period, we can choose to either start a new billing period or maintain the existing one. If we want to maintain the existing billing period, the `resume=true` option must be passed in request parameters.

An exception to the above are subscriptions that are on calendar billing. These subscriptions cannot be reactivated within the current period. If the `resume=true` option is not passed, the request will return an error.

The `resume_members` option is ignored in this case. All eligible group members will be automatically resumed.


## Reactivating beyond the current period

In this case, a subscription group can only be reactivated with a new billing period. If the `resume=true` option is passed it will be ignored.

Member subscriptions can have billing periods that are longer than the primary (e.g. a monthly primary with annual group members). If the primary subscription in a group cannot be reactivated within the current period, but other group members can be, passing `resume_members=true` will resume the existing billing period for eligible group members. The primary subscription will begin a new billing period.

For calendar billing subscriptions, the new billing period created will be a partial one, spanning from the date of reactivation to the next corresponding calendar renewal date.

## 3D Secure (3DS) Authentication post-authentication flow

When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will direct the customer through 3DS Authentication. 

See the [3D Secure Post-Authentication Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow) article in the product documentation to learn how to manage the redirect flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_group_status.reactivate_subscription_group(
        "some example string", body=ReactivateSubscriptionGroupRequest(resume=True)
    )
    # TODO: Handle 'response' of type ReactivateSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReactivateSubscriptionGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_group_status.reactivate_subscription_group(
        "some example string", body=ReactivateSubscriptionGroupRequest(resume=True)
    )
    # TODO: Handle 'response' of type ReactivateSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReactivateSubscriptionGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>body</code> | <code>[ReactivateSubscriptionGroupRequest](maxio_advanced_billing/models/reactivate_subscription_group_request.py) \| [ReactivateSubscriptionGroupRequestDict](maxio_advanced_billing/models/reactivate_subscription_group_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReactivateSubscriptionGroupResponse](maxio_advanced_billing/models/reactivate_subscription_group_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReactivateSubscriptionGroupErrorBody](maxio_advanced_billing/errors/reactivate_subscription_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionGroups

> Source: [SubscriptionGroups](maxio_advanced_billing/apis/subscription_groups.py)

<details>
<summary><code>def add_subscription_to_group(subscription_id: int, *, body: AddSubscriptionToAGroup | AddSubscriptionToAGroupDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionGroupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds an existing subscription to a subscription group. For sites making use of the [Relationship Billing](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview) and [Customer Hierarchy](https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies) features, it is possible to add existing subscriptions to subscription groups.

Passing `group` parameters with a `target` containing a `type` and optional `id` is all that's needed. When the `target` parameter specifies a `"customer"` or `"subscription"` that is already part of a hierarchy, the subscription will become a member of the customer's subscription group.  If the target customer or subscription is not part of a subscription group, a new group will be created and the subscription will become part of the group with the specified target customer set as the responsible payer for the group's subscriptions.

**Note:** In order to add an existing subscription to a subscription group, it must belong to either the same customer record as the target, or be within the same customer hierarchy.

Rather than specifying a customer, the `target` parameter could instead simply have a value of
* `"self"` which indicates the subscription will be paid for not by some other customer, but by the subscribing customer,
* `"parent"` which indicates the subscription will be paid for by the subscribing customer's parent within a customer hierarchy, or
* `"eldest"` which indicates the subscription will be paid for by the root-level customer in the subscribing customer's hierarchy.

To create a new subscription into a subscription group, reference the following:
[Create Subscription in a Subscription Group](https://developers.chargify.com/docs/api-docs/d571659cf0f24-create-subscription#subscription-in-a-subscription-group)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.add_subscription_to_group(
        1,
        body=AddSubscriptionToAGroup(
            group=GroupSettings(
                target=GroupTarget(type_=GroupTargetType.SUBSCRIPTION, id=32987),
                billing=GroupBilling(accrue=True, align_date=True, prorate=True),
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_groups.add_subscription_to_group(
        1,
        body=AddSubscriptionToAGroup(
            group=GroupSettings(
                target=GroupTarget(type_=GroupTargetType.SUBSCRIPTION, id=32987),
                billing=GroupBilling(accrue=True, align_date=True, prorate=True),
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[AddSubscriptionToAGroup](maxio_advanced_billing/models/add_subscription_to_a_group.py) \| [AddSubscriptionToAGroupDict](maxio_advanced_billing/models/add_subscription_to_a_group.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionGroupResponse](maxio_advanced_billing/models/subscription_group_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_subscription_group(*, body: CreateSubscriptionGroupRequest | CreateSubscriptionGroupRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionGroupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a subscription group with given members.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.create_subscription_group(
        body=CreateSubscriptionGroupRequest(
            subscription_group=CreateSubscriptionGroup(subscription_id=1, member_ids=[2, 3, 4])
        ),
    )
    # TODO: Handle 'response' of type SubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_groups.create_subscription_group(
        body=CreateSubscriptionGroupRequest(
            subscription_group=CreateSubscriptionGroup(subscription_id=1, member_ids=[2, 3, 4])
        ),
    )
    # TODO: Handle 'response' of type SubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateSubscriptionGroupRequest](maxio_advanced_billing/models/create_subscription_group_request.py) \| [CreateSubscriptionGroupRequestDict](maxio_advanced_billing/models/create_subscription_group_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionGroupResponse](maxio_advanced_billing/models/subscription_group_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateSubscriptionGroupErrorBody](maxio_advanced_billing/errors/create_subscription_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SubscriptionGroupCreateErrorResponse1](maxio_advanced_billing/models/subscription_group_create_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription_group(uid: str, *, request_options: RequestOptionsOrDict | None = None) -> DeleteSubscriptionGroupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a subscription group.
 Only groups without members can be deleted.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.delete_subscription_group("some example string")
    # TODO: Handle 'response' of type DeleteSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteSubscriptionGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_groups.delete_subscription_group("some example string")
    # TODO: Handle 'response' of type DeleteSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteSubscriptionGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DeleteSubscriptionGroupResponse](maxio_advanced_billing/models/delete_subscription_group_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteSubscriptionGroupErrorBody](maxio_advanced_billing/errors/delete_subscription_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_subscription_group(subscription_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FullSubscriptionGroupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Finds the subscription group associated with a subscription.

If the subscription is not in a group, this endpoint returns an error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.find_subscription_group("some example string")
    # TODO: Handle 'response' of type FullSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FindSubscriptionGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_groups.find_subscription_group("some example string")
    # TODO: Handle 'response' of type FullSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FindSubscriptionGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The Advanced Billing id of the subscription associated with the subscription group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FullSubscriptionGroupResponse](maxio_advanced_billing/models/full_subscription_group_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[FindSubscriptionGroupErrorBody](maxio_advanced_billing/errors/find_subscription_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_groups(*, page: int | None = 1, per_page: int | None = 20, include: list[SubscriptionGroupsListIncludeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ListSubscriptionGroupsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists subscription groups for the site. The response is paginated and will return a `meta` key with pagination information.

#### Account Balance Information

Account balance information for the subscription groups is not returned by default. If this information is desired, the `include[]=account_balances` parameter must be provided with the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.list_subscription_groups(
        page=1, per_page=50, include=[SubscriptionGroupsListInclude.ACCOUNT_BALANCES]
    )
    # TODO: Handle 'response' of type ListSubscriptionGroupsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_groups.list_subscription_groups(
        page=1, per_page=50, include=[SubscriptionGroupsListInclude.ACCOUNT_BALANCES]
    )
    # TODO: Handle 'response' of type ListSubscriptionGroupsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>include</code> | <code>list&#91;[SubscriptionGroupsListIncludeOrStr](maxio_advanced_billing/models/enums/subscription_groups_list_include.py)&#93; \| None</code> | A list of additional information to include in the response. The following values are supported:<br><br>- `account_balances`: Account balance information for the subscription groups. Use in query: `include[]=account_balances`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListSubscriptionGroupsResponse](maxio_advanced_billing/models/list_subscription_groups_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_subscription_group(uid: str, *, include: list[SubscriptionGroupIncludeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> FullSubscriptionGroupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns subscription group details.

#### Current Billing Amount in Cents

Current billing amount for the subscription group is not returned by default. If this information is desired, the `include[]=current_billing_amount_in_cents` parameter must be provided with the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.read_subscription_group(
        "some example string", include=[SubscriptionGroupInclude.CURRENT_BILLING_AMOUNT_IN_CENTS]
    )
    # TODO: Handle 'response' of type FullSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_groups.read_subscription_group(
        "some example string", include=[SubscriptionGroupInclude.CURRENT_BILLING_AMOUNT_IN_CENTS]
    )
    # TODO: Handle 'response' of type FullSubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>include</code> | <code>list&#91;[SubscriptionGroupIncludeOrStr](maxio_advanced_billing/models/enums/subscription_group_include.py)&#93; \| None</code> | Allows including additional data in the response. Use in query: `include[]=current_billing_amount_in_cents`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FullSubscriptionGroupResponse](maxio_advanced_billing/models/full_subscription_group_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_subscription_from_group(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes an existing subscription from a subscription group. For sites making use of the [Relationship Billing](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview) and [Customer Hierarchy](https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies) features, it is possible to remove an existing subscription from a subscription group.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_groups.remove_subscription_from_group(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveSubscriptionFromGroupErrorBody
```

**Async**

```python
try:
    await async_client.subscription_groups.remove_subscription_from_group(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveSubscriptionFromGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RemoveSubscriptionFromGroupErrorBody](maxio_advanced_billing/errors/remove_subscription_from_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signup_with_subscription_group(*, body: SubscriptionGroupSignupRequest | SubscriptionGroupSignupRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionGroupSignupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates multiple subscriptions at once under the same customer and consolidates them into a subscription group.

You must provide one and only one of the `payer_id`/`payer_reference`/`payer_attributes` for the customer attached to the group.

You must provide one and only one of the `payment_profile_id`/`credit_card_attributes`/`bank_account_attributes` for the payment profile attached to the group.

Only one of the `subscriptions` can have `"primary": true` attribute set.

When passing a product to a subscription you can use either `product_id` or `product_handle` or `offer_id`. You can also use `custom_price` instead.
The subscription request examples below will be split into two sections.
The first section, "Subscription Customization", will focus on passing different information with a subscription, such as components, calendar billing, and custom fields. These examples will presume you are using a secure chargify_token generated by Maxio.js (formerly Chargify.js).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.signup_with_subscription_group(
        body=SubscriptionGroupSignupRequest(
            subscription_group=SubscriptionGroupSignup(
                payment_profile_id=123,
                payer_id=123,
                subscriptions=[
                    SubscriptionGroupSignupItem(product_id=11, primary=True),
                    SubscriptionGroupSignupItem(product_id=12),
                    SubscriptionGroupSignupItem(product_id=13),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionGroupSignupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SignupWithSubscriptionGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_groups.signup_with_subscription_group(
        body=SubscriptionGroupSignupRequest(
            subscription_group=SubscriptionGroupSignup(
                payment_profile_id=123,
                payer_id=123,
                subscriptions=[
                    SubscriptionGroupSignupItem(product_id=11, primary=True),
                    SubscriptionGroupSignupItem(product_id=12),
                    SubscriptionGroupSignupItem(product_id=13),
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionGroupSignupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SignupWithSubscriptionGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SubscriptionGroupSignupRequest](maxio_advanced_billing/models/subscription_group_signup_request.py) \| [SubscriptionGroupSignupRequestDict](maxio_advanced_billing/models/subscription_group_signup_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionGroupSignupResponse](maxio_advanced_billing/models/subscription_group_signup_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[SignupWithSubscriptionGroupErrorBody](maxio_advanced_billing/errors/signup_with_subscription_group_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SubscriptionGroupSignupErrorResponse1](maxio_advanced_billing/models/subscription_group_signup_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_subscription_group_members(uid: str, *, body: UpdateSubscriptionGroupRequest | UpdateSubscriptionGroupRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionGroupResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates subscription group members.
`"member_ids"` should contain an array of both subscription IDs to set as group members and subscription IDs already present in the groups. Not including them will result in removing them from the subscription group. To clean up members, just leave the array empty.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_groups.update_subscription_group_members(
        "some example string",
        body=UpdateSubscriptionGroupRequest(subscription_group=UpdateSubscriptionGroup(member_ids=[1, 2, 3])),
    )
    # TODO: Handle 'response' of type SubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSubscriptionGroupMembersErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_groups.update_subscription_group_members(
        "some example string",
        body=UpdateSubscriptionGroupRequest(subscription_group=UpdateSubscriptionGroup(member_ids=[1, 2, 3])),
    )
    # TODO: Handle 'response' of type SubscriptionGroupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSubscriptionGroupMembersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>uid</code> | <code>str</code> | The uid of the subscription group |
| <code>body</code> | <code>[UpdateSubscriptionGroupRequest](maxio_advanced_billing/models/update_subscription_group_request.py) \| [UpdateSubscriptionGroupRequestDict](maxio_advanced_billing/models/update_subscription_group_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionGroupResponse](maxio_advanced_billing/models/subscription_group_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateSubscriptionGroupMembersErrorBody](maxio_advanced_billing/errors/update_subscription_group_members_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SubscriptionGroupUpdateErrorResponse1](maxio_advanced_billing/models/subscription_group_update_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionInvoiceAccount

> Source: [SubscriptionInvoiceAccount](maxio_advanced_billing/apis/subscription_invoice_account.py)

<details>
<summary><code>def create_prepayment(subscription_id: int, *, body: CreatePrepaymentRequest | CreatePrepaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CreatePrepaymentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a prepayment for a subscription.

In order to specify a prepayment made against a subscription, specify the `amount, memo, details, method`.

When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected using the default credit card payment profile and applied to the prepayment account balance.  This is especially useful for manual replenishment of prepaid subscriptions.

Note that passing `amount_in_cents` is now allowed.

## 3D Secure (3DS) Authentication post-authentication flow

When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will direct the customer through 3DS Authentication. 

See the [3D Secure Post-Authentication Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow) article in the product documentation to learn how to manage the redirect flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_invoice_account.create_prepayment(
        1,
        body=CreatePrepaymentRequest(
            prepayment=CreatePrepayment(
                amount=100,
                details="John Doe signup for $100",
                memo="Signup for $100",
                method=CreatePrepaymentMethod.CHECK,
            ),
        ),
    )
    # TODO: Handle 'response' of type CreatePrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePrepaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_invoice_account.create_prepayment(
        1,
        body=CreatePrepaymentRequest(
            prepayment=CreatePrepayment(
                amount=100,
                details="John Doe signup for $100",
                memo="Signup for $100",
                method=CreatePrepaymentMethod.CHECK,
            ),
        ),
    )
    # TODO: Handle 'response' of type CreatePrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreatePrepaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[CreatePrepaymentRequest](maxio_advanced_billing/models/create_prepayment_request.py) \| [CreatePrepaymentRequestDict](maxio_advanced_billing/models/create_prepayment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreatePrepaymentResponse](maxio_advanced_billing/models/create_prepayment_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreatePrepaymentErrorBody](maxio_advanced_billing/errors/create_prepayment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[CreatePrepaymentErrorResponse](maxio_advanced_billing/models/unions/create_prepayment_error_response.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deduct_service_credit(subscription_id: int, *, body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deducts a service credit from the subscription in the specified amount. The credit amount being deducted must be equal to or less than the current credit balance.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_invoice_account.deduct_service_credit(
        1, body=DeductServiceCreditRequest(deduction=DeductServiceCredit(amount="1", memo="Deduction"))
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeductServiceCreditErrorBody
```

**Async**

```python
try:
    await async_client.subscription_invoice_account.deduct_service_credit(
        1, body=DeductServiceCreditRequest(deduction=DeductServiceCredit(amount="1", memo="Deduction"))
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeductServiceCreditErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[DeductServiceCreditRequest](maxio_advanced_billing/models/deduct_service_credit_request.py) \| [DeductServiceCreditRequestDict](maxio_advanced_billing/models/deduct_service_credit_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeductServiceCreditErrorBody](maxio_advanced_billing/errors/deduct_service_credit_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[DeductServiceCreditErrorResponse](maxio_advanced_billing/models/unions/deduct_service_credit_error_response.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def issue_service_credit(subscription_id: int, *, body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ServiceCredit</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a service credit to the subscription in the specified amount. The credit is subsequently applied to the next generated invoice.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_invoice_account.issue_service_credit(
        1, body=IssueServiceCreditRequest(service_credit=IssueServiceCredit(amount="1"))
    )
    # TODO: Handle 'response' of type ServiceCredit
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueServiceCreditErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_invoice_account.issue_service_credit(
        1, body=IssueServiceCreditRequest(service_credit=IssueServiceCredit(amount="1"))
    )
    # TODO: Handle 'response' of type ServiceCredit
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IssueServiceCreditErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[IssueServiceCreditRequest](maxio_advanced_billing/models/issue_service_credit_request.py) \| [IssueServiceCreditRequestDict](maxio_advanced_billing/models/issue_service_credit_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ServiceCredit](maxio_advanced_billing/models/service_credit.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[IssueServiceCreditErrorBody](maxio_advanced_billing/errors/issue_service_credit_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[IssueServiceCreditErrorResponse](maxio_advanced_billing/models/unions/issue_service_credit_error_response.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_prepayments(subscription_id: int, *, page: int | None = 1, per_page: int | None = 20, filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PrepaymentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists a subscription's prepayments.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_invoice_account.list_prepayments(1, page=1, per_page=50)
    # TODO: Handle 'response' of type PrepaymentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPrepaymentsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_invoice_account.list_prepayments(1, page=1, per_page=50)
    # TODO: Handle 'response' of type PrepaymentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPrepaymentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>filter_</code> | <code>[ListPrepaymentsFilter](maxio_advanced_billing/models/list_prepayments_filter.py) \| [ListPrepaymentsFilterDict](maxio_advanced_billing/models/list_prepayments_filter.py) \| None</code> | Filter to use for List Prepayments operations<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PrepaymentsResponse](maxio_advanced_billing/models/prepayments_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListPrepaymentsErrorBody](maxio_advanced_billing/errors/list_prepayments_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_service_credits(subscription_id: int, *, page: int | None = 1, per_page: int | None = 20, direction: SortingDirectionOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ListServiceCreditsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists a subscription's service credits.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_invoice_account.list_service_credits(1, page=1, per_page=50)
    # TODO: Handle 'response' of type ListServiceCreditsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListServiceCreditsErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_invoice_account.list_service_credits(1, page=1, per_page=50)
    # TODO: Handle 'response' of type ListServiceCreditsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListServiceCreditsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListServiceCreditsResponse](maxio_advanced_billing/models/list_service_credits_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListServiceCreditsErrorBody](maxio_advanced_billing/errors/list_service_credits_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_account_balances(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> AccountBalances</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the `balance_in_cents` of the Subscription's Pending Discount, Service Credit, and Prepayment accounts, as well as the sum of the Subscription's open, payable invoices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_invoice_account.read_account_balances(1)
    # TODO: Handle 'response' of type AccountBalances
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_invoice_account.read_account_balances(1)
    # TODO: Handle 'response' of type AccountBalances
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AccountBalances](maxio_advanced_billing/models/account_balances.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refund_prepayment(subscription_id: int, prepayment_id: int, *, body: RefundPrepaymentRequest | RefundPrepaymentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PrepaymentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Refunds a prepayment applied to a subscription, either fully or partially. The `prepayment_id` will be the account transaction ID of the original payment. The prepayment must have some amount remaining in order to be refunded.

The amount may be passed either as a decimal, with `amount`, or an integer in cents, with `amount_in_cents`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_invoice_account.refund_prepayment(1, 1)
    # TODO: Handle 'response' of type PrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundPrepaymentErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_invoice_account.refund_prepayment(1, 1)
    # TODO: Handle 'response' of type PrepaymentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundPrepaymentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>prepayment_id</code> | <code>int</code> | id of prepayment |
| <code>body</code> | <code>[RefundPrepaymentRequest](maxio_advanced_billing/models/refund_prepayment_request.py) \| [RefundPrepaymentRequestDict](maxio_advanced_billing/models/refund_prepayment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PrepaymentResponse](maxio_advanced_billing/models/prepayment_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RefundPrepaymentErrorBody](maxio_advanced_billing/errors/refund_prepayment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RefundPrepaymentBaseErrorsResponse1](maxio_advanced_billing/models/refund_prepayment_base_errors_response1.py)</code> |
| 404 | <code>str</code> |
| 422 | <code>[RefundPrepaymentErrorResponse](maxio_advanced_billing/models/unions/refund_prepayment_error_response.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionNotes

> Source: [SubscriptionNotes](maxio_advanced_billing/apis/subscription_notes.py)

<details>
<summary><code>def create_subscription_note(subscription_id: int, *, body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionNoteResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a note for a subscription.

Notes allow you to record information about a particular Subscription in a free text format.

If you have structured data such as birth date, color, etc., consider using [Metadata]($e/Custom%20Fields/createMetadata) instead.

For more information, see [Adding Notes](https://docs.maxio.com/hc/en-us/articles/24251654953997-Understanding-the-Subscription-Summary-Page#billing-portal-status:~:text=documentation%20for%20more.-,Adding%20Notes,-Notes%20are%20optional) in the product documentation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_notes.create_subscription_note(
        1, body=UpdateSubscriptionNoteRequest(note=UpdateSubscriptionNote(body="New test note.", sticky=True))
    )
    # TODO: Handle 'response' of type SubscriptionNoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionNoteErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_notes.create_subscription_note(
        1, body=UpdateSubscriptionNoteRequest(note=UpdateSubscriptionNote(body="New test note.", sticky=True))
    )
    # TODO: Handle 'response' of type SubscriptionNoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionNoteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[UpdateSubscriptionNoteRequest](maxio_advanced_billing/models/update_subscription_note_request.py) \| [UpdateSubscriptionNoteRequestDict](maxio_advanced_billing/models/update_subscription_note_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionNoteResponse](maxio_advanced_billing/models/subscription_note_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateSubscriptionNoteErrorBody](maxio_advanced_billing/errors/create_subscription_note_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription_note(subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a note for a Subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_notes.delete_subscription_note(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.subscription_notes.delete_subscription_note(1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>note_id</code> | <code>int</code> | The Advanced Billing id of the note |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_notes(subscription_id: int, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> list[SubscriptionNoteResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of notes associated with a subscription. The response will be an array of Notes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_notes.list_subscription_notes(1, page=1, per_page=50)
    # TODO: Handle 'response' of type list[SubscriptionNoteResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionNotesErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_notes.list_subscription_notes(1, page=1, per_page=50)
    # TODO: Handle 'response' of type list[SubscriptionNoteResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSubscriptionNotesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SubscriptionNoteResponse](maxio_advanced_billing/models/subscription_note_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListSubscriptionNotesErrorBody](maxio_advanced_billing/errors/list_subscription_notes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_subscription_note(subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None) -> SubscriptionNoteResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific note attached to a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_notes.read_subscription_note(1, 1)
    # TODO: Handle 'response' of type SubscriptionNoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_notes.read_subscription_note(1, 1)
    # TODO: Handle 'response' of type SubscriptionNoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>note_id</code> | <code>int</code> | The Advanced Billing id of the note |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionNoteResponse](maxio_advanced_billing/models/subscription_note_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_subscription_note(subscription_id: int, note_id: int, *, body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionNoteResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a note for a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_notes.update_subscription_note(
        1, 1, body=UpdateSubscriptionNoteRequest(note=UpdateSubscriptionNote(body="Modified test note.", sticky=True))
    )
    # TODO: Handle 'response' of type SubscriptionNoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSubscriptionNoteErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_notes.update_subscription_note(
        1, 1, body=UpdateSubscriptionNoteRequest(note=UpdateSubscriptionNote(body="Modified test note.", sticky=True))
    )
    # TODO: Handle 'response' of type SubscriptionNoteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSubscriptionNoteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>note_id</code> | <code>int</code> | The Advanced Billing id of the note |
| <code>body</code> | <code>[UpdateSubscriptionNoteRequest](maxio_advanced_billing/models/update_subscription_note_request.py) \| [UpdateSubscriptionNoteRequestDict](maxio_advanced_billing/models/update_subscription_note_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionNoteResponse](maxio_advanced_billing/models/subscription_note_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateSubscriptionNoteErrorBody](maxio_advanced_billing/errors/update_subscription_note_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionProducts

> Source: [SubscriptionProducts](maxio_advanced_billing/apis/subscription_products.py)

<details>
<summary><code>def migrate_subscription_product(subscription_id: int, *, body: SubscriptionProductMigrationRequest | SubscriptionProductMigrationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Migrates a subscription to a different product.

To create a migration, you must pass the `product_id` or `product_handle` in the object when you send a POST request. You can also pass either a `product_price_point_id` or `product_price_point_handle` to choose which price point the subscription is moved to. If no price point identifier is passed, the subscription is moved to the product's default price point. The response is the updated subscription.

## Valid Subscriptions

Subscriptions should be in the `active` or `trialing` state to be migrated.

(For backwards compatibility reasons, it is possible to migrate a subscription that is in the `trial_ended` state via the API, however this is not recommended.  Since `trial_ended` is an end-of-life state, the subscription should be canceled, the product changed, and then the subscription can be reactivated.)

For more information, see [Product Changes and Migrations](https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations).

## Failed Migrations

Important note: One of the most common ways that a migration can fail is when the attempt is made to migrate a subscription to its current product. 

## 3D Secure (3DS) Authentication post-authentication flow

When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will direct the customer through 3DS Authentication. 

See the [3D Secure Post-Authentication Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow) article in the product documentation to learn how to manage the redirect flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_products.migrate_subscription_product(
        1,
        body=SubscriptionProductMigrationRequest(
            migration=SubscriptionProductMigration(
                product_id=3801242,
                include_trial=False,
                include_initial_charge=False,
                include_coupons=True,
                preserve_period=True,
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MigrateSubscriptionProductErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_products.migrate_subscription_product(
        1,
        body=SubscriptionProductMigrationRequest(
            migration=SubscriptionProductMigration(
                product_id=3801242,
                include_trial=False,
                include_initial_charge=False,
                include_coupons=True,
                preserve_period=True,
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MigrateSubscriptionProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[SubscriptionProductMigrationRequest](maxio_advanced_billing/models/subscription_product_migration_request.py) \| [SubscriptionProductMigrationRequestDict](maxio_advanced_billing/models/subscription_product_migration_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[MigrateSubscriptionProductErrorBody](maxio_advanced_billing/errors/migrate_subscription_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_subscription_product_migration(subscription_id: int, *, body: SubscriptionMigrationPreviewRequest | SubscriptionMigrationPreviewRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionMigrationPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Previews the charges resulting from migrating a subscription to a different product.

## Previewing a future date
It is also possible to preview the migration for a date in the future, as long as it's still within the subscription's current billing period, by passing a `proration_date` along with the request (e.g., `"proration_date": "2020-12-18T18:25:43.511Z"`).

This will calculate the prorated adjustment, charge, payment and credit applied values assuming the migration is done at that date in the future as opposed to right now.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_products.preview_subscription_product_migration(1)
    # TODO: Handle 'response' of type SubscriptionMigrationPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewSubscriptionProductMigrationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_products.preview_subscription_product_migration(1)
    # TODO: Handle 'response' of type SubscriptionMigrationPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewSubscriptionProductMigrationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[SubscriptionMigrationPreviewRequest](maxio_advanced_billing/models/subscription_migration_preview_request.py) \| [SubscriptionMigrationPreviewRequestDict](maxio_advanced_billing/models/subscription_migration_preview_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionMigrationPreviewResponse](maxio_advanced_billing/models/subscription_migration_preview_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PreviewSubscriptionProductMigrationErrorBody](maxio_advanced_billing/errors/preview_subscription_product_migration_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionRenewals

> Source: [SubscriptionRenewals](maxio_advanced_billing/apis/subscription_renewals.py)

<details>
<summary><code>def cancel_scheduled_renewal_configuration(subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a scheduled renewal configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.cancel_scheduled_renewal_configuration(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelScheduledRenewalConfigurationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.cancel_scheduled_renewal_configuration(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelScheduledRenewalConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>id_</code> | <code>int</code> | The renewal id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CancelScheduledRenewalConfigurationErrorBody](maxio_advanced_billing/errors/cancel_scheduled_renewal_configuration_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_scheduled_renewal_configuration(subscription_id: int, *, body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a scheduled renewal configuration for a subscription. The scheduled renewal is based on the subscription’s current product and component setup.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.create_scheduled_renewal_configuration(
        1,
        body=ScheduledRenewalConfigurationRequest(
            renewal_configuration=ScheduledRenewalConfigurationRequestBody(
                starts_at=datetime(2024, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                ends_at=datetime(2025, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                lock_in_at=datetime(2024, 11, 15, 0, 0, 0, tzinfo=timezone.utc),
                contract_id=222,
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateScheduledRenewalConfigurationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.create_scheduled_renewal_configuration(
        1,
        body=ScheduledRenewalConfigurationRequest(
            renewal_configuration=ScheduledRenewalConfigurationRequestBody(
                starts_at=datetime(2024, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                ends_at=datetime(2025, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                lock_in_at=datetime(2024, 11, 15, 0, 0, 0, tzinfo=timezone.utc),
                contract_id=222,
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateScheduledRenewalConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[ScheduledRenewalConfigurationRequest](maxio_advanced_billing/models/scheduled_renewal_configuration_request.py) \| [ScheduledRenewalConfigurationRequestDict](maxio_advanced_billing/models/scheduled_renewal_configuration_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateScheduledRenewalConfigurationErrorBody](maxio_advanced_billing/errors/create_scheduled_renewal_configuration_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_scheduled_renewal_configuration_item(subscription_id: int, scheduled_renewals_configuration_id: int, *, body: ScheduledRenewalConfigurationItemRequest | ScheduledRenewalConfigurationItemRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds product and component line items to the scheduled renewal.

If your site has list vs sales pricing enabled, accepts renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral impact). This functionality is supported in the API, but is not currently supported in SDKs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.create_scheduled_renewal_configuration_item(
        1,
        1,
        body=ScheduledRenewalConfigurationItemRequest(
            renewal_configuration_item=ScheduledRenewalItemRequestBodyComponent(
                item_type="Component",
                item_id=57,
                quantity=1,
                custom_price=ScheduledRenewalComponentCustomPrice(
                    pricing_scheme=PricingScheme.STAIRSTEP, prices=[Price()]
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateScheduledRenewalConfigurationItemErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.create_scheduled_renewal_configuration_item(
        1,
        1,
        body=ScheduledRenewalConfigurationItemRequest(
            renewal_configuration_item=ScheduledRenewalItemRequestBodyComponent(
                item_type="Component",
                item_id=57,
                quantity=1,
                custom_price=ScheduledRenewalComponentCustomPrice(
                    pricing_scheme=PricingScheme.STAIRSTEP, prices=[Price()]
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateScheduledRenewalConfigurationItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>scheduled_renewals_configuration_id</code> | <code>int</code> | The scheduled renewal configuration id. |
| <code>body</code> | <code>[ScheduledRenewalConfigurationItemRequest](maxio_advanced_billing/models/scheduled_renewal_configuration_item_request.py) \| [ScheduledRenewalConfigurationItemRequestDict](maxio_advanced_billing/models/scheduled_renewal_configuration_item_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationItemResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_item_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateScheduledRenewalConfigurationItemErrorBody](maxio_advanced_billing/errors/create_scheduled_renewal_configuration_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_scheduled_renewal_configuration_item(subscription_id: int, scheduled_renewals_configuration_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes an item from the pending renewal configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscription_renewals.delete_scheduled_renewal_configuration_item(1, 1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteScheduledRenewalConfigurationItemErrorBody
```

**Async**

```python
try:
    await async_client.subscription_renewals.delete_scheduled_renewal_configuration_item(1, 1, 1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteScheduledRenewalConfigurationItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>scheduled_renewals_configuration_id</code> | <code>int</code> | The scheduled renewal configuration id. |
| <code>id_</code> | <code>int</code> | The scheduled renewal configuration item id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[DeleteScheduledRenewalConfigurationItemErrorBody](maxio_advanced_billing/errors/delete_scheduled_renewal_configuration_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_scheduled_renewal_configurations(subscription_id: int, *, status: StatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists scheduled renewal configurations for the subscription and permits an optional status query filter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.list_scheduled_renewal_configurations(1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.list_scheduled_renewal_configurations(1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>status</code> | <code>[StatusOrStr](maxio_advanced_billing/models/enums/status.py) \| None</code> | (Optional) Status filter for scheduled renewal configurations.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationsResponse](maxio_advanced_billing/models/scheduled_renewal_configurations_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def lock_in_scheduled_renewal_immediately(subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Locks in the renewal immediately.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.lock_in_scheduled_renewal_immediately(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LockInScheduledRenewalImmediatelyErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.lock_in_scheduled_renewal_immediately(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type LockInScheduledRenewalImmediatelyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>id_</code> | <code>int</code> | The renewal id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[LockInScheduledRenewalImmediatelyErrorBody](maxio_advanced_billing/errors/lock_in_scheduled_renewal_immediately_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_scheduled_renewal_configuration(subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the configuration settings for the scheduled renewal.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.read_scheduled_renewal_configuration(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.read_scheduled_renewal_configuration(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>id_</code> | <code>int</code> | The renewal id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_scheduled_renewal_lock_in(subscription_id: int, id_: int, *, body: ScheduledRenewalLockInRequest | ScheduledRenewalLockInRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a future lock-in date for the renewal.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.schedule_scheduled_renewal_lock_in(
        1, 1, body=ScheduledRenewalLockInRequest(lock_in_at=date(2025, 11, 15))
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleScheduledRenewalLockInErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.schedule_scheduled_renewal_lock_in(
        1, 1, body=ScheduledRenewalLockInRequest(lock_in_at=date(2025, 11, 15))
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleScheduledRenewalLockInErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>id_</code> | <code>int</code> | The renewal id. |
| <code>body</code> | <code>[ScheduledRenewalLockInRequest](maxio_advanced_billing/models/scheduled_renewal_lock_in_request.py) \| [ScheduledRenewalLockInRequestDict](maxio_advanced_billing/models/scheduled_renewal_lock_in_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ScheduleScheduledRenewalLockInErrorBody](maxio_advanced_billing/errors/schedule_scheduled_renewal_lock_in_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unpublish_scheduled_renewal_configuration(subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Restores a scheduled renewal configuration to an editable state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.unpublish_scheduled_renewal_configuration(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnpublishScheduledRenewalConfigurationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.unpublish_scheduled_renewal_configuration(1, 1)
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnpublishScheduledRenewalConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>id_</code> | <code>int</code> | The renewal id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UnpublishScheduledRenewalConfigurationErrorBody](maxio_advanced_billing/errors/unpublish_scheduled_renewal_configuration_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_scheduled_renewal_configuration(subscription_id: int, id_: int, *, body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.update_scheduled_renewal_configuration(
        1,
        1,
        body=ScheduledRenewalConfigurationRequest(
            renewal_configuration=ScheduledRenewalConfigurationRequestBody(
                starts_at=datetime(2025, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                ends_at=datetime(2026, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                lock_in_at=datetime(2025, 11, 15, 0, 0, 0, tzinfo=timezone.utc),
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateScheduledRenewalConfigurationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.update_scheduled_renewal_configuration(
        1,
        1,
        body=ScheduledRenewalConfigurationRequest(
            renewal_configuration=ScheduledRenewalConfigurationRequestBody(
                starts_at=datetime(2025, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                ends_at=datetime(2026, 12, 1, 0, 0, 0, tzinfo=timezone.utc),
                lock_in_at=datetime(2025, 11, 15, 0, 0, 0, tzinfo=timezone.utc),
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateScheduledRenewalConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>id_</code> | <code>int</code> | The renewal id. |
| <code>body</code> | <code>[ScheduledRenewalConfigurationRequest](maxio_advanced_billing/models/scheduled_renewal_configuration_request.py) \| [ScheduledRenewalConfigurationRequestDict](maxio_advanced_billing/models/scheduled_renewal_configuration_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateScheduledRenewalConfigurationErrorBody](maxio_advanced_billing/errors/update_scheduled_renewal_configuration_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_scheduled_renewal_configuration_item(subscription_id: int, scheduled_renewals_configuration_id: int, id_: int, *, body: ScheduledRenewalUpdateRequest | ScheduledRenewalUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ScheduledRenewalConfigurationItemResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing configuration item’s pricing and quantity.

If you site has list vs sales pricing enabled, accepts renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral impact). This functionality is supported in the API, but is not currently supported in SDKs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_renewals.update_scheduled_renewal_configuration_item(
        1,
        1,
        1,
        body=ScheduledRenewalUpdateRequest(
            renewal_configuration_item=ScheduledRenewalItemRequestBodyComponent(
                item_type="Component",
                item_id=57,
                quantity=2,
                custom_price=ScheduledRenewalComponentCustomPrice(
                    pricing_scheme=PricingScheme.STAIRSTEP, prices=[Price()]
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateScheduledRenewalConfigurationItemErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_renewals.update_scheduled_renewal_configuration_item(
        1,
        1,
        1,
        body=ScheduledRenewalUpdateRequest(
            renewal_configuration_item=ScheduledRenewalItemRequestBodyComponent(
                item_type="Component",
                item_id=57,
                quantity=2,
                custom_price=ScheduledRenewalComponentCustomPrice(
                    pricing_scheme=PricingScheme.STAIRSTEP, prices=[Price()]
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type ScheduledRenewalConfigurationItemResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateScheduledRenewalConfigurationItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>scheduled_renewals_configuration_id</code> | <code>int</code> | The scheduled renewal configuration id. |
| <code>id_</code> | <code>int</code> | The scheduled renewal configuration item id. |
| <code>body</code> | <code>[ScheduledRenewalUpdateRequest](maxio_advanced_billing/models/scheduled_renewal_update_request.py) \| [ScheduledRenewalUpdateRequestDict](maxio_advanced_billing/models/scheduled_renewal_update_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduledRenewalConfigurationItemResponse](maxio_advanced_billing/models/scheduled_renewal_configuration_item_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateScheduledRenewalConfigurationItemErrorBody](maxio_advanced_billing/errors/update_scheduled_renewal_configuration_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SubscriptionStatus

> Source: [SubscriptionStatus](maxio_advanced_billing/apis/subscription_status.py)

<details>
<summary><code>def cancel_delayed_cancellation(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> DelayedCancellationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes the delayed cancellation from a subscription, ensuring it is not canceled at the end of the current period. The request will reset the `cancel_at_end_of_period` flag to `false`.

This endpoint is idempotent. If the subscription was not set to cancel in the future, removing the delayed cancellation has no effect and the call will be successful.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.cancel_delayed_cancellation(1)
    # TODO: Handle 'response' of type DelayedCancellationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelDelayedCancellationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.cancel_delayed_cancellation(1)
    # TODO: Handle 'response' of type DelayedCancellationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelDelayedCancellationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DelayedCancellationResponse](maxio_advanced_billing/models/delayed_cancellation_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CancelDelayedCancellationErrorBody](maxio_advanced_billing/errors/cancel_delayed_cancellation_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_dunning(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels the active dunning process for a subscription and sets it to active.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.cancel_dunning(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelDunningErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.cancel_dunning(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelDunningErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CancelDunningErrorBody](maxio_advanced_billing/errors/cancel_dunning_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_subscription(subscription_id: int, *, body: CancellationRequest | CancellationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels the Subscription. The Delete method sets the Subscription state to `canceled`.
To cancel the subscription immediately, omit any schedule parameters from the request. To use the schedule options, the Schedule Subscription Cancellation feature must be enabled on your site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.cancel_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.cancel_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[CancellationRequest](maxio_advanced_billing/models/cancellation_request.py) \| [CancellationRequestDict](maxio_advanced_billing/models/cancellation_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CancelSubscriptionErrorBody](maxio_advanced_billing/errors/cancel_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[CancelSubscriptionErrorResponse](maxio_advanced_billing/models/unions/cancel_subscription_error_response.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def initiate_delayed_cancellation(subscription_id: int, *, body: CancellationRequest | CancellationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> DelayedCancellationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a subscription at the end of the current billing period based on the subscription's current product. You cannot set `cancel_at_end_of_period` at subscription creation, or if the subscription is past due.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.initiate_delayed_cancellation(1)
    # TODO: Handle 'response' of type DelayedCancellationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InitiateDelayedCancellationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.initiate_delayed_cancellation(1)
    # TODO: Handle 'response' of type DelayedCancellationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InitiateDelayedCancellationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[CancellationRequest](maxio_advanced_billing/models/cancellation_request.py) \| [CancellationRequestDict](maxio_advanced_billing/models/cancellation_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DelayedCancellationResponse](maxio_advanced_billing/models/delayed_cancellation_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[InitiateDelayedCancellationErrorBody](maxio_advanced_billing/errors/initiate_delayed_cancellation_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pause_subscription(subscription_id: int, *, body: PauseRequest | PauseRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Places the subscription on hold, preventing it from renewing.

## Limitations

You may not place a subscription on hold if the `next_billing_at` date is within 24 hours.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.pause_subscription(
        1,
        body=PauseRequest(
            hold=AutoResume(automatically_resume_at=datetime(2017, 5, 25, 11, 25, 0, tzinfo=timezone.utc))
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PauseSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.pause_subscription(
        1,
        body=PauseRequest(
            hold=AutoResume(automatically_resume_at=datetime(2017, 5, 25, 11, 25, 0, tzinfo=timezone.utc))
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PauseSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[PauseRequest](maxio_advanced_billing/models/pause_request.py) \| [PauseRequestDict](maxio_advanced_billing/models/pause_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PauseSubscriptionErrorBody](maxio_advanced_billing/errors/pause_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_renewal(subscription_id: int, *, body: RenewalPreviewRequest | RenewalPreviewRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> RenewalPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Previews a subscription’s next renewal assessment. Renewal Preview is an object representing a subscription’s next assessment. You can retrieve it to see a snapshot of how much your customer will be charged on their next renewal.

The "Next Billing" amount and "Next Billing" date are already represented in the UI on each Subscriber's Summary. For more information, see [Subscriber Interface Overview](https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview).

## Optional Component Fields

This endpoint is particularly useful because it returns the computed billing amount for the base product and the components which are in use by a subscriber.

By default, the preview includes billing details for all components _at their **current** quantities_. This means:

* Current `allocated_quantity` for quantity-based components
* Current enabled/disabled status for on/off components
* Current metered usage `unit_balance` for metered components
* Current metric quantity value for events recorded thus far for events-based components

In the above statements, "current" means the quantity or value as of the call to the renewal preview endpoint. End-of-period values for components are not predicted, so metered or events-based usage may be less than it will eventually be at the end of the period.

Optionally, **you can provide your own custom quantities** for any component to see a billing preview for non-current quantities. This is accomplished by sending a request body with data under the `components` key. See the request body documentation below.

## Preview Behavior

Sending a `POST` request to this endpoint returns preview data without modifying the subscription. This method previews data, but does not log any changes against a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.preview_renewal(
        1,
        body=RenewalPreviewRequest(
            components=[
                RenewalPreviewComponent(component_id=10708, quantity=10000),
                RenewalPreviewComponent(
                    component_id="handle:small-instance-hours", quantity=10000, price_point_id=8712
                ),
                RenewalPreviewComponent(
                    component_id="handle:large-instance-hours", quantity=100, price_point_id="handle:startup-pricing"
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type RenewalPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewRenewalErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.preview_renewal(
        1,
        body=RenewalPreviewRequest(
            components=[
                RenewalPreviewComponent(component_id=10708, quantity=10000),
                RenewalPreviewComponent(
                    component_id="handle:small-instance-hours", quantity=10000, price_point_id=8712
                ),
                RenewalPreviewComponent(
                    component_id="handle:large-instance-hours", quantity=100, price_point_id="handle:startup-pricing"
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type RenewalPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewRenewalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[RenewalPreviewRequest](maxio_advanced_billing/models/renewal_preview_request.py) \| [RenewalPreviewRequestDict](maxio_advanced_billing/models/renewal_preview_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RenewalPreviewResponse](maxio_advanced_billing/models/renewal_preview_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PreviewRenewalErrorBody](maxio_advanced_billing/errors/preview_renewal_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reactivate_subscription(subscription_id: int, *, body: ReactivateSubscriptionRequest | ReactivateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reactivates a previously canceled subscription. For details on how the reactivation works, and how to reactivate subscriptions through the application, see [reactivation](https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming).

**Note: The term "resume" is used also during another process in Advanced Billing. This occurs when an on-hold subscription is "resumed". This returns the subscription to an active state.**

+ The response returns the subscription object in the `active` or `trialing` state.
+ The `canceled_at` and `cancellation_message` fields do not have values.
+ The method works for "Canceled" or "Trial Ended" subscriptions.
+ It will not work for items not marked as "Canceled", "Unpaid", or "Trial Ended".

## Resume the current billing period for a subscription

A subscription is considered "resumable" if you are attempting to reactivate within the billing period the subscription was canceled in.

A resumed subscription's billing date remains the same as before it was canceled. In other words, it does not start a new billing period. Payment may or may not be collected for a resumed subscription, depending on whether or not the subscription had a balance when it was canceled (for example, if it was canceled because of dunning).

Consider a subscription which was created on June 1st, and would renew on July 1st. The subscription is then canceled on June 15.

If a reactivation with `resume: true` were attempted _before_ what would have been the next billing date of July 1st, then Advanced Billing would resume the subscription.

If a reactivation with `resume: true` were attempted _after_ what would have been the next billing date of July 1st, then Advanced Billing would not resume the subscription, and instead it would be reactivated with a new billing period.

If a reactivation with `resume: false`, or where 'resume' is omitted were attempted, then Advanced Billing would reactivate the subscription with a new billing period regardless of whether or not resuming the previous billing period was possible.

| Canceled | Reactivation | Resumable? |
|---|---|---|
| Jun 15 | June 28 | Yes |
| Jun 15 | July 2 | No |

## Reactivation Scenarios

### Reactivating Canceled Subscription While Preserving Balance

+ Given you have a product that costs $20
+ Given you have a canceled subscription to the $20 product
    + 1 charge should exist for $20
    + 1 payment should exist for $20
+ When the subscription has canceled due to dunning, it retained a negative balance of $20

#### Results

The resulting charges upon reactivation will be:
+ 1 charge for $20 for the new product
+ 1 charge for $20 for the balance due
+ Total charges = $40

+ The subscription will transition to active
+ The subscription balance will be zero

### Reactivating a Canceled Subscription With Coupon

+ Given you have a canceled subscription
+ It has no current period defined
+ You have a coupon code "EARLYBIRD"
+ The coupon is set to recur for 6 periods

PUT request sent to:
`https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?coupon_code=EARLYBIRD`

#### Results

+ The subscription will transition to active
+ The subscription should have applied a coupon with code "EARLYBIRD"

### Reactivating Canceled Subscription With a Trial, Without the include_trial Flag

+ Given you have a canceled subscription
+ The product associated with the subscription has a trial

+ PUT request to
`https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json`


#### Results
+ The subscription will transition to active

### Reactivating Canceled Subscription With Trial, With the include_trial Flag

+ Given you have a canceled subscription
+ The product associated with the subscription has a trial

+ Send a PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?include_trial=1`


#### Results

+ The subscription will transition to trialing

### Reactivating Trial Ended Subscription

+ Given you have a trial_ended subscription
+ Send a PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json`

#### Results

+ The subscription will transition to active

### Resuming a Canceled Subscription

+ Given you have a `canceled` subscription and it is resumable
+ Send a PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`

#### Results

+ The subscription will transition to active
+ The next billing date should not have changed

### Attempting to resume a subscription which is not resumable

+ Given you have a `canceled` subscription, and it is not resumable
+ Send a PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`

#### Results

+ The subscription will transition to active, with a new billing period.

### Attempting to resume but not reactivate a subscription which is not resumable

+ Given you have a `canceled` subscription, and it is not resumable
+ Send a PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume[require_resume]=true`
+ The response status should be "422 UNPROCESSABLE ENTITY"
+ The subscription should be canceled with the following response
``
  {
    "errors": ["Request was 'resume only', but this subscription cannot be resumed."]
  }
``

#### Results

+ The subscription should remain `canceled`
+ The next billing date should not have changed

### Resuming Subscription Which Was Trialing

+ Given you have a `trial_ended` subscription, and it is resumable
+ And the subscription was canceled in the middle of a trial
+ And there is still time left on the trial
+ Send a PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`

#### Results

+ The subscription will transition to trialing
+ The next billing date should not have changed

### Resuming Subscription Which Was trial_ended

+ Given you have a `trial_ended` subscription, and it is resumable
+ Send a PUT request to `https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true`

#### Results

+ The subscription will transition to active
+ The next billing date should not have changed
+ Any product-related charges should have been collected

## 3D Secure (3DS) Authentication post-authentication flow

When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will direct the customer through 3DS Authentication. 

See the [3D Secure Post-Authentication Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow) article in the product documentation to learn how to manage the redirect flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.reactivate_subscription(
        1,
        body=ReactivateSubscriptionRequest(
            calendar_billing=ReactivationBilling(reactivation_charge=ReactivationCharge.PRORATED),
            include_trial=True,
            preserve_balance=True,
            coupon_code="10OFF",
            use_credits_and_prepayments=True,
            resume=True,
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReactivateSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.reactivate_subscription(
        1,
        body=ReactivateSubscriptionRequest(
            calendar_billing=ReactivationBilling(reactivation_charge=ReactivationCharge.PRORATED),
            include_trial=True,
            preserve_balance=True,
            coupon_code="10OFF",
            use_credits_and_prepayments=True,
            resume=True,
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReactivateSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[ReactivateSubscriptionRequest](maxio_advanced_billing/models/reactivate_subscription_request.py) \| [ReactivateSubscriptionRequestDict](maxio_advanced_billing/models/reactivate_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReactivateSubscriptionErrorBody](maxio_advanced_billing/errors/reactivate_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def resume_subscription(subscription_id: int, *, calendar_billing_resumption_charge: ResumptionChargeOrStr | None = ResumptionCharge.PRORATED, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Resumes a paused (on-hold) subscription. If the normal next renewal date has not passed, the subscription will return to active and will renew on that date.  Otherwise, it will behave like a reactivation, setting the billing date to 'now' and charging the subscriber.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.resume_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResumeSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.resume_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResumeSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>calendar_billing_resumption_charge</code> | <code>[ResumptionChargeOrStr](maxio_advanced_billing/models/enums/resumption_charge.py) \| None</code> | (For calendar billing subscriptions only) The way that the resumed subscription's charge should be handled.<br>**Default**: <code>ResumptionCharge.PRORATED</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ResumeSubscriptionErrorBody](maxio_advanced_billing/errors/resume_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retry_subscription(subscription_id: int, *, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retries collecting the balance due on a past-due subscription without waiting for the next scheduled attempt.

## 3D Secure (3DS) Authentication post-authentication flow

When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will direct the customer through 3DS Authentication. 

See the [3D Secure Post-Authentication Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow) article in the product documentation to learn how to manage the redirect flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.retry_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrySubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.retry_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrySubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RetrySubscriptionErrorBody](maxio_advanced_billing/errors/retry_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_automatic_subscription_resumption(subscription_id: int, *, body: PauseRequest | PauseRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the date on which a paused subscription will automatically resume.

To update a subscription's resume date, use this method to change or update the `automatically_resume_at` date.

### Remove the resume date

Alternatively, you can change the `automatically_resume_at` to `null` if you would like the subscription to not have a resume date.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscription_status.update_automatic_subscription_resumption(
        1,
        body=PauseRequest(hold=AutoResume(automatically_resume_at=datetime(2019, 1, 20, 0, 0, 0, tzinfo=timezone.utc))),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateAutomaticSubscriptionResumptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscription_status.update_automatic_subscription_resumption(
        1,
        body=PauseRequest(hold=AutoResume(automatically_resume_at=datetime(2019, 1, 20, 0, 0, 0, tzinfo=timezone.utc))),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateAutomaticSubscriptionResumptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[PauseRequest](maxio_advanced_billing/models/pause_request.py) \| [PauseRequestDict](maxio_advanced_billing/models/pause_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateAutomaticSubscriptionResumptionErrorBody](maxio_advanced_billing/errors/update_automatic_subscription_resumption_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Subscriptions

> Source: [Subscriptions](maxio_advanced_billing/apis/subscriptions.py)

<details>
<summary><code>def activate_subscription(subscription_id: int, *, body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Activates awaiting signup and trialing subscriptions. This feature is only available on the Relationship Invoicing architecture. Subscriptions in a group cannot be activated immediately.

The `revert_on_failure` parameter controls the behavior upon activation failure.
- If set to `true` and something goes wrong i.e. payment fails, the subscription's state does not change. The subscription’s billing period also remains the same.
- If set to `false` and something goes wrong i.e. payment fails, the activation continues and enters an end of life state. For trialing subscriptions, that is either trial ended (if the trial is no obligation), past due (if the trial has an obligation), or canceled (if the site has no dunning strategy, or has a strategy that says to cancel immediately). For awaiting signup subscriptions, that is always canceled.

The default activation failure behavior can be configured per activation attempt, or you can set a default value under Config > Settings > Subscription Activation Settings.

## Activation Scenarios

### Activate Awaiting Signup subscription

- Given you have a product without trial
- Given you have a site without dunning strategy

``mermaid
  flowchart LR
    AS[Awaiting Signup] --> A{Activate}
    A -->|Success| Active
    A -->|Failure| ROF{revert_on_failure}
    ROF -->|true| AS
    ROF -->|false| Canceled
``

- Given you have a product with trial
- Given you have a site with dunning strategy

``mermaid
  flowchart LR
    AS[Awaiting Signup] --> A{Activate}
    A -->|Success| Trialing
    A -->|Failure| ROF{revert_on_failure}
    ROF -->|true| AS
    ROF -->|false| PD[Past Due]
``

### Activate Trialing subscription

For more information about the behavior of trialing subscriptions, see [Trialing Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trialing-Subscriptions).
When the `revert_on_failure` parameter is set to `true`, the subscription's state remains Trialing; the invoice from activation is voided, and any prepayments and credits applied to the invoice are returned to the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.activate_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.activate_subscription(1)
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[ActivateSubscriptionRequest](maxio_advanced_billing/models/activate_subscription_request.py) \| [ActivateSubscriptionRequestDict](maxio_advanced_billing/models/activate_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ActivateSubscriptionErrorBody](maxio_advanced_billing/errors/activate_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorArrayMapResponse1](maxio_advanced_billing/models/error_array_map_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apply_coupons_to_subscription(subscription_id: int, *, code: str | None = None, body: AddCouponsRequest | AddCouponsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Applies one or more coupon codes to an existing subscription.

An existing subscription can accommodate multiple discounts/coupon codes. This is only applicable if each coupon is stackable. For more information on stackable coupons, we recommend reviewing our [coupon documentation.](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#stackability-rules)

## Query Parameters vs Request Body Parameters

Passing in a coupon code as a query parameter will add the code to the subscription, completely replacing all existing coupon codes on the subscription.

For this reason, using this query parameter on this endpoint has been deprecated in favor of using the request body parameters as described below. When passing in request body parameters, the list of coupon codes will simply be added to any existing list of codes on the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.apply_coupons_to_subscription(
        1, body=AddCouponsRequest(codes=["COUPON_1", "COUPON_2"])
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ApplyCouponsToSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.apply_coupons_to_subscription(
        1, body=AddCouponsRequest(codes=["COUPON_1", "COUPON_2"])
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ApplyCouponsToSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>code</code> | <code>str \| None</code> | A code for the coupon that would be applied to a subscription<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[AddCouponsRequest](maxio_advanced_billing/models/add_coupons_request.py) \| [AddCouponsRequestDict](maxio_advanced_billing/models/add_coupons_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ApplyCouponsToSubscriptionErrorBody](maxio_advanced_billing/errors/apply_coupons_to_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SubscriptionAddCouponError1](maxio_advanced_billing/models/subscription_add_coupon_error1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_subscription(*, body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Subscription for a customer and product.

Specify the product with `product_id` or `product_handle`. To set a specific product price point, use `product_price_point_handle` or `product_price_point_id`.

Identify an existing customer with `customer_id` or `customer_reference`. Optionally, include an existing payment profile using `payment_profile_id`. To create a new customer, pass customer_attributes. 

Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of common scenarios for creating subscriptions. 

## List vs Sales Pricing

When a subscription uses custom pricing as the sales price, you can optionally provide a list price for any item. If omitted, the list price defaults to the sales price. The difference between the list price and sales price is used to calculate implicit discounts, which appear on Invoices and in reporting. List price can also support revenue allocations in [Advanced Revenue](https://docs.maxio.com/hc/en-us/articles/24177001342861-Create-and-Configure-RevenueBooks).

If your site has list pricing enabled, the API accepts `custom_price.list_price_point_id` for custom pricing, validates and persists it, and returns list price metadata in subscription responses. If list pricing is disabled, this input is ignored and related response fields are omitted.

When list pricing is enabled:

- Subscription → Product `product_price_point_list_price_point_id` (integer)
- `product_price_point_list_price_point_handle` (string)
- Subscription Components (when components are included in the response, such as with subscriptions built from components or component serialization paths) `component_id` (integer)
- `price_point_id` (integer)
- `list_price_point_id` (integer)

When list pricing is disabled:

- Subscription → Product `product_price_point_list_price_point_id`: omitted
- `product_price_point_list_price_point_handle`: omitted
- Subscription Components `list_price_point_id`: omitted

This functionality is supported in the API, but is not currently supported in SDKs.

## Subscriptions can now work independently from the catalog

 If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, you can create subscriptions without a `product_id` or `product_handle` using POST /subscriptions, building them entirely from components.

A valid subscription must include at least one active component with:
- a positive `allocated_quantity`,
- a positive `unit_balance`, or
- 'enabled: true' (for on/off components)
- a configured metered component

`component_id` can be provided as a numeric ID or in handle: format. If `trial_interval` and `trial_interval_unit` are included, they are applied at creation.

In the response, product and product price point fields are null, and component details are returned instead.

This functionality is supported in the API, but is not currently supported in SDKs.

## Payment information

Payment information may be required to create a subscription, depending on the options for the Product being subscribed. See [product options](https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products) for more information. See the [Payments Profile]($e/Payment%20Profiles/createPaymentProfile) endpoint for details on payment parameters.
See the [Subscription Signups](page:introduction/basic-concepts/subscription-signup) article for more information on working with subscriptions in Advanced Billing.

## Payment information  

Payment information may be required to create a subscription, depending on the options for the Product being subscribed. See [product options](https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products) for more information. See the [Payments Profile]($e/Payment%20Profiles/createPaymentProfile) endpoint for details on payment parameters. 

Do not use real card information for testing. See the Sites articles that cover [testing your site setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0) for more details on testing in your sandbox.

Note that collecting and sending raw card details in production requires [PCI compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0) on your end. If your business is not PCI compliant, use [Maxio.js (formerly Chargify.js)](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0) to collect credit card or bank account information.

## 3D Secure (3DS) Authentication post-authentication flow

When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will direct the customer through 3DS Authentication. 

See the [3D Secure Post-Authentication Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow) article in the product documentation to learn how to manage the redirect flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.create_subscription(
        body=CreateSubscriptionRequest(
            subscription=CreateSubscription(
                product_handle="basic",
                payment_collection_method=CollectionMethod.REMITTANCE,
                customer_attributes=CustomerAttributes(
                    first_name="Joe",
                    last_name="Smith",
                    email="joe@example.com",
                    organization="Acme",
                    reference="XYZ",
                    address="123 Mass Ave.",
                    address_2="some example string",
                    city="Boston",
                    state="MA",
                    zip="02120",
                    country="US",
                    phone="(617) 111 - 0000",
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.create_subscription(
        body=CreateSubscriptionRequest(
            subscription=CreateSubscription(
                product_handle="basic",
                payment_collection_method=CollectionMethod.REMITTANCE,
                customer_attributes=CustomerAttributes(
                    first_name="Joe",
                    last_name="Smith",
                    email="joe@example.com",
                    organization="Acme",
                    reference="XYZ",
                    address="123 Mass Ave.",
                    address_2="some example string",
                    city="Boston",
                    state="MA",
                    zip="02120",
                    country="US",
                    phone="(617) 111 - 0000",
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateSubscriptionRequest](maxio_advanced_billing/models/create_subscription_request.py) \| [CreateSubscriptionRequestDict](maxio_advanced_billing/models/create_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- Created

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateSubscriptionErrorBody](maxio_advanced_billing/errors/create_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_subscription(*, reference: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Finds a subscription by its reference.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.find_subscription()
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FindSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.find_subscription()
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FindSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reference</code> | <code>str \| None</code> | Subscription reference<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[FindSubscriptionErrorBody](maxio_advanced_billing/errors/find_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscriptions(*, page: int | None = 1, per_page: int | None = 20, sort: SubscriptionSortOrStr | None = SubscriptionSort.SIGNUP_DATE, direction: SortingDirectionOrStr | None = None, state: SubscriptionStateFilterOrStr | None = None, product: Product1 | Product1Dict | None = None, q: str | None = None, q_scope: QScopeOrStr | None = None, customer_id: int | None = None, product_price_point_id: int | None = None, coupon: int | None = None, coupon_code: str | None = None, collection_method: CollectionMethod1OrStr | None = None, branding_theme_id: int | None = None, date_field: SubscriptionDateFieldOrStr | None = None, start_date: Date | None = None, end_date: Date | None = None, start_datetime: RFC3339DateTime | None = None, end_datetime: RFC3339DateTime | None = None, metadata: dict[str, str] | None = None, group_status: GroupStatusOrStr | None = None, dunning_exemption: bool | None = None, payment_gateways: str | None = None, currencies: str | None = None, include: list[SubscriptionListIncludeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SubscriptionResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists subscriptions for a site. Use the query string filters and pagination to control responses from the server.

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, some subscriptions may not have an associated product. For subscriptions without an associated product, 'product', 'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

## Search for a subscription

Use the query strings below to search for a subscription using the criteria available. The return value will be an array.

## Self-Service Page token

Self-Service Page token for the subscriptions is not returned by default. If this information is desired, the include[]=self_service_page_token parameter must be provided with the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.list_subscriptions(
        page=1, per_page=50, include=[SubscriptionListInclude.SELF_SERVICE_PAGE_TOKEN]
    )
    # TODO: Handle 'response' of type list[SubscriptionResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscriptions.list_subscriptions(
        page=1, per_page=50, include=[SubscriptionListInclude.SELF_SERVICE_PAGE_TOKEN]
    )
    # TODO: Handle 'response' of type list[SubscriptionResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>sort</code> | <code>[SubscriptionSortOrStr](maxio_advanced_billing/models/enums/subscription_sort.py) \| None</code> | The attribute by which to sort<br>**Default**: <code>SubscriptionSort.SIGNUP_DATE</code> |
| <code>direction</code> | <code>[SortingDirectionOrStr](maxio_advanced_billing/models/enums/sorting_direction.py) \| None</code> | Controls the order in which results are returned.<br>Use in query `direction=asc`.<br>**Default**: <code>None</code> |
| <code>state</code> | <code>[SubscriptionStateFilterOrStr](maxio_advanced_billing/models/enums/subscription_state_filter.py) \| None</code> | The current state of the subscription<br>**Default**: <code>None</code> |
| <code>product</code> | <code>[Product1](maxio_advanced_billing/models/unions/product1.py) \| [Product1Dict](maxio_advanced_billing/models/unions/product1.py) \| None</code> | Filter subscriptions by product. Accepts product ID or exact product name. Product handle is not supported.<br>**Default**: <code>None</code> |
| <code>q</code> | <code>str \| None</code> | Search string.<br>**Default**: <code>None</code> |
| <code>q_scope</code> | <code>[QScopeOrStr](maxio_advanced_billing/models/enums/q_scope.py) \| None</code> | Scope of fields used by the q search.<br>**Default**: <code>None</code> |
| <code>customer_id</code> | <code>int \| None</code> | The Advanced Billing id of the customer.<br>**Default**: <code>None</code> |
| <code>product_price_point_id</code> | <code>int \| None</code> | The ID of the product price point. If supplied, product is required.<br>**Default**: <code>None</code> |
| <code>coupon</code> | <code>int \| None</code> | The numeric id of the coupon currently applied to the subscription. (This can be found in the URL when editing a coupon. Note that the coupon code cannot be used.)<br>**Default**: <code>None</code> |
| <code>coupon_code</code> | <code>str \| None</code> | The coupon code currently applied to the subscription<br>**Default**: <code>None</code> |
| <code>collection_method</code> | <code>[CollectionMethod1OrStr](maxio_advanced_billing/models/enums/collection_method1.py) \| None</code> | The collection method for the subscription.<br>**Default**: <code>None</code> |
| <code>branding_theme_id</code> | <code>int \| None</code> | Filter subscriptions by the ID of an assigned Branding Theme. Branding Themes is a beta feature. See [Understand Branding Themes](https://docs.maxio.com/hc/en-us/articles/43796895662093-Understand-Branding-Themes#understand-branding-themes-0-0) for more information.<br>**Default**: <code>None</code> |
| <code>date_field</code> | <code>[SubscriptionDateFieldOrStr](maxio_advanced_billing/models/enums/subscription_date_field.py) \| None</code> | The type of filter you'd like to apply to your search.  Allowed Values: , current_period_ends_at, current_period_starts_at, created_at, activated_at, canceled_at, expires_at, trial_started_at, trial_ended_at, updated_at<br>**Default**: <code>None</code> |
| <code>start_date</code> | <code>Date \| None</code> | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in query `start_date=2022-07-01`.<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>Date \| None</code> | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query `end_date=2022-08-01`.<br>**Default**: <code>None</code> |
| <code>start_datetime</code> | <code>RFC3339DateTime \| None</code> | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns subscriptions with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. Use in query `start_datetime=2022-07-01 09:00:05`.<br>**Default**: <code>None</code> |
| <code>end_datetime</code> | <code>RFC3339DateTime \| None</code> | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns subscriptions with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. Use in query `end_datetime=2022-08-01 10:00:05`.<br>**Default**: <code>None</code> |
| <code>metadata</code> | <code>dict&#91;str, str&#93; \| None</code> | The value of the metadata field specified in the parameter. Use in query `metadata[my-field]=value&metadata[other-field]=another_value`.<br>**Default**: <code>None</code> |
| <code>group_status</code> | <code>[GroupStatusOrStr](maxio_advanced_billing/models/enums/group_status.py) \| None</code> | Filter by whether a subscription is in a group.<br>**Default**: <code>None</code> |
| <code>dunning_exemption</code> | <code>bool \| None</code> | Filter by dunning exemption status.<br>**Default**: <code>None</code> |
| <code>payment_gateways</code> | <code>str \| None</code> | Comma-separated payment gateway identifiers.<br>**Default**: <code>None</code> |
| <code>currencies</code> | <code>str \| None</code> | Comma-separated currency codes.<br>**Default**: <code>None</code> |
| <code>include</code> | <code>list&#91;[SubscriptionListIncludeOrStr](maxio_advanced_billing/models/enums/subscription_list_include.py)&#93; \| None</code> | Allows including additional data in the response. Use in query: `include[]=self_service_page_token`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def override_subscription(subscription_id: int, *, body: OverrideSubscriptionRequest | OverrideSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets certain subscription fields that are usually managed automatically. Some of the fields can be set via the normal Subscriptions Update API, but others can only be set using this endpoint.

This endpoint is provided for cases where you need to “align” Advanced Billing data with data that happened in your system, perhaps before you started using Advanced Billing. For example, you may choose to import your historical subscription data, and would like the activation and cancellation dates in Advanced Billing to match your existing historical dates. Advanced Billing does not backfill historical events (i.e. from the Events API), but some static data can be changed via this API.

Why are some fields only settable from this endpoint, and not the normal subscription create and update endpoints? Because we want users of this endpoint to be aware that these fields are usually managed by Advanced Billing, and using this API means **you are stepping out on your own.**

Changing these fields will not affect any other attributes. For example, adding an expiration date will not affect the next assessment date on the subscription.

If you regularly need to override the current_period_starts_at for new subscriptions, this can also be accomplished by setting both `previous_billing_at` and `next_billing_at` at subscription creation. See the documentation on [Importing Subscriptions](./b3A6MTQxMDgzODg-create-subscription#subscriptions-import) for more information.

## Limitations

When passing `current_period_starts_at` some validations are made:

1. The subscription needs to be unbilled (no statements or invoices).
2. The value passed must be a valid date/time. We recommend using the iso 8601 format.
3. The value passed must be before the current date/time.

If unpermitted parameters are sent, a 400 HTTP response is sent along with a string giving the reason for the problem.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.subscriptions.override_subscription(
        1,
        body=OverrideSubscriptionRequest(
            subscription=OverrideSubscription(
                activated_at=datetime(1999, 12, 1, 15, 28, 34, tzinfo=timezone.utc),
                canceled_at=datetime(2000, 12, 31, 15, 28, 34, tzinfo=timezone.utc),
                cancellation_message="Original cancellation in 2000",
                expires_at=datetime(2001, 7, 15, 15, 28, 34, tzinfo=timezone.utc),
            ),
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OverrideSubscriptionErrorBody
```

**Async**

```python
try:
    await async_client.subscriptions.override_subscription(
        1,
        body=OverrideSubscriptionRequest(
            subscription=OverrideSubscription(
                activated_at=datetime(1999, 12, 1, 15, 28, 34, tzinfo=timezone.utc),
                canceled_at=datetime(2000, 12, 31, 15, 28, 34, tzinfo=timezone.utc),
                cancellation_message="Original cancellation in 2000",
                expires_at=datetime(2001, 7, 15, 15, 28, 34, tzinfo=timezone.utc),
            ),
        ),
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OverrideSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[OverrideSubscriptionRequest](maxio_advanced_billing/models/override_subscription_request.py) \| [OverrideSubscriptionRequestDict](maxio_advanced_billing/models/override_subscription_request.py) \| None</code> | Only these fields are available to be set.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[OverrideSubscriptionErrorBody](maxio_advanced_billing/errors/override_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SingleErrorResponse1](maxio_advanced_billing/models/single_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_subscription(*, body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Previews a subscription by POSTing the same JSON or XML as for a subscription creation.

The "Next Billing" amount and "Next Billing" date are represented in each Subscriber's Summary.

This endpoint does not create a subscription; it is meant to serve as a prediction.

For more information, see [Subscriber Interface Overview](https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview).

## Subscriptions can now work independently from the catalog

 If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, you can create subscriptions without a `product_id` or `product_handle` using POST /subscriptions, building them entirely from components.

A valid subscription must include at least one active component with:
- a positive `allocated_quantity`,
- a positive `unit_balance`, or
- 'enabled: true' (for on/off components)

`component_id` can be provided as a numeric ID or in handle: format. If `trial_interval` and `trial_interval_unit` are included, they are applied at creation.

In the response, product and product price point fields are null, and component details are returned instead.

This functionality is supported in the API, but is not currently supported in SDKs.

## Taxable Subscriptions

This endpoint previews taxes applicable to a purchase. For taxes to be previewed, the following conditions must be met:

+ Taxes must be configured on the subscription
+ The preview must be for the purchase of a taxable product or component, or combination of the two.
+ The subscription payload must contain a full billing or shipping address to calculate tax

For more information about creating taxable previews, see [Taxes](https://maxio.zendesk.com/hc/en-us/sections/24287012349325-Taxes).

You do **not** need to include a card number to generate tax information when you are previewing a subscription. However, when you actually want to create the subscription, you must include the credit card information if you want the billing address to be stored. The billing address and the credit card information are stored together within the payment profile object. Also, you cannot send a billing address without payment profile information, as the address is stored on the card.

You can pass shipping and billing addresses and still decide not to calculate taxes. To do that, pass `skip_billing_manifest_taxes: true` attribute.

## Non-taxable Subscriptions

If you'd like to calculate subscriptions that do not include tax, you can leave off the billing information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.preview_subscription(
        body=CreateSubscriptionRequest(subscription=CreateSubscription(product_handle="gold-product"))
    )
    # TODO: Handle 'response' of type SubscriptionPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscriptions.preview_subscription(
        body=CreateSubscriptionRequest(subscription=CreateSubscription(product_handle="gold-product"))
    )
    # TODO: Handle 'response' of type SubscriptionPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateSubscriptionRequest](maxio_advanced_billing/models/create_subscription_request.py) \| [CreateSubscriptionRequestDict](maxio_advanced_billing/models/create_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionPreviewResponse](maxio_advanced_billing/models/subscription_preview_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def purge_subscription(subscription_id: int, ack: int, *, cascade: list[SubscriptionPurgeTypeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Purges an individual subscription for sites in test mode.

Provide the subscription ID in the URL.  To confirm, supply the customer ID in the query string `ack` parameter. You may also delete the customer record and/or payment profiles by passing `cascade` parameters. For example, to delete just the customer record, the query params would be: `?ack={customer_id}&cascade[]=customer`

If you need to remove subscriptions from a live site, contact support to discuss your use case.

### Delete customer and payment profile

The query params will be: `?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.purge_subscription(
        1, 1, cascade=[SubscriptionPurgeType.CUSTOMER, SubscriptionPurgeType.PAYMENT_PROFILE]
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PurgeSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.purge_subscription(
        1, 1, cascade=[SubscriptionPurgeType.CUSTOMER, SubscriptionPurgeType.PAYMENT_PROFILE]
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PurgeSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>ack</code> | <code>int</code> | id of the customer. |
| <code>cascade</code> | <code>list&#91;[SubscriptionPurgeTypeOrStr](maxio_advanced_billing/models/enums/subscription_purge_type.py)&#93; \| None</code> | Options are "customer" or "payment_profile".<br>Use in query: `cascade[]=customer&cascade[]=payment_profile`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PurgeSubscriptionErrorBody](maxio_advanced_billing/errors/purge_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_subscription(subscription_id: int, *, include: list[SubscriptionIncludeOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves subscription details.

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, some subscriptions may not have an associated product. For subscriptions without an associated product, 'product', 'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

## Self-Service Page token

Self-Service Page token for the subscription is not returned by default. If this information is desired, the include[]=self_service_page_token parameter must be provided with the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.read_subscription(
        1, include=[SubscriptionInclude.COUPONS, SubscriptionInclude.SELF_SERVICE_PAGE_TOKEN]
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.subscriptions.read_subscription(
        1, include=[SubscriptionInclude.COUPONS, SubscriptionInclude.SELF_SERVICE_PAGE_TOKEN]
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>include</code> | <code>list&#91;[SubscriptionIncludeOrStr](maxio_advanced_billing/models/enums/subscription_include.py)&#93; \| None</code> | Allows including additional data in the response. Use in query: `include[]=coupons&include[]=self_service_page_token`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_coupon_from_subscription(subscription_id: int, *, coupon_code: str | None = None, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a coupon from an existing subscription.

For more information on the expected behavior of removing a coupon from a subscription, see [Coupons and Subscriptions](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#removing-a-coupon).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.remove_coupon_from_subscription(1)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveCouponFromSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.remove_coupon_from_subscription(1)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveCouponFromSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>coupon_code</code> | <code>str \| None</code> | The coupon code<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>str</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RemoveCouponFromSubscriptionErrorBody](maxio_advanced_billing/errors/remove_coupon_from_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[SubscriptionRemoveCouponErrors1](maxio_advanced_billing/models/subscription_remove_coupon_errors1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_prepaid_subscription_configuration(subscription_id: int, *, body: UpsertPrepaidConfigurationRequest | UpsertPrepaidConfigurationRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PrepaidConfigurationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a subscription's prepaid configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.update_prepaid_subscription_configuration(
        1,
        body=UpsertPrepaidConfigurationRequest(
            prepaid_configuration=UpsertPrepaidConfiguration(
                initial_funding_amount_in_cents=50000,
                replenish_to_amount_in_cents=50000,
                auto_replenish=True,
                replenish_threshold_amount_in_cents=10000,
            ),
        ),
    )
    # TODO: Handle 'response' of type PrepaidConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdatePrepaidSubscriptionConfigurationErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.update_prepaid_subscription_configuration(
        1,
        body=UpsertPrepaidConfigurationRequest(
            prepaid_configuration=UpsertPrepaidConfiguration(
                initial_funding_amount_in_cents=50000,
                replenish_to_amount_in_cents=50000,
                auto_replenish=True,
                replenish_threshold_amount_in_cents=10000,
            ),
        ),
    )
    # TODO: Handle 'response' of type PrepaidConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdatePrepaidSubscriptionConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[UpsertPrepaidConfigurationRequest](maxio_advanced_billing/models/upsert_prepaid_configuration_request.py) \| [UpsertPrepaidConfigurationRequestDict](maxio_advanced_billing/models/upsert_prepaid_configuration_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PrepaidConfigurationResponse](maxio_advanced_billing/models/prepaid_configuration_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdatePrepaidSubscriptionConfigurationErrorBody](maxio_advanced_billing/errors/update_prepaid_subscription_configuration_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[PrepaidConfigurationErrorResponse](maxio_advanced_billing/models/unions/prepaid_configuration_error_response.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_subscription(subscription_id: int, *, body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SubscriptionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates one or more attributes of a subscription.

## Update Subscription Payment Method

Change the card that your subscriber uses for their subscription. You can also use this method to change the expiration date of the card **if your gateway allows**.

Do not use real card information for testing. See the Sites articles that cover [testing your site setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0) for more details on testing in your sandbox.

Note that collecting and sending raw card details in production requires [PCI compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0) on your end. If your business is not PCI compliant, use [Chargify.js](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0) to collect credit card or bank account information.

> Note: Partial card updates for **Authorize.Net** are not allowed via this endpoint. The existing Payment Profile must be directly updated instead.

## Update Product

You also use this method to change the subscription to a different product by setting a new value for product_handle. A product change can be done in two different ways, **product change** or **delayed product change**.

### Product Change

You can change a subscription's product. The new payment amount is calculated and charged at the normal start of the next period. If you require complex product changes or prorated upgrades and downgrades instead, please see the documentation on [Migrating Subscription Products](https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations#product-changes-and-migrations-0-0).

To perform a product change, set either the `product_handle` or `product_id` attribute to that of a different product from the same site as the subscription. You can also change the price point by passing in either `product_price_point_id` or `product_price_point_handle` - otherwise the new product's default price point is used.

### Delayed Product Change

This method also changes the product and/or price point, and the new payment amount is calculated and charged at the normal start of the next period.

This method schedules the product change to happen automatically at the subscription’s next renewal date. To perform a delayed product change, set the `product_handle` attribute as you would in a regular product change, but also set the `product_change_delayed` attribute to `true`. No proration applies in this case.

You can also perform a delayed change to the price point by passing in either `product_price_point_id` or `product_price_point_handle`

> **Note:** To cancel a delayed product change, set `next_product_id` to an empty string.

## Billing Date Changes

You can update dates for a subscription.

### Regular Billing Date Changes

Send the `next_billing_at` to set the next billing date for the subscription. After that date passes and the subscription is processed, the following billing date will be set according to the subscription's product period.

> Note: If you pass an invalid date, the correct date is automatically set to the correct date. For example, if February 30 is passed, the next billing would be set to March 2nd in a non-leap year.

The server response will not return data under the key/value pair of `next_billing_at`. View the key/value pair of `current_period_ends_at` to verify that the `next_billing_at` date has been changed successfully.

### Calendar Billing and Snap Day Changes

For a subscription using Calendar Billing, setting the next billing date is a bit different. Send the `snap_day` attribute to change the calendar billing date for **a subscription using a product eligible for calendar billing**.

> Note: If you change the product associated with a subscription that contains a `snap_day` and immediately READ/GET the subscription data, it will still contain the original `snap_day`. The `snap_day` will be reset to `null` on the next billing cycle. This is because a product change is instantaneous and only affects the product associated with a subscription.

If you have the new [Catalog experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology) enabled, some subscriptions may not have an associated product. For subscriptions without an associated product, `product`, `product_price_point_id`, and `product_price_point_type` are returned as `null`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.subscriptions.update_subscription(
        1,
        body=UpdateSubscriptionRequest(
            subscription=UpdateSubscription(
                next_billing_at=datetime(2010, 8, 6, 15, 34, 0, tzinfo=timezone.utc),
                payment_collection_method="remittance",
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.subscriptions.update_subscription(
        1,
        body=UpdateSubscriptionRequest(
            subscription=UpdateSubscription(
                next_billing_at=datetime(2010, 8, 6, 15, 34, 0, tzinfo=timezone.utc),
                payment_collection_method="remittance",
            ),
        ),
    )
    # TODO: Handle 'response' of type SubscriptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>int</code> | The Chargify id of the subscription. |
| <code>body</code> | <code>[UpdateSubscriptionRequest](maxio_advanced_billing/models/update_subscription_request.py) \| [UpdateSubscriptionRequestDict](maxio_advanced_billing/models/update_subscription_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SubscriptionResponse](maxio_advanced_billing/models/subscription_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateSubscriptionErrorBody](maxio_advanced_billing/errors/update_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WalletAdjustments

> Source: [WalletAdjustments](maxio_advanced_billing/apis/wallet_adjustments.py)

<details>
<summary><code>def create_wallet_adjustment(wallet_id: int, *, body: CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletGrantResultResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Posts a signed correction against a specific grant (or, for an overdraft entry, against the overdraft): positive adds units to the grant, negative removes them. `reason` is required and is written to the ledger row's `memo`. Writes exactly one ledger row, of kind `adjustment`.

Use `source_transaction_id` to name a specific `debit` row when you're correcting one recorded consumption rather than the grant's balance as a whole. When it names a grant-attributed debit, it's recorded for audit only: naming it doesn't change how `amount` is applied, and more than one adjustment may name the same row. When it names an overdraft entry, it switches the correction to the overdraft path described below.

An overdraft entry (a `debit` row with no `grant_id`, written when an `allow_negative` wallet consumes past its grants) can be corrected without a `grant_id`. That correction is credit-only, credits no grant, and is bounded by the usage the entry still records and by the overdraft the wallet still owes. Once a later grant has repaid the overdraft, correct that grant's balance instead.

An adjustment corrects the ledger, so it works on the grant's recorded remainder, `posted_remaining`, not on `remaining`, which on a metered wallet read through [Read Wallet]($e/Wallets/readWallet) also subtracts usage not yet posted. Send `posted_remaining` back as `expected_remaining`; sending `remaining` on a metered wallet with pending usage returns `409`.

`expected_remaining` and `expected_source_corrections` are optional optimistic-concurrency checks; see their field descriptions. Use them when the correction's `amount` was derived from a value read earlier that might have moved since.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_adjustments.create_wallet_adjustment(
        1,
        body=CreateWalletAdjustmentRequest(
            adjustment=Adjustment(amount="10.0", reason="Support credit for outage on 2026-07-30", grant_id=9)
        ),
    )
    # TODO: Handle 'response' of type WalletGrantResultResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletAdjustmentErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_adjustments.create_wallet_adjustment(
        1,
        body=CreateWalletAdjustmentRequest(
            adjustment=Adjustment(amount="10.0", reason="Support credit for outage on 2026-07-30", grant_id=9)
        ),
    )
    # TODO: Handle 'response' of type WalletGrantResultResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletAdjustmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wallet_id</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>body</code> | <code>[CreateWalletAdjustmentRequest](maxio_advanced_billing/models/create_wallet_adjustment_request.py) \| [CreateWalletAdjustmentRequestDict](maxio_advanced_billing/models/create_wallet_adjustment_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletGrantResultResponse](maxio_advanced_billing/models/wallet_grant_result_response.py)</code> -- The ledger row written, plus the wallet's new balance.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateWalletAdjustmentErrorBody](maxio_advanced_billing/errors/create_wallet_adjustment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 409, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WalletProducts

> Source: [WalletProducts](maxio_advanced_billing/apis/wallet_products.py)

<details>
<summary><code>def archive_wallet_product(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> WalletProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives the Wallet Product. Refuses when an active Feature's `wallet_behavior` still points at it, or when it's used in a scheduled renewal. This protects Feature-provisioned wallets, but not a wallet created manually against this product: a manual wallet can be left denominated by an archived Wallet Product, and [Create Wallet Purchase]($e/Wallet%20Purchases/createWalletPurchase) doesn't check whether the billing product is archived before pricing and charging a purchase against it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_products.archive_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveWalletProductErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_products.archive_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveWalletProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for example `handle:token-pack`). A bare handle returns `404`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletProductResponse](maxio_advanced_billing/models/wallet_product_response.py)</code> -- Wallet Product archived.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ArchiveWalletProductErrorBody](maxio_advanced_billing/errors/archive_wallet_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_wallet_product(*, body: CreateWalletProductRequest | CreateWalletProductRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Wallet Product: a billing product with no product family, meant to denominate wallets and to be purchased through [Create Wallet Purchase]($e/Wallet%20Purchases/createWalletPurchase). It's a Component under the hood, so it returns the full Component field set, and can optionally be priced with one or more price points in the same call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_products.create_wallet_product(
        body=CreateWalletProductRequest(
            wallet_product=WalletProduct(
                name="Token pack",
                unit_name="tokens",
                price_point=WalletProductPricePointAttributes(
                    name="Standard", pricing_scheme=PricingScheme.PER_UNIT, unit_price="0.05"
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletProductErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_products.create_wallet_product(
        body=CreateWalletProductRequest(
            wallet_product=WalletProduct(
                name="Token pack",
                unit_name="tokens",
                price_point=WalletProductPricePointAttributes(
                    name="Standard", pricing_scheme=PricingScheme.PER_UNIT, unit_price="0.05"
                ),
            ),
        ),
    )
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateWalletProductRequest](maxio_advanced_billing/models/create_wallet_product_request.py) \| [CreateWalletProductRequestDict](maxio_advanced_billing/models/create_wallet_product_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletProductResponse](maxio_advanced_billing/models/wallet_product_response.py)</code> -- Wallet Product created.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateWalletProductErrorBody](maxio_advanced_billing/errors/create_wallet_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_wallet_products(*, include_archived: bool | None = None, status: Status1OrStr | None = None, q: str | None = None, sort_by: SortBy1OrStr | None = SortBy1.NAME, sort_direction: SortDirectionOrStr | None = SortDirection.ASC, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> WalletProductsListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the Wallet Products on your site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_products.list_wallet_products(page=1, per_page=50)
    # TODO: Handle 'response' of type WalletProductsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListWalletProductsErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_products.list_wallet_products(page=1, per_page=50)
    # TODO: Handle 'response' of type WalletProductsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListWalletProductsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include_archived</code> | <code>bool \| None</code> | Includes archived Wallet Products in the result. Defaults to `false`. Ignored when `status` is also sent.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[Status1OrStr](maxio_advanced_billing/models/enums/status1.py) \| None</code> | Restricts the result by status, and overrides `include_archived` when sent. An unrecognized value falls back to `active` rather than returning `422`.<br>**Default**: <code>None</code> |
| <code>q</code> | <code>str \| None</code> | Restricts the result to Wallet Products whose name, handle, or unit name contains this substring (case-insensitive).<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>[SortBy1OrStr](maxio_advanced_billing/models/enums/sort_by1.py) \| None</code> | The field to sort results by. An unrecognized value falls back to `name`.<br>**Default**: <code>SortBy1.NAME</code> |
| <code>sort_direction</code> | <code>[SortDirectionOrStr](maxio_advanced_billing/models/enums/sort_direction.py) \| None</code> | The sort direction. Anything other than `desc` is treated as `asc`.<br>**Default**: <code>SortDirection.ASC</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletProductsListResponse](maxio_advanced_billing/models/wallet_products_list_response.py)</code> -- OK. Unlike most list endpoints, this one is unpaginated (returns the full matching set in one response) unless `page` or `per_page` is sent; sending either turns on pagination, defaulting to 20 per page with a maximum of 200.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListWalletProductsErrorBody](maxio_advanced_billing/errors/list_wallet_products_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_wallet_product(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> WalletProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the Wallet Product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_products.read_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadWalletProductErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_products.read_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadWalletProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for example `handle:token-pack`). A bare handle returns `404`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletProductResponse](maxio_advanced_billing/models/wallet_product_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadWalletProductErrorBody](maxio_advanced_billing/errors/read_wallet_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_wallet_product_usage(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> WalletProductUsageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns everything drawing on this Wallet Product: the wallet templates billing through it, split into ones using its default price point and ones overriding it, plus a sample of up to 50 of the active wallets actually created from them. A wallet template can appear more than once in `wallet_templates`/`price_point_overrides`, once per Feature and owning plan/component sharing it, so these arrays aren't one row per template.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_products.read_wallet_product_usage("some example string")
    # TODO: Handle 'response' of type WalletProductUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadWalletProductUsageErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_products.read_wallet_product_usage("some example string")
    # TODO: Handle 'response' of type WalletProductUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadWalletProductUsageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for example `handle:token-pack`). A bare handle returns `404`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletProductUsageResponse](maxio_advanced_billing/models/wallet_product_usage_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadWalletProductUsageErrorBody](maxio_advanced_billing/errors/read_wallet_product_usage_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unarchive_wallet_product(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> WalletProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Restores an archived Wallet Product.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_products.unarchive_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnarchiveWalletProductErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_products.unarchive_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnarchiveWalletProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for example `handle:token-pack`). A bare handle returns `404`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletProductResponse](maxio_advanced_billing/models/wallet_product_response.py)</code> -- Wallet Product unarchived.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UnarchiveWalletProductErrorBody](maxio_advanced_billing/errors/unarchive_wallet_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_wallet_product(id_: str, *, body: UpdateWalletProductRequest | UpdateWalletProductRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletProductResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the Wallet Product's catalog-facing fields. Omitted fields are left unchanged. Unlike [Create Wallet Product]($e/Wallet%20Products/createWalletProduct), this does not accept `unit_name`, `handle`, `price_point`, or `price_points`; see the request schema for which fields are actually mutable.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_products.update_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateWalletProductErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_products.update_wallet_product("some example string")
    # TODO: Handle 'response' of type WalletProductResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateWalletProductErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for example `handle:token-pack`). A bare handle returns `404`. |
| <code>body</code> | <code>[UpdateWalletProductRequest](maxio_advanced_billing/models/update_wallet_product_request.py) \| [UpdateWalletProductRequestDict](maxio_advanced_billing/models/update_wallet_product_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletProductResponse](maxio_advanced_billing/models/wallet_product_response.py)</code> -- Wallet Product updated.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateWalletProductErrorBody](maxio_advanced_billing/errors/update_wallet_product_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WalletPurchases

> Source: [WalletPurchases](maxio_advanced_billing/apis/wallet_purchases.py)

<details>
<summary><code>def create_wallet_purchase(wallet_id: int, *, body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletPurchaseResultResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Purchases prepaid units for the wallet and charges the subscription's payment method for them, using the wallet's `price_point_id` unless a different price point is named. A successful purchase writes a grant of origin `purchase`, with its expiration following the funding entitlement's grant expiration policy.

How "charged" works depends on the subscription's collection method. For card/automatic collection, the payment is attempted immediately; a decline writes nothing to the wallet, and the call fails with a `422` naming the gateway's decline reason. For invoice-billed (remittance) subscriptions, there's no immediate charge to decline: an invoice is drafted, the wallet is credited right away, and the invoice is issued afterward. If issuing the invoice fails at that point, the invoice is left in draft state and reported for follow-up, but the call still returns `201` and the units already credited are **not** rolled back. See [Preview Wallet Purchase]($e/Wallet%20Purchases/previewWalletPurchase) to quote a price before charging anything.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_purchases.create_wallet_purchase(
        1, body=CreateWalletPurchaseRequest(purchase=Purchase(quantity="500.0"))
    )
    # TODO: Handle 'response' of type WalletPurchaseResultResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletPurchaseErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_purchases.create_wallet_purchase(
        1, body=CreateWalletPurchaseRequest(purchase=Purchase(quantity="500.0"))
    )
    # TODO: Handle 'response' of type WalletPurchaseResultResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletPurchaseErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wallet_id</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>body</code> | <code>[CreateWalletPurchaseRequest](maxio_advanced_billing/models/create_wallet_purchase_request.py) \| [CreateWalletPurchaseRequestDict](maxio_advanced_billing/models/create_wallet_purchase_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletPurchaseResultResponse](maxio_advanced_billing/models/wallet_purchase_result_response.py)</code> -- Purchase completed. Charges the subscription's payment method and, once payment succeeds, credits the wallet.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateWalletPurchaseErrorBody](maxio_advanced_billing/errors/create_wallet_purchase_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def preview_wallet_purchase(wallet_id: int, *, body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletPurchasePreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Quotes the price for a purchase at the given quantity and price point, without charging the payment method or writing to the wallet. Takes the same parameters as [Create Wallet Purchase]($e/Wallet%20Purchases/createWalletPurchase).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_purchases.preview_wallet_purchase(
        1, body=CreateWalletPurchaseRequest(purchase=Purchase(quantity="500.0"))
    )
    # TODO: Handle 'response' of type WalletPurchasePreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewWalletPurchaseErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_purchases.preview_wallet_purchase(
        1, body=CreateWalletPurchaseRequest(purchase=Purchase(quantity="500.0"))
    )
    # TODO: Handle 'response' of type WalletPurchasePreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PreviewWalletPurchaseErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wallet_id</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>body</code> | <code>[CreateWalletPurchaseRequest](maxio_advanced_billing/models/create_wallet_purchase_request.py) \| [CreateWalletPurchaseRequestDict](maxio_advanced_billing/models/create_wallet_purchase_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletPurchasePreviewResponse](maxio_advanced_billing/models/wallet_purchase_preview_response.py)</code> -- A price quote. Charges nothing and writes nothing to the wallet.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[PreviewWalletPurchaseErrorBody](maxio_advanced_billing/errors/preview_wallet_purchase_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WalletTransactions

> Source: [WalletTransactions](maxio_advanced_billing/apis/wallet_transactions.py)

<details>
<summary><code>def create_wallet_transaction(wallet_id: int, *, body: CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletTransactionResultResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Grants units to the wallet, or debits units from it, depending on `kind`. `amount` is always sent positive, and `kind` determines the direction written to the ledger.

**`kind: grant`**: a one-time manual top-up. On a non-negative balance, this creates a grant and writes one ledger row. On a negative balance, it repays the overdraft first (a `kind: grant` row with `grant_id: null`, for the repaid amount), then creates the grant: its `original` is always the full `amount` sent, and its `remaining` is what's left after the overdraft was repaid, which is `0` if the overdraft absorbed the whole top-up. The grant row is still written, and its `amount` is that `remaining`, not `original`, so the ledger rows sum to the balance change. A grant may carry `expires_at`; a debit may not.

**`kind: debit`**: direct consumption. Drains grants earliest-expiration-first, one `kind: debit` row per grant touched, plus any overdue expiration rows this same call triggers first (see below):
- Under the wallet's default `hard_stop_overflow: discard`, the drain is capped at the available balance. For a metered wallet, that cap is the live metered balance, not the stored one, so a debit can drain less than its stored balance would suggest, or even drain nothing at all (`201` with `drained_amount: "0.0"`) if live usage has already consumed what the ledger hadn't caught up to yet. A debit against a wallet whose *stored* balance is already zero or negative (`discard` only ever reaches zero) returns `422 "Wallet is depleted"`. Before that failure is returned, this call still expires any grants that were already overdue, so a `422` response can still leave new `kind: expiration` rows written.
- Under `hard_stop_overflow: allow_negative`, the full amount is deducted. The excess past the wallet's grants is booked as one overdraft row with `grant_id: null`, `rejected_amount` is always `"0.0"`, and the balance goes negative.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_transactions.create_wallet_transaction(
        1,
        body=CreateWalletTransactionRequest(
            wallet_transaction=WalletTransaction1(kind=Kind1.GRANT, amount="100.0", memo="Manual top-up")
        ),
    )
    # TODO: Handle 'response' of type WalletTransactionResultResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletTransactionErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_transactions.create_wallet_transaction(
        1,
        body=CreateWalletTransactionRequest(
            wallet_transaction=WalletTransaction1(kind=Kind1.GRANT, amount="100.0", memo="Manual top-up")
        ),
    )
    # TODO: Handle 'response' of type WalletTransactionResultResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletTransactionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wallet_id</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>body</code> | <code>[CreateWalletTransactionRequest](maxio_advanced_billing/models/create_wallet_transaction_request.py) \| [CreateWalletTransactionRequestDict](maxio_advanced_billing/models/create_wallet_transaction_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletTransactionResultResponse](maxio_advanced_billing/models/wallet_transaction_result_response.py)</code> -- Transaction applied. For `kind: grant`, the ledger row(s) written plus the new balance. For `kind: debit`, one row per grant touched plus the requested/drained/rejected accounting and the new balance.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateWalletTransactionErrorBody](maxio_advanced_billing/errors/create_wallet_transaction_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422, 500, 503 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_wallet_transactions(wallet_id: int, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None) -> WalletTransactionsListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the wallet's append-only ledger, newest first, paginated.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallet_transactions.list_wallet_transactions(1, page=1, per_page=50)
    # TODO: Handle 'response' of type WalletTransactionsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListWalletTransactionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wallet_transactions.list_wallet_transactions(1, page=1, per_page=50)
    # TODO: Handle 'response' of type WalletTransactionsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListWalletTransactionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>wallet_id</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletTransactionsListResponse](maxio_advanced_billing/models/wallet_transactions_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListWalletTransactionsErrorBody](maxio_advanced_billing/errors/list_wallet_transactions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Wallets

> Source: [Wallets](maxio_advanced_billing/apis/wallets.py)

<details>
<summary><code>def archive_wallet(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> WalletResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives the wallet: blocks further grants, debits, adjustments, and purchases (each returns `422`), stops any metered drawdown, and stops recurring funding (its schedule is deactivated with reason `wallet_archived`, not removed), while reads and the ledger stay available. Nothing already on the wallet is destroyed or clawed back, but nothing on it can be spent either, by any path, once archived. Idempotent: archiving an already-archived wallet returns the same `200`. There is no restore endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallets.archive_wallet(1)
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveWalletErrorBody
```

**Async**

```python
try:
    response = await async_client.wallets.archive_wallet(1)
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ArchiveWalletErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletResponse](maxio_advanced_billing/models/wallet_response.py)</code> -- The wallet, with `"status": "archived"`.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ArchiveWalletErrorBody](maxio_advanced_billing/errors/archive_wallet_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_wallet(*, body: CreateWalletRequest | CreateWalletRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a wallet owned by a subscription and denominated by a [Wallet Product]($e/Wallet%20Products/createWalletProduct): only a Wallet Product can denominate a wallet, not an ordinary component. The Wallet Product must be active; it never belongs to a product family, so there's no family check against the subscription. It's **immutable for the life of the wallet**; there's no way to repoint an existing wallet at a different one.

This endpoint always creates a `manual` wallet. To provision a wallet automatically from a usage-limit entitlement instead, configure `wallet_behavior` on the Feature behind that entitlement (see [the Wallets concept guide](page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature)) rather than sending `entitlement_id` here.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallets.create_wallet(
        body=CreateWalletRequest(wallet=Wallet1(subscription_id=23, wallet_product_id=76))
    )
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletErrorBody
```

**Async**

```python
try:
    response = await async_client.wallets.create_wallet(
        body=CreateWalletRequest(wallet=Wallet1(subscription_id=23, wallet_product_id=76))
    )
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWalletErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateWalletRequest](maxio_advanced_billing/models/create_wallet_request.py) \| [CreateWalletRequestDict](maxio_advanced_billing/models/create_wallet_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletResponse](maxio_advanced_billing/models/wallet_response.py)</code> -- Wallet created. The balance is `"0.0"` with no grants, unless a non-zero `initial_balance` was given. In that case, the balance and its seeded grant are already reflected.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateWalletErrorBody](maxio_advanced_billing/errors/create_wallet_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_wallets(*, page: int | None = 1, per_page: int | None = 20, subscription_id: int | None = None, status: Status2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletsListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the wallets on your site, in creation order, paginated. Without `subscription_id`, returns every wallet on the site. The API key is the tenancy boundary; `subscription_id` only narrows the result set further. Archived wallets are included unless you filter them out with `status=active`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallets.list_wallets(page=1, per_page=50)
    # TODO: Handle 'response' of type WalletsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListWalletsErrorBody
```

**Async**

```python
try:
    response = await async_client.wallets.list_wallets(page=1, per_page=50)
    # TODO: Handle 'response' of type WalletsListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListWalletsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>subscription_id</code> | <code>int \| None</code> | Restricts the result to wallets owned by this subscription.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[Status2OrStr](maxio_advanced_billing/models/enums/status2.py) \| None</code> | Restricts the result by wallet status. An unrecognized value returns `422` rather than being silently ignored.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletsListResponse](maxio_advanced_billing/models/wallets_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ListWalletsErrorBody](maxio_advanced_billing/errors/list_wallets_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def read_wallet(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> WalletResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the wallet's balance and grant breakdown. For an active, metered wallet on a site with metered consumption enabled, this is the only operation that computes a live balance from meter usage; see the wallet resource's `metered_*` fields. It is also the only operation where `balance` can differ from `posted_balance`, and a grant's `remaining` from its `posted_remaining`: the pending usage is drawn from the grants in drain order, so the grants' `remaining` add up to `balance`. Readable regardless of status. Archiving a wallet doesn't affect reads.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallets.read_wallet(1)
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadWalletErrorBody
```

**Async**

```python
try:
    response = await async_client.wallets.read_wallet(1)
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReadWalletErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletResponse](maxio_advanced_billing/models/wallet_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[ReadWalletErrorBody](maxio_advanced_billing/errors/read_wallet_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_wallet(id_: int, *, body: UpdateWalletRequest | UpdateWalletRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> WalletResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the wallet's editable attributes. Only `name` is editable; any other attribute in the body is ignored. Send only the attributes to change.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wallets.update_wallet(1, body=UpdateWalletRequest(wallet=Wallet2(name="Onboarding credits")))
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateWalletErrorBody
```

**Async**

```python
try:
    response = await async_client.wallets.update_wallet(
        1, body=UpdateWalletRequest(wallet=Wallet2(name="Onboarding credits"))
    )
    # TODO: Handle 'response' of type WalletResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateWalletErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | The Advanced Billing id of the wallet. |
| <code>body</code> | <code>[UpdateWalletRequest](maxio_advanced_billing/models/update_wallet_request.py) \| [UpdateWalletRequestDict](maxio_advanced_billing/models/update_wallet_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WalletResponse](maxio_advanced_billing/models/wallet_response.py)</code> -- The updated wallet. Reports the stored balance, equal to `posted_balance`, with the `metered_*` fields `null`, as on list, create, and archive.

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateWalletErrorBody](maxio_advanced_billing/errors/update_wallet_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 404, 422 | <code>[WalletErrorResponse1](maxio_advanced_billing/models/wallet_error_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Webhooks

> Source: [Webhooks](maxio_advanced_billing/apis/webhooks.py)

<details>
<summary><code>def create_endpoint(*, body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> EndpointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an endpoint and assigns a list of webhook subscriptions (events) to it.
See the [Webhooks Reference](page:introduction/webhooks/webhooks-reference#events) page for available events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.webhooks.create_endpoint(
        body=CreateOrUpdateEndpointRequest(
            endpoint=CreateOrUpdateEndpoint(
                url="https://your.site/webhooks",
                webhook_subscriptions=[
                    WebhookSubscription.PAYMENT_SUCCESS,
                    WebhookSubscription.PAYMENT_FAILURE,
                    WebhookSubscription.INVOICE_PENDING,
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type EndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateEndpointErrorBody
```

**Async**

```python
try:
    response = await async_client.webhooks.create_endpoint(
        body=CreateOrUpdateEndpointRequest(
            endpoint=CreateOrUpdateEndpoint(
                url="https://your.site/webhooks",
                webhook_subscriptions=[
                    WebhookSubscription.PAYMENT_SUCCESS,
                    WebhookSubscription.PAYMENT_FAILURE,
                    WebhookSubscription.INVOICE_PENDING,
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type EndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateEndpointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateOrUpdateEndpointRequest](maxio_advanced_billing/models/create_or_update_endpoint_request.py) \| [CreateOrUpdateEndpointRequestDict](maxio_advanced_billing/models/create_or_update_endpoint_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EndpointResponse](maxio_advanced_billing/models/endpoint_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[CreateEndpointErrorBody](maxio_advanced_billing/errors/create_endpoint_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_webhooks(*, body: EnableWebhooksRequest | EnableWebhooksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> EnableWebhooksResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables webhooks for your site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.webhooks.enable_webhooks(body=EnableWebhooksRequest(webhooks_enabled=True))
    # TODO: Handle 'response' of type EnableWebhooksResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.webhooks.enable_webhooks(body=EnableWebhooksRequest(webhooks_enabled=True))
    # TODO: Handle 'response' of type EnableWebhooksResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[EnableWebhooksRequest](maxio_advanced_billing/models/enable_webhooks_request.py) \| [EnableWebhooksRequestDict](maxio_advanced_billing/models/enable_webhooks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EnableWebhooksResponse](maxio_advanced_billing/models/enable_webhooks_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_endpoints(*, request_options: RequestOptionsOrDict | None = None) -> list[Endpoint]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists endpoints configured for a site.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.webhooks.list_endpoints()
    # TODO: Handle 'response' of type list[Endpoint]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.webhooks.list_endpoints()
    # TODO: Handle 'response' of type list[Endpoint]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[Endpoint](maxio_advanced_billing/models/endpoint.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_webhooks(*, status: WebhookStatusOrStr | None = None, since_date: str | None = None, until_date: str | None = None, page: int | None = 1, per_page: int | None = 20, order: WebhookOrderOrStr | None = None, subscription: int | None = None, request_options: RequestOptionsOrDict | None = None) -> list[WebhookResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of webhooks.  You can pass query parameters if you want to filter webhooks. See the [Webhooks](page:introduction/webhooks/webhooks) documentation for more information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.webhooks.list_webhooks(page=1, per_page=50)
    # TODO: Handle 'response' of type list[WebhookResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.webhooks.list_webhooks(page=1, per_page=50)
    # TODO: Handle 'response' of type list[WebhookResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>status</code> | <code>[WebhookStatusOrStr](maxio_advanced_billing/models/enums/webhook_status.py) \| None</code> | Webhooks with matching status would be returned.<br>**Default**: <code>None</code> |
| <code>since_date</code> | <code>str \| None</code> | Format YYYY-MM-DD. Returns Webhooks with the created_at date greater than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>until_date</code> | <code>str \| None</code> | Format YYYY-MM-DD. Returns Webhooks with the created_at date less than or equal to the one specified.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: <code>1</code> |
| <code>per_page</code> | <code>int \| None</code> | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: <code>20</code> |
| <code>order</code> | <code>[WebhookOrderOrStr](maxio_advanced_billing/models/enums/webhook_order.py) \| None</code> | The order in which the Webhooks are returned.<br>**Default**: <code>None</code> |
| <code>subscription</code> | <code>int \| None</code> | The Advanced Billing id of a subscription you'd like to filter for<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[WebhookResponse](maxio_advanced_billing/models/webhook_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def replay_webhooks(*, body: ReplayWebhooksRequest | ReplayWebhooksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ReplayWebhooksResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Replays webhooks. Posting to this endpoint does not immediately resend the webhooks. They are added to a queue and sent as soon as possible, depending on available system resources. You can submit an array of up to 1000 webhook IDs in the replay request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.webhooks.replay_webhooks(body=ReplayWebhooksRequest(ids=[123456789, 123456788]))
    # TODO: Handle 'response' of type ReplayWebhooksResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.webhooks.replay_webhooks(body=ReplayWebhooksRequest(ids=[123456789, 123456788]))
    # TODO: Handle 'response' of type ReplayWebhooksResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ReplayWebhooksRequest](maxio_advanced_billing/models/replay_webhooks_request.py) \| [ReplayWebhooksRequestDict](maxio_advanced_billing/models/replay_webhooks_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReplayWebhooksResponse](maxio_advanced_billing/models/replay_webhooks_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[RawError](maxio_advanced_billing/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_endpoint(endpoint_id: int, *, body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> EndpointResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an Endpoint. You can change the `url` of your endpoint or the list of `webhook_subscriptions` to which you are subscribed. See the [Webhooks Reference](page:introduction/webhooks/webhooks-reference#events) page for available events.

Always send a complete list of events to which you want to subscribe. Sending a PUT request for an existing endpoint with an empty list of `webhook_subscriptions` will unsubscribe all events.

If you want to unsubscribe from a specific event, send a list of `webhook_subscriptions` without the specific event key.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.webhooks.update_endpoint(
        1,
        body=CreateOrUpdateEndpointRequest(
            endpoint=CreateOrUpdateEndpoint(
                url="https://your.site/webhooks/1/json.",
                webhook_subscriptions=[
                    WebhookSubscription.PAYMENT_FAILURE,
                    WebhookSubscription.PAYMENT_SUCCESS,
                    WebhookSubscription.REFUND_FAILURE,
                    WebhookSubscription.INVOICE_PENDING,
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type EndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateEndpointErrorBody
```

**Async**

```python
try:
    response = await async_client.webhooks.update_endpoint(
        1,
        body=CreateOrUpdateEndpointRequest(
            endpoint=CreateOrUpdateEndpoint(
                url="https://your.site/webhooks/1/json.",
                webhook_subscriptions=[
                    WebhookSubscription.PAYMENT_FAILURE,
                    WebhookSubscription.PAYMENT_SUCCESS,
                    WebhookSubscription.REFUND_FAILURE,
                    WebhookSubscription.INVOICE_PENDING,
                ],
            ),
        ),
    )
    # TODO: Handle 'response' of type EndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateEndpointErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>endpoint_id</code> | <code>int</code> | The Advanced Billing id for the endpoint that should be updated |
| <code>body</code> | <code>[CreateOrUpdateEndpointRequest](maxio_advanced_billing/models/create_or_update_endpoint_request.py) \| [CreateOrUpdateEndpointRequestDict](maxio_advanced_billing/models/create_or_update_endpoint_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](maxio_advanced_billing/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EndpointResponse](maxio_advanced_billing/models/endpoint_response.py)</code> -- OK

**OnError**: <code>[ApiError](maxio_advanced_billing/core/exceptions.py)&#91;[UpdateEndpointErrorBody](maxio_advanced_billing/errors/update_endpoint_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |
| 422 | <code>[ErrorListResponse1](maxio_advanced_billing/models/error_list_response1.py)</code> |
| anything unmapped | <code>[RawError](maxio_advanced_billing/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

