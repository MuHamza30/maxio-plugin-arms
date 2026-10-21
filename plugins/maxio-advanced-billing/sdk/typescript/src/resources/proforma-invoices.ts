import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createSignupProformaPreviewIncludeSchema,
  type CreateSignupProformaPreviewInclude,
} from "../models/create-signup-proforma-preview-include.js";
import {
  createSubscriptionRequestSchema,
  type CreateSubscriptionRequest,
} from "../models/create-subscription-request.js";
import {
  deliverProformaInvoiceRequestSchema,
  type DeliverProformaInvoiceRequest,
} from "../models/deliver-proforma-invoice-request.js";
import { Direction, directionSchema } from "../models/direction.js";
import {
  errorArrayMapResponse1Schema,
  type ErrorArrayMapResponse1,
} from "../models/error-array-map-response1.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  listProformaInvoicesResponseSchema,
  type ListProformaInvoicesResponse,
} from "../models/list-proforma-invoices-response.js";
import {
  proformaBadRequestErrorResponse1Schema,
  type ProformaBadRequestErrorResponse1,
} from "../models/proforma-bad-request-error-response1.js";
import {
  proformaInvoiceStatusSchema,
  type ProformaInvoiceStatus,
} from "../models/proforma-invoice-status.js";
import { proformaInvoiceSchema, type ProformaInvoice } from "../models/proforma-invoice.js";
import {
  signupProformaPreviewResponseSchema,
  type SignupProformaPreviewResponse,
} from "../models/signup-proforma-preview-response.js";
import { voidInvoiceRequestSchema, type VoidInvoiceRequest } from "../models/void-invoice-request.js";
import type { Servers } from "../servers.js";

