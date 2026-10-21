from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_reason_code_error import CreateReasonCodeErrorBody, create_reason_code_error_mapper
from ..errors.delete_reason_code_error import DeleteReasonCodeErrorBody, delete_reason_code_error_mapper
from ..errors.list_reason_codes_error import ListReasonCodesErrorBody, list_reason_codes_error_mapper
from ..errors.read_reason_code_error import ReadReasonCodeErrorBody, read_reason_code_error_mapper
from ..errors.update_reason_code_error import UpdateReasonCodeErrorBody, update_reason_code_error_mapper
from ..models.create_reason_code_request import CreateReasonCodeRequest, CreateReasonCodeRequestDict
from ..models.ok_response import OkResponse
from ..models.reason_code_response import ReasonCodeResponse
from ..models.update_reason_code_request import UpdateReasonCodeRequest, UpdateReasonCodeRequestDict
from ..server.server import Server


class ReasonCodes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReasonCodesWithRawResponse(client, server, auth)

    def create_reason_code(
        self,
        *,
        body: CreateReasonCodeRequest | CreateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReasonCodeResponse:
        """Creates a reason code for a given site.

        Reason Codes are a way to gain a high-level view of why your customers are cancelling the subscription to your
        product or service.

        Add a set of churn reason codes to be displayed in-app and/or the Maxio Billing Portal. As your subscribers
        decide to cancel their subscription, learn why they decided to cancel.

        For more information, see `Churn Reason Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24286647554701-Churn-Reason-Codes>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_reason_code(body=body, request_options=request_options))

    def delete_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> OkResponse:
        """Deletes a reason code from the Churn Reason Codes. This code will be immediately removed. This action is not
        reversible.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_reason_code(reason_code_id, request_options=request_options))

    def list_reason_codes(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> list[ReasonCodeResponse]:
        """Lists all current churn codes for a given site.

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
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_reason_codes(page=page, per_page=per_page, request_options=request_options)
        )

    def read_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReasonCodeResponse:
        """Returns a particular churn reason code for a given site by its unique ID.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_reason_code(reason_code_id, request_options=request_options))

    def update_reason_code(
        self,
        reason_code_id: int,
        *,
        body: UpdateReasonCodeRequest | UpdateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReasonCodeResponse:
        """Updates an existing reason code for a given site.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_reason_code(reason_code_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> ReasonCodesWithRawResponse:
        return self._with_raw_response


class AsyncReasonCodes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReasonCodesWithRawResponse(client, server, auth)

    async def create_reason_code(
        self,
        *,
        body: CreateReasonCodeRequest | CreateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReasonCodeResponse:
        """Creates a reason code for a given site.

        Reason Codes are a way to gain a high-level view of why your customers are cancelling the subscription to your
        product or service.

        Add a set of churn reason codes to be displayed in-app and/or the Maxio Billing Portal. As your subscribers
        decide to cancel their subscription, learn why they decided to cancel.

        For more information, see `Churn Reason Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24286647554701-Churn-Reason-Codes>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_reason_code(body=body, request_options=request_options))

    async def delete_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> OkResponse:
        """Deletes a reason code from the Churn Reason Codes. This code will be immediately removed. This action is not
        reversible.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.delete_reason_code(reason_code_id, request_options=request_options))

    async def list_reason_codes(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> list[ReasonCodeResponse]:
        """Lists all current churn codes for a given site.

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
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_reason_codes(
                page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def read_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReasonCodeResponse:
        """Returns a particular churn reason code for a given site by its unique ID.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.read_reason_code(reason_code_id, request_options=request_options))

    async def update_reason_code(
        self,
        reason_code_id: int,
        *,
        body: UpdateReasonCodeRequest | UpdateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReasonCodeResponse:
        """Updates an existing reason code for a given site.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_reason_code(reason_code_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncReasonCodesWithRawResponse:
        return self._with_raw_response


class ReasonCodesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_reason_code(
        self,
        *,
        body: CreateReasonCodeRequest | CreateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReasonCodeResponse, CreateReasonCodeErrorBody]:
        """Creates a reason code for a given site.

        Reason Codes are a way to gain a high-level view of why your customers are cancelling the subscription to your
        product or service.

        Add a set of churn reason codes to be displayed in-app and/or the Maxio Billing Portal. As your subscribers
        decide to cancel their subscription, learn why they decided to cancel.

        For more information, see `Churn Reason Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24286647554701-Churn-Reason-Codes>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/reason_codes.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReasonCodeRequest | CreateReasonCodeRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ReasonCodeResponse],
            error_mapper=create_reason_code_error_mapper,
            request_options=request_options,
        )

    def delete_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OkResponse, DeleteReasonCodeErrorBody]:
        """Deletes a reason code from the Churn Reason Codes. This code will be immediately removed. This action is not
        reversible.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/reason_codes/{reason_code_id}.json"),
            path_params=[param[int]("reason_code_id", reason_code_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[OkResponse],
            error_mapper=delete_reason_code_error_mapper,
            request_options=request_options,
        )

    def list_reason_codes(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ReasonCodeResponse], ListReasonCodesErrorBody]:
        """Lists all current churn codes for a given site.

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
            url_template=self._server.production("/reason_codes.json"),
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ReasonCodeResponse]],
            error_mapper=list_reason_codes_error_mapper,
            request_options=request_options,
        )

    def read_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReasonCodeResponse, ReadReasonCodeErrorBody]:
        """Returns a particular churn reason code for a given site by its unique ID.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/reason_codes/{reason_code_id}.json"),
            path_params=[param[int]("reason_code_id", reason_code_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ReasonCodeResponse],
            error_mapper=read_reason_code_error_mapper,
            request_options=request_options,
        )

    def update_reason_code(
        self,
        reason_code_id: int,
        *,
        body: UpdateReasonCodeRequest | UpdateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReasonCodeResponse, UpdateReasonCodeErrorBody]:
        """Updates an existing reason code for a given site.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/reason_codes/{reason_code_id}.json"),
            path_params=[param[int]("reason_code_id", reason_code_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateReasonCodeRequest | UpdateReasonCodeRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ReasonCodeResponse],
            error_mapper=update_reason_code_error_mapper,
            request_options=request_options,
        )


class AsyncReasonCodesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_reason_code(
        self,
        *,
        body: CreateReasonCodeRequest | CreateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReasonCodeResponse, CreateReasonCodeErrorBody]:
        """Creates a reason code for a given site.

        Reason Codes are a way to gain a high-level view of why your customers are cancelling the subscription to your
        product or service.

        Add a set of churn reason codes to be displayed in-app and/or the Maxio Billing Portal. As your subscribers
        decide to cancel their subscription, learn why they decided to cancel.

        For more information, see `Churn Reason Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24286647554701-Churn-Reason-Codes>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/reason_codes.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReasonCodeRequest | CreateReasonCodeRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ReasonCodeResponse],
            error_mapper=create_reason_code_error_mapper,
            request_options=request_options,
        )

    async def delete_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OkResponse, DeleteReasonCodeErrorBody]:
        """Deletes a reason code from the Churn Reason Codes. This code will be immediately removed. This action is not
        reversible.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/reason_codes/{reason_code_id}.json"),
            path_params=[param[int]("reason_code_id", reason_code_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[OkResponse],
            error_mapper=delete_reason_code_error_mapper,
            request_options=request_options,
        )

    async def list_reason_codes(
        self, *, page: int | None = 1, per_page: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ReasonCodeResponse], ListReasonCodesErrorBody]:
        """Lists all current churn codes for a given site.

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
            url_template=self._server.production("/reason_codes.json"),
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ReasonCodeResponse]],
            error_mapper=list_reason_codes_error_mapper,
            request_options=request_options,
        )

    async def read_reason_code(
        self, reason_code_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReasonCodeResponse, ReadReasonCodeErrorBody]:
        """Returns a particular churn reason code for a given site by its unique ID.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/reason_codes/{reason_code_id}.json"),
            path_params=[param[int]("reason_code_id", reason_code_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ReasonCodeResponse],
            error_mapper=read_reason_code_error_mapper,
            request_options=request_options,
        )

    async def update_reason_code(
        self,
        reason_code_id: int,
        *,
        body: UpdateReasonCodeRequest | UpdateReasonCodeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReasonCodeResponse, UpdateReasonCodeErrorBody]:
        """Updates an existing reason code for a given site.

        Args:
            reason_code_id: The Advanced Billing id of the reason code
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/reason_codes/{reason_code_id}.json"),
            path_params=[param[int]("reason_code_id", reason_code_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateReasonCodeRequest | UpdateReasonCodeRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ReasonCodeResponse],
            error_mapper=update_reason_code_error_mapper,
            request_options=request_options,
        )
