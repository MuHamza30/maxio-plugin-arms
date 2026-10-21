import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { batchJobResponseSchema, type BatchJobResponse } from "../models/batch-job-response.js";
import { invoiceSchema, type Invoice } from "../models/invoice.js";
import { proformaInvoiceSchema, type ProformaInvoice } from "../models/proforma-invoice.js";
import { singleErrorResponse1Schema, type SingleErrorResponse1 } from "../models/single-error-response1.js";
import { subscriptionSchema, type Subscription } from "../models/subscription.js";
import type { Servers } from "../servers.js";

export class ApiExports {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Invoices Export
   *
   * @remarks
   * Creates an invoices export and returns a batch job object.
   *
   * @returns Created
   *
   * @throws {@link ApiExports.ExportInvoicesError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  exportInvoices(options?: RequestOptions): ApiPromise<BatchJobResponse, ApiExports.ExportInvoicesError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/api_exports/invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: batchJobResponseSchema },
        errorFactory: ApiExports.ExportInvoicesError,
      },
      options,
    );
  }

  /**
   * Create Proforma Invoices Export
   *
   * @remarks
   * Creates a proforma invoices export and returns a batch job object. Proforma invoices are only
   * available on Relationship Invoicing sites.
   *
   * @returns Created
   *
   * @throws {@link ApiExports.ExportProformaInvoicesError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  exportProformaInvoices(
    options?: RequestOptions,
  ): ApiPromise<BatchJobResponse, ApiExports.ExportProformaInvoicesError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/api_exports/proforma_invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: batchJobResponseSchema },
        errorFactory: ApiExports.ExportProformaInvoicesError,
      },
      options,
    );
  }

  /**
   * Create Subscriptions Export
   *
   * @remarks
   * Creates a subscriptions export and returns a batch job object.
   *
   * @returns Created
   *
   * @throws {@link ApiExports.ExportSubscriptionsError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  exportSubscriptions(
    options?: RequestOptions,
  ): ApiPromise<BatchJobResponse, ApiExports.ExportSubscriptionsError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/api_exports/subscriptions.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: batchJobResponseSchema },
        errorFactory: ApiExports.ExportSubscriptionsError,
      },
      options,
    );
  }

  /**
   * List Exported Invoices
   *
   * @remarks
   * Lists exported invoices for a provided `batch_id`. Use pagination to control responses returned
   * from the server.
   *
   * Example: `GET
   * https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page=10000&page=1`.
   *
   * @returns OK
   *
   * @throws {@link ApiExports.ListExportedInvoicesError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listExportedInvoices(
    request: ApiExports.ListExportedInvoicesRequest,
    options?: RequestOptions,
  ): ApiPromise<Invoice[], ApiExports.ListExportedInvoicesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/api_exports/invoices/{batch_id}/rows.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "batch_id", value: request.batchId, schema: s.string() }],
        query: [
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 100) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => invoiceSchema)) },
        errorFactory: ApiExports.ListExportedInvoicesError,
      },
      options,
    );
  }

  /**
   * List Exported Proforma Invoices
   *
   * @remarks
   * Lists exported proforma invoices for a provided `batch_id`. Use pagination to control responses
   * returned from the server.
   *
   * Example: `GET
   * https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows?per_page=10000&page=1`.
   *
   * @returns OK
   *
   * @throws {@link ApiExports.ListExportedProformaInvoicesError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listExportedProformaInvoices(
    request: ApiExports.ListExportedProformaInvoicesRequest,
    options?: RequestOptions,
  ): ApiPromise<ProformaInvoice[], ApiExports.ListExportedProformaInvoicesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/api_exports/proforma_invoices/{batch_id}/rows.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "batch_id", value: request.batchId, schema: s.string() }],
        query: [
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 100) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => proformaInvoiceSchema)) },
        errorFactory: ApiExports.ListExportedProformaInvoicesError,
      },
      options,
    );
  }

  /**
   * List Exported Subscriptions
   *
   * @remarks
   * Lists exported subscriptions for a provided `batch_id`. Use pagination to control responses
   * returned from the server.
   *
   * Example: `GET
   * https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per_page=200&page=1`.
   *
   * @returns OK
   *
   * @throws {@link ApiExports.ListExportedSubscriptionsError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listExportedSubscriptions(
    request: ApiExports.ListExportedSubscriptionsRequest,
    options?: RequestOptions,
  ): ApiPromise<Subscription[], ApiExports.ListExportedSubscriptionsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/api_exports/subscriptions/{batch_id}/rows.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "batch_id", value: request.batchId, schema: s.string() }],
        query: [
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 100) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => subscriptionSchema)) },
        errorFactory: ApiExports.ListExportedSubscriptionsError,
      },
      options,
    );
  }

  /**
   * Read Invoices Export
   *
   * @remarks
   * Returns a batch job object for an invoices export.
   *
   * @returns OK
   *
   * @throws {@link ApiExports.ReadInvoicesExportError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readInvoicesExport(
    request: ApiExports.ReadInvoicesExportRequest,
    options?: RequestOptions,
  ): ApiPromise<BatchJobResponse, ApiExports.ReadInvoicesExportError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/api_exports/invoices/{batch_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "batch_id", value: request.batchId, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: batchJobResponseSchema },
        errorFactory: ApiExports.ReadInvoicesExportError,
      },
      options,
    );
  }

  /**
   * Read Proforma Invoices Export
   *
   * @remarks
   * Returns a batch job object for a proforma invoices export. Proforma invoices are only available
   * on Relationship Invoicing sites.
   *
   * @returns OK
   *
   * @throws {@link ApiExports.ReadProformaInvoicesExportError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readProformaInvoicesExport(
    request: ApiExports.ReadProformaInvoicesExportRequest,
    options?: RequestOptions,
  ): ApiPromise<BatchJobResponse, ApiExports.ReadProformaInvoicesExportError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/api_exports/proforma_invoices/{batch_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "batch_id", value: request.batchId, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: batchJobResponseSchema },
        errorFactory: ApiExports.ReadProformaInvoicesExportError,
      },
      options,
    );
  }

  /**
   * Read Subscriptions Export
   *
   * @remarks
   * Returns a batch job object for a subscriptions export.
   *
   * @returns OK
   *
   * @throws {@link ApiExports.ReadSubscriptionsExportError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSubscriptionsExport(
    request: ApiExports.ReadSubscriptionsExportRequest,
    options?: RequestOptions,
  ): ApiPromise<BatchJobResponse, ApiExports.ReadSubscriptionsExportError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/api_exports/subscriptions/{batch_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "batch_id", value: request.batchId, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: batchJobResponseSchema },
        errorFactory: ApiExports.ReadSubscriptionsExportError,
      },
      options,
    );
  }
}

export namespace ApiExports {
  export class ExportInvoicesError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"singleErrorResponse1", SingleErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<ExportInvoicesError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 409, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }

  export class ExportProformaInvoicesError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"singleErrorResponse1", SingleErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<ExportProformaInvoicesError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 409, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }

  export class ExportSubscriptionsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"singleErrorResponse1", SingleErrorResponse1>>;

    static readonly errors: ErrorDecoders<ExportSubscriptionsError> = [
      { on: 409, kind: "singleErrorResponse1", decode: { kind: "json", schema: singleErrorResponse1Schema } },
    ];
  }

  export type ListExportedInvoicesRequest = {
    /** Id of a Batch Job. */
    batchId: string;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 100. The
     * maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
     *
     * @default 100
     */
    perPage?: number;
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
  };

  export class ListExportedInvoicesError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ListExportedInvoicesError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ListExportedProformaInvoicesRequest = {
    /** Id of a Batch Job. */
    batchId: string;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 100. The
     * maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
     *
     * @default 100
     */
    perPage?: number;
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
  };

  export class ListExportedProformaInvoicesError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ListExportedProformaInvoicesError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ListExportedSubscriptionsRequest = {
    /** Id of a Batch Job. */
    batchId: string;
    /**
     * This parameter indicates how many records to fetch in each request. Default value is 100. The
     * maximum allowed values is 10000; any per_page value over 10000 will be changed to 10000.
     *
     * @default 100
     */
    perPage?: number;
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
  };

  export class ListExportedSubscriptionsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ListExportedSubscriptionsError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ReadInvoicesExportRequest = {
    /** Id of a Batch Job. */
    batchId: string;
  };

  export class ReadInvoicesExportError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ReadInvoicesExportError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ReadProformaInvoicesExportRequest = {
    /** Id of a Batch Job. */
    batchId: string;
  };

  export class ReadProformaInvoicesExportError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ReadProformaInvoicesExportError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ReadSubscriptionsExportRequest = {
    /** Id of a Batch Job. */
    batchId: string;
  };

  export class ReadSubscriptionsExportError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ReadSubscriptionsExportError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }
}
