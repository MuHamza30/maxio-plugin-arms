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
from ..errors.create_wallet_adjustment_error import (
    CreateWalletAdjustmentErrorBody,
    create_wallet_adjustment_error_mapper,
)
from ..models.create_wallet_adjustment_request import CreateWalletAdjustmentRequest, CreateWalletAdjustmentRequestDict
from ..models.wallet_grant_result_response import WalletGrantResultResponse
from ..server.server import Server


class WalletAdjustments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WalletAdjustmentsWithRawResponse(client, server, auth)

    def create_wallet_adjustment(
        self,
        wallet_id: int,
        *,
        body: CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletGrantResultResponse:
        """Posts a signed correction against a specific grant (or, for an overdraft entry, against the overdraft):
        positive adds units to the grant, negative removes them. ``reason`` is required and is written to the ledger
        row's ``memo``. Writes exactly one ledger row, of kind ``adjustment``.

        Use ``source_transaction_id`` to name a specific ``debit`` row when you're correcting one recorded consumption
        rather than the grant's balance as a whole. When it names a grant-attributed debit, it's recorded for audit
        only: naming it doesn't change how ``amount`` is applied, and more than one adjustment may name the same row.
        When it names an overdraft entry, it switches the correction to the overdraft path described below.

        An overdraft entry (a ``debit`` row with no ``grant_id``, written when an ``allow_negative`` wallet consumes
        past its grants) can be corrected without a ``grant_id``. That correction is credit-only, credits no grant, and
        is bounded by the usage the entry still records and by the overdraft the wallet still owes. Once a later grant
        has repaid the overdraft, correct that grant's balance instead.

        An adjustment corrects the ledger, so it works on the grant's recorded remainder, ``posted_remaining``, not on
        ``remaining``, which on a metered wallet read through `Read Wallet <$e/Wallets/readWallet>`__ also subtracts
        usage not yet posted. Send ``posted_remaining`` back as ``expected_remaining``; sending ``remaining`` on a
        metered wallet with pending usage returns ``409``.

        ``expected_remaining`` and ``expected_source_corrections`` are optional optimistic-concurrency checks; see their
        field descriptions. Use them when the correction's ``amount`` was derived from a value read earlier that might
        have moved since.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The ledger row written, plus the wallet's new balance.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found The state the ``amount`` was derived from has
                moved: either the grant's ``posted_remaining`` no longer matches ``expected_remaining``, or the
                corrections already posted against ``source_transaction_id`` no longer sum to
                ``expected_source_corrections``. Nothing is written. Reload and re-derive the amount. Validation
                failure. Includes a missing ``reason``, a ``reason`` over 255 characters, a missing or not-found
                ``grant_id``, a zero, malformed, or out-of-range ``amount``, a negative adjustment exceeding the grant's
                ``posted_remaining``, a positive adjustment exceeding the grant's ``original``, a malformed
                ``expected_remaining`` or ``expected_source_corrections`` (including an empty string, which is treated
                as malformed rather than omitted), a ``source_transaction_id`` not on this wallet or not a ``debit``
                row, an overdraft correction that debits instead of credits ("Overdraft usage can only be corrected
                downward"), that exceeds the usage the entry still records ("Adjustment exceeds the usage this entry
                still records"), or that exceeds the overdraft the wallet still owes ("Adjustment exceeds the wallet's
                outstanding overdraft", followed by how much can still be corrected), a ``grant_id`` sent with an
                overdraft entry, and an archived wallet. ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_wallet_adjustment(wallet_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> WalletAdjustmentsWithRawResponse:
        return self._with_raw_response


class AsyncWalletAdjustments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWalletAdjustmentsWithRawResponse(client, server, auth)

    async def create_wallet_adjustment(
        self,
        wallet_id: int,
        *,
        body: CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletGrantResultResponse:
        """Posts a signed correction against a specific grant (or, for an overdraft entry, against the overdraft):
        positive adds units to the grant, negative removes them. ``reason`` is required and is written to the ledger
        row's ``memo``. Writes exactly one ledger row, of kind ``adjustment``.

        Use ``source_transaction_id`` to name a specific ``debit`` row when you're correcting one recorded consumption
        rather than the grant's balance as a whole. When it names a grant-attributed debit, it's recorded for audit
        only: naming it doesn't change how ``amount`` is applied, and more than one adjustment may name the same row.
        When it names an overdraft entry, it switches the correction to the overdraft path described below.

        An overdraft entry (a ``debit`` row with no ``grant_id``, written when an ``allow_negative`` wallet consumes
        past its grants) can be corrected without a ``grant_id``. That correction is credit-only, credits no grant, and
        is bounded by the usage the entry still records and by the overdraft the wallet still owes. Once a later grant
        has repaid the overdraft, correct that grant's balance instead.

        An adjustment corrects the ledger, so it works on the grant's recorded remainder, ``posted_remaining``, not on
        ``remaining``, which on a metered wallet read through `Read Wallet <$e/Wallets/readWallet>`__ also subtracts
        usage not yet posted. Send ``posted_remaining`` back as ``expected_remaining``; sending ``remaining`` on a
        metered wallet with pending usage returns ``409``.

        ``expected_remaining`` and ``expected_source_corrections`` are optional optimistic-concurrency checks; see their
        field descriptions. Use them when the correction's ``amount`` was derived from a value read earlier that might
        have moved since.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The ledger row written, plus the wallet's new balance.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found The state the ``amount`` was derived from has
                moved: either the grant's ``posted_remaining`` no longer matches ``expected_remaining``, or the
                corrections already posted against ``source_transaction_id`` no longer sum to
                ``expected_source_corrections``. Nothing is written. Reload and re-derive the amount. Validation
                failure. Includes a missing ``reason``, a ``reason`` over 255 characters, a missing or not-found
                ``grant_id``, a zero, malformed, or out-of-range ``amount``, a negative adjustment exceeding the grant's
                ``posted_remaining``, a positive adjustment exceeding the grant's ``original``, a malformed
                ``expected_remaining`` or ``expected_source_corrections`` (including an empty string, which is treated
                as malformed rather than omitted), a ``source_transaction_id`` not on this wallet or not a ``debit``
                row, an overdraft correction that debits instead of credits ("Overdraft usage can only be corrected
                downward"), that exceeds the usage the entry still records ("Adjustment exceeds the usage this entry
                still records"), or that exceeds the overdraft the wallet still owes ("Adjustment exceeds the wallet's
                outstanding overdraft", followed by how much can still be corrected), a ``grant_id`` sent with an
                overdraft entry, and an archived wallet. ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_wallet_adjustment(
                wallet_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWalletAdjustmentsWithRawResponse:
        return self._with_raw_response


class WalletAdjustmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_wallet_adjustment(
        self,
        wallet_id: int,
        *,
        body: CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletGrantResultResponse, CreateWalletAdjustmentErrorBody]:
        """Posts a signed correction against a specific grant (or, for an overdraft entry, against the overdraft):
        positive adds units to the grant, negative removes them. ``reason`` is required and is written to the ledger
        row's ``memo``. Writes exactly one ledger row, of kind ``adjustment``.

        Use ``source_transaction_id`` to name a specific ``debit`` row when you're correcting one recorded consumption
        rather than the grant's balance as a whole. When it names a grant-attributed debit, it's recorded for audit
        only: naming it doesn't change how ``amount`` is applied, and more than one adjustment may name the same row.
        When it names an overdraft entry, it switches the correction to the overdraft path described below.

        An overdraft entry (a ``debit`` row with no ``grant_id``, written when an ``allow_negative`` wallet consumes
        past its grants) can be corrected without a ``grant_id``. That correction is credit-only, credits no grant, and
        is bounded by the usage the entry still records and by the overdraft the wallet still owes. Once a later grant
        has repaid the overdraft, correct that grant's balance instead.

        An adjustment corrects the ledger, so it works on the grant's recorded remainder, ``posted_remaining``, not on
        ``remaining``, which on a metered wallet read through `Read Wallet <$e/Wallets/readWallet>`__ also subtracts
        usage not yet posted. Send ``posted_remaining`` back as ``expected_remaining``; sending ``remaining`` on a
        metered wallet with pending usage returns ``409``.

        ``expected_remaining`` and ``expected_source_corrections`` are optional optimistic-concurrency checks; see their
        field descriptions. Use them when the correction's ``amount`` was derived from a value read earlier that might
        have moved since.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/adjustments.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletGrantResultResponse],
            error_mapper=create_wallet_adjustment_error_mapper,
            request_options=request_options,
        )


class AsyncWalletAdjustmentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_wallet_adjustment(
        self,
        wallet_id: int,
        *,
        body: CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletGrantResultResponse, CreateWalletAdjustmentErrorBody]:
        """Posts a signed correction against a specific grant (or, for an overdraft entry, against the overdraft):
        positive adds units to the grant, negative removes them. ``reason`` is required and is written to the ledger
        row's ``memo``. Writes exactly one ledger row, of kind ``adjustment``.

        Use ``source_transaction_id`` to name a specific ``debit`` row when you're correcting one recorded consumption
        rather than the grant's balance as a whole. When it names a grant-attributed debit, it's recorded for audit
        only: naming it doesn't change how ``amount`` is applied, and more than one adjustment may name the same row.
        When it names an overdraft entry, it switches the correction to the overdraft path described below.

        An overdraft entry (a ``debit`` row with no ``grant_id``, written when an ``allow_negative`` wallet consumes
        past its grants) can be corrected without a ``grant_id``. That correction is credit-only, credits no grant, and
        is bounded by the usage the entry still records and by the overdraft the wallet still owes. Once a later grant
        has repaid the overdraft, correct that grant's balance instead.

        An adjustment corrects the ledger, so it works on the grant's recorded remainder, ``posted_remaining``, not on
        ``remaining``, which on a metered wallet read through `Read Wallet <$e/Wallets/readWallet>`__ also subtracts
        usage not yet posted. Send ``posted_remaining`` back as ``expected_remaining``; sending ``remaining`` on a
        metered wallet with pending usage returns ``409``.

        ``expected_remaining`` and ``expected_source_corrections`` are optional optimistic-concurrency checks; see their
        field descriptions. Use them when the correction's ``amount`` was derived from a value read earlier that might
        have moved since.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/adjustments.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletAdjustmentRequest | CreateWalletAdjustmentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletGrantResultResponse],
            error_mapper=create_wallet_adjustment_error_mapper,
            request_options=request_options,
        )
