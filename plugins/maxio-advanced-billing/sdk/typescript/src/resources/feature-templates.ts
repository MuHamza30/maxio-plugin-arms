import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createFeatureTemplateRequestSchema,
  type CreateFeatureTemplateRequest,
} from "../models/create-feature-template-request.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  featureTemplateResponseSchema,
  type FeatureTemplateResponse,
} from "../models/feature-template-response.js";
import {
  featureTemplatesListResponseSchema,
  type FeatureTemplatesListResponse,
} from "../models/feature-templates-list-response.js";
import { kindSchema, type Kind } from "../models/kind.js";
import { SortBy, sortBySchema } from "../models/sort-by.js";
import { SortDirection, sortDirectionSchema } from "../models/sort-direction.js";
import { Status1, status1Schema } from "../models/status1.js";
import {
  updateFeatureTemplateRequestSchema,
  type UpdateFeatureTemplateRequest,
} from "../models/update-feature-template-request.js";
import type { Servers } from "../servers.js";

/**
 * The Feature Template object defines a feature once at the site level, such as Single Sign-On, a
 * monthly API call limit, or a support tier.
 *
 * A feature template is not billable on its own. Attach the template to products or components to
 * grant the feature to subscribers. The kind (access_right, usage_limit, or service_right)
 * determines how the feature's value behaves. For more information, see [Configure
 * Entitlements](https://docs.maxio.com/billing/catalog/entitlements/configure-entitlements).
 */
export class FeatureTemplates {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Feature Template
   *
   * @remarks
   * Archives a feature template. Archived feature templates are not addressable via [Read Feature
   * Template]($e/Feature%20Templates/readFeatureTemplate) or [Update Feature
   * Template]($e/Feature%20Templates/updateFeatureTemplate). Both endpoints return `404` until the
   * template is restored.
   *
   * The feature template record itself is never hard-deleted, and can always be restored with
   * [Restore Feature Template]($e/Feature%20Templates/restoreFeatureTemplate). Reversibility does
   * not extend to `remove_from_catalog=true`: the feature catalog items and entitlements that
   * parameter destroys are gone permanently, and restoring the template will not bring subscriber
   * access back.
   *
   * @returns No Content
   *
   * @throws {@link FeatureTemplates.ArchiveFeatureTemplateError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveFeatureTemplate(
    request: FeatureTemplates.ArchiveFeatureTemplateRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, FeatureTemplates.ArchiveFeatureTemplateError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [
          {
            name: "remove_from_catalog",
            value: request.removeFromCatalog,
            schema: s.defaulted(s.boolean(), false),
          },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: FeatureTemplates.ArchiveFeatureTemplateError,
      },
      options,
    );
  }

