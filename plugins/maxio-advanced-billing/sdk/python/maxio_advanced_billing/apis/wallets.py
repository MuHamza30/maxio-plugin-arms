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
from ..errors.archive_wallet_error import ArchiveWalletErrorBody, archive_wallet_error_mapper
from ..errors.create_wallet_error import CreateWalletErrorBody, create_wallet_error_mapper
from ..errors.list_wallets_error import ListWalletsErrorBody, list_wallets_error_mapper
from ..errors.read_wallet_error import ReadWalletErrorBody, read_wallet_error_mapper
from ..errors.update_wallet_error import UpdateWalletErrorBody, update_wallet_error_mapper
from ..models.create_wallet_request import CreateWalletRequest, CreateWalletRequestDict
from ..models.enums.status2 import Status2OrStr
from ..models.update_wallet_request import UpdateWalletRequest, UpdateWalletRequestDict
from ..models.wallet_response import WalletResponse
from ..models.wallets_list_response import WalletsListResponse
from ..server.server import Server


class Wallets:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WalletsWithRawResponse(client, server, auth)

    def archive_wallet(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> WalletResponse:
        """Archives the wallet: blocks further grants, debits, adjustments, and purchases (each returns ``422``), stops
        any metered drawdown, and stops recurring funding (its schedule is deactivated with reason ``wallet_archived``,
        not removed), while reads and the ledger stay available. Nothing already on the wallet is destroyed or clawed
        back, but nothing on it can be spent either, by any path, once archived. Idempotent: archiving an
        already-archived wallet returns the same ``200``. There is no restore endpoint.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The wallet, with ``"status": "archived"``.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.archive_wallet(id_, request_options=request_options))

    def create_wallet(
        self,
        *,
        body: CreateWalletRequest | CreateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletResponse:
        """Creates a wallet owned by a subscription and denominated by a `Wallet Product
        <$e/Wallet%20Products/createWalletProduct>`__: only a Wallet Product can denominate a wallet, not an ordinary
        component. The Wallet Product must be active; it never belongs to a product family, so there's no family check
        against the subscription. It's **immutable for the life of the wallet**; there's no way to repoint an existing
        wallet at a different one.

        This endpoint always creates a ``manual`` wallet. To provision a wallet automatically from a usage-limit
        entitlement instead, configure ``wallet_behavior`` on the Feature behind that entitlement (see `the Wallets
        concept guide <page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature>`__) rather than
        sending ``entitlement_id`` here.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet created. The balance is ``"0.0"`` with no grants, unless a non-zero ``initial_balance`` was given. In
            that case, the balance and its seeded grant are already reflected.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Unknown or cross-site subscription or meter, or a
                ``wallet_product_id`` that doesn't resolve to a Wallet Product on this site. Validation failure.
                Includes a missing or archived ``wallet_product_id``; a ``price_point_id`` that's missing, archived, a
                subscription-specific custom price point, or doesn't belong to the Wallet Product; an invalid
                ``depletion_policy`` or ``hard_stop_overflow`` value; a meter that isn't a ``sum`` or ``count`` meter;
                an invalid ``conversion_rate``; a subscription with no reference, when pairing a meter whose stream
                bills by subscription reference; and the ``initial_balance`` / ``initial_balance_expires_at`` error
                cases described on those fields. Also returned for ``entitlement_id``: this endpoint never accepts it,
                and rejects it with the message shown below rather than silently ignoring it. Also returned when
                ``subscription_id`` names a prepaid subscription: a wallet would double-meter a balance the subscription
                already tracks on its own, so the two are mutually exclusive. ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.create_wallet(body=body, request_options=request_options))

    def list_wallets(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        subscription_id: int | None = None,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletsListResponse:
        """Lists the wallets on your site, in creation order, paginated. Without ``subscription_id``, returns every
        wallet on the site. The API key is the tenancy boundary; ``subscription_id`` only narrows the result set
        further. Archived wallets are included unless you filter them out with ``status=active``.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            subscription_id: Restricts the result to wallets owned by this subscription.
            status: Restricts the result by wallet status. An unrecognized value returns ``422`` rather than being
                silently ignored.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Unprocessable Entity (WebDAV) ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_wallets(
                page=page,
                per_page=per_page,
                subscription_id=subscription_id,
                status=status,
                request_options=request_options,
            ),
        )

    def read_wallet(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> WalletResponse:
        """Returns the wallet's balance and grant breakdown. For an active, metered wallet on a site with metered
        consumption enabled, this is the only operation that computes a live balance from meter usage; see the wallet
        resource's ``metered_*`` fields. It is also the only operation where ``balance`` can differ from
        ``posted_balance``, and a grant's ``remaining`` from its ``posted_remaining``: the pending usage is drawn from
        the grants in drain order, so the grants' ``remaining`` add up to ``balance``. Readable regardless of status.
        Archiving a wallet doesn't affect reads.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.read_wallet(id_, request_options=request_options))

    def update_wallet(
        self,
        id_: int,
        *,
        body: UpdateWalletRequest | UpdateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletResponse:
        """Updates the wallet's editable attributes. Only ``name`` is editable; any other attribute in the body is
        ignored. Send only the attributes to change.

        Args:
            id_: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated wallet. Reports the stored balance, equal to ``posted_balance``, with the ``metered_*`` fields
            ``null``, as on list, create, and archive.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Includes a body with no
                editable attribute (``parameter_missing``), a ``name`` over 255 characters (``validation_failed``), and
                an archived wallet (``wallet_archived``). ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.update_wallet(id_, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> WalletsWithRawResponse:
        return self._with_raw_response


class AsyncWallets:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWalletsWithRawResponse(client, server, auth)

    async def archive_wallet(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> WalletResponse:
        """Archives the wallet: blocks further grants, debits, adjustments, and purchases (each returns ``422``), stops
        any metered drawdown, and stops recurring funding (its schedule is deactivated with reason ``wallet_archived``,
        not removed), while reads and the ledger stay available. Nothing already on the wallet is destroyed or clawed
        back, but nothing on it can be spent either, by any path, once archived. Idempotent: archiving an
        already-archived wallet returns the same ``200``. There is no restore endpoint.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The wallet, with ``"status": "archived"``.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.archive_wallet(id_, request_options=request_options))

    async def create_wallet(
        self,
        *,
        body: CreateWalletRequest | CreateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletResponse:
        """Creates a wallet owned by a subscription and denominated by a `Wallet Product
        <$e/Wallet%20Products/createWalletProduct>`__: only a Wallet Product can denominate a wallet, not an ordinary
        component. The Wallet Product must be active; it never belongs to a product family, so there's no family check
        against the subscription. It's **immutable for the life of the wallet**; there's no way to repoint an existing
        wallet at a different one.

        This endpoint always creates a ``manual`` wallet. To provision a wallet automatically from a usage-limit
        entitlement instead, configure ``wallet_behavior`` on the Feature behind that entitlement (see `the Wallets
        concept guide <page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature>`__) rather than
        sending ``entitlement_id`` here.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet created. The balance is ``"0.0"`` with no grants, unless a non-zero ``initial_balance`` was given. In
            that case, the balance and its seeded grant are already reflected.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Unknown or cross-site subscription or meter, or a
                ``wallet_product_id`` that doesn't resolve to a Wallet Product on this site. Validation failure.
                Includes a missing or archived ``wallet_product_id``; a ``price_point_id`` that's missing, archived, a
                subscription-specific custom price point, or doesn't belong to the Wallet Product; an invalid
                ``depletion_policy`` or ``hard_stop_overflow`` value; a meter that isn't a ``sum`` or ``count`` meter;
                an invalid ``conversion_rate``; a subscription with no reference, when pairing a meter whose stream
                bills by subscription reference; and the ``initial_balance`` / ``initial_balance_expires_at`` error
                cases described on those fields. Also returned for ``entitlement_id``: this endpoint never accepts it,
                and rejects it with the message shown below rather than silently ignoring it. Also returned when
                ``subscription_id`` names a prepaid subscription: a wallet would double-meter a balance the subscription
                already tracks on its own, so the two are mutually exclusive. ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.create_wallet(body=body, request_options=request_options))

    async def list_wallets(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        subscription_id: int | None = None,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletsListResponse:
        """Lists the wallets on your site, in creation order, paginated. Without ``subscription_id``, returns every
        wallet on the site. The API key is the tenancy boundary; ``subscription_id`` only narrows the result set
        further. Archived wallets are included unless you filter them out with ``status=active``.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            subscription_id: Restricts the result to wallets owned by this subscription.
            status: Restricts the result by wallet status. An unrecognized value returns ``422`` rather than being
                silently ignored.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Unprocessable Entity (WebDAV) ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_wallets(
                page=page,
                per_page=per_page,
                subscription_id=subscription_id,
                status=status,
                request_options=request_options,
            ),
        )

    async def read_wallet(self, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> WalletResponse:
        """Returns the wallet's balance and grant breakdown. For an active, metered wallet on a site with metered
        consumption enabled, this is the only operation that computes a live balance from meter usage; see the wallet
        resource's ``metered_*`` fields. It is also the only operation where ``balance`` can differ from
        ``posted_balance``, and a grant's ``remaining`` from its ``posted_remaining``: the pending usage is drawn from
        the grants in drain order, so the grants' ``remaining`` add up to ``balance``. Readable regardless of status.
        Archiving a wallet doesn't affect reads.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.read_wallet(id_, request_options=request_options))

    async def update_wallet(
        self,
        id_: int,
        *,
        body: UpdateWalletRequest | UpdateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletResponse:
        """Updates the wallet's editable attributes. Only ``name`` is editable; any other attribute in the body is
        ignored. Send only the attributes to change.

        Args:
            id_: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated wallet. Reports the stored balance, equal to ``posted_balance``, with the ``metered_*`` fields
            ``null``, as on list, create, and archive.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. Includes a body with no
                editable attribute (``parameter_missing``), a ``name`` over 255 characters (``validation_failed``), and
                an archived wallet (``wallet_archived``). ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.update_wallet(id_, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncWalletsWithRawResponse:
        return self._with_raw_response


class WalletsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_wallet(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletResponse, ArchiveWalletErrorBody]:
        """Archives the wallet: blocks further grants, debits, adjustments, and purchases (each returns ``422``), stops
        any metered drawdown, and stops recurring funding (its schedule is deactivated with reason ``wallet_archived``,
        not removed), while reads and the ledger stay available. Nothing already on the wallet is destroyed or clawed
        back, but nothing on it can be spent either, by any path, once archived. Idempotent: archiving an
        already-archived wallet returns the same ``200``. There is no restore endpoint.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/wallets/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletResponse],
            error_mapper=archive_wallet_error_mapper,
            request_options=request_options,
        )

    def create_wallet(
        self,
        *,
        body: CreateWalletRequest | CreateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletResponse, CreateWalletErrorBody]:
        """Creates a wallet owned by a subscription and denominated by a `Wallet Product
        <$e/Wallet%20Products/createWalletProduct>`__: only a Wallet Product can denominate a wallet, not an ordinary
        component. The Wallet Product must be active; it never belongs to a product family, so there's no family check
        against the subscription. It's **immutable for the life of the wallet**; there's no way to repoint an existing
        wallet at a different one.

        This endpoint always creates a ``manual`` wallet. To provision a wallet automatically from a usage-limit
        entitlement instead, configure ``wallet_behavior`` on the Feature behind that entitlement (see `the Wallets
        concept guide <page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature>`__) rather than
        sending ``entitlement_id`` here.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletRequest | CreateWalletRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletResponse],
            error_mapper=create_wallet_error_mapper,
            request_options=request_options,
        )

    def list_wallets(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        subscription_id: int | None = None,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletsListResponse, ListWalletsErrorBody]:
        """Lists the wallets on your site, in creation order, paginated. Without ``subscription_id``, returns every
        wallet on the site. The API key is the tenancy boundary; ``subscription_id`` only narrows the result set
        further. Archived wallets are included unless you filter them out with ``status=active``.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            subscription_id: Restricts the result to wallets owned by this subscription.
            status: Restricts the result by wallet status. An unrecognized value returns ``422`` rather than being
                silently ignored.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallets.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("subscription_id", subscription_id),
                param[Status2OrStr | None]("status", status),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletsListResponse],
            error_mapper=list_wallets_error_mapper,
            request_options=request_options,
        )

    def read_wallet(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletResponse, ReadWalletErrorBody]:
        """Returns the wallet's balance and grant breakdown. For an active, metered wallet on a site with metered
        consumption enabled, this is the only operation that computes a live balance from meter usage; see the wallet
        resource's ``metered_*`` fields. It is also the only operation where ``balance`` can differ from
        ``posted_balance``, and a grant's ``remaining`` from its ``posted_remaining``: the pending usage is drawn from
        the grants in drain order, so the grants' ``remaining`` add up to ``balance``. Readable regardless of status.
        Archiving a wallet doesn't affect reads.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallets/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletResponse],
            error_mapper=read_wallet_error_mapper,
            request_options=request_options,
        )

    def update_wallet(
        self,
        id_: int,
        *,
        body: UpdateWalletRequest | UpdateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletResponse, UpdateWalletErrorBody]:
        """Updates the wallet's editable attributes. Only ``name`` is editable; any other attribute in the body is
        ignored. Send only the attributes to change.

        Args:
            id_: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.production("/wallets/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateWalletRequest | UpdateWalletRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletResponse],
            error_mapper=update_wallet_error_mapper,
            request_options=request_options,
        )


class AsyncWalletsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_wallet(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletResponse, ArchiveWalletErrorBody]:
        """Archives the wallet: blocks further grants, debits, adjustments, and purchases (each returns ``422``), stops
        any metered drawdown, and stops recurring funding (its schedule is deactivated with reason ``wallet_archived``,
        not removed), while reads and the ledger stay available. Nothing already on the wallet is destroyed or clawed
        back, but nothing on it can be spent either, by any path, once archived. Idempotent: archiving an
        already-archived wallet returns the same ``200``. There is no restore endpoint.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/wallets/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletResponse],
            error_mapper=archive_wallet_error_mapper,
            request_options=request_options,
        )

    async def create_wallet(
        self,
        *,
        body: CreateWalletRequest | CreateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletResponse, CreateWalletErrorBody]:
        """Creates a wallet owned by a subscription and denominated by a `Wallet Product
        <$e/Wallet%20Products/createWalletProduct>`__: only a Wallet Product can denominate a wallet, not an ordinary
        component. The Wallet Product must be active; it never belongs to a product family, so there's no family check
        against the subscription. It's **immutable for the life of the wallet**; there's no way to repoint an existing
        wallet at a different one.

        This endpoint always creates a ``manual`` wallet. To provision a wallet automatically from a usage-limit
        entitlement instead, configure ``wallet_behavior`` on the Feature behind that entitlement (see `the Wallets
        concept guide <page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature>`__) rather than
        sending ``entitlement_id`` here.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallets.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletRequest | CreateWalletRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletResponse],
            error_mapper=create_wallet_error_mapper,
            request_options=request_options,
        )

    async def list_wallets(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        subscription_id: int | None = None,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletsListResponse, ListWalletsErrorBody]:
        """Lists the wallets on your site, in creation order, paginated. Without ``subscription_id``, returns every
        wallet on the site. The API key is the tenancy boundary; ``subscription_id`` only narrows the result set
        further. Archived wallets are included unless you filter them out with ``status=active``.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            subscription_id: Restricts the result to wallets owned by this subscription.
            status: Restricts the result by wallet status. An unrecognized value returns ``422`` rather than being
                silently ignored.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallets.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("subscription_id", subscription_id),
                param[Status2OrStr | None]("status", status),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletsListResponse],
            error_mapper=list_wallets_error_mapper,
            request_options=request_options,
        )

    async def read_wallet(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletResponse, ReadWalletErrorBody]:
        """Returns the wallet's balance and grant breakdown. For an active, metered wallet on a site with metered
        consumption enabled, this is the only operation that computes a live balance from meter usage; see the wallet
        resource's ``metered_*`` fields. It is also the only operation where ``balance`` can differ from
        ``posted_balance``, and a grant's ``remaining`` from its ``posted_remaining``: the pending usage is drawn from
        the grants in drain order, so the grants' ``remaining`` add up to ``balance``. Readable regardless of status.
        Archiving a wallet doesn't affect reads.

        Args:
            id_: The Advanced Billing id of the wallet.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallets/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletResponse],
            error_mapper=read_wallet_error_mapper,
            request_options=request_options,
        )

    async def update_wallet(
        self,
        id_: int,
        *,
        body: UpdateWalletRequest | UpdateWalletRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletResponse, UpdateWalletErrorBody]:
        """Updates the wallet's editable attributes. Only ``name`` is editable; any other attribute in the body is
        ignored. Send only the attributes to change.

        Args:
            id_: The Advanced Billing id of the wallet.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.production("/wallets/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateWalletRequest | UpdateWalletRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletResponse],
            error_mapper=update_wallet_error_mapper,
            request_options=request_options,
        )
