from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.create_consolidated_proforma_invoice_error import (
    CreateConsolidatedProformaInvoiceErrorBody,
    create_consolidated_proforma_invoice_error_mapper,
)
from ..errors.create_proforma_invoice_error import CreateProformaInvoiceErrorBody, create_proforma_invoice_error_mapper
from ..errors.create_signup_proforma_invoice_error import (
    CreateSignupProformaInvoiceErrorBody,
    create_signup_proforma_invoice_error_mapper,
)
from ..errors.deliver_proforma_invoice_error import (
    DeliverProformaInvoiceErrorBody,
    deliver_proforma_invoice_error_mapper,
)
from ..errors.list_subscription_group_proforma_invoices_error import (
    ListSubscriptionGroupProformaInvoicesErrorBody,
    list_subscription_group_proforma_invoices_error_mapper,
)
from ..errors.preview_proforma_invoice_error import (
    PreviewProformaInvoiceErrorBody,
    preview_proforma_invoice_error_mapper,
)
from ..errors.preview_signup_proforma_invoice_error import (
    PreviewSignupProformaInvoiceErrorBody,
    preview_signup_proforma_invoice_error_mapper,
)
from ..errors.read_proforma_invoice_error import ReadProformaInvoiceErrorBody, read_proforma_invoice_error_mapper
from ..errors.void_proforma_invoice_error import VoidProformaInvoiceErrorBody, void_proforma_invoice_error_mapper
from ..models.create_subscription_request import CreateSubscriptionRequest, CreateSubscriptionRequestDict
from ..models.deliver_proforma_invoice_request import DeliverProformaInvoiceRequest, DeliverProformaInvoiceRequestDict
from ..models.enums.create_signup_proforma_preview_include import CreateSignupProformaPreviewIncludeOrStr
from ..models.enums.direction import Direction, DirectionOrStr
from ..models.enums.proforma_invoice_status import ProformaInvoiceStatusOrStr
from ..models.list_proforma_invoices_response import ListProformaInvoicesResponse
from ..models.proforma_invoice import ProformaInvoice
from ..models.signup_proforma_preview_response import SignupProformaPreviewResponse
from ..models.void_invoice_request import VoidInvoiceRequest, VoidInvoiceRequestDict
from ..server.server import Server


