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
from ..errors.create_invoice_error import CreateInvoiceErrorBody, create_invoice_error_mapper
from ..errors.delete_invoice_error import DeleteInvoiceErrorBody, delete_invoice_error_mapper
from ..errors.issue_invoice_error import IssueInvoiceErrorBody, issue_invoice_error_mapper
from ..errors.preview_customer_information_changes_error import (
    PreviewCustomerInformationChangesErrorBody,
    preview_customer_information_changes_error_mapper,
)
from ..errors.record_payment_for_invoice_error import (
    RecordPaymentForInvoiceErrorBody,
    record_payment_for_invoice_error_mapper,
)
from ..errors.record_payment_for_multiple_invoices_error import (
    RecordPaymentForMultipleInvoicesErrorBody,
    record_payment_for_multiple_invoices_error_mapper,
)
from ..errors.record_payment_for_subscription_error import (
    RecordPaymentForSubscriptionErrorBody,
    record_payment_for_subscription_error_mapper,
)
from ..errors.refund_invoice_error import RefundInvoiceErrorBody, refund_invoice_error_mapper
from ..errors.reopen_invoice_error import ReopenInvoiceErrorBody, reopen_invoice_error_mapper
from ..errors.send_invoice_error import SendInvoiceErrorBody, send_invoice_error_mapper
from ..errors.update_customer_information_error import (
    UpdateCustomerInformationErrorBody,
    update_customer_information_error_mapper,
)
from ..errors.update_invoice_error import UpdateInvoiceErrorBody, update_invoice_error_mapper
from ..errors.void_invoice_error import VoidInvoiceErrorBody, void_invoice_error_mapper
from ..models.consolidated_invoice import ConsolidatedInvoice
from ..models.create_invoice_payment_request import CreateInvoicePaymentRequest, CreateInvoicePaymentRequestDict
from ..models.create_invoice_request import CreateInvoiceRequest, CreateInvoiceRequestDict
from ..models.create_multi_invoice_payment_request import (
    CreateMultiInvoicePaymentRequest,
    CreateMultiInvoicePaymentRequestDict,
)
from ..models.credit_note import CreditNote
from ..models.customer_changes_preview_response import CustomerChangesPreviewResponse
from ..models.enums.credit_note_date_field import CreditNoteDateField, CreditNoteDateFieldOrStr
from ..models.enums.direction import Direction, DirectionOrStr
from ..models.enums.invoice_date_field import InvoiceDateField, InvoiceDateFieldOrStr
from ..models.enums.invoice_event_type import InvoiceEventTypeOrStr
from ..models.enums.invoice_sort_field import InvoiceSortField, InvoiceSortFieldOrStr
from ..models.enums.invoice_status import InvoiceStatusOrStr
from ..models.invoice import Invoice
from ..models.invoice_response import InvoiceResponse
from ..models.issue_invoice_request import IssueInvoiceRequest, IssueInvoiceRequestDict
from ..models.list_credit_notes_response import ListCreditNotesResponse
from ..models.list_invoice_events_response import ListInvoiceEventsResponse
from ..models.list_invoices_response import ListInvoicesResponse
from ..models.multi_invoice_payment_response import MultiInvoicePaymentResponse
from ..models.record_payment_request import RecordPaymentRequest, RecordPaymentRequestDict
from ..models.record_payment_response import RecordPaymentResponse
from ..models.refund_invoice_request import RefundInvoiceRequest, RefundInvoiceRequestDict
from ..models.send_invoice_request import SendInvoiceRequest, SendInvoiceRequestDict
from ..models.update_invoice_request import UpdateInvoiceRequest, UpdateInvoiceRequestDict
from ..models.void_invoice_request import VoidInvoiceRequest, VoidInvoiceRequestDict
from ..server.server import Server


