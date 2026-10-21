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
from ..errors.create_wallet_purchase_error import CreateWalletPurchaseErrorBody, create_wallet_purchase_error_mapper
from ..errors.preview_wallet_purchase_error import PreviewWalletPurchaseErrorBody, preview_wallet_purchase_error_mapper
from ..models.create_wallet_purchase_request import CreateWalletPurchaseRequest, CreateWalletPurchaseRequestDict
from ..models.wallet_purchase_preview_response import WalletPurchasePreviewResponse
from ..models.wallet_purchase_result_response import WalletPurchaseResultResponse
from ..server.server import Server


class WalletPurchases:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WalletPurchasesWithRawResponse(client, server, auth)

    def create_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletPurchaseResultResponse:
        """Purchases prepaid units for the wallet and charges the subscription's payment method for them, using the
        wallet's ``price_point_id`` unless a different price point is named. A successful purchase writes a grant of
        origin ``purchase``, with its expiration following the funding entitlement's grant expiration policy.

        How "charged" works depends on the subscription's collection method. For card/automatic collection, the payment
        is attempted immediately; a decline writes nothing to the wallet, and the call fails with a ``422`` naming the
        gateway's decline reason. For invoice-billed (remittance) subscriptions, there's no immediate charge to decline:
        an invoice is drafted, the wallet is credited right away, and the invoice is issued afterward. If issuing the
        invoice fails at that point, the invoice is left in draft state and reported for follow-up, but the call still
        returns ``201`` and the units already credited are **not** rolled back. See `Preview Wallet Purchase
        <$e/Wallet%20Purchases/previewWalletPurchase>`__ to quote a price before charging anything.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Purchase completed. Charges the subscription's payment method and, once payment succeeds, credits the
            wallet.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Includes a missing
                ``purchase`` root, a missing, malformed, non-positive, or out-of-range ``quantity``, a
                ``price_point_id`` that doesn't belong to the wallet's billing product, an archived, custom, or
                otherwise unusable price point, no price point to purchase at (neither sent nor set on the wallet), a
                memo over 255 characters, an archived wallet, a price point with no price in the subscription's
                currency, a declined payment (message includes the gateway's own detail), an invoice that couldn't be
                created at all, a payment that settled but whose units could not be credited
                (``purchase_paid_but_uncredited``, whose message ends with the paid invoice's uid so it can be
                reconciled), and a wallet whose billing product isn't a Wallet Product (only possible for a wallet
                created before Wallet Products became required). ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_wallet_purchase(wallet_id, body=body, request_options=request_options)
        )

    def preview_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletPurchasePreviewResponse:
        """Quotes the price for a purchase at the given quantity and price point, without charging the payment method or
        writing to the wallet. Takes the same parameters as `Create Wallet Purchase
        <$e/Wallet%20Purchases/createWalletPurchase>`__.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A price quote. Charges nothing and writes nothing to the wallet.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Same cases as Create Wallet
                Purchase, minus the payment-outcome cases, since nothing is charged. ``error`` is ``WalletErrorResponse1
                | RawError``."""
        return unwrap(
            self._with_raw_response.preview_wallet_purchase(wallet_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> WalletPurchasesWithRawResponse:
        return self._with_raw_response


class AsyncWalletPurchases:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWalletPurchasesWithRawResponse(client, server, auth)

    async def create_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletPurchaseResultResponse:
        """Purchases prepaid units for the wallet and charges the subscription's payment method for them, using the
        wallet's ``price_point_id`` unless a different price point is named. A successful purchase writes a grant of
        origin ``purchase``, with its expiration following the funding entitlement's grant expiration policy.

        How "charged" works depends on the subscription's collection method. For card/automatic collection, the payment
        is attempted immediately; a decline writes nothing to the wallet, and the call fails with a ``422`` naming the
        gateway's decline reason. For invoice-billed (remittance) subscriptions, there's no immediate charge to decline:
        an invoice is drafted, the wallet is credited right away, and the invoice is issued afterward. If issuing the
        invoice fails at that point, the invoice is left in draft state and reported for follow-up, but the call still
        returns ``201`` and the units already credited are **not** rolled back. See `Preview Wallet Purchase
        <$e/Wallet%20Purchases/previewWalletPurchase>`__ to quote a price before charging anything.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Purchase completed. Charges the subscription's payment method and, once payment succeeds, credits the
            wallet.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Includes a missing
                ``purchase`` root, a missing, malformed, non-positive, or out-of-range ``quantity``, a
                ``price_point_id`` that doesn't belong to the wallet's billing product, an archived, custom, or
                otherwise unusable price point, no price point to purchase at (neither sent nor set on the wallet), a
                memo over 255 characters, an archived wallet, a price point with no price in the subscription's
                currency, a declined payment (message includes the gateway's own detail), an invoice that couldn't be
                created at all, a payment that settled but whose units could not be credited
                (``purchase_paid_but_uncredited``, whose message ends with the paid invoice's uid so it can be
                reconciled), and a wallet whose billing product isn't a Wallet Product (only possible for a wallet
                created before Wallet Products became required). ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_wallet_purchase(wallet_id, body=body, request_options=request_options)
        )

    async def preview_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletPurchasePreviewResponse:
        """Quotes the price for a purchase at the given quantity and price point, without charging the payment method or
        writing to the wallet. Takes the same parameters as `Create Wallet Purchase
        <$e/Wallet%20Purchases/createWalletPurchase>`__.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A price quote. Charges nothing and writes nothing to the wallet.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Same cases as Create Wallet
                Purchase, minus the payment-outcome cases, since nothing is charged. ``error`` is ``WalletErrorResponse1
                | RawError``."""
        return unwrap(
            await self._with_raw_response.preview_wallet_purchase(wallet_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncWalletPurchasesWithRawResponse:
        return self._with_raw_response


class WalletPurchasesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletPurchaseResultResponse, CreateWalletPurchaseErrorBody]:
        """Purchases prepaid units for the wallet and charges the subscription's payment method for them, using the
        wallet's ``price_point_id`` unless a different price point is named. A successful purchase writes a grant of
        origin ``purchase``, with its expiration following the funding entitlement's grant expiration policy.

        How "charged" works depends on the subscription's collection method. For card/automatic collection, the payment
        is attempted immediately; a decline writes nothing to the wallet, and the call fails with a ``422`` naming the
        gateway's decline reason. For invoice-billed (remittance) subscriptions, there's no immediate charge to decline:
        an invoice is drafted, the wallet is credited right away, and the invoice is issued afterward. If issuing the
        invoice fails at that point, the invoice is left in draft state and reported for follow-up, but the call still
        returns ``201`` and the units already credited are **not** rolled back. See `Preview Wallet Purchase
        <$e/Wallet%20Purchases/previewWalletPurchase>`__ to quote a price before charging anything.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/purchases.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletPurchaseResultResponse],
            error_mapper=create_wallet_purchase_error_mapper,
            request_options=request_options,
        )

    def preview_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletPurchasePreviewResponse, PreviewWalletPurchaseErrorBody]:
        """Quotes the price for a purchase at the given quantity and price point, without charging the payment method or
        writing to the wallet. Takes the same parameters as `Create Wallet Purchase
        <$e/Wallet%20Purchases/createWalletPurchase>`__.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/purchases/preview.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletPurchasePreviewResponse],
            error_mapper=preview_wallet_purchase_error_mapper,
            request_options=request_options,
        )


class AsyncWalletPurchasesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletPurchaseResultResponse, CreateWalletPurchaseErrorBody]:
        """Purchases prepaid units for the wallet and charges the subscription's payment method for them, using the
        wallet's ``price_point_id`` unless a different price point is named. A successful purchase writes a grant of
        origin ``purchase``, with its expiration following the funding entitlement's grant expiration policy.

        How "charged" works depends on the subscription's collection method. For card/automatic collection, the payment
        is attempted immediately; a decline writes nothing to the wallet, and the call fails with a ``422`` naming the
        gateway's decline reason. For invoice-billed (remittance) subscriptions, there's no immediate charge to decline:
        an invoice is drafted, the wallet is credited right away, and the invoice is issued afterward. If issuing the
        invoice fails at that point, the invoice is left in draft state and reported for follow-up, but the call still
        returns ``201`` and the units already credited are **not** rolled back. See `Preview Wallet Purchase
        <$e/Wallet%20Purchases/previewWalletPurchase>`__ to quote a price before charging anything.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/purchases.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletPurchaseResultResponse],
            error_mapper=create_wallet_purchase_error_mapper,
            request_options=request_options,
        )

    async def preview_wallet_purchase(
        self,
        wallet_id: int,
        *,
        body: CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletPurchasePreviewResponse, PreviewWalletPurchaseErrorBody]:
        """Quotes the price for a purchase at the given quantity and price point, without charging the payment method or
        writing to the wallet. Takes the same parameters as `Create Wallet Purchase
        <$e/Wallet%20Purchases/createWalletPurchase>`__.

        Args:
            wallet_id: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets/{wallet_id}/purchases/preview.json"),
            path_params=[param[int]("wallet_id", wallet_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletPurchaseRequest | CreateWalletPurchaseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletPurchasePreviewResponse],
            error_mapper=preview_wallet_purchase_error_mapper,
            request_options=request_options,
        )
