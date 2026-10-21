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
from ..errors.create_offer_error import CreateOfferErrorBody, create_offer_error_mapper
from ..errors.list_offers_error import ListOffersErrorBody, list_offers_error_mapper
from ..models.create_offer_request import CreateOfferRequest, CreateOfferRequestDict
from ..models.list_offers_response import ListOffersResponse
from ..models.offer_response import OfferResponse
from ..server.server import Server


class Offers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OffersWithRawResponse(client, server, auth)

    def archive_offer(self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Archives an existing offer. Please provide an ``offer_id`` in order to archive the correct item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.archive_offer(offer_id, request_options=request_options))

    def create_offer(
        self,
        *,
        body: CreateOfferRequest | CreateOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OfferResponse:
        """Creates an offer within your site.

        Offers allow you to package complicated combinations of products, components and coupons into a convenient
        package which can then be subscribed to just like products.

        Once an offer is defined it can be used as an alternative to the product when creating subscriptions.

        For more information, see `Offers
        <https://maxio.zendesk.com/hc/en-us/articles/24261295098637-Offers-Overview>`__ in the product documentation.

        ## Using a Product Price Point

        You can optionally pass in a ``product_price_point_id`` that corresponds with the ``product_id`` and the offer
        will use that price point. If a ``product_price_point_id`` is not passed in, the product's default price point
        will be used.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_offer(body=body, request_options=request_options))

    def list_offers(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListOffersResponse:
        """Lists offers for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_offers(
                page=page, per_page=per_page, include_archived=include_archived, request_options=request_options
            ),
        )

    def read_offer(self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> OfferResponse:
        """Returns a specific offer's attributes. This is different from listing all offers for a site, as it requires
        an ``offer_id``.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_offer(offer_id, request_options=request_options))

    def unarchive_offer(self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Unarchives a previously archived offer. Please provide an ``offer_id`` in order to unarchive the correct
        item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.unarchive_offer(offer_id, request_options=request_options))

    @property
    def with_raw_response(self) -> OffersWithRawResponse:
        return self._with_raw_response


class AsyncOffers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOffersWithRawResponse(client, server, auth)

    async def archive_offer(self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Archives an existing offer. Please provide an ``offer_id`` in order to archive the correct item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.archive_offer(offer_id, request_options=request_options))

    async def create_offer(
        self,
        *,
        body: CreateOfferRequest | CreateOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OfferResponse:
        """Creates an offer within your site.

        Offers allow you to package complicated combinations of products, components and coupons into a convenient
        package which can then be subscribed to just like products.

        Once an offer is defined it can be used as an alternative to the product when creating subscriptions.

        For more information, see `Offers
        <https://maxio.zendesk.com/hc/en-us/articles/24261295098637-Offers-Overview>`__ in the product documentation.

        ## Using a Product Price Point

        You can optionally pass in a ``product_price_point_id`` that corresponds with the ``product_id`` and the offer
        will use that price point. If a ``product_price_point_id`` is not passed in, the product's default price point
        will be used.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_offer(body=body, request_options=request_options))

    async def list_offers(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListOffersResponse:
        """Lists offers for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_offers(
                page=page, per_page=per_page, include_archived=include_archived, request_options=request_options
            ),
        )

    async def read_offer(self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> OfferResponse:
        """Returns a specific offer's attributes. This is different from listing all offers for a site, as it requires
        an ``offer_id``.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_offer(offer_id, request_options=request_options))

    async def unarchive_offer(self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Unarchives a previously archived offer. Please provide an ``offer_id`` in order to unarchive the correct
        item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.unarchive_offer(offer_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncOffersWithRawResponse:
        return self._with_raw_response


class OffersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_offer(
        self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Archives an existing offer. Please provide an ``offer_id`` in order to archive the correct item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/offers/{offer_id}/archive.json"),
            path_params=[param[int]("offer_id", offer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_offer(
        self,
        *,
        body: CreateOfferRequest | CreateOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OfferResponse, CreateOfferErrorBody]:
        """Creates an offer within your site.

        Offers allow you to package complicated combinations of products, components and coupons into a convenient
        package which can then be subscribed to just like products.

        Once an offer is defined it can be used as an alternative to the product when creating subscriptions.

        For more information, see `Offers
        <https://maxio.zendesk.com/hc/en-us/articles/24261295098637-Offers-Overview>`__ in the product documentation.

        ## Using a Product Price Point

        You can optionally pass in a ``product_price_point_id`` that corresponds with the ``product_id`` and the offer
        will use that price point. If a ``product_price_point_id`` is not passed in, the product's default price point
        will be used.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/offers.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOfferRequest | CreateOfferRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[OfferResponse],
            error_mapper=create_offer_error_mapper,
            request_options=request_options,
        )

    def list_offers(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListOffersResponse, ListOffersErrorBody]:
        """Lists offers for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/offers.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("include_archived", include_archived),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListOffersResponse],
            error_mapper=list_offers_error_mapper,
            request_options=request_options,
        )

    def read_offer(
        self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OfferResponse, RawError]:
        """Returns a specific offer's attributes. This is different from listing all offers for a site, as it requires
        an ``offer_id``.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/offers/{offer_id}.json"),
            path_params=[param[int]("offer_id", offer_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[OfferResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unarchive_offer(
        self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Unarchives a previously archived offer. Please provide an ``offer_id`` in order to unarchive the correct
        item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/offers/{offer_id}/unarchive.json"),
            path_params=[param[int]("offer_id", offer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncOffersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_offer(
        self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Archives an existing offer. Please provide an ``offer_id`` in order to archive the correct item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/offers/{offer_id}/archive.json"),
            path_params=[param[int]("offer_id", offer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_offer(
        self,
        *,
        body: CreateOfferRequest | CreateOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OfferResponse, CreateOfferErrorBody]:
        """Creates an offer within your site.

        Offers allow you to package complicated combinations of products, components and coupons into a convenient
        package which can then be subscribed to just like products.

        Once an offer is defined it can be used as an alternative to the product when creating subscriptions.

        For more information, see `Offers
        <https://maxio.zendesk.com/hc/en-us/articles/24261295098637-Offers-Overview>`__ in the product documentation.

        ## Using a Product Price Point

        You can optionally pass in a ``product_price_point_id`` that corresponds with the ``product_id`` and the offer
        will use that price point. If a ``product_price_point_id`` is not passed in, the product's default price point
        will be used.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/offers.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOfferRequest | CreateOfferRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[OfferResponse],
            error_mapper=create_offer_error_mapper,
            request_options=request_options,
        )

    async def list_offers(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include_archived: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListOffersResponse, ListOffersErrorBody]:
        """Lists offers for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include_archived: Include archived products. Use in query: ``include_archived=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/offers.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[bool | None]("include_archived", include_archived),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListOffersResponse],
            error_mapper=list_offers_error_mapper,
            request_options=request_options,
        )

    async def read_offer(
        self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OfferResponse, RawError]:
        """Returns a specific offer's attributes. This is different from listing all offers for a site, as it requires
        an ``offer_id``.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/offers/{offer_id}.json"),
            path_params=[param[int]("offer_id", offer_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[OfferResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unarchive_offer(
        self, offer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Unarchives a previously archived offer. Please provide an ``offer_id`` in order to unarchive the correct
        item.

        Args:
            offer_id: The Chargify id of the offer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/offers/{offer_id}/unarchive.json"),
            path_params=[param[int]("offer_id", offer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
