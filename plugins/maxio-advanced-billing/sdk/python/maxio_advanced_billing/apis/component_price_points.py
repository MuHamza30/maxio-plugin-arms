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
from ..errors.archive_component_price_point_error import (
    ArchiveComponentPricePointErrorBody,
    archive_component_price_point_error_mapper,
)
from ..errors.bulk_create_component_price_points_error import (
    BulkCreateComponentPricePointsErrorBody,
    bulk_create_component_price_points_error_mapper,
)
from ..errors.clone_component_price_point_error import (
    CloneComponentPricePointErrorBody,
    clone_component_price_point_error_mapper,
)
from ..errors.create_component_price_point_error import (
    CreateComponentPricePointErrorBody,
    create_component_price_point_error_mapper,
)
from ..errors.create_currency_prices_error import CreateCurrencyPricesErrorBody, create_currency_prices_error_mapper
from ..errors.list_all_component_price_points_error import (
    ListAllComponentPricePointsErrorBody,
    list_all_component_price_points_error_mapper,
)
from ..errors.update_component_price_point_error import (
    UpdateComponentPricePointErrorBody,
    update_component_price_point_error_mapper,
)
from ..errors.update_currency_prices_error import UpdateCurrencyPricesErrorBody, update_currency_prices_error_mapper
from ..models.clone_component_price_point_request import (
    CloneComponentPricePointRequest,
    CloneComponentPricePointRequestDict,
)
from ..models.component_currency_prices_response import ComponentCurrencyPricesResponse
from ..models.component_price_point_currency_overage_response import ComponentPricePointCurrencyOverageResponse
from ..models.component_price_point_response import ComponentPricePointResponse
from ..models.component_price_points_response import ComponentPricePointsResponse
from ..models.component_response import ComponentResponse
from ..models.create_component_price_point_request import (
    CreateComponentPricePointRequest,
    CreateComponentPricePointRequestDict,
)
from ..models.create_component_price_points_request import (
    CreateComponentPricePointsRequest,
    CreateComponentPricePointsRequestDict,
)
from ..models.create_currency_prices_request import CreateCurrencyPricesRequest, CreateCurrencyPricesRequestDict
from ..models.enums.list_components_price_points_include import ListComponentsPricePointsIncludeOrStr
from ..models.enums.price_point_type import PricePointTypeOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.list_components_price_points_response import ListComponentsPricePointsResponse
from ..models.list_price_points_filter import ListPricePointsFilter, ListPricePointsFilterDict
from ..models.unions.component_id_model import ComponentIdModel, ComponentIdModelDict
from ..models.unions.price_point_id_model import PricePointIdModel, PricePointIdModelDict
from ..models.update_component_price_point_request import (
    UpdateComponentPricePointRequest,
    UpdateComponentPricePointRequestDict,
)
from ..models.update_currency_prices_request import UpdateCurrencyPricesRequest, UpdateCurrencyPricesRequestDict
from ..server.server import Server


