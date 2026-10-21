import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  cloneComponentPricePointRequestSchema,
  type CloneComponentPricePointRequest,
} from "../models/clone-component-price-point-request.js";
import {
  componentCurrencyPricesResponseSchema,
  type ComponentCurrencyPricesResponse,
} from "../models/component-currency-prices-response.js";
import {
  componentPricePointCurrencyOverageResponseSchema,
  type ComponentPricePointCurrencyOverageResponse,
} from "../models/component-price-point-currency-overage-response.js";
import {
  componentPricePointResponseSchema,
  type ComponentPricePointResponse,
} from "../models/component-price-point-response.js";
import {
  componentPricePointsResponseSchema,
  type ComponentPricePointsResponse,
} from "../models/component-price-points-response.js";
import { componentResponseSchema, type ComponentResponse } from "../models/component-response.js";
import {
  createComponentPricePointRequestSchema,
  type CreateComponentPricePointRequest,
} from "../models/create-component-price-point-request.js";
import {
  createComponentPricePointsRequestSchema,
  type CreateComponentPricePointsRequest,
} from "../models/create-component-price-points-request.js";
import {
  createCurrencyPricesRequestSchema,
  type CreateCurrencyPricesRequest,
} from "../models/create-currency-prices-request.js";
import {
  errorArrayMapResponse1Schema,
  type ErrorArrayMapResponse1,
} from "../models/error-array-map-response1.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  listComponentsPricePointsIncludeSchema,
  type ListComponentsPricePointsInclude,
} from "../models/list-components-price-points-include.js";
import {
  listComponentsPricePointsResponseSchema,
  type ListComponentsPricePointsResponse,
} from "../models/list-components-price-points-response.js";
import {
  listPricePointsFilterSchema,
  type ListPricePointsFilter,
} from "../models/list-price-points-filter.js";
import { pricePointTypeSchema, type PricePointType } from "../models/price-point-type.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import { componentIdModelSchema, type ComponentIdModel } from "../models/unions/component-id-model.js";
import { pricePointIdModelSchema, type PricePointIdModel } from "../models/unions/price-point-id-model.js";
import {
  updateComponentPricePointRequestSchema,
  type UpdateComponentPricePointRequest,
} from "../models/update-component-price-point-request.js";
import {
  updateCurrencyPricesRequestSchema,
  type UpdateCurrencyPricesRequest,
} from "../models/update-currency-prices-request.js";
import type { Servers } from "../servers.js";

