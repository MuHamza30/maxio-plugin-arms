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
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.cleanup_scope import CleanupScope, CleanupScopeOrStr
from ..models.list_public_keys_response import ListPublicKeysResponse
from ..models.site_response import SiteResponse
from ..server.server import Server


class Sites:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SitesWithRawResponse(client, server, auth)

    def clear_site(
        self,
        *,
        cleanup_scope: CleanupScopeOrStr | None = CleanupScope.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Clears all data from a test site asynchronously. This call is asynchronous and there may be a delay before
        the site data is fully deleted. If you are clearing site data for an automated test, you will need to build in a
        delay and/or check that there are no products, etc., in the site before proceeding.

        **This functionality will only work on sites in TEST mode. Attempts to perform this on sites in “live” mode will
        result in a response of 403 FORBIDDEN.**

        Args:
            cleanup_scope: ``all``: Will clear all products, customers, and related subscriptions from the site.
                ``customers``: Will clear only customers and related subscriptions (leaving the products untouched) for
                the site. Revenue will also be reset to 0. Use in query ``cleanup_scope=all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.clear_site(cleanup_scope=cleanup_scope, request_options=request_options))

    def list_chargify_js_public_keys(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ListPublicKeysResponse:
        """Lists public keys used for Maxio.js (formerly Chargify.js).

        Args:
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
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_chargify_js_public_keys(
                page=page, per_page=per_page, request_options=request_options
            ),
        )

    def read_site(self, *, request_options: RequestOptionsOrDict | None = None) -> SiteResponse:
        """Retrieves site data.

        For more information, see `Sites <https://maxio.zendesk.com/hc/en-us/sections/24250550707085-Sites>`__ in the
        product documentation. Specifically, the `Clearing Site Data
        <https://maxio.zendesk.com/hc/en-us/articles/24250617028365-Clearing-Site-Data>`__ section is relevant to this
        endpoint.

        #### Relationship invoicing enabled If the site has Relationship invoicing enabled, additional properties are
        returned in the response:

        ```
        "customer_hierarchy_enabled": true, "whopays_enabled": true, "whopays_default_payer": "self"
        ```

        For more information, see `Who Pays & Customer Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_site(request_options=request_options))

    @property
    def with_raw_response(self) -> SitesWithRawResponse:
        return self._with_raw_response


class AsyncSites:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSitesWithRawResponse(client, server, auth)

    async def clear_site(
        self,
        *,
        cleanup_scope: CleanupScopeOrStr | None = CleanupScope.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Clears all data from a test site asynchronously. This call is asynchronous and there may be a delay before
        the site data is fully deleted. If you are clearing site data for an automated test, you will need to build in a
        delay and/or check that there are no products, etc., in the site before proceeding.

        **This functionality will only work on sites in TEST mode. Attempts to perform this on sites in “live” mode will
        result in a response of 403 FORBIDDEN.**

        Args:
            cleanup_scope: ``all``: Will clear all products, customers, and related subscriptions from the site.
                ``customers``: Will clear only customers and related subscriptions (leaving the products untouched) for
                the site. Revenue will also be reset to 0. Use in query ``cleanup_scope=all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.clear_site(cleanup_scope=cleanup_scope, request_options=request_options)
        )

    async def list_chargify_js_public_keys(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ListPublicKeysResponse:
        """Lists public keys used for Maxio.js (formerly Chargify.js).

        Args:
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
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_chargify_js_public_keys(
                page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def read_site(self, *, request_options: RequestOptionsOrDict | None = None) -> SiteResponse:
        """Retrieves site data.

        For more information, see `Sites <https://maxio.zendesk.com/hc/en-us/sections/24250550707085-Sites>`__ in the
        product documentation. Specifically, the `Clearing Site Data
        <https://maxio.zendesk.com/hc/en-us/articles/24250617028365-Clearing-Site-Data>`__ section is relevant to this
        endpoint.

        #### Relationship invoicing enabled If the site has Relationship invoicing enabled, additional properties are
        returned in the response:

        ```
        "customer_hierarchy_enabled": true, "whopays_enabled": true, "whopays_default_payer": "self"
        ```

        For more information, see `Who Pays & Customer Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_site(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncSitesWithRawResponse:
        return self._with_raw_response


class SitesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def clear_site(
        self,
        *,
        cleanup_scope: CleanupScopeOrStr | None = CleanupScope.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Clears all data from a test site asynchronously. This call is asynchronous and there may be a delay before
        the site data is fully deleted. If you are clearing site data for an automated test, you will need to build in a
        delay and/or check that there are no products, etc., in the site before proceeding.

        **This functionality will only work on sites in TEST mode. Attempts to perform this on sites in “live” mode will
        result in a response of 403 FORBIDDEN.**

        Args:
            cleanup_scope: ``all``: Will clear all products, customers, and related subscriptions from the site.
                ``customers``: Will clear only customers and related subscriptions (leaving the products untouched) for
                the site. Revenue will also be reset to 0. Use in query ``cleanup_scope=all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/sites/clear_data.json"),
            query_params=[param[CleanupScopeOrStr | None]("cleanup_scope", cleanup_scope)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_chargify_js_public_keys(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListPublicKeysResponse, RawError]:
        """Lists public keys used for Maxio.js (formerly Chargify.js).

        Args:
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
            url_template=self._server.production("/chargify_js_keys.json"),
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListPublicKeysResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_site(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SiteResponse, RawError]:
        """Retrieves site data.

        For more information, see `Sites <https://maxio.zendesk.com/hc/en-us/sections/24250550707085-Sites>`__ in the
        product documentation. Specifically, the `Clearing Site Data
        <https://maxio.zendesk.com/hc/en-us/articles/24250617028365-Clearing-Site-Data>`__ section is relevant to this
        endpoint.

        #### Relationship invoicing enabled If the site has Relationship invoicing enabled, additional properties are
        returned in the response:

        ```
        "customer_hierarchy_enabled": true, "whopays_enabled": true, "whopays_default_payer": "self"
        ```

        For more information, see `Who Pays & Customer Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/site.json"),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SiteResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSitesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def clear_site(
        self,
        *,
        cleanup_scope: CleanupScopeOrStr | None = CleanupScope.ALL,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Clears all data from a test site asynchronously. This call is asynchronous and there may be a delay before
        the site data is fully deleted. If you are clearing site data for an automated test, you will need to build in a
        delay and/or check that there are no products, etc., in the site before proceeding.

        **This functionality will only work on sites in TEST mode. Attempts to perform this on sites in “live” mode will
        result in a response of 403 FORBIDDEN.**

        Args:
            cleanup_scope: ``all``: Will clear all products, customers, and related subscriptions from the site.
                ``customers``: Will clear only customers and related subscriptions (leaving the products untouched) for
                the site. Revenue will also be reset to 0. Use in query ``cleanup_scope=all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/sites/clear_data.json"),
            query_params=[param[CleanupScopeOrStr | None]("cleanup_scope", cleanup_scope)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_chargify_js_public_keys(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListPublicKeysResponse, RawError]:
        """Lists public keys used for Maxio.js (formerly Chargify.js).

        Args:
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
            url_template=self._server.production("/chargify_js_keys.json"),
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListPublicKeysResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_site(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteResponse, RawError]:
        """Retrieves site data.

        For more information, see `Sites <https://maxio.zendesk.com/hc/en-us/sections/24250550707085-Sites>`__ in the
        product documentation. Specifically, the `Clearing Site Data
        <https://maxio.zendesk.com/hc/en-us/articles/24250617028365-Clearing-Site-Data>`__ section is relevant to this
        endpoint.

        #### Relationship invoicing enabled If the site has Relationship invoicing enabled, additional properties are
        returned in the response:

        ```
        "customer_hierarchy_enabled": true, "whopays_enabled": true, "whopays_default_payer": "self"
        ```

        For more information, see `Who Pays & Customer Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/site.json"),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SiteResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
