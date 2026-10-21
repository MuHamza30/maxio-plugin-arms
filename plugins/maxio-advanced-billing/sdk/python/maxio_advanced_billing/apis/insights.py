from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.list_mrr_per_subscription_error import (
    ListMrrPerSubscriptionErrorBody,
    list_mrr_per_subscription_error_mapper,
)
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.list_mrr_filter import ListMrrFilter, ListMrrFilterDict
from ..models.list_mrr_response import ListMrrResponse
from ..models.mrr_response import MrrResponse
from ..models.site_summary import SiteSummary
from ..models.subscription_mrr_response import SubscriptionMrrResponse
from ..server.server import Server


class Insights:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightsWithRawResponse(client, server, auth)

    def list_mrr_movements(
        self,
        *,
        subscription_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 10,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMrrResponse:
        """Lists your site's MRR movements.

        ## Understanding MRR movements

        This endpoint will aid in accessing your site's `MRR Report
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics>`__ data.

        Whenever a subscription event occurs that causes your site's MRR to change (such as a signup or upgrade), we
        record an MRR movement. These records are accessible via the MRR Movements endpoint.

        Each MRR Movement belongs to a subscription and contains a timestamp, category, and an amount. ``line_items``
        represent the subscription's product configuration at the time of the movement.

        ### Plan & Usage Breakouts

        In the MRR Report UI, we support a setting to `include or exclude
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics#displaying-component-based-metered-usage-in-mrr>`__
        usage revenue. In the MRR APIs, responses include ``plan`` and ``usage`` breakouts.

        Plan includes revenue from:
        * Products
        * Quantity-Based Components
        * On/Off Components

        Usage includes revenue from:
        * Metered Components
        * Prepaid Usage Components

        Args:
            subscription_id: (Optional) Filter results by subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 50; any per_page value over 50 will be changed to 50. Use in query
                ``per_page=20``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_mrr_movements(
                subscription_id=subscription_id,
                page=page,
                per_page=per_page,
                direction=direction,
                request_options=request_options,
            ),
        )

    def list_mrr_per_subscription(
        self,
        *,
        filter_: ListMrrFilter | ListMrrFilterDict | None = None,
        at_time: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionMrrResponse:
        """Lists your site's current MRR, including plan and usage breakouts split per subscription.

        Args:
            filter_: Filter to use for List MRR per subscription operation
            at_time: Submit a timestamp in ISO8601 format to request MRR for a historic time. Use in query:
                ``at_time=2022-01-10T10:00:00-05:00``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Records are ordered by subscription_id in
                ascending order by default. Use in query ``direction=desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``SubscriptionsMrrErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_mrr_per_subscription(
                filter_=filter_,
                at_time=at_time,
                page=page,
                per_page=per_page,
                direction=direction,
                request_options=request_options,
            ),
        )

    def read_mrr(
        self,
        *,
        at_time: RFC3339DateTime | None = None,
        subscription_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MrrResponse:
        """Returns your site's current MRR, including plan and usage breakouts.

        Args:
            at_time: submit a timestamp in ISO8601 format to request MRR for a historic time.
            subscription_id: submit the id of a subscription in order to limit results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_mrr(
                at_time=at_time, subscription_id=subscription_id, request_options=request_options
            ),
        )

    def read_site_stats(self, *, request_options: RequestOptionsOrDict | None = None) -> SiteSummary:
        """Returns basic site-level stats. This API call only answers with JSON responses. An XML version is not
        provided.

        ## Stats Documentation

        There currently is not a complimentary matching set of documentation that compliments this endpoint. However,
        each Site's dashboard will reflect the summary of information provided in the Stats response.

        ```
        https://subdomain.chargify.com/dashboard
        ```

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_site_stats(request_options=request_options))

    @property
    def with_raw_response(self) -> InsightsWithRawResponse:
        return self._with_raw_response


