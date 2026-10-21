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
from ..errors.create_subscription_note_error import (
    CreateSubscriptionNoteErrorBody,
    create_subscription_note_error_mapper,
)
from ..errors.list_subscription_notes_error import ListSubscriptionNotesErrorBody, list_subscription_notes_error_mapper
from ..errors.update_subscription_note_error import (
    UpdateSubscriptionNoteErrorBody,
    update_subscription_note_error_mapper,
)
from ..models.subscription_note_response import SubscriptionNoteResponse
from ..models.update_subscription_note_request import UpdateSubscriptionNoteRequest, UpdateSubscriptionNoteRequestDict
from ..server.server import Server


class SubscriptionNotes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionNotesWithRawResponse(client, server, auth)

    def create_subscription_note(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionNoteResponse:
        """Creates a note for a subscription.

        Notes allow you to record information about a particular Subscription in a free text format.

        If you have structured data such as birth date, color, etc., consider using `Metadata
        <$e/Custom%20Fields/createMetadata>`__ instead.

        For more information, see `Adding Notes
        <https://docs.maxio.com/hc/en-us/articles/24251654953997-Understanding-the-Subscription-Summary-Page#billing-portal-status:~:text=documentation%20for%20more.-,Adding%20Notes,-Notes%20are%20optional>`__
        in the product documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_subscription_note(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def delete_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a note for a Subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_subscription_note(subscription_id, note_id, request_options=request_options)
        )

    def list_subscription_notes(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SubscriptionNoteResponse]:
        """Retrieves a list of notes associated with a subscription. The response will be an array of Notes.

        Args:
            subscription_id: The Chargify id of the subscription.
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
            self._with_raw_response.list_subscription_notes(
                subscription_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    def read_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionNoteResponse:
        """Retrieves a specific note attached to a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_subscription_note(subscription_id, note_id, request_options=request_options)
        )

    def update_subscription_note(
        self,
        subscription_id: int,
        note_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionNoteResponse:
        """Updates a note for a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_subscription_note(
                subscription_id, note_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SubscriptionNotesWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionNotes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionNotesWithRawResponse(client, server, auth)

    async def create_subscription_note(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionNoteResponse:
        """Creates a note for a subscription.

        Notes allow you to record information about a particular Subscription in a free text format.

        If you have structured data such as birth date, color, etc., consider using `Metadata
        <$e/Custom%20Fields/createMetadata>`__ instead.

        For more information, see `Adding Notes
        <https://docs.maxio.com/hc/en-us/articles/24251654953997-Understanding-the-Subscription-Summary-Page#billing-portal-status:~:text=documentation%20for%20more.-,Adding%20Notes,-Notes%20are%20optional>`__
        in the product documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_subscription_note(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def delete_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a note for a Subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_subscription_note(
                subscription_id, note_id, request_options=request_options
            ),
        )

    async def list_subscription_notes(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SubscriptionNoteResponse]:
        """Retrieves a list of notes associated with a subscription. The response will be an array of Notes.

        Args:
            subscription_id: The Chargify id of the subscription.
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
            await self._with_raw_response.list_subscription_notes(
                subscription_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def read_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionNoteResponse:
        """Retrieves a specific note attached to a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_subscription_note(
                subscription_id, note_id, request_options=request_options
            ),
        )

    async def update_subscription_note(
        self,
        subscription_id: int,
        note_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionNoteResponse:
        """Updates a note for a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_subscription_note(
                subscription_id, note_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionNotesWithRawResponse:
        return self._with_raw_response


class SubscriptionNotesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_subscription_note(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionNoteResponse, CreateSubscriptionNoteErrorBody]:
        """Creates a note for a subscription.

        Notes allow you to record information about a particular Subscription in a free text format.

        If you have structured data such as birth date, color, etc., consider using `Metadata
        <$e/Custom%20Fields/createMetadata>`__ instead.

        For more information, see `Adding Notes
        <https://docs.maxio.com/hc/en-us/articles/24251654953997-Understanding-the-Subscription-Summary-Page#billing-portal-status:~:text=documentation%20for%20more.-,Adding%20Notes,-Notes%20are%20optional>`__
        in the product documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionNoteResponse],
            error_mapper=create_subscription_note_error_mapper,
            request_options=request_options,
        )

    def delete_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a note for a Subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("note_id", note_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_subscription_notes(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SubscriptionNoteResponse], ListSubscriptionNotesErrorBody]:
        """Retrieves a list of notes associated with a subscription. The response will be an array of Notes.

        Args:
            subscription_id: The Chargify id of the subscription.
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
            url_template=self._server.production("/subscriptions/{subscription_id}/notes.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[SubscriptionNoteResponse]],
            error_mapper=list_subscription_notes_error_mapper,
            request_options=request_options,
        )

    def read_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionNoteResponse, RawError]:
        """Retrieves a specific note attached to a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("note_id", note_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionNoteResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_subscription_note(
        self,
        subscription_id: int,
        note_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionNoteResponse, UpdateSubscriptionNoteErrorBody]:
        """Updates a note for a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("note_id", note_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionNoteResponse],
            error_mapper=update_subscription_note_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionNotesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_subscription_note(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionNoteResponse, CreateSubscriptionNoteErrorBody]:
        """Creates a note for a subscription.

        Notes allow you to record information about a particular Subscription in a free text format.

        If you have structured data such as birth date, color, etc., consider using `Metadata
        <$e/Custom%20Fields/createMetadata>`__ instead.

        For more information, see `Adding Notes
        <https://docs.maxio.com/hc/en-us/articles/24251654953997-Understanding-the-Subscription-Summary-Page#billing-portal-status:~:text=documentation%20for%20more.-,Adding%20Notes,-Notes%20are%20optional>`__
        in the product documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionNoteResponse],
            error_mapper=create_subscription_note_error_mapper,
            request_options=request_options,
        )

    async def delete_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a note for a Subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("note_id", note_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_subscription_notes(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SubscriptionNoteResponse], ListSubscriptionNotesErrorBody]:
        """Retrieves a list of notes associated with a subscription. The response will be an array of Notes.

        Args:
            subscription_id: The Chargify id of the subscription.
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
            url_template=self._server.production("/subscriptions/{subscription_id}/notes.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[SubscriptionNoteResponse]],
            error_mapper=list_subscription_notes_error_mapper,
            request_options=request_options,
        )

    async def read_subscription_note(
        self, subscription_id: int, note_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionNoteResponse, RawError]:
        """Retrieves a specific note attached to a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("note_id", note_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionNoteResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_subscription_note(
        self,
        subscription_id: int,
        note_id: int,
        *,
        body: UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionNoteResponse, UpdateSubscriptionNoteErrorBody]:
        """Updates a note for a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            note_id: The Advanced Billing id of the note
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/notes/{note_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("note_id", note_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionNoteRequest | UpdateSubscriptionNoteRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionNoteResponse],
            error_mapper=update_subscription_note_error_mapper,
            request_options=request_options,
        )
