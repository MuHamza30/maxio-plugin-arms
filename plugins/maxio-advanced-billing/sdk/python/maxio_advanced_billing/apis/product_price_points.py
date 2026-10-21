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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.archive_product_price_point_error import (
    ArchiveProductPricePointErrorBody,
    archive_product_price_point_error_mapper,
)
from ..errors.bulk_create_product_price_points_error import (
    BulkCreateProductPricePointsErrorBody,
    bulk_create_product_price_points_error_mapper,
)
from ..errors.create_product_currency_prices_error import (
    CreateProductCurrencyPricesErrorBody,
    create_product_currency_prices_error_mapper,
)
from ..errors.create_product_price_point_error import (
    CreateProductPricePointErrorBody,
    create_product_price_point_error_mapper,
)
from ..errors.list_all_product_price_points_error import (
    ListAllProductPricePointsErrorBody,
    list_all_product_price_points_error_mapper,
)
from ..errors.update_product_currency_prices_error import (
    UpdateProductCurrencyPricesErrorBody,
    update_product_currency_prices_error_mapper,
)
from ..models.bulk_create_product_price_points_request import (
    BulkCreateProductPricePointsRequest,
    BulkCreateProductPricePointsRequestDict,
)
from ..models.bulk_create_product_price_points_response import BulkCreateProductPricePointsResponse
from ..models.create_product_currency_prices_request import (
    CreateProductCurrencyPricesRequest,
    CreateProductCurrencyPricesRequestDict,
)
from ..models.create_product_price_point_request import (
    CreateProductPricePointRequest,
    CreateProductPricePointRequestDict,
)
from ..models.currency_prices_response import CurrencyPricesResponse
from ..models.enums.list_products_price_points_include import ListProductsPricePointsIncludeOrStr
from ..models.enums.price_point_type import PricePointTypeOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.list_price_points_filter import ListPricePointsFilter, ListPricePointsFilterDict
from ..models.list_product_price_points_response import ListProductPricePointsResponse
from ..models.product_price_point_response import ProductPricePointResponse
from ..models.product_response import ProductResponse
from ..models.unions.price_point_id_model import PricePointIdModel, PricePointIdModelDict
from ..models.unions.product_id_model import ProductIdModel, ProductIdModelDict
from ..models.update_currency_prices_request import UpdateCurrencyPricesRequest, UpdateCurrencyPricesRequestDict
from ..models.update_product_price_point_request import (
    UpdateProductPricePointRequest,
    UpdateProductPricePointRequestDict,
)
from ..server.server import Server


