import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { consolidatedInvoiceSchema, type ConsolidatedInvoice } from "../models/consolidated-invoice.js";
import {
  createInvoicePaymentRequestSchema,
  type CreateInvoicePaymentRequest,
} from "../models/create-invoice-payment-request.js";
import { createInvoiceRequestSchema, type CreateInvoiceRequest } from "../models/create-invoice-request.js";
import {
  createMultiInvoicePaymentRequestSchema,
  type CreateMultiInvoicePaymentRequest,
} from "../models/create-multi-invoice-payment-request.js";
import { CreditNoteDateField, creditNoteDateFieldSchema } from "../models/credit-note-date-field.js";
import { creditNoteSchema, type CreditNote } from "../models/credit-note.js";
import {
  customerChangesPreviewResponseSchema,
  type CustomerChangesPreviewResponse,
} from "../models/customer-changes-preview-response.js";
import { Direction, directionSchema } from "../models/direction.js";
import {
  errorArrayMapResponse1Schema,
  type ErrorArrayMapResponse1,
} from "../models/error-array-map-response1.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { InvoiceDateField, invoiceDateFieldSchema } from "../models/invoice-date-field.js";
import { invoiceEventTypeSchema, type InvoiceEventType } from "../models/invoice-event-type.js";
import { invoiceResponseSchema, type InvoiceResponse } from "../models/invoice-response.js";
import { InvoiceSortField, invoiceSortFieldSchema } from "../models/invoice-sort-field.js";
import { invoiceStatusSchema, type InvoiceStatus } from "../models/invoice-status.js";
import { invoiceSchema, type Invoice } from "../models/invoice.js";
import { issueInvoiceRequestSchema, type IssueInvoiceRequest } from "../models/issue-invoice-request.js";
import {
  listCreditNotesResponseSchema,
  type ListCreditNotesResponse,
} from "../models/list-credit-notes-response.js";
import {
  listInvoiceEventsResponseSchema,
  type ListInvoiceEventsResponse,
} from "../models/list-invoice-events-response.js";
import { listInvoicesResponseSchema, type ListInvoicesResponse } from "../models/list-invoices-response.js";
import {
  multiInvoicePaymentResponseSchema,
  type MultiInvoicePaymentResponse,
} from "../models/multi-invoice-payment-response.js";
import { recordPaymentRequestSchema, type RecordPaymentRequest } from "../models/record-payment-request.js";
import {
  recordPaymentResponseSchema,
  type RecordPaymentResponse,
} from "../models/record-payment-response.js";
import { refundInvoiceRequestSchema, type RefundInvoiceRequest } from "../models/refund-invoice-request.js";
import { sendInvoiceRequestSchema, type SendInvoiceRequest } from "../models/send-invoice-request.js";
import { updateInvoiceRequestSchema, type UpdateInvoiceRequest } from "../models/update-invoice-request.js";
import { voidInvoiceRequestSchema, type VoidInvoiceRequest } from "../models/void-invoice-request.js";
import type { Servers } from "../servers.js";

/**
 * The Invoice object is the billing document generated for a subscription, itemizing charges,
 * taxes, and payments, and tracking amounts owed.
 *
 * The role indicates what triggered the invoice (signup, renewal, usage, proration, etc.), and the
 * status and due_date reflect where an invoice stands in the payment lifecycle. For more
 * information, see [Get Started with
 * Invoicing](https://docs.maxio.com/billing/invoicing/overview/get-started-with-invoicing).
 */
