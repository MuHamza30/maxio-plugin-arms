from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.export_invoices_error import ExportInvoicesErrorBody, export_invoices_error_mapper
from ..errors.export_proforma_invoices_error import (
    ExportProformaInvoicesErrorBody,
    export_proforma_invoices_error_mapper,
)
from ..errors.export_subscriptions_error import ExportSubscriptionsErrorBody, export_subscriptions_error_mapper
from ..errors.list_exported_invoices_error import ListExportedInvoicesErrorBody, list_exported_invoices_error_mapper
from ..errors.list_exported_proforma_invoices_error import (
    ListExportedProformaInvoicesErrorBody,
    list_exported_proforma_invoices_error_mapper,
)
from ..errors.list_exported_subscriptions_error import (
    ListExportedSubscriptionsErrorBody,
    list_exported_subscriptions_error_mapper,
)
from ..errors.read_invoices_export_error import ReadInvoicesExportErrorBody, read_invoices_export_error_mapper
from ..errors.read_proforma_invoices_export_error import (
    ReadProformaInvoicesExportErrorBody,
    read_proforma_invoices_export_error_mapper,
)
from ..errors.read_subscriptions_export_error import (
    ReadSubscriptionsExportErrorBody,
    read_subscriptions_export_error_mapper,
)
from ..models.batch_job_response import BatchJobResponse
from ..models.invoice import Invoice
from ..models.proforma_invoice import ProformaInvoice
from ..models.subscription import Subscription
from ..server.server import Server


