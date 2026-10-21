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

export class ComponentFeatures {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Component Feature Catalog Item
   *
   * @remarks
   * Attaches a feature template to this component with a concrete value. Pass `price_point_type:
   * "PricePoint"` and `price_point_id` to create an override scoped to a single component price
   * point instead of the whole component.
   *
   * @returns Created
   *
   * @throws {@link ComponentFeatures.CreateComponentFeatureError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createComponentFeature(
    request: ComponentFeatures.CreateComponentFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.CreateComponentFeatureError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/components/{component_id}/features.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "component_id", value: request.componentId, schema: s.int() }],
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
        errorFactory: ComponentFeatures.CreateComponentFeatureError,
      },
      options,
    );
  }

  /**
   * List Component Feature Catalog Items
   *
   * @remarks
   * Lists the feature catalog items attached to this component, including price-point-specific
   * overrides.
   *
   * @returns OK
   *
   * @throws {@link ComponentFeatures.ListComponentFeaturesError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listComponentFeatures(
    request: ComponentFeatures.ListComponentFeaturesRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemsListResponse, ComponentFeatures.ListComponentFeaturesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/components/{component_id}/features.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "component_id", value: request.componentId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureCatalogItemsListResponseSchema },
        errorFactory: ComponentFeatures.ListComponentFeaturesError,
      },
      options,
    );
  }

  /**
   * Read Component Feature Catalog Item
   *
   * @remarks
   * Returns a single feature catalog item attached to this component.
   *
   * @returns OK
   *
   * @throws {@link ComponentFeatures.ReadComponentFeatureError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readComponentFeature(
    request: ComponentFeatures.ReadComponentFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.ReadComponentFeatureError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/components/{component_id}/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureCatalogItemResponseSchema },
        errorFactory: ComponentFeatures.ReadComponentFeatureError,
      },
      options,
    );
  }

  /**
   * Remove Component Feature Catalog Item
   *
   * @remarks
   * Removes a feature catalog item from this component.
   *
   * @returns No Content
   *
   * @throws {@link ComponentFeatures.RemoveComponentFeatureError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  removeComponentFeature(
    request: ComponentFeatures.RemoveComponentFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ComponentFeatures.RemoveComponentFeatureError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/components/{component_id}/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.int() },
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
        errorFactory: ComponentFeatures.RemoveComponentFeatureError,
      },
      options,
    );
  }

  /**
   * Restore Component Feature Catalog Item
   *
   * @remarks
   * Clears the archived state of a feature catalog item attached to this component. Returns `422`
   * if the parent feature template is still archived. Restore the feature template first.
   *
   * @returns OK
   *
   * @throws {@link ComponentFeatures.RestoreComponentFeatureError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  restoreComponentFeature(
    request: ComponentFeatures.RestoreComponentFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.RestoreComponentFeatureError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/components/{component_id}/features/{id}/restore.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureCatalogItemResponseSchema },
        errorFactory: ComponentFeatures.RestoreComponentFeatureError,
      },
      options,
    );
  }

  /**
   * Update Component Feature Catalog Item
   *
   * @remarks
   * Updates the value or periodicity of a feature catalog item attached to this component.
   *
   * @returns OK
   *
   * @throws {@link ComponentFeatures.UpdateComponentFeatureError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateComponentFeature(
    request: ComponentFeatures.UpdateComponentFeatureRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureCatalogItemResponse, ComponentFeatures.UpdateComponentFeatureError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/components/{component_id}/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.int() },
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
        errorFactory: ComponentFeatures.UpdateComponentFeatureError,
      },
      options,
    );
  }
}

export namespace ComponentFeatures {
  export type CreateComponentFeatureRequest = {
    /** The Advanced Billing id of the component. */
    componentId: number;
    body?: CreateFeatureCatalogItemRequest;
  };

  export class CreateComponentFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateComponentFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListComponentFeaturesRequest = {
    /** The Advanced Billing id of the component. */
    componentId: number;
  };

  export class ListComponentFeaturesError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"errorListResponse1", ErrorListResponse1> | Declared<"error404", undefined>
    >;

    static readonly errors: ErrorDecoders<ListComponentFeaturesError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ReadComponentFeatureRequest = {
    /** The Advanced Billing id of the component. */
    componentId: number;
    /** The Advanced Billing id of the feature catalog item. */
    id: number;
  };

  export class ReadComponentFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"errorListResponse1", ErrorListResponse1> | Declared<"error404", undefined>
    >;

    static readonly errors: ErrorDecoders<ReadComponentFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type RemoveComponentFeatureRequest = {
    /** The Advanced Billing id of the component. */
    componentId: number;
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

  export class RemoveComponentFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"errorListResponse1", ErrorListResponse1> | Declared<"error404", undefined>
    >;

    static readonly errors: ErrorDecoders<RemoveComponentFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type RestoreComponentFeatureRequest = {
    /** The Advanced Billing id of the component. */
    componentId: number;
    /** The Advanced Billing id of the feature catalog item. */
    id: number;
  };

  export class RestoreComponentFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<RestoreComponentFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateComponentFeatureRequest = {
    /** The Advanced Billing id of the component. */
    componentId: number;
    /** The Advanced Billing id of the feature catalog item. */
    id: number;
    body?: UpdateFeatureCatalogItemRequest;
  };

  export class UpdateComponentFeatureError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<UpdateComponentFeatureError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