class ProductPricePoints:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProductPricePointsWithRawResponse(client, server, auth)

    def archive_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Archives a product price point.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.archive_product_price_point(
                product_id, price_point_id, request_options=request_options
            ),
        )

    def bulk_create_product_price_points(
        self,
        product_id: int,
        *,
        body: BulkCreateProductPricePointsRequest | BulkCreateProductPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateProductPricePointsResponse:
        """Creates multiple product price points in one request.

        Args:
            product_id: The Advanced Billing id of the product to which the price points belong
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``dict[str, Any] | RawError``."""
        return unwrap(
            self._with_raw_response.bulk_create_product_price_points(
                product_id, body=body, request_options=request_options
            ),
        )

    def create_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: CreateProductCurrencyPricesRequest | CreateProductCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrencyPricesResponse:
        """Creates currency prices for a given currency that has been defined on the site level in your settings.

        When creating currency prices, they need to mirror the structure of your primary pricing. If the product price
        point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices are not able to be created for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_product_currency_prices(
                product_price_point_id, body=body, request_options=request_options
            ),
        )

    def create_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        body: CreateProductPricePointRequest | CreateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Creates a Product Price Point. See the `Product Price Point
        <https://maxio.zendesk.com/hc/en-us/articles/24261111947789-Product-Price-Points>`__ documentation for details.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ProductPricePointErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_product_price_point(product_id, body=body, request_options=request_options)
        )

    def list_all_product_price_points(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        include: ListProductsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProductPricePointsResponse:
        """Lists Product Price Points belonging to a site.

        Args:
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_all_product_price_points(
                direction=direction,
                filter_=filter_,
                include=include,
                page=page,
                per_page=per_page,
                request_options=request_options,
            ),
        )

    def list_product_price_points(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        page: int | None = 1,
        per_page: int | None = 10,
        currency_prices: bool | None = None,
        filter_type: list[PricePointTypeOrStr] | None = None,
        archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProductPricePointsResponse:
        """Retrieves a list of product price points.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            archived: Set to include archived price points in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_product_price_points(
                product_id,
                page=page,
                per_page=per_page,
                currency_prices=currency_prices,
                filter_type=filter_type,
                archived=archived,
                request_options=request_options,
            ),
        )

    def promote_product_price_point_to_default(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductResponse:
        """Sets a product price point as the default for the product.

        Note: Custom product price points cannot be set as the default for a product.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.promote_product_price_point_to_default(
                product_id, price_point_id, request_options=request_options
            ),
        )

    def read_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Returns details for a specific product price point. You can achieve this by using either the product price
        point ID or handle.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_product_price_point(
                product_id, price_point_id, currency_prices=currency_prices, request_options=request_options
            ),
        )

    def unarchive_product_price_point(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductPricePointResponse:
        """Unarchives an archived product price point.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.unarchive_product_price_point(
                product_id, price_point_id, request_options=request_options
            ),
        )

    def update_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrencyPricesResponse:
        """Updates the ``price``s of currency prices for a given currency that exists on the product price point.

        When updating the pricing, it needs to mirror the structure of your primary pricing. If the product price point
        defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices cannot be updated for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_product_currency_prices(
                product_price_point_id, body=body, request_options=request_options
            ),
        )

    def update_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateProductPricePointRequest | UpdateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Updates a product price point.

        Note: Custom product price points cannot be updated.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_product_price_point(
                product_id, price_point_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ProductPricePointsWithRawResponse:
        return self._with_raw_response


class AsyncProductPricePoints:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductPricePointsWithRawResponse(client, server, auth)

    async def archive_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Archives a product price point.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.archive_product_price_point(
                product_id, price_point_id, request_options=request_options
            ),
        )

    async def bulk_create_product_price_points(
        self,
        product_id: int,
        *,
        body: BulkCreateProductPricePointsRequest | BulkCreateProductPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateProductPricePointsResponse:
        """Creates multiple product price points in one request.

        Args:
            product_id: The Advanced Billing id of the product to which the price points belong
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``dict[str, Any] | RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_create_product_price_points(
                product_id, body=body, request_options=request_options
            ),
        )

    async def create_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: CreateProductCurrencyPricesRequest | CreateProductCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrencyPricesResponse:
        """Creates currency prices for a given currency that has been defined on the site level in your settings.

        When creating currency prices, they need to mirror the structure of your primary pricing. If the product price
        point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices are not able to be created for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_product_currency_prices(
                product_price_point_id, body=body, request_options=request_options
            ),
        )

    async def create_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        body: CreateProductPricePointRequest | CreateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Creates a Product Price Point. See the `Product Price Point
        <https://maxio.zendesk.com/hc/en-us/articles/24261111947789-Product-Price-Points>`__ documentation for details.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ProductPricePointErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_product_price_point(
                product_id, body=body, request_options=request_options
            ),
        )

    async def list_all_product_price_points(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        include: ListProductsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProductPricePointsResponse:
        """Lists Product Price Points belonging to a site.

        Args:
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_all_product_price_points(
                direction=direction,
                filter_=filter_,
                include=include,
                page=page,
                per_page=per_page,
                request_options=request_options,
            ),
        )

    async def list_product_price_points(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        page: int | None = 1,
        per_page: int | None = 10,
        currency_prices: bool | None = None,
        filter_type: list[PricePointTypeOrStr] | None = None,
        archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProductPricePointsResponse:
        """Retrieves a list of product price points.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            archived: Set to include archived price points in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_product_price_points(
                product_id,
                page=page,
                per_page=per_page,
                currency_prices=currency_prices,
                filter_type=filter_type,
                archived=archived,
                request_options=request_options,
            ),
        )

    async def promote_product_price_point_to_default(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductResponse:
        """Sets a product price point as the default for the product.

        Note: Custom product price points cannot be set as the default for a product.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.promote_product_price_point_to_default(
                product_id, price_point_id, request_options=request_options
            ),
        )

    async def read_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Returns details for a specific product price point. You can achieve this by using either the product price
        point ID or handle.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_product_price_point(
                product_id, price_point_id, currency_prices=currency_prices, request_options=request_options
            ),
        )

    async def unarchive_product_price_point(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductPricePointResponse:
        """Unarchives an archived product price point.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.unarchive_product_price_point(
                product_id, price_point_id, request_options=request_options
            ),
        )

    async def update_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CurrencyPricesResponse:
        """Updates the ``price``s of currency prices for a given currency that exists on the product price point.

        When updating the pricing, it needs to mirror the structure of your primary pricing. If the product price point
        defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices cannot be updated for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_product_currency_prices(
                product_price_point_id, body=body, request_options=request_options
            ),
        )

    async def update_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateProductPricePointRequest | UpdateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductPricePointResponse:
        """Updates a product price point.

        Note: Custom product price points cannot be updated.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_product_price_point(
                product_id, price_point_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncProductPricePointsWithRawResponse:
        return self._with_raw_response


class ProductPricePointsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, ArchiveProductPricePointErrorBody]:
        """Archives a product price point.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ProductIdModel | ProductIdModelDict]("product_id", product_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductPricePointResponse],
            error_mapper=archive_product_price_point_error_mapper,
            request_options=request_options,
        )

    def bulk_create_product_price_points(
        self,
        product_id: int,
        *,
        body: BulkCreateProductPricePointsRequest | BulkCreateProductPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateProductPricePointsResponse, BulkCreateProductPricePointsErrorBody]:
        """Creates multiple product price points in one request.

        Args:
            product_id: The Advanced Billing id of the product to which the price points belong
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/price_points/bulk.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateProductPricePointsRequest | BulkCreateProductPricePointsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BulkCreateProductPricePointsResponse],
            error_mapper=bulk_create_product_price_points_error_mapper,
            request_options=request_options,
        )

    def create_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: CreateProductCurrencyPricesRequest | CreateProductCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrencyPricesResponse, CreateProductCurrencyPricesErrorBody]:
        """Creates currency prices for a given currency that has been defined on the site level in your settings.

        When creating currency prices, they need to mirror the structure of your primary pricing. If the product price
        point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices are not able to be created for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_price_points/{product_price_point_id}/currency_prices.json"),
            path_params=[param[int]("product_price_point_id", product_price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProductCurrencyPricesRequest | CreateProductCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CurrencyPricesResponse],
            error_mapper=create_product_currency_prices_error_mapper,
            request_options=request_options,
        )

    def create_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        body: CreateProductPricePointRequest | CreateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, CreateProductPricePointErrorBody]:
        """Creates a Product Price Point. See the `Product Price Point
        <https://maxio.zendesk.com/hc/en-us/articles/24261111947789-Product-Price-Points>`__ documentation for details.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/price_points.json"),
            path_params=[param[ProductIdModel | ProductIdModelDict]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProductPricePointRequest | CreateProductPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductPricePointResponse],
            error_mapper=create_product_price_point_error_mapper,
            request_options=request_options,
        )

    def list_all_product_price_points(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        include: ListProductsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProductPricePointsResponse, ListAllProductPricePointsErrorBody]:
        """Lists Product Price Points belonging to a site.

        Args:
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products_price_points.json"),
            query_params=[
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListPricePointsFilter | ListPricePointsFilterDict | None]("filter", filter_),
                param[ListProductsPricePointsIncludeOrStr | None]("include", include),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListProductPricePointsResponse],
            error_mapper=list_all_product_price_points_error_mapper,
            request_options=request_options,
        )

    def list_product_price_points(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        page: int | None = 1,
        per_page: int | None = 10,
        currency_prices: bool | None = None,
        filter_type: list[PricePointTypeOrStr] | None = None,
        archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProductPricePointsResponse, RawError]:
        """Retrieves a list of product price points.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            archived: Set to include archived price points in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/price_points.json"),
            path_params=[param[ProductIdModel | ProductIdModelDict]("product_id", product_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("currency_prices", currency_prices),
                param[list[PricePointTypeOrStr] | None]("filter[type]", filter_type),
                param[bool | None]("archived", archived),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListProductPricePointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def promote_product_price_point_to_default(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductResponse, RawError]:
        """Sets a product price point as the default for the product.

        Note: Custom product price points cannot be set as the default for a product.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}/default.json"),
            path_params=[param[int]("product_id", product_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, RawError]:
        """Returns details for a specific product price point. You can achieve this by using either the product price
        point ID or handle.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ProductIdModel | ProductIdModelDict]("product_id", product_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            query_params=[param[bool | None]("currency_prices", currency_prices)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unarchive_product_price_point(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductPricePointResponse, RawError]:
        """Unarchives an archived product price point.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}/unarchive.json"),
            path_params=[param[int]("product_id", product_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrencyPricesResponse, UpdateProductCurrencyPricesErrorBody]:
        """Updates the ``price``s of currency prices for a given currency that exists on the product price point.

        When updating the pricing, it needs to mirror the structure of your primary pricing. If the product price point
        defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices cannot be updated for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/product_price_points/{product_price_point_id}/currency_prices.json"),
            path_params=[param[int]("product_price_point_id", product_price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CurrencyPricesResponse],
            error_mapper=update_product_currency_prices_error_mapper,
            request_options=request_options,
        )

    def update_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateProductPricePointRequest | UpdateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, RawError]:
        """Updates a product price point.

        Note: Custom product price points cannot be updated.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ProductIdModel | ProductIdModelDict]("product_id", product_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateProductPricePointRequest | UpdateProductPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ProductPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProductPricePointsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, ArchiveProductPricePointErrorBody]:
        """Archives a product price point.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ProductIdModel | ProductIdModelDict]("product_id", product_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductPricePointResponse],
            error_mapper=archive_product_price_point_error_mapper,
            request_options=request_options,
        )

    async def bulk_create_product_price_points(
        self,
        product_id: int,
        *,
        body: BulkCreateProductPricePointsRequest | BulkCreateProductPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateProductPricePointsResponse, BulkCreateProductPricePointsErrorBody]:
        """Creates multiple product price points in one request.

        Args:
            product_id: The Advanced Billing id of the product to which the price points belong
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/price_points/bulk.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateProductPricePointsRequest | BulkCreateProductPricePointsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BulkCreateProductPricePointsResponse],
            error_mapper=bulk_create_product_price_points_error_mapper,
            request_options=request_options,
        )

    async def create_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: CreateProductCurrencyPricesRequest | CreateProductCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrencyPricesResponse, CreateProductCurrencyPricesErrorBody]:
        """Creates currency prices for a given currency that has been defined on the site level in your settings.

        When creating currency prices, they need to mirror the structure of your primary pricing. If the product price
        point defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices are not able to be created for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_price_points/{product_price_point_id}/currency_prices.json"),
            path_params=[param[int]("product_price_point_id", product_price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProductCurrencyPricesRequest | CreateProductCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CurrencyPricesResponse],
            error_mapper=create_product_currency_prices_error_mapper,
            request_options=request_options,
        )

    async def create_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        body: CreateProductPricePointRequest | CreateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, CreateProductPricePointErrorBody]:
        """Creates a Product Price Point. See the `Product Price Point
        <https://maxio.zendesk.com/hc/en-us/articles/24261111947789-Product-Price-Points>`__ documentation for details.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/price_points.json"),
            path_params=[param[ProductIdModel | ProductIdModelDict]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProductPricePointRequest | CreateProductPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductPricePointResponse],
            error_mapper=create_product_price_point_error_mapper,
            request_options=request_options,
        )

    async def list_all_product_price_points(
        self,
        *,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        include: ListProductsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProductPricePointsResponse, ListAllProductPricePointsErrorBody]:
        """Lists Product Price Points belonging to a site.

        Args:
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products_price_points.json"),
            query_params=[
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListPricePointsFilter | ListPricePointsFilterDict | None]("filter", filter_),
                param[ListProductsPricePointsIncludeOrStr | None]("include", include),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListProductPricePointsResponse],
            error_mapper=list_all_product_price_points_error_mapper,
            request_options=request_options,
        )

    async def list_product_price_points(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        *,
        page: int | None = 1,
        per_page: int | None = 10,
        currency_prices: bool | None = None,
        filter_type: list[PricePointTypeOrStr] | None = None,
        archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProductPricePointsResponse, RawError]:
        """Retrieves a list of product price points.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            archived: Set to include archived price points in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/price_points.json"),
            path_params=[param[ProductIdModel | ProductIdModelDict]("product_id", product_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("currency_prices", currency_prices),
                param[list[PricePointTypeOrStr] | None]("filter[type]", filter_type),
                param[bool | None]("archived", archived),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListProductPricePointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def promote_product_price_point_to_default(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductResponse, RawError]:
        """Sets a product price point as the default for the product.

        Note: Custom product price points cannot be set as the default for a product.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}/default.json"),
            path_params=[param[int]("product_id", product_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, RawError]:
        """Returns details for a specific product price point. You can achieve this by using either the product price
        point ID or handle.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ?currency_prices=true to include an array of currency price data in the response. If the product price
                point is set to use_site_exchange_rate: true, it will return pricing based on the current exchange rate.
                If the flag is set to false, it will return all of the defined prices for each currency.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ProductIdModel | ProductIdModelDict]("product_id", product_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            query_params=[param[bool | None]("currency_prices", currency_prices)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unarchive_product_price_point(
        self, product_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductPricePointResponse, RawError]:
        """Unarchives an archived product price point.

        Args:
            product_id: The Advanced Billing id of the product to which the price point belongs
            price_point_id: The Advanced Billing id of the product price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}/unarchive.json"),
            path_params=[param[int]("product_id", product_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_product_currency_prices(
        self,
        product_price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CurrencyPricesResponse, UpdateProductCurrencyPricesErrorBody]:
        """Updates the ``price``s of currency prices for a given currency that exists on the product price point.

        When updating the pricing, it needs to mirror the structure of your primary pricing. If the product price point
        defines a trial and/or setup fee, each currency must also define a trial and/or setup fee.

        Note: Currency Prices cannot be updated for custom product price points.

        Args:
            product_price_point_id: The Advanced Billing id of the product price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/product_price_points/{product_price_point_id}/currency_prices.json"),
            path_params=[param[int]("product_price_point_id", product_price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CurrencyPricesResponse],
            error_mapper=update_product_currency_prices_error_mapper,
            request_options=request_options,
        )

    async def update_product_price_point(
        self,
        product_id: ProductIdModel | ProductIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateProductPricePointRequest | UpdateProductPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductPricePointResponse, RawError]:
        """Updates a product price point.

        Note: Custom product price points cannot be updated.

        Args:
            product_id: The id or handle of the product. When using the handle, it must be prefixed with ``handle:``.
                Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-price-point-handle`` for a
                string handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/products/{product_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ProductIdModel | ProductIdModelDict]("product_id", product_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateProductPricePointRequest | UpdateProductPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ProductPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
