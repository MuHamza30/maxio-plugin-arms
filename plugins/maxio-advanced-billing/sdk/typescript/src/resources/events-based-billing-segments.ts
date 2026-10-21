import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { bulkCreateSegmentsSchema, type BulkCreateSegments } from "../models/bulk-create-segments.js";
import { bulkUpdateSegmentsSchema, type BulkUpdateSegments } from "../models/bulk-update-segments.js";
import { createSegmentRequestSchema, type CreateSegmentRequest } from "../models/create-segment-request.js";
import {
  eventBasedBillingListSegmentsErrors1Schema,
  type EventBasedBillingListSegmentsErrors1,
} from "../models/event-based-billing-list-segments-errors1.js";
import {
  eventBasedBillingSegmentErrors1Schema,
  type EventBasedBillingSegmentErrors1,
} from "../models/event-based-billing-segment-errors1.js";
import {
  eventBasedBillingSegment1Schema,
  type EventBasedBillingSegment1,
} from "../models/event-based-billing-segment1.js";
import { listSegmentsFilterSchema, type ListSegmentsFilter } from "../models/list-segments-filter.js";
import { listSegmentsResponseSchema, type ListSegmentsResponse } from "../models/list-segments-response.js";
import { segmentResponseSchema, type SegmentResponse } from "../models/segment-response.js";
import { updateSegmentRequestSchema, type UpdateSegmentRequest } from "../models/update-segment-request.js";
import type { Servers } from "../servers.js";