export class Invoices {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Invoice
   *
   * @remarks
   * Creates an ad hoc invoice.
   *
   * ### Basic Behavior
   *
   * You can create a basic invoice by sending an array of line items to this endpoint. Each line
   * item, at a minimum, must include a title, a quantity and a unit price. Example:
   *
   * ```json
   * {
   *   "invoice": {
   *     "line_items": [
   *       {
   *         "title": "A Product",
   *         "quantity": 12,
   *         "unit_price": "150.00"
   *       }
   *     ]
   *   }
   * }
   * ```
   *
   * ### Catalog items
   * Instead of creating custom products like in above example, You can pass existing items like
   * products, components.
   *
   * ```json
   * {
   *   "invoice": {
   *     "line_items": [
   *       {
   *         "product_id": "handle:gold-product",
   *         "quantity": 2,
   *       }
   *     ]
   *   }
   * }
   * ```
   *
   *
   * The price for each line item will be calculated as well as a total due amount for the invoice.
   * Multiple line items can be sent.
   *
   * ### Line item types
   * When defining a line item, You can choose one of 3 types for a line item:
   * #### Custom item
   * As shown in the basic behavior example, You can pass `title` and `unit_price` for custom item.
   * #### Product id
   * Product handle (with handle: prefix) or id from the scope of current subscription's site can be
   * provided with `product_id`. By default `unit_price` is taken from product's default price
   * point, but can be overwritten by passing `unit_price` or `product_price_point_id`. If
   * `product_id` is used, following fields cannot be used: `title`, `component_id`.
   * #### Component id
   * Component handle (with handle: prefix) or id from the scope of current subscription's site can
   * be provided with `component_id`. If `component_id` is used, following fields cannot be used:
   * `title`, `product_id`. By default `unit_price` is taken from product's default price point, but
   * can be overwritten by passing `unit_price` or `price_point_id`. At this moment price points are
   * supported only for quantity based, on/off and metered components. For prepaid and event based
   * billing components `unit_price` is required.
   *
   * ### Coupons
   * When creating ad hoc invoice, new discounts can be applied in following way:
   *
   * ```json
   * {
   *   "invoice": {
   *     "line_items": [
   *       {
   *         "product_id": "handle:gold-product",
   *         "quantity": 1
   *       }
   *     ],
   *     "coupons": [
   *       {
   *         "code": "COUPONCODE",
   *         "percentage": 50.0
   *       }
   *     ]
   *   }
   * }
   * ```
   * If You want to use existing coupon for discount creation, only `code` and optional
   * `product_family_id` is needed
   *
   * ```json
   * ...
   *  "coupons": [
   *       {
   *         "code": "FREESETUP",
   *         "product_family_id": 1
   *       }
   *   ]
   * ...
   * ```
   *
   * #### Using Coupon Subcodes
   * You can also use coupon subcodes to apply existing coupons with specific subcodes:
   *
   * ```json
   * ...
   *  "coupons": [
   *       {
   *         "subcode": "SUB1",
   *         "product_family_id": 1
   *       }
   *   ]
   * ...
   * ```
   * **Important:** You cannot specify both `code` and `subcode` for the same coupon. Use either:
   * - `code` to apply a main coupon
   * - `subcode` to apply a specific coupon subcode
   *
   * The API response will include both the main coupon code and the subcode used:
   *
   * ```json
   * ...
   *  "coupons": [
   *       {
   *         "code": "MAIN123",
   *         "subcode": "SUB1",
   *         "product_family_id": 1,
   *         "percentage": 10,
   *         "description": "Special discount"
   *       }
   *   ]
   * ...
   * ```
   *
   * ### Coupon options
   * #### Code
   * Coupon `code` will be displayed on invoice discount section. Coupon code can only contain
   * uppercase letters, numbers, and allowed special characters. Lowercase letters will be converted
   * to uppercase. It can be used to select an existing coupon from the catalog, or as an ad hoc
   * coupon when passed with `percentage` or `amount`.
   * #### Subcode
   * Coupon `subcode` allows you to apply existing coupons using their subcodes. When a subcode is
   * used, the API response will include both the main coupon code and the specific subcode that was
   * applied. Subcodes are case-insensitive and will be converted to uppercase automatically.
   * #### Percentage
   * Coupon `percentage` can take values from 0 to 100 and up to 4 decimal places. It cannot be used
   * with `amount`. Only for ad hoc coupons, will be ignored if `code` is used to select an existing
   * coupon from the catalog.
   * #### Amount
   * Coupon `amount` takes number value. It cannot be used with `percentage`. Used only when not
   * matching existing coupon by `code`.
   * #### Description
   * Optional `description` will be displayed with coupon `code`. Used only when not matching
   * existing coupon by `code`.
   * #### Product Family id
   * Optional `product_family_id` handle (with handle: prefix) or id is used to match existing
   * coupon within site, when codes are not unique.
   * #### Compounding Strategy
   * Optional `compounding_strategy` for percentage coupons, can take values `compound` or
   * `full-price`.
   *
   * For amount coupons, discounts will be always calculated against the original item price, before
   * other discounts are applied.
   *
   * `compound` strategy: Percentage-based discounts will be calculated against the remaining price,
   * after prior discounts have been calculated. It is set by default.
   *
   * `full-price` strategy: Percentage-based discounts will always be calculated against the
   * original item price, before other discounts are applied.
   *
   * ### Line Item Options
   *
   * #### Period Date Range
   *
   * A custom period date range can be defined for each line item with the `period_range_start` and
   * `period_range_end` parameters. Dates must be sent in the `YYYY-MM-DD` format.
   * `period_range_end` must be greater or equal `period_range_start`.
   *
   * #### Taxes
   *
   * The `taxable` parameter can be sent as `true` if taxes should be calculated for a specific line
   * item. For this to work, the site should be configured to use and calculate taxes. Further, if
   * the site uses Avalara for tax calculations, a `tax_code` parameter should also be sent. For
   * existing catalog items: products/components taxes cannot be overwritten.
   *
   * #### Price Point
   * Price point handle (with handle: prefix) or id from the scope of current subscription's site
   * can be provided with `price_point_id` for components with `component_id` or
   * `product_price_point_id` for products with `product_id` parameter. If price point is passed
   * `unit_price` cannot be used. It can be used only with catalog items products and components.
   *
   * #### Description
   * Optional `description` parameter, it will overwrite default generated description for line
   * item.
   *
   * ### Invoice Options
   *
   * #### Issue Date
   *
   * By default, invoices will be created with a issue date set to today in your site's time zone.
   * The `issue_date` parameter can be sent to alter the default. Only today or dates in the past
   * are accepted. This date is interpreted and validated in your site's time zone. The format for
   * `issue_date` is `YYYY-MM-DD`.
   *
   * #### Net Terms
   *
   * By default, invoices will be created with a due date matching the date of invoice creation. If
   * a different due date is desired, the `net_terms` parameter can be sent indicating the number of
   * days in advance the due date should be.
   *
   * #### Addresses
   *
   * The seller, shipping and billing addresses can be sent to override the site's defaults. Each
   * address requires to send a `first_name` at a minimum in order to work. See below for the
   * details on which parameters can be sent for each address object.
   *
   * #### Memo and Payment Instructions
   *
   * A custom memo can be sent with the `memo` parameter to override the site's default. Likewise,
   * custom payment instructions can be sent with the `payment_instructions` parameter.
   *
   * #### Status
   *
   * By default, invoices will be created with open status. Possible alternative is `draft`.
   *
   * @returns OK
   *
   * @throws {@link Invoices.CreateInvoiceError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createInvoice(
    request: Invoices.CreateInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<InvoiceResponse, Invoices.CreateInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: invoiceResponseSchema },
        errorFactory: Invoices.CreateInvoiceError,
      },
      options,
    );
  }

  /**
   * Delete Draft Ad Hoc Invoice
   *
   * @remarks
   * Deletes an ad hoc invoice while it is in the `draft` state.
   *
   * **Important: only invoices with the `adhoc` role and `draft` status can be deleted.** Any other
   * invoice — issued, or with a different role (e.g. `renewal`, `signup`) — cannot be deleted
   * through this endpoint and the request returns a `422` error. Issued invoices should be voided
   * instead. If the invoice does not belong to the provided subscription, a `404` error is
   * returned.
   *
   * A successful deletion returns a `204 No Content` response and the invoice is permanently
   * removed.
   *
   * @returns No Content
   *
   * @throws {@link Invoices.DeleteInvoiceError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteInvoice(
    request: Invoices.DeleteInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, Invoices.DeleteInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/invoices/{uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "uid", value: request.uid, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: Invoices.DeleteInvoiceError,
      },
      options,
    );
  }

  /**
   * Issue Invoice
   *
   * @remarks
   * Issues an invoice that is in "pending" or "draft" status. For example, you can issue an invoice
   * that was created when allocating new quantity on a component and using "accrue charges" option.
   *
   * You cannot issue a pending child invoice that was created for a member subscription in a group.
   *
   * For Remittance subscriptions, the invoice will go into "open" status and payment won't be
   * attempted. The value for `on_failed_payment` would be rejected if sent. Any prepayments or
   * service credits that exist on the subscription will be automatically applied. Additionally, if
   * the setting is enabled, an email will be sent for the issued invoice.
   *
   * For Automatic subscriptions, prepayments and service credits will apply to the invoice before
   * payment is attempted. On successful payment, the invoice will go into "paid" status and email
   * will be sent to the customer (if setting applies). When payment fails, the next event depends
   * on the `on_failed_payment` value:
   * - `leave_open_invoice` - prepayments and credits applied to invoice; invoice status set to
   *   "open"; email sent to the customer for the issued invoice (if setting applies); payment
   *   failure recorded in the invoice history. This is the default option.
   * - `rollback_to_pending` - prepayments and credits not applied; invoice remains in "pending"
   *   status; no email sent to the customer; payment failure recorded in the invoice history.
   * - `initiate_dunning` - prepayments and credits applied to the invoice; invoice status set to
   *   "open"; email sent to the customer for the issued invoice (if setting applies); payment
   *   failure recorded in the invoice history; subscription will most likely go into "past_due" or
   *   "canceled" state (depending upon net terms and dunning settings).
   *
   * @returns OK
   *
   * @throws {@link Invoices.IssueInvoiceError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  issueInvoice(
    request: Invoices.IssueInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<Invoice, Invoices.IssueInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/{uid}/issue.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => issueInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: Invoices.IssueInvoiceError,
      },
      options,
    );
  }

  /**
   * List Segments for Consolidated Invoice
   *
   * @remarks
   * Lists segments for a consolidated invoice. Invoice segments returned on the index will only
   * include totals, not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`,
   * `payments`, or `custom_fields`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listConsolidatedInvoiceSegments(
    request: Invoices.ListConsolidatedInvoiceSegmentsRequest,
    options?: RequestOptions,
  ): ApiPromise<ConsolidatedInvoice, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/invoices/{invoice_uid}/segments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "invoice_uid", value: request.invoiceUid, schema: s.string() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "direction",
            value: request.direction,
            schema: s.defaulted(directionSchema, Direction.Asc),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: consolidatedInvoiceSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Credit Notes
   *
   * @remarks
   * Lists credit notes for a site. Credit Notes are like inverse invoices. They reduce the amount a
   * customer owes.
   *
   * By default, the credit notes returned by this endpoint will exclude the arrays of `line_items`,
   * `discounts`, `taxes`, `applications`, or `refunds`. To include these arrays, pass the specific
   * field as a key in the query with a value set to `true`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listCreditNotes(
    request: Invoices.ListCreditNotesRequest,
    options?: RequestOptions,
  ): ApiPromise<ListCreditNotesResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/credit_notes.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.optional(s.int()) },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.defaulted(creditNoteDateFieldSchema, CreditNoteDateField.IssueDate),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
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
          { name: "refunds", value: request.refunds, schema: s.defaulted(s.boolean(), false) },
          { name: "applications", value: request.applications, schema: s.defaulted(s.boolean(), false) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listCreditNotesResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Invoice Events
   *
   * @remarks
   * Lists invoice events for a site. Each event contains event "data" (such as an applied payment)
   * as well as a snapshot of the `invoice` at the time of event completion.
   *
   * Exposed event types are:
   *
   * + issue_invoice
   * + apply_credit_note
   * + apply_payment
   * + refund_invoice
   * + void_invoice
   * + void_remainder
   * + backport_invoice
   * + change_invoice_status
   * + change_invoice_collection_method
   * + remove_payment
   * + failed_payment
   * + apply_debit_note
   * + create_debit_note
   * + change_chargeback_status
   *
   * Invoice events are returned in ascending order.
   *
   * If both a `since_date` and `since_id` are provided in request parameters, the `since_date` will
   * be used.
   *
   * Note - invoice events that occurred prior to 09/05/2018 __will not__ contain an `invoice`
   * snapshot.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listInvoiceEvents(
    request: Invoices.ListInvoiceEventsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListInvoiceEventsResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/invoices/events.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "since_date", value: request.sinceDate, schema: s.optional(s.string()) },
          { name: "since_id", value: request.sinceId, schema: s.optional(s.int()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 100) },
          { name: "invoice_uid", value: request.invoiceUid, schema: s.optional(s.string()) },
          {
            name: "with_change_invoice_status",
            value: request.withChangeInvoiceStatus,
            schema: s.optional(s.string()),
          },
          {
            name: "event_types",
            value: request.eventTypes,
            schema: s.optional(s.array(s.lazy(() => invoiceEventTypeSchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listInvoiceEventsResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Invoices
   *
   * @remarks
   * Lists invoices for a site. By default, invoices returned on the index will only include totals,
   * not detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`, `payments`,
   * `custom_fields`, or `refunds`. To include breakdowns, pass the specific field as a key in the
   * query with a value set to `true`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listInvoices(
    request: Invoices.ListInvoicesRequest,
    options?: RequestOptions,
  ): ApiPromise<ListInvoicesResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/invoices.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "status", value: request.status, schema: s.optional(s.lazy(() => invoiceStatusSchema)) },
          { name: "subscription_id", value: request.subscriptionId, schema: s.optional(s.int()) },
          {
            name: "subscription_group_uid",
            value: request.subscriptionGroupUid,
            schema: s.optional(s.string()),
          },
          { name: "consolidation_level", value: request.consolidationLevel, schema: s.optional(s.string()) },
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
          { name: "refunds", value: request.refunds, schema: s.defaulted(s.boolean(), false) },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.defaulted(invoiceDateFieldSchema, InvoiceDateField.DueDate),
          },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
          { name: "customer_ids", value: request.customerIds, schema: s.optional(s.array(s.int())) },
          { name: "number", value: request.number, schema: s.optional(s.array(s.string())) },
          { name: "product_ids", value: request.productIds, schema: s.optional(s.array(s.int())) },
          {
            name: "sort",
            value: request.sort,
            schema: s.defaulted(invoiceSortFieldSchema, InvoiceSortField.Number),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listInvoicesResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Preview Customer Information Changes
   *
   * @remarks
   * Previews the effect of customer information changes on an open invoice. Customer information
   * may change after an invoice is issued, which may lead to a mismatch between customer
   * information that is present on an open invoice and actual customer information. This endpoint
   * allows you to preview these differences, if any.
   *
   * The endpoint doesn't accept a request body. Customer information differences are calculated on
   * the application side.
   *
   * @returns OK
   *
   * @throws {@link Invoices.PreviewCustomerInformationChangesError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewCustomerInformationChanges(
    request: Invoices.PreviewCustomerInformationChangesRequest,
    options?: RequestOptions,
  ): ApiPromise<CustomerChangesPreviewResponse, Invoices.PreviewCustomerInformationChangesError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/{uid}/customer_information/preview.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: customerChangesPreviewResponseSchema },
        errorFactory: Invoices.PreviewCustomerInformationChangesError,
      },
      options,
    );
  }

  /**
   * Read Credit Note
   *
   * @remarks
   * Returns the details for a credit note.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readCreditNote(
    request: Invoices.ReadCreditNoteRequest,
    options?: RequestOptions,
  ): ApiPromise<CreditNote, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/credit_notes/{uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: creditNoteSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Invoice
   *
   * @remarks
   * Returns the details for an invoice.
   *
   * ## PDF Invoice retrieval
   *
   * Individual PDF Invoices can be retrieved by using the "Accept" header application/pdf or
   * appending .pdf as the format portion of the URL:
   * ```curl -u <api_key>:x -H
   * Accept:application/pdf -H
   * https://acme.chargify.com/invoices/inv_8gd8tdhtd3hgr.pdf > output_file.pdf
   * URL: `https://<subdomain>.chargify.com/invoices/<uid>.<format>`
   * Method: GET
   * Required parameters: `uid`
   * Response: A single Invoice.
   * ```
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readInvoice(request: Invoices.ReadInvoiceRequest, options?: RequestOptions): ApiPromise<Invoice, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/invoices/{uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Record Payment for Invoice
   *
   * @remarks
   * Applies a payment of a given type against a specific invoice. If you would like to apply a
   * payment across multiple invoices, you can use the [Record Payment for Multiple
   * Invoices]($e/Invoices/recordPaymentForMultipleInvoices) endpoint.
   *
   * @returns OK
   *
   * @throws {@link Invoices.RecordPaymentForInvoiceError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  recordPaymentForInvoice(
    request: Invoices.RecordPaymentForInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<Invoice, Invoices.RecordPaymentForInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/{uid}/payments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createInvoicePaymentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: Invoices.RecordPaymentForInvoiceError,
      },
      options,
    );
  }

  /**
   * Record Payment for Multiple Invoices
   *
   * @remarks
   * Records an external payment against multiple invoices.
   *
   * To apply a payment to multiple invoices, at minimum, specify the `amount` and `applications`
   * (i.e., `invoice_uid` and `amount`) details.
   *
   * Note that the invoice payment amounts must be greater than 0. Total amount must be greater or
   * equal to invoices payment amount sum.
   *
   * @returns OK
   *
   * @throws {@link Invoices.RecordPaymentForMultipleInvoicesError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  recordPaymentForMultipleInvoices(
    request: Invoices.RecordPaymentForMultipleInvoicesRequest,
    options?: RequestOptions,
  ): ApiPromise<MultiInvoicePaymentResponse, Invoices.RecordPaymentForMultipleInvoicesError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/payments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createMultiInvoicePaymentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: multiInvoicePaymentResponseSchema },
        errorFactory: Invoices.RecordPaymentForMultipleInvoicesError,
      },
      options,
    );
  }

  /**
   * Record Payment For Subscription
   *
   * @remarks
   * Records an external payment made against a subscription that will pay partially or in full one
   * or more invoices.
   *
   * Payment will be applied starting with the oldest open invoice and then next oldest, and so on
   * until the amount of the payment is fully consumed.
   *
   * Excess payment will result in the creation of a prepayment on the Invoice Account.
   *
   * Only ungrouped or primary subscriptions may be paid using the "bulk" payment request.
   *
   * @returns OK
   *
   * @throws {@link Invoices.RecordPaymentForSubscriptionError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  recordPaymentForSubscription(
    request: Invoices.RecordPaymentForSubscriptionRequest,
    options?: RequestOptions,
  ): ApiPromise<RecordPaymentResponse, Invoices.RecordPaymentForSubscriptionError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/payments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => recordPaymentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: recordPaymentResponseSchema },
        errorFactory: Invoices.RecordPaymentForSubscriptionError,
      },
      options,
    );
  }

  /**
   * Refund Invoice
   *
   * @remarks
   * Refunds an invoice, segment, or consolidated invoice.
   *
   * ## Partial Refund for Consolidated Invoice
   *
   * A refund less than the total of a consolidated invoice will be split across its segments.
   *
   * For a $50.00 refund on a $100.00 consolidated invoice with one $60.00 segment and one $40.00
   * segment, the refunded amount will be applied as 50% of each ($30.00 and $20.00, respectively).
   *
   * @returns OK
   *
   * @throws {@link Invoices.RefundInvoiceError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  refundInvoice(
    request: Invoices.RefundInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<Invoice, Invoices.RefundInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/{uid}/refunds.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => refundInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: Invoices.RefundInvoiceError,
      },
      options,
    );
  }

  /**
   * Reopen Invoice
   *
   * @remarks
   * Reopens any invoice with the "canceled" status. Invoices enter "canceled" status if they were
   * open at the time the subscription was canceled (whether through dunning or an intentional
   * cancellation).
   *
   * Invoices with "canceled" status are no longer considered to be due. Once reopened, they are
   * considered due for payment. Payment may then be captured in one of the following ways:
   *
   * - Reactivating the subscription, which will capture all open invoices (See note below about
   *   automatic reopening of invoices.)
   * - Recording a payment directly against the invoice
   *
   * A note about reactivations: any canceled invoices from the most recent active period are
   * automatically opened as a part of the reactivation process. Reactivating via this endpoint
   * prior to reactivation is only necessary when you wish to capture older invoices from previous
   * periods during the reactivation.
   *
   * ### Reopening Consolidated Invoices
   *
   * When reopening a consolidated invoice, all of its canceled segments will also be reopened.
   *
   * @returns OK
   *
   * @throws {@link Invoices.ReopenInvoiceError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  reopenInvoice(
    request: Invoices.ReopenInvoiceRequest,
    options?: RequestOptions,
  ): ApiPromise<Invoice, Invoices.ReopenInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/{uid}/reopen.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: Invoices.ReopenInvoiceError,
      },
      options,
    );
  }

  /**
   * Send Invoice
   *
   * @remarks
   * Sends an invoice to the customer via email. This endpoint supports the delivery of both ad-hoc
   * and automatically generated invoices. Additionally, this endpoint supports email delivery to
   * direct recipients, carbon-copy (cc) recipients, and blind carbon-copy (bcc) recipients.
   *
   * **File Attachments**: You can attach files to invoice emails using `attachment_urls[]`
   * parameter by providing URLs to the files you want to attach. When using attachments, the
   * request must use `multipart/form-data` content type. Max 10 files, 10MB per file.
   *
   * If no recipient email addresses are specified in the request, then the subscription's default
   * email configuration will be used. For example, if `recipient_emails` is left blank, then the
   * invoice will be delivered to the subscription's customer email address.
   *
   * On success, a 204 no-content response will be returned. The response does not indicate that
   * email(s) have been delivered, but instead indicates that emails have been successfully queued
   * for delivery. If _any_ invalid or malformed email address is found in the request body, the
   * entire request will be rejected and a 422 response will be returned.
   *
   * @returns No Content
   *
   * @throws {@link Invoices.SendInvoiceError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  sendInvoice(
    request: Invoices.SendInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<undefined, Invoices.SendInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/{uid}/deliveries.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => sendInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: Invoices.SendInvoiceError,
      },
      options,
    );
  }

  /**
   * Update Customer Information
   *
   * @remarks
   * Updates customer information on an open invoice and returns the updated invoice. If you would
   * like to preview changes that will be applied, use the
   * `/invoices/{uid}/customer_information/preview.json` endpoint first.
   *
   * The endpoint doesn't accept a request body. Customer information differences are calculated on
   * the application side.
   *
   * @returns OK
   *
   * @throws {@link Invoices.UpdateCustomerInformationError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateCustomerInformation(
    request: Invoices.UpdateCustomerInformationRequest,
    options?: RequestOptions,
  ): ApiPromise<Invoice, Invoices.UpdateCustomerInformationError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/invoices/{uid}/customer_information.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: invoiceSchema },
        errorFactory: Invoices.UpdateCustomerInformationError,
      },
      options,
    );
  }

  /**
   * Update Draft Ad Hoc Invoice
   *
   * @remarks
   * Updates an ad hoc invoice while it is in the `draft` state.
   *
   * **Important: only invoices with the `adhoc` role and `draft` status can be updated.** Any other
   * invoice — issued, or with a different role (e.g. `renewal`, `signup`) — cannot be updated
   * through this endpoint and the request returns a `422` error. If the invoice does not belong to
   * the provided subscription, a `404` error is returned.
   *
   * Only the attributes submitted in the request are changed — omitted attributes keep their
   * current values.
   *
   * ### Line Items
   *
   * The `line_items` array describes changes to the invoice's line items. Line items not referenced
   * in the array remain unchanged.
   *
   * #### Adding a line item
   *
   * A line item without a `uid` is added to the invoice. The same line item types and options as on
   * invoice creation are supported (custom items, `product_id`, `component_id`, price points,
   * period date ranges, taxes).
   *
   * #### Updating a line item
   *
   * A line item with the `uid` of an existing line item updates that line item with the submitted
   * attributes. Amounts and taxes are recalculated.
   *
   * #### Removing a line item
   *
   * A line item with a `uid` and `"_destroy": true` is removed from the invoice. Other line items
   * remain unchanged.
   *
   * Referencing a `uid` which does not exist on the invoice returns a `422` error.
   *
   * ### Coupons
   *
   * When the `coupons` key is present, the submitted coupons replace all discounts currently
   * applied to the invoice. Send an empty array to remove all discounts. Coupon options are the
   * same as on invoice creation.
   *
   * ### Invoice Options
   *
   * #### Issue Date and Net Terms
   *
   * The `issue_date` parameter can be sent to change the invoice's issue date. Only today or dates
   * in the past are accepted. The date is interpreted and validated in your site's time zone, using
   * the `YYYY-MM-DD` format. The `net_terms` parameter indicates the number of days after the issue
   * date on which the invoice is due. The due date is recalculated whenever the issue date or net
   * terms change.
   *
   * #### Addresses
   *
   * The seller, shipping and billing addresses can be sent to replace the addresses on the invoice.
   * Each address requires to send a `first_name` at a minimum in order to work. Taxes are
   * recalculated after an address change.
   *
   * #### Memo and Payment Instructions
   *
   * A custom memo can be sent with the `memo` parameter. Likewise, custom payment instructions can
   * be sent with the `payment_instructions` parameter.
   *
   * @returns OK
   *
   * @throws {@link Invoices.UpdateInvoiceError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateInvoice(
    request: Invoices.UpdateInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<InvoiceResponse, Invoices.UpdateInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/invoices/{uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "uid", value: request.uid, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateInvoiceRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: invoiceResponseSchema },
        errorFactory: Invoices.UpdateInvoiceError,
      },
      options,
    );
  }

  /**
   * Void Invoice
   *
   * @remarks
   * Voids any invoice with the "open" or "canceled" status. It will also allow voiding of an
   * invoice with the "pending" status if it is not a consolidated invoice.
   *
   * @returns OK
   *
   * @throws {@link Invoices.VoidInvoiceError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  voidInvoice(
    request: Invoices.VoidInvoiceRequestParams,
    options?: RequestOptions,
  ): ApiPromise<Invoice, Invoices.VoidInvoiceError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/invoices/{uid}/void.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
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
        errorFactory: Invoices.VoidInvoiceError,
      },
      options,
    );
  }
}

export namespace Invoices {
  export type CreateInvoiceRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: CreateInvoiceRequest;
  };

  export class CreateInvoiceError extends ApiError {
    declare readonly payload: Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateInvoiceError> = [
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type DeleteInvoiceRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
  };

  export class DeleteInvoiceError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"errorListResponse12", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<DeleteInvoiceError> = [
      { on: 404, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type IssueInvoiceRequestParams = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
    body?: IssueInvoiceRequest;
  };

  export class IssueInvoiceError extends ApiError {
    declare readonly payload:
      | Declared<"error404", undefined>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<IssueInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListConsolidatedInvoiceSegmentsRequest = {
    /** The unique identifier of the consolidated invoice */
    invoiceUid: string;
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
    /** Sort direction of the returned segments. @default Direction.Asc */
    direction?: Direction;
  };

  export type ListCreditNotesRequest = {
    /** The subscription's Advanced Billing id */
    subscriptionId?: number;
    /**
     * The type of filter you would like to apply to your search. Use in query
     * `date_field=issue_date`. If a date range is provided without an explicit `date_field`, it
     * defaults to `issue_date`. If only `start_datetime`/`end_datetime` are provided without an
     * explicit `date_field`, it defaults to `created_at` instead. An unrecognized `date_field` is
     * ignored rather than raising an error.
     *
     * @default CreditNoteDateField.IssueDate
     */
    dateField?: CreditNoteDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns credit notes
     * with a timestamp up to and including 11:59:59PM in your site’s time zone on the date
     * specified.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns credit notes with a timestamp at or after exact time provided in query. If provided,
     * this parameter will be used instead of start_date. If no timezone offset is included in the
     * value, it is interpreted as UTC. Allowed to be used only along with date_field set to
     * created_at or updated_at.
     */
    startDatetime?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns credit notes with a timestamp at or before exact time provided in query. If provided,
     * this parameter will be used instead of end_date. If no timezone offset is included in the
     * value, it is interpreted as UTC. Allowed to be used only along with date_field set to
     * created_at or updated_at.
     */
    endDatetime?: string;
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
     * The sort direction of the returned credit notes, sorted by sequence_number.
     *
     * @default Direction.Desc
     */
    direction?: Direction;
    /** Include line items data. @default false */
    lineItems?: boolean;
    /** Include discounts data. @default false */
    discounts?: boolean;
    /** Include taxes data. @default false */
    taxes?: boolean;
    /** Include refunds data. @default false */
    refunds?: boolean;
    /** Include applications data. @default false */
    applications?: boolean;
  };

  export type ListInvoiceEventsRequest = {
    /**
     * The timestamp in a format `YYYY-MM-DD T HH:MM:SS Z`, or `YYYY-MM-DD`(in this case, it returns
     * data from the beginning of the day). of the event from which you want to start the search.
     * All the events before the `since_date` timestamp are not returned in the response.
     */
    sinceDate?: string;
    /**
     * The ID of the event from which you want to start the search(ID is not included. e.g. if ID is
     * set to 2, then all events with ID 3 and more will be shown) This parameter is not used if
     * since_date is defined.
     */
    sinceId?: number;
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
     * This parameter indicates how many records to fetch in each request. Default value is 100. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200.
     *
     * @default 100
     */
    perPage?: number;
    /**
     * Providing an invoice_uid allows for scoping of the invoice events to a single invoice or
     * credit note.
     */
    invoiceUid?: string;
    /**
     * Use this parameter if you want to fetch also invoice events with change_invoice_status type.
     */
    withChangeInvoiceStatus?: string;
    /**
     * Filter results by event_type. Supply a comma separated list of event types (listed above).
     * Use in query: `event_types=void_invoice,void_remainder`.
     */
    eventTypes?: InvoiceEventType[];
  };

  export type ListInvoicesRequest = {
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with
     * a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns invoices with a
     * timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /** The current status of the invoice. Allowed Values: draft, open, paid, pending, voided */
    status?: InvoiceStatus;
    /** The subscription's ID. */
    subscriptionId?: number;
    /**
     * The UID of the subscription group you want to fetch consolidated invoices for. This will
     * return a paginated list of consolidated invoices for the specified group.
     */
    subscriptionGroupUid?: string;
    /**
     * The consolidation level of the invoice. Allowed Values: none, parent, child or
     * comma-separated lists of thereof, e.g. none,parent.
     */
    consolidationLevel?: string;
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
    /** Include refunds data. @default false */
    refunds?: boolean;
    /**
     * The type of filter you would like to apply to your search. Use in query
     * `date_field=issue_date`.
     *
     * @default InvoiceDateField.DueDate
     */
    dateField?: InvoiceDateField;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns invoices with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of start_date. Allowed to be used only along with date_field set to
     * created_at or updated_at.
     */
    startDatetime?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns invoices with a timestamp at or before exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of end_date. Allowed to be used only along with date_field set to
     * created_at or updated_at.
     */
    endDatetime?: string;
    /**
     * Allows fetching invoices with matching customer id based on provided values. Use in query
     * `customer_ids=1,2,3`.
     */
    customerIds?: number[];
    /**
     * Allows fetching invoices with matching invoice number based on provided values. Use in query
     * `number=1234,1235`.
     */
    number?: string[];
    /**
     * Allows fetching invoices with matching line items product ids based on provided values. Use
     * in query `product_ids=23,34`.
     */
    productIds?: number[];
    /**
     * Allows specification of the order of the returned list. Use in query `sort=total_amount`.
     *
     * @default InvoiceSortField.Number
     */
    sort?: InvoiceSortField;
  };

  export type PreviewCustomerInformationChangesRequest = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
  };

  export class PreviewCustomerInformationChangesError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"errorListResponse12", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<PreviewCustomerInformationChangesError> = [
      { on: 404, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadCreditNoteRequest = {
    /** The unique identifier of the credit note */
    uid: string;
  };

  export type ReadInvoiceRequest = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
  };

  export type RecordPaymentForInvoiceRequest = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
    body?: CreateInvoicePaymentRequest;
  };

  export class RecordPaymentForInvoiceError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<RecordPaymentForInvoiceError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type RecordPaymentForMultipleInvoicesRequest = {
    body?: CreateMultiInvoicePaymentRequest;
  };

  export class RecordPaymentForMultipleInvoicesError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<RecordPaymentForMultipleInvoicesError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type RecordPaymentForSubscriptionRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: RecordPaymentRequest;
  };

  export class RecordPaymentForSubscriptionError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<RecordPaymentForSubscriptionError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type RefundInvoiceRequestParams = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
    body?: RefundInvoiceRequest;
  };

  export class RefundInvoiceError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<RefundInvoiceError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReopenInvoiceRequest = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
  };

  export class ReopenInvoiceError extends ApiError {
    declare readonly payload:
      | Declared<"error404", unknown>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ReopenInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "json", schema: s.unknown() } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type SendInvoiceRequestParams = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
    body?: SendInvoiceRequest;
  };

  export class SendInvoiceError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<SendInvoiceError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateCustomerInformationRequest = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
  };

  export class UpdateCustomerInformationError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"errorListResponse12", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateCustomerInformationError> = [
      { on: 404, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 422, kind: "errorListResponse12", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateInvoiceRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
    body?: UpdateInvoiceRequest;
  };

  export class UpdateInvoiceError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"errorArrayMapResponse1", ErrorArrayMapResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateInvoiceError> = [
      { on: 404, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      {
        on: 422,
        kind: "errorArrayMapResponse1",
        decode: { kind: "json", schema: errorArrayMapResponse1Schema },
      },
    ];
  }

  export type VoidInvoiceRequestParams = {
    /**
     * The unique identifier for the invoice, this does not refer to the public facing invoice
     * number.
     */
    uid: string;
    body?: VoidInvoiceRequest;
  };

  export class VoidInvoiceError extends ApiError {
    declare readonly payload:
      | Declared<"error404", unknown>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<VoidInvoiceError> = [
      { on: 404, kind: "error404", decode: { kind: "json", schema: s.unknown() } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
