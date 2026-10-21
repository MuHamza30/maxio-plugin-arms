from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.list_sale_rep_item import ListSaleRepItem
from ..models.sale_rep import SaleRep
from ..models.sale_rep_settings import SaleRepSettings
from ..server.server import Server


class SalesCommissions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SalesCommissionsWithRawResponse(client, server, auth)

    def list_sales_commission_settings(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SaleRepSettings]:
        """Lists subscriptions with associated sales reps.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_sales_commission_settings(
                seller_id,
                live_mode=live_mode,
                page=page,
                per_page=per_page,
                authorization=authorization,
                request_options=request_options,
            ),
        )

    def list_sales_reps(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ListSaleRepItem]:
        """Lists sales reps with details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_sales_reps(
                seller_id,
                live_mode=live_mode,
                page=page,
                per_page=per_page,
                authorization=authorization,
                request_options=request_options,
            ),
        )

    def read_sales_rep(
        self,
        seller_id: str,
        sales_rep_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> SaleRep:
        """Returns a sales rep and attached subscription details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            sales_rep_id: The Advanced Billing id of sales rep.
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_sales_rep(
                seller_id,
                sales_rep_id,
                live_mode=live_mode,
                page=page,
                per_page=per_page,
                authorization=authorization,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SalesCommissionsWithRawResponse:
        return self._with_raw_response


class AsyncSalesCommissions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSalesCommissionsWithRawResponse(client, server, auth)

    async def list_sales_commission_settings(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SaleRepSettings]:
        """Lists subscriptions with associated sales reps.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_sales_commission_settings(
                seller_id,
                live_mode=live_mode,
                page=page,
                per_page=per_page,
                authorization=authorization,
                request_options=request_options,
            ),
        )

    async def list_sales_reps(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ListSaleRepItem]:
        """Lists sales reps with details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_sales_reps(
                seller_id,
                live_mode=live_mode,
                page=page,
                per_page=per_page,
                authorization=authorization,
                request_options=request_options,
            ),
        )

    async def read_sales_rep(
        self,
        seller_id: str,
        sales_rep_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> SaleRep:
        """Returns a sales rep and attached subscription details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            sales_rep_id: The Advanced Billing id of sales rep.
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_sales_rep(
                seller_id,
                sales_rep_id,
                live_mode=live_mode,
                page=page,
                per_page=per_page,
                authorization=authorization,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSalesCommissionsWithRawResponse:
        return self._with_raw_response


class SalesCommissionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_sales_commission_settings(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SaleRepSettings], RawError]:
        """Lists subscriptions with associated sales reps.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/sellers/{seller_id}/sales_commission_settings.json"),
            path_params=[param[str]("seller_id", seller_id)],
            query_params=[
                param[bool | None]("live_mode", live_mode),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[SaleRepSettings]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sales_reps(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ListSaleRepItem], RawError]:
        """Lists sales reps with details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/sellers/{seller_id}/sales_reps.json"),
            path_params=[param[str]("seller_id", seller_id)],
            query_params=[
                param[bool | None]("live_mode", live_mode),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ListSaleRepItem]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_sales_rep(
        self,
        seller_id: str,
        sales_rep_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SaleRep, RawError]:
        """Returns a sales rep and attached subscription details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            sales_rep_id: The Advanced Billing id of sales rep.
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/sellers/{seller_id}/sales_reps/{sales_rep_id}.json"),
            path_params=[param[str]("seller_id", seller_id), param[str]("sales_rep_id", sales_rep_id)],
            query_params=[
                param[bool | None]("live_mode", live_mode),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SaleRep],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSalesCommissionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_sales_commission_settings(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SaleRepSettings], RawError]:
        """Lists subscriptions with associated sales reps.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/sellers/{seller_id}/sales_commission_settings.json"),
            path_params=[param[str]("seller_id", seller_id)],
            query_params=[
                param[bool | None]("live_mode", live_mode),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[SaleRepSettings]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sales_reps(
        self,
        seller_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ListSaleRepItem], RawError]:
        """Lists sales reps with details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/sellers/{seller_id}/sales_reps.json"),
            path_params=[param[str]("seller_id", seller_id)],
            query_params=[
                param[bool | None]("live_mode", live_mode),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ListSaleRepItem]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_sales_rep(
        self,
        seller_id: str,
        sales_rep_id: str,
        *,
        live_mode: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 100,
        authorization: str | None = "Bearer <<apiKey>>",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SaleRep, RawError]:
        """Returns a sales rep and attached subscription details.

        ## Modified Authentication Process

        The Sales Commission API differs from other Chargify API endpoints. This resource is associated with the seller
        itself. Up to now all available resources were at the level of the site, therefore creating the API Key per site
        was a sufficient solution. To share resources at the seller level, a new authentication method was introduced,
        which is user authentication. Creating an API Key for a user is a required step to correctly use the Sales
        Commission API, more details `here
        <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.

        Access to the Sales Commission API endpoints is available to users with financial access, where the seller has
        the Advanced Analytics component enabled. For further information on getting access to Advanced Analytics
        contact Maxio support.

        > Note: The request is at seller level, it means ``<<subdomain>>`` variable will be replaced by ``app``.

        Args:
            seller_id: The Chargify id of your seller account
            sales_rep_id: The Advanced Billing id of sales rep.
            live_mode: This parameter indicates if records should be fetched from live mode sites. Default value is
                true.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 100.
            authorization: For authorization use user API key. See details `here
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjMyNzk5NTg0-2020-04-20-new-api-authentication>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/sellers/{seller_id}/sales_reps/{sales_rep_id}.json"),
            path_params=[param[str]("seller_id", seller_id), param[str]("sales_rep_id", sales_rep_id)],
            query_params=[
                param[bool | None]("live_mode", live_mode),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            headers=[param[str | None]("Authorization", authorization)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SaleRep],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
