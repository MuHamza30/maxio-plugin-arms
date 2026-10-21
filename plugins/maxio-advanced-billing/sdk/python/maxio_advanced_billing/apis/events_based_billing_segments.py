from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.bulk_create_segments_error import BulkCreateSegmentsErrorBody, bulk_create_segments_error_mapper
from ..errors.bulk_update_segments_error import BulkUpdateSegmentsErrorBody, bulk_update_segments_error_mapper
from ..errors.create_segment_error import CreateSegmentErrorBody, create_segment_error_mapper
from ..errors.delete_segment_error import DeleteSegmentErrorBody, delete_segment_error_mapper
from ..errors.list_segments_for_price_point_error import (
    ListSegmentsForPricePointErrorBody,
    list_segments_for_price_point_error_mapper,
)
from ..errors.update_segment_error import UpdateSegmentErrorBody, update_segment_error_mapper
from ..models.bulk_create_segments import BulkCreateSegments, BulkCreateSegmentsDict
from ..models.bulk_update_segments import BulkUpdateSegments, BulkUpdateSegmentsDict
from ..models.create_segment_request import CreateSegmentRequest, CreateSegmentRequestDict
from ..models.list_segments_filter import ListSegmentsFilter, ListSegmentsFilterDict
from ..models.list_segments_response import ListSegmentsResponse
from ..models.segment_response import SegmentResponse
from ..models.update_segment_request import UpdateSegmentRequest, UpdateSegmentRequestDict
from ..server.server import Server


