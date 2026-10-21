import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { invoiceSchema, type Invoice } from "../models/invoice.js";
import {
  issueAdvanceInvoiceRequestSchema,
  type IssueAdvanceInvoiceRequest,
} from "../models/issue-advance-invoice-request.js";
import { voidInvoiceRequestSchema, type VoidInvoiceRequest } from "../models/void-invoice-request.js";
import type { Servers } from "../servers.js";

/**
 * Use the Advance Invoice feature to issue, retrieve, or void an invoice for a subscription ahead
 * of its normal billing schedule, collecting an outstanding balance before the next scheduled
 * renewal. For more information, see [Issue Advance Invoices for Subscription
 * Renewals](https://docs.maxio.com/billing/invoicing/advance-invoices/issue-advance-invoices-for-subscription-renewals).
 */
export class AdvanceInvoice {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Issue advance invoice
   *
   * @remarks
   * Issues an invoice in advance for a subscription's next renewal date. For the most part, advance
   * invoices function like any other invoice, except they are issued early and have special
   * behavior upon being voided. For more information on advance invoices, including eligibility for
   * generating one, see [Issue Invoice In
   * Advance](https://maxio.zendesk.com/hc/en-us/articles/24252026404749-Issue-Invoice-In-Advance).
   *
   * A subscription can only have one advance invoice per billing period. Attempting to issue an
   * advance invoice when one already exists returns an error.
   *
   * Regeneration of the invoice can be forced with the params `force: true`, which voids an advance
   * invoice if one exists and generates a new one. If no advance invoice exists, a new one is
   * generated.
   *
   * Consider using either the create or preview endpoints for proforma invoices to preview this
   * advance invoice before using this endpoint to generate it.
   *
   * @returns Created
   *
   * @throws {@link AdvanceInvoice.IssueAdvanceInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  issueAdvanceInvoice(
    request: AdvanceInvoice.IssueAdvanceInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<Invoice, AdvanceInvoice.IssueAdvanceInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/advance_invoice/issue.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => issueAdvanceInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: AdvanceInvoice.IssueAdvanceInvoiceError,
      },
      options,
    );
  }

  /**
   * Read advance invoice
   *
   * @remarks
   * Returns the advance invoice generated for a subscription's upcoming renewal. There can only be
   * one advance invoice per subscription per billing cycle.
   *
   * @returns OK
   *
   * @throws {@link AdvanceInvoice.ReadAdvanceInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readAdvanceInvoice(
    request: AdvanceInvoice.ReadAdvanceInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<Invoice, AdvanceInvoice.ReadAdvanceInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/advance_invoice.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: AdvanceInvoice.ReadAdvanceInvoiceError,
      },
      options,
    );
  }

  /**
   * Void advance invoice
   *
   * @remarks
   * Voids a subscription's existing advance invoice. Once voided, it can later be regenerated if
   * desired.
   *
   * A `reason` is required to void, and the invoice must have an open status. Voiding causes any
   * prepayments and credits that were applied to the invoice to be returned to the subscription.
   *
   * For a full overview of the impact of voiding, see [Invoice]($m/Invoice).
   *
   * @returns Created
   *
   * @throws {@link AdvanceInvoice.VoidAdvanceInvoiceError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  voidAdvanceInvoice(
    request: AdvanceInvoice.VoidAdvanceInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<Invoice, AdvanceInvoice.VoidAdvanceInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/advance_invoice/void.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => voidInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: AdvanceInvoice.VoidAdvanceInvoiceError,
      },
      options,
    );
  }
}

export namespace AdvanceInvoice {
  export type IssueAdvanceInvoiceRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: IssueAdvanceInvoiceRequest;
  };

  export class IssueAdvanceInvoiceError extends ApiError {
    declare readonly payload:
      | Declared<"error404", undefined>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<IssueAdvanceInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadAdvanceInvoiceRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class ReadAdvanceInvoiceError extends ApiError {
    declare readonly payload: Declared<"error404", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<ReadAdvanceInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type VoidAdvanceInvoiceRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: VoidInvoiceRequest;
  };

  export class VoidAdvanceInvoiceError extends ApiError {
    declare readonly payload: Declared<"error404", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<VoidAdvanceInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }
}
