import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { basicDateFieldSchema, type BasicDateField } from "../models/basic-date-field.js";
import {
  createMetadataRequestSchema,
  type CreateMetadataRequest,
} from "../models/create-metadata-request.js";
import {
  createMetafieldsRequestSchema,
  type CreateMetafieldsRequest,
} from "../models/create-metafields-request.js";
import {
  listMetafieldsResponseSchema,
  type ListMetafieldsResponse,
} from "../models/list-metafields-response.js";
import { metadataSchema, type Metadata } from "../models/metadata.js";
import { metafieldSchema, type Metafield } from "../models/metafield.js";
import { paginatedMetadataSchema, type PaginatedMetadata } from "../models/paginated-metadata.js";
import { resourceTypeSchema, type ResourceType } from "../models/resource-type.js";
import { singleErrorResponse1Schema, type SingleErrorResponse1 } from "../models/single-error-response1.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import {
  updateMetadataRequestSchema,
  type UpdateMetadataRequest,
} from "../models/update-metadata-request.js";
import {
  updateMetafieldsRequestSchema,
  type UpdateMetafieldsRequest,
} from "../models/update-metafields-request.js";
import type { Servers } from "../servers.js";

export class CustomFields {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Metadata
   *
   * @remarks
   * Creates metadata and metafields for a specific subscription or customer, or updates metadata
   * values of existing metafields for a subscription or customer. Metadata values are limited to 2
   * KB in size.
   *
   * If you create metadata on a subscription or customer with a metafield that does not already
   * exist, the metafield is created with the metadata you specify and it is always added as a text
   * field. You can update the input_type for the metafield with the [Update
   * Metafield]($e/Custom%20Fields/updateMetafield) endpoint.
   *
   * >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100
   * metafields for Subscriptions and another 100 for Customers.
   *
   * @returns OK
   *
   * @throws {@link CustomFields.CreateMetadataError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createMetadata(
    request: CustomFields.CreateMetadataRequestParams,
    options?: RequestOptions,
  ): ApiPromise<Metadata[], CustomFields.CreateMetadataError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/{resource_type}/{resource_id}/metadata.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "resource_type", value: request.resourceType, schema: resourceTypeSchema },
          { name: "resource_id", value: request.resourceId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createMetadataRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => metadataSchema)) },
        errorFactory: CustomFields.CreateMetadataError,
      },
      options,
    );
  }

  /**
   * Create Metafields
   *
   * @remarks
   * Creates metafields on a Site for either the Subscriptions or Customers resource.
   *
   * Metafields and their metadata are created in the Custom Fields configuration page on your Site.
   * Metafields can be populated with metadata when you create them or later with the [Update
   * Metafield]($e/Custom%20Fields/updateMetafield), [Create
   * Metadata]($e/Custom%20Fields/createMetadata), or [Update
   * Metadata]($e/Custom%20Fields/updateMetadata) endpoints. The Create Metadata and Update Metadata
   * endpoints allow you to add metafields and metadata values to a specific subscription or
   * customer.
   *
   * Each site is limited to 100 unique metafields per resource. This means you can have 100
   * metafields for Subscriptions and another 100 for Customers.
   *
   * > Note: After creating a metafield, the resource type cannot be modified.
   *
   * In the UI and product documentation, metafields and metadata are called Custom Fields.
   *
   * - Metafield is the custom field
   * - Metadata is the data populating the custom field.
   *
   * See [Custom Fields
   * Reference](https://docs.maxio.com/hc/en-us/articles/24266140850573-Custom-Fields-Reference) and
   * [Custom Fields
   * Tab](https://maxio.zendesk.com/hc/en-us/articles/24251701302925-Subscription-Summary-Custom-Fields-Tab)
   * for information on using Custom Fields in the Advanced Billing UI.
   *
   * @returns OK
   *
   * @throws {@link CustomFields.CreateMetafieldsError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createMetafields(
    request: CustomFields.CreateMetafieldsRequestParams,
    options?: RequestOptions,
  ): ApiPromise<Metafield[], CustomFields.CreateMetafieldsError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/{resource_type}/metafields.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "resource_type", value: request.resourceType, schema: resourceTypeSchema }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createMetafieldsRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => metafieldSchema)) },
        errorFactory: CustomFields.CreateMetafieldsError,
      },
      options,
    );
  }

  /**
   * Delete Metadata
   *
   * @remarks
   * Deletes one or more metafields (and associated metadata) from the specified subscription or
   * customer.
   *
   * @returns OK
   *
   * @throws {@link CustomFields.DeleteMetadataError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteMetadata(
    request: CustomFields.DeleteMetadataRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, CustomFields.DeleteMetadataError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/{resource_type}/{resource_id}/metadata.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "resource_type", value: request.resourceType, schema: resourceTypeSchema },
          { name: "resource_id", value: request.resourceId, schema: s.int() },
        ],
        query: [
          { name: "name", value: request.name, schema: s.optional(s.string()) },
          { name: "names", value: request.names, schema: s.optional(s.array(s.string())) },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: CustomFields.DeleteMetadataError,
      },
      options,
    );
  }

  /**
   * Delete Metafield
   *
   * @remarks
   * Deletes a metafield from your Site. Removes the metafield and associated metadata from all
   * Subscriptions or Customers resources on the Site.
   *
   * @returns OK
   *
   * @throws {@link CustomFields.DeleteMetafieldError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteMetafield(
    request: CustomFields.DeleteMetafieldRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, CustomFields.DeleteMetafieldError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/{resource_type}/metafields.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "resource_type", value: request.resourceType, schema: resourceTypeSchema }],
        query: [{ name: "name", value: request.name, schema: s.optional(s.string()) }],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: CustomFields.DeleteMetafieldError,
      },
      options,
    );
  }

  /**
   * List Metadata
   *
   * @remarks
   * Lists metadata and metafields for a specific customer or subscription.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listMetadata(
    request: CustomFields.ListMetadataRequest,
    options?: RequestOptions,
  ): ApiPromise<PaginatedMetadata, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/{resource_type}/{resource_id}/metadata.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "resource_type", value: request.resourceType, schema: resourceTypeSchema },
          { name: "resource_id", value: request.resourceId, schema: s.int() },
        ],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: paginatedMetadataSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Metadata for Resource Type
   *
   * @remarks
   * Lists metadata for a specified array of subscriptions or customers.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listMetadataForResourceType(
    request: CustomFields.ListMetadataForResourceTypeRequest,
    options?: RequestOptions,
  ): ApiPromise<PaginatedMetadata, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/{resource_type}/metadata.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "resource_type", value: request.resourceType, schema: resourceTypeSchema }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => basicDateFieldSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.dateOnly()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.dateOnly()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.dateTime()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.dateTime()) },
          { name: "with_deleted", value: request.withDeleted, schema: s.optional(s.boolean()) },
          { name: "resource_ids", value: request.resourceIds, schema: s.optional(s.array(s.int())) },
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: paginatedMetadataSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Metafields
   *
   * @remarks
   * Lists the metafields and their associated details for a Site and resource type. You can filter
   * the request to a specific metafield.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listMetafields(
    request: CustomFields.ListMetafieldsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListMetafieldsResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/{resource_type}/metafields.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "resource_type", value: request.resourceType, schema: resourceTypeSchema }],
        query: [
          { name: "name", value: request.name, schema: s.optional(s.string()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listMetafieldsResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Metadata
   *
   * @remarks
   * Updates metadata and metafields on the Site and the customer or subscription specified, and
   * updates the metadata value on a subscription or customer.
   *
   * If you update metadata on a subscription or customer with a metafield that does not already
   * exist, the metafield is created with the metadata you specify and it is always added as a text
   * field to the Site and to the subscription or customer you specify. You can update the
   * input_type for the metafield with the Update Metafield endpoint.
   *
   * Each site is limited to 100 unique metafields per resource. This means you can have 100
   * metafields for the Subscription resource and another 100 for the Customer resource.
   *
   * @returns OK
   *
   * @throws {@link CustomFields.UpdateMetadataError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateMetadata(
    request: CustomFields.UpdateMetadataRequestParams,
    options?: RequestOptions,
  ): ApiPromise<Metadata[], CustomFields.UpdateMetadataError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/{resource_type}/{resource_id}/metadata.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "resource_type", value: request.resourceType, schema: resourceTypeSchema },
          { name: "resource_id", value: request.resourceId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateMetadataRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => metadataSchema)) },
        errorFactory: CustomFields.UpdateMetadataError,
      },
      options,
    );
  }

  /**
   * Update Metafield
   *
   * @remarks
   * Updates metafields on your Site for a resource type. Depending on the request structure, you
   * can update or add metafields and metadata to the Subscriptions or Customers resource.
   *
   * With this endpoint, you can:
   *
   * - Add metafields. If the metafield specified in current_name does not exist, a new metafield is
   *   added. >Note: Each site is limited to 100 unique metafields per resource. This means you can
   *   have 100 metafields for Subscriptions and another 100 for Customers.
   *
   * - Change the name of a metafield. >Note: To keep the metafield name the same and only update
   *   the metadata for the metafield, you must use the current metafield name in both the
   *   `current_name` and `name` parameters.
   *
   * - Change the input type for the metafield. For example, you can change a metafield input type
   *   from text to a dropdown. If you change the input type from text to a dropdown or radio, you
   *   must update the specific subscriptions or customers where the metafield was used to reflect
   *   the updated metafield and metadata.
   *
   * - Add metadata values to the existing metadata for a dropdown or radio metafield. >Note:
   *   Updates to metadata overwrite. To add one or more values, you must specify all metadata
   *   values including the new value you want to add.
   *
   * - Add new metadata to a dropdown or radio for a metafield that was created without metadata.
   *
   * - Remove metadata for a dropdown or radio for a metafield. >Note: Updates to metadata overwrite
   *   existing values. To remove one or more values, specify all metadata values except those you
   *   want to remove.
   *
   * - Add or update scope settings for a metafield. >Note: Scope changes overwrite existing
   *   settings. You must specify the complete scope, including the changes you want to make.
   *
   * @returns OK
   *
   * @throws {@link CustomFields.UpdateMetafieldError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateMetafield(
    request: CustomFields.UpdateMetafieldRequest,
    options?: RequestOptions,
  ): ApiPromise<Metafield[], CustomFields.UpdateMetafieldError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/{resource_type}/metafields.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "resource_type", value: request.resourceType, schema: resourceTypeSchema }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateMetafieldsRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => metafieldSchema)) },
        errorFactory: CustomFields.UpdateMetafieldError,
      },
      options,
    );
  }
}

export namespace CustomFields {
  export type CreateMetadataRequestParams = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    /**
     * The Advanced Billing id of the customer or the subscription for which the metadata applies
     */
    resourceId: number;
    body?: CreateMetadataRequest;
  };

  export class CreateMetadataError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"singleErrorResponse1", SingleErrorResponse1>>;

    static readonly errors: ErrorDecoders<CreateMetadataError> = [
      { on: 422, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }

  export type CreateMetafieldsRequestParams = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    body?: CreateMetafieldsRequest;
  };

  export class CreateMetafieldsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"singleErrorResponse1", SingleErrorResponse1>>;

    static readonly errors: ErrorDecoders<CreateMetafieldsError> = [
      { on: 422, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }

  export type DeleteMetadataRequest = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    /**
     * The Advanced Billing id of the customer or the subscription for which the metadata applies
     */
    resourceId: number;
    /** Name of field to be removed. */
    name?: string;
    /**
     * Names of fields to be removed. Use in query:
     * `names[]=field1&names[]=my-field&names[]=another-field`.
     */
    names?: string[];
  };

  export class DeleteMetadataError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<DeleteMetadataError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type DeleteMetafieldRequest = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    /** The name of the metafield to be deleted */
    name?: string;
  };

  export class DeleteMetafieldError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<DeleteMetafieldError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ListMetadataRequest = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    /**
     * The Advanced Billing id of the customer or the subscription for which the metadata applies
     */
    resourceId: number;
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

  export type ListMetadataForResourceTypeRequest = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
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
    /** The type of filter you would like to apply to your search. */
    dateField?: BasicDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with
     * a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
     * timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns metadata with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of start_date.
     */
    startDatetime?: Date;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns metadata with a timestamp at or before exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of end_date.
     */
    endDatetime?: Date;
    /** Allow to fetch deleted metadata. */
    withDeleted?: boolean;
    /**
     * Allow to fetch metadata for multiple records based on provided ids. Use in query:
     * `resource_ids[]=122&resource_ids[]=123&resource_ids[]=124`.
     */
    resourceIds?: number[];
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
  };

  export type ListMetafieldsRequest = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    /** Filter by the name of the metafield. */
    name?: string;
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
  };

  export type UpdateMetadataRequestParams = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    /**
     * The Advanced Billing id of the customer or the subscription for which the metadata applies
     */
    resourceId: number;
    body?: UpdateMetadataRequest;
  };

  export class UpdateMetadataError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"singleErrorResponse1", SingleErrorResponse1>>;

    static readonly errors: ErrorDecoders<UpdateMetadataError> = [
      { on: 422, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }

  export type UpdateMetafieldRequest = {
    /** The resource type to which the metafields belong. */
    resourceType: ResourceType;
    body?: UpdateMetafieldsRequest;
  };

  export class UpdateMetafieldError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"singleErrorResponse1", SingleErrorResponse1>>;

    static readonly errors: ErrorDecoders<UpdateMetafieldError> = [
      { on: 422, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }
}
