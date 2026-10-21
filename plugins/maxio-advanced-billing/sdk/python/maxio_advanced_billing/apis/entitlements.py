from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.read_subscription_entitlements_error import (
    ReadSubscriptionEntitlementsErrorBody,
    read_subscription_entitlements_error_mapper,
)
from ..models.aggregated_entitlements_response import AggregatedEntitlementsResponse
from ..server.server import Server


class Entitlements:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EntitlementsWithRawResponse(client, server, auth)

    def read_subscription_entitlements(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AggregatedEntitlementsResponse:
        """Returns every feature a subscription is entitled to, collapsed into one entry per feature key and periodicity
        window across all products and components on the subscription. A ``usage_limit`` feature granted with two
        different periodicities comes back as two entries sharing one ``feature_key``, each identified by its own
        ``periodicity_key``.

        When more than one product or component grants the same feature key and periodicity, the values are combined:
        - **``access_right``** features are combined with a boolean OR. If any contributor grants access, the aggregate
            is ``true``. ``source_products`` only lists the contributors that granted ``true``.
        - **``usage_limit``** features are summed across every contributor sharing the same periodicity window.
            ``source_products`` lists every contributor. Grants with different periodicities are not summed together.
            Each periodicity is returned as a separate entry.
        - **``service_right``** features are not combined: one contributor's value wins. Do not rely on which one when
            several grant the same feature key.

        ``enabled`` reflects both the aggregated value and the subscription's state. The field is ``false`` whenever the
        subscription is not in a live state (``active``, ``trialing``, ``assessing``, ``past_due``, ``soft_failure``),
        regardless of the aggregated value. Entitlements deliberately stay enabled through dunning.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.read_subscription_entitlements(subscription_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> EntitlementsWithRawResponse:
        return self._with_raw_response


class AsyncEntitlements:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEntitlementsWithRawResponse(client, server, auth)

    async def read_subscription_entitlements(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> AggregatedEntitlementsResponse:
        """Returns every feature a subscription is entitled to, collapsed into one entry per feature key and periodicity
        window across all products and components on the subscription. A ``usage_limit`` feature granted with two
        different periodicities comes back as two entries sharing one ``feature_key``, each identified by its own
        ``periodicity_key``.

        When more than one product or component grants the same feature key and periodicity, the values are combined:
        - **``access_right``** features are combined with a boolean OR. If any contributor grants access, the aggregate
            is ``true``. ``source_products`` only lists the contributors that granted ``true``.
        - **``usage_limit``** features are summed across every contributor sharing the same periodicity window.
            ``source_products`` lists every contributor. Grants with different periodicities are not summed together.
            Each periodicity is returned as a separate entry.
        - **``service_right``** features are not combined: one contributor's value wins. Do not rely on which one when
            several grant the same feature key.

        ``enabled`` reflects both the aggregated value and the subscription's state. The field is ``false`` whenever the
        subscription is not in a live state (``active``, ``trialing``, ``assessing``, ``past_due``, ``soft_failure``),
        regardless of the aggregated value. Entitlements deliberately stay enabled through dunning.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.read_subscription_entitlements(
                subscription_id, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncEntitlementsWithRawResponse:
        return self._with_raw_response


class EntitlementsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def read_subscription_entitlements(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AggregatedEntitlementsResponse, ReadSubscriptionEntitlementsErrorBody]:
        """Returns every feature a subscription is entitled to, collapsed into one entry per feature key and periodicity
        window across all products and components on the subscription. A ``usage_limit`` feature granted with two
        different periodicities comes back as two entries sharing one ``feature_key``, each identified by its own
        ``periodicity_key``.

        When more than one product or component grants the same feature key and periodicity, the values are combined:
        - **``access_right``** features are combined with a boolean OR. If any contributor grants access, the aggregate
            is ``true``. ``source_products`` only lists the contributors that granted ``true``.
        - **``usage_limit``** features are summed across every contributor sharing the same periodicity window.
            ``source_products`` lists every contributor. Grants with different periodicities are not summed together.
            Each periodicity is returned as a separate entry.
        - **``service_right``** features are not combined: one contributor's value wins. Do not rely on which one when
            several grant the same feature key.

        ``enabled`` reflects both the aggregated value and the subscription's state. The field is ``false`` whenever the
        subscription is not in a live state (``active``, ``trialing``, ``assessing``, ``past_due``, ``soft_failure``),
        regardless of the aggregated value. Entitlements deliberately stay enabled through dunning.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/entitlements.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[AggregatedEntitlementsResponse],
            error_mapper=read_subscription_entitlements_error_mapper,
            request_options=request_options,
        )


class AsyncEntitlementsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def read_subscription_entitlements(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AggregatedEntitlementsResponse, ReadSubscriptionEntitlementsErrorBody]:
        """Returns every feature a subscription is entitled to, collapsed into one entry per feature key and periodicity
        window across all products and components on the subscription. A ``usage_limit`` feature granted with two
        different periodicities comes back as two entries sharing one ``feature_key``, each identified by its own
        ``periodicity_key``.

        When more than one product or component grants the same feature key and periodicity, the values are combined:
        - **``access_right``** features are combined with a boolean OR. If any contributor grants access, the aggregate
            is ``true``. ``source_products`` only lists the contributors that granted ``true``.
        - **``usage_limit``** features are summed across every contributor sharing the same periodicity window.
            ``source_products`` lists every contributor. Grants with different periodicities are not summed together.
            Each periodicity is returned as a separate entry.
        - **``service_right``** features are not combined: one contributor's value wins. Do not rely on which one when
            several grant the same feature key.

        ``enabled`` reflects both the aggregated value and the subscription's state. The field is ``false`` whenever the
        subscription is not in a live state (``active``, ``trialing``, ``assessing``, ``past_due``, ``soft_failure``),
        regardless of the aggregated value. Entitlements deliberately stay enabled through dunning.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/entitlements.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[AggregatedEntitlementsResponse],
            error_mapper=read_subscription_entitlements_error_mapper,
            request_options=request_options,
        )