export class EventsBasedBillingSegments {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Bulk Create Segments
   *
   * @remarks
   * Creates multiple segments in one request. The array of segments can contain up to `2000`
   * records.
   *
   * If any of the records contain an error the whole request would fail and none of the requested
   * segments get created. The error response contains a message for only the one segment that
   * failed validation, with the corresponding index in the array.
   *
   * You may specify component and/or price point by using either the numeric ID or the
   * `handle:gold` syntax.
   *
   * @returns Created
   *
   * @throws {@link EventsBasedBillingSegments.BulkCreateSegmentsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  bulkCreateSegments(
    request: EventsBasedBillingSegments.BulkCreateSegmentsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListSegmentsResponse, EventsBasedBillingSegments.BulkCreateSegmentsError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/segments/bulk.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.string() },
          { name: "price_point_id", value: request.pricePointId, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => bulkCreateSegmentsSchema)),
        },
      },
      {
        success: { kind: "json", schema: listSegmentsResponseSchema },
        errorFactory: EventsBasedBillingSegments.BulkCreateSegmentsError,
      },
      options,
    );
  }

  /**
   * Bulk Update Segments
   *
   * @remarks
   * Updates multiple segments in one request. The array of segments can contain up to `1000`
   * records.
   *
   * If any of the records contain an error the whole request would fail and none of the requested
   * segments get updated. The error response contains a message for only the one segment that
   * failed validation, with the corresponding index in the array.
   *
   * You may specify component and/or price point by using either the numeric ID or the
   * `handle:gold` syntax.
   *
   * @returns OK
   *
   * @throws {@link EventsBasedBillingSegments.BulkUpdateSegmentsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  bulkUpdateSegments(
    request: EventsBasedBillingSegments.BulkUpdateSegmentsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListSegmentsResponse, EventsBasedBillingSegments.BulkUpdateSegmentsError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/segments/bulk.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.string() },
          { name: "price_point_id", value: request.pricePointId, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => bulkUpdateSegmentsSchema)),
        },
      },
      {
        success: { kind: "json", schema: listSegmentsResponseSchema },
        errorFactory: EventsBasedBillingSegments.BulkUpdateSegmentsError,
      },
      options,
    );
  }

  /**
   * Create Single Segment
   *
   * @remarks
   * Creates a new segment for a component with a segmented metric. It allows you to specify
   * properties to bill upon and prices for each Segment. You can only pass as many
   * "property_values" as the related Metric has segmenting properties defined.
   *
   * You may specify component and/or price point by using either the numeric ID or the
   * `handle:gold` syntax.
   *
   * @returns Created
   *
   * @throws {@link EventsBasedBillingSegments.CreateSegmentError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createSegment(
    request: EventsBasedBillingSegments.CreateSegmentRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SegmentResponse, EventsBasedBillingSegments.CreateSegmentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/segments.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.string() },
          { name: "price_point_id", value: request.pricePointId, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createSegmentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: segmentResponseSchema },
        errorFactory: EventsBasedBillingSegments.CreateSegmentError,
      },
      options,
    );
  }

  /**
   * Delete Single Segment
   *
   * @remarks
   * Deletes a segment with the specified ID.
   *
   * You may specify component and/or price point by using either the numeric ID or the
   * `handle:gold` syntax.
   *
   * @returns No Content
   *
   * @throws {@link EventsBasedBillingSegments.DeleteSegmentError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteSegment(
    request: EventsBasedBillingSegments.DeleteSegmentRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, EventsBasedBillingSegments.DeleteSegmentError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/segments/{id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.string() },
          { name: "price_point_id", value: request.pricePointId, schema: s.string() },
          { name: "id", value: request.id, schema: s.float64() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: EventsBasedBillingSegments.DeleteSegmentError,
      },
      options,
    );
  }

  /**
   * List Segments for a Price Point
   *
   * @remarks
   * Lists segments created for a given price point, in order of creation.
   *
   * You can pass `page` and `per_page` parameters in order to access all of the segments. By
   * default it will return `30` records. You can set `per_page` to `200` at most.
   *
   * You may specify component and/or price point by using either the numeric ID or the
   * `handle:gold` syntax.
   *
   * @returns OK
   *
   * @throws {@link EventsBasedBillingSegments.ListSegmentsForPricePointError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSegmentsForPricePoint(
    request: EventsBasedBillingSegments.ListSegmentsForPricePointRequest,
    options?: RequestOptions,
  ): ApiPromise<ListSegmentsResponse, EventsBasedBillingSegments.ListSegmentsForPricePointError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/segments.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.string() },
          { name: "price_point_id", value: request.pricePointId, schema: s.string() },
        ],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 30) },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listSegmentsFilterSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listSegmentsResponseSchema },
        errorFactory: EventsBasedBillingSegments.ListSegmentsForPricePointError,
      },
      options,
    );
  }

  /**
   * Update Single Segment
   *
   * @remarks
   * Updates a single segment for a component with a segmented metric. You can also update the
   * pricing for the segment.
   *
   * You can specify component and/or price point by using either the numeric ID or the
   * `handle:gold` syntax.
   *
   * @returns OK
   *
   * @throws {@link EventsBasedBillingSegments.UpdateSegmentError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateSegment(
    request: EventsBasedBillingSegments.UpdateSegmentRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SegmentResponse, EventsBasedBillingSegments.UpdateSegmentError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/components/{component_id}/price_points/{price_point_id}/segments/{id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "component_id", value: request.componentId, schema: s.string() },
          { name: "price_point_id", value: request.pricePointId, schema: s.string() },
          { name: "id", value: request.id, schema: s.float64() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateSegmentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: segmentResponseSchema },
        errorFactory: EventsBasedBillingSegments.UpdateSegmentError,
      },
      options,
    );
  }
}

export namespace EventsBasedBillingSegments {
  export type BulkCreateSegmentsRequest = {
    /** ID or Handle for the Component */
    componentId: string;
    /** ID or Handle for the Price Point belonging to the Component */
    pricePointId: string;
    body?: BulkCreateSegments;
  };

  export class BulkCreateSegmentsError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"eventBasedBillingSegment1", EventBasedBillingSegment1>
    >;

    static readonly errors: ErrorDecoders<BulkCreateSegmentsError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "eventBasedBillingSegment1",
        decode: { kind: "json", schema: eventBasedBillingSegment1Schema },
      },
    ];
  }

  export type BulkUpdateSegmentsRequest = {
    /** ID or Handle for the Component */
    componentId: string;
    /** ID or Handle for the Price Point belonging to the Component */
    pricePointId: string;
    body?: BulkUpdateSegments;
  };

  export class BulkUpdateSegmentsError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"eventBasedBillingSegment1", EventBasedBillingSegment1>
    >;

    static readonly errors: ErrorDecoders<BulkUpdateSegmentsError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "eventBasedBillingSegment1",
        decode: { kind: "json", schema: eventBasedBillingSegment1Schema },
      },
    ];
  }

  export type CreateSegmentRequestParams = {
    /** ID or Handle for the Component */
    componentId: string;
    /** ID or Handle for the Price Point belonging to the Component */
    pricePointId: string;
    body?: CreateSegmentRequest;
  };

  export class CreateSegmentError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error404", undefined>
      | Declared<"eventBasedBillingSegmentErrors1", EventBasedBillingSegmentErrors1>
    >;

    static readonly errors: ErrorDecoders<CreateSegmentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "eventBasedBillingSegmentErrors1",
        decode: { kind: "json", schema: eventBasedBillingSegmentErrors1Schema },
      },
    ];
  }

  export type DeleteSegmentRequest = {
    /** ID or Handle of the Component */
    componentId: string;
    /** ID or Handle of the Price Point belonging to the Component */
    pricePointId: string;
    /** The ID of the Segment */
    id: number;
  };

  export class DeleteSegmentError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined> | Declared<"error422", undefined>>;

    static readonly errors: ErrorDecoders<DeleteSegmentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "error422", decode: { kind: "empty" } },
    ];
  }

  export type ListSegmentsForPricePointRequest = {
    /** ID or Handle for the Component */
    componentId: string;
    /** ID or Handle for the Price Point belonging to the Component */
    pricePointId: string;
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
     * This parameter indicates how many records to fetch in each request. Default value is 30. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in
     * query `per_page=200`.
     *
     * @default 30
     */
    perPage?: number;
    /** Filter to use for List Segments for a Price Point operation */
    filter?: ListSegmentsFilter;
  };

  export class ListSegmentsForPricePointError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error404", undefined>
      | Declared<"eventBasedBillingListSegmentsErrors1", EventBasedBillingListSegmentsErrors1>
    >;

    static readonly errors: ErrorDecoders<ListSegmentsForPricePointError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "eventBasedBillingListSegmentsErrors1",
        decode: { kind: "json", schema: eventBasedBillingListSegmentsErrors1Schema },
      },
    ];
  }

  export type UpdateSegmentRequestParams = {
    /** ID or Handle of the Component */
    componentId: string;
    /** ID or Handle of the Price Point belonging to the Component */
    pricePointId: string;
    /** The ID of the Segment */
    id: number;
    body?: UpdateSegmentRequest;
  };

  export class UpdateSegmentError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error404", undefined>
      | Declared<"eventBasedBillingSegmentErrors1", EventBasedBillingSegmentErrors1>
    >;

    static readonly errors: ErrorDecoders<UpdateSegmentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "eventBasedBillingSegmentErrors1",
        decode: { kind: "json", schema: eventBasedBillingSegmentErrors1Schema },
      },
    ];
  }
}
