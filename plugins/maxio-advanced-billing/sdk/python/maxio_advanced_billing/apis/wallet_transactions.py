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
from ..errors.create_wallet_transaction_error import (
    CreateWalletTransactionErrorBody,
    create_wallet_transaction_error_mapper,
)
from ..errors.list_wallet_transactions_error import (
    ListWalletTransactionsErrorBody,
    list_wallet_transactions_error_mapper,
)
from ..models.create_wallet_transaction_request import (
    CreateWalletTransactionRequest,
    CreateWalletTransactionRequestDict,
)
from ..models.wallet_transaction_result_response import WalletTransactionResultResponse
from ..models.wallet_transactions_list_response import WalletTransactionsListResponse
from ..server.server import Server


class WalletTransactions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WalletTransactionsWithRawResponse(client, server, auth)

    def create_wallet_transaction(
        self,
        wallet_id: int,
        *,
        body: CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletTransactionResultResponse:
        """Grants units to the wallet, or debits units from it, depending on ``kind``. ``amount`` is always sent
        positive, and ``kind`` determines the direction written to the ledger.

        **``kind: grant``**: a one-time manual top-up. On a non-negative balance, this creates a grant and writes one
        ledger row. On a negative balance, it repays the overdraft first (a ``kind: grant`` row with ``grant_id: null``,
        for the repaid amount), then creates the grant: its ``original`` is always the full ``amount`` sent, and its
        ``remaining`` is what's left after the overdraft was repaid, which is ``0`` if the overdraft absorbed the whole
        top-up. The grant row is still written, and its ``amount`` is that ``remaining``, not ``original``, so the
        ledger rows sum to the balance change. A grant may carry ``expires_at``; a debit may not.

        **``kind: debit``**: direct consumption. Drains grants earliest-expiration-first, one ``kind: debit`` row per
        grant touched, plus any overdue expiration rows this same call triggers first (see below):
        - Under the wallet's default ``hard_stop_overflow: discard``, the drain is capped at the available balance. For
            a metered wallet, that cap is the live metered balance, not the stored one, so a debit can drain less than
            its stored balance would suggest, or even drain nothing at all (``201`` with ``drained_amount: "0.0"``) if
            live usage has already consumed what the ledger hadn't caught up to yet. A debit against a wallet whose
            *stored* balance is already zero or negative (``discard`` only ever reaches zero) returns ``422 "Wallet is
            depleted"``. Before that failure is returned, this call still expires any grants that were already overdue,
            so a ``422`` response can still leave new ``kind: expiration`` rows written.
        - Under ``hard_stop_overflow: allow_negative``, the full amount is deducted. The excess past the wallet's grants
            is booked as one overdraft row with ``grant_id: null``, ``rejected_amount`` is always ``"0.0"``, and the
            balance goes negative.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Transaction applied. For ``kind: grant``, the ledger row(s) written plus the new balance. For ``kind:
            debit``, one row per grant touched plus the requested/drained/rejected accounting and the new balance.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Includes an unrecognized
                ``kind``, a missing ``wallet_transaction`` root, a malformed, non-positive, or out-of-range ``amount``,
                a memo over 255 characters, ``expires_at`` sent with ``kind: debit``, a malformed or past-dated
                ``expires_at``, an archived wallet, and, for ``kind: debit`` only, a depleted wallet. For a metered
                wallet, usage could be read but settling it against the ledger failed. For a metered wallet, live usage
                could not be read in time to compute the debit. Not returned for ``kind: grant``. ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_wallet_transaction(wallet_id, body=body, request_options=request_options)
        )

    def list_wallet_transactions(
        self,
        wallet_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletTransactionsListResponse:
        """Lists the wallet's append-only ledger, newest first, paginated.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
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
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.list_wallet_transactions(
                wallet_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> WalletTransactionsWithRawResponse:
        return self._with_raw_response


class AsyncWalletTransactions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWalletTransactionsWithRawResponse(client, server, auth)

    async def create_wallet_transaction(
        self,
        wallet_id: int,
        *,
        body: CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletTransactionResultResponse:
        """Grants units to the wallet, or debits units from it, depending on ``kind``. ``amount`` is always sent
        positive, and ``kind`` determines the direction written to the ledger.

        **``kind: grant``**: a one-time manual top-up. On a non-negative balance, this creates a grant and writes one
        ledger row. On a negative balance, it repays the overdraft first (a ``kind: grant`` row with ``grant_id: null``,
        for the repaid amount), then creates the grant: its ``original`` is always the full ``amount`` sent, and its
        ``remaining`` is what's left after the overdraft was repaid, which is ``0`` if the overdraft absorbed the whole
        top-up. The grant row is still written, and its ``amount`` is that ``remaining``, not ``original``, so the
        ledger rows sum to the balance change. A grant may carry ``expires_at``; a debit may not.

        **``kind: debit``**: direct consumption. Drains grants earliest-expiration-first, one ``kind: debit`` row per
        grant touched, plus any overdue expiration rows this same call triggers first (see below):
        - Under the wallet's default ``hard_stop_overflow: discard``, the drain is capped at the available balance. For
            a metered wallet, that cap is the live metered balance, not the stored one, so a debit can drain less than
            its stored balance would suggest, or even drain nothing at all (``201`` with ``drained_amount: "0.0"``) if
            live usage has already consumed what the ledger hadn't caught up to yet. A debit against a wallet whose
            *stored* balance is already zero or negative (``discard`` only ever reaches zero) returns ``422 "Wallet is
            depleted"``. Before that failure is returned, this call still expires any grants that were already overdue,
            so a ``422`` response can still leave new ``kind: expiration`` rows written.
        - Under ``hard_stop_overflow: allow_negative``, the full amount is deducted. The excess past the wallet's grants
            is booked as one overdraft row with ``grant_id: null``, ``rejected_amount`` is always ``"0.0"``, and the
            balance goes negative.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Transaction applied. For ``kind: grant``, the ledger row(s) written plus the new balance. For ``kind:
            debit``, one row per grant touched plus the requested/drained/rejected accounting and the new balance.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Includes an unrecognized
                ``kind``, a missing ``wallet_transaction`` root, a malformed, non-positive, or out-of-range ``amount``,
                a memo over 255 characters, ``expires_at`` sent with ``kind: debit``, a malformed or past-dated
                ``expires_at``, an archived wallet, and, for ``kind: debit`` only, a depleted wallet. For a metered
                wallet, usage could be read but settling it against the ledger failed. For a metered wallet, live usage
                could not be read in time to compute the debit. Not returned for ``kind: grant``. ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_wallet_transaction(
                wallet_id, body=body, request_options=request_options
            ),
        )

    async def list_wallet_transactions(
        self,
        wallet_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletTransactionsListResponse:
        """Lists the wallet's append-only ledger, newest first, paginated.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
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
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.list_wallet_transactions(
                wallet_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWalletTransactionsWithRawResponse:
        return self._with_raw_response


class WalletTransactionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_wallet_transaction(
        self,
        wallet_id: int,
        *,
        body: CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletTransactionResultResponse, CreateWalletTransactionErrorBody]:
        """Grants units to the wallet, or debits units from it, depending on ``kind``. ``amount`` is always sent
        positive, and ``kind`` determines the direction written to the ledger.

        **``kind: grant``**: a one-time manual top-up. On a non-negative balance, this creates a grant and writes one
        ledger row. On a negative balance, it repays the overdraft first (a ``kind: grant`` row with ``grant_id: null``,
        for the repaid amount), then creates the grant: its ``original`` is always the full ``amount`` sent, and its
        ``remaining`` is what's left after the overdraft was repaid, which is ``0`` if the overdraft absorbed the whole
        top-up. The grant row is still written, and its ``amount`` is that ``remaining``, not ``original``, so the
        ledger rows sum to the balance change. A grant may carry ``expires_at``; a debit may not.

        **``kind: debit``**: direct consumption. Drains grants earliest-expiration-first, one ``kind: debit`` row per
        grant touched, plus any overdue expiration rows this same call triggers first (see below):
        - Under the wallet's default ``hard_stop_overflow: discard``, the drain is capped at the available balance. For
            a metered wallet, that cap is the live metered balance, not the stored one, so a debit can drain less than
            its stored balance would suggest, or even drain nothing at all (``201`` with ``drained_amount: "0.0"``) if
            live usage has already consumed what the ledger hadn't caught up to yet. A debit against a wallet whose
            *stored* balance is already zero or negative (``discard`` only ever reaches zero) returns ``422 "Wallet is
            depleted"``. Before that failure is returned, this call still expires any grants that were already overdue,
            so a ``422`` response can still leave new ``kind: expiration`` rows written.
        - Under ``hard_stop_overflow: allow_negative``, the full amount is deducted. The excess past the wallet's grants
            is booked as one overdraft row with ``grant_id: null``, ``rejected_amount`` is always ``"0.0"``, and the
            balance goes negative.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/transactions.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletTransactionResultResponse],
            error_mapper=create_wallet_transaction_error_mapper,
            request_options=request_options,
        )

    def list_wallet_transactions(
        self,
        wallet_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletTransactionsListResponse, ListWalletTransactionsErrorBody]:
        """Lists the wallet's append-only ledger, newest first, paginated.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
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
            url_template=self._server.production("/wallets/{wallet_id}/transactions.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletTransactionsListResponse],
            error_mapper=list_wallet_transactions_error_mapper,
            request_options=request_options,
        )


class AsyncWalletTransactionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_wallet_transaction(
        self,
        wallet_id: int,
        *,
        body: CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletTransactionResultResponse, CreateWalletTransactionErrorBody]:
        """Grants units to the wallet, or debits units from it, depending on ``kind``. ``amount`` is always sent
        positive, and ``kind`` determines the direction written to the ledger.

        **``kind: grant``**: a one-time manual top-up. On a non-negative balance, this creates a grant and writes one
        ledger row. On a negative balance, it repays the overdraft first (a ``kind: grant`` row with ``grant_id: null``,
        for the repaid amount), then creates the grant: its ``original`` is always the full ``amount`` sent, and its
        ``remaining`` is what's left after the overdraft was repaid, which is ``0`` if the overdraft absorbed the whole
        top-up. The grant row is still written, and its ``amount`` is that ``remaining``, not ``original``, so the
        ledger rows sum to the balance change. A grant may carry ``expires_at``; a debit may not.

        **``kind: debit``**: direct consumption. Drains grants earliest-expiration-first, one ``kind: debit`` row per
        grant touched, plus any overdue expiration rows this same call triggers first (see below):
        - Under the wallet's default ``hard_stop_overflow: discard``, the drain is capped at the available balance. For
            a metered wallet, that cap is the live metered balance, not the stored one, so a debit can drain less than
            its stored balance would suggest, or even drain nothing at all (``201`` with ``drained_amount: "0.0"``) if
            live usage has already consumed what the ledger hadn't caught up to yet. A debit against a wallet whose
            *stored* balance is already zero or negative (``discard`` only ever reaches zero) returns ``422 "Wallet is
            depleted"``. Before that failure is returned, this call still expires any grants that were already overdue,
            so a ``422`` response can still leave new ``kind: expiration`` rows written.
        - Under ``hard_stop_overflow: allow_negative``, the full amount is deducted. The excess past the wallet's grants
            is booked as one overdraft row with ``grant_id: null``, ``rejected_amount`` is always ``"0.0"``, and the
            balance goes negative.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/transactions.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletTransactionRequest | CreateWalletTransactionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletTransactionResultResponse],
            error_mapper=create_wallet_transaction_error_mapper,
            request_options=request_options,
        )

    async def list_wallet_transactions(
        self,
        wallet_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletTransactionsListResponse, ListWalletTransactionsErrorBody]:
        """Lists the wallet's append-only ledger, newest first, paginated.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
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
            url_template=self._server.production("/wallets/{wallet_id}/transactions.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletTransactionsListResponse],
            error_mapper=list_wallet_transactions_error_mapper,
            request_options=request_options,
        )
