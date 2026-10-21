from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.create_product_family_error import CreateProductFamilyErrorBody, create_product_family_error_mapper
from ..errors.list_products_for_product_family_error import (
    ListProductsForProductFamilyErrorBody,
    list_products_for_product_family_error_mapper,
)
from ..models.create_product_family_request import CreateProductFamilyRequest, CreateProductFamilyRequestDict
from ..models.enums.basic_date_field import BasicDateFieldOrStr
from ..models.enums.list_products_include import ListProductsIncludeOrStr
from ..models.list_products_filter import ListProductsFilter, ListProductsFilterDict
from ..models.product_family_response import ProductFamilyResponse
from ..models.product_response import ProductResponse
from ..server.server import Server


class ProductFamilies:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProductFamiliesWithRawResponse(client, server, auth)

    def create_product_family(
        self,
        *,
        body: CreateProductFamilyRequest | CreateProductFamilyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductFamilyResponse:
        """Creates a Product Family within your site. Create a Product Family to act as a container for your products,
        components, and coupons.

        Full documentation on how Product Families operate within the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261098936205-Product-Families>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_product_family(body=body, request_options=request_options))

    def list_product_families(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProductFamilyResponse]:
        """Lists Product Families for a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_product_families(
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                request_options=request_options,
            ),
        )

    def list_products_for_product_family(
        self,
        product_family_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProductResponse]:
        """Retrieves a list of Products belonging to a Product Family.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            include_archived: Include archived products.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``str | RawError``."""
        return unwrap(
            self._with_raw_response.list_products_for_product_family(
                product_family_id,
                page=page,
                per_page=per_page,
                date_field=date_field,
                filter_=filter_,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                include_archived=include_archived,
                include=include,
                request_options=request_options,
            ),
        )

    def read_product_family(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductFamilyResponse:
        """Retrieves a Product Family via the ``product_family_id``. The response will contain a Product Family object.

        The product family can be specified either with the id number, or with the ``handle:my-family`` format.

        Args:
            id_: The Advanced Billing id of the product family
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_product_family(id_, request_options=request_options))

    @property
    def with_raw_response(self) -> ProductFamiliesWithRawResponse:
        return self._with_raw_response


class AsyncProductFamilies:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductFamiliesWithRawResponse(client, server, auth)

    async def create_product_family(
        self,
        *,
        body: CreateProductFamilyRequest | CreateProductFamilyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductFamilyResponse:
        """Creates a Product Family within your site. Create a Product Family to act as a container for your products,
        components, and coupons.

        Full documentation on how Product Families operate within the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261098936205-Product-Families>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_product_family(body=body, request_options=request_options))

    async def list_product_families(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProductFamilyResponse]:
        """Lists Product Families for a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_product_families(
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                request_options=request_options,
            ),
        )

    async def list_products_for_product_family(
        self,
        product_family_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProductResponse]:
        """Retrieves a list of Products belonging to a Product Family.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            include_archived: Include archived products.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``str | RawError``."""
        return unwrap(
            await self._with_raw_response.list_products_for_product_family(
                product_family_id,
                page=page,
                per_page=per_page,
                date_field=date_field,
                filter_=filter_,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                include_archived=include_archived,
                include=include,
                request_options=request_options,
            ),
        )

    async def read_product_family(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductFamilyResponse:
        """Retrieves a Product Family via the ``product_family_id``. The response will contain a Product Family object.

        The product family can be specified either with the id number, or with the ``handle:my-family`` format.

        Args:
            id_: The Advanced Billing id of the product family
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_product_family(id_, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncProductFamiliesWithRawResponse:
        return self._with_raw_response


class ProductFamiliesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_product_family(
        self,
        *,
        body: CreateProductFamilyRequest | CreateProductFamilyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductFamilyResponse, CreateProductFamilyErrorBody]:
        """Creates a Product Family within your site. Create a Product Family to act as a container for your products,
        components, and coupons.

        Full documentation on how Product Families operate within the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261098936205-Product-Families>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProductFamilyRequest | CreateProductFamilyRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductFamilyResponse],
            error_mapper=create_product_family_error_mapper,
            request_options=request_options,
        )

    def list_product_families(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProductFamilyResponse], RawError]:
        """Lists Product Families for a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families.json"),
            query_params=[
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ProductFamilyResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_products_for_product_family(
        self,
        product_family_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProductResponse], ListProductsForProductFamilyErrorBody]:
        """Retrieves a list of Products belonging to a Product Family.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            include_archived: Include archived products.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/products.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[ListProductsFilter | ListProductsFilterDict | None]("filter", filter_),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[bool | None]("include_archived", include_archived),
                param[ListProductsIncludeOrStr | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ProductResponse]],
            error_mapper=list_products_for_product_family_error_mapper,
            request_options=request_options,
        )

    def read_product_family(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductFamilyResponse, RawError]:
        """Retrieves a Product Family via the ``product_family_id``. The response will contain a Product Family object.

        The product family can be specified either with the id number, or with the ``handle:my-family`` format.

        Args:
            id_: The Advanced Billing id of the product family
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductFamilyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProductFamiliesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_product_family(
        self,
        *,
        body: CreateProductFamilyRequest | CreateProductFamilyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductFamilyResponse, CreateProductFamilyErrorBody]:
        """Creates a Product Family within your site. Create a Product Family to act as a container for your products,
        components, and coupons.

        Full documentation on how Product Families operate within the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261098936205-Product-Families>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProductFamilyRequest | CreateProductFamilyRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductFamilyResponse],
            error_mapper=create_product_family_error_mapper,
            request_options=request_options,
        )

    async def list_product_families(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProductFamilyResponse], RawError]:
        """Lists Product Families for a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families.json"),
            query_params=[
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ProductFamilyResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_products_for_product_family(
        self,
        product_family_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProductResponse], ListProductsForProductFamilyErrorBody]:
        """Retrieves a list of Products belonging to a Product Family.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            include_archived: Include archived products.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/products.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[ListProductsFilter | ListProductsFilterDict | None]("filter", filter_),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[bool | None]("include_archived", include_archived),
                param[ListProductsIncludeOrStr | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ProductResponse]],
            error_mapper=list_products_for_product_family_error_mapper,
            request_options=request_options,
        )

    async def read_product_family(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductFamilyResponse, RawError]:
        """Retrieves a Product Family via the ``product_family_id``. The response will contain a Product Family object.

        The product family can be specified either with the id number, or with the ``handle:my-family`` format.

        Args:
            id_: The Advanced Billing id of the product family
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductFamilyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