export class ProformaInvoices {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Consolidated Proforma Invoices
   *
   * @remarks
   * Creates a consolidated proforma invoice asynchronously. To find and view the new consolidated
   * proforma invoice, you can poll the subscription group listing for proforma invoices; only one
   * consolidated proforma invoice can be created per group at a time.
   *
   * If the information becomes outdated, simply void the old consolidated proforma invoice and
   * generate a new one.
   *
   * ## Restrictions
   *
   * Proforma invoices are only available on Relationship Invoicing sites. To create a proforma
   * invoice, the subscription must not be prepaid, and must be in a live state.
   *
   * @returns Created
   *
   * @throws {@link ProformaInvoices.CreateConsolidatedProformaInvoiceError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createConsolidatedProformaInvoice(
    request: ProformaInvoices.CreateConsolidatedProformaInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ProformaInvoices.CreateConsolidatedProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/proforma_invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: ProformaInvoices.CreateConsolidatedProformaInvoiceError,
      },
      options,
    );
  }

  /**
   * Create Proforma Invoice
   *
   * @remarks
   * Creates a proforma invoice and returns it as a response. If the information becomes outdated,
   * simply void the old proforma invoice and generate a new one.
   *
   * If you would like to preview the next billing amounts without generating a full proforma
   * invoice, use the renewal preview endpoint.
   *
   * ## Restrictions
   *
   * Proforma invoices are only available on Relationship Invoicing sites. To create a proforma
   * invoice, the subscription must not be in a group, must not be prepaid, and must be in a live
   * state.
   *
   * @returns OK
   *
   * @throws {@link ProformaInvoices.CreateProformaInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createProformaInvoice(
    request: ProformaInvoices.CreateProformaInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<ProformaInvoice, ProformaInvoices.CreateProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/proforma_invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: proformaInvoiceSchema },
        errorFactory: ProformaInvoices.CreateProformaInvoiceError,
      },
      options,
    );
  }

  /**
   * Create signup proforma invoice
   *
   * @remarks
   * Creates a proforma invoice to preview costs before a subscription's signup. This endpoint is
   * only available for Relationship Invoicing sites and cannot be used to create consolidated
   * proforma invoices or preview prepaid subscriptions. Like other proforma invoices, it can be
   * emailed to the customer, voided, and publicly viewed on the chargifypay domain.
   *
   * Pass a payload that resembles a subscription create or signup preview request. For example, you
   * can specify components, coupons/a referral, offers, custom pricing, and an existing customer or
   * payment profile to populate a shipping or billing address.
   *
   * A product and customer first name, last name, and email are the minimum requirements. We
   * recommend associating the proforma invoice with a customer_id to easily find their proforma
   * invoices, since the subscription_id will always be blank.
   *
   * @returns Created
   *
   * @throws {@link ProformaInvoices.CreateSignupProformaInvoiceError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createSignupProformaInvoice(
    request: ProformaInvoices.CreateSignupProformaInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<ProformaInvoice, ProformaInvoices.CreateSignupProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/proforma_invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: proformaInvoiceSchema },
        errorFactory: ProformaInvoices.CreateSignupProformaInvoiceError,
      },
      options,
    );
  }

  /**
   * Deliver Proforma Invoice
   *
   * @remarks
   * Delivers a proforma invoice programmatically via email. Supports email delivery to direct
   * recipients, carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.
   *
   * If `recipient_emails` is omitted, the system will fall back to the primary recipient derived
   * from the invoice or subscription. At least one recipient must be present, either via the
   * request body or via this default behavior, so an empty body may still succeed when defaults are
   * available.
   *
   * @returns Created
   *
   * @throws {@link ProformaInvoices.DeliverProformaInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deliverProformaInvoice(
    request: ProformaInvoices.DeliverProformaInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ProformaInvoice, ProformaInvoices.DeliverProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/proforma_invoices/{proforma_invoice_uid}/deliveries.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "proforma_invoice_uid", value: request.proformaInvoiceUid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => deliverProformaInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: proformaInvoiceSchema },
        errorFactory: ProformaInvoices.DeliverProformaInvoiceError,
      },
      options,
    );
  }

  /**
   * List Subscription Proforma Invoices
   *
   * @remarks
   * Lists proforma invoices for a subscription. By default, results only include totals, not
   * detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, or
   * `custom_fields`. To include breakdowns, pass the specific field as a key in the query with a
   * value set to `true`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listProformaInvoices(
    request: ProformaInvoices.ListProformaInvoicesRequest,
    options?: RequestOptions,
  ): ApiPromise<ListProformaInvoicesResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/proforma_invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          {
            name: "status",
            value: request.status,
            schema: s.optional(s.lazy(() => proformaInvoiceStatusSchema)),
          },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "direction",
            value: request.direction,
            schema: s.defaulted(directionSchema, Direction.Desc),
          },
          { name: "line_items", value: request.lineItems, schema: s.defaulted(s.boolean(), false) },
          { name: "discounts", value: request.discounts, schema: s.defaulted(s.boolean(), false) },
          { name: "taxes", value: request.taxes, schema: s.defaulted(s.boolean(), false) },
          { name: "credits", value: request.credits, schema: s.defaulted(s.boolean(), false) },
          { name: "payments", value: request.payments, schema: s.defaulted(s.boolean(), false) },
          { name: "custom_fields", value: request.customFields, schema: s.defaulted(s.boolean(), false) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listProformaInvoicesResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Subscription Group Proforma Invoices
   *
   * @remarks
   * Lists proforma invoices with a `consolidation_level` of parent for the subscription group.
   *
   * By default, proforma invoices returned on the index will only include totals, not detailed
   * breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`, `custom_fields`. To
   * include breakdowns, pass the specific field as a key in the query with a value set to true.
   *
   * @returns OK
   *
   * @throws {@link ProformaInvoices.ListSubscriptionGroupProformaInvoicesError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSubscriptionGroupProformaInvoices(
    request: ProformaInvoices.ListSubscriptionGroupProformaInvoicesRequest,
    options?: RequestOptions,
  ): ApiPromise<ListProformaInvoicesResponse, ProformaInvoices.ListSubscriptionGroupProformaInvoicesError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}/proforma_invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [
          { name: "line_items", value: request.lineItems, schema: s.defaulted(s.boolean(), false) },
          { name: "discounts", value: request.discounts, schema: s.defaulted(s.boolean(), false) },
          { name: "taxes", value: request.taxes, schema: s.defaulted(s.boolean(), false) },
          { name: "credits", value: request.credits, schema: s.defaulted(s.boolean(), false) },
          { name: "payments", value: request.payments, schema: s.defaulted(s.boolean(), false) },
          { name: "custom_fields", value: request.customFields, schema: s.defaulted(s.boolean(), false) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listProformaInvoicesResponseSchema },
        errorFactory: ProformaInvoices.ListSubscriptionGroupProformaInvoicesError,
      },
      options,
    );
  }

  /**
   * Preview Proforma Invoice
   *
   * @remarks
   * Previews the data that will be included on a given subscription's proforma invoice if one were
   * to be generated. It will have similar line items and totals as a renewal preview, but the
   * response will be presented in the format of a proforma invoice. Consequently it will include
   * additional information such as the name and addresses that will appear on the proforma invoice.
   *
   * The preview endpoint is subject to all the same conditions as the proforma invoice endpoint.
   * For example, previews are only available on the Relationship Invoicing architecture, and
   * previews cannot be made for end-of-life subscriptions.
   *
   * If all the data returned in the preview is as expected, you may then create a static proforma
   * invoice and send it to your customer. The data within a preview will not be saved and will not
   * be accessible after the call is made.
   *
   * Alternatively, if you have some proforma invoices already, you may make a preview call to
   * determine whether any billing information for the subscription's upcoming renewal has changed.
   *
   * @returns OK
   *
   * @throws {@link ProformaInvoices.PreviewProformaInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewProformaInvoice(
    request: ProformaInvoices.PreviewProformaInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<ProformaInvoice, ProformaInvoices.PreviewProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/proforma_invoices/preview.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: proformaInvoiceSchema },
        errorFactory: ProformaInvoices.PreviewProformaInvoiceError,
      },
      options,
    );
  }

  /**
   * Create signup proforma preview
   *
   * @remarks
   * Creates a signup preview in the format of a proforma invoice to preview costs before a
   * subscription's signup. This endpoint is only available for Relationship Invoicing sites and
   * cannot be used to create consolidated proforma invoice previews or preview prepaid
   * subscriptions. You have the option of previewing the first renewal's costs as well. The
   * proforma invoice preview will not be persisted.
   *
   * Pass a payload that resembles a subscription create or signup preview request. For example, you
   * can specify components, coupons/a referral, offers, custom pricing, and an existing customer or
   * payment profile to populate a shipping or billing address.
   *
   * A product and customer first name, last name, and email are the minimum requirements.
   *
   * @returns Created
   *
   * @throws {@link ProformaInvoices.PreviewSignupProformaInvoiceError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewSignupProformaInvoice(
    request: ProformaInvoices.PreviewSignupProformaInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<SignupProformaPreviewResponse, ProformaInvoices.PreviewSignupProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/proforma_invoices/preview.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.lazy(() => createSignupProformaPreviewIncludeSchema)),
          },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createSubscriptionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: signupProformaPreviewResponseSchema },
        errorFactory: ProformaInvoices.PreviewSignupProformaInvoiceError,
      },
      options,
    );
  }

  /**
   * Read Proforma Invoice
   *
   * @remarks
   * Returns the details of an existing proforma invoice.
   *
   * ## Restrictions
   *
   * Proforma invoices are only available on Relationship Invoicing sites.
   *
   * @returns OK
   *
   * @throws {@link ProformaInvoices.ReadProformaInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readProformaInvoice(
    request: ProformaInvoices.ReadProformaInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<ProformaInvoice, ProformaInvoices.ReadProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/proforma_invoices/{proforma_invoice_uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "proforma_invoice_uid", value: request.proformaInvoiceUid, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: proformaInvoiceSchema },
        errorFactory: ProformaInvoices.ReadProformaInvoiceError,
      },
      options,
    );
  }

  /**
   * Void Proforma Invoice
   *
   * @remarks
   * Voids a proforma invoice that has the status "draft".
   *
   * ## Restrictions
   *
   * Proforma invoices are only available on Relationship Invoicing sites.
   *
   * Only proforma invoices that have the appropriate status may be reopened. If the invoice
   * identified by {uid} does not have the appropriate status, the response will have HTTP status
   * code 422 and an error message.
   *
   * A reason for the void operation is required to be included in the request body. If one is not
   * provided, the response will have HTTP status code 422 and an error message.
   *
   * @returns OK
   *
   * @throws {@link ProformaInvoices.VoidProformaInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  voidProformaInvoice(
    request: ProformaInvoices.VoidProformaInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<ProformaInvoice, ProformaInvoices.VoidProformaInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/proforma_invoices/{proforma_invoice_uid}/void.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "proforma_invoice_uid", value: request.proformaInvoiceUid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => voidInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: proformaInvoiceSchema },
        errorFactory: ProformaInvoices.VoidProformaInvoiceError,
      },
      options,
    );
  }
}

export namespace ProformaInvoices {
  export type CreateConsolidatedProformaInvoiceRequest = {
    /** The uid of the subscription group */
    uid: string;
  };

  export class CreateConsolidatedProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateConsolidatedProformaInvoiceError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateProformaInvoiceRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class CreateProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateProformaInvoiceError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateSignupProformaInvoiceRequest = {
    body?: CreateSubscriptionRequest;
  };

  export class CreateSignupProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"proformaBadRequestErrorResponse1", ProformaBadRequestErrorResponse1>
      | Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateSignupProformaInvoiceError> = [
      {
        on: 400,
        kind: "proformaBadRequestErrorResponse1",
        decode: { kind: "json", schema: proformaBadRequestErrorResponse1Schema },
      },
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type DeliverProformaInvoiceRequestParams = {
    /** The uid of the proforma invoice */
    proformaInvoiceUid: string;
    body?: DeliverProformaInvoiceRequest;
  };

  export class DeliverProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<DeliverProformaInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListProformaInvoicesRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The beginning date range for the invoice's Due Date, in the YYYY-MM-DD format. */
    startDate?: string;
    /** The ending date range for the invoice's Due Date, in the YYYY-MM-DD format. */
    endDate?: string;
    /** The current status of the invoice. Allowed Values: draft, open, paid, pending, voided */
    status?: ProformaInvoiceStatus;
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
    /** The sort direction of the returned invoices. @default Direction.Desc */
    direction?: Direction;
    /** Include line items data. @default false */
    lineItems?: boolean;
    /** Include discounts data. @default false */
    discounts?: boolean;
    /** Include taxes data. @default false */
    taxes?: boolean;
    /** Include credits data. @default false */
    credits?: boolean;
    /** Include payments data. @default false */
    payments?: boolean;
    /** Include custom fields data. @default false */
    customFields?: boolean;
  };

  export type ListSubscriptionGroupProformaInvoicesRequest = {
    /** The uid of the subscription group */
    uid: string;
    /** Include line items data. @default false */
    lineItems?: boolean;
    /** Include discounts data. @default false */
    discounts?: boolean;
    /** Include taxes data. @default false */
    taxes?: boolean;
    /** Include credits data. @default false */
    credits?: boolean;
    /** Include payments data. @default false */
    payments?: boolean;
    /** Include custom fields data. @default false */
    customFields?: boolean;
  };

  export class ListSubscriptionGroupProformaInvoicesError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ListSubscriptionGroupProformaInvoicesError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type PreviewProformaInvoiceRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class PreviewProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<PreviewProformaInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type PreviewSignupProformaInvoiceRequest = {
    /**
     * Choose to include a proforma invoice preview for the first renewal. Use in query
     * `include=next_proforma_invoice`.
     */
    include?: CreateSignupProformaPreviewInclude;
    body?: CreateSubscriptionRequest;
  };

  export class PreviewSignupProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"proformaBadRequestErrorResponse1", ProformaBadRequestErrorResponse1>
      | Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>
    >;

    static readonly errors: ErrorDecoders<PreviewSignupProformaInvoiceError> = [
      {
        on: 400,
        kind: "proformaBadRequestErrorResponse1",
        decode: { kind: "json", schema: proformaBadRequestErrorResponse1Schema },
      },
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type ReadProformaInvoiceRequest = {
    /** The uid of the proforma invoice */
    proformaInvoiceUid: string;
  };

  export class ReadProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ReadProformaInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type VoidProformaInvoiceRequest = {
    /** The uid of the proforma invoice */
    proformaInvoiceUid: string;
    body?: VoidInvoiceRequest;
  };

  export class VoidProformaInvoiceError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<VoidProformaInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
