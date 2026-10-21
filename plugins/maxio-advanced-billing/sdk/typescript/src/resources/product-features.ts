import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createFeatureCatalogItemRequestSchema,
  type CreateFeatureCatalogItemRequest,
} from "../models/create-feature-catalog-item-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  featureCatalogItemResponseSchema,
  type FeatureCatalogItemResponse,
} from "../models/feature-catalog-item-response.js";
import {
  featureCatalogItemsListResponseSchema,
  type FeatureCatalogItemsListResponse,
} from "../models/feature-catalog-items-list-response.js";
import {
  updateFeatureCatalogItemRequestSchema,
  type UpdateFeatureCatalogItemRequest,
} from "../models/update-feature-catalog-item-request.js";
import type { Servers } from "../servers.js";

export class ProductFeatures {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Product Feature Catalog Item
   *
   * @remarks
   * Attaches a feature template to this product with a concrete value. Pass `price_point_type:
   * "ProductPricePoint"` and `price_point_id` to create an override scoped to a single product
   * price point instead of the whole product.
   *
   * @returns Created
   *
   * @throws {@link ProductFeatures.CreateProductFeatureError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createProductFeature(
    request: ProductFeatures.CreateProductFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.CreateProductFeatureError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/products/{product_id}/features.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createFeatureCatalogItemRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: featureCatalogItemResponseSchema },
        errorFactory: ProductFeatures.CreateProductFeatureError,
      },
      options,
    );
  }

  /**
   * List Product Feature Catalog Items
   *
   * @remarks
   * Lists the feature catalog items attached to this product, including price-point-specific
   * overrides.
   *
   * @returns OK
   *
   * @throws {@link ProductFeatures.ListProductFeaturesError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listProductFeatures(
    request: ProductFeatures.ListProductFeaturesRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemsListResponse, ProductFeatures.ListProductFeaturesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products/{product_id}/features.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_id", value: request.productId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureCatalogItemsListResponseSchema },
        errorFactory: ProductFeatures.ListProductFeaturesError,
      },
      options,
    );
  }

  /**
   * Read Product Feature Catalog Item
   *
   * @remarks
   * Returns a single feature catalog item attached to this product.
   *
   * @returns OK
   *
   * @throws {@link ProductFeatures.ReadProductFeatureError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readProductFeature(
    request: ProductFeatures.ReadProductFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.ReadProductFeatureError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/products/{product_id}/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureCatalogItemResponseSchema },
        errorFactory: ProductFeatures.ReadProductFeatureError,
      },
      options,
    );
  }

  /**
   * Remove Product Feature Catalog Item
   *
   * @remarks
   * Removes a feature catalog item from this product.
   *
   * @returns No Content
   *
   * @throws {@link ProductFeatures.RemoveProductFeatureError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  removeProductFeature(
    request: ProductFeatures.RemoveProductFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ProductFeatures.RemoveProductFeatureError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/products/{product_id}/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [
          {
            name: "destroy_entitlements",
            value: request.destroyEntitlements,
            schema: s.defaulted(s.boolean(), false),
          },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: ProductFeatures.RemoveProductFeatureError,
      },
      options,
    );
  }

  /**
   * Restore Product Feature Catalog Item
   *
   * @remarks
   * Clears the archived state of a feature catalog item attached to this product. Returns `422` if
   * the parent feature template is still archived. Restore the feature template first.
   *
   * @returns OK
   *
   * @throws {@link ProductFeatures.RestoreProductFeatureError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  restoreProductFeature(
    request: ProductFeatures.RestoreProductFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.RestoreProductFeatureError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/products/{product_id}/features/{id}/restore.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureCatalogItemResponseSchema },
        errorFactory: ProductFeatures.RestoreProductFeatureError,
      },
      options,
    );
  }

  /**
   * Update Product Feature Catalog Item
   *
   * @remarks
   * Updates the value or periodicity of a feature catalog item attached to this product.
   *
   * @returns OK
   *
   * @throws {@link ProductFeatures.UpdateProductFeatureError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateProductFeature(
    request: ProductFeatures.UpdateProductFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ProductFeatures.UpdateProductFeatureError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/products/{product_id}/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_id", value: request.productId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateFeatureCatalogItemRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: featureCatalogItemResponseSchema },
        errorFactory: ProductFeatures.UpdateProductFeatureError,
      },
      options,
    );
  }
}

export namespace ProductFeatures {
  export type CreateProductFeatureRequest = {
    /** The Advanced Billing id of the product. */
    productId: number;
    body?: CreateFeatureCatalogItemRequest;
  };

  export class CreateProductFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateProductFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListProductFeaturesRequest = {
    /** The Advanced Billing id of the product. */
    productId: number;
  };

  export class ListProductFeaturesError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"errorListResponse1", ErrorListResponse1> | Declared<"error404", undefined>
    >;

    static readonly errors: ErrorDecoders<ListProductFeaturesError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ReadProductFeatureRequest = {
    /** The Advanced Billing id of the product. */
    productId: number;
    /** The Advanced Billing id of the feature catalog item. */
    id: number;
  };

  export class ReadProductFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"errorListResponse1", ErrorListResponse1> | Declared<"error404", undefined>
    >;

    static readonly errors: ErrorDecoders<ReadProductFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type RemoveProductFeatureRequest = {
    /** The Advanced Billing id of the product. */
    productId: number;
    /** The Advanced Billing id of the feature catalog item. */
    id: number;
    /**
     * When `true`, permanently deletes this feature catalog item and every entitlement it created,
     * revoking subscriber access immediately. When `false` (default), the feature catalog item is
     * archived and existing entitlements are preserved.
     *
     * @default false
     */
    destroyEntitlements?: boolean;
  };

  export class RemoveProductFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"errorListResponse1", ErrorListResponse1> | Declared<"error404", undefined>
    >;

    static readonly errors: ErrorDecoders<RemoveProductFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type RestoreProductFeatureRequest = {
    /** The Advanced Billing id of the product. */
    productId: number;
    /** The Advanced Billing id of the feature catalog item. */
    id: number;
  };

  export class RestoreProductFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<RestoreProductFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateProductFeatureRequest = {
    /** The Advanced Billing id of the product. */
    productId: number;
    /** The Advanced Billing id of the feature catalog item. */
    id: number;
    body?: UpdateFeatureCatalogItemRequest;
  };

  export class UpdateProductFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<UpdateProductFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
