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
from ..errors.migrate_subscription_product_error import (
    MigrateSubscriptionProductErrorBody,
    migrate_subscription_product_error_mapper,
)
from ..errors.preview_subscription_product_migration_error import (
    PreviewSubscriptionProductMigrationErrorBody,
    preview_subscription_product_migration_error_mapper,
)
from ..models.subscription_migration_preview_request import (
    SubscriptionMigrationPreviewRequest,
    SubscriptionMigrationPreviewRequestDict,
)
from ..models.subscription_migration_preview_response import SubscriptionMigrationPreviewResponse
from ..models.subscription_product_migration_request import (
    SubscriptionProductMigrationRequest,
    SubscriptionProductMigrationRequestDict,
)
from ..models.subscription_response import SubscriptionResponse
from ..server.server import Server


class SubscriptionProducts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionProductsWithRawResponse(client, server, auth)

    def migrate_subscription_product(
        self,
        subscription_id: int,
        *,
        body: SubscriptionProductMigrationRequest | SubscriptionProductMigrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Migrates a subscription to a different product.

        To create a migration, you must pass the ``product_id`` or ``product_handle`` in the object when you send a POST
        request. You can also pass either a ``product_price_point_id`` or ``product_price_point_handle`` to choose which
        price point the subscription is moved to. If no price point identifier is passed, the subscription is moved to
        the product's default price point. The response is the updated subscription.

        ## Valid Subscriptions

        Subscriptions should be in the ``active`` or ``trialing`` state to be migrated.

        (For backwards compatibility reasons, it is possible to migrate a subscription that is in the ``trial_ended``
        state via the API, however this is not recommended. Since ``trial_ended`` is an end-of-life state, the
        subscription should be canceled, the product changed, and then the subscription can be reactivated.)

        For more information, see `Product Changes and Migrations
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__.

        ## Failed Migrations

        Important note: One of the most common ways that a migration can fail is when the attempt is made to migrate a
        subscription to its current product.

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
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.migrate_subscription_product(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def preview_subscription_product_migration(
        self,
        subscription_id: int,
        *,
        body: SubscriptionMigrationPreviewRequest | SubscriptionMigrationPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionMigrationPreviewResponse:
        """Previews the charges resulting from migrating a subscription to a different product.

        ## Previewing a future date It is also possible to preview the migration for a date in the future, as long as
        it's still within the subscription's current billing period, by passing a ``proration_date`` along with the
        request (e.g., ``"proration_date": "2020-12-18T18:25:43.511Z"``).

        This will calculate the prorated adjustment, charge, payment and credit applied values assuming the migration is
        done at that date in the future as opposed to right now.

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
            self._with_raw_response.preview_subscription_product_migration(
                subscription_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SubscriptionProductsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionProducts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionProductsWithRawResponse(client, server, auth)

    async def migrate_subscription_product(
        self,
        subscription_id: int,
        *,
        body: SubscriptionProductMigrationRequest | SubscriptionProductMigrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Migrates a subscription to a different product.

        To create a migration, you must pass the ``product_id`` or ``product_handle`` in the object when you send a POST
        request. You can also pass either a ``product_price_point_id`` or ``product_price_point_handle`` to choose which
        price point the subscription is moved to. If no price point identifier is passed, the subscription is moved to
        the product's default price point. The response is the updated subscription.

        ## Valid Subscriptions

        Subscriptions should be in the ``active`` or ``trialing`` state to be migrated.

        (For backwards compatibility reasons, it is possible to migrate a subscription that is in the ``trial_ended``
        state via the API, however this is not recommended. Since ``trial_ended`` is an end-of-life state, the
        subscription should be canceled, the product changed, and then the subscription can be reactivated.)

        For more information, see `Product Changes and Migrations
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__.

        ## Failed Migrations

        Important note: One of the most common ways that a migration can fail is when the attempt is made to migrate a
        subscription to its current product.

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
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.migrate_subscription_product(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def preview_subscription_product_migration(
        self,
        subscription_id: int,
        *,
        body: SubscriptionMigrationPreviewRequest | SubscriptionMigrationPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionMigrationPreviewResponse:
        """Previews the charges resulting from migrating a subscription to a different product.

        ## Previewing a future date It is also possible to preview the migration for a date in the future, as long as
        it's still within the subscription's current billing period, by passing a ``proration_date`` along with the
        request (e.g., ``"proration_date": "2020-12-18T18:25:43.511Z"``).

        This will calculate the prorated adjustment, charge, payment and credit applied values assuming the migration is
        done at that date in the future as opposed to right now.

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
            await self._with_raw_response.preview_subscription_product_migration(
                subscription_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionProductsWithRawResponse:
        return self._with_raw_response


class SubscriptionProductsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def migrate_subscription_product(
        self,
        subscription_id: int,
        *,
        body: SubscriptionProductMigrationRequest | SubscriptionProductMigrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, MigrateSubscriptionProductErrorBody]:
        """Migrates a subscription to a different product.

        To create a migration, you must pass the ``product_id`` or ``product_handle`` in the object when you send a POST
        request. You can also pass either a ``product_price_point_id`` or ``product_price_point_handle`` to choose which
        price point the subscription is moved to. If no price point identifier is passed, the subscription is moved to
        the product's default price point. The response is the updated subscription.

        ## Valid Subscriptions

        Subscriptions should be in the ``active`` or ``trialing`` state to be migrated.

        (For backwards compatibility reasons, it is possible to migrate a subscription that is in the ``trial_ended``
        state via the API, however this is not recommended. Since ``trial_ended`` is an end-of-life state, the
        subscription should be canceled, the product changed, and then the subscription can be reactivated.)

        For more information, see `Product Changes and Migrations
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__.

        ## Failed Migrations

        Important note: One of the most common ways that a migration can fail is when the attempt is made to migrate a
        subscription to its current product.

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
            url_template=self._server.production("/subscriptions/{subscription_id}/migrations.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionProductMigrationRequest | SubscriptionProductMigrationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=migrate_subscription_product_error_mapper,
            request_options=request_options,
        )

    def preview_subscription_product_migration(
        self,
        subscription_id: int,
        *,
        body: SubscriptionMigrationPreviewRequest | SubscriptionMigrationPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionMigrationPreviewResponse, PreviewSubscriptionProductMigrationErrorBody]:
        """Previews the charges resulting from migrating a subscription to a different product.

        ## Previewing a future date It is also possible to preview the migration for a date in the future, as long as
        it's still within the subscription's current billing period, by passing a ``proration_date`` along with the
        request (e.g., ``"proration_date": "2020-12-18T18:25:43.511Z"``).

        This will calculate the prorated adjustment, charge, payment and credit applied values assuming the migration is
        done at that date in the future as opposed to right now.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/migrations/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionMigrationPreviewRequest | SubscriptionMigrationPreviewRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionMigrationPreviewResponse],
            error_mapper=preview_subscription_product_migration_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionProductsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def migrate_subscription_product(
        self,
        subscription_id: int,
        *,
        body: SubscriptionProductMigrationRequest | SubscriptionProductMigrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, MigrateSubscriptionProductErrorBody]:
        """Migrates a subscription to a different product.

        To create a migration, you must pass the ``product_id`` or ``product_handle`` in the object when you send a POST
        request. You can also pass either a ``product_price_point_id`` or ``product_price_point_handle`` to choose which
        price point the subscription is moved to. If no price point identifier is passed, the subscription is moved to
        the product's default price point. The response is the updated subscription.

        ## Valid Subscriptions

        Subscriptions should be in the ``active`` or ``trialing`` state to be migrated.

        (For backwards compatibility reasons, it is possible to migrate a subscription that is in the ``trial_ended``
        state via the API, however this is not recommended. Since ``trial_ended`` is an end-of-life state, the
        subscription should be canceled, the product changed, and then the subscription can be reactivated.)

        For more information, see `Product Changes and Migrations
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations>`__.

        ## Failed Migrations

        Important note: One of the most common ways that a migration can fail is when the attempt is made to migrate a
        subscription to its current product.

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
            url_template=self._server.production("/subscriptions/{subscription_id}/migrations.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionProductMigrationRequest | SubscriptionProductMigrationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=migrate_subscription_product_error_mapper,
            request_options=request_options,
        )

    async def preview_subscription_product_migration(
        self,
        subscription_id: int,
        *,
        body: SubscriptionMigrationPreviewRequest | SubscriptionMigrationPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionMigrationPreviewResponse, PreviewSubscriptionProductMigrationErrorBody]:
        """Previews the charges resulting from migrating a subscription to a different product.

        ## Previewing a future date It is also possible to preview the migration for a date in the future, as long as
        it's still within the subscription's current billing period, by passing a ``proration_date`` along with the
        request (e.g., ``"proration_date": "2020-12-18T18:25:43.511Z"``).

        This will calculate the prorated adjustment, charge, payment and credit applied values assuming the migration is
        done at that date in the future as opposed to right now.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/migrations/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionMigrationPreviewRequest | SubscriptionMigrationPreviewRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionMigrationPreviewResponse],
            error_mapper=preview_subscription_product_migration_error_mapper,
            request_options=request_options,
        )