class ApiExports:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApiExportsWithRawResponse(client, server, auth)

    def export_invoices(self, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse:
        """Creates an invoices export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Conflict ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.export_invoices(request_options=request_options))

    def export_proforma_invoices(self, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse:
        """Creates a proforma invoices export and returns a batch job object. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Conflict ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.export_proforma_invoices(request_options=request_options))

    def export_subscriptions(self, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse:
        """Creates a subscriptions export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Conflict ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.export_subscriptions(request_options=request_options))

    def list_exported_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Invoice]:
        """Lists exported invoices for a provided ``batch_id``. Use pagination to control responses returned from the
        server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_exported_invoices(
                batch_id, per_page=per_page, page=page, request_options=request_options
            ),
        )

    def list_exported_proforma_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProformaInvoice]:
        """Lists exported proforma invoices for a provided ``batch_id``. Use pagination to control responses returned
        from the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_exported_proforma_invoices(
                batch_id, per_page=per_page, page=page, request_options=request_options
            ),
        )

    def list_exported_subscriptions(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Subscription]:
        """Lists exported subscriptions for a provided ``batch_id``. Use pagination to control responses returned from
        the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_exported_subscriptions(
                batch_id, per_page=per_page, page=page, request_options=request_options
            ),
        )

    def read_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchJobResponse:
        """Returns a batch job object for an invoices export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_invoices_export(batch_id, request_options=request_options))

    def read_proforma_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchJobResponse:
        """Returns a batch job object for a proforma invoices export. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_proforma_invoices_export(batch_id, request_options=request_options))

    def read_subscriptions_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchJobResponse:
        """Returns a batch job object for a subscriptions export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_subscriptions_export(batch_id, request_options=request_options))

    @property
    def with_raw_response(self) -> ApiExportsWithRawResponse:
        return self._with_raw_response


class AsyncApiExports:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApiExportsWithRawResponse(client, server, auth)

    async def export_invoices(self, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse:
        """Creates an invoices export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Conflict ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.export_invoices(request_options=request_options))

    async def export_proforma_invoices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchJobResponse:
        """Creates a proforma invoices export and returns a batch job object. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Conflict ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.export_proforma_invoices(request_options=request_options))

    async def export_subscriptions(self, *, request_options: RequestOptionsOrDict | None = None) -> BatchJobResponse:
        """Creates a subscriptions export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Conflict ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.export_subscriptions(request_options=request_options))

    async def list_exported_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Invoice]:
        """Lists exported invoices for a provided ``batch_id``. Use pagination to control responses returned from the
        server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_exported_invoices(
                batch_id, per_page=per_page, page=page, request_options=request_options
            ),
        )

    async def list_exported_proforma_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProformaInvoice]:
        """Lists exported proforma invoices for a provided ``batch_id``. Use pagination to control responses returned
        from the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_exported_proforma_invoices(
                batch_id, per_page=per_page, page=page, request_options=request_options
            ),
        )

    async def list_exported_subscriptions(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Subscription]:
        """Lists exported subscriptions for a provided ``batch_id``. Use pagination to control responses returned from
        the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_exported_subscriptions(
                batch_id, per_page=per_page, page=page, request_options=request_options
            ),
        )

    async def read_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchJobResponse:
        """Returns a batch job object for an invoices export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_invoices_export(batch_id, request_options=request_options))

    async def read_proforma_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchJobResponse:
        """Returns a batch job object for a proforma invoices export. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_proforma_invoices_export(batch_id, request_options=request_options)
        )

    async def read_subscriptions_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchJobResponse:
        """Returns a batch job object for a subscriptions export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_subscriptions_export(batch_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncApiExportsWithRawResponse:
        return self._with_raw_response


class ApiExportsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def export_invoices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ExportInvoicesErrorBody]:
        """Creates an invoices export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/api_exports/invoices.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BatchJobResponse],
            error_mapper=export_invoices_error_mapper,
            request_options=request_options,
        )

    def export_proforma_invoices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ExportProformaInvoicesErrorBody]:
        """Creates a proforma invoices export and returns a batch job object. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/api_exports/proforma_invoices.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BatchJobResponse],
            error_mapper=export_proforma_invoices_error_mapper,
            request_options=request_options,
        )

    def export_subscriptions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ExportSubscriptionsErrorBody]:
        """Creates a subscriptions export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/api_exports/subscriptions.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BatchJobResponse],
            error_mapper=export_subscriptions_error_mapper,
            request_options=request_options,
        )

    def list_exported_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Invoice], ListExportedInvoicesErrorBody]:
        """Lists exported invoices for a provided ``batch_id``. Use pagination to control responses returned from the
        server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/invoices/{batch_id}/rows.json"),
            path_params=[param[str]("batch_id", batch_id)],
            query_params=[param[int | None]("per_page", per_page), param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[Invoice]],
            error_mapper=list_exported_invoices_error_mapper,
            request_options=request_options,
        )

    def list_exported_proforma_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProformaInvoice], ListExportedProformaInvoicesErrorBody]:
        """Lists exported proforma invoices for a provided ``batch_id``. Use pagination to control responses returned
        from the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/proforma_invoices/{batch_id}/rows.json"),
            path_params=[param[str]("batch_id", batch_id)],
            query_params=[param[int | None]("per_page", per_page), param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ProformaInvoice]],
            error_mapper=list_exported_proforma_invoices_error_mapper,
            request_options=request_options,
        )

    def list_exported_subscriptions(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Subscription], ListExportedSubscriptionsErrorBody]:
        """Lists exported subscriptions for a provided ``batch_id``. Use pagination to control responses returned from
        the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/subscriptions/{batch_id}/rows.json"),
            path_params=[param[str]("batch_id", batch_id)],
            query_params=[param[int | None]("per_page", per_page), param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[Subscription]],
            error_mapper=list_exported_subscriptions_error_mapper,
            request_options=request_options,
        )

    def read_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ReadInvoicesExportErrorBody]:
        """Returns a batch job object for an invoices export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/invoices/{batch_id}.json"),
            path_params=[param[str]("batch_id", batch_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BatchJobResponse],
            error_mapper=read_invoices_export_error_mapper,
            request_options=request_options,
        )

    def read_proforma_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ReadProformaInvoicesExportErrorBody]:
        """Returns a batch job object for a proforma invoices export. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/proforma_invoices/{batch_id}.json"),
            path_params=[param[str]("batch_id", batch_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BatchJobResponse],
            error_mapper=read_proforma_invoices_export_error_mapper,
            request_options=request_options,
        )

    def read_subscriptions_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ReadSubscriptionsExportErrorBody]:
        """Returns a batch job object for a subscriptions export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/subscriptions/{batch_id}.json"),
            path_params=[param[str]("batch_id", batch_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BatchJobResponse],
            error_mapper=read_subscriptions_export_error_mapper,
            request_options=request_options,
        )


class AsyncApiExportsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def export_invoices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ExportInvoicesErrorBody]:
        """Creates an invoices export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/api_exports/invoices.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BatchJobResponse],
            error_mapper=export_invoices_error_mapper,
            request_options=request_options,
        )

    async def export_proforma_invoices(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ExportProformaInvoicesErrorBody]:
        """Creates a proforma invoices export and returns a batch job object. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/api_exports/proforma_invoices.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BatchJobResponse],
            error_mapper=export_proforma_invoices_error_mapper,
            request_options=request_options,
        )

    async def export_subscriptions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ExportSubscriptionsErrorBody]:
        """Creates a subscriptions export and returns a batch job object.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/api_exports/subscriptions.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BatchJobResponse],
            error_mapper=export_subscriptions_error_mapper,
            request_options=request_options,
        )

    async def list_exported_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Invoice], ListExportedInvoicesErrorBody]:
        """Lists exported invoices for a provided ``batch_id``. Use pagination to control responses returned from the
        server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/invoices/{batch_id}/rows.json"),
            path_params=[param[str]("batch_id", batch_id)],
            query_params=[param[int | None]("per_page", per_page), param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[Invoice]],
            error_mapper=list_exported_invoices_error_mapper,
            request_options=request_options,
        )

    async def list_exported_proforma_invoices(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProformaInvoice], ListExportedProformaInvoicesErrorBody]:
        """Lists exported proforma invoices for a provided ``batch_id``. Use pagination to control responses returned
        from the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/proforma_invoices/{batch_id}/rows.json"),
            path_params=[param[str]("batch_id", batch_id)],
            query_params=[param[int | None]("per_page", per_page), param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ProformaInvoice]],
            error_mapper=list_exported_proforma_invoices_error_mapper,
            request_options=request_options,
        )

    async def list_exported_subscriptions(
        self,
        batch_id: str,
        *,
        per_page: int | None = 100,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Subscription], ListExportedSubscriptionsErrorBody]:
        """Lists exported subscriptions for a provided ``batch_id``. Use pagination to control responses returned from
        the server.

        Example: ``GET https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1``.

        Args:
            batch_id: Id of a Batch Job.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/subscriptions/{batch_id}/rows.json"),
            path_params=[param[str]("batch_id", batch_id)],
            query_params=[param[int | None]("per_page", per_page), param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[Subscription]],
            error_mapper=list_exported_subscriptions_error_mapper,
            request_options=request_options,
        )

    async def read_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ReadInvoicesExportErrorBody]:
        """Returns a batch job object for an invoices export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/invoices/{batch_id}.json"),
            path_params=[param[str]("batch_id", batch_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BatchJobResponse],
            error_mapper=read_invoices_export_error_mapper,
            request_options=request_options,
        )

    async def read_proforma_invoices_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ReadProformaInvoicesExportErrorBody]:
        """Returns a batch job object for a proforma invoices export. Proforma invoices are only available on
        Relationship Invoicing sites.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/proforma_invoices/{batch_id}.json"),
            path_params=[param[str]("batch_id", batch_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BatchJobResponse],
            error_mapper=read_proforma_invoices_export_error_mapper,
            request_options=request_options,
        )

    async def read_subscriptions_export(
        self, batch_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchJobResponse, ReadSubscriptionsExportErrorBody]:
        """Returns a batch job object for a subscriptions export.

        Args:
            batch_id: Id of a Batch Job.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/api_exports/subscriptions/{batch_id}.json"),
            path_params=[param[str]("batch_id", batch_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BatchJobResponse],
            error_mapper=read_subscriptions_export_error_mapper,
            request_options=request_options,
        )
