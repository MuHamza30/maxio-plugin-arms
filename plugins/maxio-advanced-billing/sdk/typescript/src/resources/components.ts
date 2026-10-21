import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { basicDateFieldSchema, type BasicDateField } from "../models/basic-date-field.js";
import { componentResponseSchema, type ComponentResponse } from "../models/component-response.js";
import { componentSchema, type Component } from "../models/component.js";
import { createEbbComponentSchema, type CreateEbbComponent } from "../models/create-ebb-component.js";
import {
  createMeteredComponentSchema,
  type CreateMeteredComponent,
} from "../models/create-metered-component.js";
import { createOnOffComponentSchema, type CreateOnOffComponent } from "../models/create-on-off-component.js";
import {
  createPrepaidComponentSchema,
  type CreatePrepaidComponent,
} from "../models/create-prepaid-component.js";
import {
  createQuantityBasedComponentSchema,
  type CreateQuantityBasedComponent,
} from "../models/create-quantity-based-component.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { listComponentsFilterSchema, type ListComponentsFilter } from "../models/list-components-filter.js";
import {
  updateComponentRequestSchema,
  type UpdateComponentRequest,
} from "../models/update-component-request.js";
import type { Servers } from "../servers.js";

export class Components {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Component
   *
   * @remarks
   * Archives the component; all current subscribers will continue to be charged as usual.
   *
   * @returns OK
   *
   * @throws {@link Components.ArchiveComponentError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveComponent(
    request: Components.ArchiveComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<Component, Components.ArchiveComponentError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/components/{component_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentSchema },
        errorFactory: Components.ArchiveComponentError,
      },
      options,
    );
  }

  /**
   * Create Event Based Component
   *
   * @remarks
   * Creates an event-based component definition under the specified product family. An event-based
   * component can then be added and “allocated” for a subscription.
   *
   * Event-based components are similar to other component types, in that you define the component
   * parameters (such as name and taxability) and the pricing. A key difference for the event-based
   * component is that it must be attached to a metric. This is because the metric provides the
   * component with the actual quantity used in computing what and how much will be billed each
   * period for each subscription.
   *
   * So, instead of reporting usage directly for each component (as you would with metered
   * components), the usage is derived from analysis of your events.
   *
   * For more information, see [Components
   * Overview](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, taxable components must include a non-blank `tax_code`; sending a blank value results
   * in a validation error.
   *
   * @returns Created
   *
   * @throws {@link Components.CreateEventBasedComponentError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createEventBasedComponent(
    request: Components.CreateEventBasedComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, Components.CreateEventBasedComponentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/event_based_components.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createEbbComponentSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: Components.CreateEventBasedComponentError,
      },
      options,
    );
  }

  /**
   * Create Metered Component
   *
   * @remarks
   * Creates a metered component definition under the specified product family. A metered component
   * can then be added and “allocated” for a subscription.
   *
   * Metered components are used to bill for any type of unit that resets to 0 at the end of the
   * billing period (think daily Google Ads clicks or monthly cell phone minutes). This is most
   * commonly associated with usage-based billing and many other pricing schemes.
   *
   * Note that this is different from recurring quantity-based components, which DO NOT reset to
   * zero at the start of every billing period. If you want to bill for a quantity of something that
   * does not change unless you change it, then you want quantity components, instead.
   *
   * #### Hybrid Pricing
   * A `volume`, `tiered`, or `stairstep` metered component can combine its primary pricing with a
   * secondary pricing model (the `overage_pricing` parameter) so both bill as a single invoice line
   * item instead of two. This does not apply to metered components configured for event-based
   * billing (metric, meter, or formula). See [Hybrid
   * Pricing](page:introduction/basic-concepts/hybrid-pricing) for requirements and configuration
   * details.
   *
   * For more information on components, see our documentation
   * [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""`
   * returns `422`.
   *
   * @returns Created
   *
   * @throws {@link Components.CreateMeteredComponentError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createMeteredComponent(
    request: Components.CreateMeteredComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, Components.CreateMeteredComponentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/metered_components.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createMeteredComponentSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: Components.CreateMeteredComponentError,
      },
      options,
    );
  }

  /**
   * Create On/Off Component
   *
   * @remarks
   * Creates an On/Off component definition under the specified product family. An On/Off component
   * can then be added and “allocated” for a subscription.
   *
   * On/off components are used for any flat fee, recurring add on (think $99/month for tech support
   * or a flat add on shipping fee).
   *
   * For more information on components, see our documentation
   * [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""`
   * returns `422`.
   *
   * @returns Created
   *
   * @throws {@link Components.CreateOnOffComponentError} when the API answers with an error status
   * — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createOnOffComponent(
    request: Components.CreateOnOffComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, Components.CreateOnOffComponentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/product_families/{product_family_id}/on_off_components.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createOnOffComponentSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: Components.CreateOnOffComponentError,
      },
      options,
    );
  }

  /**
   * Create Prepaid Usage Component
   *
   * @remarks
   * Creates a prepaid usage component definition under the specified product family. A prepaid
   * component can then be added and “allocated” for a subscription.
   *
   * Prepaid components allow customers to pre-purchase units that can be used up over time on their
   * subscription. In a sense, they are the mirror image of metered components; while metered
   * components charge at the end of the period for the amount of units used, prepaid components are
   * charged for at the time of purchase, and usage is subsequently tracked against the amount
   * purchased.
   *
   * For more information, see [Components
   * Overview](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, taxable components must include a non-blank `tax_code`; sending a blank value results
   * in a validation error.
   *
   * @returns Created
   *
   * @throws {@link Components.CreatePrepaidUsageComponentError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createPrepaidUsageComponent(
    request: Components.CreatePrepaidUsageComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, Components.CreatePrepaidUsageComponentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/prepaid_usage_components.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createPrepaidComponentSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: Components.CreatePrepaidUsageComponentError,
      },
      options,
    );
  }

  /**
   * Create Quantity Based Component
   *
   * @remarks
   * Creates a Quantity Based component definition under the specified product family. A Quantity
   * Based component can then be added and “allocated” for a subscription.
   *
   * When defining a Quantity Based component, you can choose one of two types:
   * #### Recurring
   * Recurring quantity-based components are used to bill for the number of some unit (think monthly
   * software user licenses or the number of pairs of socks in a box-a-month club). This is most
   * commonly associated with billing for user licenses, number of users, number of employees, etc.
   *
   * #### One-time
   * One-time quantity-based components are used to create ad hoc usage charges that do not recur.
   * For example, at the time of signup, you might want to charge your customer a one-time fee for
   * onboarding or other services.
   *
   * The allocated quantity for one-time quantity-based components immediately gets reset back to
   * zero after the allocation is made.
   *
   * For more information, see [Components
   * Overview](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).
   * #### Hybrid Pricing
   * A `volume`, `tiered`, or `stairstep` component can combine its primary pricing with a secondary
   * pricing model (the `overage_pricing` parameter) so both bill as a single invoice line item
   * instead of two. See [Hybrid Pricing](page:introduction/basic-concepts/hybrid-pricing) for
   * requirements and configuration details.
   *
   * For more information on components, see our documentation
   * [here](https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview).
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""`
   * returns `422`.
   *
   * @returns Created
   *
   * @throws {@link Components.CreateQuantityBasedComponentError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createQuantityBasedComponent(
    request: Components.CreateQuantityBasedComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, Components.CreateQuantityBasedComponentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/quantity_based_components.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createQuantityBasedComponentSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: Components.CreateQuantityBasedComponentError,
      },
      options,
    );
  }

  /**
   * Find Component
   *
   * @remarks
   * Returns information for a component matching the provided handle. You can identify your
   * components with a handle so you don't have to save or reference the IDs we generate.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  findComponent(
    request: Components.FindComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/components/lookup.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [{ name: "handle", value: request.handle, schema: s.string() }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Components
   *
   * @remarks
   * Lists components for a site.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listComponents(
    request: Components.ListComponentsRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/components.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => basicDateFieldSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
          { name: "include_archived", value: request.includeArchived, schema: s.optional(s.boolean()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listComponentsFilterSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => componentResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Components for Product Family
   *
   * @remarks
   * Lists components for a particular product family.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listComponentsForProductFamily(
    request: Components.ListComponentsForProductFamilyRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/product_families/{product_family_id}/components.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "product_family_id", value: request.productFamilyId, schema: s.int() }],
        query: [
          { name: "include_archived", value: request.includeArchived, schema: s.optional(s.boolean()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listComponentsFilterSchema)),
          },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => basicDateFieldSchema)),
          },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => componentResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Component
   *
   * @remarks
   * Returns information regarding a component from a specific product family.
   *
   * You can read the component by either the component's id or handle. When using the handle, it
   * must be prefixed with `handle:`.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readComponent(
    request: Components.ReadComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/components/{component_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.string() },
        ],
        query: [
          {
            name: "include_features",
            value: request.includeFeatures,
            schema: s.defaulted(s.boolean(), false),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Component
   *
   * @remarks
   * Updates a component.
   *
   * You may read the component by either the component's id or handle. When using the handle, it
   * must be prefixed with `handle:`.
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""`
   * returns `422`.
   *
   * @returns OK
   *
   * @throws {@link Components.UpdateComponentError} when the API answers with an error status —
   * narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateComponent(
    request: Components.UpdateComponentRequestParams,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, Components.UpdateComponentError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/components/{component_id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "component_id", value: request.componentId, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateComponentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: Components.UpdateComponentError,
      },
      options,
    );
  }

  /**
   * Update Product Family Component
   *
   * @remarks
   * Updates a component from a specific product family.
   *
   * You may read the component by either the component's id or handle. When using the handle, it
   * must be prefixed with `handle:`.
   *
   * If you have the new [Catalog
   * experience](page:help/announcements/2026-announcements#new-catalog-experience-and-terminology)
   * enabled, taxable components must include a non-blank `tax_code`. Sending `"tax_code": ""`
   * returns `422`.
   *
   * @returns OK
   *
   * @throws {@link Components.UpdateProductFamilyComponentError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateProductFamilyComponent(
    request: Components.UpdateProductFamilyComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<ComponentResponse, Components.UpdateProductFamilyComponentError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/product_families/{product_family_id}/components/{component_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "product_family_id", value: request.productFamilyId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.string() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateComponentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: componentResponseSchema },
        errorFactory: Components.UpdateProductFamilyComponentError,
      },
      options,
    );
  }
}

export namespace Components {
  export type ArchiveComponentRequest = {
    /** The Advanced Billing id of the product family to which the component belongs */
    productFamilyId: number;
    /**
     * Either the Advanced Billing id of the component or the handle for the component prefixed with
     * `handle:`
     */
    componentId: string;
  };

  export class ArchiveComponentError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<ArchiveComponentError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateEventBasedComponentRequest = {
    /** Either the product family's id or its handle prefixed with `handle:` */
    productFamilyId: string;
    body?: CreateEbbComponent;
  };

  export class CreateEventBasedComponentError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateEventBasedComponentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateMeteredComponentRequest = {
    /** Either the product family's id or its handle prefixed with `handle:` */
    productFamilyId: string;
    body?: CreateMeteredComponent;
  };

  export class CreateMeteredComponentError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateMeteredComponentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateOnOffComponentRequest = {
    /** Either the product family's id or its handle prefixed with `handle:` */
    productFamilyId: string;
    body?: CreateOnOffComponent;
  };

  export class CreateOnOffComponentError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateOnOffComponentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreatePrepaidUsageComponentRequest = {
    /** Either the product family's id or its handle prefixed with `handle:` */
    productFamilyId: string;
    body?: CreatePrepaidComponent;
  };

  export class CreatePrepaidUsageComponentError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreatePrepaidUsageComponentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateQuantityBasedComponentRequest = {
    /** Either the product family's id or its handle prefixed with `handle:` */
    productFamilyId: string;
    body?: CreateQuantityBasedComponent;
  };

  export class CreateQuantityBasedComponentError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateQuantityBasedComponentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type FindComponentRequest = {
    /** The handle of the component to find */
    handle: string;
  };

  export type ListComponentsRequest = {
    /** The type of filter you would like to apply to your search. */
    dateField?: BasicDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
     * a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of start_date.
     */
    startDatetime?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or before exact time provided in query. You can
     * specify timezone in query - otherwise your site's time zone will be used. If provided, this
     * parameter will be used instead of end_date.
     */
    endDatetime?: string;
    /** Include archived items. */
    includeArchived?: boolean;
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
    /** Filter to use for List Components operations */
    filter?: ListComponentsFilter;
  };

  export type ListComponentsForProductFamilyRequest = {
    /** The Advanced Billing id of the product family */
    productFamilyId: number;
    /** Include archived items. */
    includeArchived?: boolean;
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
    /** Filter to use for List Components operations */
    filter?: ListComponentsFilter;
    /**
     * The type of filter you would like to apply to your search. Use in query
     * `date_field=created_at`.
     */
    dateField?: BasicDateField;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
     * a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or before exact time provided in query. You can
     * specify timezone in query - otherwise your site's time zone will be used. If provided, this
     * parameter will be used instead of end_date.
     */
    endDatetime?: string;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site's time zone will be used. If provided, this parameter
     * will be used instead of start_date.
     */
    startDatetime?: string;
  };

  export type ReadComponentRequest = {
    /** The Advanced Billing id of the product family to which the component belongs */
    productFamilyId: number;
    /**
     * Either the Advanced Billing id of the component or the handle for the component prefixed with
     * `handle:`
     */
    componentId: string;
    /**
     * When `true`, embeds the active feature catalog items for each result in a `features` array.
     * Default value is `false`.
     *
     * @default false
     */
    includeFeatures?: boolean;
  };

  export type UpdateComponentRequestParams = {
    /** The id or handle of the component */
    componentId: string;
    body?: UpdateComponentRequest;
  };

  export class UpdateComponentError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<UpdateComponentError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateProductFamilyComponentRequest = {
    /** The Advanced Billing id of the product family to which the component belongs */
    productFamilyId: number;
    /**
     * Either the Advanced Billing id of the component or the handle for the component prefixed with
     * `handle:`
     */
    componentId: string;
    body?: UpdateComponentRequest;
  };

  export class UpdateProductFamilyComponentError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<UpdateProductFamilyComponentError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
