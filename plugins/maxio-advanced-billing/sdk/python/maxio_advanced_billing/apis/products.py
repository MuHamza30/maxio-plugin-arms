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
from ..errors.archive_product_error import ArchiveProductErrorBody, archive_product_error_mapper
from ..errors.create_product_error import CreateProductErrorBody, create_product_error_mapper
from ..errors.update_product_error import UpdateProductErrorBody, update_product_error_mapper
from ..models.create_or_update_product_request import CreateOrUpdateProductRequest, CreateOrUpdateProductRequestDict
from ..models.enums.basic_date_field import BasicDateFieldOrStr
from ..models.enums.list_products_include import ListProductsIncludeOrStr
from ..models.list_products_filter import ListProductsFilter, ListProductsFilterDict
from ..models.product_response import ProductResponse
from ..server.server import Server


class Products:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProductsWithRawResponse(client, server, auth)

    def archive_product(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductResponse:
        """Archives the product. All current subscribers will be unaffected; their subscription/purchase will continue
        to be charged monthly.

        This will restrict the option to chose the product for purchase via the Billing Portal, as well as disable
        Public Signup Pages for the product.

        Args:
            product_id: The Advanced Billing id of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.archive_product(product_id, request_options=request_options))

    def create_product(
        self,
        product_family_id: str,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductResponse:
        """Creates a product in your site.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, the
        ``auto_create_signup_page`` parameter is not supported. If ``auto_create_signup_page`` is included (with any
        value) an error is returned.

        For more information, see:

        + `Products Overview <https://maxio.zendesk.com/hc/en-us/articles/24261090117645-Products-Overview>`__
        + `Changing a Subscription's Product
            <https://maxio.zendesk.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_product(product_family_id, body=body, request_options=request_options)
        )

    def list_products(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        end_date: Date | None = None,
        end_datetime: RFC3339DateTime | None = None,
        start_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProductResponse]:
        """Lists products belonging to a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of start_date.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_products(
                date_field=date_field,
                filter_=filter_,
                end_date=end_date,
                end_datetime=end_datetime,
                start_date=start_date,
                start_datetime=start_datetime,
                page=page,
                per_page=per_page,
                include_archived=include_archived,
                include=include,
                include_features=include_features,
                request_options=request_options,
            ),
        )

    def read_product(
        self,
        product_id: int,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductResponse:
        """Reads the current details of a product.

        Args:
            product_id: The Advanced Billing id of the product
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_product(
                product_id, include_features=include_features, request_options=request_options
            ),
        )

    def read_product_by_handle(
        self, api_handle: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductResponse:
        """Retrieves a Product object by its ``api_handle``.

        Args:
            api_handle: The handle of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_product_by_handle(api_handle, request_options=request_options))

    def update_product(
        self,
        product_id: int,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductResponse:
        """Updates aspects of an existing product.

        ### Input Attributes Update Notes

        + ``update_return_params`` The parameters we will append to your ``update_return_url``. See Return URLs and
            Parameters

        ### Product Price Point

        Updating a product using this endpoint will create a new price point and set it as the default price point for
        this product. If you should like to update an existing product price point, that must be done separately.

        Args:
            product_id: The Advanced Billing id of the product
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.update_product(product_id, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> ProductsWithRawResponse:
        return self._with_raw_response


class AsyncProducts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductsWithRawResponse(client, server, auth)

    async def archive_product(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductResponse:
        """Archives the product. All current subscribers will be unaffected; their subscription/purchase will continue
        to be charged monthly.

        This will restrict the option to chose the product for purchase via the Billing Portal, as well as disable
        Public Signup Pages for the product.

        Args:
            product_id: The Advanced Billing id of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.archive_product(product_id, request_options=request_options))

    async def create_product(
        self,
        product_family_id: str,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductResponse:
        """Creates a product in your site.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, the
        ``auto_create_signup_page`` parameter is not supported. If ``auto_create_signup_page`` is included (with any
        value) an error is returned.

        For more information, see:

        + `Products Overview <https://maxio.zendesk.com/hc/en-us/articles/24261090117645-Products-Overview>`__
        + `Changing a Subscription's Product
            <https://maxio.zendesk.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_product(product_family_id, body=body, request_options=request_options)
        )

    async def list_products(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        end_date: Date | None = None,
        end_datetime: RFC3339DateTime | None = None,
        start_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ProductResponse]:
        """Lists products belonging to a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of start_date.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_products(
                date_field=date_field,
                filter_=filter_,
                end_date=end_date,
                end_datetime=end_datetime,
                start_date=start_date,
                start_datetime=start_datetime,
                page=page,
                per_page=per_page,
                include_archived=include_archived,
                include=include,
                include_features=include_features,
                request_options=request_options,
            ),
        )

    async def read_product(
        self,
        product_id: int,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductResponse:
        """Reads the current details of a product.

        Args:
            product_id: The Advanced Billing id of the product
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_product(
                product_id, include_features=include_features, request_options=request_options
            ),
        )

    async def read_product_by_handle(
        self, api_handle: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductResponse:
        """Retrieves a Product object by its ``api_handle``.

        Args:
            api_handle: The handle of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_product_by_handle(api_handle, request_options=request_options))

    async def update_product(
        self,
        product_id: int,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductResponse:
        """Updates aspects of an existing product.

        ### Input Attributes Update Notes

        + ``update_return_params`` The parameters we will append to your ``update_return_url``. See Return URLs and
            Parameters

        ### Product Price Point

        Updating a product using this endpoint will create a new price point and set it as the default price point for
        this product. If you should like to update an existing product price point, that must be done separately.

        Args:
            product_id: The Advanced Billing id of the product
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_product(product_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncProductsWithRawResponse:
        return self._with_raw_response


class ProductsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_product(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductResponse, ArchiveProductErrorBody]:
        """Archives the product. All current subscribers will be unaffected; their subscription/purchase will continue
        to be charged monthly.

        This will restrict the option to chose the product for purchase via the Billing Portal, as well as disable
        Public Signup Pages for the product.

        Args:
            product_id: The Advanced Billing id of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/products/{product_id}.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductResponse],
            error_mapper=archive_product_error_mapper,
            request_options=request_options,
        )

    def create_product(
        self,
        product_family_id: str,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductResponse, CreateProductErrorBody]:
        """Creates a product in your site.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, the
        ``auto_create_signup_page`` parameter is not supported. If ``auto_create_signup_page`` is included (with any
        value) an error is returned.

        For more information, see:

        + `Products Overview <https://maxio.zendesk.com/hc/en-us/articles/24261090117645-Products-Overview>`__
        + `Changing a Subscription's Product
            <https://maxio.zendesk.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/products.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductResponse],
            error_mapper=create_product_error_mapper,
            request_options=request_options,
        )

    def list_products(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        end_date: Date | None = None,
        end_datetime: RFC3339DateTime | None = None,
        start_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProductResponse], RawError]:
        """Lists products belonging to a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of start_date.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products.json"),
            query_params=[
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[ListProductsFilter | ListProductsFilterDict | None]("filter", filter_),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[Date | None]("start_date", start_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("include_archived", include_archived),
                param[ListProductsIncludeOrStr | None]("include", include),
                param[bool | None]("include_features", include_features),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ProductResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_product(
        self,
        product_id: int,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductResponse, RawError]:
        """Reads the current details of a product.

        Args:
            product_id: The Advanced Billing id of the product
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}.json"),
            path_params=[param[int]("product_id", product_id)],
            query_params=[param[bool | None]("include_features", include_features)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_product_by_handle(
        self, api_handle: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductResponse, RawError]:
        """Retrieves a Product object by its ``api_handle``.

        Args:
            api_handle: The handle of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/handle/{api_handle}.json"),
            path_params=[param[str]("api_handle", api_handle)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_product(
        self,
        product_id: int,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductResponse, UpdateProductErrorBody]:
        """Updates aspects of an existing product.

        ### Input Attributes Update Notes

        + ``update_return_params`` The parameters we will append to your ``update_return_url``. See Return URLs and
            Parameters

        ### Product Price Point

        Updating a product using this endpoint will create a new price point and set it as the default price point for
        this product. If you should like to update an existing product price point, that must be done separately.

        Args:
            product_id: The Advanced Billing id of the product
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/products/{product_id}.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductResponse],
            error_mapper=update_product_error_mapper,
            request_options=request_options,
        )


class AsyncProductsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_product(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductResponse, ArchiveProductErrorBody]:
        """Archives the product. All current subscribers will be unaffected; their subscription/purchase will continue
        to be charged monthly.

        This will restrict the option to chose the product for purchase via the Billing Portal, as well as disable
        Public Signup Pages for the product.

        Args:
            product_id: The Advanced Billing id of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/products/{product_id}.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductResponse],
            error_mapper=archive_product_error_mapper,
            request_options=request_options,
        )

    async def create_product(
        self,
        product_family_id: str,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductResponse, CreateProductErrorBody]:
        """Creates a product in your site.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, the
        ``auto_create_signup_page`` parameter is not supported. If ``auto_create_signup_page`` is included (with any
        value) an error is returned.

        For more information, see:

        + `Products Overview <https://maxio.zendesk.com/hc/en-us/articles/24261090117645-Products-Overview>`__
        + `Changing a Subscription's Product
            <https://maxio.zendesk.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/products.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductResponse],
            error_mapper=create_product_error_mapper,
            request_options=request_options,
        )

    async def list_products(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        filter_: ListProductsFilter | ListProductsFilterDict | None = None,
        end_date: Date | None = None,
        end_datetime: RFC3339DateTime | None = None,
        start_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        include: ListProductsIncludeOrStr | None = None,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ProductResponse], RawError]:
        """Lists products belonging to a site.

        Args:
            date_field: The type of filter you would like to apply to your search. Use in query:
                ``date_field=created_at``.
            filter_: Filter to use for List Products operations
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns products with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns products with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site''s time zone will be used. If provided, this parameter will be used instead
                of start_date.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            include: Allows including additional data in the response. Use in query
                ``include=prepaid_product_price_point``.
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products.json"),
            query_params=[
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[ListProductsFilter | ListProductsFilterDict | None]("filter", filter_),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[Date | None]("start_date", start_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("include_archived", include_archived),
                param[ListProductsIncludeOrStr | None]("include", include),
                param[bool | None]("include_features", include_features),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ProductResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_product(
        self,
        product_id: int,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductResponse, RawError]:
        """Reads the current details of a product.

        Args:
            product_id: The Advanced Billing id of the product
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}.json"),
            path_params=[param[int]("product_id", product_id)],
            query_params=[param[bool | None]("include_features", include_features)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_product_by_handle(
        self, api_handle: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductResponse, RawError]:
        """Retrieves a Product object by its ``api_handle``.

        Args:
            api_handle: The handle of the product
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/handle/{api_handle}.json"),
            path_params=[param[str]("api_handle", api_handle)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_product(
        self,
        product_id: int,
        *,
        body: CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductResponse, UpdateProductErrorBody]:
        """Updates aspects of an existing product.

        ### Input Attributes Update Notes

        + ``update_return_params`` The parameters we will append to your ``update_return_url``. See Return URLs and
            Parameters

        ### Product Price Point

        Updating a product using this endpoint will create a new price point and set it as the default price point for
        this product. If you should like to update an existing product price point, that must be done separately.

        Args:
            product_id: The Advanced Billing id of the product
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/products/{product_id}.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateProductRequest | CreateOrUpdateProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductResponse],
            error_mapper=update_product_error_mapper,
            request_options=request_options,
        )
