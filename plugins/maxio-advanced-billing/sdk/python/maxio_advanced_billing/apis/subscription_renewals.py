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
from ..errors.cancel_scheduled_renewal_configuration_error import (
    CancelScheduledRenewalConfigurationErrorBody,
    cancel_scheduled_renewal_configuration_error_mapper,
)
from ..errors.create_scheduled_renewal_configuration_error import (
    CreateScheduledRenewalConfigurationErrorBody,
    create_scheduled_renewal_configuration_error_mapper,
)
from ..errors.create_scheduled_renewal_configuration_item_error import (
    CreateScheduledRenewalConfigurationItemErrorBody,
    create_scheduled_renewal_configuration_item_error_mapper,
)
from ..errors.delete_scheduled_renewal_configuration_item_error import (
    DeleteScheduledRenewalConfigurationItemErrorBody,
    delete_scheduled_renewal_configuration_item_error_mapper,
)
from ..errors.lock_in_scheduled_renewal_immediately_error import (
    LockInScheduledRenewalImmediatelyErrorBody,
    lock_in_scheduled_renewal_immediately_error_mapper,
)
from ..errors.schedule_scheduled_renewal_lock_in_error import (
    ScheduleScheduledRenewalLockInErrorBody,
    schedule_scheduled_renewal_lock_in_error_mapper,
)
from ..errors.unpublish_scheduled_renewal_configuration_error import (
    UnpublishScheduledRenewalConfigurationErrorBody,
    unpublish_scheduled_renewal_configuration_error_mapper,
)
from ..errors.update_scheduled_renewal_configuration_error import (
    UpdateScheduledRenewalConfigurationErrorBody,
    update_scheduled_renewal_configuration_error_mapper,
)
from ..errors.update_scheduled_renewal_configuration_item_error import (
    UpdateScheduledRenewalConfigurationItemErrorBody,
    update_scheduled_renewal_configuration_item_error_mapper,
)
from ..models.enums.status import StatusOrStr
from ..models.scheduled_renewal_configuration_item_request import (
    ScheduledRenewalConfigurationItemRequest,
    ScheduledRenewalConfigurationItemRequestDict,
)
from ..models.scheduled_renewal_configuration_item_response import ScheduledRenewalConfigurationItemResponse
from ..models.scheduled_renewal_configuration_request import (
    ScheduledRenewalConfigurationRequest,
    ScheduledRenewalConfigurationRequestDict,
)
from ..models.scheduled_renewal_configuration_response import ScheduledRenewalConfigurationResponse
from ..models.scheduled_renewal_configurations_response import ScheduledRenewalConfigurationsResponse
from ..models.scheduled_renewal_lock_in_request import ScheduledRenewalLockInRequest, ScheduledRenewalLockInRequestDict
from ..models.scheduled_renewal_update_request import ScheduledRenewalUpdateRequest, ScheduledRenewalUpdateRequestDict
from ..server.server import Server


