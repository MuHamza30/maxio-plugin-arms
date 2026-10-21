from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_component_feature_error import (
    CreateComponentFeatureErrorBody,
    create_component_feature_error_mapper,
)
from ..errors.list_component_features_error import ListComponentFeaturesErrorBody, list_component_features_error_mapper
from ..errors.read_component_feature_error import ReadComponentFeatureErrorBody, read_component_feature_error_mapper
from ..errors.remove_component_feature_error import (
    RemoveComponentFeatureErrorBody,
    remove_component_feature_error_mapper,
)
from ..errors.restore_component_feature_error import (
    RestoreComponentFeatureErrorBody,
    restore_component_feature_error_mapper,
)
from ..errors.update_component_feature_error import (
    UpdateComponentFeatureErrorBody,
    update_component_feature_error_mapper,
)
from ..models.create_feature_catalog_item_request import (
    CreateFeatureCatalogItemRequest,
    CreateFeatureCatalogItemRequestDict,
)
from ..models.feature_catalog_item_response import FeatureCatalogItemResponse
from ..models.feature_catalog_items_list_response import FeatureCatalogItemsListResponse
from ..models.update_feature_catalog_item_request import (
    UpdateFeatureCatalogItemRequest,
    UpdateFeatureCatalogItemRequestDict,
)
from ..server.server import Server


class ComponentFeatures:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ComponentFeaturesWithRawResponse(client, server, auth)

    def create_component_feature(
        self,
        component_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Attaches a feature template to this component with a concrete value. Pass ``price_point_type: "PricePoint"``
        and ``price_point_id`` to create an override scoped to a single component price point instead of the whole
        component.

        Args:
            component_id: The Advanced Billing id of the component.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.create_component_feature(component_id, body=body, request_options=request_options)
        )

    def list_component_features(
        self, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemsListResponse:
        """Lists the feature catalog items attached to this component, including price-point-specific overrides.

        Args:
            component_id: The Advanced Billing id of the component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.list_component_features(component_id, request_options=request_options))

    def read_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Returns a single feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.read_component_feature(component_id, id_, request_options=request_options)
        )

    def remove_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes a feature catalog item from this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            destroy_entitlements: When ``true``, permanently deletes this feature catalog item and every entitlement it
                created, revoking subscriber access immediately. When ``false`` (default), the feature catalog item is
                archived and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.remove_component_feature(
                component_id, id_, destroy_entitlements=destroy_entitlements, request_options=request_options
            ),
        )

    def restore_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Clears the archived state of a feature catalog item attached to this component. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.restore_component_feature(component_id, id_, request_options=request_options)
        )

    def update_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Updates the value or periodicity of a feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.update_component_feature(
                component_id, id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ComponentFeaturesWithRawResponse:
        return self._with_raw_response


class AsyncComponentFeatures:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncComponentFeaturesWithRawResponse(client, server, auth)

    async def create_component_feature(
        self,
        component_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Attaches a feature template to this component with a concrete value. Pass ``price_point_type: "PricePoint"``
        and ``price_point_id`` to create an override scoped to a single component price point instead of the whole
        component.

        Args:
            component_id: The Advanced Billing id of the component.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.create_component_feature(
                component_id, body=body, request_options=request_options
            ),
        )

    async def list_component_features(
        self, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemsListResponse:
        """Lists the feature catalog items attached to this component, including price-point-specific overrides.

        Args:
            component_id: The Advanced Billing id of the component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_component_features(component_id, request_options=request_options)
        )

    async def read_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Returns a single feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.read_component_feature(component_id, id_, request_options=request_options)
        )

    async def remove_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes a feature catalog item from this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            destroy_entitlements: When ``true``, permanently deletes this feature catalog item and every entitlement it
                created, revoking subscriber access immediately. When ``false`` (default), the feature catalog item is
                archived and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.remove_component_feature(
                component_id, id_, destroy_entitlements=destroy_entitlements, request_options=request_options
            ),
        )

    async def restore_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Clears the archived state of a feature catalog item attached to this component. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.restore_component_feature(component_id, id_, request_options=request_options)
        )

    async def update_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Updates the value or periodicity of a feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_component_feature(
                component_id, id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncComponentFeaturesWithRawResponse:
        return self._with_raw_response


class ComponentFeaturesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_component_feature(
        self,
        component_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, CreateComponentFeatureErrorBody]:
        """Attaches a feature template to this component with a concrete value. Pass ``price_point_type: "PricePoint"``
        and ``price_point_id`` to create an override scoped to a single component price point instead of the whole
        component.

        Args:
            component_id: The Advanced Billing id of the component.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/features.json"),
            path_params=[param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=create_component_feature_error_mapper,
            request_options=request_options,
        )

    def list_component_features(
        self, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemsListResponse, ListComponentFeaturesErrorBody]:
        """Lists the feature catalog items attached to this component, including price-point-specific overrides.

        Args:
            component_id: The Advanced Billing id of the component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/features.json"),
            path_params=[param[int]("component_id", component_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemsListResponse],
            error_mapper=list_component_features_error_mapper,
            request_options=request_options,
        )

    def read_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, ReadComponentFeatureErrorBody]:
        """Returns a single feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/features/{id}.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=read_component_feature_error_mapper,
            request_options=request_options,
        )

    def remove_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveComponentFeatureErrorBody]:
        """Removes a feature catalog item from this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            destroy_entitlements: When ``true``, permanently deletes this feature catalog item and every entitlement it
                created, revoking subscriber access immediately. When ``false`` (default), the feature catalog item is
                archived and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/components/{component_id}/features/{id}.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            query_params=[param[bool | None]("destroy_entitlements", destroy_entitlements)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=remove_component_feature_error_mapper,
            request_options=request_options,
        )

    def restore_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, RestoreComponentFeatureErrorBody]:
        """Clears the archived state of a feature catalog item attached to this component. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/features/{id}/restore.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=restore_component_feature_error_mapper,
            request_options=request_options,
        )

    def update_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, UpdateComponentFeatureErrorBody]:
        """Updates the value or periodicity of a feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/components/{component_id}/features/{id}.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=update_component_feature_error_mapper,
            request_options=request_options,
        )


class AsyncComponentFeaturesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_component_feature(
        self,
        component_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, CreateComponentFeatureErrorBody]:
        """Attaches a feature template to this component with a concrete value. Pass ``price_point_type: "PricePoint"``
        and ``price_point_id`` to create an override scoped to a single component price point instead of the whole
        component.

        Args:
            component_id: The Advanced Billing id of the component.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/features.json"),
            path_params=[param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=create_component_feature_error_mapper,
            request_options=request_options,
        )

    async def list_component_features(
        self, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemsListResponse, ListComponentFeaturesErrorBody]:
        """Lists the feature catalog items attached to this component, including price-point-specific overrides.

        Args:
            component_id: The Advanced Billing id of the component.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/features.json"),
            path_params=[param[int]("component_id", component_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemsListResponse],
            error_mapper=list_component_features_error_mapper,
            request_options=request_options,
        )

    async def read_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, ReadComponentFeatureErrorBody]:
        """Returns a single feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/{component_id}/features/{id}.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=read_component_feature_error_mapper,
            request_options=request_options,
        )

    async def remove_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveComponentFeatureErrorBody]:
        """Removes a feature catalog item from this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            destroy_entitlements: When ``true``, permanently deletes this feature catalog item and every entitlement it
                created, revoking subscriber access immediately. When ``false`` (default), the feature catalog item is
                archived and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/components/{component_id}/features/{id}.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            query_params=[param[bool | None]("destroy_entitlements", destroy_entitlements)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=remove_component_feature_error_mapper,
            request_options=request_options,
        )

    async def restore_component_feature(
        self, component_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, RestoreComponentFeatureErrorBody]:
        """Clears the archived state of a feature catalog item attached to this component. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/components/{component_id}/features/{id}/restore.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=restore_component_feature_error_mapper,
            request_options=request_options,
        )

    async def update_component_feature(
        self,
        component_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, UpdateComponentFeatureErrorBody]:
        """Updates the value or periodicity of a feature catalog item attached to this component.

        Args:
            component_id: The Advanced Billing id of the component.
            id_: The Advanced Billing id of the feature catalog item.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/components/{component_id}/features/{id}.json"),
            path_params=[param[int]("component_id", component_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=update_component_feature_error_mapper,
            request_options=request_options,
        )
