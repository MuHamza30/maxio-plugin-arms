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
from ..errors.create_prepayment_error import CreatePrepaymentErrorBody, create_prepayment_error_mapper
from ..errors.deduct_service_credit_error import DeductServiceCreditErrorBody, deduct_service_credit_error_mapper
from ..errors.issue_service_credit_error import IssueServiceCreditErrorBody, issue_service_credit_error_mapper
from ..errors.list_prepayments_error import ListPrepaymentsErrorBody, list_prepayments_error_mapper
from ..errors.list_service_credits_error import ListServiceCreditsErrorBody, list_service_credits_error_mapper
from ..errors.refund_prepayment_error import RefundPrepaymentErrorBody, refund_prepayment_error_mapper
from ..models.account_balances import AccountBalances
from ..models.create_prepayment_request import CreatePrepaymentRequest, CreatePrepaymentRequestDict
from ..models.create_prepayment_response import CreatePrepaymentResponse
from ..models.deduct_service_credit_request import DeductServiceCreditRequest, DeductServiceCreditRequestDict
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.issue_service_credit_request import IssueServiceCreditRequest, IssueServiceCreditRequestDict
from ..models.list_prepayments_filter import ListPrepaymentsFilter, ListPrepaymentsFilterDict
from ..models.list_service_credits_response import ListServiceCreditsResponse
from ..models.prepayment_response import PrepaymentResponse
from ..models.prepayments_response import PrepaymentsResponse
from ..models.refund_prepayment_request import RefundPrepaymentRequest, RefundPrepaymentRequestDict
from ..models.service_credit import ServiceCredit
from ..server.server import Server