class SubscriptionRenewals:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionRenewalsWithRawResponse(client, server, auth)

    def cancel_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Cancels a scheduled renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.cancel_scheduled_renewal_configuration(
                subscription_id, id_, request_options=request_options
            ),
        )

    def create_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationResponse:
        """Creates a scheduled renewal configuration for a subscription. The scheduled renewal is based on the
        subscription’s current product and component setup.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_scheduled_renewal_configuration(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def create_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        *,
        body: ScheduledRenewalConfigurationItemRequest | ScheduledRenewalConfigurationItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationItemResponse:
        """Adds product and component line items to the scheduled renewal.

        If your site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_scheduled_renewal_configuration_item(
                subscription_id, scheduled_renewals_configuration_id, body=body, request_options=request_options
            ),
        )

    def delete_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes an item from the pending renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.delete_scheduled_renewal_configuration_item(
                subscription_id, scheduled_renewals_configuration_id, id_, request_options=request_options
            ),
        )

    def list_scheduled_renewal_configurations(
        self,
        subscription_id: int,
        *,
        status: StatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationsResponse:
        """Lists scheduled renewal configurations for the subscription and permits an optional status query filter.

        Args:
            subscription_id: The Chargify id of the subscription.
            status: (Optional) Status filter for scheduled renewal configurations.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_scheduled_renewal_configurations(
                subscription_id, status=status, request_options=request_options
            ),
        )

    def lock_in_scheduled_renewal_immediately(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Locks in the renewal immediately.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.lock_in_scheduled_renewal_immediately(
                subscription_id, id_, request_options=request_options
            ),
        )

    def read_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Retrieves the configuration settings for the scheduled renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_scheduled_renewal_configuration(
                subscription_id, id_, request_options=request_options
            ),
        )

    def schedule_scheduled_renewal_lock_in(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalLockInRequest | ScheduledRenewalLockInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationResponse:
        """Schedules a future lock-in date for the renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.schedule_scheduled_renewal_lock_in(
                subscription_id, id_, body=body, request_options=request_options
            ),
        )

    def unpublish_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Restores a scheduled renewal configuration to an editable state.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.unpublish_scheduled_renewal_configuration(
                subscription_id, id_, request_options=request_options
            ),
        )

    def update_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationResponse:
        """Updates an existing configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_scheduled_renewal_configuration(
                subscription_id, id_, body=body, request_options=request_options
            ),
        )

    def update_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        body: ScheduledRenewalUpdateRequest | ScheduledRenewalUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationItemResponse:
        """Updates an existing configuration item’s pricing and quantity.

        If you site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_scheduled_renewal_configuration_item(
                subscription_id, scheduled_renewals_configuration_id, id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SubscriptionRenewalsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionRenewals:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionRenewalsWithRawResponse(client, server, auth)

    async def cancel_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Cancels a scheduled renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_scheduled_renewal_configuration(
                subscription_id, id_, request_options=request_options
            ),
        )

    async def create_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationResponse:
        """Creates a scheduled renewal configuration for a subscription. The scheduled renewal is based on the
        subscription’s current product and component setup.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_scheduled_renewal_configuration(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def create_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        *,
        body: ScheduledRenewalConfigurationItemRequest | ScheduledRenewalConfigurationItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationItemResponse:
        """Adds product and component line items to the scheduled renewal.

        If your site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_scheduled_renewal_configuration_item(
                subscription_id, scheduled_renewals_configuration_id, body=body, request_options=request_options
            ),
        )

    async def delete_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes an item from the pending renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_scheduled_renewal_configuration_item(
                subscription_id, scheduled_renewals_configuration_id, id_, request_options=request_options
            ),
        )

    async def list_scheduled_renewal_configurations(
        self,
        subscription_id: int,
        *,
        status: StatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationsResponse:
        """Lists scheduled renewal configurations for the subscription and permits an optional status query filter.

        Args:
            subscription_id: The Chargify id of the subscription.
            status: (Optional) Status filter for scheduled renewal configurations.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_scheduled_renewal_configurations(
                subscription_id, status=status, request_options=request_options
            ),
        )

    async def lock_in_scheduled_renewal_immediately(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Locks in the renewal immediately.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.lock_in_scheduled_renewal_immediately(
                subscription_id, id_, request_options=request_options
            ),
        )

    async def read_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Retrieves the configuration settings for the scheduled renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_scheduled_renewal_configuration(
                subscription_id, id_, request_options=request_options
            ),
        )

    async def schedule_scheduled_renewal_lock_in(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalLockInRequest | ScheduledRenewalLockInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationResponse:
        """Schedules a future lock-in date for the renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.schedule_scheduled_renewal_lock_in(
                subscription_id, id_, body=body, request_options=request_options
            ),
        )

    async def unpublish_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScheduledRenewalConfigurationResponse:
        """Restores a scheduled renewal configuration to an editable state.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.unpublish_scheduled_renewal_configuration(
                subscription_id, id_, request_options=request_options
            ),
        )

    async def update_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationResponse:
        """Updates an existing configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_scheduled_renewal_configuration(
                subscription_id, id_, body=body, request_options=request_options
            ),
        )

    async def update_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        body: ScheduledRenewalUpdateRequest | ScheduledRenewalUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduledRenewalConfigurationItemResponse:
        """Updates an existing configuration item’s pricing and quantity.

        If you site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_scheduled_renewal_configuration_item(
                subscription_id, scheduled_renewals_configuration_id, id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionRenewalsWithRawResponse:
        return self._with_raw_response


class SubscriptionRenewalsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, CancelScheduledRenewalConfigurationErrorBody]:
        """Cancels a scheduled renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/cancel.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=cancel_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    def create_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, CreateScheduledRenewalConfigurationErrorBody]:
        """Creates a scheduled renewal configuration for a subscription. The scheduled renewal is based on the
        subscription’s current product and component setup.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None](
                body
            ),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=create_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    def create_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        *,
        body: ScheduledRenewalConfigurationItemRequest | ScheduledRenewalConfigurationItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationItemResponse, CreateScheduledRenewalConfigurationItemErrorBody]:
        """Adds product and component line items to the scheduled renewal.

        If your site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items.json",
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("scheduled_renewals_configuration_id", scheduled_renewals_configuration_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                ScheduledRenewalConfigurationItemRequest | ScheduledRenewalConfigurationItemRequestDict | None
            ](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationItemResponse],
            error_mapper=create_scheduled_renewal_configuration_item_error_mapper,
            request_options=request_options,
        )

    def delete_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteScheduledRenewalConfigurationItemErrorBody]:
        """Removes an item from the pending renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json",
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("scheduled_renewals_configuration_id", scheduled_renewals_configuration_id),
                param[int]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_scheduled_renewal_configuration_item_error_mapper,
            request_options=request_options,
        )

    def list_scheduled_renewal_configurations(
        self,
        subscription_id: int,
        *,
        status: StatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationsResponse, RawError]:
        """Lists scheduled renewal configurations for the subscription and permits an optional status query filter.

        Args:
            subscription_id: The Chargify id of the subscription.
            status: (Optional) Status filter for scheduled renewal configurations.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[StatusOrStr | None]("status", status)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def lock_in_scheduled_renewal_immediately(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, LockInScheduledRenewalImmediatelyErrorBody]:
        """Locks in the renewal immediately.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/immediate_lock_in.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=lock_in_scheduled_renewal_immediately_error_mapper,
            request_options=request_options,
        )

    def read_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, RawError]:
        """Retrieves the configuration settings for the scheduled renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals/{id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def schedule_scheduled_renewal_lock_in(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalLockInRequest | ScheduledRenewalLockInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, ScheduleScheduledRenewalLockInErrorBody]:
        """Schedules a future lock-in date for the renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/schedule_lock_in.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalLockInRequest | ScheduledRenewalLockInRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=schedule_scheduled_renewal_lock_in_error_mapper,
            request_options=request_options,
        )

    def unpublish_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, UnpublishScheduledRenewalConfigurationErrorBody]:
        """Restores a scheduled renewal configuration to an editable state.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/unpublish.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=unpublish_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    def update_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, UpdateScheduledRenewalConfigurationErrorBody]:
        """Updates an existing configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals/{id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None](
                body
            ),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=update_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    def update_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        body: ScheduledRenewalUpdateRequest | ScheduledRenewalUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationItemResponse, UpdateScheduledRenewalConfigurationItemErrorBody]:
        """Updates an existing configuration item’s pricing and quantity.

        If you site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json",
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("scheduled_renewals_configuration_id", scheduled_renewals_configuration_id),
                param[int]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalUpdateRequest | ScheduledRenewalUpdateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ScheduledRenewalConfigurationItemResponse],
            error_mapper=update_scheduled_renewal_configuration_item_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionRenewalsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, CancelScheduledRenewalConfigurationErrorBody]:
        """Cancels a scheduled renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/cancel.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=cancel_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    async def create_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, CreateScheduledRenewalConfigurationErrorBody]:
        """Creates a scheduled renewal configuration for a subscription. The scheduled renewal is based on the
        subscription’s current product and component setup.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None](
                body
            ),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=create_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    async def create_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        *,
        body: ScheduledRenewalConfigurationItemRequest | ScheduledRenewalConfigurationItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationItemResponse, CreateScheduledRenewalConfigurationItemErrorBody]:
        """Adds product and component line items to the scheduled renewal.

        If your site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items.json",
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("scheduled_renewals_configuration_id", scheduled_renewals_configuration_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                ScheduledRenewalConfigurationItemRequest | ScheduledRenewalConfigurationItemRequestDict | None
            ](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationItemResponse],
            error_mapper=create_scheduled_renewal_configuration_item_error_mapper,
            request_options=request_options,
        )

    async def delete_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteScheduledRenewalConfigurationItemErrorBody]:
        """Removes an item from the pending renewal configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json",
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("scheduled_renewals_configuration_id", scheduled_renewals_configuration_id),
                param[int]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_scheduled_renewal_configuration_item_error_mapper,
            request_options=request_options,
        )

    async def list_scheduled_renewal_configurations(
        self,
        subscription_id: int,
        *,
        status: StatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationsResponse, RawError]:
        """Lists scheduled renewal configurations for the subscription and permits an optional status query filter.

        Args:
            subscription_id: The Chargify id of the subscription.
            status: (Optional) Status filter for scheduled renewal configurations.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[StatusOrStr | None]("status", status)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def lock_in_scheduled_renewal_immediately(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, LockInScheduledRenewalImmediatelyErrorBody]:
        """Locks in the renewal immediately.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/immediate_lock_in.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=lock_in_scheduled_renewal_immediately_error_mapper,
            request_options=request_options,
        )

    async def read_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, RawError]:
        """Retrieves the configuration settings for the scheduled renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals/{id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def schedule_scheduled_renewal_lock_in(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalLockInRequest | ScheduledRenewalLockInRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, ScheduleScheduledRenewalLockInErrorBody]:
        """Schedules a future lock-in date for the renewal.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/schedule_lock_in.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalLockInRequest | ScheduledRenewalLockInRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=schedule_scheduled_renewal_lock_in_error_mapper,
            request_options=request_options,
        )

    async def unpublish_scheduled_renewal_configuration(
        self, subscription_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, UnpublishScheduledRenewalConfigurationErrorBody]:
        """Restores a scheduled renewal configuration to an editable state.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{id}/unpublish.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=unpublish_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    async def update_scheduled_renewal_configuration(
        self,
        subscription_id: int,
        id_: int,
        *,
        body: ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationResponse, UpdateScheduledRenewalConfigurationErrorBody]:
        """Updates an existing configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            id_: The renewal id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/scheduled_renewals/{id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalConfigurationRequest | ScheduledRenewalConfigurationRequestDict | None](
                body
            ),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationResponse],
            error_mapper=update_scheduled_renewal_configuration_error_mapper,
            request_options=request_options,
        )

    async def update_scheduled_renewal_configuration_item(
        self,
        subscription_id: int,
        scheduled_renewals_configuration_id: int,
        id_: int,
        *,
        body: ScheduledRenewalUpdateRequest | ScheduledRenewalUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduledRenewalConfigurationItemResponse, UpdateScheduledRenewalConfigurationItemErrorBody]:
        """Updates an existing configuration item’s pricing and quantity.

        If you site has list vs sales pricing enabled, accepts
        renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted value follows
        existing/default behavior; with list vs sales pricing disabled, parameter is ignored (no validation/behavioral
        impact). This functionality is supported in the API, but is not currently supported in SDKs.

        Args:
            subscription_id: The Chargify id of the subscription.
            scheduled_renewals_configuration_id: The scheduled renewal configuration id.
            id_: The scheduled renewal configuration item id.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json",
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("scheduled_renewals_configuration_id", scheduled_renewals_configuration_id),
                param[int]("id", id_),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduledRenewalUpdateRequest | ScheduledRenewalUpdateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ScheduledRenewalConfigurationItemResponse],
            error_mapper=update_scheduled_renewal_configuration_item_error_mapper,
            request_options=request_options,
        )