export class ComponentPricePoints {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Component Price Point
   *
   * @remarks
   * Archives a component price point. Subscriptions using a price point that has been archived will
   * continue using it until they're moved to another price point.
   *
   * @returns OK
   *
   * @throws {@link ComponentPricePoints.ArchiveComponentPricePointError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveComponentPricePoint(
    request: ComponentPricePoints.ArchiveComponentPricePointRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentPricePointResponse, ComponentPricePoints.ArchiveComponentPricePointError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: componentIdModelSchema },
          { name: "price_point_id", value: request.pricePointId, schema: pricePointIdModelSchema },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentPricePointResponseSchema },
        errorFactory: ComponentPricePoints.ArchiveComponentPricePointError,
      },
      options,
    );
  }

  /**
   * Bulk Create Component Price Points
   *
   * @remarks
   * Creates multiple component price points in one request.
   *
   * @returns OK
   *
   * @throws {@link ComponentPricePoints.BulkCreateComponentPricePointsError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  bulkCreateComponentPricePoints(
    request: ComponentPricePoints.BulkCreateComponentPricePointsRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentPricePointsResponse, ComponentPricePoints.BulkCreateComponentPricePointsError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/components/{component_id}/price_points/bulk.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "component_id", value: request.componentId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createComponentPricePointsRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentPricePointsResponseSchema },
        errorFactory: ComponentPricePoints.BulkCreateComponentPricePointsError,
      },
      options,
    );
  }

  /**
   * Clone Component Price Point
   *
   * @remarks
   * Clones a component price point. Custom price points (tied to a specific subscription) cannot be
   * cloned. The following attributes are copied from the source price point:
   * - Pricing scheme
   * - All price tiers (with starting/ending quantities and unit prices)
   * - Tax included setting
   * - Currency prices (if definitive pricing is set)
   * - Overage pricing (for prepaid usage components)
   * - Interval settings (if multi-frequency is enabled)
   * - Event-based billing segments (if applicable)
   *
   * @returns Created
   *
   * @throws {@link ComponentPricePoints.CloneComponentPricePointError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  cloneComponentPricePoint(
    request: ComponentPricePoints.CloneComponentPricePointRequestParams,
    options?: RequestOptions,
  ): ApiPromise<
    ComponentPricePointCurrencyOverageResponse,
    ComponentPricePoints.CloneComponentPricePointError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/clone.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: componentIdModelSchema },
          { name: "price_point_id", value: request.pricePointId, schema: pricePointIdModelSchema },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => cloneComponentPricePointRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentPricePointCurrencyOverageResponseSchema },
        errorFactory: ComponentPricePoints.CloneComponentPricePointError,
      },
      options,
    );
  }

  /**
   * Create Component Price Point
   *
   * @remarks
   * Creates a price point for an existing component.
   *
   * @returns OK
   *
   * @throws {@link ComponentPricePoints.CreateComponentPricePointError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createComponentPricePoint(
    request: ComponentPricePoints.CreateComponentPricePointRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ComponentPricePointResponse, ComponentPricePoints.CreateComponentPricePointError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/components/{component_id}/price_points.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "component_id", value: request.componentId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createComponentPricePointRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentPricePointResponseSchema },
        errorFactory: ComponentPricePoints.CreateComponentPricePointError,
      },
      options,
    );
  }

  /**
   * Create Currency Prices
   *
   * @remarks
   * Creates currency prices for a given currency defined at the site level.
   *
   * When creating currency prices, they need to mirror the structure of your primary pricing. For
   * each price level defined on the component price point, there should be a matching price level
   * created in the given currency.
   *
   * Note: Currency Prices are not able to be created for custom price points.
   *
   * @returns OK
   *
   * @throws {@link ComponentPricePoints.CreateCurrencyPricesError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createCurrencyPrices(
    request: ComponentPricePoints.CreateCurrencyPricesRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ComponentCurrencyPricesResponse, ComponentPricePoints.CreateCurrencyPricesError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/price_points/{price_point_id}/currency_prices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "price_point_id", value: request.pricePointId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createCurrencyPricesRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentCurrencyPricesResponseSchema },
        errorFactory: ComponentPricePoints.CreateCurrencyPricesError,
      },
      options,
    );
  }

  /**
   * List All Components Price Points
   *
   * @remarks
   * Lists all component price points belonging to a site.
   *
   * @returns OK
   *
   * @throws {@link ComponentPricePoints.ListAllComponentPricePointsError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listAllComponentPricePoints(
    request: ComponentPricePoints.ListAllComponentPricePointsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListComponentsPricePointsResponse, ComponentPricePoints.ListAllComponentPricePointsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/components_price_points.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.lazy(() => listComponentsPricePointsIncludeSchema)),
          },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listPricePointsFilterSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listComponentsPricePointsResponseSchema },
        errorFactory: ComponentPricePoints.ListAllComponentPricePointsError,
      },
      options,
    );
  }

  /**
   * List Component Price Points
   *
   * @remarks
   * Lists the price points associated with a component.
   *
   * You may specify the component by using either the numeric id or the `handle:gold` syntax.
   *
   * If the price point is set to `use_site_exchange_rate: true`, it will return pricing based on
   * the current exchange rate. If the flag is set to false, it will return all of the defined
   * prices for each currency.
   *
   * @returns Created
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listComponentPricePoints(
    request: ComponentPricePoints.ListComponentPricePointsRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentPricePointsResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/components/{component_id}/price_points.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "component_id", value: request.componentId, schema: s.int() }],
        query: [
          { name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "filter[type]",
            value: request.filterType,
            schema: s.optional(s.array(s.lazy(() => pricePointTypeSchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentPricePointsResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Promote Price Point to Default
   *
   * @remarks
   * Sets a new default price point for the component. This new default will apply to all new
   * subscriptions going forward - existing subscriptions will remain on their current price point.
   *
   * See [Price Points
   * Documentation](https://maxio.zendesk.com/hc/en-us/articles/24261191737101-Price-Points-Components)
   * for more information on price points and moving subscriptions between price points.
   *
   * Note: Custom price points are not able to be set as the default for a component.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  promoteComponentPricePointToDefault(
    request: ComponentPricePoints.PromoteComponentPricePointToDefaultRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/default.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.int() },
          { name: "price_point_id", value: request.pricePointId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Component Price Point
   *
   * @remarks
   * Returns details for a specific component price point. You can achieve this by using either the
   * component price point ID or handle.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readComponentPricePoint(
    request: ComponentPricePoints.ReadComponentPricePointRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentPricePointCurrencyOverageResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: componentIdModelSchema },
          { name: "price_point_id", value: request.pricePointId, schema: pricePointIdModelSchema },
        ],
        query: [{ name: "currency_prices", value: request.currencyPrices, schema: s.optional(s.boolean()) }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentPricePointCurrencyOverageResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Unarchive Component Price Point
   *
   * @remarks
   * Unarchives a component price point.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  unarchiveComponentPricePoint(
    request: ComponentPricePoints.UnarchiveComponentPricePointRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentPricePointResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/unarchive.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.int() },
          { name: "price_point_id", value: request.pricePointId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentPricePointResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Component Price Point
   *
   * @remarks
   * Updates a component price point and its associated prices.
   *
   * Passing in a price bracket without an `id` will attempt to create a new price.
   *
   * Including an `id` will update the corresponding price, and including the `_destroy` flag set to
   * true along with the `id` will remove that price.
   *
   * Note: Custom price points cannot be updated directly. They must be edited through the
   * Subscription.
   *
   * @returns OK
   *
   * @throws {@link ComponentPricePoints.UpdateComponentPricePointError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateComponentPricePoint(
    request: ComponentPricePoints.UpdateComponentPricePointRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ComponentPricePointResponse, ComponentPricePoints.UpdateComponentPricePointError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: componentIdModelSchema },
          { name: "price_point_id", value: request.pricePointId, schema: pricePointIdModelSchema },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateComponentPricePointRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentPricePointResponseSchema },
        errorFactory: ComponentPricePoints.UpdateComponentPricePointError,
      },
      options,
    );
  }

  /**
   * Update Currency Prices
   *
   * @remarks
   * Updates currency prices for a given currency defined at the site level.
   *
   * Note: Currency Prices are not able to be updated for custom price points.
   *
   * @returns OK
   *
   * @throws {@link ComponentPricePoints.UpdateCurrencyPricesError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateCurrencyPrices(
    request: ComponentPricePoints.UpdateCurrencyPricesRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ComponentCurrencyPricesResponse, ComponentPricePoints.UpdateCurrencyPricesError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/price_points/{price_point_id}/currency_prices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "price_point_id", value: request.pricePointId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateCurrencyPricesRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentCurrencyPricesResponseSchema },
        errorFactory: ComponentPricePoints.UpdateCurrencyPricesError,
      },
      options,
    );
  }
}

export namespace ComponentPricePoints {
  export type ArchiveComponentPricePointRequest = {
    /**
     * The id or handle of the component. When using the handle, it must be prefixed with `handle:`.
     * Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle.
     */
    componentId: ComponentIdModel;
    /**
     * The id or handle of the price point. When using the handle, it must be prefixed with
     * `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a
     * string handle.
     */
    pricePointId: PricePointIdModel;
  };

  export class ArchiveComponentPricePointError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ArchiveComponentPricePointError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type BulkCreateComponentPricePointsRequest = {
    /** The Advanced Billing id of the component for which you want to fetch price points. */
    componentId: string;
    body?: CreateComponentPricePointsRequest;
  };

  export class BulkCreateComponentPricePointsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<BulkCreateComponentPricePointsError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CloneComponentPricePointRequestParams = {
    /**
     * The id or handle of the component. When using the handle, it must be prefixed with `handle:`.
     * Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle.
     */
    componentId: ComponentIdModel;
    /**
     * The id or handle of the price point. When using the handle, it must be prefixed with
     * `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a
     * string handle.
     */
    pricePointId: PricePointIdModel;
    body?: CloneComponentPricePointRequest;
  };

  export class CloneComponentPricePointError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CloneComponentPricePointError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateComponentPricePointRequestParams = {
    /** The Advanced Billing id of the component */
    componentId: number;
    body?: CreateComponentPricePointRequest;
  };

  export class CreateComponentPricePointError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>>;

    static readonly errors: ErrorDecoders<CreateComponentPricePointError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type CreateCurrencyPricesRequestParams = {
    /** The Advanced Billing id of the price point */
    pricePointId: number;
    body?: CreateCurrencyPricesRequest;
  };

  export class CreateCurrencyPricesError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>>;

    static readonly errors: ErrorDecoders<CreateCurrencyPricesError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type ListAllComponentPricePointsRequest = {
    /**
     * Allows including additional data in the response. Use in query: `include=currency_prices`.
     */
    include?: ListComponentsPricePointsInclude;
    /**
     * Result records are organized in pages. By default, the first page of results is displayed.
     * The page parameter specifies a page number of results to fetch. You can start navigating
     * through the pages to consume the results. You do this by passing in a page parameter.
     * Retrieve the next page by adding ?page=2 to the query string. If there are no results to
     * return, then an empty result set will be returned. Use in query `page=1`.
     *
     * @default 1
     */
    page?: number;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 20. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in
     * query `per_page=200`.
     *
     * @default 20
     */
    perPage?: number;
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
    /** Filter to use for List PricePoints operations */
    filter?: ListPricePointsFilter;
  };

  export class ListAllComponentPricePointsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ListAllComponentPricePointsError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListComponentPricePointsRequest = {
    /** The Advanced Billing id of the component */
    componentId: number;
    /** Include an array of currency price data. */
    currencyPrices?: boolean;
    /**
     * Result records are organized in pages. By default, the first page of results is displayed.
     * The page parameter specifies a page number of results to fetch. You can start navigating
     * through the pages to consume the results. You do this by passing in a page parameter.
     * Retrieve the next page by adding ?page=2 to the query string. If there are no results to
     * return, then an empty result set will be returned. Use in query `page=1`.
     *
     * @default 1
     */
    page?: number;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 20. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in
     * query `per_page=200`.
     *
     * @default 20
     */
    perPage?: number;
    /** Use in query: `filter[type]=catalog,default`. */
    filterType?: PricePointType[];
  };

  export type PromoteComponentPricePointToDefaultRequest = {
    /** The Advanced Billing id of the component to which the price point belongs */
    componentId: number;
    /** The Advanced Billing id of the price point */
    pricePointId: number;
  };

  export type ReadComponentPricePointRequest = {
    /**
     * The id or handle of the component. When using the handle, it must be prefixed with `handle:`.
     * Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle.
     */
    componentId: ComponentIdModel;
    /**
     * The id or handle of the price point. When using the handle, it must be prefixed with
     * `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a
     * string handle.
     */
    pricePointId: PricePointIdModel;
    /** Include an array of currency price data. */
    currencyPrices?: boolean;
  };

  export type UnarchiveComponentPricePointRequest = {
    /** The Advanced Billing id of the component to which the price point belongs */
    componentId: number;
    /** The Advanced Billing id of the price point */
    pricePointId: number;
  };

  export type UpdateComponentPricePointRequestParams = {
    /**
     * The id or handle of the component. When using the handle, it must be prefixed with `handle:`.
     * Example: `123` for an integer ID, or `handle:example-product-handle` for a string handle.
     */
    componentId: ComponentIdModel;
    /**
     * The id or handle of the price point. When using the handle, it must be prefixed with
     * `handle:`. Example: `123` for an integer ID, or `handle:example-price_point-handle` for a
     * string handle.
     */
    pricePointId: PricePointIdModel;
    body?: UpdateComponentPricePointRequest;
  };

  export class UpdateComponentPricePointError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>>;

    static readonly errors: ErrorDecoders<UpdateComponentPricePointError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type UpdateCurrencyPricesRequestParams = {
    /** The Advanced Billing id of the price point */
    pricePointId: number;
    body?: UpdateCurrencyPricesRequest;
  };

  export class UpdateCurrencyPricesError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>>;

    static readonly errors: ErrorDecoders<UpdateCurrencyPricesError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }
}
