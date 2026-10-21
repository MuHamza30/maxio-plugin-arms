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
from ..errors.archive_wallet_product_error import ArchiveWalletProductErrorBody, archive_wallet_product_error_mapper
from ..errors.create_wallet_product_error import CreateWalletProductErrorBody, create_wallet_product_error_mapper
from ..errors.list_wallet_products_error import ListWalletProductsErrorBody, list_wallet_products_error_mapper
from ..errors.read_wallet_product_error import ReadWalletProductErrorBody, read_wallet_product_error_mapper
from ..errors.read_wallet_product_usage_error import (
    ReadWalletProductUsageErrorBody,
    read_wallet_product_usage_error_mapper,
)
from ..errors.unarchive_wallet_product_error import (
    UnarchiveWalletProductErrorBody,
    unarchive_wallet_product_error_mapper,
)
from ..errors.update_wallet_product_error import UpdateWalletProductErrorBody, update_wallet_product_error_mapper
from ..models.create_wallet_product_request import CreateWalletProductRequest, CreateWalletProductRequestDict
from ..models.enums.sort_by1 import SortBy1, SortBy1OrStr
from ..models.enums.sort_direction import SortDirection, SortDirectionOrStr
from ..models.enums.status1 import Status1OrStr
from ..models.update_wallet_product_request import UpdateWalletProductRequest, UpdateWalletProductRequestDict
from ..models.wallet_product_response import WalletProductResponse
from ..models.wallet_product_usage_response import WalletProductUsageResponse
from ..models.wallet_products_list_response import WalletProductsListResponse
from ..server.server import Server