  /**
   * Create Feature Template
   *
   * @remarks
   * Defines a new feature at the site level. Feature templates aren't billable on their own. Attach
   * a template to products or components to grant the feature to subscribers.
   *
   * @returns Created
   *
   * @throws {@link FeatureTemplates.CreateFeatureTemplateError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createFeatureTemplate(
    request: FeatureTemplates.CreateFeatureTemplateRequestParams,
    options?: RequestOptions,
  ): ApiPromise<FeatureTemplateResponse, FeatureTemplates.CreateFeatureTemplateError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/features.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createFeatureTemplateRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: featureTemplateResponseSchema },
        errorFactory: FeatureTemplates.CreateFeatureTemplateError,
      },
      options,
    );
  }

  /**
   * List Feature Templates
   *
   * @remarks
   * Lists the feature templates defined for your site, active (non-archived) ones by default. Pass
   * `status=archived` or `status=all` to widen the result set.
   *
   * Supply `page` or `per_page` to paginate. Without either parameter, the response includes the
   * full result set.
   *
   * @returns OK
   *
   * @throws {@link FeatureTemplates.ListFeatureTemplatesError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listFeatureTemplates(
    request: FeatureTemplates.ListFeatureTemplatesRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureTemplatesListResponse, FeatureTemplates.ListFeatureTemplatesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/features.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "status", value: request.status, schema: s.defaulted(status1Schema, Status1.Active) },
          { name: "q", value: request.q, schema: s.optional(s.string()) },
          { name: "kind", value: request.kind, schema: s.optional(s.lazy(() => kindSchema)) },
          { name: "updated_from", value: request.updatedFrom, schema: s.optional(s.dateOnly()) },
          { name: "updated_to", value: request.updatedTo, schema: s.optional(s.dateOnly()) },
          { name: "sort_by", value: request.sortBy, schema: s.defaulted(sortBySchema, SortBy.Name) },
          {
            name: "sort_direction",
            value: request.sortDirection,
            schema: s.defaulted(sortDirectionSchema, SortDirection.Asc),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureTemplatesListResponseSchema },
        errorFactory: FeatureTemplates.ListFeatureTemplatesError,
      },
      options,
    );
  }

  /**
   * Read Feature Template
   *
   * @remarks
   * Returns a single feature template. Archived feature templates are not addressable here and
   * return `404`. Restore a template first to read or update it.
   *
   * @returns OK
   *
   * @throws {@link FeatureTemplates.ReadFeatureTemplateError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readFeatureTemplate(
    request: FeatureTemplates.ReadFeatureTemplateRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureTemplateResponse, FeatureTemplates.ReadFeatureTemplateError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureTemplateResponseSchema },
        errorFactory: FeatureTemplates.ReadFeatureTemplateError,
      },
      options,
    );
  }

  /**
   * Restore Feature Template
   *
   * @remarks
   * Clears the feature template's archived state. Feature catalog items created from this template
   * are not automatically restored. Restore each one individually.
   *
   * @returns OK
   *
   * @throws {@link FeatureTemplates.RestoreFeatureTemplateError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  restoreFeatureTemplate(
    request: FeatureTemplates.RestoreFeatureTemplateRequest,
    options?: RequestOptions,
  ): ApiPromise<FeatureTemplateResponse, FeatureTemplates.RestoreFeatureTemplateError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/features/{id}/restore.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: featureTemplateResponseSchema },
        errorFactory: FeatureTemplates.RestoreFeatureTemplateError,
      },
      options,
    );
  }

  /**
   * Update Feature Template
   *
   * @remarks
   * Updates the name, description, unit, value type, default value, or default periodicity of a
   * feature template. `key` is rejected on every update. `kind` is rejected once any feature
   * catalog item has been created from this template.
   *
   * Archived feature templates are not addressable here and return `404`. Restore a template first
   * to update it.
   *
   * @returns OK
   *
   * @throws {@link FeatureTemplates.UpdateFeatureTemplateError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateFeatureTemplate(
    request: FeatureTemplates.UpdateFeatureTemplateRequestParams,
    options?: RequestOptions,
  ): ApiPromise<FeatureTemplateResponse, FeatureTemplates.UpdateFeatureTemplateError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/features/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateFeatureTemplateRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: featureTemplateResponseSchema },
        errorFactory: FeatureTemplates.UpdateFeatureTemplateError,
      },
      options,
    );
  }
}

export namespace FeatureTemplates {
  export type ArchiveFeatureTemplateRequest = {
    /** The Advanced Billing id of the feature template. */
    id: number;
    /**
     * When `true`, also destroys every feature catalog item created from this template and cascades
     * to their entitlements, revoking subscriber access immediately. When `false` (default), the
     * feature template and its feature catalog items are archived, and existing entitlements are
     * preserved.
     *
     * @default false
     */
    removeFromCatalog?: boolean;
  };

  export class ArchiveFeatureTemplateError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Undeclared;

    static readonly errors: ErrorDecoders<ArchiveFeatureTemplateError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type CreateFeatureTemplateRequestParams = {
    body?: CreateFeatureTemplateRequest;
  };

  export class CreateFeatureTemplateError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"errorListResponse12", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<CreateFeatureTemplateError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListFeatureTemplatesRequest = {
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
    /**
     * Filters by archived state. Defaults to `active` (non-archived templates only).
     *
     * @default Status1.Active
     */
    status?: Status1;
    /** Filters to feature templates whose name contains this substring (case-insensitive). */
    q?: string;
    /** Filters by feature kind. */
    kind?: Kind;
    /** Returns feature templates updated on or after this date. */
    updatedFrom?: string;
    /** Returns feature templates updated on or before this date. */
    updatedTo?: string;
    /** The field to sort results by. @default SortBy.Name */
    sortBy?: SortBy;
    /** The sort direction of the returned feature templates. @default SortDirection.Asc */
    sortDirection?: SortDirection;
  };

  export class ListFeatureTemplatesError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<ListFeatureTemplatesError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadFeatureTemplateRequest = {
    /** The Advanced Billing id of the feature template. */
    id: number;
  };

  export class ReadFeatureTemplateError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Undeclared;

    static readonly errors: ErrorDecoders<ReadFeatureTemplateError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type RestoreFeatureTemplateRequest = {
    /** The Advanced Billing id of the feature template. */
    id: number;
  };

  export class RestoreFeatureTemplateError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<RestoreFeatureTemplateError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateFeatureTemplateRequestParams = {
    /** The Advanced Billing id of the feature template. */
    id: number;
    body?: UpdateFeatureTemplateRequest;
  };

  export class UpdateFeatureTemplateError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Declared<"errorListResponse12", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateFeatureTemplateError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
