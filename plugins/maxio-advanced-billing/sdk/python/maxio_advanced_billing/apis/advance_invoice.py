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
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.issue_advance_invoice_error import IssueAdvanceInvoiceErrorBody, issue_advance_invoice_error_mapper
from ..errors.read_advance_invoice_error import ReadAdvanceInvoiceErrorBody, read_advance_invoice_error_mapper
from ..errors.void_advance_invoice_error import VoidAdvanceInvoiceErrorBody, void_advance_invoice_error_mapper
from ..models.invoice import Invoice
from ..models.issue_advance_invoice_request import IssueAdvanceInvoiceRequest, IssueAdvanceInvoiceRequestDict
from ..models.void_invoice_request import VoidInvoiceRequest, VoidInvoiceRequestDict
from ..server.server import Server


class AdvanceInvoice:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AdvanceInvoiceWithRawResponse(client, server, auth)

    def issue_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: IssueAdvanceInvoiceRequest | IssueAdvanceInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Issues an invoice in advance for a subscription's next renewal date. For the most part, advance invoices
        function like any other invoice, except they are issued early and have special behavior upon being voided. For
        more information on advance invoices, including eligibility for generating one, see `Issue Invoice In Advance
        <https://maxio.zendesk.com/hc/en-us/articles/24252026404749-Issue-Invoice-In-Advance>`__.

        A subscription can only have one advance invoice per billing period. Attempting to issue an advance invoice when
        one already exists returns an error.

        Regeneration of the invoice can be forced with the params ``force: true``, which voids an advance invoice if one
        exists and generates a new one. If no advance invoice exists, a new one is generated.

        Consider using either the create or preview endpoints for proforma invoices to preview this advance invoice
        before using this endpoint to generate it.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.issue_advance_invoice(subscription_id, body=body, request_options=request_options)
        )

    def read_advance_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> Invoice:
        """Returns the advance invoice generated for a subscription's upcoming renewal. There can only be one advance
        invoice per subscription per billing cycle.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_advance_invoice(subscription_id, request_options=request_options))

    def void_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Voids a subscription's existing advance invoice. Once voided, it can later be regenerated if desired.

        A ``reason`` is required to void, and the invoice must have an open status. Voiding causes any prepayments and
        credits that were applied to the invoice to be returned to the subscription.

        For a full overview of the impact of voiding, see `Invoice <$m/Invoice>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.void_advance_invoice(subscription_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AdvanceInvoiceWithRawResponse:
        return self._with_raw_response


class AsyncAdvanceInvoice:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAdvanceInvoiceWithRawResponse(client, server, auth)

    async def issue_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: IssueAdvanceInvoiceRequest | IssueAdvanceInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Issues an invoice in advance for a subscription's next renewal date. For the most part, advance invoices
        function like any other invoice, except they are issued early and have special behavior upon being voided. For
        more information on advance invoices, including eligibility for generating one, see `Issue Invoice In Advance
        <https://maxio.zendesk.com/hc/en-us/articles/24252026404749-Issue-Invoice-In-Advance>`__.

        A subscription can only have one advance invoice per billing period. Attempting to issue an advance invoice when
        one already exists returns an error.

        Regeneration of the invoice can be forced with the params ``force: true``, which voids an advance invoice if one
        exists and generates a new one. If no advance invoice exists, a new one is generated.

        Consider using either the create or preview endpoints for proforma invoices to preview this advance invoice
        before using this endpoint to generate it.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.issue_advance_invoice(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def read_advance_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> Invoice:
        """Returns the advance invoice generated for a subscription's upcoming renewal. There can only be one advance
        invoice per subscription per billing cycle.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_advance_invoice(subscription_id, request_options=request_options)
        )

    async def void_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Voids a subscription's existing advance invoice. Once voided, it can later be regenerated if desired.

        A ``reason`` is required to void, and the invoice must have an open status. Voiding causes any prepayments and
        credits that were applied to the invoice to be returned to the subscription.

        For a full overview of the impact of voiding, see `Invoice <$m/Invoice>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.void_advance_invoice(
                subscription_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncAdvanceInvoiceWithRawResponse:
        return self._with_raw_response


class AdvanceInvoiceWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def issue_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: IssueAdvanceInvoiceRequest | IssueAdvanceInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, IssueAdvanceInvoiceErrorBody]:
        """Issues an invoice in advance for a subscription's next renewal date. For the most part, advance invoices
        function like any other invoice, except they are issued early and have special behavior upon being voided. For
        more information on advance invoices, including eligibility for generating one, see `Issue Invoice In Advance
        <https://maxio.zendesk.com/hc/en-us/articles/24252026404749-Issue-Invoice-In-Advance>`__.

        A subscription can only have one advance invoice per billing period. Attempting to issue an advance invoice when
        one already exists returns an error.

        Regeneration of the invoice can be forced with the params ``force: true``, which voids an advance invoice if one
        exists and generates a new one. If no advance invoice exists, a new one is generated.

        Consider using either the create or preview endpoints for proforma invoices to preview this advance invoice
        before using this endpoint to generate it.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/advance_invoice/issue.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueAdvanceInvoiceRequest | IssueAdvanceInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=issue_advance_invoice_error_mapper,
            request_options=request_options,
        )

    def read_advance_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, ReadAdvanceInvoiceErrorBody]:
        """Returns the advance invoice generated for a subscription's upcoming renewal. There can only be one advance
        invoice per subscription per billing cycle.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/advance_invoice.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=read_advance_invoice_error_mapper,
            request_options=request_options,
        )

    def void_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, VoidAdvanceInvoiceErrorBody]:
        """Voids a subscription's existing advance invoice. Once voided, it can later be regenerated if desired.

        A ``reason`` is required to void, and the invoice must have an open status. Voiding causes any prepayments and
        credits that were applied to the invoice to be returned to the subscription.

        For a full overview of the impact of voiding, see `Invoice <$m/Invoice>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/advance_invoice/void.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidInvoiceRequest | VoidInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=void_advance_invoice_error_mapper,
            request_options=request_options,
        )


class AsyncAdvanceInvoiceWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def issue_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: IssueAdvanceInvoiceRequest | IssueAdvanceInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, IssueAdvanceInvoiceErrorBody]:
        """Issues an invoice in advance for a subscription's next renewal date. For the most part, advance invoices
        function like any other invoice, except they are issued early and have special behavior upon being voided. For
        more information on advance invoices, including eligibility for generating one, see `Issue Invoice In Advance
        <https://maxio.zendesk.com/hc/en-us/articles/24252026404749-Issue-Invoice-In-Advance>`__.

        A subscription can only have one advance invoice per billing period. Attempting to issue an advance invoice when
        one already exists returns an error.

        Regeneration of the invoice can be forced with the params ``force: true``, which voids an advance invoice if one
        exists and generates a new one. If no advance invoice exists, a new one is generated.

        Consider using either the create or preview endpoints for proforma invoices to preview this advance invoice
        before using this endpoint to generate it.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/advance_invoice/issue.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueAdvanceInvoiceRequest | IssueAdvanceInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=issue_advance_invoice_error_mapper,
            request_options=request_options,
        )

    async def read_advance_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, ReadAdvanceInvoiceErrorBody]:
        """Returns the advance invoice generated for a subscription's upcoming renewal. There can only be one advance
        invoice per subscription per billing cycle.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/advance_invoice.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=read_advance_invoice_error_mapper,
            request_options=request_options,
        )

    async def void_advance_invoice(
        self,
        subscription_id: int,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, VoidAdvanceInvoiceErrorBody]:
        """Voids a subscription's existing advance invoice. Once voided, it can later be regenerated if desired.

        A ``reason`` is required to void, and the invoice must have an open status. Voiding causes any prepayments and
        credits that were applied to the invoice to be returned to the subscription.

        For a full overview of the impact of voiding, see `Invoice <$m/Invoice>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/advance_invoice/void.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidInvoiceRequest | VoidInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=void_advance_invoice_error_mapper,
            request_options=request_options,
        )