class EventsBasedBillingSegments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EventsBasedBillingSegmentsWithRawResponse(client, server, auth)

    def bulk_create_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkCreateSegments | BulkCreateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSegmentsResponse:
        """Creates multiple segments in one request. The array of segments can contain up to ``2000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        created. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegment1 | RawError``."""
        return unwrap(
            self._with_raw_response.bulk_create_segments(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    def bulk_update_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkUpdateSegments | BulkUpdateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSegmentsResponse:
        """Updates multiple segments in one request. The array of segments can contain up to ``1000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        updated. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegment1 | RawError``."""
        return unwrap(
            self._with_raw_response.bulk_update_segments(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    def create_segment(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: CreateSegmentRequest | CreateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SegmentResponse:
        """Creates a new segment for a component with a segmented metric. It allows you to specify properties to bill
        upon and prices for each Segment. You can only pass as many "property_values" as the related Metric has
        segmenting properties defined.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegmentErrors1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.create_segment(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    def delete_segment(
        self, component_id: str, price_point_id: str, id_: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a segment with the specified ID.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_segment(component_id, price_point_id, id_, request_options=request_options)
        )

    def list_segments_for_price_point(
        self,
        component_id: str,
        price_point_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListSegmentsFilter | ListSegmentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSegmentsResponse:
        """Lists segments created for a given price point, in order of creation.

        You can pass ``page`` and ``per_page`` parameters in order to access all of the segments. By default it will
        return ``30`` records. You can set ``per_page`` to ``200`` at most.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Segments for a Price Point operation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingListSegmentsErrors1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.list_segments_for_price_point(
                component_id,
                price_point_id,
                page=page,
                per_page=per_page,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    def update_segment(
        self,
        component_id: str,
        price_point_id: str,
        id_: float,
        *,
        body: UpdateSegmentRequest | UpdateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SegmentResponse:
        """Updates a single segment for a component with a segmented metric. You can also update the pricing for the
        segment.

        You can specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegmentErrors1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.update_segment(
                component_id, price_point_id, id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> EventsBasedBillingSegmentsWithRawResponse:
        return self._with_raw_response


class AsyncEventsBasedBillingSegments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEventsBasedBillingSegmentsWithRawResponse(client, server, auth)

    async def bulk_create_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkCreateSegments | BulkCreateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSegmentsResponse:
        """Creates multiple segments in one request. The array of segments can contain up to ``2000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        created. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegment1 | RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_create_segments(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    async def bulk_update_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkUpdateSegments | BulkUpdateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSegmentsResponse:
        """Updates multiple segments in one request. The array of segments can contain up to ``1000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        updated. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegment1 | RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_update_segments(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    async def create_segment(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: CreateSegmentRequest | CreateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SegmentResponse:
        """Creates a new segment for a component with a segmented metric. It allows you to specify properties to bill
        upon and prices for each Segment. You can only pass as many "property_values" as the related Metric has
        segmenting properties defined.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegmentErrors1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.create_segment(
                component_id, price_point_id, body=body, request_options=request_options
            ),
        )

    async def delete_segment(
        self, component_id: str, price_point_id: str, id_: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a segment with the specified ID.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_segment(
                component_id, price_point_id, id_, request_options=request_options
            ),
        )

    async def list_segments_for_price_point(
        self,
        component_id: str,
        price_point_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListSegmentsFilter | ListSegmentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSegmentsResponse:
        """Lists segments created for a given price point, in order of creation.

        You can pass ``page`` and ``per_page`` parameters in order to access all of the segments. By default it will
        return ``30`` records. You can set ``per_page`` to ``200`` at most.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Segments for a Price Point operation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingListSegmentsErrors1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.list_segments_for_price_point(
                component_id,
                price_point_id,
                page=page,
                per_page=per_page,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    async def update_segment(
        self,
        component_id: str,
        price_point_id: str,
        id_: float,
        *,
        body: UpdateSegmentRequest | UpdateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SegmentResponse:
        """Updates a single segment for a component with a segmented metric. You can also update the pricing for the
        segment.

        You can specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``EventBasedBillingSegmentErrors1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_segment(
                component_id, price_point_id, id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncEventsBasedBillingSegmentsWithRawResponse:
        return self._with_raw_response


class EventsBasedBillingSegmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_create_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkCreateSegments | BulkCreateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSegmentsResponse, BulkCreateSegmentsErrorBody]:
        """Creates multiple segments in one request. The array of segments can contain up to ``2000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        created. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/bulk.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateSegments | BulkCreateSegmentsDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListSegmentsResponse],
            error_mapper=bulk_create_segments_error_mapper,
            request_options=request_options,
        )

    def bulk_update_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkUpdateSegments | BulkUpdateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSegmentsResponse, BulkUpdateSegmentsErrorBody]:
        """Updates multiple segments in one request. The array of segments can contain up to ``1000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        updated. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/bulk.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateSegments | BulkUpdateSegmentsDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListSegmentsResponse],
            error_mapper=bulk_update_segments_error_mapper,
            request_options=request_options,
        )

    def create_segment(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: CreateSegmentRequest | CreateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SegmentResponse, CreateSegmentErrorBody]:
        """Creates a new segment for a component with a segmented metric. It allows you to specify properties to bill
        upon and prices for each Segment. You can only pass as many "property_values" as the related Metric has
        segmenting properties defined.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSegmentRequest | CreateSegmentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SegmentResponse],
            error_mapper=create_segment_error_mapper,
            request_options=request_options,
        )

    def delete_segment(
        self, component_id: str, price_point_id: str, id_: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteSegmentErrorBody]:
        """Deletes a segment with the specified ID.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/{id}.json"
            ),
            path_params=[
                param[str]("component_id", component_id),
                param[str]("price_point_id", price_point_id),
                param[float]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_segment_error_mapper,
            request_options=request_options,
        )

    def list_segments_for_price_point(
        self,
        component_id: str,
        price_point_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListSegmentsFilter | ListSegmentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSegmentsResponse, ListSegmentsForPricePointErrorBody]:
        """Lists segments created for a given price point, in order of creation.

        You can pass ``page`` and ``per_page`` parameters in order to access all of the segments. By default it will
        return ``30`` records. You can set ``per_page`` to ``200`` at most.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Segments for a Price Point operation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListSegmentsFilter | ListSegmentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListSegmentsResponse],
            error_mapper=list_segments_for_price_point_error_mapper,
            request_options=request_options,
        )

    def update_segment(
        self,
        component_id: str,
        price_point_id: str,
        id_: float,
        *,
        body: UpdateSegmentRequest | UpdateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SegmentResponse, UpdateSegmentErrorBody]:
        """Updates a single segment for a component with a segmented metric. You can also update the pricing for the
        segment.

        You can specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/{id}.json"
            ),
            path_params=[
                param[str]("component_id", component_id),
                param[str]("price_point_id", price_point_id),
                param[float]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSegmentRequest | UpdateSegmentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SegmentResponse],
            error_mapper=update_segment_error_mapper,
            request_options=request_options,
        )


class AsyncEventsBasedBillingSegmentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_create_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkCreateSegments | BulkCreateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSegmentsResponse, BulkCreateSegmentsErrorBody]:
        """Creates multiple segments in one request. The array of segments can contain up to ``2000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        created. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/bulk.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateSegments | BulkCreateSegmentsDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListSegmentsResponse],
            error_mapper=bulk_create_segments_error_mapper,
            request_options=request_options,
        )

    async def bulk_update_segments(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: BulkUpdateSegments | BulkUpdateSegmentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSegmentsResponse, BulkUpdateSegmentsErrorBody]:
        """Updates multiple segments in one request. The array of segments can contain up to ``1000`` records.

        If any of the records contain an error the whole request would fail and none of the requested segments get
        updated. The error response contains a message for only the one segment that failed validation, with the
        corresponding index in the array.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/bulk.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateSegments | BulkUpdateSegmentsDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListSegmentsResponse],
            error_mapper=bulk_update_segments_error_mapper,
            request_options=request_options,
        )

    async def create_segment(
        self,
        component_id: str,
        price_point_id: str,
        *,
        body: CreateSegmentRequest | CreateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SegmentResponse, CreateSegmentErrorBody]:
        """Creates a new segment for a component with a segmented metric. It allows you to specify properties to bill
        upon and prices for each Segment. You can only pass as many "property_values" as the related Metric has
        segmenting properties defined.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSegmentRequest | CreateSegmentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SegmentResponse],
            error_mapper=create_segment_error_mapper,
            request_options=request_options,
        )

    async def delete_segment(
        self, component_id: str, price_point_id: str, id_: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteSegmentErrorBody]:
        """Deletes a segment with the specified ID.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/{id}.json"
            ),
            path_params=[
                param[str]("component_id", component_id),
                param[str]("price_point_id", price_point_id),
                param[float]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_segment_error_mapper,
            request_options=request_options,
        )

    async def list_segments_for_price_point(
        self,
        component_id: str,
        price_point_id: str,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListSegmentsFilter | ListSegmentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSegmentsResponse, ListSegmentsForPricePointErrorBody]:
        """Lists segments created for a given price point, in order of creation.

        You can pass ``page`` and ``per_page`` parameters in order to access all of the segments. By default it will
        return ``30`` records. You can set ``per_page`` to ``200`` at most.

        You may specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle for the Component
            price_point_id: ID or Handle for the Price Point belonging to the Component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Segments for a Price Point operation
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments.json"
            ),
            path_params=[param[str]("component_id", component_id), param[str]("price_point_id", price_point_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListSegmentsFilter | ListSegmentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListSegmentsResponse],
            error_mapper=list_segments_for_price_point_error_mapper,
            request_options=request_options,
        )

    async def update_segment(
        self,
        component_id: str,
        price_point_id: str,
        id_: float,
        *,
        body: UpdateSegmentRequest | UpdateSegmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SegmentResponse, UpdateSegmentErrorBody]:
        """Updates a single segment for a component with a segmented metric. You can also update the pricing for the
        segment.

        You can specify component and/or price point by using either the numeric ID or the ``handle:gold`` syntax.

        Args:
            component_id: ID or Handle of the Component
            price_point_id: ID or Handle of the Price Point belonging to the Component
            id_: The ID of the Segment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/components/{component_id}/price_points/{price_point_id}/segments/{id}.json"
            ),
            path_params=[
                param[str]("component_id", component_id),
                param[str]("price_point_id", price_point_id),
                param[float]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSegmentRequest | UpdateSegmentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SegmentResponse],
            error_mapper=update_segment_error_mapper,
            request_options=request_options,
        )