class AsyncInsights:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightsWithRawResponse(client, server, auth)

    async def list_mrr_movements(
        self,
        *,
        subscription_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 10,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMrrResponse:
        """Lists your site's MRR movements.

        ## Understanding MRR movements

        This endpoint will aid in accessing your site's `MRR Report
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics>`__ data.

        Whenever a subscription event occurs that causes your site's MRR to change (such as a signup or upgrade), we
        record an MRR movement. These records are accessible via the MRR Movements endpoint.

        Each MRR Movement belongs to a subscription and contains a timestamp, category, and an amount. ``line_items``
        represent the subscription's product configuration at the time of the movement.

        ### Plan & Usage Breakouts

        In the MRR Report UI, we support a setting to `include or exclude
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics#displaying-component-based-metered-usage-in-mrr>`__
        usage revenue. In the MRR APIs, responses include ``plan`` and ``usage`` breakouts.

        Plan includes revenue from:
        * Products
        * Quantity-Based Components
        * On/Off Components

        Usage includes revenue from:
        * Metered Components
        * Prepaid Usage Components

        Args:
            subscription_id: (Optional) Filter results by subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 50; any per_page value over 50 will be changed to 50. Use in query
                ``per_page=20``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_mrr_movements(
                subscription_id=subscription_id,
                page=page,
                per_page=per_page,
                direction=direction,
                request_options=request_options,
            ),
        )

    async def list_mrr_per_subscription(
        self,
        *,
        filter_: ListMrrFilter | ListMrrFilterDict | None = None,
        at_time: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionMrrResponse:
        """Lists your site's current MRR, including plan and usage breakouts split per subscription.

        Args:
            filter_: Filter to use for List MRR per subscription operation
            at_time: Submit a timestamp in ISO8601 format to request MRR for a historic time. Use in query:
                ``at_time=2022-01-10T10:00:00-05:00``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Records are ordered by subscription_id in
                ascending order by default. Use in query ``direction=desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``SubscriptionsMrrErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_mrr_per_subscription(
                filter_=filter_,
                at_time=at_time,
                page=page,
                per_page=per_page,
                direction=direction,
                request_options=request_options,
            ),
        )

    async def read_mrr(
        self,
        *,
        at_time: RFC3339DateTime | None = None,
        subscription_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MrrResponse:
        """Returns your site's current MRR, including plan and usage breakouts.

        Args:
            at_time: submit a timestamp in ISO8601 format to request MRR for a historic time.
            subscription_id: submit the id of a subscription in order to limit results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_mrr(
                at_time=at_time, subscription_id=subscription_id, request_options=request_options
            ),
        )

    async def read_site_stats(self, *, request_options: RequestOptionsOrDict | None = None) -> SiteSummary:
        """Returns basic site-level stats. This API call only answers with JSON responses. An XML version is not
        provided.

        ## Stats Documentation

        There currently is not a complimentary matching set of documentation that compliments this endpoint. However,
        each Site's dashboard will reflect the summary of information provided in the Stats response.

        ```
        https://subdomain.chargify.com/dashboard
        ```

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_site_stats(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncInsightsWithRawResponse:
        return self._with_raw_response


class InsightsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_mrr_movements(
        self,
        *,
        subscription_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 10,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMrrResponse, RawError]:
        """Lists your site's MRR movements.

        ## Understanding MRR movements

        This endpoint will aid in accessing your site's `MRR Report
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics>`__ data.

        Whenever a subscription event occurs that causes your site's MRR to change (such as a signup or upgrade), we
        record an MRR movement. These records are accessible via the MRR Movements endpoint.

        Each MRR Movement belongs to a subscription and contains a timestamp, category, and an amount. ``line_items``
        represent the subscription's product configuration at the time of the movement.

        ### Plan & Usage Breakouts

        In the MRR Report UI, we support a setting to `include or exclude
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics#displaying-component-based-metered-usage-in-mrr>`__
        usage revenue. In the MRR APIs, responses include ``plan`` and ``usage`` breakouts.

        Plan includes revenue from:
        * Products
        * Quantity-Based Components
        * On/Off Components

        Usage includes revenue from:
        * Metered Components
        * Prepaid Usage Components

        Args:
            subscription_id: (Optional) Filter results by subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 50; any per_page value over 50 will be changed to 50. Use in query
                ``per_page=20``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/mrr_movements.json"),
            query_params=[
                param[int | None]("subscription_id", subscription_id),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListMrrResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_mrr_per_subscription(
        self,
        *,
        filter_: ListMrrFilter | ListMrrFilterDict | None = None,
        at_time: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionMrrResponse, ListMrrPerSubscriptionErrorBody]:
        """Lists your site's current MRR, including plan and usage breakouts split per subscription.

        Args:
            filter_: Filter to use for List MRR per subscription operation
            at_time: Submit a timestamp in ISO8601 format to request MRR for a historic time. Use in query:
                ``at_time=2022-01-10T10:00:00-05:00``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Records are ordered by subscription_id in
                ascending order by default. Use in query ``direction=desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions_mrr.json"),
            query_params=[
                param[ListMrrFilter | ListMrrFilterDict | None]("filter", filter_),
                param[str | None]("at_time", at_time),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionMrrResponse],
            error_mapper=list_mrr_per_subscription_error_mapper,
            request_options=request_options,
        )

    def read_mrr(
        self,
        *,
        at_time: RFC3339DateTime | None = None,
        subscription_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MrrResponse, RawError]:
        """Returns your site's current MRR, including plan and usage breakouts.

        Args:
            at_time: submit a timestamp in ISO8601 format to request MRR for a historic time.
            subscription_id: submit the id of a subscription in order to limit results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/mrr.json"),
            query_params=[
                param[RFC3339DateTime | None]("at_time", at_time), param[int | None]("subscription_id", subscription_id)
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[MrrResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_site_stats(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteSummary, RawError]:
        """Returns basic site-level stats. This API call only answers with JSON responses. An XML version is not
        provided.

        ## Stats Documentation

        There currently is not a complimentary matching set of documentation that compliments this endpoint. However,
        each Site's dashboard will reflect the summary of information provided in the Stats response.

        ```
        https://subdomain.chargify.com/dashboard
        ```

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/stats.json"),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SiteSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInsightsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_mrr_movements(
        self,
        *,
        subscription_id: int | None = None,
        page: int | None = 1,
        per_page: int | None = 10,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMrrResponse, RawError]:
        """Lists your site's MRR movements.

        ## Understanding MRR movements

        This endpoint will aid in accessing your site's `MRR Report
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics>`__ data.

        Whenever a subscription event occurs that causes your site's MRR to change (such as a signup or upgrade), we
        record an MRR movement. These records are accessible via the MRR Movements endpoint.

        Each MRR Movement belongs to a subscription and contains a timestamp, category, and an amount. ``line_items``
        represent the subscription's product configuration at the time of the movement.

        ### Plan & Usage Breakouts

        In the MRR Report UI, we support a setting to `include or exclude
        <https://maxio.zendesk.com/hc/en-us/articles/24285894587021-MRR-Analytics#displaying-component-based-metered-usage-in-mrr>`__
        usage revenue. In the MRR APIs, responses include ``plan`` and ``usage`` breakouts.

        Plan includes revenue from:
        * Products
        * Quantity-Based Components
        * On/Off Components

        Usage includes revenue from:
        * Metered Components
        * Prepaid Usage Components

        Args:
            subscription_id: (Optional) Filter results by subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 10. The
                maximum allowed values is 50; any per_page value over 50 will be changed to 50. Use in query
                ``per_page=20``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/mrr_movements.json"),
            query_params=[
                param[int | None]("subscription_id", subscription_id),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListMrrResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_mrr_per_subscription(
        self,
        *,
        filter_: ListMrrFilter | ListMrrFilterDict | None = None,
        at_time: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: DirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionMrrResponse, ListMrrPerSubscriptionErrorBody]:
        """Lists your site's current MRR, including plan and usage breakouts split per subscription.

        Args:
            filter_: Filter to use for List MRR per subscription operation
            at_time: Submit a timestamp in ISO8601 format to request MRR for a historic time. Use in query:
                ``at_time=2022-01-10T10:00:00-05:00``.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Records are ordered by subscription_id in
                ascending order by default. Use in query ``direction=desc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions_mrr.json"),
            query_params=[
                param[ListMrrFilter | ListMrrFilterDict | None]("filter", filter_),
                param[str | None]("at_time", at_time),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[DirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionMrrResponse],
            error_mapper=list_mrr_per_subscription_error_mapper,
            request_options=request_options,
        )

    async def read_mrr(
        self,
        *,
        at_time: RFC3339DateTime | None = None,
        subscription_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MrrResponse, RawError]:
        """Returns your site's current MRR, including plan and usage breakouts.

        Args:
            at_time: submit a timestamp in ISO8601 format to request MRR for a historic time.
            subscription_id: submit the id of a subscription in order to limit results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/mrr.json"),
            query_params=[
                param[RFC3339DateTime | None]("at_time", at_time), param[int | None]("subscription_id", subscription_id)
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[MrrResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_site_stats(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteSummary, RawError]:
        """Returns basic site-level stats. This API call only answers with JSON responses. An XML version is not
        provided.

        ## Stats Documentation

        There currently is not a complimentary matching set of documentation that compliments this endpoint. However,
        each Site's dashboard will reflect the summary of information provided in the Stats response.

        ```
        https://subdomain.chargify.com/dashboard
        ```

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/stats.json"),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SiteSummary],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
