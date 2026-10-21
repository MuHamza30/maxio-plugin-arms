import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { basicDateFieldSchema, type BasicDateField } from "../models/basic-date-field.js";
import {
  createCustomerRequestSchema,
  type CreateCustomerRequest,
} from "../models/create-customer-request.js";
import {
  customerErrorResponse1Schema,
  type CustomerErrorResponse1,
} from "../models/customer-error-response1.js";
import { customerResponseSchema, type CustomerResponse } from "../models/customer-response.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import { subscriptionResponseSchema, type SubscriptionResponse } from "../models/subscription-response.js";
import {
  updateCustomerRequestSchema,
  type UpdateCustomerRequest,
} from "../models/update-customer-request.js";
import type { Servers } from "../servers.js";

export class Customers {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Customer
   *
   * @remarks
   * Creates a new customer; can also be created alongside a new subscription. The only validation
   * restriction is that you can only create one customer for a given reference value.
   *
   * If provided, the `reference` value must be unique. It represents a unique identifier for the
   * customer from your own app, i.e. the customer’s ID. This allows you to retrieve a given
   * customer via a piece of shared information. Alternatively, you can choose to leave `reference`
   * blank, and store the system-assigned unique ID for the customer, which is in the `id`
   * attribute.
   *
   * For more information, see [Customer
   * Details](https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details).
   *
   * ## Required Country Format
   *
   * Format the country attribute of the customer using the ISO Standard Country codes.
   *
   * Countries should be formatted as two characters. For more information, see [ISO
   * 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes).
   *
   * ## Required State Format
   *
   * Format the state attribute of the customer using the ISO Standard State codes.
   *
   * + US States (two characters): see [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:US).
   *
   * + States Outside the US (two to three characters): To find the correct state codes outside the
   *   US, go to [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) and click on
   *   the link in the “ISO 3166-2 codes” column next to the country you wish to populate.
   *
   * ## Locale
   *
   * You can attribute a language/region to the customer to deliver invoices in any required
   * language. For more information, see [Customer
   * Locale](https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale).
   *
   * ## Tax and Business Identifiers
   *
   * Send `entity_identifier_kind` and `entity_identifier_value` together to store the customer's
   * tax or business identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer
   * holds one identifier at a time.
   *
   * The `vat_eu` and `national_tax` kinds also require `vat_country`. An unsupported kind, a
   * missing or mismatched `vat_country`, or a `gln`, `duns`, or `lei` value in the wrong format
   * returns `422`.
   *
   * Always send the kind. `entity_identifier_value` on its own is stored as a `company_reg` when no
   * `vat_country` is present, and returns `422` naming `entity_identifier_kind` when one is.
   *
   * A blank pair is ignored rather than rejected, so a `vat_number` sent alongside it still takes
   * effect.
   *
   * The legacy `vat_number` and `vat_country` pair still works on its own. When neither entity
   * identifier field is sent, Advanced Billing derives the kind from `vat_country`: an EU member
   * state code or `GB` gives `vat_eu`, one of the national tax country codes gives `national_tax`,
   * and a blank or unrecognized country gives `company_reg`.
   *
   * The response reports the stored identifier in `entity_identifier_kind` and
   * `entity_identifier_value`, and repeats its value in `vat_number`.
   *
   * @returns OK
   *
   * @throws {@link Customers.CreateCustomerError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createCustomer(
    request: Customers.CreateCustomerRequestParams,
    options?: RequestOptions,
  ): ApiPromise<CustomerResponse, Customers.CreateCustomerError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/customers.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createCustomerRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: customerResponseSchema },
        errorFactory: Customers.CreateCustomerError,
      },
      options,
    );
  }

  /**
   * Delete Customer
   *
   * @remarks
   * Deletes the customer.
   *
   * @returns No Content
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteCustomer(
    request: Customers.DeleteCustomerRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/customers/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
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
   * List Customer Subscriptions
   *
   * @remarks
   * Lists all subscriptions that belong to a customer.
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, subscriptions no longer require an associated product. For subscriptions without an
   * associated product, 'product', 'product_price_point_id', and 'product_price_point_type' are
   * returned as 'null'.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listCustomerSubscriptions(
    request: Customers.ListCustomerSubscriptionsRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/customers/{customer_id}/subscriptions.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "customer_id", value: request.customerId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => subscriptionResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List or Find Customers
   *
   * @remarks
   * Lists all customers associated with your site, or filters results using the search parameter.
   *
   * ## Find Customer
   *
   * Use the search feature with the `q` query parameter to retrieve an array of customers that
   * matches the search query.
   *
   * Common use cases are:
   *
   * + Search by an email
   * + Search by an Advanced Billing ID
   * + Search by an organization
   * + Search by a reference value from your application
   * + Search by a first or last name
   *
   * To retrieve a single, exact match by reference, use the [lookup
   * endpoint](https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference).
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listCustomers(
    request: Customers.ListCustomersRequest,
    options?: RequestOptions,
  ): ApiPromise<CustomerResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/customers.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 50) },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => basicDateFieldSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
          { name: "q", value: request.q, schema: s.optional(s.string()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => customerResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Customer
   *
   * @remarks
   * Retrieves the Customer properties by Advanced Billing-generated Customer ID.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readCustomer(
    request: Customers.ReadCustomerRequest,
    options?: RequestOptions,
  ): ApiPromise<CustomerResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/customers/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: customerResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Customer by Reference
   *
   * @remarks
   * Returns a customer by their unique reference ID. It will return a single match.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readCustomerByReference(
    request: Customers.ReadCustomerByReferenceRequest,
    options?: RequestOptions,
  ): ApiPromise<CustomerResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/customers/lookup.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [{ name: "reference", value: request.reference, schema: s.string() }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: customerResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Customer
   *
   * @remarks
   * Updates the customer.
   *
   * ## Tax and Business Identifiers
   *
   * Send `entity_identifier_kind` and `entity_identifier_value` together to store the customer's
   * tax or business identifier, such as an EU VAT number, a French SIREN, or a LEI. A customer
   * holds one identifier at a time, so saving an identifier of a different kind replaces the
   * existing one.
   *
   * The `vat_eu` and `national_tax` kinds also require `vat_country`. An unsupported kind, a
   * missing or mismatched `vat_country`, or a `gln`, `duns`, or `lei` value in the wrong format
   * returns `422`.
   *
   * Always send the kind. `entity_identifier_value` on its own is stored as a `company_reg` when no
   * `vat_country` is present, and returns `422` naming `entity_identifier_kind` when one is.
   *
   * To clear an identifier, send a supported `entity_identifier_kind` with a blank
   * `entity_identifier_value`, or send a blank `vat_number` on its own. The first form also clears
   * `vat_number` and `vat_country`, and it removes whichever identifier the customer holds,
   * whatever kind you send with it.
   *
   * The legacy `vat_number` and `vat_country` pair still works on its own. When neither entity
   * identifier field is sent, Advanced Billing derives the kind from `vat_country`: an EU member
   * state code or `GB` gives `vat_eu`, one of the national tax country codes gives `national_tax`,
   * and a blank or unrecognized country gives `company_reg`.
   *
   * Sending a customer response straight back leaves the tax ID alone. A blank pair, and a pair
   * that still matches the stored identifier with `vat_country` unchanged, are read as nothing to
   * change rather than as a request to clear. For `gln`, `duns`, and `lei` that also covers the
   * `vat_number` the response mirrors back, so the kind survives the round trip.
   *
   * What you do change is applied, and the entity identifier fields take precedence over
   * `vat_number`. A different kind or value writes that identifier, and `vat_number` and
   * `vat_country` follow from it. A different `vat_country` next to an unchanged pair is a real
   * edit, so it is validated and can return `422`. Changing only `vat_number` leaves the pair
   * unchanged, so the derivation above decides the kind, which turns a `gln`, `duns`, or `lei`
   * customer into a `company_reg`. Setting `vat_number` to `null` or a blank string still clears
   * the identifier.
   *
   * The response reports the stored identifier in `entity_identifier_kind` and
   * `entity_identifier_value`, and repeats its value in `vat_number`.
   *
   * @returns OK
   *
   * @throws {@link Customers.UpdateCustomerError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateCustomer(
    request: Customers.UpdateCustomerRequestParams,
    options?: RequestOptions,
  ): ApiPromise<CustomerResponse, Customers.UpdateCustomerError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/customers/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateCustomerRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: customerResponseSchema },
        errorFactory: Customers.UpdateCustomerError,
      },
      options,
    );
  }
}

export namespace Customers {
  export type CreateCustomerRequestParams = {
    body?: CreateCustomerRequest;
  };

  export class CreateCustomerError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"customerErrorResponse1", CustomerErrorResponse1>>;

    static readonly errors: ErrorDecoders<CreateCustomerError> = [
      {
        on: 422,
        kind: "customerErrorResponse1",
        decode: { kind: "json", schema: customerErrorResponse1Schema },
      },
    ];
  }

  export type DeleteCustomerRequest = {
    /** The Advanced Billing id of the customer */
    id: number;
  };

  export type ListCustomerSubscriptionsRequest = {
    /** The Chargify id of the customer */
    customerId: number;
  };

  export type ListCustomersRequest = {
    /** Direction to sort customers by time of creation */
    direction?: SortingDirection;
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
     * This parameter indicates how many records to fetch in each request. Default value is 50. The
     * maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in
     * query `per_page=200`.
     *
     * @default 50
     */
    perPage?: number;
    /**
     * The type of filter you would like to apply to your search. Use in query:
     * `date_field=created_at`.
     */
    dateField?: BasicDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
     * with a timestamp up to and including 11:59:59PM in your site’s time zone on the date
     * specified.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns subscriptions with a timestamp at or after exact time provided in query. You can
     * specify timezone in query - otherwise your site's time zone will be used. If provided, this
     * parameter will be used instead of start_date.
     */
    startDatetime?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns subscriptions with a timestamp at or before exact time provided in query. You can
     * specify timezone in query - otherwise your site's time zone will be used. If provided, this
     * parameter will be used instead of end_date.
     */
    endDatetime?: string;
    /**
     * A search query by which to filter customers (can be an email, an ID, a reference,
     * organization)
     */
    q?: string;
  };

  export type ReadCustomerRequest = {
    /** The Advanced Billing id of the customer */
    id: number;
  };

  export type ReadCustomerByReferenceRequest = {
    /** Customer reference */
    reference: string;
  };

  export type UpdateCustomerRequestParams = {
    /** The Advanced Billing id of the customer */
    id: number;
    body?: UpdateCustomerRequest;
  };

  export class UpdateCustomerError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"customerErrorResponse1", CustomerErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<UpdateCustomerError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "customerErrorResponse1",
        decode: { kind: "json", schema: customerErrorResponse1Schema },
      },
    ];
  }
}
