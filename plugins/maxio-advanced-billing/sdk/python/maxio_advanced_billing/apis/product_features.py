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
from ..errors.create_product_feature_error import CreateProductFeatureErrorBody, create_product_feature_error_mapper
from ..errors.list_product_features_error import ListProductFeaturesErrorBody, list_product_features_error_mapper
from ..errors.read_product_feature_error import ReadProductFeatureErrorBody, read_product_feature_error_mapper
from ..errors.remove_product_feature_error import RemoveProductFeatureErrorBody, remove_product_feature_error_mapper
from ..errors.restore_product_feature_error import RestoreProductFeatureErrorBody, restore_product_feature_error_mapper
from ..errors.update_product_feature_error import UpdateProductFeatureErrorBody, update_product_feature_error_mapper
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


class ProductFeatures:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProductFeaturesWithRawResponse(client, server, auth)

    def create_product_feature(
        self,
        product_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Attaches a feature template to this product with a concrete value. Pass ``price_point_type:
        "ProductPricePoint"`` and ``price_point_id`` to create an override scoped to a single product price point
        instead of the whole product.

        Args:
            product_id: The Advanced Billing id of the product.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.create_product_feature(product_id, body=body, request_options=request_options)
        )

    def list_product_features(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemsListResponse:
        """Lists the feature catalog items attached to this product, including price-point-specific overrides.

        Args:
            product_id: The Advanced Billing id of the product.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.list_product_features(product_id, request_options=request_options))

    def read_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Returns a single feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.read_product_feature(product_id, id_, request_options=request_options))

    def remove_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes a feature catalog item from this product.

        Args:
            product_id: The Advanced Billing id of the product.
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
            self._with_raw_response.remove_product_feature(
                product_id, id_, destroy_entitlements=destroy_entitlements, request_options=request_options
            ),
        )

    def restore_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Clears the archived state of a feature catalog item attached to this product. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.restore_product_feature(product_id, id_, request_options=request_options))

    def update_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Updates the value or periodicity of a feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
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
            self._with_raw_response.update_product_feature(product_id, id_, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> ProductFeaturesWithRawResponse:
        return self._with_raw_response


class AsyncProductFeatures:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductFeaturesWithRawResponse(client, server, auth)

    async def create_product_feature(
        self,
        product_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Attaches a feature template to this product with a concrete value. Pass ``price_point_type:
        "ProductPricePoint"`` and ``price_point_id`` to create an override scoped to a single product price point
        instead of the whole product.

        Args:
            product_id: The Advanced Billing id of the product.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.create_product_feature(product_id, body=body, request_options=request_options)
        )

    async def list_product_features(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemsListResponse:
        """Lists the feature catalog items attached to this product, including price-point-specific overrides.

        Args:
            product_id: The Advanced Billing id of the product.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.list_product_features(product_id, request_options=request_options))

    async def read_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Returns a single feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.read_product_feature(product_id, id_, request_options=request_options)
        )

    async def remove_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Removes a feature catalog item from this product.

        Args:
            product_id: The Advanced Billing id of the product.
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
            await self._with_raw_response.remove_product_feature(
                product_id, id_, destroy_entitlements=destroy_entitlements, request_options=request_options
            ),
        )

    async def restore_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureCatalogItemResponse:
        """Clears the archived state of a feature catalog item attached to this product. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.restore_product_feature(product_id, id_, request_options=request_options)
        )

    async def update_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureCatalogItemResponse:
        """Updates the value or periodicity of a feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
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
            await self._with_raw_response.update_product_feature(
                product_id, id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncProductFeaturesWithRawResponse:
        return self._with_raw_response


class ProductFeaturesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_product_feature(
        self,
        product_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, CreateProductFeatureErrorBody]:
        """Attaches a feature template to this product with a concrete value. Pass ``price_point_type:
        "ProductPricePoint"`` and ``price_point_id`` to create an override scoped to a single product price point
        instead of the whole product.

        Args:
            product_id: The Advanced Billing id of the product.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/features.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=create_product_feature_error_mapper,
            request_options=request_options,
        )

    def list_product_features(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemsListResponse, ListProductFeaturesErrorBody]:
        """Lists the feature catalog items attached to this product, including price-point-specific overrides.

        Args:
            product_id: The Advanced Billing id of the product.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/features.json"),
            path_params=[param[int]("product_id", product_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemsListResponse],
            error_mapper=list_product_features_error_mapper,
            request_options=request_options,
        )

    def read_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, ReadProductFeatureErrorBody]:
        """Returns a single feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/features/{id}.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=read_product_feature_error_mapper,
            request_options=request_options,
        )

    def remove_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveProductFeatureErrorBody]:
        """Removes a feature catalog item from this product.

        Args:
            product_id: The Advanced Billing id of the product.
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
            url_template=self._server.production("/products/{product_id}/features/{id}.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            query_params=[param[bool | None]("destroy_entitlements", destroy_entitlements)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=remove_product_feature_error_mapper,
            request_options=request_options,
        )

    def restore_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, RestoreProductFeatureErrorBody]:
        """Clears the archived state of a feature catalog item attached to this product. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/features/{id}/restore.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=restore_product_feature_error_mapper,
            request_options=request_options,
        )

    def update_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, UpdateProductFeatureErrorBody]:
        """Updates the value or periodicity of a feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/products/{product_id}/features/{id}.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureCatalogItemResponse],
            error_mapper=update_product_feature_error_mapper,
            request_options=request_options,
        )


class AsyncProductFeaturesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_product_feature(
        self,
        product_id: int,
        *,
        body: CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, CreateProductFeatureErrorBody]:
        """Attaches a feature template to this product with a concrete value. Pass ``price_point_type:
        "ProductPricePoint"`` and ``price_point_id`` to create an override scoped to a single product price point
        instead of the whole product.

        Args:
            product_id: The Advanced Billing id of the product.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/features.json"),
            path_params=[param[int]("product_id", product_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFeatureCatalogItemRequest | CreateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=create_product_feature_error_mapper,
            request_options=request_options,
        )

    async def list_product_features(
        self, product_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemsListResponse, ListProductFeaturesErrorBody]:
        """Lists the feature catalog items attached to this product, including price-point-specific overrides.

        Args:
            product_id: The Advanced Billing id of the product.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/features.json"),
            path_params=[param[int]("product_id", product_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemsListResponse],
            error_mapper=list_product_features_error_mapper,
            request_options=request_options,
        )

    async def read_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, ReadProductFeatureErrorBody]:
        """Returns a single feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/products/{product_id}/features/{id}.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=read_product_feature_error_mapper,
            request_options=request_options,
        )

    async def remove_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        destroy_entitlements: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RemoveProductFeatureErrorBody]:
        """Removes a feature catalog item from this product.

        Args:
            product_id: The Advanced Billing id of the product.
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
            url_template=self._server.production("/products/{product_id}/features/{id}.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            query_params=[param[bool | None]("destroy_entitlements", destroy_entitlements)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=remove_product_feature_error_mapper,
            request_options=request_options,
        )

    async def restore_product_feature(
        self, product_id: int, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureCatalogItemResponse, RestoreProductFeatureErrorBody]:
        """Clears the archived state of a feature catalog item attached to this product. Returns ``422`` if the parent
        feature template is still archived. Restore the feature template first.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/products/{product_id}/features/{id}/restore.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=restore_product_feature_error_mapper,
            request_options=request_options,
        )

    async def update_product_feature(
        self,
        product_id: int,
        id_: int,
        *,
        body: UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureCatalogItemResponse, UpdateProductFeatureErrorBody]:
        """Updates the value or periodicity of a feature catalog item attached to this product.

        Args:
            product_id: The Advanced Billing id of the product.
            id_: The Advanced Billing id of the feature catalog item.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/products/{product_id}/features/{id}.json"),
            path_params=[param[int]("product_id", product_id), param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFeatureCatalogItemRequest | UpdateFeatureCatalogItemRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureCatalogItemResponse],
            error_mapper=update_product_feature_error_mapper,
            request_options=request_options,
        )