class ProformaInvoices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProformaInvoicesWithRawResponse(client, server, auth)

    def create_consolidated_proforma_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Creates a consolidated proforma invoice asynchronously. To find and view the new consolidated proforma
        invoice, you can poll the subscription group listing for proforma invoices; only one consolidated proforma
        invoice can be created per group at a time.

        If the information becomes outdated, simply void the old consolidated proforma invoice and generate a new one.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be prepaid, and must be in a live state.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_consolidated_proforma_invoice(uid, request_options=request_options)
        )

    def create_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProformaInvoice:
        """Creates a proforma invoice and returns it as a response. If the information becomes outdated, simply void the
        old proforma invoice and generate a new one.

        If you would like to preview the next billing amounts without generating a full proforma invoice, use the
        renewal preview endpoint.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be in a group, must not be prepaid, and must be in a live state.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_proforma_invoice(subscription_id, request_options=request_options))

    def create_signup_proforma_invoice(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProformaInvoice:
        """Creates a proforma invoice to preview costs before a subscription's signup. This endpoint is only available
        for Relationship Invoicing sites and cannot be used to create consolidated proforma invoices or preview prepaid
        subscriptions. Like other proforma invoices, it can be emailed to the customer, voided, and publicly viewed on
        the chargifypay domain.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements. We recommend associating
        the proforma invoice with a customer_id to easily find their proforma invoices, since the subscription_id will
        always be blank.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Unprocessable Entity (WebDAV) ``error`` is ``ProformaBadRequestErrorResponse1 |
                ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_signup_proforma_invoice(body=body, request_options=request_options)
        )

    def deliver_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: DeliverProformaInvoiceRequest | DeliverProformaInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProformaInvoice:
        """Delivers a proforma invoice programmatically via email. Supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        If ``recipient_emails`` is omitted, the system will fall back to the primary recipient derived from the invoice
        or subscription. At least one recipient must be present, either via the request body or via this default
        behavior, so an empty body may still succeed when defaults are available.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.deliver_proforma_invoice(
                proforma_invoice_uid, body=body, request_options=request_options
            ),
        )

    def list_proforma_invoices(
        self,
        subscription_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: ProformaInvoiceStatusOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProformaInvoicesResponse:
        """Lists proforma invoices for a subscription. By default, results only include totals, not detailed breakdowns
        for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or ``custom_fields``. To include
        breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            subscription_id: The Chargify id of the subscription.
            start_date: The beginning date range for the invoice's Due Date, in the YYYY-MM-DD format.
            end_date: The ending date range for the invoice's Due Date, in the YYYY-MM-DD format.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned invoices.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_proforma_invoices(
                subscription_id,
                start_date=start_date,
                end_date=end_date,
                status=status,
                page=page,
                per_page=per_page,
                direction=direction,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                credits_=credits_,
                payments=payments,
                custom_fields=custom_fields,
                request_options=request_options,
            ),
        )

    def list_subscription_group_proforma_invoices(
        self,
        uid: str,
        *,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProformaInvoicesResponse:
        """Lists proforma invoices with a ``consolidation_level`` of parent for the subscription group.

        By default, proforma invoices returned on the index will only include totals, not detailed breakdowns for
        ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``. To include breakdowns,
        pass the specific field as a key in the query with a value set to true.

        Args:
            uid: The uid of the subscription group
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_subscription_group_proforma_invoices(
                uid,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                credits_=credits_,
                payments=payments,
                custom_fields=custom_fields,
                request_options=request_options,
            ),
        )

    def preview_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProformaInvoice:
        """Previews the data that will be included on a given subscription's proforma invoice if one were to be
        generated. It will have similar line items and totals as a renewal preview, but the response will be presented
        in the format of a proforma invoice. Consequently it will include additional information such as the name and
        addresses that will appear on the proforma invoice.

        The preview endpoint is subject to all the same conditions as the proforma invoice endpoint. For example,
        previews are only available on the Relationship Invoicing architecture, and previews cannot be made for
        end-of-life subscriptions.

        If all the data returned in the preview is as expected, you may then create a static proforma invoice and send
        it to your customer. The data within a preview will not be saved and will not be accessible after the call is
        made.

        Alternatively, if you have some proforma invoices already, you may make a preview call to determine whether any
        billing information for the subscription's upcoming renewal has changed.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.preview_proforma_invoice(subscription_id, request_options=request_options)
        )

    def preview_signup_proforma_invoice(
        self,
        *,
        include: CreateSignupProformaPreviewIncludeOrStr | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignupProformaPreviewResponse:
        """Creates a signup preview in the format of a proforma invoice to preview costs before a subscription's signup.
        This endpoint is only available for Relationship Invoicing sites and cannot be used to create consolidated
        proforma invoice previews or preview prepaid subscriptions. You have the option of previewing the first
        renewal's costs as well. The proforma invoice preview will not be persisted.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements.

        Args:
            include: Choose to include a proforma invoice preview for the first renewal. Use in query
                ``include=next_proforma_invoice``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Unprocessable Entity (WebDAV) ``error`` is ``ProformaBadRequestErrorResponse1 |
                ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.preview_signup_proforma_invoice(
                include=include, body=body, request_options=request_options
            ),
        )

    def read_proforma_invoice(
        self, proforma_invoice_uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProformaInvoice:
        """Returns the details of an existing proforma invoice.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_proforma_invoice(proforma_invoice_uid, request_options=request_options)
        )

    def void_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProformaInvoice:
        """Voids a proforma invoice that has the status "draft".

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Only proforma invoices that have the appropriate status may be reopened. If the invoice identified by {uid} does
        not have the appropriate status, the response will have HTTP status code 422 and an error message.

        A reason for the void operation is required to be included in the request body. If one is not provided, the
        response will have HTTP status code 422 and an error message.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.void_proforma_invoice(
                proforma_invoice_uid, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ProformaInvoicesWithRawResponse:
        return self._with_raw_response


class AsyncProformaInvoices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProformaInvoicesWithRawResponse(client, server, auth)

    async def create_consolidated_proforma_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Creates a consolidated proforma invoice asynchronously. To find and view the new consolidated proforma
        invoice, you can poll the subscription group listing for proforma invoices; only one consolidated proforma
        invoice can be created per group at a time.

        If the information becomes outdated, simply void the old consolidated proforma invoice and generate a new one.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be prepaid, and must be in a live state.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_consolidated_proforma_invoice(uid, request_options=request_options)
        )

    async def create_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProformaInvoice:
        """Creates a proforma invoice and returns it as a response. If the information becomes outdated, simply void the
        old proforma invoice and generate a new one.

        If you would like to preview the next billing amounts without generating a full proforma invoice, use the
        renewal preview endpoint.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be in a group, must not be prepaid, and must be in a live state.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_proforma_invoice(subscription_id, request_options=request_options)
        )

    async def create_signup_proforma_invoice(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProformaInvoice:
        """Creates a proforma invoice to preview costs before a subscription's signup. This endpoint is only available
        for Relationship Invoicing sites and cannot be used to create consolidated proforma invoices or preview prepaid
        subscriptions. Like other proforma invoices, it can be emailed to the customer, voided, and publicly viewed on
        the chargifypay domain.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements. We recommend associating
        the proforma invoice with a customer_id to easily find their proforma invoices, since the subscription_id will
        always be blank.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Unprocessable Entity (WebDAV) ``error`` is ``ProformaBadRequestErrorResponse1 |
                ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_signup_proforma_invoice(body=body, request_options=request_options)
        )

    async def deliver_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: DeliverProformaInvoiceRequest | DeliverProformaInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProformaInvoice:
        """Delivers a proforma invoice programmatically via email. Supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        If ``recipient_emails`` is omitted, the system will fall back to the primary recipient derived from the invoice
        or subscription. At least one recipient must be present, either via the request body or via this default
        behavior, so an empty body may still succeed when defaults are available.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.deliver_proforma_invoice(
                proforma_invoice_uid, body=body, request_options=request_options
            ),
        )

    async def list_proforma_invoices(
        self,
        subscription_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: ProformaInvoiceStatusOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProformaInvoicesResponse:
        """Lists proforma invoices for a subscription. By default, results only include totals, not detailed breakdowns
        for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or ``custom_fields``. To include
        breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            subscription_id: The Chargify id of the subscription.
            start_date: The beginning date range for the invoice's Due Date, in the YYYY-MM-DD format.
            end_date: The ending date range for the invoice's Due Date, in the YYYY-MM-DD format.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned invoices.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_proforma_invoices(
                subscription_id,
                start_date=start_date,
                end_date=end_date,
                status=status,
                page=page,
                per_page=per_page,
                direction=direction,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                credits_=credits_,
                payments=payments,
                custom_fields=custom_fields,
                request_options=request_options,
            ),
        )

    async def list_subscription_group_proforma_invoices(
        self,
        uid: str,
        *,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProformaInvoicesResponse:
        """Lists proforma invoices with a ``consolidation_level`` of parent for the subscription group.

        By default, proforma invoices returned on the index will only include totals, not detailed breakdowns for
        ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``. To include breakdowns,
        pass the specific field as a key in the query with a value set to true.

        Args:
            uid: The uid of the subscription group
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_subscription_group_proforma_invoices(
                uid,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                credits_=credits_,
                payments=payments,
                custom_fields=custom_fields,
                request_options=request_options,
            ),
        )

    async def preview_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProformaInvoice:
        """Previews the data that will be included on a given subscription's proforma invoice if one were to be
        generated. It will have similar line items and totals as a renewal preview, but the response will be presented
        in the format of a proforma invoice. Consequently it will include additional information such as the name and
        addresses that will appear on the proforma invoice.

        The preview endpoint is subject to all the same conditions as the proforma invoice endpoint. For example,
        previews are only available on the Relationship Invoicing architecture, and previews cannot be made for
        end-of-life subscriptions.

        If all the data returned in the preview is as expected, you may then create a static proforma invoice and send
        it to your customer. The data within a preview will not be saved and will not be accessible after the call is
        made.

        Alternatively, if you have some proforma invoices already, you may make a preview call to determine whether any
        billing information for the subscription's upcoming renewal has changed.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.preview_proforma_invoice(subscription_id, request_options=request_options)
        )

    async def preview_signup_proforma_invoice(
        self,
        *,
        include: CreateSignupProformaPreviewIncludeOrStr | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignupProformaPreviewResponse:
        """Creates a signup preview in the format of a proforma invoice to preview costs before a subscription's signup.
        This endpoint is only available for Relationship Invoicing sites and cannot be used to create consolidated
        proforma invoice previews or preview prepaid subscriptions. You have the option of previewing the first
        renewal's costs as well. The proforma invoice preview will not be persisted.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements.

        Args:
            include: Choose to include a proforma invoice preview for the first renewal. Use in query
                ``include=next_proforma_invoice``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Unprocessable Entity (WebDAV) ``error`` is ``ProformaBadRequestErrorResponse1 |
                ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.preview_signup_proforma_invoice(
                include=include, body=body, request_options=request_options
            ),
        )

    async def read_proforma_invoice(
        self, proforma_invoice_uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProformaInvoice:
        """Returns the details of an existing proforma invoice.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_proforma_invoice(proforma_invoice_uid, request_options=request_options)
        )

    async def void_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProformaInvoice:
        """Voids a proforma invoice that has the status "draft".

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Only proforma invoices that have the appropriate status may be reopened. If the invoice identified by {uid} does
        not have the appropriate status, the response will have HTTP status code 422 and an error message.

        A reason for the void operation is required to be included in the request body. If one is not provided, the
        response will have HTTP status code 422 and an error message.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.void_proforma_invoice(
                proforma_invoice_uid, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncProformaInvoicesWithRawResponse:
        return self._with_raw_response


class ProformaInvoicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_consolidated_proforma_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CreateConsolidatedProformaInvoiceErrorBody]:
        """Creates a consolidated proforma invoice asynchronously. To find and view the new consolidated proforma
        invoice, you can poll the subscription group listing for proforma invoices; only one consolidated proforma
        invoice can be created per group at a time.

        If the information becomes outdated, simply void the old consolidated proforma invoice and generate a new one.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be prepaid, and must be in a live state.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/proforma_invoices.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=create_consolidated_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    def create_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProformaInvoice, CreateProformaInvoiceErrorBody]:
        """Creates a proforma invoice and returns it as a response. If the information becomes outdated, simply void the
        old proforma invoice and generate a new one.

        If you would like to preview the next billing amounts without generating a full proforma invoice, use the
        renewal preview endpoint.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be in a group, must not be prepaid, and must be in a live state.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/proforma_invoices.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProformaInvoice],
            error_mapper=create_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    def create_signup_proforma_invoice(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProformaInvoice, CreateSignupProformaInvoiceErrorBody]:
        """Creates a proforma invoice to preview costs before a subscription's signup. This endpoint is only available
        for Relationship Invoicing sites and cannot be used to create consolidated proforma invoices or preview prepaid
        subscriptions. Like other proforma invoices, it can be emailed to the customer, voided, and publicly viewed on
        the chargifypay domain.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements. We recommend associating
        the proforma invoice with a customer_id to easily find their proforma invoices, since the subscription_id will
        always be blank.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/proforma_invoices.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProformaInvoice],
            error_mapper=create_signup_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    def deliver_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: DeliverProformaInvoiceRequest | DeliverProformaInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProformaInvoice, DeliverProformaInvoiceErrorBody]:
        """Delivers a proforma invoice programmatically via email. Supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        If ``recipient_emails`` is omitted, the system will fall back to the primary recipient derived from the invoice
        or subscription. At least one recipient must be present, either via the request body or via this default
        behavior, so an empty body may still succeed when defaults are available.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/proforma_invoices/{proforma_invoice_uid}/deliveries.json"),
            path_params=[param[str]("proforma_invoice_uid", proforma_invoice_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeliverProformaInvoiceRequest | DeliverProformaInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProformaInvoice],
            error_mapper=deliver_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    def list_proforma_invoices(
        self,
        subscription_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: ProformaInvoiceStatusOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProformaInvoicesResponse, RawError]:
        """Lists proforma invoices for a subscription. By default, results only include totals, not detailed breakdowns
        for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or ``custom_fields``. To include
        breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            subscription_id: The Chargify id of the subscription.
            start_date: The beginning date range for the invoice's Due Date, in the YYYY-MM-DD format.
            end_date: The ending date range for the invoice's Due Date, in the YYYY-MM-DD format.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned invoices.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/proforma_invoices.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[ProformaInvoiceStatusOrStr | None]("status", status),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("credits", credits_),
                param[bool | None]("payments", payments),
                param[bool | None]("custom_fields", custom_fields),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListProformaInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_subscription_group_proforma_invoices(
        self,
        uid: str,
        *,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProformaInvoicesResponse, ListSubscriptionGroupProformaInvoicesErrorBody]:
        """Lists proforma invoices with a ``consolidation_level`` of parent for the subscription group.

        By default, proforma invoices returned on the index will only include totals, not detailed breakdowns for
        ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``. To include breakdowns,
        pass the specific field as a key in the query with a value set to true.

        Args:
            uid: The uid of the subscription group
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/{uid}/proforma_invoices.json"),
            path_params=[param[str]("uid", uid)],
            query_params=[
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("credits", credits_),
                param[bool | None]("payments", payments),
                param[bool | None]("custom_fields", custom_fields),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListProformaInvoicesResponse],
            error_mapper=list_subscription_group_proforma_invoices_error_mapper,
            request_options=request_options,
        )

    def preview_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProformaInvoice, PreviewProformaInvoiceErrorBody]:
        """Previews the data that will be included on a given subscription's proforma invoice if one were to be
        generated. It will have similar line items and totals as a renewal preview, but the response will be presented
        in the format of a proforma invoice. Consequently it will include additional information such as the name and
        addresses that will appear on the proforma invoice.

        The preview endpoint is subject to all the same conditions as the proforma invoice endpoint. For example,
        previews are only available on the Relationship Invoicing architecture, and previews cannot be made for
        end-of-life subscriptions.

        If all the data returned in the preview is as expected, you may then create a static proforma invoice and send
        it to your customer. The data within a preview will not be saved and will not be accessible after the call is
        made.

        Alternatively, if you have some proforma invoices already, you may make a preview call to determine whether any
        billing information for the subscription's upcoming renewal has changed.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/proforma_invoices/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProformaInvoice],
            error_mapper=preview_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    def preview_signup_proforma_invoice(
        self,
        *,
        include: CreateSignupProformaPreviewIncludeOrStr | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignupProformaPreviewResponse, PreviewSignupProformaInvoiceErrorBody]:
        """Creates a signup preview in the format of a proforma invoice to preview costs before a subscription's signup.
        This endpoint is only available for Relationship Invoicing sites and cannot be used to create consolidated
        proforma invoice previews or preview prepaid subscriptions. You have the option of previewing the first
        renewal's costs as well. The proforma invoice preview will not be persisted.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements.

        Args:
            include: Choose to include a proforma invoice preview for the first renewal. Use in query
                ``include=next_proforma_invoice``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/proforma_invoices/preview.json"),
            query_params=[param[CreateSignupProformaPreviewIncludeOrStr | None]("include", include)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SignupProformaPreviewResponse],
            error_mapper=preview_signup_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    def read_proforma_invoice(
        self, proforma_invoice_uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProformaInvoice, ReadProformaInvoiceErrorBody]:
        """Returns the details of an existing proforma invoice.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/proforma_invoices/{proforma_invoice_uid}.json"),
            path_params=[param[str]("proforma_invoice_uid", proforma_invoice_uid)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProformaInvoice],
            error_mapper=read_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    def void_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProformaInvoice, VoidProformaInvoiceErrorBody]:
        """Voids a proforma invoice that has the status "draft".

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Only proforma invoices that have the appropriate status may be reopened. If the invoice identified by {uid} does
        not have the appropriate status, the response will have HTTP status code 422 and an error message.

        A reason for the void operation is required to be included in the request body. If one is not provided, the
        response will have HTTP status code 422 and an error message.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/proforma_invoices/{proforma_invoice_uid}/void.json"),
            path_params=[param[str]("proforma_invoice_uid", proforma_invoice_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidInvoiceRequest | VoidInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProformaInvoice],
            error_mapper=void_proforma_invoice_error_mapper,
            request_options=request_options,
        )


class AsyncProformaInvoicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_consolidated_proforma_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, CreateConsolidatedProformaInvoiceErrorBody]:
        """Creates a consolidated proforma invoice asynchronously. To find and view the new consolidated proforma
        invoice, you can poll the subscription group listing for proforma invoices; only one consolidated proforma
        invoice can be created per group at a time.

        If the information becomes outdated, simply void the old consolidated proforma invoice and generate a new one.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be prepaid, and must be in a live state.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/proforma_invoices.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=create_consolidated_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    async def create_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProformaInvoice, CreateProformaInvoiceErrorBody]:
        """Creates a proforma invoice and returns it as a response. If the information becomes outdated, simply void the
        old proforma invoice and generate a new one.

        If you would like to preview the next billing amounts without generating a full proforma invoice, use the
        renewal preview endpoint.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites. To create a proforma invoice, the
        subscription must not be in a group, must not be prepaid, and must be in a live state.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/proforma_invoices.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProformaInvoice],
            error_mapper=create_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    async def create_signup_proforma_invoice(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProformaInvoice, CreateSignupProformaInvoiceErrorBody]:
        """Creates a proforma invoice to preview costs before a subscription's signup. This endpoint is only available
        for Relationship Invoicing sites and cannot be used to create consolidated proforma invoices or preview prepaid
        subscriptions. Like other proforma invoices, it can be emailed to the customer, voided, and publicly viewed on
        the chargifypay domain.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements. We recommend associating
        the proforma invoice with a customer_id to easily find their proforma invoices, since the subscription_id will
        always be blank.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/proforma_invoices.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProformaInvoice],
            error_mapper=create_signup_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    async def deliver_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: DeliverProformaInvoiceRequest | DeliverProformaInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProformaInvoice, DeliverProformaInvoiceErrorBody]:
        """Delivers a proforma invoice programmatically via email. Supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        If ``recipient_emails`` is omitted, the system will fall back to the primary recipient derived from the invoice
        or subscription. At least one recipient must be present, either via the request body or via this default
        behavior, so an empty body may still succeed when defaults are available.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/proforma_invoices/{proforma_invoice_uid}/deliveries.json"),
            path_params=[param[str]("proforma_invoice_uid", proforma_invoice_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeliverProformaInvoiceRequest | DeliverProformaInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProformaInvoice],
            error_mapper=deliver_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    async def list_proforma_invoices(
        self,
        subscription_id: int,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: ProformaInvoiceStatusOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProformaInvoicesResponse, RawError]:
        """Lists proforma invoices for a subscription. By default, results only include totals, not detailed breakdowns
        for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or ``custom_fields``. To include
        breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            subscription_id: The Chargify id of the subscription.
            start_date: The beginning date range for the invoice's Due Date, in the YYYY-MM-DD format.
            end_date: The ending date range for the invoice's Due Date, in the YYYY-MM-DD format.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned invoices.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/proforma_invoices.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[ProformaInvoiceStatusOrStr | None]("status", status),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("credits", credits_),
                param[bool | None]("payments", payments),
                param[bool | None]("custom_fields", custom_fields),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListProformaInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_subscription_group_proforma_invoices(
        self,
        uid: str,
        *,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProformaInvoicesResponse, ListSubscriptionGroupProformaInvoicesErrorBody]:
        """Lists proforma invoices with a ``consolidation_level`` of parent for the subscription group.

        By default, proforma invoices returned on the index will only include totals, not detailed breakdowns for
        ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``. To include breakdowns,
        pass the specific field as a key in the query with a value set to true.

        Args:
            uid: The uid of the subscription group
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            credits_: Include credits data.
            payments: Include payments data.
            custom_fields: Include custom fields data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/{uid}/proforma_invoices.json"),
            path_params=[param[str]("uid", uid)],
            query_params=[
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("credits", credits_),
                param[bool | None]("payments", payments),
                param[bool | None]("custom_fields", custom_fields),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListProformaInvoicesResponse],
            error_mapper=list_subscription_group_proforma_invoices_error_mapper,
            request_options=request_options,
        )

    async def preview_proforma_invoice(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProformaInvoice, PreviewProformaInvoiceErrorBody]:
        """Previews the data that will be included on a given subscription's proforma invoice if one were to be
        generated. It will have similar line items and totals as a renewal preview, but the response will be presented
        in the format of a proforma invoice. Consequently it will include additional information such as the name and
        addresses that will appear on the proforma invoice.

        The preview endpoint is subject to all the same conditions as the proforma invoice endpoint. For example,
        previews are only available on the Relationship Invoicing architecture, and previews cannot be made for
        end-of-life subscriptions.

        If all the data returned in the preview is as expected, you may then create a static proforma invoice and send
        it to your customer. The data within a preview will not be saved and will not be accessible after the call is
        made.

        Alternatively, if you have some proforma invoices already, you may make a preview call to determine whether any
        billing information for the subscription's upcoming renewal has changed.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/proforma_invoices/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProformaInvoice],
            error_mapper=preview_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    async def preview_signup_proforma_invoice(
        self,
        *,
        include: CreateSignupProformaPreviewIncludeOrStr | None = None,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignupProformaPreviewResponse, PreviewSignupProformaInvoiceErrorBody]:
        """Creates a signup preview in the format of a proforma invoice to preview costs before a subscription's signup.
        This endpoint is only available for Relationship Invoicing sites and cannot be used to create consolidated
        proforma invoice previews or preview prepaid subscriptions. You have the option of previewing the first
        renewal's costs as well. The proforma invoice preview will not be persisted.

        Pass a payload that resembles a subscription create or signup preview request. For example, you can specify
        components, coupons/a referral, offers, custom pricing, and an existing customer or payment profile to populate
        a shipping or billing address.

        A product and customer first name, last name, and email are the minimum requirements.

        Args:
            include: Choose to include a proforma invoice preview for the first renewal. Use in query
                ``include=next_proforma_invoice``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/proforma_invoices/preview.json"),
            query_params=[param[CreateSignupProformaPreviewIncludeOrStr | None]("include", include)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SignupProformaPreviewResponse],
            error_mapper=preview_signup_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    async def read_proforma_invoice(
        self, proforma_invoice_uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProformaInvoice, ReadProformaInvoiceErrorBody]:
        """Returns the details of an existing proforma invoice.

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/proforma_invoices/{proforma_invoice_uid}.json"),
            path_params=[param[str]("proforma_invoice_uid", proforma_invoice_uid)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProformaInvoice],
            error_mapper=read_proforma_invoice_error_mapper,
            request_options=request_options,
        )

    async def void_proforma_invoice(
        self,
        proforma_invoice_uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProformaInvoice, VoidProformaInvoiceErrorBody]:
        """Voids a proforma invoice that has the status "draft".

        ## Restrictions

        Proforma invoices are only available on Relationship Invoicing sites.

        Only proforma invoices that have the appropriate status may be reopened. If the invoice identified by {uid} does
        not have the appropriate status, the response will have HTTP status code 422 and an error message.

        A reason for the void operation is required to be included in the request body. If one is not provided, the
        response will have HTTP status code 422 and an error message.

        Args:
            proforma_invoice_uid: The uid of the proforma invoice
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/proforma_invoices/{proforma_invoice_uid}/void.json"),
            path_params=[param[str]("proforma_invoice_uid", proforma_invoice_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidInvoiceRequest | VoidInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProformaInvoice],
            error_mapper=void_proforma_invoice_error_mapper,
            request_options=request_options,
        )