class Invoices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InvoicesWithRawResponse(client, server, auth)

    def create_invoice(
        self,
        subscription_id: int,
        *,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvoiceResponse:
        """Creates an ad hoc invoice.

        ### Basic Behavior

        You can create a basic invoice by sending an array of line items to this endpoint. Each line item, at a minimum,
        must include a title, a quantity and a unit price. Example:

        ```json
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
        ```

        ### Catalog items Instead of creating custom products like in above example, You can pass existing items like
        products, components.

        ```json
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
        ```


        The price for each line item will be calculated as well as a total due amount for the invoice. Multiple line
        items can be sent.

        ### Line item types When defining a line item, You can choose one of 3 types for a line item: #### Custom item
        As shown in the basic behavior example, You can pass ``title`` and ``unit_price`` for custom item. #### Product
        id Product handle (with handle: prefix) or id from the scope of current subscription's site can be provided with
        ``product_id``. By default ``unit_price`` is taken from product's default price point, but can be overwritten by
        passing ``unit_price`` or ``product_price_point_id``. If ``product_id`` is used, following fields cannot be
        used: ``title``, ``component_id``. #### Component id Component handle (with handle: prefix) or id from the scope
        of current subscription's site can be provided with ``component_id``. If ``component_id`` is used, following
        fields cannot be used: ``title``, ``product_id``. By default ``unit_price`` is taken from product's default
        price point, but can be overwritten by passing ``unit_price`` or ``price_point_id``. At this moment price points
        are supported only for quantity based, on/off and metered components. For prepaid and event based billing
        components ``unit_price`` is required.

        ### Coupons When creating ad hoc invoice, new discounts can be applied in following way:

        ```json
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
        ```
        If You want to use existing coupon for discount creation, only ``code`` and optional ``product_family_id`` is
        needed

        ```json
        ...
         "coupons": [
              {
                "code": "FREESETUP",
                "product_family_id": 1
              }
          ]
        ...
        ```

        #### Using Coupon Subcodes You can also use coupon subcodes to apply existing coupons with specific subcodes:

        ```json
        ...
         "coupons": [
              {
                "subcode": "SUB1",
                "product_family_id": 1
              }
          ]
        ...
        ```
        **Important:** You cannot specify both ``code`` and ``subcode`` for the same coupon. Use either:
        - ``code`` to apply a main coupon
        - ``subcode`` to apply a specific coupon subcode

        The API response will include both the main coupon code and the subcode used:

        ```json
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
        ```

        ### Coupon options #### Code Coupon ``code`` will be displayed on invoice discount section. Coupon code can only
        contain uppercase letters, numbers, and allowed special characters. Lowercase letters will be converted to
        uppercase. It can be used to select an existing coupon from the catalog, or as an ad hoc coupon when passed with
        ``percentage`` or ``amount``. #### Subcode Coupon ``subcode`` allows you to apply existing coupons using their
        subcodes. When a subcode is used, the API response will include both the main coupon code and the specific
        subcode that was applied. Subcodes are case-insensitive and will be converted to uppercase automatically. ####
        Percentage Coupon ``percentage`` can take values from 0 to 100 and up to 4 decimal places. It cannot be used
        with ``amount``. Only for ad hoc coupons, will be ignored if ``code`` is used to select an existing coupon from
        the catalog. #### Amount Coupon ``amount`` takes number value. It cannot be used with ``percentage``. Used only
        when not matching existing coupon by ``code``. #### Description Optional ``description`` will be displayed with
        coupon ``code``. Used only when not matching existing coupon by ``code``. #### Product Family id Optional
        ``product_family_id`` handle (with handle: prefix) or id is used to match existing coupon within site, when
        codes are not unique. #### Compounding Strategy Optional ``compounding_strategy`` for percentage coupons, can
        take values ``compound`` or ``full-price``.

        For amount coupons, discounts will be always calculated against the original item price, before other discounts
        are applied.

        ``compound`` strategy: Percentage-based discounts will be calculated against the remaining price, after prior
        discounts have been calculated. It is set by default.

        ``full-price`` strategy: Percentage-based discounts will always be calculated against the original item price,
        before other discounts are applied.

        ### Line Item Options

        #### Period Date Range

        A custom period date range can be defined for each line item with the ``period_range_start`` and
        ``period_range_end`` parameters. Dates must be sent in the ``YYYY-MM-DD`` format. ``period_range_end`` must be
        greater or equal ``period_range_start``.

        #### Taxes

        The ``taxable`` parameter can be sent as ``true`` if taxes should be calculated for a specific line item. For
        this to work, the site should be configured to use and calculate taxes. Further, if the site uses Avalara for
        tax calculations, a ``tax_code`` parameter should also be sent. For existing catalog items: products/components
        taxes cannot be overwritten.

        #### Price Point Price point handle (with handle: prefix) or id from the scope of current subscription's site
        can be provided with ``price_point_id`` for components with ``component_id`` or ``product_price_point_id`` for
        products with ``product_id`` parameter. If price point is passed ``unit_price`` cannot be used. It can be used
        only with catalog items products and components.

        #### Description Optional ``description`` parameter, it will overwrite default generated description for line
        item.

        ### Invoice Options

        #### Issue Date

        By default, invoices will be created with a issue date set to today in your site's time zone. The ``issue_date``
        parameter can be sent to alter the default. Only today or dates in the past are accepted. This date is
        interpreted and validated in your site's time zone. The format for ``issue_date`` is ``YYYY-MM-DD``.

        #### Net Terms

        By default, invoices will be created with a due date matching the date of invoice creation. If a different due
        date is desired, the ``net_terms`` parameter can be sent indicating the number of days in advance the due date
        should be.

        #### Addresses

        The seller, shipping and billing addresses can be sent to override the site's defaults. Each address requires to
        send a ``first_name`` at a minimum in order to work. See below for the details on which parameters can be sent
        for each address object.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter to override the site's default. Likewise, custom payment
        instructions can be sent with the ``payment_instructions`` parameter.

        #### Status

        By default, invoices will be created with open status. Possible alternative is ``draft``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_invoice(subscription_id, body=body, request_options=request_options)
        )

    def delete_invoice(
        self, subscription_id: int, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be deleted.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be deleted through this endpoint and
        the request returns a ``422`` error. Issued invoices should be voided instead. If the invoice does not belong to
        the provided subscription, a ``404`` error is returned.

        A successful deletion returns a ``204 No Content`` response and the invoice is permanently removed.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.delete_invoice(subscription_id, uid, request_options=request_options))

    def issue_invoice(
        self,
        uid: str,
        *,
        body: IssueInvoiceRequest | IssueInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Issues an invoice that is in "pending" or "draft" status. For example, you can issue an invoice that was
        created when allocating new quantity on a component and using "accrue charges" option.

        You cannot issue a pending child invoice that was created for a member subscription in a group.

        For Remittance subscriptions, the invoice will go into "open" status and payment won't be attempted. The value
        for ``on_failed_payment`` would be rejected if sent. Any prepayments or service credits that exist on the
        subscription will be automatically applied. Additionally, if the setting is enabled, an email will be sent for
        the issued invoice.

        For Automatic subscriptions, prepayments and service credits will apply to the invoice before payment is
        attempted. On successful payment, the invoice will go into "paid" status and email will be sent to the customer
        (if setting applies). When payment fails, the next event depends on the ``on_failed_payment`` value:
        - ``leave_open_invoice`` - prepayments and credits applied to invoice; invoice status set to "open"; email sent
            to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history. This is the default option.
        - ``rollback_to_pending`` - prepayments and credits not applied; invoice remains in "pending" status; no email
            sent to the customer; payment failure recorded in the invoice history.
        - ``initiate_dunning`` - prepayments and credits applied to the invoice; invoice status set to "open"; email
            sent to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history; subscription will most likely go into "past_due" or "canceled" state (depending upon net terms and
            dunning settings).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.issue_invoice(uid, body=body, request_options=request_options))

    def list_consolidated_invoice_segments(
        self,
        invoice_uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConsolidatedInvoice:
        """Lists segments for a consolidated invoice. Invoice segments returned on the index will only include totals,
        not detailed breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or
        ``custom_fields``.

        Args:
            invoice_uid: The unique identifier of the consolidated invoice
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Sort direction of the returned segments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_consolidated_invoice_segments(
                invoice_uid, page=page, per_page=per_page, direction=direction, request_options=request_options
            ),
        )

    def list_credit_notes(
        self,
        *,
        subscription_id: int | None = None,
        date_field: CreditNoteDateFieldOrStr | None = CreditNoteDateField.ISSUE_DATE,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        refunds: bool | None = False,
        applications: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCreditNotesResponse:
        """Lists credit notes for a site. Credit Notes are like inverse invoices. They reduce the amount a customer
        owes.

        By default, the credit notes returned by this endpoint will exclude the arrays of ``line_items``, ``discounts``,
        ``taxes``, ``applications``, or ``refunds``. To include these arrays, pass the specific field as a key in the
        query with a value set to ``true``.

        Args:
            subscription_id: The subscription's Advanced Billing id
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``. If a date range is provided without an explicit ``date_field``, it defaults
                to ``issue_date``. If only ``start_datetime``/``end_datetime`` are provided without an explicit
                ``date_field``, it defaults to ``created_at`` instead. An unrecognized ``date_field`` is ignored rather
                than raising an error.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or after exact time provided in query. If provided, this
                parameter will be used instead of start_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or before exact time provided in query. If provided, this
                parameter will be used instead of end_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned credit notes, sorted by sequence_number.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            refunds: Include refunds data.
            applications: Include applications data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_credit_notes(
                subscription_id=subscription_id,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                page=page,
                per_page=per_page,
                direction=direction,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                refunds=refunds,
                applications=applications,
                request_options=request_options,
            ),
        )

    def list_invoice_events(
        self,
        *,
        since_date: str | None = None,
        since_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        invoice_uid: str | None = None,
        with_change_invoice_status: str | None = None,
        event_types: list[InvoiceEventTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInvoiceEventsResponse:
        """Lists invoice events for a site. Each event contains event "data" (such as an applied payment) as well as a
        snapshot of the ``invoice`` at the time of event completion.

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

        If both a ``since_date`` and ``since_id`` are provided in request parameters, the ``since_date`` will be used.

        Note - invoice events that occurred prior to 09/05/2018 __will not__ contain an ``invoice`` snapshot.

        Args:
            since_date: The timestamp in a format ``YYYY-MM-DD T HH:MM:SS Z``, or ``YYYY-MM-DD``(in this case, it
                returns data from the beginning of the day). of the event from which you want to start the search. All
                the events before the ``since_date`` timestamp are not returned in the response.
            since_id: The ID of the event from which you want to start the search(ID is not included. e.g. if ID is set
                to 2, then all events with ID 3 and more will be shown) This parameter is not used if since_date is
                defined.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            invoice_uid: Providing an invoice_uid allows for scoping of the invoice events to a single invoice or credit
                note.
            with_change_invoice_status: Use this parameter if you want to fetch also invoice events with
                change_invoice_status type.
            event_types: Filter results by event_type. Supply a comma separated list of event types (listed above). Use
                in query: ``event_types=void_invoice,void_remainder``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_invoice_events(
                since_date=since_date,
                since_id=since_id,
                page=page,
                per_page=per_page,
                invoice_uid=invoice_uid,
                with_change_invoice_status=with_change_invoice_status,
                event_types=event_types,
                request_options=request_options,
            ),
        )

    def list_invoices(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: InvoiceStatusOrStr | None = None,
        subscription_id: int | None = None,
        subscription_group_uid: str | None = None,
        consolidation_level: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        refunds: bool | None = False,
        date_field: InvoiceDateFieldOrStr | None = InvoiceDateField.DUE_DATE,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        customer_ids: list[int] | None = None,
        number: list[str] | None = None,
        product_ids: list[int] | None = None,
        sort: InvoiceSortFieldOrStr | None = InvoiceSortField.NUMBER,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInvoicesResponse:
        """Lists invoices for a site. By default, invoices returned on the index will only include totals, not detailed
        breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``, or
        ``refunds``. To include breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            subscription_id: The subscription's ID.
            subscription_group_uid: The UID of the subscription group you want to fetch consolidated invoices for. This
                will return a paginated list of consolidated invoices for the specified group.
            consolidation_level: The consolidation level of the invoice. Allowed Values: none, parent, child or
                comma-separated lists of thereof, e.g. none,parent.
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
            refunds: Include refunds data.
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date. Allowed to be used only along with date_field set to created_at or updated_at.
            customer_ids: Allows fetching invoices with matching customer id based on provided values. Use in query
                ``customer_ids=1,2,3``.
            number: Allows fetching invoices with matching invoice number based on provided values. Use in query
                ``number=1234,1235``.
            product_ids: Allows fetching invoices with matching line items product ids based on provided values. Use in
                query ``product_ids=23,34``.
            sort: Allows specification of the order of the returned list. Use in query ``sort=total_amount``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_invoices(
                start_date=start_date,
                end_date=end_date,
                status=status,
                subscription_id=subscription_id,
                subscription_group_uid=subscription_group_uid,
                consolidation_level=consolidation_level,
                page=page,
                per_page=per_page,
                direction=direction,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                credits_=credits_,
                payments=payments,
                custom_fields=custom_fields,
                refunds=refunds,
                date_field=date_field,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                customer_ids=customer_ids,
                number=number,
                product_ids=product_ids,
                sort=sort,
                request_options=request_options,
            ),
        )

    def preview_customer_information_changes(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomerChangesPreviewResponse:
        """Previews the effect of customer information changes on an open invoice. Customer information may change after
        an invoice is issued, which may lead to a mismatch between customer information that is present on an open
        invoice and actual customer information. This endpoint allows you to preview these differences, if any.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.preview_customer_information_changes(uid, request_options=request_options)
        )

    def read_credit_note(self, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> CreditNote:
        """Returns the details for a credit note.

        Args:
            uid: The unique identifier of the credit note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_credit_note(uid, request_options=request_options))

    def read_invoice(self, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice:
        """Returns the details for an invoice.

        ## PDF Invoice retrieval

        Individual PDF Invoices can be retrieved by using the "Accept" header application/pdf or appending .pdf as the
        format portion of the URL: ```curl -u <api_key>:x -H Accept:application/pdf -H
        https://acme.chargify.com/invoices/inv_8gd8tdhtd3hgr.pdf > output_file.pdf URL:
        ``https://<subdomain>.chargify.com/invoices/<uid>.<format>`` Method: GET Required parameters: ``uid`` Response:
        A single Invoice.
        ```

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_invoice(uid, request_options=request_options))

    def record_payment_for_invoice(
        self,
        uid: str,
        *,
        body: CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Applies a payment of a given type against a specific invoice. If you would like to apply a payment across
        multiple invoices, you can use the `Record Payment for Multiple Invoices
        <$e/Invoices/recordPaymentForMultipleInvoices>`__ endpoint.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.record_payment_for_invoice(uid, body=body, request_options=request_options)
        )

    def record_payment_for_multiple_invoices(
        self,
        *,
        body: CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiInvoicePaymentResponse:
        """Records an external payment against multiple invoices.

        To apply a payment to multiple invoices, at minimum, specify the ``amount`` and ``applications`` (i.e.,
        ``invoice_uid`` and ``amount``) details.

        Note that the invoice payment amounts must be greater than 0. Total amount must be greater or equal to invoices
        payment amount sum.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.record_payment_for_multiple_invoices(body=body, request_options=request_options)
        )

    def record_payment_for_subscription(
        self,
        subscription_id: int,
        *,
        body: RecordPaymentRequest | RecordPaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecordPaymentResponse:
        """Records an external payment made against a subscription that will pay partially or in full one or more
        invoices.

        Payment will be applied starting with the oldest open invoice and then next oldest, and so on until the amount
        of the payment is fully consumed.

        Excess payment will result in the creation of a prepayment on the Invoice Account.

        Only ungrouped or primary subscriptions may be paid using the "bulk" payment request.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.record_payment_for_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def refund_invoice(
        self,
        uid: str,
        *,
        body: RefundInvoiceRequest | RefundInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Refunds an invoice, segment, or consolidated invoice.

        ## Partial Refund for Consolidated Invoice

        A refund less than the total of a consolidated invoice will be split across its segments.

        For a $50.00 refund on a $100.00 consolidated invoice with one $60.00 segment and one $40.00 segment, the
        refunded amount will be applied as 50% of each ($30.00 and $20.00, respectively).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.refund_invoice(uid, body=body, request_options=request_options))

    def reopen_invoice(self, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice:
        """Reopens any invoice with the "canceled" status. Invoices enter "canceled" status if they were open at the
        time the subscription was canceled (whether through dunning or an intentional cancellation).

        Invoices with "canceled" status are no longer considered to be due. Once reopened, they are considered due for
        payment. Payment may then be captured in one of the following ways:

        - Reactivating the subscription, which will capture all open invoices (See note below about automatic reopening
            of invoices.)
        - Recording a payment directly against the invoice

        A note about reactivations: any canceled invoices from the most recent active period are automatically opened as
        a part of the reactivation process. Reactivating via this endpoint prior to reactivation is only necessary when
        you wish to capture older invoices from previous periods during the reactivation.

        ### Reopening Consolidated Invoices

        When reopening a consolidated invoice, all of its canceled segments will also be reopened.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``Any | None | ErrorListResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.reopen_invoice(uid, request_options=request_options))

    def send_invoice(
        self,
        uid: str,
        *,
        body: SendInvoiceRequest | SendInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Sends an invoice to the customer via email. This endpoint supports the delivery of both ad-hoc and
        automatically generated invoices. Additionally, this endpoint supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        **File Attachments**: You can attach files to invoice emails using ``attachment_urls[]`` parameter by providing
        URLs to the files you want to attach. When using attachments, the request must use ``multipart/form-data``
        content type. Max 10 files, 10MB per file.

        If no recipient email addresses are specified in the request, then the subscription's default email
        configuration will be used. For example, if ``recipient_emails`` is left blank, then the invoice will be
        delivered to the subscription's customer email address.

        On success, a 204 no-content response will be returned. The response does not indicate that email(s) have been
        delivered, but instead indicates that emails have been successfully queued for delivery. If _any_ invalid or
        malformed email address is found in the request body, the entire request will be rejected and a 422 response
        will be returned.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.send_invoice(uid, body=body, request_options=request_options))

    def update_customer_information(self, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice:
        """Updates customer information on an open invoice and returns the updated invoice. If you would like to preview
        changes that will be applied, use the ``/invoices/{uid}/customer_information/preview.json`` endpoint first.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.update_customer_information(uid, request_options=request_options))

    def update_invoice(
        self,
        subscription_id: int,
        uid: str,
        *,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvoiceResponse:
        """Updates an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be updated.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be updated through this endpoint and
        the request returns a ``422`` error. If the invoice does not belong to the provided subscription, a ``404``
        error is returned.

        Only the attributes submitted in the request are changed — omitted attributes keep their current values.

        ### Line Items

        The ``line_items`` array describes changes to the invoice's line items. Line items not referenced in the array
        remain unchanged.

        #### Adding a line item

        A line item without a ``uid`` is added to the invoice. The same line item types and options as on invoice
        creation are supported (custom items, ``product_id``, ``component_id``, price points, period date ranges,
        taxes).

        #### Updating a line item

        A line item with the ``uid`` of an existing line item updates that line item with the submitted attributes.
        Amounts and taxes are recalculated.

        #### Removing a line item

        A line item with a ``uid`` and ``"_destroy": true`` is removed from the invoice. Other line items remain
        unchanged.

        Referencing a ``uid`` which does not exist on the invoice returns a ``422`` error.

        ### Coupons

        When the ``coupons`` key is present, the submitted coupons replace all discounts currently applied to the
        invoice. Send an empty array to remove all discounts. Coupon options are the same as on invoice creation.

        ### Invoice Options

        #### Issue Date and Net Terms

        The ``issue_date`` parameter can be sent to change the invoice's issue date. Only today or dates in the past are
        accepted. The date is interpreted and validated in your site's time zone, using the ``YYYY-MM-DD`` format. The
        ``net_terms`` parameter indicates the number of days after the issue date on which the invoice is due. The due
        date is recalculated whenever the issue date or net terms change.

        #### Addresses

        The seller, shipping and billing addresses can be sent to replace the addresses on the invoice. Each address
        requires to send a ``first_name`` at a minimum in order to work. Taxes are recalculated after an address change.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter. Likewise, custom payment instructions can be sent with
        the ``payment_instructions`` parameter.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | ErrorArrayMapResponse1
                | RawError``."""
        return unwrap(
            self._with_raw_response.update_invoice(subscription_id, uid, body=body, request_options=request_options)
        )

    def void_invoice(
        self,
        uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Voids any invoice with the "open" or "canceled" status. It will also allow voiding of an invoice with the
        "pending" status if it is not a consolidated invoice.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``Any | None | ErrorListResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.void_invoice(uid, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> InvoicesWithRawResponse:
        return self._with_raw_response


class AsyncInvoices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInvoicesWithRawResponse(client, server, auth)

    async def create_invoice(
        self,
        subscription_id: int,
        *,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvoiceResponse:
        """Creates an ad hoc invoice.

        ### Basic Behavior

        You can create a basic invoice by sending an array of line items to this endpoint. Each line item, at a minimum,
        must include a title, a quantity and a unit price. Example:

        ```json
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
        ```

        ### Catalog items Instead of creating custom products like in above example, You can pass existing items like
        products, components.

        ```json
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
        ```


        The price for each line item will be calculated as well as a total due amount for the invoice. Multiple line
        items can be sent.

        ### Line item types When defining a line item, You can choose one of 3 types for a line item: #### Custom item
        As shown in the basic behavior example, You can pass ``title`` and ``unit_price`` for custom item. #### Product
        id Product handle (with handle: prefix) or id from the scope of current subscription's site can be provided with
        ``product_id``. By default ``unit_price`` is taken from product's default price point, but can be overwritten by
        passing ``unit_price`` or ``product_price_point_id``. If ``product_id`` is used, following fields cannot be
        used: ``title``, ``component_id``. #### Component id Component handle (with handle: prefix) or id from the scope
        of current subscription's site can be provided with ``component_id``. If ``component_id`` is used, following
        fields cannot be used: ``title``, ``product_id``. By default ``unit_price`` is taken from product's default
        price point, but can be overwritten by passing ``unit_price`` or ``price_point_id``. At this moment price points
        are supported only for quantity based, on/off and metered components. For prepaid and event based billing
        components ``unit_price`` is required.

        ### Coupons When creating ad hoc invoice, new discounts can be applied in following way:

        ```json
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
        ```
        If You want to use existing coupon for discount creation, only ``code`` and optional ``product_family_id`` is
        needed

        ```json
        ...
         "coupons": [
              {
                "code": "FREESETUP",
                "product_family_id": 1
              }
          ]
        ...
        ```

        #### Using Coupon Subcodes You can also use coupon subcodes to apply existing coupons with specific subcodes:

        ```json
        ...
         "coupons": [
              {
                "subcode": "SUB1",
                "product_family_id": 1
              }
          ]
        ...
        ```
        **Important:** You cannot specify both ``code`` and ``subcode`` for the same coupon. Use either:
        - ``code`` to apply a main coupon
        - ``subcode`` to apply a specific coupon subcode

        The API response will include both the main coupon code and the subcode used:

        ```json
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
        ```

        ### Coupon options #### Code Coupon ``code`` will be displayed on invoice discount section. Coupon code can only
        contain uppercase letters, numbers, and allowed special characters. Lowercase letters will be converted to
        uppercase. It can be used to select an existing coupon from the catalog, or as an ad hoc coupon when passed with
        ``percentage`` or ``amount``. #### Subcode Coupon ``subcode`` allows you to apply existing coupons using their
        subcodes. When a subcode is used, the API response will include both the main coupon code and the specific
        subcode that was applied. Subcodes are case-insensitive and will be converted to uppercase automatically. ####
        Percentage Coupon ``percentage`` can take values from 0 to 100 and up to 4 decimal places. It cannot be used
        with ``amount``. Only for ad hoc coupons, will be ignored if ``code`` is used to select an existing coupon from
        the catalog. #### Amount Coupon ``amount`` takes number value. It cannot be used with ``percentage``. Used only
        when not matching existing coupon by ``code``. #### Description Optional ``description`` will be displayed with
        coupon ``code``. Used only when not matching existing coupon by ``code``. #### Product Family id Optional
        ``product_family_id`` handle (with handle: prefix) or id is used to match existing coupon within site, when
        codes are not unique. #### Compounding Strategy Optional ``compounding_strategy`` for percentage coupons, can
        take values ``compound`` or ``full-price``.

        For amount coupons, discounts will be always calculated against the original item price, before other discounts
        are applied.

        ``compound`` strategy: Percentage-based discounts will be calculated against the remaining price, after prior
        discounts have been calculated. It is set by default.

        ``full-price`` strategy: Percentage-based discounts will always be calculated against the original item price,
        before other discounts are applied.

        ### Line Item Options

        #### Period Date Range

        A custom period date range can be defined for each line item with the ``period_range_start`` and
        ``period_range_end`` parameters. Dates must be sent in the ``YYYY-MM-DD`` format. ``period_range_end`` must be
        greater or equal ``period_range_start``.

        #### Taxes

        The ``taxable`` parameter can be sent as ``true`` if taxes should be calculated for a specific line item. For
        this to work, the site should be configured to use and calculate taxes. Further, if the site uses Avalara for
        tax calculations, a ``tax_code`` parameter should also be sent. For existing catalog items: products/components
        taxes cannot be overwritten.

        #### Price Point Price point handle (with handle: prefix) or id from the scope of current subscription's site
        can be provided with ``price_point_id`` for components with ``component_id`` or ``product_price_point_id`` for
        products with ``product_id`` parameter. If price point is passed ``unit_price`` cannot be used. It can be used
        only with catalog items products and components.

        #### Description Optional ``description`` parameter, it will overwrite default generated description for line
        item.

        ### Invoice Options

        #### Issue Date

        By default, invoices will be created with a issue date set to today in your site's time zone. The ``issue_date``
        parameter can be sent to alter the default. Only today or dates in the past are accepted. This date is
        interpreted and validated in your site's time zone. The format for ``issue_date`` is ``YYYY-MM-DD``.

        #### Net Terms

        By default, invoices will be created with a due date matching the date of invoice creation. If a different due
        date is desired, the ``net_terms`` parameter can be sent indicating the number of days in advance the due date
        should be.

        #### Addresses

        The seller, shipping and billing addresses can be sent to override the site's defaults. Each address requires to
        send a ``first_name`` at a minimum in order to work. See below for the details on which parameters can be sent
        for each address object.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter to override the site's default. Likewise, custom payment
        instructions can be sent with the ``payment_instructions`` parameter.

        #### Status

        By default, invoices will be created with open status. Possible alternative is ``draft``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_invoice(subscription_id, body=body, request_options=request_options)
        )

    async def delete_invoice(
        self, subscription_id: int, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be deleted.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be deleted through this endpoint and
        the request returns a ``422`` error. Issued invoices should be voided instead. If the invoice does not belong to
        the provided subscription, a ``404`` error is returned.

        A successful deletion returns a ``204 No Content`` response and the invoice is permanently removed.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_invoice(subscription_id, uid, request_options=request_options)
        )

    async def issue_invoice(
        self,
        uid: str,
        *,
        body: IssueInvoiceRequest | IssueInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Issues an invoice that is in "pending" or "draft" status. For example, you can issue an invoice that was
        created when allocating new quantity on a component and using "accrue charges" option.

        You cannot issue a pending child invoice that was created for a member subscription in a group.

        For Remittance subscriptions, the invoice will go into "open" status and payment won't be attempted. The value
        for ``on_failed_payment`` would be rejected if sent. Any prepayments or service credits that exist on the
        subscription will be automatically applied. Additionally, if the setting is enabled, an email will be sent for
        the issued invoice.

        For Automatic subscriptions, prepayments and service credits will apply to the invoice before payment is
        attempted. On successful payment, the invoice will go into "paid" status and email will be sent to the customer
        (if setting applies). When payment fails, the next event depends on the ``on_failed_payment`` value:
        - ``leave_open_invoice`` - prepayments and credits applied to invoice; invoice status set to "open"; email sent
            to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history. This is the default option.
        - ``rollback_to_pending`` - prepayments and credits not applied; invoice remains in "pending" status; no email
            sent to the customer; payment failure recorded in the invoice history.
        - ``initiate_dunning`` - prepayments and credits applied to the invoice; invoice status set to "open"; email
            sent to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history; subscription will most likely go into "past_due" or "canceled" state (depending upon net terms and
            dunning settings).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.issue_invoice(uid, body=body, request_options=request_options))

    async def list_consolidated_invoice_segments(
        self,
        invoice_uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConsolidatedInvoice:
        """Lists segments for a consolidated invoice. Invoice segments returned on the index will only include totals,
        not detailed breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or
        ``custom_fields``.

        Args:
            invoice_uid: The unique identifier of the consolidated invoice
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Sort direction of the returned segments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_consolidated_invoice_segments(
                invoice_uid, page=page, per_page=per_page, direction=direction, request_options=request_options
            ),
        )

    async def list_credit_notes(
        self,
        *,
        subscription_id: int | None = None,
        date_field: CreditNoteDateFieldOrStr | None = CreditNoteDateField.ISSUE_DATE,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        refunds: bool | None = False,
        applications: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCreditNotesResponse:
        """Lists credit notes for a site. Credit Notes are like inverse invoices. They reduce the amount a customer
        owes.

        By default, the credit notes returned by this endpoint will exclude the arrays of ``line_items``, ``discounts``,
        ``taxes``, ``applications``, or ``refunds``. To include these arrays, pass the specific field as a key in the
        query with a value set to ``true``.

        Args:
            subscription_id: The subscription's Advanced Billing id
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``. If a date range is provided without an explicit ``date_field``, it defaults
                to ``issue_date``. If only ``start_datetime``/``end_datetime`` are provided without an explicit
                ``date_field``, it defaults to ``created_at`` instead. An unrecognized ``date_field`` is ignored rather
                than raising an error.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or after exact time provided in query. If provided, this
                parameter will be used instead of start_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or before exact time provided in query. If provided, this
                parameter will be used instead of end_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned credit notes, sorted by sequence_number.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            refunds: Include refunds data.
            applications: Include applications data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_credit_notes(
                subscription_id=subscription_id,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                page=page,
                per_page=per_page,
                direction=direction,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                refunds=refunds,
                applications=applications,
                request_options=request_options,
            ),
        )

    async def list_invoice_events(
        self,
        *,
        since_date: str | None = None,
        since_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        invoice_uid: str | None = None,
        with_change_invoice_status: str | None = None,
        event_types: list[InvoiceEventTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInvoiceEventsResponse:
        """Lists invoice events for a site. Each event contains event "data" (such as an applied payment) as well as a
        snapshot of the ``invoice`` at the time of event completion.

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

        If both a ``since_date`` and ``since_id`` are provided in request parameters, the ``since_date`` will be used.

        Note - invoice events that occurred prior to 09/05/2018 __will not__ contain an ``invoice`` snapshot.

        Args:
            since_date: The timestamp in a format ``YYYY-MM-DD T HH:MM:SS Z``, or ``YYYY-MM-DD``(in this case, it
                returns data from the beginning of the day). of the event from which you want to start the search. All
                the events before the ``since_date`` timestamp are not returned in the response.
            since_id: The ID of the event from which you want to start the search(ID is not included. e.g. if ID is set
                to 2, then all events with ID 3 and more will be shown) This parameter is not used if since_date is
                defined.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            invoice_uid: Providing an invoice_uid allows for scoping of the invoice events to a single invoice or credit
                note.
            with_change_invoice_status: Use this parameter if you want to fetch also invoice events with
                change_invoice_status type.
            event_types: Filter results by event_type. Supply a comma separated list of event types (listed above). Use
                in query: ``event_types=void_invoice,void_remainder``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_invoice_events(
                since_date=since_date,
                since_id=since_id,
                page=page,
                per_page=per_page,
                invoice_uid=invoice_uid,
                with_change_invoice_status=with_change_invoice_status,
                event_types=event_types,
                request_options=request_options,
            ),
        )

    async def list_invoices(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: InvoiceStatusOrStr | None = None,
        subscription_id: int | None = None,
        subscription_group_uid: str | None = None,
        consolidation_level: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        refunds: bool | None = False,
        date_field: InvoiceDateFieldOrStr | None = InvoiceDateField.DUE_DATE,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        customer_ids: list[int] | None = None,
        number: list[str] | None = None,
        product_ids: list[int] | None = None,
        sort: InvoiceSortFieldOrStr | None = InvoiceSortField.NUMBER,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInvoicesResponse:
        """Lists invoices for a site. By default, invoices returned on the index will only include totals, not detailed
        breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``, or
        ``refunds``. To include breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            subscription_id: The subscription's ID.
            subscription_group_uid: The UID of the subscription group you want to fetch consolidated invoices for. This
                will return a paginated list of consolidated invoices for the specified group.
            consolidation_level: The consolidation level of the invoice. Allowed Values: none, parent, child or
                comma-separated lists of thereof, e.g. none,parent.
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
            refunds: Include refunds data.
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date. Allowed to be used only along with date_field set to created_at or updated_at.
            customer_ids: Allows fetching invoices with matching customer id based on provided values. Use in query
                ``customer_ids=1,2,3``.
            number: Allows fetching invoices with matching invoice number based on provided values. Use in query
                ``number=1234,1235``.
            product_ids: Allows fetching invoices with matching line items product ids based on provided values. Use in
                query ``product_ids=23,34``.
            sort: Allows specification of the order of the returned list. Use in query ``sort=total_amount``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_invoices(
                start_date=start_date,
                end_date=end_date,
                status=status,
                subscription_id=subscription_id,
                subscription_group_uid=subscription_group_uid,
                consolidation_level=consolidation_level,
                page=page,
                per_page=per_page,
                direction=direction,
                line_items=line_items,
                discounts=discounts,
                taxes=taxes,
                credits_=credits_,
                payments=payments,
                custom_fields=custom_fields,
                refunds=refunds,
                date_field=date_field,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                customer_ids=customer_ids,
                number=number,
                product_ids=product_ids,
                sort=sort,
                request_options=request_options,
            ),
        )

    async def preview_customer_information_changes(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomerChangesPreviewResponse:
        """Previews the effect of customer information changes on an open invoice. Customer information may change after
        an invoice is issued, which may lead to a mismatch between customer information that is present on an open
        invoice and actual customer information. This endpoint allows you to preview these differences, if any.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.preview_customer_information_changes(uid, request_options=request_options)
        )

    async def read_credit_note(self, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> CreditNote:
        """Returns the details for a credit note.

        Args:
            uid: The unique identifier of the credit note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_credit_note(uid, request_options=request_options))

    async def read_invoice(self, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice:
        """Returns the details for an invoice.

        ## PDF Invoice retrieval

        Individual PDF Invoices can be retrieved by using the "Accept" header application/pdf or appending .pdf as the
        format portion of the URL: ```curl -u <api_key>:x -H Accept:application/pdf -H
        https://acme.chargify.com/invoices/inv_8gd8tdhtd3hgr.pdf > output_file.pdf URL:
        ``https://<subdomain>.chargify.com/invoices/<uid>.<format>`` Method: GET Required parameters: ``uid`` Response:
        A single Invoice.
        ```

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_invoice(uid, request_options=request_options))

    async def record_payment_for_invoice(
        self,
        uid: str,
        *,
        body: CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Applies a payment of a given type against a specific invoice. If you would like to apply a payment across
        multiple invoices, you can use the `Record Payment for Multiple Invoices
        <$e/Invoices/recordPaymentForMultipleInvoices>`__ endpoint.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.record_payment_for_invoice(uid, body=body, request_options=request_options)
        )

    async def record_payment_for_multiple_invoices(
        self,
        *,
        body: CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiInvoicePaymentResponse:
        """Records an external payment against multiple invoices.

        To apply a payment to multiple invoices, at minimum, specify the ``amount`` and ``applications`` (i.e.,
        ``invoice_uid`` and ``amount``) details.

        Note that the invoice payment amounts must be greater than 0. Total amount must be greater or equal to invoices
        payment amount sum.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.record_payment_for_multiple_invoices(
                body=body, request_options=request_options
            ),
        )

    async def record_payment_for_subscription(
        self,
        subscription_id: int,
        *,
        body: RecordPaymentRequest | RecordPaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RecordPaymentResponse:
        """Records an external payment made against a subscription that will pay partially or in full one or more
        invoices.

        Payment will be applied starting with the oldest open invoice and then next oldest, and so on until the amount
        of the payment is fully consumed.

        Excess payment will result in the creation of a prepayment on the Invoice Account.

        Only ungrouped or primary subscriptions may be paid using the "bulk" payment request.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.record_payment_for_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def refund_invoice(
        self,
        uid: str,
        *,
        body: RefundInvoiceRequest | RefundInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Refunds an invoice, segment, or consolidated invoice.

        ## Partial Refund for Consolidated Invoice

        A refund less than the total of a consolidated invoice will be split across its segments.

        For a $50.00 refund on a $100.00 consolidated invoice with one $60.00 segment and one $40.00 segment, the
        refunded amount will be applied as 50% of each ($30.00 and $20.00, respectively).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.refund_invoice(uid, body=body, request_options=request_options))

    async def reopen_invoice(self, uid: str, *, request_options: RequestOptionsOrDict | None = None) -> Invoice:
        """Reopens any invoice with the "canceled" status. Invoices enter "canceled" status if they were open at the
        time the subscription was canceled (whether through dunning or an intentional cancellation).

        Invoices with "canceled" status are no longer considered to be due. Once reopened, they are considered due for
        payment. Payment may then be captured in one of the following ways:

        - Reactivating the subscription, which will capture all open invoices (See note below about automatic reopening
            of invoices.)
        - Recording a payment directly against the invoice

        A note about reactivations: any canceled invoices from the most recent active period are automatically opened as
        a part of the reactivation process. Reactivating via this endpoint prior to reactivation is only necessary when
        you wish to capture older invoices from previous periods during the reactivation.

        ### Reopening Consolidated Invoices

        When reopening a consolidated invoice, all of its canceled segments will also be reopened.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``Any | None | ErrorListResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.reopen_invoice(uid, request_options=request_options))

    async def send_invoice(
        self,
        uid: str,
        *,
        body: SendInvoiceRequest | SendInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Sends an invoice to the customer via email. This endpoint supports the delivery of both ad-hoc and
        automatically generated invoices. Additionally, this endpoint supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        **File Attachments**: You can attach files to invoice emails using ``attachment_urls[]`` parameter by providing
        URLs to the files you want to attach. When using attachments, the request must use ``multipart/form-data``
        content type. Max 10 files, 10MB per file.

        If no recipient email addresses are specified in the request, then the subscription's default email
        configuration will be used. For example, if ``recipient_emails`` is left blank, then the invoice will be
        delivered to the subscription's customer email address.

        On success, a 204 no-content response will be returned. The response does not indicate that email(s) have been
        delivered, but instead indicates that emails have been successfully queued for delivery. If _any_ invalid or
        malformed email address is found in the request body, the entire request will be rejected and a 422 response
        will be returned.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.send_invoice(uid, body=body, request_options=request_options))

    async def update_customer_information(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Invoice:
        """Updates customer information on an open invoice and returns the updated invoice. If you would like to preview
        changes that will be applied, use the ``/invoices/{uid}/customer_information/preview.json`` endpoint first.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.update_customer_information(uid, request_options=request_options))

    async def update_invoice(
        self,
        subscription_id: int,
        uid: str,
        *,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvoiceResponse:
        """Updates an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be updated.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be updated through this endpoint and
        the request returns a ``422`` error. If the invoice does not belong to the provided subscription, a ``404``
        error is returned.

        Only the attributes submitted in the request are changed — omitted attributes keep their current values.

        ### Line Items

        The ``line_items`` array describes changes to the invoice's line items. Line items not referenced in the array
        remain unchanged.

        #### Adding a line item

        A line item without a ``uid`` is added to the invoice. The same line item types and options as on invoice
        creation are supported (custom items, ``product_id``, ``component_id``, price points, period date ranges,
        taxes).

        #### Updating a line item

        A line item with the ``uid`` of an existing line item updates that line item with the submitted attributes.
        Amounts and taxes are recalculated.

        #### Removing a line item

        A line item with a ``uid`` and ``"_destroy": true`` is removed from the invoice. Other line items remain
        unchanged.

        Referencing a ``uid`` which does not exist on the invoice returns a ``422`` error.

        ### Coupons

        When the ``coupons`` key is present, the submitted coupons replace all discounts currently applied to the
        invoice. Send an empty array to remove all discounts. Coupon options are the same as on invoice creation.

        ### Invoice Options

        #### Issue Date and Net Terms

        The ``issue_date`` parameter can be sent to change the invoice's issue date. Only today or dates in the past are
        accepted. The date is interpreted and validated in your site's time zone, using the ``YYYY-MM-DD`` format. The
        ``net_terms`` parameter indicates the number of days after the issue date on which the invoice is due. The due
        date is recalculated whenever the issue date or net terms change.

        #### Addresses

        The seller, shipping and billing addresses can be sent to replace the addresses on the invoice. Each address
        requires to send a ``first_name`` at a minimum in order to work. Taxes are recalculated after an address change.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter. Likewise, custom payment instructions can be sent with
        the ``payment_instructions`` parameter.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | ErrorArrayMapResponse1
                | RawError``."""
        return unwrap(
            await self._with_raw_response.update_invoice(
                subscription_id, uid, body=body, request_options=request_options
            ),
        )

    async def void_invoice(
        self,
        uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Invoice:
        """Voids any invoice with the "open" or "canceled" status. It will also allow voiding of an invoice with the
        "pending" status if it is not a consolidated invoice.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``Any | None | ErrorListResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.void_invoice(uid, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncInvoicesWithRawResponse:
        return self._with_raw_response


class InvoicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_invoice(
        self,
        subscription_id: int,
        *,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvoiceResponse, CreateInvoiceErrorBody]:
        """Creates an ad hoc invoice.

        ### Basic Behavior

        You can create a basic invoice by sending an array of line items to this endpoint. Each line item, at a minimum,
        must include a title, a quantity and a unit price. Example:

        ```json
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
        ```

        ### Catalog items Instead of creating custom products like in above example, You can pass existing items like
        products, components.

        ```json
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
        ```


        The price for each line item will be calculated as well as a total due amount for the invoice. Multiple line
        items can be sent.

        ### Line item types When defining a line item, You can choose one of 3 types for a line item: #### Custom item
        As shown in the basic behavior example, You can pass ``title`` and ``unit_price`` for custom item. #### Product
        id Product handle (with handle: prefix) or id from the scope of current subscription's site can be provided with
        ``product_id``. By default ``unit_price`` is taken from product's default price point, but can be overwritten by
        passing ``unit_price`` or ``product_price_point_id``. If ``product_id`` is used, following fields cannot be
        used: ``title``, ``component_id``. #### Component id Component handle (with handle: prefix) or id from the scope
        of current subscription's site can be provided with ``component_id``. If ``component_id`` is used, following
        fields cannot be used: ``title``, ``product_id``. By default ``unit_price`` is taken from product's default
        price point, but can be overwritten by passing ``unit_price`` or ``price_point_id``. At this moment price points
        are supported only for quantity based, on/off and metered components. For prepaid and event based billing
        components ``unit_price`` is required.

        ### Coupons When creating ad hoc invoice, new discounts can be applied in following way:

        ```json
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
        ```
        If You want to use existing coupon for discount creation, only ``code`` and optional ``product_family_id`` is
        needed

        ```json
        ...
         "coupons": [
              {
                "code": "FREESETUP",
                "product_family_id": 1
              }
          ]
        ...
        ```

        #### Using Coupon Subcodes You can also use coupon subcodes to apply existing coupons with specific subcodes:

        ```json
        ...
         "coupons": [
              {
                "subcode": "SUB1",
                "product_family_id": 1
              }
          ]
        ...
        ```
        **Important:** You cannot specify both ``code`` and ``subcode`` for the same coupon. Use either:
        - ``code`` to apply a main coupon
        - ``subcode`` to apply a specific coupon subcode

        The API response will include both the main coupon code and the subcode used:

        ```json
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
        ```

        ### Coupon options #### Code Coupon ``code`` will be displayed on invoice discount section. Coupon code can only
        contain uppercase letters, numbers, and allowed special characters. Lowercase letters will be converted to
        uppercase. It can be used to select an existing coupon from the catalog, or as an ad hoc coupon when passed with
        ``percentage`` or ``amount``. #### Subcode Coupon ``subcode`` allows you to apply existing coupons using their
        subcodes. When a subcode is used, the API response will include both the main coupon code and the specific
        subcode that was applied. Subcodes are case-insensitive and will be converted to uppercase automatically. ####
        Percentage Coupon ``percentage`` can take values from 0 to 100 and up to 4 decimal places. It cannot be used
        with ``amount``. Only for ad hoc coupons, will be ignored if ``code`` is used to select an existing coupon from
        the catalog. #### Amount Coupon ``amount`` takes number value. It cannot be used with ``percentage``. Used only
        when not matching existing coupon by ``code``. #### Description Optional ``description`` will be displayed with
        coupon ``code``. Used only when not matching existing coupon by ``code``. #### Product Family id Optional
        ``product_family_id`` handle (with handle: prefix) or id is used to match existing coupon within site, when
        codes are not unique. #### Compounding Strategy Optional ``compounding_strategy`` for percentage coupons, can
        take values ``compound`` or ``full-price``.

        For amount coupons, discounts will be always calculated against the original item price, before other discounts
        are applied.

        ``compound`` strategy: Percentage-based discounts will be calculated against the remaining price, after prior
        discounts have been calculated. It is set by default.

        ``full-price`` strategy: Percentage-based discounts will always be calculated against the original item price,
        before other discounts are applied.

        ### Line Item Options

        #### Period Date Range

        A custom period date range can be defined for each line item with the ``period_range_start`` and
        ``period_range_end`` parameters. Dates must be sent in the ``YYYY-MM-DD`` format. ``period_range_end`` must be
        greater or equal ``period_range_start``.

        #### Taxes

        The ``taxable`` parameter can be sent as ``true`` if taxes should be calculated for a specific line item. For
        this to work, the site should be configured to use and calculate taxes. Further, if the site uses Avalara for
        tax calculations, a ``tax_code`` parameter should also be sent. For existing catalog items: products/components
        taxes cannot be overwritten.

        #### Price Point Price point handle (with handle: prefix) or id from the scope of current subscription's site
        can be provided with ``price_point_id`` for components with ``component_id`` or ``product_price_point_id`` for
        products with ``product_id`` parameter. If price point is passed ``unit_price`` cannot be used. It can be used
        only with catalog items products and components.

        #### Description Optional ``description`` parameter, it will overwrite default generated description for line
        item.

        ### Invoice Options

        #### Issue Date

        By default, invoices will be created with a issue date set to today in your site's time zone. The ``issue_date``
        parameter can be sent to alter the default. Only today or dates in the past are accepted. This date is
        interpreted and validated in your site's time zone. The format for ``issue_date`` is ``YYYY-MM-DD``.

        #### Net Terms

        By default, invoices will be created with a due date matching the date of invoice creation. If a different due
        date is desired, the ``net_terms`` parameter can be sent indicating the number of days in advance the due date
        should be.

        #### Addresses

        The seller, shipping and billing addresses can be sent to override the site's defaults. Each address requires to
        send a ``first_name`` at a minimum in order to work. See below for the details on which parameters can be sent
        for each address object.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter to override the site's default. Likewise, custom payment
        instructions can be sent with the ``payment_instructions`` parameter.

        #### Status

        By default, invoices will be created with open status. Possible alternative is ``draft``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/invoices.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateInvoiceRequest | CreateInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[InvoiceResponse],
            error_mapper=create_invoice_error_mapper,
            request_options=request_options,
        )

    def delete_invoice(
        self, subscription_id: int, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteInvoiceErrorBody]:
        """Deletes an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be deleted.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be deleted through this endpoint and
        the request returns a ``422`` error. Issued invoices should be voided instead. If the invoice does not belong to
        the provided subscription, a ``404`` error is returned.

        A successful deletion returns a ``204 No Content`` response and the invoice is permanently removed.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/invoices/{uid}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_invoice_error_mapper,
            request_options=request_options,
        )

    def issue_invoice(
        self,
        uid: str,
        *,
        body: IssueInvoiceRequest | IssueInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, IssueInvoiceErrorBody]:
        """Issues an invoice that is in "pending" or "draft" status. For example, you can issue an invoice that was
        created when allocating new quantity on a component and using "accrue charges" option.

        You cannot issue a pending child invoice that was created for a member subscription in a group.

        For Remittance subscriptions, the invoice will go into "open" status and payment won't be attempted. The value
        for ``on_failed_payment`` would be rejected if sent. Any prepayments or service credits that exist on the
        subscription will be automatically applied. Additionally, if the setting is enabled, an email will be sent for
        the issued invoice.

        For Automatic subscriptions, prepayments and service credits will apply to the invoice before payment is
        attempted. On successful payment, the invoice will go into "paid" status and email will be sent to the customer
        (if setting applies). When payment fails, the next event depends on the ``on_failed_payment`` value:
        - ``leave_open_invoice`` - prepayments and credits applied to invoice; invoice status set to "open"; email sent
            to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history. This is the default option.
        - ``rollback_to_pending`` - prepayments and credits not applied; invoice remains in "pending" status; no email
            sent to the customer; payment failure recorded in the invoice history.
        - ``initiate_dunning`` - prepayments and credits applied to the invoice; invoice status set to "open"; email
            sent to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history; subscription will most likely go into "past_due" or "canceled" state (depending upon net terms and
            dunning settings).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/issue.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueInvoiceRequest | IssueInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=issue_invoice_error_mapper,
            request_options=request_options,
        )

    def list_consolidated_invoice_segments(
        self,
        invoice_uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConsolidatedInvoice, RawError]:
        """Lists segments for a consolidated invoice. Invoice segments returned on the index will only include totals,
        not detailed breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or
        ``custom_fields``.

        Args:
            invoice_uid: The unique identifier of the consolidated invoice
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Sort direction of the returned segments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices/{invoice_uid}/segments.json"),
            path_params=[param[str]("invoice_uid", invoice_uid)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ConsolidatedInvoice],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_credit_notes(
        self,
        *,
        subscription_id: int | None = None,
        date_field: CreditNoteDateFieldOrStr | None = CreditNoteDateField.ISSUE_DATE,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        refunds: bool | None = False,
        applications: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCreditNotesResponse, RawError]:
        """Lists credit notes for a site. Credit Notes are like inverse invoices. They reduce the amount a customer
        owes.

        By default, the credit notes returned by this endpoint will exclude the arrays of ``line_items``, ``discounts``,
        ``taxes``, ``applications``, or ``refunds``. To include these arrays, pass the specific field as a key in the
        query with a value set to ``true``.

        Args:
            subscription_id: The subscription's Advanced Billing id
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``. If a date range is provided without an explicit ``date_field``, it defaults
                to ``issue_date``. If only ``start_datetime``/``end_datetime`` are provided without an explicit
                ``date_field``, it defaults to ``created_at`` instead. An unrecognized ``date_field`` is ignored rather
                than raising an error.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or after exact time provided in query. If provided, this
                parameter will be used instead of start_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or before exact time provided in query. If provided, this
                parameter will be used instead of end_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned credit notes, sorted by sequence_number.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            refunds: Include refunds data.
            applications: Include applications data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/credit_notes.json"),
            query_params=[
                param[int | None]("subscription_id", subscription_id),
                param[CreditNoteDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("refunds", refunds),
                param[bool | None]("applications", applications),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListCreditNotesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_invoice_events(
        self,
        *,
        since_date: str | None = None,
        since_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        invoice_uid: str | None = None,
        with_change_invoice_status: str | None = None,
        event_types: list[InvoiceEventTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInvoiceEventsResponse, RawError]:
        """Lists invoice events for a site. Each event contains event "data" (such as an applied payment) as well as a
        snapshot of the ``invoice`` at the time of event completion.

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

        If both a ``since_date`` and ``since_id`` are provided in request parameters, the ``since_date`` will be used.

        Note - invoice events that occurred prior to 09/05/2018 __will not__ contain an ``invoice`` snapshot.

        Args:
            since_date: The timestamp in a format ``YYYY-MM-DD T HH:MM:SS Z``, or ``YYYY-MM-DD``(in this case, it
                returns data from the beginning of the day). of the event from which you want to start the search. All
                the events before the ``since_date`` timestamp are not returned in the response.
            since_id: The ID of the event from which you want to start the search(ID is not included. e.g. if ID is set
                to 2, then all events with ID 3 and more will be shown) This parameter is not used if since_date is
                defined.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            invoice_uid: Providing an invoice_uid allows for scoping of the invoice events to a single invoice or credit
                note.
            with_change_invoice_status: Use this parameter if you want to fetch also invoice events with
                change_invoice_status type.
            event_types: Filter results by event_type. Supply a comma separated list of event types (listed above). Use
                in query: ``event_types=void_invoice,void_remainder``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices/events.json"),
            query_params=[
                param[str | None]("since_date", since_date),
                param[int | None]("since_id", since_id),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("invoice_uid", invoice_uid),
                param[str | None]("with_change_invoice_status", with_change_invoice_status),
                param[list[InvoiceEventTypeOrStr] | None]("event_types", event_types),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListInvoiceEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_invoices(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: InvoiceStatusOrStr | None = None,
        subscription_id: int | None = None,
        subscription_group_uid: str | None = None,
        consolidation_level: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        refunds: bool | None = False,
        date_field: InvoiceDateFieldOrStr | None = InvoiceDateField.DUE_DATE,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        customer_ids: list[int] | None = None,
        number: list[str] | None = None,
        product_ids: list[int] | None = None,
        sort: InvoiceSortFieldOrStr | None = InvoiceSortField.NUMBER,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInvoicesResponse, RawError]:
        """Lists invoices for a site. By default, invoices returned on the index will only include totals, not detailed
        breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``, or
        ``refunds``. To include breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            subscription_id: The subscription's ID.
            subscription_group_uid: The UID of the subscription group you want to fetch consolidated invoices for. This
                will return a paginated list of consolidated invoices for the specified group.
            consolidation_level: The consolidation level of the invoice. Allowed Values: none, parent, child or
                comma-separated lists of thereof, e.g. none,parent.
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
            refunds: Include refunds data.
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date. Allowed to be used only along with date_field set to created_at or updated_at.
            customer_ids: Allows fetching invoices with matching customer id based on provided values. Use in query
                ``customer_ids=1,2,3``.
            number: Allows fetching invoices with matching invoice number based on provided values. Use in query
                ``number=1234,1235``.
            product_ids: Allows fetching invoices with matching line items product ids based on provided values. Use in
                query ``product_ids=23,34``.
            sort: Allows specification of the order of the returned list. Use in query ``sort=total_amount``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices.json"),
            query_params=[
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[InvoiceStatusOrStr | None]("status", status),
                param[int | None]("subscription_id", subscription_id),
                param[str | None]("subscription_group_uid", subscription_group_uid),
                param[str | None]("consolidation_level", consolidation_level),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("credits", credits_),
                param[bool | None]("payments", payments),
                param[bool | None]("custom_fields", custom_fields),
                param[bool | None]("refunds", refunds),
                param[InvoiceDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[list[int] | None]("customer_ids", customer_ids),
                param[list[str] | None]("number", number),
                param[list[int] | None]("product_ids", product_ids),
                param[InvoiceSortFieldOrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def preview_customer_information_changes(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerChangesPreviewResponse, PreviewCustomerInformationChangesErrorBody]:
        """Previews the effect of customer information changes on an open invoice. Customer information may change after
        an invoice is issued, which may lead to a mismatch between customer information that is present on an open
        invoice and actual customer information. This endpoint allows you to preview these differences, if any.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/customer_information/preview.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CustomerChangesPreviewResponse],
            error_mapper=preview_customer_information_changes_error_mapper,
            request_options=request_options,
        )

    def read_credit_note(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreditNote, RawError]:
        """Returns the details for a credit note.

        Args:
            uid: The unique identifier of the credit note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/credit_notes/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CreditNote],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, RawError]:
        """Returns the details for an invoice.

        ## PDF Invoice retrieval

        Individual PDF Invoices can be retrieved by using the "Accept" header application/pdf or appending .pdf as the
        format portion of the URL: ```curl -u <api_key>:x -H Accept:application/pdf -H
        https://acme.chargify.com/invoices/inv_8gd8tdhtd3hgr.pdf > output_file.pdf URL:
        ``https://<subdomain>.chargify.com/invoices/<uid>.<format>`` Method: GET Required parameters: ``uid`` Response:
        A single Invoice.
        ```

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def record_payment_for_invoice(
        self,
        uid: str,
        *,
        body: CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, RecordPaymentForInvoiceErrorBody]:
        """Applies a payment of a given type against a specific invoice. If you would like to apply a payment across
        multiple invoices, you can use the `Record Payment for Multiple Invoices
        <$e/Invoices/recordPaymentForMultipleInvoices>`__ endpoint.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/payments.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=record_payment_for_invoice_error_mapper,
            request_options=request_options,
        )

    def record_payment_for_multiple_invoices(
        self,
        *,
        body: CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiInvoicePaymentResponse, RecordPaymentForMultipleInvoicesErrorBody]:
        """Records an external payment against multiple invoices.

        To apply a payment to multiple invoices, at minimum, specify the ``amount`` and ``applications`` (i.e.,
        ``invoice_uid`` and ``amount``) details.

        Note that the invoice payment amounts must be greater than 0. Total amount must be greater or equal to invoices
        payment amount sum.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/payments.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[MultiInvoicePaymentResponse],
            error_mapper=record_payment_for_multiple_invoices_error_mapper,
            request_options=request_options,
        )

    def record_payment_for_subscription(
        self,
        subscription_id: int,
        *,
        body: RecordPaymentRequest | RecordPaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecordPaymentResponse, RecordPaymentForSubscriptionErrorBody]:
        """Records an external payment made against a subscription that will pay partially or in full one or more
        invoices.

        Payment will be applied starting with the oldest open invoice and then next oldest, and so on until the amount
        of the payment is fully consumed.

        Excess payment will result in the creation of a prepayment on the Invoice Account.

        Only ungrouped or primary subscriptions may be paid using the "bulk" payment request.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/payments.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RecordPaymentRequest | RecordPaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[RecordPaymentResponse],
            error_mapper=record_payment_for_subscription_error_mapper,
            request_options=request_options,
        )

    def refund_invoice(
        self,
        uid: str,
        *,
        body: RefundInvoiceRequest | RefundInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, RefundInvoiceErrorBody]:
        """Refunds an invoice, segment, or consolidated invoice.

        ## Partial Refund for Consolidated Invoice

        A refund less than the total of a consolidated invoice will be split across its segments.

        For a $50.00 refund on a $100.00 consolidated invoice with one $60.00 segment and one $40.00 segment, the
        refunded amount will be applied as 50% of each ($30.00 and $20.00, respectively).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/refunds.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundInvoiceRequest | RefundInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=refund_invoice_error_mapper,
            request_options=request_options,
        )

    def reopen_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, ReopenInvoiceErrorBody]:
        """Reopens any invoice with the "canceled" status. Invoices enter "canceled" status if they were open at the
        time the subscription was canceled (whether through dunning or an intentional cancellation).

        Invoices with "canceled" status are no longer considered to be due. Once reopened, they are considered due for
        payment. Payment may then be captured in one of the following ways:

        - Reactivating the subscription, which will capture all open invoices (See note below about automatic reopening
            of invoices.)
        - Recording a payment directly against the invoice

        A note about reactivations: any canceled invoices from the most recent active period are automatically opened as
        a part of the reactivation process. Reactivating via this endpoint prior to reactivation is only necessary when
        you wish to capture older invoices from previous periods during the reactivation.

        ### Reopening Consolidated Invoices

        When reopening a consolidated invoice, all of its canceled segments will also be reopened.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/reopen.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=reopen_invoice_error_mapper,
            request_options=request_options,
        )

    def send_invoice(
        self,
        uid: str,
        *,
        body: SendInvoiceRequest | SendInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SendInvoiceErrorBody]:
        """Sends an invoice to the customer via email. This endpoint supports the delivery of both ad-hoc and
        automatically generated invoices. Additionally, this endpoint supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        **File Attachments**: You can attach files to invoice emails using ``attachment_urls[]`` parameter by providing
        URLs to the files you want to attach. When using attachments, the request must use ``multipart/form-data``
        content type. Max 10 files, 10MB per file.

        If no recipient email addresses are specified in the request, then the subscription's default email
        configuration will be used. For example, if ``recipient_emails`` is left blank, then the invoice will be
        delivered to the subscription's customer email address.

        On success, a 204 no-content response will be returned. The response does not indicate that email(s) have been
        delivered, but instead indicates that emails have been successfully queued for delivery. If _any_ invalid or
        malformed email address is found in the request body, the entire request will be rejected and a 422 response
        will be returned.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/deliveries.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SendInvoiceRequest | SendInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=send_invoice_error_mapper,
            request_options=request_options,
        )

    def update_customer_information(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, UpdateCustomerInformationErrorBody]:
        """Updates customer information on an open invoice and returns the updated invoice. If you would like to preview
        changes that will be applied, use the ``/invoices/{uid}/customer_information/preview.json`` endpoint first.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/invoices/{uid}/customer_information.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=update_customer_information_error_mapper,
            request_options=request_options,
        )

    def update_invoice(
        self,
        subscription_id: int,
        uid: str,
        *,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvoiceResponse, UpdateInvoiceErrorBody]:
        """Updates an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be updated.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be updated through this endpoint and
        the request returns a ``422`` error. If the invoice does not belong to the provided subscription, a ``404``
        error is returned.

        Only the attributes submitted in the request are changed — omitted attributes keep their current values.

        ### Line Items

        The ``line_items`` array describes changes to the invoice's line items. Line items not referenced in the array
        remain unchanged.

        #### Adding a line item

        A line item without a ``uid`` is added to the invoice. The same line item types and options as on invoice
        creation are supported (custom items, ``product_id``, ``component_id``, price points, period date ranges,
        taxes).

        #### Updating a line item

        A line item with the ``uid`` of an existing line item updates that line item with the submitted attributes.
        Amounts and taxes are recalculated.

        #### Removing a line item

        A line item with a ``uid`` and ``"_destroy": true`` is removed from the invoice. Other line items remain
        unchanged.

        Referencing a ``uid`` which does not exist on the invoice returns a ``422`` error.

        ### Coupons

        When the ``coupons`` key is present, the submitted coupons replace all discounts currently applied to the
        invoice. Send an empty array to remove all discounts. Coupon options are the same as on invoice creation.

        ### Invoice Options

        #### Issue Date and Net Terms

        The ``issue_date`` parameter can be sent to change the invoice's issue date. Only today or dates in the past are
        accepted. The date is interpreted and validated in your site's time zone, using the ``YYYY-MM-DD`` format. The
        ``net_terms`` parameter indicates the number of days after the issue date on which the invoice is due. The due
        date is recalculated whenever the issue date or net terms change.

        #### Addresses

        The seller, shipping and billing addresses can be sent to replace the addresses on the invoice. Each address
        requires to send a ``first_name`` at a minimum in order to work. Taxes are recalculated after an address change.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter. Likewise, custom payment instructions can be sent with
        the ``payment_instructions`` parameter.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/invoices/{uid}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateInvoiceRequest | UpdateInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[InvoiceResponse],
            error_mapper=update_invoice_error_mapper,
            request_options=request_options,
        )

    def void_invoice(
        self,
        uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, VoidInvoiceErrorBody]:
        """Voids any invoice with the "open" or "canceled" status. It will also allow voiding of an invoice with the
        "pending" status if it is not a consolidated invoice.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/void.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidInvoiceRequest | VoidInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Invoice],
            error_mapper=void_invoice_error_mapper,
            request_options=request_options,
        )


class AsyncInvoicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_invoice(
        self,
        subscription_id: int,
        *,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvoiceResponse, CreateInvoiceErrorBody]:
        """Creates an ad hoc invoice.

        ### Basic Behavior

        You can create a basic invoice by sending an array of line items to this endpoint. Each line item, at a minimum,
        must include a title, a quantity and a unit price. Example:

        ```json
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
        ```

        ### Catalog items Instead of creating custom products like in above example, You can pass existing items like
        products, components.

        ```json
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
        ```


        The price for each line item will be calculated as well as a total due amount for the invoice. Multiple line
        items can be sent.

        ### Line item types When defining a line item, You can choose one of 3 types for a line item: #### Custom item
        As shown in the basic behavior example, You can pass ``title`` and ``unit_price`` for custom item. #### Product
        id Product handle (with handle: prefix) or id from the scope of current subscription's site can be provided with
        ``product_id``. By default ``unit_price`` is taken from product's default price point, but can be overwritten by
        passing ``unit_price`` or ``product_price_point_id``. If ``product_id`` is used, following fields cannot be
        used: ``title``, ``component_id``. #### Component id Component handle (with handle: prefix) or id from the scope
        of current subscription's site can be provided with ``component_id``. If ``component_id`` is used, following
        fields cannot be used: ``title``, ``product_id``. By default ``unit_price`` is taken from product's default
        price point, but can be overwritten by passing ``unit_price`` or ``price_point_id``. At this moment price points
        are supported only for quantity based, on/off and metered components. For prepaid and event based billing
        components ``unit_price`` is required.

        ### Coupons When creating ad hoc invoice, new discounts can be applied in following way:

        ```json
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
        ```
        If You want to use existing coupon for discount creation, only ``code`` and optional ``product_family_id`` is
        needed

        ```json
        ...
         "coupons": [
              {
                "code": "FREESETUP",
                "product_family_id": 1
              }
          ]
        ...
        ```

        #### Using Coupon Subcodes You can also use coupon subcodes to apply existing coupons with specific subcodes:

        ```json
        ...
         "coupons": [
              {
                "subcode": "SUB1",
                "product_family_id": 1
              }
          ]
        ...
        ```
        **Important:** You cannot specify both ``code`` and ``subcode`` for the same coupon. Use either:
        - ``code`` to apply a main coupon
        - ``subcode`` to apply a specific coupon subcode

        The API response will include both the main coupon code and the subcode used:

        ```json
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
        ```

        ### Coupon options #### Code Coupon ``code`` will be displayed on invoice discount section. Coupon code can only
        contain uppercase letters, numbers, and allowed special characters. Lowercase letters will be converted to
        uppercase. It can be used to select an existing coupon from the catalog, or as an ad hoc coupon when passed with
        ``percentage`` or ``amount``. #### Subcode Coupon ``subcode`` allows you to apply existing coupons using their
        subcodes. When a subcode is used, the API response will include both the main coupon code and the specific
        subcode that was applied. Subcodes are case-insensitive and will be converted to uppercase automatically. ####
        Percentage Coupon ``percentage`` can take values from 0 to 100 and up to 4 decimal places. It cannot be used
        with ``amount``. Only for ad hoc coupons, will be ignored if ``code`` is used to select an existing coupon from
        the catalog. #### Amount Coupon ``amount`` takes number value. It cannot be used with ``percentage``. Used only
        when not matching existing coupon by ``code``. #### Description Optional ``description`` will be displayed with
        coupon ``code``. Used only when not matching existing coupon by ``code``. #### Product Family id Optional
        ``product_family_id`` handle (with handle: prefix) or id is used to match existing coupon within site, when
        codes are not unique. #### Compounding Strategy Optional ``compounding_strategy`` for percentage coupons, can
        take values ``compound`` or ``full-price``.

        For amount coupons, discounts will be always calculated against the original item price, before other discounts
        are applied.

        ``compound`` strategy: Percentage-based discounts will be calculated against the remaining price, after prior
        discounts have been calculated. It is set by default.

        ``full-price`` strategy: Percentage-based discounts will always be calculated against the original item price,
        before other discounts are applied.

        ### Line Item Options

        #### Period Date Range

        A custom period date range can be defined for each line item with the ``period_range_start`` and
        ``period_range_end`` parameters. Dates must be sent in the ``YYYY-MM-DD`` format. ``period_range_end`` must be
        greater or equal ``period_range_start``.

        #### Taxes

        The ``taxable`` parameter can be sent as ``true`` if taxes should be calculated for a specific line item. For
        this to work, the site should be configured to use and calculate taxes. Further, if the site uses Avalara for
        tax calculations, a ``tax_code`` parameter should also be sent. For existing catalog items: products/components
        taxes cannot be overwritten.

        #### Price Point Price point handle (with handle: prefix) or id from the scope of current subscription's site
        can be provided with ``price_point_id`` for components with ``component_id`` or ``product_price_point_id`` for
        products with ``product_id`` parameter. If price point is passed ``unit_price`` cannot be used. It can be used
        only with catalog items products and components.

        #### Description Optional ``description`` parameter, it will overwrite default generated description for line
        item.

        ### Invoice Options

        #### Issue Date

        By default, invoices will be created with a issue date set to today in your site's time zone. The ``issue_date``
        parameter can be sent to alter the default. Only today or dates in the past are accepted. This date is
        interpreted and validated in your site's time zone. The format for ``issue_date`` is ``YYYY-MM-DD``.

        #### Net Terms

        By default, invoices will be created with a due date matching the date of invoice creation. If a different due
        date is desired, the ``net_terms`` parameter can be sent indicating the number of days in advance the due date
        should be.

        #### Addresses

        The seller, shipping and billing addresses can be sent to override the site's defaults. Each address requires to
        send a ``first_name`` at a minimum in order to work. See below for the details on which parameters can be sent
        for each address object.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter to override the site's default. Likewise, custom payment
        instructions can be sent with the ``payment_instructions`` parameter.

        #### Status

        By default, invoices will be created with open status. Possible alternative is ``draft``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/invoices.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateInvoiceRequest | CreateInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[InvoiceResponse],
            error_mapper=create_invoice_error_mapper,
            request_options=request_options,
        )

    async def delete_invoice(
        self, subscription_id: int, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteInvoiceErrorBody]:
        """Deletes an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be deleted.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be deleted through this endpoint and
        the request returns a ``422`` error. Issued invoices should be voided instead. If the invoice does not belong to
        the provided subscription, a ``404`` error is returned.

        A successful deletion returns a ``204 No Content`` response and the invoice is permanently removed.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/invoices/{uid}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_invoice_error_mapper,
            request_options=request_options,
        )

    async def issue_invoice(
        self,
        uid: str,
        *,
        body: IssueInvoiceRequest | IssueInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, IssueInvoiceErrorBody]:
        """Issues an invoice that is in "pending" or "draft" status. For example, you can issue an invoice that was
        created when allocating new quantity on a component and using "accrue charges" option.

        You cannot issue a pending child invoice that was created for a member subscription in a group.

        For Remittance subscriptions, the invoice will go into "open" status and payment won't be attempted. The value
        for ``on_failed_payment`` would be rejected if sent. Any prepayments or service credits that exist on the
        subscription will be automatically applied. Additionally, if the setting is enabled, an email will be sent for
        the issued invoice.

        For Automatic subscriptions, prepayments and service credits will apply to the invoice before payment is
        attempted. On successful payment, the invoice will go into "paid" status and email will be sent to the customer
        (if setting applies). When payment fails, the next event depends on the ``on_failed_payment`` value:
        - ``leave_open_invoice`` - prepayments and credits applied to invoice; invoice status set to "open"; email sent
            to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history. This is the default option.
        - ``rollback_to_pending`` - prepayments and credits not applied; invoice remains in "pending" status; no email
            sent to the customer; payment failure recorded in the invoice history.
        - ``initiate_dunning`` - prepayments and credits applied to the invoice; invoice status set to "open"; email
            sent to the customer for the issued invoice (if setting applies); payment failure recorded in the invoice
            history; subscription will most likely go into "past_due" or "canceled" state (depending upon net terms and
            dunning settings).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/issue.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueInvoiceRequest | IssueInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=issue_invoice_error_mapper,
            request_options=request_options,
        )

    async def list_consolidated_invoice_segments(
        self,
        invoice_uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConsolidatedInvoice, RawError]:
        """Lists segments for a consolidated invoice. Invoice segments returned on the index will only include totals,
        not detailed breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, or
        ``custom_fields``.

        Args:
            invoice_uid: The unique identifier of the consolidated invoice
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Sort direction of the returned segments.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices/{invoice_uid}/segments.json"),
            path_params=[param[str]("invoice_uid", invoice_uid)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ConsolidatedInvoice],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_credit_notes(
        self,
        *,
        subscription_id: int | None = None,
        date_field: CreditNoteDateFieldOrStr | None = CreditNoteDateField.ISSUE_DATE,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        refunds: bool | None = False,
        applications: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCreditNotesResponse, RawError]:
        """Lists credit notes for a site. Credit Notes are like inverse invoices. They reduce the amount a customer
        owes.

        By default, the credit notes returned by this endpoint will exclude the arrays of ``line_items``, ``discounts``,
        ``taxes``, ``applications``, or ``refunds``. To include these arrays, pass the specific field as a key in the
        query with a value set to ``true``.

        Args:
            subscription_id: The subscription's Advanced Billing id
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``. If a date range is provided without an explicit ``date_field``, it defaults
                to ``issue_date``. If only ``start_datetime``/``end_datetime`` are provided without an explicit
                ``date_field``, it defaults to ``created_at`` instead. An unrecognized ``date_field`` is ignored rather
                than raising an error.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or after exact time provided in query. If provided, this
                parameter will be used instead of start_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns credit notes with a timestamp at or before exact time provided in query. If provided, this
                parameter will be used instead of end_date. If no timezone offset is included in the value, it is
                interpreted as UTC. Allowed to be used only along with date_field set to created_at or updated_at.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: The sort direction of the returned credit notes, sorted by sequence_number.
            line_items: Include line items data.
            discounts: Include discounts data.
            taxes: Include taxes data.
            refunds: Include refunds data.
            applications: Include applications data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/credit_notes.json"),
            query_params=[
                param[int | None]("subscription_id", subscription_id),
                param[CreditNoteDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("refunds", refunds),
                param[bool | None]("applications", applications),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListCreditNotesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_invoice_events(
        self,
        *,
        since_date: str | None = None,
        since_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        invoice_uid: str | None = None,
        with_change_invoice_status: str | None = None,
        event_types: list[InvoiceEventTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInvoiceEventsResponse, RawError]:
        """Lists invoice events for a site. Each event contains event "data" (such as an applied payment) as well as a
        snapshot of the ``invoice`` at the time of event completion.

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

        If both a ``since_date`` and ``since_id`` are provided in request parameters, the ``since_date`` will be used.

        Note - invoice events that occurred prior to 09/05/2018 __will not__ contain an ``invoice`` snapshot.

        Args:
            since_date: The timestamp in a format ``YYYY-MM-DD T HH:MM:SS Z``, or ``YYYY-MM-DD``(in this case, it
                returns data from the beginning of the day). of the event from which you want to start the search. All
                the events before the ``since_date`` timestamp are not returned in the response.
            since_id: The ID of the event from which you want to start the search(ID is not included. e.g. if ID is set
                to 2, then all events with ID 3 and more will be shown) This parameter is not used if since_date is
                defined.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            invoice_uid: Providing an invoice_uid allows for scoping of the invoice events to a single invoice or credit
                note.
            with_change_invoice_status: Use this parameter if you want to fetch also invoice events with
                change_invoice_status type.
            event_types: Filter results by event_type. Supply a comma separated list of event types (listed above). Use
                in query: ``event_types=void_invoice,void_remainder``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices/events.json"),
            query_params=[
                param[str | None]("since_date", since_date),
                param[int | None]("since_id", since_id),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[str | None]("invoice_uid", invoice_uid),
                param[str | None]("with_change_invoice_status", with_change_invoice_status),
                param[list[InvoiceEventTypeOrStr] | None]("event_types", event_types),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListInvoiceEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_invoices(
        self,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
        status: InvoiceStatusOrStr | None = None,
        subscription_id: int | None = None,
        subscription_group_uid: str | None = None,
        consolidation_level: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = Direction.DESC,
        line_items: bool | None = False,
        discounts: bool | None = False,
        taxes: bool | None = False,
        credits_: bool | None = False,
        payments: bool | None = False,
        custom_fields: bool | None = False,
        refunds: bool | None = False,
        date_field: InvoiceDateFieldOrStr | None = InvoiceDateField.DUE_DATE,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        customer_ids: list[int] | None = None,
        number: list[str] | None = None,
        product_ids: list[int] | None = None,
        sort: InvoiceSortFieldOrStr | None = InvoiceSortField.NUMBER,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInvoicesResponse, RawError]:
        """Lists invoices for a site. By default, invoices returned on the index will only include totals, not detailed
        breakdowns for ``line_items``, ``discounts``, ``taxes``, ``credits``, ``payments``, ``custom_fields``, or
        ``refunds``. To include breakdowns, pass the specific field as a key in the query with a value set to ``true``.

        Args:
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            status: The current status of the invoice. Allowed Values: draft, open, paid, pending, voided
            subscription_id: The subscription's ID.
            subscription_group_uid: The UID of the subscription group you want to fetch consolidated invoices for. This
                will return a paginated list of consolidated invoices for the specified group.
            consolidation_level: The consolidation level of the invoice. Allowed Values: none, parent, child or
                comma-separated lists of thereof, e.g. none,parent.
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
            refunds: Include refunds data.
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=issue_date``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date. Allowed to be used only along with date_field set to created_at or updated_at.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns invoices with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date. Allowed to be used only along with date_field set to created_at or updated_at.
            customer_ids: Allows fetching invoices with matching customer id based on provided values. Use in query
                ``customer_ids=1,2,3``.
            number: Allows fetching invoices with matching invoice number based on provided values. Use in query
                ``number=1234,1235``.
            product_ids: Allows fetching invoices with matching line items product ids based on provided values. Use in
                query ``product_ids=23,34``.
            sort: Allows specification of the order of the returned list. Use in query ``sort=total_amount``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices.json"),
            query_params=[
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[InvoiceStatusOrStr | None]("status", status),
                param[int | None]("subscription_id", subscription_id),
                param[str | None]("subscription_group_uid", subscription_group_uid),
                param[str | None]("consolidation_level", consolidation_level),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
                param[bool | None]("line_items", line_items),
                param[bool | None]("discounts", discounts),
                param[bool | None]("taxes", taxes),
                param[bool | None]("credits", credits_),
                param[bool | None]("payments", payments),
                param[bool | None]("custom_fields", custom_fields),
                param[bool | None]("refunds", refunds),
                param[InvoiceDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[list[int] | None]("customer_ids", customer_ids),
                param[list[str] | None]("number", number),
                param[list[int] | None]("product_ids", product_ids),
                param[InvoiceSortFieldOrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def preview_customer_information_changes(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerChangesPreviewResponse, PreviewCustomerInformationChangesErrorBody]:
        """Previews the effect of customer information changes on an open invoice. Customer information may change after
        an invoice is issued, which may lead to a mismatch between customer information that is present on an open
        invoice and actual customer information. This endpoint allows you to preview these differences, if any.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/customer_information/preview.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CustomerChangesPreviewResponse],
            error_mapper=preview_customer_information_changes_error_mapper,
            request_options=request_options,
        )

    async def read_credit_note(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreditNote, RawError]:
        """Returns the details for a credit note.

        Args:
            uid: The unique identifier of the credit note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/credit_notes/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CreditNote],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, RawError]:
        """Returns the details for an invoice.

        ## PDF Invoice retrieval

        Individual PDF Invoices can be retrieved by using the "Accept" header application/pdf or appending .pdf as the
        format portion of the URL: ```curl -u <api_key>:x -H Accept:application/pdf -H
        https://acme.chargify.com/invoices/inv_8gd8tdhtd3hgr.pdf > output_file.pdf URL:
        ``https://<subdomain>.chargify.com/invoices/<uid>.<format>`` Method: GET Required parameters: ``uid`` Response:
        A single Invoice.
        ```

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/invoices/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def record_payment_for_invoice(
        self,
        uid: str,
        *,
        body: CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, RecordPaymentForInvoiceErrorBody]:
        """Applies a payment of a given type against a specific invoice. If you would like to apply a payment across
        multiple invoices, you can use the `Record Payment for Multiple Invoices
        <$e/Invoices/recordPaymentForMultipleInvoices>`__ endpoint.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/payments.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateInvoicePaymentRequest | CreateInvoicePaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=record_payment_for_invoice_error_mapper,
            request_options=request_options,
        )

    async def record_payment_for_multiple_invoices(
        self,
        *,
        body: CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiInvoicePaymentResponse, RecordPaymentForMultipleInvoicesErrorBody]:
        """Records an external payment against multiple invoices.

        To apply a payment to multiple invoices, at minimum, specify the ``amount`` and ``applications`` (i.e.,
        ``invoice_uid`` and ``amount``) details.

        Note that the invoice payment amounts must be greater than 0. Total amount must be greater or equal to invoices
        payment amount sum.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/payments.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMultiInvoicePaymentRequest | CreateMultiInvoicePaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[MultiInvoicePaymentResponse],
            error_mapper=record_payment_for_multiple_invoices_error_mapper,
            request_options=request_options,
        )

    async def record_payment_for_subscription(
        self,
        subscription_id: int,
        *,
        body: RecordPaymentRequest | RecordPaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RecordPaymentResponse, RecordPaymentForSubscriptionErrorBody]:
        """Records an external payment made against a subscription that will pay partially or in full one or more
        invoices.

        Payment will be applied starting with the oldest open invoice and then next oldest, and so on until the amount
        of the payment is fully consumed.

        Excess payment will result in the creation of a prepayment on the Invoice Account.

        Only ungrouped or primary subscriptions may be paid using the "bulk" payment request.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/payments.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RecordPaymentRequest | RecordPaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[RecordPaymentResponse],
            error_mapper=record_payment_for_subscription_error_mapper,
            request_options=request_options,
        )

    async def refund_invoice(
        self,
        uid: str,
        *,
        body: RefundInvoiceRequest | RefundInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, RefundInvoiceErrorBody]:
        """Refunds an invoice, segment, or consolidated invoice.

        ## Partial Refund for Consolidated Invoice

        A refund less than the total of a consolidated invoice will be split across its segments.

        For a $50.00 refund on a $100.00 consolidated invoice with one $60.00 segment and one $40.00 segment, the
        refunded amount will be applied as 50% of each ($30.00 and $20.00, respectively).

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/refunds.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundInvoiceRequest | RefundInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=refund_invoice_error_mapper,
            request_options=request_options,
        )

    async def reopen_invoice(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, ReopenInvoiceErrorBody]:
        """Reopens any invoice with the "canceled" status. Invoices enter "canceled" status if they were open at the
        time the subscription was canceled (whether through dunning or an intentional cancellation).

        Invoices with "canceled" status are no longer considered to be due. Once reopened, they are considered due for
        payment. Payment may then be captured in one of the following ways:

        - Reactivating the subscription, which will capture all open invoices (See note below about automatic reopening
            of invoices.)
        - Recording a payment directly against the invoice

        A note about reactivations: any canceled invoices from the most recent active period are automatically opened as
        a part of the reactivation process. Reactivating via this endpoint prior to reactivation is only necessary when
        you wish to capture older invoices from previous periods during the reactivation.

        ### Reopening Consolidated Invoices

        When reopening a consolidated invoice, all of its canceled segments will also be reopened.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/reopen.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=reopen_invoice_error_mapper,
            request_options=request_options,
        )

    async def send_invoice(
        self,
        uid: str,
        *,
        body: SendInvoiceRequest | SendInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SendInvoiceErrorBody]:
        """Sends an invoice to the customer via email. This endpoint supports the delivery of both ad-hoc and
        automatically generated invoices. Additionally, this endpoint supports email delivery to direct recipients,
        carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.

        **File Attachments**: You can attach files to invoice emails using ``attachment_urls[]`` parameter by providing
        URLs to the files you want to attach. When using attachments, the request must use ``multipart/form-data``
        content type. Max 10 files, 10MB per file.

        If no recipient email addresses are specified in the request, then the subscription's default email
        configuration will be used. For example, if ``recipient_emails`` is left blank, then the invoice will be
        delivered to the subscription's customer email address.

        On success, a 204 no-content response will be returned. The response does not indicate that email(s) have been
        delivered, but instead indicates that emails have been successfully queued for delivery. If _any_ invalid or
        malformed email address is found in the request body, the entire request will be rejected and a 422 response
        will be returned.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/deliveries.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SendInvoiceRequest | SendInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=send_invoice_error_mapper,
            request_options=request_options,
        )

    async def update_customer_information(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Invoice, UpdateCustomerInformationErrorBody]:
        """Updates customer information on an open invoice and returns the updated invoice. If you would like to preview
        changes that will be applied, use the ``/invoices/{uid}/customer_information/preview.json`` endpoint first.

        The endpoint doesn't accept a request body. Customer information differences are calculated on the application
        side.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/invoices/{uid}/customer_information.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=update_customer_information_error_mapper,
            request_options=request_options,
        )

    async def update_invoice(
        self,
        subscription_id: int,
        uid: str,
        *,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvoiceResponse, UpdateInvoiceErrorBody]:
        """Updates an ad hoc invoice while it is in the ``draft`` state.

        **Important: only invoices with the ``adhoc`` role and ``draft`` status can be updated.** Any other invoice —
        issued, or with a different role (e.g. ``renewal``, ``signup``) — cannot be updated through this endpoint and
        the request returns a ``422`` error. If the invoice does not belong to the provided subscription, a ``404``
        error is returned.

        Only the attributes submitted in the request are changed — omitted attributes keep their current values.

        ### Line Items

        The ``line_items`` array describes changes to the invoice's line items. Line items not referenced in the array
        remain unchanged.

        #### Adding a line item

        A line item without a ``uid`` is added to the invoice. The same line item types and options as on invoice
        creation are supported (custom items, ``product_id``, ``component_id``, price points, period date ranges,
        taxes).

        #### Updating a line item

        A line item with the ``uid`` of an existing line item updates that line item with the submitted attributes.
        Amounts and taxes are recalculated.

        #### Removing a line item

        A line item with a ``uid`` and ``"_destroy": true`` is removed from the invoice. Other line items remain
        unchanged.

        Referencing a ``uid`` which does not exist on the invoice returns a ``422`` error.

        ### Coupons

        When the ``coupons`` key is present, the submitted coupons replace all discounts currently applied to the
        invoice. Send an empty array to remove all discounts. Coupon options are the same as on invoice creation.

        ### Invoice Options

        #### Issue Date and Net Terms

        The ``issue_date`` parameter can be sent to change the invoice's issue date. Only today or dates in the past are
        accepted. The date is interpreted and validated in your site's time zone, using the ``YYYY-MM-DD`` format. The
        ``net_terms`` parameter indicates the number of days after the issue date on which the invoice is due. The due
        date is recalculated whenever the issue date or net terms change.

        #### Addresses

        The seller, shipping and billing addresses can be sent to replace the addresses on the invoice. Each address
        requires to send a ``first_name`` at a minimum in order to work. Taxes are recalculated after an address change.

        #### Memo and Payment Instructions

        A custom memo can be sent with the ``memo`` parameter. Likewise, custom payment instructions can be sent with
        the ``payment_instructions`` parameter.

        Args:
            subscription_id: The Chargify id of the subscription.
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/invoices/{uid}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateInvoiceRequest | UpdateInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[InvoiceResponse],
            error_mapper=update_invoice_error_mapper,
            request_options=request_options,
        )

    async def void_invoice(
        self,
        uid: str,
        *,
        body: VoidInvoiceRequest | VoidInvoiceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Invoice, VoidInvoiceErrorBody]:
        """Voids any invoice with the "open" or "canceled" status. It will also allow voiding of an invoice with the
        "pending" status if it is not a consolidated invoice.

        Args:
            uid: The unique identifier for the invoice, this does not refer to the public facing invoice number.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/invoices/{uid}/void.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoidInvoiceRequest | VoidInvoiceRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Invoice],
            error_mapper=void_invoice_error_mapper,
            request_options=request_options,
        )