class SubscriptionInvoiceAccount:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionInvoiceAccountWithRawResponse(client, server, auth)

    def create_prepayment(
        self,
        subscription_id: int,
        *,
        body: CreatePrepaymentRequest | CreatePrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePrepaymentResponse:
        """Creates a prepayment for a subscription.

        In order to specify a prepayment made against a subscription, specify the ``amount, memo, details, method``.

        When the ``method`` specified is ``"credit_card_on_file"``, the prepayment amount will be collected using the
        default credit card payment profile and applied to the prepayment account balance. This is especially useful for
        manual replenishment of prepaid subscriptions.

        Note that passing ``amount_in_cents`` is now allowed.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``CreatePrepaymentErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.create_prepayment(subscription_id, body=body, request_options=request_options)
        )

    def deduct_service_credit(
        self,
        subscription_id: int,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deducts a service credit from the subscription in the specified amount. The credit amount being deducted must
        be equal to or less than the current credit balance.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``DeductServiceCreditErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.deduct_service_credit(subscription_id, body=body, request_options=request_options)
        )

    def issue_service_credit(
        self,
        subscription_id: int,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceCredit:
        """Adds a service credit to the subscription in the specified amount. The credit is subsequently applied to the
        next generated invoice.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``IssueServiceCreditErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.issue_service_credit(subscription_id, body=body, request_options=request_options)
        )

    def list_prepayments(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PrepaymentsResponse:
        """Lists a subscription's prepayments.

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
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_prepayments(
                subscription_id, page=page, per_page=per_page, filter_=filter_, request_options=request_options
            ),
        )

    def list_service_credits(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceCreditsResponse:
        """Lists a subscription's service credits.

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
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_service_credits(
                subscription_id, page=page, per_page=per_page, direction=direction, request_options=request_options
            ),
        )

    def read_account_balances(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountBalances:
        """Returns the ``balance_in_cents`` of the Subscription's Pending Discount, Service Credit, and Prepayment
        accounts, as well as the sum of the Subscription's open, payable invoices.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_account_balances(subscription_id, request_options=request_options))

    def refund_prepayment(
        self,
        subscription_id: int,
        prepayment_id: int,
        *,
        body: RefundPrepaymentRequest | RefundPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PrepaymentResponse:
        """Refunds a prepayment applied to a subscription, either fully or partially. The ``prepayment_id`` will be the
        account transaction ID of the original payment. The prepayment must have some amount remaining in order to be
        refunded.

        The amount may be passed either as a decimal, with ``amount``, or an integer in cents, with ``amount_in_cents``.

        Args:
            subscription_id: The Chargify id of the subscription.
            prepayment_id: id of prepayment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Unprocessable Entity ``error`` is ``RefundPrepaymentBaseErrorsResponse1 |
                str | RefundPrepaymentErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.refund_prepayment(
                subscription_id, prepayment_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SubscriptionInvoiceAccountWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionInvoiceAccount:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionInvoiceAccountWithRawResponse(client, server, auth)

    async def create_prepayment(
        self,
        subscription_id: int,
        *,
        body: CreatePrepaymentRequest | CreatePrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePrepaymentResponse:
        """Creates a prepayment for a subscription.

        In order to specify a prepayment made against a subscription, specify the ``amount, memo, details, method``.

        When the ``method`` specified is ``"credit_card_on_file"``, the prepayment amount will be collected using the
        default credit card payment profile and applied to the prepayment account balance. This is especially useful for
        manual replenishment of prepaid subscriptions.

        Note that passing ``amount_in_cents`` is now allowed.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``CreatePrepaymentErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.create_prepayment(subscription_id, body=body, request_options=request_options)
        )

    async def deduct_service_credit(
        self,
        subscription_id: int,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deducts a service credit from the subscription in the specified amount. The credit amount being deducted must
        be equal to or less than the current credit balance.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``DeductServiceCreditErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.deduct_service_credit(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def issue_service_credit(
        self,
        subscription_id: int,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ServiceCredit:
        """Adds a service credit to the subscription in the specified amount. The credit is subsequently applied to the
        next generated invoice.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``IssueServiceCreditErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.issue_service_credit(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def list_prepayments(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PrepaymentsResponse:
        """Lists a subscription's prepayments.

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
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_prepayments(
                subscription_id, page=page, per_page=per_page, filter_=filter_, request_options=request_options
            ),
        )

    async def list_service_credits(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListServiceCreditsResponse:
        """Lists a subscription's service credits.

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
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_service_credits(
                subscription_id, page=page, per_page=per_page, direction=direction, request_options=request_options
            ),
        )

    async def read_account_balances(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountBalances:
        """Returns the ``balance_in_cents`` of the Subscription's Pending Discount, Service Credit, and Prepayment
        accounts, as well as the sum of the Subscription's open, payable invoices.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_account_balances(subscription_id, request_options=request_options)
        )

    async def refund_prepayment(
        self,
        subscription_id: int,
        prepayment_id: int,
        *,
        body: RefundPrepaymentRequest | RefundPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PrepaymentResponse:
        """Refunds a prepayment applied to a subscription, either fully or partially. The ``prepayment_id`` will be the
        account transaction ID of the original payment. The prepayment must have some amount remaining in order to be
        refunded.

        The amount may be passed either as a decimal, with ``amount``, or an integer in cents, with ``amount_in_cents``.

        Args:
            subscription_id: The Chargify id of the subscription.
            prepayment_id: id of prepayment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Bad Request Not Found Unprocessable Entity ``error`` is ``RefundPrepaymentBaseErrorsResponse1 |
                str | RefundPrepaymentErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.refund_prepayment(
                subscription_id, prepayment_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionInvoiceAccountWithRawResponse:
        return self._with_raw_response


class SubscriptionInvoiceAccountWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_prepayment(
        self,
        subscription_id: int,
        *,
        body: CreatePrepaymentRequest | CreatePrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePrepaymentResponse, CreatePrepaymentErrorBody]:
        """Creates a prepayment for a subscription.

        In order to specify a prepayment made against a subscription, specify the ``amount, memo, details, method``.

        When the ``method`` specified is ``"credit_card_on_file"``, the prepayment amount will be collected using the
        default credit card payment profile and applied to the prepayment account balance. This is especially useful for
        manual replenishment of prepaid subscriptions.

        Note that passing ``amount_in_cents`` is now allowed.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/prepayments.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePrepaymentRequest | CreatePrepaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CreatePrepaymentResponse],
            error_mapper=create_prepayment_error_mapper,
            request_options=request_options,
        )

    def deduct_service_credit(
        self,
        subscription_id: int,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeductServiceCreditErrorBody]:
        """Deducts a service credit from the subscription in the specified amount. The credit amount being deducted must
        be equal to or less than the current credit balance.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/service_credit_deductions.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeductServiceCreditRequest | DeductServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=deduct_service_credit_error_mapper,
            request_options=request_options,
        )

    def issue_service_credit(
        self,
        subscription_id: int,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceCredit, IssueServiceCreditErrorBody]:
        """Adds a service credit to the subscription in the specified amount. The credit is subsequently applied to the
        next generated invoice.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/service_credits.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueServiceCreditRequest | IssueServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ServiceCredit],
            error_mapper=issue_service_credit_error_mapper,
            request_options=request_options,
        )

    def list_prepayments(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PrepaymentsResponse, ListPrepaymentsErrorBody]:
        """Lists a subscription's prepayments.

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
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/prepayments.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListPrepaymentsFilter | ListPrepaymentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PrepaymentsResponse],
            error_mapper=list_prepayments_error_mapper,
            request_options=request_options,
        )

    def list_service_credits(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceCreditsResponse, ListServiceCreditsErrorBody]:
        """Lists a subscription's service credits.

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
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/service_credits/list.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListServiceCreditsResponse],
            error_mapper=list_service_credits_error_mapper,
            request_options=request_options,
        )

    def read_account_balances(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountBalances, RawError]:
        """Returns the ``balance_in_cents`` of the Subscription's Pending Discount, Service Credit, and Prepayment
        accounts, as well as the sum of the Subscription's open, payable invoices.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/account_balances.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[AccountBalances],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def refund_prepayment(
        self,
        subscription_id: int,
        prepayment_id: int,
        *,
        body: RefundPrepaymentRequest | RefundPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PrepaymentResponse, RefundPrepaymentErrorBody]:
        """Refunds a prepayment applied to a subscription, either fully or partially. The ``prepayment_id`` will be the
        account transaction ID of the original payment. The prepayment must have some amount remaining in order to be
        refunded.

        The amount may be passed either as a decimal, with ``amount``, or an integer in cents, with ``amount_in_cents``.

        Args:
            subscription_id: The Chargify id of the subscription.
            prepayment_id: id of prepayment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/prepayments/{prepayment_id}/refunds.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("prepayment_id", prepayment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundPrepaymentRequest | RefundPrepaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PrepaymentResponse],
            error_mapper=refund_prepayment_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionInvoiceAccountWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_prepayment(
        self,
        subscription_id: int,
        *,
        body: CreatePrepaymentRequest | CreatePrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePrepaymentResponse, CreatePrepaymentErrorBody]:
        """Creates a prepayment for a subscription.

        In order to specify a prepayment made against a subscription, specify the ``amount, memo, details, method``.

        When the ``method`` specified is ``"credit_card_on_file"``, the prepayment amount will be collected using the
        default credit card payment profile and applied to the prepayment account balance. This is especially useful for
        manual replenishment of prepaid subscriptions.

        Note that passing ``amount_in_cents`` is now allowed.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/prepayments.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePrepaymentRequest | CreatePrepaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CreatePrepaymentResponse],
            error_mapper=create_prepayment_error_mapper,
            request_options=request_options,
        )

    async def deduct_service_credit(
        self,
        subscription_id: int,
        *,
        body: DeductServiceCreditRequest | DeductServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeductServiceCreditErrorBody]:
        """Deducts a service credit from the subscription in the specified amount. The credit amount being deducted must
        be equal to or less than the current credit balance.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/service_credit_deductions.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeductServiceCreditRequest | DeductServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=deduct_service_credit_error_mapper,
            request_options=request_options,
        )

    async def issue_service_credit(
        self,
        subscription_id: int,
        *,
        body: IssueServiceCreditRequest | IssueServiceCreditRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ServiceCredit, IssueServiceCreditErrorBody]:
        """Adds a service credit to the subscription in the specified amount. The credit is subsequently applied to the
        next generated invoice.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/service_credits.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IssueServiceCreditRequest | IssueServiceCreditRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ServiceCredit],
            error_mapper=issue_service_credit_error_mapper,
            request_options=request_options,
        )

    async def list_prepayments(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListPrepaymentsFilter | ListPrepaymentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PrepaymentsResponse, ListPrepaymentsErrorBody]:
        """Lists a subscription's prepayments.

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
            filter_: Filter to use for List Prepayments operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/prepayments.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListPrepaymentsFilter | ListPrepaymentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PrepaymentsResponse],
            error_mapper=list_prepayments_error_mapper,
            request_options=request_options,
        )

    async def list_service_credits(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListServiceCreditsResponse, ListServiceCreditsErrorBody]:
        """Lists a subscription's service credits.

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
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/service_credits/list.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListServiceCreditsResponse],
            error_mapper=list_service_credits_error_mapper,
            request_options=request_options,
        )

    async def read_account_balances(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountBalances, RawError]:
        """Returns the ``balance_in_cents`` of the Subscription's Pending Discount, Service Credit, and Prepayment
        accounts, as well as the sum of the Subscription's open, payable invoices.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/account_balances.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[AccountBalances],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def refund_prepayment(
        self,
        subscription_id: int,
        prepayment_id: int,
        *,
        body: RefundPrepaymentRequest | RefundPrepaymentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PrepaymentResponse, RefundPrepaymentErrorBody]:
        """Refunds a prepayment applied to a subscription, either fully or partially. The ``prepayment_id`` will be the
        account transaction ID of the original payment. The prepayment must have some amount remaining in order to be
        refunded.

        The amount may be passed either as a decimal, with ``amount``, or an integer in cents, with ``amount_in_cents``.

        Args:
            subscription_id: The Chargify id of the subscription.
            prepayment_id: id of prepayment
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/prepayments/{prepayment_id}/refunds.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("prepayment_id", prepayment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundPrepaymentRequest | RefundPrepaymentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PrepaymentResponse],
            error_mapper=refund_prepayment_error_mapper,
            request_options=request_options,
        )
