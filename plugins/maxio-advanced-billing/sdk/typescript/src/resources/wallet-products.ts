import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createWalletProductRequestSchema,
  type CreateWalletProductRequest,
} from "../models/create-wallet-product-request.js";
import { SortBy1, sortBy1Schema } from "../models/sort-by1.js";
import { SortDirection, sortDirectionSchema } from "../models/sort-direction.js";
import { status1Schema, type Status1 } from "../models/status1.js";
import {
  updateWalletProductRequestSchema,
  type UpdateWalletProductRequest,
} from "../models/update-wallet-product-request.js";
import { walletErrorResponse1Schema, type WalletErrorResponse1 } from "../models/wallet-error-response1.js";
import {
  walletProductResponseSchema,
  type WalletProductResponse,
} from "../models/wallet-product-response.js";
import {
  walletProductUsageResponseSchema,
  type WalletProductUsageResponse,
} from "../models/wallet-product-usage-response.js";
import {
  walletProductsListResponseSchema,
  type WalletProductsListResponse,
} from "../models/wallet-products-list-response.js";
import type { Servers } from "../servers.js";

/**
 * The Wallet Product object is a billing product created specifically to denominate wallets and to
 * price wallet purchases. A Wallet Product does not belong to a product family, and the Wallet
 * Product behind a wallet cannot be changed after the wallet is created. For more information, see
 * [Create and Manage Wallet
 * Products](https://docs.maxio.com/billing/catalog/wallets/create-and-manage-wallet-products).
 */
