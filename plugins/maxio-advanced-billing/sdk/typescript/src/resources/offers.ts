import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { createOfferRequestSchema, type CreateOfferRequest } from "../models/create-offer-request.js";
import {
  errorArrayMapResponse1Schema,
  type ErrorArrayMapResponse1,
} from "../models/error-array-map-response1.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { listOffersResponseSchema, type ListOffersResponse } from "../models/list-offers-response.js";
import { offerResponseSchema, type OfferResponse } from "../models/offer-response.js";
import type { Servers } from "../servers.js";

/**
 * The Offer object bundles a specific Product, Price Point, and any associated discounts into a
 * single pre-configured signup option that customers can subscribe to directly.
 *
 * Offers are commonly used to power self-service signup pages without requiring each pricing
 * combination to be built manually. For more information, see [Understand
 * Offers](https://docs.maxio.com/billing/catalog/offers/understand-offers).
 */
export class Offers {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Offer
   *
   * @remarks
   * Archives an existing offer. Please provide an `offer_id` in order to archive the correct item.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveOffer(
    request: Offers.ArchiveOfferRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/offers/{offer_id}/archive.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "offer_id", value: request.offerId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Create Offer
   *
   * @remarks
   * Creates an offer within your site.
   *
   * Offers allow you to package complicated combinations of products, components and coupons into a
   * convenient package which can then be subscribed to just like products.
   *
   * Once an offer is defined it can be used as an alternative to the product when creating
   * subscriptions.
   *
   * For more information, see
   * [Offers](https://maxio.zendesk.com/hc/en-us/articles/24261295098637-Offers-Overview) in the
   * product documentation.
   *
   * ## Using a Product Price Point
   *
   * You can optionally pass in a `product_price_point_id` that corresponds with the `product_id`
   * and the offer will use that price point. If a `product_price_point_id` is not passed in, the
   * product's default price point will be used.
   *
   * @returns Created
   *
   * @throws {@link Offers.CreateOfferError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createOffer(
    request: Offers.CreateOfferRequestParams = {},
    options?: RequestOptions,
  ): ApiPromise<OfferResponse, Offers.CreateOfferError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/offers.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createOfferRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: offerResponseSchema },
        errorFactory: Offers.CreateOfferError,
      },
      options,
    );
  }

  /**
   * List Offers
   *
   * @remarks
   * Lists offers for a site.
   *
   * @returns OK
   *
   * @throws {@link Offers.ListOffersError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listOffers(
    request: Offers.ListOffersRequest = {},
    options?: RequestOptions,
  ): ApiPromise<ListOffersResponse, Offers.ListOffersError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/offers.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "include_archived", value: request.includeArchived, schema: s.optional(s.boolean()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listOffersResponseSchema },
        errorFactory: Offers.ListOffersError,
      },
      options,
    );
  }

  /**
   * Read Offer
   *
   * @remarks
   * Returns a specific offer's attributes. This is different from listing all offers for a site, as
   * it requires an `offer_id`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readOffer(request: Offers.ReadOfferRequest, options?: RequestOptions): ApiPromise<OfferResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/offers/{offer_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "offer_id", value: request.offerId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: offerResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Unarchive Offer
   *
   * @remarks
   * Unarchives a previously archived offer. Please provide an `offer_id` in order to unarchive the
   * correct item.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  unarchiveOffer(
    request: Offers.UnarchiveOfferRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/offers/{offer_id}/unarchive.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "offer_id", value: request.offerId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace Offers {
  export type ArchiveOfferRequest = {
    /** The Chargify id of the offer */
    offerId: number;
  };

  export type CreateOfferRequestParams = {
    body?: CreateOfferRequest;
  };

  export class CreateOfferError extends ApiError {
    declare readonly payload: Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateOfferError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type ListOffersRequest = {
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
    /** Include archived products. Use in query: `include_archived=true`. */
    includeArchived?: boolean;
  };

  export class ListOffersError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<ListOffersError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadOfferRequest = {
    /** The Chargify id of the offer */
    offerId: number;
  };

  export type UnarchiveOfferRequest = {
    /** The Chargify id of the offer */
    offerId: number;
  };
}
