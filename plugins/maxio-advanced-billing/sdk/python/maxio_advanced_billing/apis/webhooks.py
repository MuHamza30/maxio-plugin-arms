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
from ..errors.create_endpoint_error import CreateEndpointErrorBody, create_endpoint_error_mapper
from ..errors.update_endpoint_error import UpdateEndpointErrorBody, update_endpoint_error_mapper
from ..models.create_or_update_endpoint_request import CreateOrUpdateEndpointRequest, CreateOrUpdateEndpointRequestDict
from ..models.enable_webhooks_request import EnableWebhooksRequest, EnableWebhooksRequestDict
from ..models.enable_webhooks_response import EnableWebhooksResponse
from ..models.endpoint import Endpoint
from ..models.endpoint_response import EndpointResponse
from ..models.enums.webhook_order import WebhookOrderOrStr
from ..models.enums.webhook_status import WebhookStatusOrStr
from ..models.replay_webhooks_request import ReplayWebhooksRequest, ReplayWebhooksRequestDict
from ..models.replay_webhooks_response import ReplayWebhooksResponse
from ..models.webhook_response import WebhookResponse
from ..server.server import Server


class Webhooks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WebhooksWithRawResponse(client, server, auth)

    def create_endpoint(
        self,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EndpointResponse:
        """Creates an endpoint and assigns a list of webhook subscriptions (events) to it. See the `Webhooks Reference
        <page:introduction/webhooks/webhooks-reference#events>`__ page for available events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_endpoint(body=body, request_options=request_options))

    def enable_webhooks(
        self,
        *,
        body: EnableWebhooksRequest | EnableWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EnableWebhooksResponse:
        """Enables webhooks for your site.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.enable_webhooks(body=body, request_options=request_options))

    def list_endpoints(self, *, request_options: RequestOptionsOrDict | None = None) -> list[Endpoint]:
        """Lists endpoints configured for a site.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.list_endpoints(request_options=request_options))

    def list_webhooks(
        self,
        *,
        status: WebhookStatusOrStr | None = None,
        since_date: str | None = None,
        until_date: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        order: WebhookOrderOrStr | None = None,
        subscription: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[WebhookResponse]:
        """Retrieves a list of webhooks. You can pass query parameters if you want to filter webhooks. See the `Webhooks
        <page:introduction/webhooks/webhooks>`__ documentation for more information.

        Args:
            status: Webhooks with matching status would be returned.
            since_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date greater than or equal to the one
                specified.
            until_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date less than or equal to the one
                specified.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            order: The order in which the Webhooks are returned.
            subscription: The Advanced Billing id of a subscription you'd like to filter for
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_webhooks(
                status=status,
                since_date=since_date,
                until_date=until_date,
                page=page,
                per_page=per_page,
                order=order,
                subscription=subscription,
                request_options=request_options,
            ),
        )

    def replay_webhooks(
        self,
        *,
        body: ReplayWebhooksRequest | ReplayWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReplayWebhooksResponse:
        """Replays webhooks. Posting to this endpoint does not immediately resend the webhooks. They are added to a
        queue and sent as soon as possible, depending on available system resources. You can submit an array of up to
        1000 webhook IDs in the replay request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.replay_webhooks(body=body, request_options=request_options))

    def update_endpoint(
        self,
        endpoint_id: int,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EndpointResponse:
        """Updates an Endpoint. You can change the ``url`` of your endpoint or the list of ``webhook_subscriptions`` to
        which you are subscribed. See the `Webhooks Reference <page:introduction/webhooks/webhooks-reference#events>`__
        page for available events.

        Always send a complete list of events to which you want to subscribe. Sending a PUT request for an existing
        endpoint with an empty list of ``webhook_subscriptions`` will unsubscribe all events.

        If you want to unsubscribe from a specific event, send a list of ``webhook_subscriptions`` without the specific
        event key.

        Args:
            endpoint_id: The Advanced Billing id for the endpoint that should be updated
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.update_endpoint(endpoint_id, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> WebhooksWithRawResponse:
        return self._with_raw_response


class AsyncWebhooks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWebhooksWithRawResponse(client, server, auth)

    async def create_endpoint(
        self,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EndpointResponse:
        """Creates an endpoint and assigns a list of webhook subscriptions (events) to it. See the `Webhooks Reference
        <page:introduction/webhooks/webhooks-reference#events>`__ page for available events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_endpoint(body=body, request_options=request_options))

    async def enable_webhooks(
        self,
        *,
        body: EnableWebhooksRequest | EnableWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EnableWebhooksResponse:
        """Enables webhooks for your site.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.enable_webhooks(body=body, request_options=request_options))

    async def list_endpoints(self, *, request_options: RequestOptionsOrDict | None = None) -> list[Endpoint]:
        """Lists endpoints configured for a site.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.list_endpoints(request_options=request_options))

    async def list_webhooks(
        self,
        *,
        status: WebhookStatusOrStr | None = None,
        since_date: str | None = None,
        until_date: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        order: WebhookOrderOrStr | None = None,
        subscription: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[WebhookResponse]:
        """Retrieves a list of webhooks. You can pass query parameters if you want to filter webhooks. See the `Webhooks
        <page:introduction/webhooks/webhooks>`__ documentation for more information.

        Args:
            status: Webhooks with matching status would be returned.
            since_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date greater than or equal to the one
                specified.
            until_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date less than or equal to the one
                specified.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            order: The order in which the Webhooks are returned.
            subscription: The Advanced Billing id of a subscription you'd like to filter for
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_webhooks(
                status=status,
                since_date=since_date,
                until_date=until_date,
                page=page,
                per_page=per_page,
                order=order,
                subscription=subscription,
                request_options=request_options,
            ),
        )

    async def replay_webhooks(
        self,
        *,
        body: ReplayWebhooksRequest | ReplayWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReplayWebhooksResponse:
        """Replays webhooks. Posting to this endpoint does not immediately resend the webhooks. They are added to a
        queue and sent as soon as possible, depending on available system resources. You can submit an array of up to
        1000 webhook IDs in the replay request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.replay_webhooks(body=body, request_options=request_options))

    async def update_endpoint(
        self,
        endpoint_id: int,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EndpointResponse:
        """Updates an Endpoint. You can change the ``url`` of your endpoint or the list of ``webhook_subscriptions`` to
        which you are subscribed. See the `Webhooks Reference <page:introduction/webhooks/webhooks-reference#events>`__
        page for available events.

        Always send a complete list of events to which you want to subscribe. Sending a PUT request for an existing
        endpoint with an empty list of ``webhook_subscriptions`` will unsubscribe all events.

        If you want to unsubscribe from a specific event, send a list of ``webhook_subscriptions`` without the specific
        event key.

        Args:
            endpoint_id: The Advanced Billing id for the endpoint that should be updated
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_endpoint(endpoint_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncWebhooksWithRawResponse:
        return self._with_raw_response


class WebhooksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_endpoint(
        self,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EndpointResponse, CreateEndpointErrorBody]:
        """Creates an endpoint and assigns a list of webhook subscriptions (events) to it. See the `Webhooks Reference
        <page:introduction/webhooks/webhooks-reference#events>`__ page for available events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/endpoints.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[EndpointResponse],
            error_mapper=create_endpoint_error_mapper,
            request_options=request_options,
        )

    def enable_webhooks(
        self,
        *,
        body: EnableWebhooksRequest | EnableWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EnableWebhooksResponse, RawError]:
        """Enables webhooks for your site.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/webhooks/settings.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EnableWebhooksRequest | EnableWebhooksRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[EnableWebhooksResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_endpoints(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Endpoint], RawError]:
        """Lists endpoints configured for a site.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/endpoints.json"),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[Endpoint]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_webhooks(
        self,
        *,
        status: WebhookStatusOrStr | None = None,
        since_date: str | None = None,
        until_date: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        order: WebhookOrderOrStr | None = None,
        subscription: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[WebhookResponse], RawError]:
        """Retrieves a list of webhooks. You can pass query parameters if you want to filter webhooks. See the `Webhooks
        <page:introduction/webhooks/webhooks>`__ documentation for more information.

        Args:
            status: Webhooks with matching status would be returned.
            since_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date greater than or equal to the one
                specified.
            until_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date less than or equal to the one
                specified.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            order: The order in which the Webhooks are returned.
            subscription: The Advanced Billing id of a subscription you'd like to filter for
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/webhooks.json"),
            query_params=[
                param[WebhookStatusOrStr | None]("status", status),
                param[str | None]("since_date", since_date),
                param[str | None]("until_date", until_date),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[WebhookOrderOrStr | None]("order", order),
                param[int | None]("subscription", subscription),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[WebhookResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def replay_webhooks(
        self,
        *,
        body: ReplayWebhooksRequest | ReplayWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReplayWebhooksResponse, RawError]:
        """Replays webhooks. Posting to this endpoint does not immediately resend the webhooks. They are added to a
        queue and sent as soon as possible, depending on available system resources. You can submit an array of up to
        1000 webhook IDs in the replay request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/webhooks/replay.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReplayWebhooksRequest | ReplayWebhooksRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ReplayWebhooksResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_endpoint(
        self,
        endpoint_id: int,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EndpointResponse, UpdateEndpointErrorBody]:
        """Updates an Endpoint. You can change the ``url`` of your endpoint or the list of ``webhook_subscriptions`` to
        which you are subscribed. See the `Webhooks Reference <page:introduction/webhooks/webhooks-reference#events>`__
        page for available events.

        Always send a complete list of events to which you want to subscribe. Sending a PUT request for an existing
        endpoint with an empty list of ``webhook_subscriptions`` will unsubscribe all events.

        If you want to unsubscribe from a specific event, send a list of ``webhook_subscriptions`` without the specific
        event key.

        Args:
            endpoint_id: The Advanced Billing id for the endpoint that should be updated
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/endpoints/{endpoint_id}.json"),
            path_params=[param[int]("endpoint_id", endpoint_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[EndpointResponse],
            error_mapper=update_endpoint_error_mapper,
            request_options=request_options,
        )


class AsyncWebhooksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_endpoint(
        self,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EndpointResponse, CreateEndpointErrorBody]:
        """Creates an endpoint and assigns a list of webhook subscriptions (events) to it. See the `Webhooks Reference
        <page:introduction/webhooks/webhooks-reference#events>`__ page for available events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/endpoints.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[EndpointResponse],
            error_mapper=create_endpoint_error_mapper,
            request_options=request_options,
        )

    async def enable_webhooks(
        self,
        *,
        body: EnableWebhooksRequest | EnableWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EnableWebhooksResponse, RawError]:
        """Enables webhooks for your site.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/webhooks/settings.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EnableWebhooksRequest | EnableWebhooksRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[EnableWebhooksResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_endpoints(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Endpoint], RawError]:
        """Lists endpoints configured for a site.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/endpoints.json"),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[Endpoint]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_webhooks(
        self,
        *,
        status: WebhookStatusOrStr | None = None,
        since_date: str | None = None,
        until_date: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        order: WebhookOrderOrStr | None = None,
        subscription: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[WebhookResponse], RawError]:
        """Retrieves a list of webhooks. You can pass query parameters if you want to filter webhooks. See the `Webhooks
        <page:introduction/webhooks/webhooks>`__ documentation for more information.

        Args:
            status: Webhooks with matching status would be returned.
            since_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date greater than or equal to the one
                specified.
            until_date: Format YYYY-MM-DD. Returns Webhooks with the created_at date less than or equal to the one
                specified.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            order: The order in which the Webhooks are returned.
            subscription: The Advanced Billing id of a subscription you'd like to filter for
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/webhooks.json"),
            query_params=[
                param[WebhookStatusOrStr | None]("status", status),
                param[str | None]("since_date", since_date),
                param[str | None]("until_date", until_date),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[WebhookOrderOrStr | None]("order", order),
                param[int | None]("subscription", subscription),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[WebhookResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def replay_webhooks(
        self,
        *,
        body: ReplayWebhooksRequest | ReplayWebhooksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReplayWebhooksResponse, RawError]:
        """Replays webhooks. Posting to this endpoint does not immediately resend the webhooks. They are added to a
        queue and sent as soon as possible, depending on available system resources. You can submit an array of up to
        1000 webhook IDs in the replay request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/webhooks/replay.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReplayWebhooksRequest | ReplayWebhooksRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ReplayWebhooksResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_endpoint(
        self,
        endpoint_id: int,
        *,
        body: CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EndpointResponse, UpdateEndpointErrorBody]:
        """Updates an Endpoint. You can change the ``url`` of your endpoint or the list of ``webhook_subscriptions`` to
        which you are subscribed. See the `Webhooks Reference <page:introduction/webhooks/webhooks-reference#events>`__
        page for available events.

        Always send a complete list of events to which you want to subscribe. Sending a PUT request for an existing
        endpoint with an empty list of ``webhook_subscriptions`` will unsubscribe all events.

        If you want to unsubscribe from a specific event, send a list of ``webhook_subscriptions`` without the specific
        event key.

        Args:
            endpoint_id: The Advanced Billing id for the endpoint that should be updated
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/endpoints/{endpoint_id}.json"),
            path_params=[param[int]("endpoint_id", endpoint_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrUpdateEndpointRequest | CreateOrUpdateEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[EndpointResponse],
            error_mapper=update_endpoint_error_mapper,
            request_options=request_options,
        )