class ComponentPricePoints:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ComponentPricePointsWithRawResponse(client, server, auth)

    def archive_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointResponse:
        """Archives a component price point. Subscriptions using a price point that has been archived will continue
        using it until they're moved to another price point.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.archive_component_price_point(
                component_id, price_point_id, request_options=request_options
            ),
        )

    def bulk_create_component_price_points(
        self,
        component_id: str,
        *,
        body: CreateComponentPricePointsRequest | CreateComponentPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointsResponse:
        """Creates multiple component price points in one request.

        Args:
            component_id: The Advanced Billing id of the component for which you want to fetch price points.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.bulk_create_component_price_points(
                component_id, body=body, request_options=request_options
            ),
        )

    def clone_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: CloneComponentPricePointRequest | CloneComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointCurrencyOverageResponse:
        """Clones a component price point. Custom price points (tied to a specific subscription) cannot be cloned. The
        following attributes are copied from the source price point:
        - Pricing scheme
        - All price tiers (with starting/ending quantities and unit prices)
        - Tax included setting
        - Currency prices (if definitive pricing is set)
        - Overage pricing (for prepaid usage components)
        - Interval settings (if multi-frequency is enabled)
        - Event-based billing segments (if applicable)

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.clone_component_price_point(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    def create_component_price_point(
        self,
        component_id: int,
        *,
        body: CreateComponentPricePointRequest | CreateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointResponse:
        """Creates a price point for an existing component.

        Args:
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_component_price_point(
                component_id, body=body, request_options=request_options
            ),
        )

    def create_currency_prices(
        self,
        price_point_id: int,
        *,
        body: CreateCurrencyPricesRequest | CreateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentCurrencyPricesResponse:
        """Creates currency prices for a given currency defined at the site level.

        When creating currency prices, they need to mirror the structure of your primary pricing. For each price level
        defined on the component price point, there should be a matching price level created in the given currency.

        Note: Currency Prices are not able to be created for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_currency_prices(price_point_id, body=body, request_options=request_options)
        )

    def list_all_component_price_points(
        self,
        *,
        include: ListComponentsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListComponentsPricePointsResponse:
        """Lists all component price points belonging to a site.

        Args:
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_all_component_price_points(
                include=include,
                page=page,
                per_page=per_page,
                direction=direction,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    def list_component_price_points(
        self,
        component_id: int,
        *,
        currency_prices: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_type: list[PricePointTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointsResponse:
        """Lists the price points associated with a component.

        You may specify the component by using either the numeric id or the ``handle:gold`` syntax.

        If the price point is set to ``use_site_exchange_rate: true``, it will return pricing based on the current
        exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.

        Args:
            component_id: The Advanced Billing id of the component
            currency_prices: Include an array of currency price data.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_component_price_points(
                component_id,
                currency_prices=currency_prices,
                page=page,
                per_page=per_page,
                filter_type=filter_type,
                request_options=request_options,
            ),
        )

    def promote_component_price_point_to_default(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComponentResponse:
        """Sets a new default price point for the component. This new default will apply to all new subscriptions going
        forward - existing subscriptions will remain on their current price point.

        See `Price Points Documentation
        <https://maxio.zendesk.com/hc/en-us/articles/24261191737101-Price-Points-Components>`__ for more information on
        price points and moving subscriptions between price points.

        Note: Custom price points are not able to be set as the default for a component.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.promote_component_price_point_to_default(
                component_id, price_point_id, request_options=request_options
            ),
        )

    def read_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointCurrencyOverageResponse:
        """Returns details for a specific component price point. You can achieve this by using either the component
        price point ID or handle.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            currency_prices: Include an array of currency price data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_component_price_point(
                component_id, price_point_id, currency_prices=currency_prices, request_options=request_options
            ),
        )

    def unarchive_component_price_point(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComponentPricePointResponse:
        """Unarchives a component price point.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.unarchive_component_price_point(
                component_id, price_point_id, request_options=request_options
            ),
        )

    def update_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateComponentPricePointRequest | UpdateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointResponse:
        """Updates a component price point and its associated prices.

        Passing in a price bracket without an ``id`` will attempt to create a new price.

        Including an ``id`` will update the corresponding price, and including the ``_destroy`` flag set to true along
        with the ``id`` will remove that price.

        Note: Custom price points cannot be updated directly. They must be edited through the Subscription.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_component_price_point(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    def update_currency_prices(
        self,
        price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentCurrencyPricesResponse:
        """Updates currency prices for a given currency defined at the site level.

        Note: Currency Prices are not able to be updated for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_currency_prices(price_point_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> ComponentPricePointsWithRawResponse:
        return self._with_raw_response


class AsyncComponentPricePoints:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncComponentPricePointsWithRawResponse(client, server, auth)

    async def archive_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointResponse:
        """Archives a component price point. Subscriptions using a price point that has been archived will continue
        using it until they're moved to another price point.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.archive_component_price_point(
                component_id, price_point_id, request_options=request_options
            ),
        )

    async def bulk_create_component_price_points(
        self,
        component_id: str,
        *,
        body: CreateComponentPricePointsRequest | CreateComponentPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointsResponse:
        """Creates multiple component price points in one request.

        Args:
            component_id: The Advanced Billing id of the component for which you want to fetch price points.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_create_component_price_points(
                component_id, body=body, request_options=request_options
            ),
        )

    async def clone_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: CloneComponentPricePointRequest | CloneComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointCurrencyOverageResponse:
        """Clones a component price point. Custom price points (tied to a specific subscription) cannot be cloned. The
        following attributes are copied from the source price point:
        - Pricing scheme
        - All price tiers (with starting/ending quantities and unit prices)
        - Tax included setting
        - Currency prices (if definitive pricing is set)
        - Overage pricing (for prepaid usage components)
        - Interval settings (if multi-frequency is enabled)
        - Event-based billing segments (if applicable)

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.clone_component_price_point(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    async def create_component_price_point(
        self,
        component_id: int,
        *,
        body: CreateComponentPricePointRequest | CreateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointResponse:
        """Creates a price point for an existing component.

        Args:
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_component_price_point(
                component_id, body=body, request_options=request_options
            ),
        )

    async def create_currency_prices(
        self,
        price_point_id: int,
        *,
        body: CreateCurrencyPricesRequest | CreateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentCurrencyPricesResponse:
        """Creates currency prices for a given currency defined at the site level.

        When creating currency prices, they need to mirror the structure of your primary pricing. For each price level
        defined on the component price point, there should be a matching price level created in the given currency.

        Note: Currency Prices are not able to be created for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_currency_prices(
                price_point_id, body=body, request_options=request_options
            ),
        )

    async def list_all_component_price_points(
        self,
        *,
        include: ListComponentsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListComponentsPricePointsResponse:
        """Lists all component price points belonging to a site.

        Args:
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_all_component_price_points(
                include=include,
                page=page,
                per_page=per_page,
                direction=direction,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    async def list_component_price_points(
        self,
        component_id: int,
        *,
        currency_prices: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_type: list[PricePointTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointsResponse:
        """Lists the price points associated with a component.

        You may specify the component by using either the numeric id or the ``handle:gold`` syntax.

        If the price point is set to ``use_site_exchange_rate: true``, it will return pricing based on the current
        exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.

        Args:
            component_id: The Advanced Billing id of the component
            currency_prices: Include an array of currency price data.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_component_price_points(
                component_id,
                currency_prices=currency_prices,
                page=page,
                per_page=per_page,
                filter_type=filter_type,
                request_options=request_options,
            ),
        )

    async def promote_component_price_point_to_default(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComponentResponse:
        """Sets a new default price point for the component. This new default will apply to all new subscriptions going
        forward - existing subscriptions will remain on their current price point.

        See `Price Points Documentation
        <https://maxio.zendesk.com/hc/en-us/articles/24261191737101-Price-Points-Components>`__ for more information on
        price points and moving subscriptions between price points.

        Note: Custom price points are not able to be set as the default for a component.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.promote_component_price_point_to_default(
                component_id, price_point_id, request_options=request_options
            ),
        )

    async def read_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointCurrencyOverageResponse:
        """Returns details for a specific component price point. You can achieve this by using either the component
        price point ID or handle.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            currency_prices: Include an array of currency price data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_component_price_point(
                component_id, price_point_id, currency_prices=currency_prices, request_options=request_options
            ),
        )

    async def unarchive_component_price_point(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComponentPricePointResponse:
        """Unarchives a component price point.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.unarchive_component_price_point(
                component_id, price_point_id, request_options=request_options
            ),
        )

    async def update_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateComponentPricePointRequest | UpdateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentPricePointResponse:
        """Updates a component price point and its associated prices.

        Passing in a price bracket without an ``id`` will attempt to create a new price.

        Including an ``id`` will update the corresponding price, and including the ``_destroy`` flag set to true along
        with the ``id`` will remove that price.

        Note: Custom price points cannot be updated directly. They must be edited through the Subscription.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_component_price_point(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    async def update_currency_prices(
        self,
        price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentCurrencyPricesResponse:
        """Updates currency prices for a given currency defined at the site level.

        Note: Currency Prices are not able to be updated for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_currency_prices(
                price_point_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncComponentPricePointsWithRawResponse:
        return self._with_raw_response


class ComponentPricePointsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointResponse, ArchiveComponentPricePointErrorBody]:
        """Archives a component price point. Subscriptions using a price point that has been archived will continue
        using it until they're moved to another price point.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointResponse],
            error_mapper=archive_component_price_point_error_mapper,
            request_options=request_options,
        )

    def bulk_create_component_price_points(
        self,
        component_id: str,
        *,
        body: CreateComponentPricePointsRequest | CreateComponentPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointsResponse, BulkCreateComponentPricePointsErrorBody]:
        """Creates multiple component price points in one request.

        Args:
            component_id: The Advanced Billing id of the component for which you want to fetch price points.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/price_points/bulk.json"),
            path_params=[param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateComponentPricePointsRequest | CreateComponentPricePointsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointsResponse],
            error_mapper=bulk_create_component_price_points_error_mapper,
            request_options=request_options,
        )

    def clone_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: CloneComponentPricePointRequest | CloneComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointCurrencyOverageResponse, CloneComponentPricePointErrorBody]:
        """Clones a component price point. Custom price points (tied to a specific subscription) cannot be cloned. The
        following attributes are copied from the source price point:
        - Pricing scheme
        - All price tiers (with starting/ending quantities and unit prices)
        - Tax included setting
        - Currency prices (if definitive pricing is set)
        - Overage pricing (for prepaid usage components)
        - Interval settings (if multi-frequency is enabled)
        - Event-based billing segments (if applicable)

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}/clone.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloneComponentPricePointRequest | CloneComponentPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointCurrencyOverageResponse],
            error_mapper=clone_component_price_point_error_mapper,
            request_options=request_options,
        )

    def create_component_price_point(
        self,
        component_id: int,
        *,
        body: CreateComponentPricePointRequest | CreateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointResponse, CreateComponentPricePointErrorBody]:
        """Creates a price point for an existing component.

        Args:
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/price_points.json"),
            path_params=[param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateComponentPricePointRequest | CreateComponentPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointResponse],
            error_mapper=create_component_price_point_error_mapper,
            request_options=request_options,
        )

    def create_currency_prices(
        self,
        price_point_id: int,
        *,
        body: CreateCurrencyPricesRequest | CreateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentCurrencyPricesResponse, CreateCurrencyPricesErrorBody]:
        """Creates currency prices for a given currency defined at the site level.

        When creating currency prices, they need to mirror the structure of your primary pricing. For each price level
        defined on the component price point, there should be a matching price level created in the given currency.

        Note: Currency Prices are not able to be created for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/price_points/{price_point_id}/currency_prices.json"),
            path_params=[param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCurrencyPricesRequest | CreateCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentCurrencyPricesResponse],
            error_mapper=create_currency_prices_error_mapper,
            request_options=request_options,
        )

    def list_all_component_price_points(
        self,
        *,
        include: ListComponentsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListComponentsPricePointsResponse, ListAllComponentPricePointsErrorBody]:
        """Lists all component price points belonging to a site.

        Args:
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components_price_points.json"),
            query_params=[
                param[ListComponentsPricePointsIncludeOrStr | None]("include", include),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListPricePointsFilter | ListPricePointsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListComponentsPricePointsResponse],
            error_mapper=list_all_component_price_points_error_mapper,
            request_options=request_options,
        )

    def list_component_price_points(
        self,
        component_id: int,
        *,
        currency_prices: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_type: list[PricePointTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointsResponse, RawError]:
        """Lists the price points associated with a component.

        You may specify the component by using either the numeric id or the ``handle:gold`` syntax.

        If the price point is set to ``use_site_exchange_rate: true``, it will return pricing based on the current
        exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.

        Args:
            component_id: The Advanced Billing id of the component
            currency_prices: Include an array of currency price data.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/price_points.json"),
            path_params=[param[int]("component_id", component_id)],
            query_params=[
                param[bool | None]("currency_prices", currency_prices),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[PricePointTypeOrStr] | None]("filter[type]", filter_type),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def promote_component_price_point_to_default(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComponentResponse, RawError]:
        """Sets a new default price point for the component. This new default will apply to all new subscriptions going
        forward - existing subscriptions will remain on their current price point.

        See `Price Points Documentation
        <https://maxio.zendesk.com/hc/en-us/articles/24261191737101-Price-Points-Components>`__ for more information on
        price points and moving subscriptions between price points.

        Note: Custom price points are not able to be set as the default for a component.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/default.json"
            ),
            path_params=[param[int]("component_id", component_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointCurrencyOverageResponse, RawError]:
        """Returns details for a specific component price point. You can achieve this by using either the component
        price point ID or handle.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            currency_prices: Include an array of currency price data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            query_params=[param[bool | None]("currency_prices", currency_prices)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointCurrencyOverageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unarchive_component_price_point(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComponentPricePointResponse, RawError]:
        """Unarchives a component price point.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/unarchive.json"
            ),
            path_params=[param[int]("component_id", component_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateComponentPricePointRequest | UpdateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointResponse, UpdateComponentPricePointErrorBody]:
        """Updates a component price point and its associated prices.

        Passing in a price bracket without an ``id`` will attempt to create a new price.

        Including an ``id`` will update the corresponding price, and including the ``_destroy`` flag set to true along
        with the ``id`` will remove that price.

        Note: Custom price points cannot be updated directly. They must be edited through the Subscription.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateComponentPricePointRequest | UpdateComponentPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentPricePointResponse],
            error_mapper=update_component_price_point_error_mapper,
            request_options=request_options,
        )

    def update_currency_prices(
        self,
        price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentCurrencyPricesResponse, UpdateCurrencyPricesErrorBody]:
        """Updates currency prices for a given currency defined at the site level.

        Note: Currency Prices are not able to be updated for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/price_points/{price_point_id}/currency_prices.json"),
            path_params=[param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentCurrencyPricesResponse],
            error_mapper=update_currency_prices_error_mapper,
            request_options=request_options,
        )


class AsyncComponentPricePointsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointResponse, ArchiveComponentPricePointErrorBody]:
        """Archives a component price point. Subscriptions using a price point that has been archived will continue
        using it until they're moved to another price point.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointResponse],
            error_mapper=archive_component_price_point_error_mapper,
            request_options=request_options,
        )

    async def bulk_create_component_price_points(
        self,
        component_id: str,
        *,
        body: CreateComponentPricePointsRequest | CreateComponentPricePointsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointsResponse, BulkCreateComponentPricePointsErrorBody]:
        """Creates multiple component price points in one request.

        Args:
            component_id: The Advanced Billing id of the component for which you want to fetch price points.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/price_points/bulk.json"),
            path_params=[param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateComponentPricePointsRequest | CreateComponentPricePointsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointsResponse],
            error_mapper=bulk_create_component_price_points_error_mapper,
            request_options=request_options,
        )

    async def clone_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: CloneComponentPricePointRequest | CloneComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointCurrencyOverageResponse, CloneComponentPricePointErrorBody]:
        """Clones a component price point. Custom price points (tied to a specific subscription) cannot be cloned. The
        following attributes are copied from the source price point:
        - Pricing scheme
        - All price tiers (with starting/ending quantities and unit prices)
        - Tax included setting
        - Currency prices (if definitive pricing is set)
        - Overage pricing (for prepaid usage components)
        - Interval settings (if multi-frequency is enabled)
        - Event-based billing segments (if applicable)

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}/clone.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloneComponentPricePointRequest | CloneComponentPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointCurrencyOverageResponse],
            error_mapper=clone_component_price_point_error_mapper,
            request_options=request_options,
        )

    async def create_component_price_point(
        self,
        component_id: int,
        *,
        body: CreateComponentPricePointRequest | CreateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointResponse, CreateComponentPricePointErrorBody]:
        """Creates a price point for an existing component.

        Args:
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/price_points.json"),
            path_params=[param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateComponentPricePointRequest | CreateComponentPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointResponse],
            error_mapper=create_component_price_point_error_mapper,
            request_options=request_options,
        )

    async def create_currency_prices(
        self,
        price_point_id: int,
        *,
        body: CreateCurrencyPricesRequest | CreateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentCurrencyPricesResponse, CreateCurrencyPricesErrorBody]:
        """Creates currency prices for a given currency defined at the site level.

        When creating currency prices, they need to mirror the structure of your primary pricing. For each price level
        defined on the component price point, there should be a matching price level created in the given currency.

        Note: Currency Prices are not able to be created for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/price_points/{price_point_id}/currency_prices.json"),
            path_params=[param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCurrencyPricesRequest | CreateCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentCurrencyPricesResponse],
            error_mapper=create_currency_prices_error_mapper,
            request_options=request_options,
        )

    async def list_all_component_price_points(
        self,
        *,
        include: ListComponentsPricePointsIncludeOrStr | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListPricePointsFilter | ListPricePointsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListComponentsPricePointsResponse, ListAllComponentPricePointsErrorBody]:
        """Lists all component price points belonging to a site.

        Args:
            include: Allows including additional data in the response. Use in query: ``include=currency_prices``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List PricePoints operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components_price_points.json"),
            query_params=[
                param[ListComponentsPricePointsIncludeOrStr | None]("include", include),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListPricePointsFilter | ListPricePointsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListComponentsPricePointsResponse],
            error_mapper=list_all_component_price_points_error_mapper,
            request_options=request_options,
        )

    async def list_component_price_points(
        self,
        component_id: int,
        *,
        currency_prices: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_type: list[PricePointTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointsResponse, RawError]:
        """Lists the price points associated with a component.

        You may specify the component by using either the numeric id or the ``handle:gold`` syntax.

        If the price point is set to ``use_site_exchange_rate: true``, it will return pricing based on the current
        exchange rate. If the flag is set to false, it will return all of the defined prices for each currency.

        Args:
            component_id: The Advanced Billing id of the component
            currency_prices: Include an array of currency price data.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_type: Use in query: ``filter[type]=catalog,default``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/price_points.json"),
            path_params=[param[int]("component_id", component_id)],
            query_params=[
                param[bool | None]("currency_prices", currency_prices),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[PricePointTypeOrStr] | None]("filter[type]", filter_type),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def promote_component_price_point_to_default(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComponentResponse, RawError]:
        """Sets a new default price point for the component. This new default will apply to all new subscriptions going
        forward - existing subscriptions will remain on their current price point.

        See `Price Points Documentation
        <https://maxio.zendesk.com/hc/en-us/articles/24261191737101-Price-Points-Components>`__ for more information on
        price points and moving subscriptions between price points.

        Note: Custom price points are not able to be set as the default for a component.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/default.json"
            ),
            path_params=[param[int]("component_id", component_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointCurrencyOverageResponse, RawError]:
        """Returns details for a specific component price point. You can achieve this by using either the component
        price point ID or handle.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            currency_prices: Include an array of currency price data.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            query_params=[param[bool | None]("currency_prices", currency_prices)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointCurrencyOverageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unarchive_component_price_point(
        self, component_id: int, price_point_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComponentPricePointResponse, RawError]:
        """Unarchives a component price point.

        Args:
            component_id: The Advanced Billing id of the component to which the price point belongs
            price_point_id: The Advanced Billing id of the price point
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/unarchive.json"
            ),
            path_params=[param[int]("component_id", component_id), param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_component_price_point(
        self,
        component_id: ComponentIdModel | ComponentIdModelDict,
        price_point_id: PricePointIdModel | PricePointIdModelDict,
        *,
        body: UpdateComponentPricePointRequest | UpdateComponentPricePointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentPricePointResponse, UpdateComponentPricePointErrorBody]:
        """Updates a component price point and its associated prices.

        Passing in a price bracket without an ``id`` will attempt to create a new price.

        Including an ``id`` will update the corresponding price, and including the ``_destroy`` flag set to true along
        with the ``id`` will remove that price.

        Note: Custom price points cannot be updated directly. They must be edited through the Subscription.

        Args:
            component_id: The id or handle of the component. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-product-handle`` for a string
                handle.
            price_point_id: The id or handle of the price point. When using the handle, it must be prefixed with
                ``handle:``. Example: ``123`` for an integer ID, or ``handle:example-price_point-handle`` for a string
                handle.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/components/{component_id}/price_points/{price_point_id}.json"),
            path_params=[
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
                param[PricePointIdModel | PricePointIdModelDict]("price_point_id", price_point_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateComponentPricePointRequest | UpdateComponentPricePointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentPricePointResponse],
            error_mapper=update_component_price_point_error_mapper,
            request_options=request_options,
        )

    async def update_currency_prices(
        self,
        price_point_id: int,
        *,
        body: UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentCurrencyPricesResponse, UpdateCurrencyPricesErrorBody]:
        """Updates currency prices for a given currency defined at the site level.

        Note: Currency Prices are not able to be updated for custom price points.

        Args:
            price_point_id: The Advanced Billing id of the price point
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/price_points/{price_point_id}/currency_prices.json"),
            path_params=[param[int]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCurrencyPricesRequest | UpdateCurrencyPricesRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentCurrencyPricesResponse],
            error_mapper=update_currency_prices_error_mapper,
            request_options=request_options,
        )