export class WalletProducts {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Wallet Product
   *
   * @remarks
   * Archives the Wallet Product. Refuses when an active Feature's `wallet_behavior` still points at
   * it, or when it's used in a scheduled renewal. This protects Feature-provisioned wallets, but
   * not a wallet created manually against this product: a manual wallet can be left denominated by
   * an archived Wallet Product, and [Create Wallet
   * Purchase]($e/Wallet%20Purchases/createWalletPurchase) doesn't check whether the billing product
   * is archived before pricing and charging a purchase against it.
   *
   * @returns Wallet Product archived.
   *
   * @throws {@link WalletProducts.ArchiveWalletProductError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveWalletProduct(
    request: WalletProducts.ArchiveWalletProductRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletProductResponse, WalletProducts.ArchiveWalletProductError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallet_products/{id}/archive.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletProductResponseSchema },
        errorFactory: WalletProducts.ArchiveWalletProductError,
      },
      options,
    );
  }

  /**
   * Create Wallet Product
   *
   * @remarks
   * Creates a Wallet Product: a billing product with no product family, meant to denominate wallets
   * and to be purchased through [Create Wallet
   * Purchase]($e/Wallet%20Purchases/createWalletPurchase). It's a Component under the hood, so it
   * returns the full Component field set, and can optionally be priced with one or more price
   * points in the same call.
   *
   * @returns Wallet Product created.
   *
   * @throws {@link WalletProducts.CreateWalletProductError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createWalletProduct(
    request: WalletProducts.CreateWalletProductRequestParams,
    options?: RequestOptions,
  ): ApiPromise<WalletProductResponse, WalletProducts.CreateWalletProductError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallet_products.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createWalletProductRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletProductResponseSchema },
        errorFactory: WalletProducts.CreateWalletProductError,
      },
      options,
    );
  }

  /**
   * List Wallet Products
   *
   * @remarks
   * Lists the Wallet Products on your site.
   *
   * @returns OK. Unlike most list endpoints, this one is unpaginated (returns the full matching set
   * in one response) unless `page` or `per_page` is sent; sending either turns on pagination,
   * defaulting to 20 per page with a maximum of 200.
   *
   * @throws {@link WalletProducts.ListWalletProductsError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listWalletProducts(
    request: WalletProducts.ListWalletProductsRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletProductsListResponse, WalletProducts.ListWalletProductsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/wallet_products.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "include_archived", value: request.includeArchived, schema: s.optional(s.boolean()) },
          { name: "status", value: request.status, schema: s.optional(s.lazy(() => status1Schema)) },
          { name: "q", value: request.q, schema: s.optional(s.string()) },
          { name: "sort_by", value: request.sortBy, schema: s.defaulted(sortBy1Schema, SortBy1.Name) },
          {
            name: "sort_direction",
            value: request.sortDirection,
            schema: s.defaulted(sortDirectionSchema, SortDirection.Asc),
          },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletProductsListResponseSchema },
        errorFactory: WalletProducts.ListWalletProductsError,
      },
      options,
    );
  }

  /**
   * Read Wallet Product
   *
   * @remarks
   * Returns the Wallet Product.
   *
   * @returns OK
   *
   * @throws {@link WalletProducts.ReadWalletProductError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readWalletProduct(
    request: WalletProducts.ReadWalletProductRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletProductResponse, WalletProducts.ReadWalletProductError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/wallet_products/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletProductResponseSchema },
        errorFactory: WalletProducts.ReadWalletProductError,
      },
      options,
    );
  }

  /**
   * Read Wallet Product Usage
   *
   * @remarks
   * Returns everything drawing on this Wallet Product: the wallet templates billing through it,
   * split into ones using its default price point and ones overriding it, plus a sample of up to 50
   * of the active wallets actually created from them. A wallet template can appear more than once
   * in `wallet_templates`/`price_point_overrides`, once per Feature and owning plan/component
   * sharing it, so these arrays aren't one row per template.
   *
   * @returns OK
   *
   * @throws {@link WalletProducts.ReadWalletProductUsageError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readWalletProductUsage(
    request: WalletProducts.ReadWalletProductUsageRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletProductUsageResponse, WalletProducts.ReadWalletProductUsageError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/wallet_products/{id}/usage.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletProductUsageResponseSchema },
        errorFactory: WalletProducts.ReadWalletProductUsageError,
      },
      options,
    );
  }

  /**
   * Unarchive Wallet Product
   *
   * @remarks
   * Restores an archived Wallet Product.
   *
   * @returns Wallet Product unarchived.
   *
   * @throws {@link WalletProducts.UnarchiveWalletProductError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  unarchiveWalletProduct(
    request: WalletProducts.UnarchiveWalletProductRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletProductResponse, WalletProducts.UnarchiveWalletProductError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallet_products/{id}/unarchive.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletProductResponseSchema },
        errorFactory: WalletProducts.UnarchiveWalletProductError,
      },
      options,
    );
  }

  /**
   * Update Wallet Product
   *
   * @remarks
   * Updates the Wallet Product's catalog-facing fields. Omitted fields are left unchanged. Unlike
   * [Create Wallet Product]($e/Wallet%20Products/createWalletProduct), this does not accept
   * `unit_name`, `handle`, `price_point`, or `price_points`; see the request schema for which
   * fields are actually mutable.
   *
   * @returns Wallet Product updated.
   *
   * @throws {@link WalletProducts.UpdateWalletProductError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateWalletProduct(
    request: WalletProducts.UpdateWalletProductRequestParams,
    options?: RequestOptions,
  ): ApiPromise<WalletProductResponse, WalletProducts.UpdateWalletProductError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/wallet_products/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateWalletProductRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletProductResponseSchema },
        errorFactory: WalletProducts.UpdateWalletProductError,
      },
      options,
    );
  }
}

export namespace WalletProducts {
  export type ArchiveWalletProductRequest = {
    /**
     * The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for
     * example `handle:token-pack`). A bare handle returns `404`.
     */
    id: string;
  };

  export class ArchiveWalletProductError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ArchiveWalletProductError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 422,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }

  export type CreateWalletProductRequestParams = {
    body?: CreateWalletProductRequest;
  };

  export class CreateWalletProductError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<CreateWalletProductError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 422, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
    ];
  }

  export type ListWalletProductsRequest = {
    /**
     * Includes archived Wallet Products in the result. Defaults to `false`. Ignored when `status`
     * is also sent.
     */
    includeArchived?: boolean;
    /**
     * Restricts the result by status, and overrides `include_archived` when sent. An unrecognized
     * value falls back to `active` rather than returning `422`.
     */
    status?: Status1;
    /**
     * Restricts the result to Wallet Products whose name, handle, or unit name contains this
     * substring (case-insensitive).
     */
    q?: string;
    /**
     * The field to sort results by. An unrecognized value falls back to `name`.
     *
     * @default SortBy1.Name
     */
    sortBy?: SortBy1;
    /**
     * The sort direction. Anything other than `desc` is treated as `asc`.
     *
     * @default SortDirection.Asc
     */
    sortDirection?: SortDirection;
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
  };

  export class ListWalletProductsError extends ApiError {
    declare readonly payload: Declared<"error403", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<ListWalletProductsError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
    ];
  }

  export type ReadWalletProductRequest = {
    /**
     * The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for
     * example `handle:token-pack`). A bare handle returns `404`.
     */
    id: string;
  };

  export class ReadWalletProductError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ReadWalletProductError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
    ];
  }

  export type ReadWalletProductUsageRequest = {
    /**
     * The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for
     * example `handle:token-pack`). A bare handle returns `404`.
     */
    id: string;
  };

  export class ReadWalletProductUsageError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ReadWalletProductUsageError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
    ];
  }

  export type UnarchiveWalletProductRequest = {
    /**
     * The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for
     * example `handle:token-pack`). A bare handle returns `404`.
     */
    id: string;
  };

  export class UnarchiveWalletProductError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UnarchiveWalletProductError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 422,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }

  export type UpdateWalletProductRequestParams = {
    /**
     * The Advanced Billing id of the Wallet Product, or its handle prefixed with `handle:` (for
     * example `handle:token-pack`). A bare handle returns `404`.
     */
    id: string;
    body?: UpdateWalletProductRequest;
  };

  export class UpdateWalletProductError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateWalletProductError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 422,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }
}
