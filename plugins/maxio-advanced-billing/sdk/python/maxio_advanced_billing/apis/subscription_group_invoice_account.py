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
from ..errors.create_subscription_group_prepayment_error import (
    CreateSubscriptionGroupPrepaymentErrorBody,
    create_subscription_group_prepayment_error_mapper,
)
from ..errors.deduct_subscription_group_service_credit_error import (
    DeductSubscriptionGroupServiceCreditErrorBody,
    deduct_subscription_group_service_credit_error_mapper,
)
from ..errors.issue_subscription_group_service_credit_error import (
    IssueSubscriptionGroupServiceCreditErrorBody,
    issue_subscription_group_service_credit_error_mapper,
)
from ..errors.list_prepayments_for_subscription_group_error import (
    ListPrepaymentsForSubscriptionGroupErrorBody,
    list_prepayments_for_subscription_group_error_mapper,
)
from ..models.deduct_service_credit_request import DeductServiceCreditRequest, DeductServiceCreditRequestDict
from ..models.issue_service_credit_request import IssueServiceCreditRequest, IssueServiceCreditRequestDict
from ..models.list_prepayments_filter import ListPrepaymentsFilter, ListPrepaymentsFilterDict
from ..models.list_subscription_group_prepayment_response import ListSubscriptionGroupPrepaymentResponse
from ..models.service_credit import ServiceCredit
from ..models.service_credit_response import ServiceCreditResponse
from ..models.subscription_group_prepayment_request import (
    SubscriptionGroupPrepaymentRequest,
    SubscriptionGroupPrepaymentRequestDict,
)
from ..models.subscription_group_prepayment_response import SubscriptionGroupPrepaymentResponse
from ..server.server import Server


