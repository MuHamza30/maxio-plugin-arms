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
from ..errors.create_customer_error import CreateCustomerErrorBody, create_customer_error_mapper
from ..errors.update_customer_error import UpdateCustomerErrorBody, update_customer_error_mapper
from ..models.create_customer_request import CreateCustomerRequest, CreateCustomerRequestDict
from ..models.customer_response import CustomerResponse
from ..models.enums.basic_date_field import BasicDateFieldOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.subscription_response import SubscriptionResponse
from ..models.update_customer_request import UpdateCustomerRequest, UpdateCustomerRequestDict
from ..server.server import Server


class Customers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomersWithRawResponse(client, server, auth)

    def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you can only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you can choose to leave ``reference`` blank, and store the system-assigned unique ID
        for the customer, which is in the ``id`` attribute.

        For more information, see `Customer Details
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Format the country attribute of the customer using the ISO Standard Country codes.

        Countries should be formatted as two characters. For more information, see `ISO 3166-1
        <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__.

        ## Required State Format

        Format the state attribute of the customer using the ISO Standard State codes.

        + US States (two characters): see `ISO 3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__.

        + States Outside the US (two to three characters): To find the correct state codes outside the US, go to `ISO
            3166-1 <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2
            codes” column next to the country you wish to populate.

        ## Locale

        You can attribute a language/region to the customer to deliver invoices in any required language. For more
        information, see `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        A blank pair is ignored rather than rejected, so a ``vat_number`` sent alongside it still takes effect.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_customer(body=body, request_options=request_options))

    def delete_customer(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes the customer.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_customer(id_, request_options=request_options))

    def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SubscriptionResponse]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.list_customer_subscriptions(customer_id, request_options=request_options))

    def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomerResponse]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_customers(
                direction=direction,
                page=page,
                per_page=per_page,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                q=q,
                request_options=request_options,
            ),
        )

    def read_customer(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_customer(id_, request_options=request_options))

    def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomerResponse:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_customer_by_reference(reference, request_options=request_options))

    def update_customer(
        self,
        id_: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Updates the customer.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time, so
        saving an identifier of a different kind replaces the existing one.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        To clear an identifier, send a supported ``entity_identifier_kind`` with a blank ``entity_identifier_value``, or
        send a blank ``vat_number`` on its own. The first form also clears ``vat_number`` and ``vat_country``, and it
        removes whichever identifier the customer holds, whatever kind you send with it.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        Sending a customer response straight back leaves the tax ID alone. A blank pair, and a pair that still matches
        the stored identifier with ``vat_country`` unchanged, are read as nothing to change rather than as a request to
        clear. For ``gln``, ``duns``, and ``lei`` that also covers the ``vat_number`` the response mirrors back, so the
        kind survives the round trip.

        What you do change is applied, and the entity identifier fields take precedence over ``vat_number``. A different
        kind or value writes that identifier, and ``vat_number`` and ``vat_country`` follow from it. A different
        ``vat_country`` next to an unchanged pair is a real edit, so it is validated and can return ``422``. Changing
        only ``vat_number`` leaves the pair unchanged, so the derivation above decides the kind, which turns a ``gln``,
        ``duns``, or ``lei`` customer into a ``company_reg``. Setting ``vat_number`` to ``null`` or a blank string still
        clears the identifier.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            id_: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.update_customer(id_, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> CustomersWithRawResponse:
        return self._with_raw_response


class AsyncCustomers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomersWithRawResponse(client, server, auth)

    async def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you can only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you can choose to leave ``reference`` blank, and store the system-assigned unique ID
        for the customer, which is in the ``id`` attribute.

        For more information, see `Customer Details
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Format the country attribute of the customer using the ISO Standard Country codes.

        Countries should be formatted as two characters. For more information, see `ISO 3166-1
        <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__.

        ## Required State Format

        Format the state attribute of the customer using the ISO Standard State codes.

        + US States (two characters): see `ISO 3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__.

        + States Outside the US (two to three characters): To find the correct state codes outside the US, go to `ISO
            3166-1 <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2
            codes” column next to the country you wish to populate.

        ## Locale

        You can attribute a language/region to the customer to deliver invoices in any required language. For more
        information, see `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        A blank pair is ignored rather than rejected, so a ``vat_number`` sent alongside it still takes effect.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_customer(body=body, request_options=request_options))

    async def delete_customer(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes the customer.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.delete_customer(id_, request_options=request_options))

    async def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SubscriptionResponse]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_customer_subscriptions(customer_id, request_options=request_options)
        )

    async def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CustomerResponse]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_customers(
                direction=direction,
                page=page,
                per_page=per_page,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                q=q,
                request_options=request_options,
            ),
        )

    async def read_customer(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> CustomerResponse:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_customer(id_, request_options=request_options))

    async def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CustomerResponse:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_customer_by_reference(reference, request_options=request_options)
        )

    async def update_customer(
        self,
        id_: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Updates the customer.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time, so
        saving an identifier of a different kind replaces the existing one.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        To clear an identifier, send a supported ``entity_identifier_kind`` with a blank ``entity_identifier_value``, or
        send a blank ``vat_number`` on its own. The first form also clears ``vat_number`` and ``vat_country``, and it
        removes whichever identifier the customer holds, whatever kind you send with it.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        Sending a customer response straight back leaves the tax ID alone. A blank pair, and a pair that still matches
        the stored identifier with ``vat_country`` unchanged, are read as nothing to change rather than as a request to
        clear. For ``gln``, ``duns``, and ``lei`` that also covers the ``vat_number`` the response mirrors back, so the
        kind survives the round trip.

        What you do change is applied, and the entity identifier fields take precedence over ``vat_number``. A different
        kind or value writes that identifier, and ``vat_number`` and ``vat_country`` follow from it. A different
        ``vat_country`` next to an unchanged pair is a real edit, so it is validated and can return ``422``. Changing
        only ``vat_number`` leaves the pair unchanged, so the derivation above decides the kind, which turns a ``gln``,
        ``duns``, or ``lei`` customer into a ``company_reg``. Setting ``vat_number`` to ``null`` or a blank string still
        clears the identifier.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            id_: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``CustomerErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.update_customer(id_, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncCustomersWithRawResponse:
        return self._with_raw_response


class CustomersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, CreateCustomerErrorBody]:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you can only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you can choose to leave ``reference`` blank, and store the system-assigned unique ID
        for the customer, which is in the ``id`` attribute.

        For more information, see `Customer Details
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Format the country attribute of the customer using the ISO Standard Country codes.

        Countries should be formatted as two characters. For more information, see `ISO 3166-1
        <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__.

        ## Required State Format

        Format the state attribute of the customer using the ISO Standard State codes.

        + US States (two characters): see `ISO 3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__.

        + States Outside the US (two to three characters): To find the correct state codes outside the US, go to `ISO
            3166-1 <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2
            codes” column next to the country you wish to populate.

        ## Locale

        You can attribute a language/region to the customer to deliver invoices in any required language. For more
        information, see `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        A blank pair is ignored rather than rejected, so a ``vat_number`` sent alongside it still takes effect.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/customers.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerRequest | CreateCustomerRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CustomerResponse],
            error_mapper=create_customer_error_mapper,
            request_options=request_options,
        )

    def delete_customer(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes the customer.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SubscriptionResponse], RawError]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{customer_id}/subscriptions.json"),
            path_params=[param[int]("customer_id", customer_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[SubscriptionResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomerResponse], RawError]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers.json"),
            query_params=[
                param[SortingDirectionOrStr | None]("direction", direction),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[str | None]("q", q),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[CustomerResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_customer(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/lookup.json"),
            query_params=[param[str]("reference", reference)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_customer(
        self,
        id_: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, UpdateCustomerErrorBody]:
        """Updates the customer.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time, so
        saving an identifier of a different kind replaces the existing one.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        To clear an identifier, send a supported ``entity_identifier_kind`` with a blank ``entity_identifier_value``, or
        send a blank ``vat_number`` on its own. The first form also clears ``vat_number`` and ``vat_country``, and it
        removes whichever identifier the customer holds, whatever kind you send with it.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        Sending a customer response straight back leaves the tax ID alone. A blank pair, and a pair that still matches
        the stored identifier with ``vat_country`` unchanged, are read as nothing to change rather than as a request to
        clear. For ``gln``, ``duns``, and ``lei`` that also covers the ``vat_number`` the response mirrors back, so the
        kind survives the round trip.

        What you do change is applied, and the entity identifier fields take precedence over ``vat_number``. A different
        kind or value writes that identifier, and ``vat_number`` and ``vat_country`` follow from it. A different
        ``vat_country`` next to an unchanged pair is a real edit, so it is validated and can return ``422``. Changing
        only ``vat_number`` leaves the pair unchanged, so the derivation above decides the kind, which turns a ``gln``,
        ``duns``, or ``lei`` customer into a ``company_reg``. Setting ``vat_number`` to ``null`` or a blank string still
        clears the identifier.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            id_: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerRequest | UpdateCustomerRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CustomerResponse],
            error_mapper=update_customer_error_mapper,
            request_options=request_options,
        )


class AsyncCustomersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_customer(
        self,
        *,
        body: CreateCustomerRequest | CreateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, CreateCustomerErrorBody]:
        """Creates a new customer; can also be created alongside a new subscription. The only validation restriction is
        that you can only create one customer for a given reference value.

        If provided, the ``reference`` value must be unique. It represents a unique identifier for the customer from
        your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared
        information. Alternatively, you can choose to leave ``reference`` blank, and store the system-assigned unique ID
        for the customer, which is in the ``id`` attribute.

        For more information, see `Customer Details
        <https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details>`__.

        ## Required Country Format

        Format the country attribute of the customer using the ISO Standard Country codes.

        Countries should be formatted as two characters. For more information, see `ISO 3166-1
        <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__.

        ## Required State Format

        Format the state attribute of the customer using the ISO Standard State codes.

        + US States (two characters): see `ISO 3166-2 <https://en.wikipedia.org/wiki/ISO_3166-2:US>`__.

        + States Outside the US (two to three characters): To find the correct state codes outside the US, go to `ISO
            3166-1 <http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ and click on the link in the “ISO 3166-2
            codes” column next to the country you wish to populate.

        ## Locale

        You can attribute a language/region to the customer to deliver invoices in any required language. For more
        information, see `Customer Locale
        <https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale>`__.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        A blank pair is ignored rather than rejected, so a ``vat_number`` sent alongside it still takes effect.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/customers.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerRequest | CreateCustomerRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CustomerResponse],
            error_mapper=create_customer_error_mapper,
            request_options=request_options,
        )

    async def delete_customer(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes the customer.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_subscriptions(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SubscriptionResponse], RawError]:
        """Lists all subscriptions that belong to a customer.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, subscriptions no
        longer require an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{customer_id}/subscriptions.json"),
            path_params=[param[int]("customer_id", customer_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[SubscriptionResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customers(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 50,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        q: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CustomerResponse], RawError]:
        """Lists all customers associated with your site, or filters results using the search parameter.

        ## Find Customer

        Use the search feature with the ``q`` query parameter to retrieve an array of customers that matches the search
        query.

        Common use cases are:

        + Search by an email
        + Search by an Advanced Billing ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name

        To retrieve a single, exact match by reference, use the `lookup endpoint
        <https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference>`__.

        Args:
            direction: Direction to sort customers by time of creation
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date.
            q: A search query by which to filter customers (can be an email, an ID, a reference, organization)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers.json"),
            query_params=[
                param[SortingDirectionOrStr | None]("direction", direction),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[str | None]("q", q),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[CustomerResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_customer(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Retrieves the Customer properties by Advanced Billing-generated Customer ID.

        Args:
            id_: The Advanced Billing id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_customer_by_reference(
        self, reference: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CustomerResponse, RawError]:
        """Returns a customer by their unique reference ID. It will return a single match.

        Args:
            reference: Customer reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/customers/lookup.json"),
            query_params=[param[str]("reference", reference)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_customer(
        self,
        id_: int,
        *,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, UpdateCustomerErrorBody]:
        """Updates the customer.

        ## Tax and Business Identifiers

        Send ``entity_identifier_kind`` and ``entity_identifier_value`` together to store the customer's tax or business
        identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer holds one identifier at a time, so
        saving an identifier of a different kind replaces the existing one.

        The ``vat_eu`` and ``national_tax`` kinds also require ``vat_country``. An unsupported kind, a missing or
        mismatched ``vat_country``, or a ``gln``, ``duns``, or ``lei`` value in the wrong format returns ``422``.

        Always send the kind. ``entity_identifier_value`` on its own is stored as a ``company_reg`` when no
        ``vat_country`` is present, and returns ``422`` naming ``entity_identifier_kind`` when one is.

        To clear an identifier, send a supported ``entity_identifier_kind`` with a blank ``entity_identifier_value``, or
        send a blank ``vat_number`` on its own. The first form also clears ``vat_number`` and ``vat_country``, and it
        removes whichever identifier the customer holds, whatever kind you send with it.

        The legacy ``vat_number`` and ``vat_country`` pair still works on its own. When neither entity identifier field
        is sent, Advanced Billing derives the kind from ``vat_country``: an EU member state code or ``GB`` gives
        ``vat_eu``, one of the national tax country codes gives ``national_tax``, and a blank or unrecognized country
        gives ``company_reg``.

        Sending a customer response straight back leaves the tax ID alone. A blank pair, and a pair that still matches
        the stored identifier with ``vat_country`` unchanged, are read as nothing to change rather than as a request to
        clear. For ``gln``, ``duns``, and ``lei`` that also covers the ``vat_number`` the response mirrors back, so the
        kind survives the round trip.

        What you do change is applied, and the entity identifier fields take precedence over ``vat_number``. A different
        kind or value writes that identifier, and ``vat_number`` and ``vat_country`` follow from it. A different
        ``vat_country`` next to an unchanged pair is a real edit, so it is validated and can return ``422``. Changing
        only ``vat_number`` leaves the pair unchanged, so the derivation above decides the kind, which turns a ``gln``,
        ``duns``, or ``lei`` customer into a ``company_reg``. Setting ``vat_number`` to ``null`` or a blank string still
        clears the identifier.

        The response reports the stored identifier in ``entity_identifier_kind`` and ``entity_identifier_value``, and
        repeats its value in ``vat_number``.

        Args:
            id_: The Advanced Billing id of the customer
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/customers/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerRequest | UpdateCustomerRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CustomerResponse],
            error_mapper=update_customer_error_mapper,
            request_options=request_options,
        )