class WalletProducts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WalletProductsWithRawResponse(client, server, auth)

    def archive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductResponse:
        """Archives the Wallet Product. Refuses when an active Feature's ``wallet_behavior`` still points at it, or when
        it's used in a scheduled renewal. This protects Feature-provisioned wallets, but not a wallet created manually
        against this product: a manual wallet can be left denominated by an archived Wallet Product, and `Create Wallet
        Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__ doesn't check whether the billing product is archived
        before pricing and charging a purchase against it.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product archived.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found The Wallet Product is already archived, is in use
                by one or more Features, or is in use by a scheduled renewal. ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.archive_wallet_product(id_, request_options=request_options))

    def create_wallet_product(
        self,
        *,
        body: CreateWalletProductRequest | CreateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletProductResponse:
        """Creates a Wallet Product: a billing product with no product family, meant to denominate wallets and to be
        purchased through `Create Wallet Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__. It's a Component
        under the hood, so it returns the full Component field set, and can optionally be priced with one or more price
        points in the same call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product created.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Validation failure. Includes a ``product_family_id``
                (rejected rather than ignored), and any failure validating a price point in
                ``price_point``/``price_points``, which rolls back the whole call, including the Wallet Product itself.
                ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_wallet_product(body=body, request_options=request_options))

    def list_wallet_products(
        self,
        *,
        include_archived: bool | None = None,
        status: Status1OrStr | None = None,
        q: str | None = None,
        sort_by: SortBy1OrStr | None = SortBy1.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletProductsListResponse:
        """Lists the Wallet Products on your site.

        Args:
            include_archived: Includes archived Wallet Products in the result. Defaults to ``false``. Ignored when
                ``status`` is also sent.
            status: Restricts the result by status, and overrides ``include_archived`` when sent. An unrecognized value
                falls back to ``active`` rather than returning ``422``.
            q: Restricts the result to Wallet Products whose name, handle, or unit name contains this substring
                (case-insensitive).
            sort_by: The field to sort results by. An unrecognized value falls back to ``name``.
            sort_direction: The sort direction. Anything other than ``desc`` is treated as ``asc``.
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
            OK. Unlike most list endpoints, this one is unpaginated (returns the full matching set in one response)
            unless ``page`` or ``per_page`` is sent; sending either turns on pagination, defaulting to 20 per page with
            a maximum of 200.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_wallet_products(
                include_archived=include_archived,
                status=status,
                q=q,
                sort_by=sort_by,
                sort_direction=sort_direction,
                page=page,
                per_page=per_page,
                request_options=request_options,
            ),
        )

    def read_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductResponse:
        """Returns the Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.read_wallet_product(id_, request_options=request_options))

    def read_wallet_product_usage(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductUsageResponse:
        """Returns everything drawing on this Wallet Product: the wallet templates billing through it, split into ones
        using its default price point and ones overriding it, plus a sample of up to 50 of the active wallets actually
        created from them. A wallet template can appear more than once in
        ``wallet_templates``/``price_point_overrides``, once per Feature and owning plan/component sharing it, so these
        arrays aren't one row per template.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.read_wallet_product_usage(id_, request_options=request_options))

    def unarchive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductResponse:
        """Restores an archived Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product unarchived.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found The Wallet Product is not archived. ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.unarchive_wallet_product(id_, request_options=request_options))

    def update_wallet_product(
        self,
        id_: str,
        *,
        body: UpdateWalletProductRequest | UpdateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletProductResponse:
        """Updates the Wallet Product's catalog-facing fields. Omitted fields are left unchanged. Unlike `Create Wallet
        Product <$e/Wallet%20Products/createWalletProduct>`__, this does not accept ``unit_name``, ``handle``,
        ``price_point``, or ``price_points``; see the request schema for which fields are actually mutable.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product updated.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.update_wallet_product(id_, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> WalletProductsWithRawResponse:
        return self._with_raw_response


class AsyncWalletProducts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWalletProductsWithRawResponse(client, server, auth)

    async def archive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductResponse:
        """Archives the Wallet Product. Refuses when an active Feature's ``wallet_behavior`` still points at it, or when
        it's used in a scheduled renewal. This protects Feature-provisioned wallets, but not a wallet created manually
        against this product: a manual wallet can be left denominated by an archived Wallet Product, and `Create Wallet
        Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__ doesn't check whether the billing product is archived
        before pricing and charging a purchase against it.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product archived.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found The Wallet Product is already archived, is in use
                by one or more Features, or is in use by a scheduled renewal. ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.archive_wallet_product(id_, request_options=request_options))

    async def create_wallet_product(
        self,
        *,
        body: CreateWalletProductRequest | CreateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletProductResponse:
        """Creates a Wallet Product: a billing product with no product family, meant to denominate wallets and to be
        purchased through `Create Wallet Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__. It's a Component
        under the hood, so it returns the full Component field set, and can optionally be priced with one or more price
        points in the same call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product created.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Validation failure. Includes a ``product_family_id``
                (rejected rather than ignored), and any failure validating a price point in
                ``price_point``/``price_points``, which rolls back the whole call, including the Wallet Product itself.
                ``error`` is ``WalletErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_wallet_product(body=body, request_options=request_options))

    async def list_wallet_products(
        self,
        *,
        include_archived: bool | None = None,
        status: Status1OrStr | None = None,
        q: str | None = None,
        sort_by: SortBy1OrStr | None = SortBy1.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletProductsListResponse:
        """Lists the Wallet Products on your site.

        Args:
            include_archived: Includes archived Wallet Products in the result. Defaults to ``false``. Ignored when
                ``status`` is also sent.
            status: Restricts the result by status, and overrides ``include_archived`` when sent. An unrecognized value
                falls back to ``active`` rather than returning ``422``.
            q: Restricts the result to Wallet Products whose name, handle, or unit name contains this substring
                (case-insensitive).
            sort_by: The field to sort results by. An unrecognized value falls back to ``name``.
            sort_direction: The sort direction. Anything other than ``desc`` is treated as ``asc``.
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
            OK. Unlike most list endpoints, this one is unpaginated (returns the full matching set in one response)
            unless ``page`` or ``per_page`` is sent; sending either turns on pagination, defaulting to 20 per page with
            a maximum of 200.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_wallet_products(
                include_archived=include_archived,
                status=status,
                q=q,
                sort_by=sort_by,
                sort_direction=sort_direction,
                page=page,
                per_page=per_page,
                request_options=request_options,
            ),
        )

    async def read_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductResponse:
        """Returns the Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.read_wallet_product(id_, request_options=request_options))

    async def read_wallet_product_usage(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductUsageResponse:
        """Returns everything drawing on this Wallet Product: the wallet templates billing through it, split into ones
        using its default price point and ones overriding it, plus a sample of up to 50 of the active wallets actually
        created from them. A wallet template can appear more than once in
        ``wallet_templates``/``price_point_overrides``, once per Feature and owning plan/component sharing it, so these
        arrays aren't one row per template.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found ``error`` is ``WalletErrorResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.read_wallet_product_usage(id_, request_options=request_options))

    async def unarchive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WalletProductResponse:
        """Restores an archived Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product unarchived.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found The Wallet Product is not archived. ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.unarchive_wallet_product(id_, request_options=request_options))

    async def update_wallet_product(
        self,
        id_: str,
        *,
        body: UpdateWalletProductRequest | UpdateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WalletProductResponse:
        """Updates the Wallet Product's catalog-facing fields. Omitted fields are left unchanged. Unlike `Create Wallet
        Product <$e/Wallet%20Products/createWalletProduct>`__, this does not accept ``unit_name``, ``handle``,
        ``price_point``, or ``price_points``; see the request schema for which fields are actually mutable.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Wallet Product updated.

        Raises:
            ApiError: Forbidden. The response body is plain text (``403 Forbidden``), not JSON. Returned when the
                Wallets feature isn't enabled for the site. Not Found Validation failure. ``error`` is
                ``WalletErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_wallet_product(id_, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncWalletProductsWithRawResponse:
        return self._with_raw_response


class WalletProductsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductResponse, ArchiveWalletProductErrorBody]:
        """Archives the Wallet Product. Refuses when an active Feature's ``wallet_behavior`` still points at it, or when
        it's used in a scheduled renewal. This protects Feature-provisioned wallets, but not a wallet created manually
        against this product: a manual wallet can be left denominated by an archived Wallet Product, and `Create Wallet
        Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__ doesn't check whether the billing product is archived
        before pricing and charging a purchase against it.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallet_products/{id}/archive.json"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletProductResponse],
            error_mapper=archive_wallet_product_error_mapper,
            request_options=request_options,
        )

    def create_wallet_product(
        self,
        *,
        body: CreateWalletProductRequest | CreateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletProductResponse, CreateWalletProductErrorBody]:
        """Creates a Wallet Product: a billing product with no product family, meant to denominate wallets and to be
        purchased through `Create Wallet Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__. It's a Component
        under the hood, so it returns the full Component field set, and can optionally be priced with one or more price
        points in the same call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallet_products.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletProductRequest | CreateWalletProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletProductResponse],
            error_mapper=create_wallet_product_error_mapper,
            request_options=request_options,
        )

    def list_wallet_products(
        self,
        *,
        include_archived: bool | None = None,
        status: Status1OrStr | None = None,
        q: str | None = None,
        sort_by: SortBy1OrStr | None = SortBy1.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletProductsListResponse, ListWalletProductsErrorBody]:
        """Lists the Wallet Products on your site.

        Args:
            include_archived: Includes archived Wallet Products in the result. Defaults to ``false``. Ignored when
                ``status`` is also sent.
            status: Restricts the result by status, and overrides ``include_archived`` when sent. An unrecognized value
                falls back to ``active`` rather than returning ``422``.
            q: Restricts the result to Wallet Products whose name, handle, or unit name contains this substring
                (case-insensitive).
            sort_by: The field to sort results by. An unrecognized value falls back to ``name``.
            sort_direction: The sort direction. Anything other than ``desc`` is treated as ``asc``.
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
            url_template=self._server.production("/wallet_products.json"),
            query_params=[
                param[bool | None]("include_archived", include_archived),
                param[Status1OrStr | None]("status", status),
                param[str | None]("q", q),
                param[SortBy1OrStr | None]("sort_by", sort_by),
                param[SortDirectionOrStr | None]("sort_direction", sort_direction),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletProductsListResponse],
            error_mapper=list_wallet_products_error_mapper,
            request_options=request_options,
        )

    def read_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductResponse, ReadWalletProductErrorBody]:
        """Returns the Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallet_products/{id}.json"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletProductResponse],
            error_mapper=read_wallet_product_error_mapper,
            request_options=request_options,
        )

    def read_wallet_product_usage(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductUsageResponse, ReadWalletProductUsageErrorBody]:
        """Returns everything drawing on this Wallet Product: the wallet templates billing through it, split into ones
        using its default price point and ones overriding it, plus a sample of up to 50 of the active wallets actually
        created from them. A wallet template can appear more than once in
        ``wallet_templates``/``price_point_overrides``, once per Feature and owning plan/component sharing it, so these
        arrays aren't one row per template.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallet_products/{id}/usage.json"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletProductUsageResponse],
            error_mapper=read_wallet_product_usage_error_mapper,
            request_options=request_options,
        )

    def unarchive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductResponse, UnarchiveWalletProductErrorBody]:
        """Restores an archived Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallet_products/{id}/unarchive.json"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletProductResponse],
            error_mapper=unarchive_wallet_product_error_mapper,
            request_options=request_options,
        )

    def update_wallet_product(
        self,
        id_: str,
        *,
        body: UpdateWalletProductRequest | UpdateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletProductResponse, UpdateWalletProductErrorBody]:
        """Updates the Wallet Product's catalog-facing fields. Omitted fields are left unchanged. Unlike `Create Wallet
        Product <$e/Wallet%20Products/createWalletProduct>`__, this does not accept ``unit_name``, ``handle``,
        ``price_point``, or ``price_points``; see the request schema for which fields are actually mutable.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/wallet_products/{id}.json"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateWalletProductRequest | UpdateWalletProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[WalletProductResponse],
            error_mapper=update_wallet_product_error_mapper,
            request_options=request_options,
        )


class AsyncWalletProductsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductResponse, ArchiveWalletProductErrorBody]:
        """Archives the Wallet Product. Refuses when an active Feature's ``wallet_behavior`` still points at it, or when
        it's used in a scheduled renewal. This protects Feature-provisioned wallets, but not a wallet created manually
        against this product: a manual wallet can be left denominated by an archived Wallet Product, and `Create Wallet
        Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__ doesn't check whether the billing product is archived
        before pricing and charging a purchase against it.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallet_products/{id}/archive.json"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletProductResponse],
            error_mapper=archive_wallet_product_error_mapper,
            request_options=request_options,
        )

    async def create_wallet_product(
        self,
        *,
        body: CreateWalletProductRequest | CreateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletProductResponse, CreateWalletProductErrorBody]:
        """Creates a Wallet Product: a billing product with no product family, meant to denominate wallets and to be
        purchased through `Create Wallet Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__. It's a Component
        under the hood, so it returns the full Component field set, and can optionally be priced with one or more price
        points in the same call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallet_products.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWalletProductRequest | CreateWalletProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletProductResponse],
            error_mapper=create_wallet_product_error_mapper,
            request_options=request_options,
        )

    async def list_wallet_products(
        self,
        *,
        include_archived: bool | None = None,
        status: Status1OrStr | None = None,
        q: str | None = None,
        sort_by: SortBy1OrStr | None = SortBy1.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletProductsListResponse, ListWalletProductsErrorBody]:
        """Lists the Wallet Products on your site.

        Args:
            include_archived: Includes archived Wallet Products in the result. Defaults to ``false``. Ignored when
                ``status`` is also sent.
            status: Restricts the result by status, and overrides ``include_archived`` when sent. An unrecognized value
                falls back to ``active`` rather than returning ``422``.
            q: Restricts the result to Wallet Products whose name, handle, or unit name contains this substring
                (case-insensitive).
            sort_by: The field to sort results by. An unrecognized value falls back to ``name``.
            sort_direction: The sort direction. Anything other than ``desc`` is treated as ``asc``.
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
            url_template=self._server.production("/wallet_products.json"),
            query_params=[
                param[bool | None]("include_archived", include_archived),
                param[Status1OrStr | None]("status", status),
                param[str | None]("q", q),
                param[SortBy1OrStr | None]("sort_by", sort_by),
                param[SortDirectionOrStr | None]("sort_direction", sort_direction),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletProductsListResponse],
            error_mapper=list_wallet_products_error_mapper,
            request_options=request_options,
        )

    async def read_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductResponse, ReadWalletProductErrorBody]:
        """Returns the Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallet_products/{id}.json"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletProductResponse],
            error_mapper=read_wallet_product_error_mapper,
            request_options=request_options,
        )

    async def read_wallet_product_usage(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductUsageResponse, ReadWalletProductUsageErrorBody]:
        """Returns everything drawing on this Wallet Product: the wallet templates billing through it, split into ones
        using its default price point and ones overriding it, plus a sample of up to 50 of the active wallets actually
        created from them. A wallet template can appear more than once in
        ``wallet_templates``/``price_point_overrides``, once per Feature and owning plan/component sharing it, so these
        arrays aren't one row per template.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/wallet_products/{id}/usage.json"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletProductUsageResponse],
            error_mapper=read_wallet_product_usage_error_mapper,
            request_options=request_options,
        )

    async def unarchive_wallet_product(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WalletProductResponse, UnarchiveWalletProductErrorBody]:
        """Restores an archived Wallet Product.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/wallet_products/{id}/unarchive.json"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletProductResponse],
            error_mapper=unarchive_wallet_product_error_mapper,
            request_options=request_options,
        )

    async def update_wallet_product(
        self,
        id_: str,
        *,
        body: UpdateWalletProductRequest | UpdateWalletProductRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WalletProductResponse, UpdateWalletProductErrorBody]:
        """Updates the Wallet Product's catalog-facing fields. Omitted fields are left unchanged. Unlike `Create Wallet
        Product <$e/Wallet%20Products/createWalletProduct>`__, this does not accept ``unit_name``, ``handle``,
        ``price_point``, or ``price_points``; see the request schema for which fields are actually mutable.

        Args:
            id_: The Advanced Billing id of the Wallet Product, or its handle prefixed with ``handle:`` (for example
                ``handle:token-pack``). A bare handle returns ``404``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/wallet_products/{id}.json"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateWalletProductRequest | UpdateWalletProductRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[WalletProductResponse],
            error_mapper=update_wallet_product_error_mapper,
            request_options=request_options,
        )