class SubscriptionGroupInvoiceAccount:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionGroupInvoiceAccountWithRawResponse(client, server, auth)

    def create_subscription_group_prepayment(
        self,
        uid: str,
        *,
        body: SubscriptionGroupPrepaymentRequest | SubscriptionGroupPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupPrepaymentResponse:
        """Adds a prepayment for a subscription group. This endpoint requires an ``amount``, ``details``, ``method``,
        and ``memo``. On success, the prepayment will be added to the group's prepayment balance.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_subscription_group_prepayment(
                uid, body=body, request_options=request_options
            ),
        )

    def deduct_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceCredit:
        """Deducts service credit for a subscription group. Credit will be deducted from the group in the amount
        specified in the request body.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.deduct_subscription_group_service_credit(
                uid, body=body, request_options=request_options
            ),
        )

    def issue_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceCreditResponse:
        """Issues service credit for a subscription group. Credit will be added to the group in the amount specified in
        the request body. The credit will be applied to group member invoices as they are generated.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.issue_subscription_group_service_credit(
                uid, body=body, request_options=request_options
            ),
        )

    def list_prepayments_for_subscription_group(
        self,
        uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionGroupPrepaymentResponse:
        """Lists a subscription group's prepayments.

        Args:
            uid: The uid of the subscription group
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_prepayments_for_subscription_group(
                uid, page=page, per_page=per_page, filter_=filter_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SubscriptionGroupInvoiceAccountWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionGroupInvoiceAccount:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionGroupInvoiceAccountWithRawResponse(client, server, auth)

    async def create_subscription_group_prepayment(
        self,
        uid: str,
        *,
        body: SubscriptionGroupPrepaymentRequest | SubscriptionGroupPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupPrepaymentResponse:
        """Adds a prepayment for a subscription group. This endpoint requires an ``amount``, ``details``, ``method``,
        and ``memo``. On success, the prepayment will be added to the group's prepayment balance.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_subscription_group_prepayment(
                uid, body=body, request_options=request_options
            ),
        )

    async def deduct_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceCredit:
        """Deducts service credit for a subscription group. Credit will be deducted from the group in the amount
        specified in the request body.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.deduct_subscription_group_service_credit(
                uid, body=body, request_options=request_options
            ),
        )

    async def issue_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceCreditResponse:
        """Issues service credit for a subscription group. Credit will be added to the group in the amount specified in
        the request body. The credit will be applied to group member invoices as they are generated.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.issue_subscription_group_service_credit(
                uid, body=body, request_options=request_options
            ),
        )

    async def list_prepayments_for_subscription_group(
        self,
        uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionGroupPrepaymentResponse:
        """Lists a subscription group's prepayments.

        Args:
            uid: The uid of the subscription group
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_prepayments_for_subscription_group(
                uid, page=page, per_page=per_page, filter_=filter_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionGroupInvoiceAccountWithRawResponse:
        return self._with_raw_response


class SubscriptionGroupInvoiceAccountWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_subscription_group_prepayment(
        self,
        uid: str,
        *,
        body: SubscriptionGroupPrepaymentRequest | SubscriptionGroupPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupPrepaymentResponse, CreateSubscriptionGroupPrepaymentErrorBody]:
        """Adds a prepayment for a subscription group. This endpoint requires an ``amount``, ``details``, ``method``,
        and ``memo``. On success, the prepayment will be added to the group's prepayment balance.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/prepayments.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionGroupPrepaymentRequest | SubscriptionGroupPrepaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionGroupPrepaymentResponse],
            error_mapper=create_subscription_group_prepayment_error_mapper,
            request_options=request_options,
        )

    def deduct_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceCredit, DeductSubscriptionGroupServiceCreditErrorBody]:
        """Deducts service credit for a subscription group. Credit will be deducted from the group in the amount
        specified in the request body.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/service_credit_deductions.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeductServiceCreditRequest | DeductServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ServiceCredit],
            error_mapper=deduct_subscription_group_service_credit_error_mapper,
            request_options=request_options,
        )

    def issue_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceCreditResponse, IssueSubscriptionGroupServiceCreditErrorBody]:
        """Issues service credit for a subscription group. Credit will be added to the group in the amount specified in
        the request body. The credit will be applied to group member invoices as they are generated.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/service_credits.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueServiceCreditRequest | IssueServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ServiceCreditResponse],
            error_mapper=issue_subscription_group_service_credit_error_mapper,
            request_options=request_options,
        )

    def list_prepayments_for_subscription_group(
        self,
        uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionGroupPrepaymentResponse, ListPrepaymentsForSubscriptionGroupErrorBody]:
        """Lists a subscription group's prepayments.

        Args:
            uid: The uid of the subscription group
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/{uid}/prepayments.json"),
            path_params=[param[str]("uid", uid)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListPrepaymentsFilter | ListPrepaymentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListSubscriptionGroupPrepaymentResponse],
            error_mapper=list_prepayments_for_subscription_group_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionGroupInvoiceAccountWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_subscription_group_prepayment(
        self,
        uid: str,
        *,
        body: SubscriptionGroupPrepaymentRequest | SubscriptionGroupPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupPrepaymentResponse, CreateSubscriptionGroupPrepaymentErrorBody]:
        """Adds a prepayment for a subscription group. This endpoint requires an ``amount``, ``details``, ``method``,
        and ``memo``. On success, the prepayment will be added to the group's prepayment balance.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/prepayments.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionGroupPrepaymentRequest | SubscriptionGroupPrepaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionGroupPrepaymentResponse],
            error_mapper=create_subscription_group_prepayment_error_mapper,
            request_options=request_options,
        )

    async def deduct_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceCredit, DeductSubscriptionGroupServiceCreditErrorBody]:
        """Deducts service credit for a subscription group. Credit will be deducted from the group in the amount
        specified in the request body.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/service_credit_deductions.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeductServiceCreditRequest | DeductServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ServiceCredit],
            error_mapper=deduct_subscription_group_service_credit_error_mapper,
            request_options=request_options,
        )

    async def issue_subscription_group_service_credit(
        self,
        uid: str,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceCreditResponse, IssueSubscriptionGroupServiceCreditErrorBody]:
        """Issues service credit for a subscription group. Credit will be added to the group in the amount specified in
        the request body. The credit will be applied to group member invoices as they are generated.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/{uid}/service_credits.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueServiceCreditRequest | IssueServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ServiceCreditResponse],
            error_mapper=issue_subscription_group_service_credit_error_mapper,
            request_options=request_options,
        )

    async def list_prepayments_for_subscription_group(
        self,
        uid: str,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionGroupPrepaymentResponse, ListPrepaymentsForSubscriptionGroupErrorBody]:
        """Lists a subscription group's prepayments.

        Args:
            uid: The uid of the subscription group
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/{uid}/prepayments.json"),
            path_params=[param[str]("uid", uid)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListPrepaymentsFilter | ListPrepaymentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListSubscriptionGroupPrepaymentResponse],
            error_mapper=list_prepayments_for_subscription_group_error_mapper,
            request_options=request_options,
        )
