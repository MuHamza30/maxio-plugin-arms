import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  activateEventBasedComponentSchema,
  type ActivateEventBasedComponent,
} from "../models/activate-event-based-component.js";
import { allocateComponentsSchema, type AllocateComponents } from "../models/allocate-components.js";
import {
  allocationPreviewResponseSchema,
  type AllocationPreviewResponse,
} from "../models/allocation-preview-response.js";
import { allocationResponseSchema, type AllocationResponse } from "../models/allocation-response.js";
import {
  bulkComponentsPricePointAssignmentSchema,
  type BulkComponentsPricePointAssignment,
} from "../models/bulk-components-price-point-assignment.js";
import {
  componentAllocationError1Schema,
  type ComponentAllocationError1,
} from "../models/component-allocation-error1.js";
import {
  componentPricePointError1Schema,
  type ComponentPricePointError1,
} from "../models/component-price-point-error1.js";
import {
  createAllocationRequestSchema,
  type CreateAllocationRequest,
} from "../models/create-allocation-request.js";
import { createUsageRequestSchema, type CreateUsageRequest } from "../models/create-usage-request.js";
import { creditSchemeRequestSchema, type CreditSchemeRequest } from "../models/credit-scheme-request.js";
import { ebbEventSchema, type EbbEvent } from "../models/ebb-event.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { includeNotNullSchema, type IncludeNotNull } from "../models/include-not-null.js";
import {
  listSubscriptionComponentsFilterSchema,
  type ListSubscriptionComponentsFilter,
} from "../models/list-subscription-components-filter.js";
import {
  listSubscriptionComponentsForSiteFilterSchema,
  type ListSubscriptionComponentsForSiteFilter,
} from "../models/list-subscription-components-for-site-filter.js";
import {
  listSubscriptionComponentsIncludeSchema,
  type ListSubscriptionComponentsInclude,
} from "../models/list-subscription-components-include.js";
import {
  listSubscriptionComponentsResponseSchema,
  type ListSubscriptionComponentsResponse,
} from "../models/list-subscription-components-response.js";
import {
  listSubscriptionComponentsSortSchema,
  type ListSubscriptionComponentsSort,
} from "../models/list-subscription-components-sort.js";
import {
  previewAllocationsRequestSchema,
  type PreviewAllocationsRequest,
} from "../models/preview-allocations-request.js";
import { sortingDirectionSchema, type SortingDirection } from "../models/sorting-direction.js";
import {
  subscriptionComponentAllocationError1Schema,
  type SubscriptionComponentAllocationError1,
} from "../models/subscription-component-allocation-error1.js";
import {
  subscriptionComponentResponseSchema,
  type SubscriptionComponentResponse,
} from "../models/subscription-component-response.js";
import {
  subscriptionListDateFieldSchema,
  type SubscriptionListDateField,
} from "../models/subscription-list-date-field.js";
import { subscriptionResponseSchema, type SubscriptionResponse } from "../models/subscription-response.js";
import { componentIdModelSchema, type ComponentIdModel } from "../models/unions/component-id-model.js";
import {
  subscriptionIdOrReferenceSchema,
  type SubscriptionIdOrReference,
} from "../models/unions/subscription-id-or-reference.js";
import {
  updateAllocationExpirationDateSchema,
  type UpdateAllocationExpirationDate,
} from "../models/update-allocation-expiration-date.js";
import { usageResponseSchema, type UsageResponse } from "../models/usage-response.js";
import type { Servers } from "../servers.js";

export class SubscriptionComponents {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Activate Event-Based Component
   *
   * @remarks
   * Activates an event-based component for a single subscription.
   *
   * To bill your subscribers on your Events data under the Events-Based Billing feature, the
   * components must be activated for the subscriber.
   *
   * For more information, see [Design Your
   * Catalog](https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes).
   *
   * Use this endpoint to activate an event-based component for a single subscription. Activating an
   * event-based component causes billing for events when the subscription is renewed.
   *
   * Note: it is possible to stream events for a subscription at any time, regardless of component
   * activation status. The activation status only determines if the subscription should be billed
   * for event-based component usage at renewal.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  activateEventBasedComponent(
    request: SubscriptionComponents.ActivateEventBasedComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/activate.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => activateEventBasedComponentSchema)),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Allocate Component
   *
   * @remarks
   * Creates an allocation, sets the current allocated quantity for the component, and records a
   * memo. Allocations can only be updated for Quantity, On/Off, and Prepaid Components.
   *
   * When creating an allocation via the API, you can pass the `upgrade_charge`, `downgrade_credit`,
   * and `accrue_charge` to be applied.
   *
   * > **Note:** These proration and accrual fields are ignored for Prepaid Components since this
   * component type always generates charges immediately without proration.
   *
   * For information on prorated components and upgrade/downgrade schemes, see [Setting Component
   * Allocations.](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration)
   *
   * ### Order of Resolution for upgrade_charge and downgrade_credit
   *
   * 1. Per allocation in API call (within a single allocation of the `allocations` array)
   * 2. [Component-level default
   *    value](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview)
   * 3. Allocation API call top level (outside of the `allocations` array)
   * 4. [Site-level default
   *    value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)
   *
   * ### Order of Resolution for accrue charge
   *
   * 1. Allocation API call top level (outside of the `allocations` array)
   * 2. [Site-level default
   *    value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)
   *
   * > **Note:** Proration uses the current price of the component as well as the current tax rates.
   * Changes to either may cause the prorated charge/credit to be wrong.
   *
   * For more information, see the [Component
   * Allocations](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview)
   * product Documentation.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.AllocateComponentError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  allocateComponent(
    request: SubscriptionComponents.AllocateComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<AllocationResponse, SubscriptionComponents.AllocateComponentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/components/{component_id}/allocations.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createAllocationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: allocationResponseSchema },
        errorFactory: SubscriptionComponents.AllocateComponentError,
      },
      options,
    );
  }

  /**
   * Allocate Components
   *
   * @remarks
   * Creates multiple allocations, sets the current allocated quantity for each of the components,
   * and records a memo. A `component_id` is required for each allocation.
   *
   * The charges and/or credits that are created will be rolled up into a single total which is used
   * to determine whether this is an upgrade or a downgrade.
   *
   * ### Order of Resolution for upgrade_charge and downgrade_credit
   *
   * 1. Per allocation in API call (within a single allocation of the `allocations` array)
   * 2. [Component-level default
   *    value](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview)
   * 3. Allocation API call top level (outside of the `allocations` array)
   * 4. [Site-level default
   *    value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)
   *
   * ### Order of Resolution for accrue charge
   *
   * 1. Allocation API call top level (outside of the `allocations` array)
   * 2. [Site-level default
   *    value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes)
   *
   * > **Note:** Proration uses the current price of the component as well as the current tax rates.
   * Changes to either may cause the prorated charge/credit to be wrong.
   *
   * For more information, see the [Component
   * Allocations](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview)
   * product documentation.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.AllocateComponentsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  allocateComponents(
    request: SubscriptionComponents.AllocateComponentsRequest,
    options?: RequestOptions,
  ): ApiPromise<AllocationResponse[], SubscriptionComponents.AllocateComponentsError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/allocations.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => allocateComponentsSchema)),
        },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => allocationResponseSchema)) },
        errorFactory: SubscriptionComponents.AllocateComponentsError,
      },
      options,
    );
  }

  /**
   * Bulk Event Ingestion
   *
   * @remarks
   * Records a collection of events.
   *
   * Note: this endpoint differs from the standard URL for this API in that `events` and your site
   * subdomain are included in the path.
   *
   * A maximum of 1000 events can be published in a single request. A 422 will be returned if this
   * limit is exceeded.
   *
   * @returns Created
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  bulkRecordEvents(
    request: SubscriptionComponents.BulkRecordEventsRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.ebb("/events/{api_handle}/bulk.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "api_handle", value: request.apiHandle, schema: s.string() }],
        query: [{ name: "store_uid", value: request.storeUid, schema: s.optional(s.string()) }],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.array(s.lazy(() => ebbEventSchema))),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Bulk Reset Subscription Components' Price Points
   *
   * @remarks
   * Resets all of a subscription's components to use the current default.
   *
   * **Note**: this will update the price point for all of the subscription's components, even ones
   * that have not been allocated yet.
   *
   * @returns Created
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  bulkResetSubscriptionComponentsPricePoints(
    request: SubscriptionComponents.BulkResetSubscriptionComponentsPricePointsRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/price_points/reset.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Bulk Update Subscription Components' Price Points
   *
   * @remarks
   * Updates the price points on one or more of a subscription's components.
   *
   * The `price_point` key can take either a:
   * 1. Price point id (integer)
   * 2. Price point handle (string)
   * 3. `"_default"` string, which will reset the price point to the component's current default
   *    price point.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsError} when
   * the API answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  bulkUpdateSubscriptionComponentsPricePoints(
    request: SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsRequest,
    options?: RequestOptions,
  ): ApiPromise<
    BulkComponentsPricePointAssignment,
    SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/price_points.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => bulkComponentsPricePointAssignmentSchema)),
        },
      },
      {
        success: { kind: "json", schema: bulkComponentsPricePointAssignmentSchema },
        errorFactory: SubscriptionComponents.BulkUpdateSubscriptionComponentsPricePointsError,
      },
      options,
    );
  }

  /**
   * Create Usage
   *
   * @remarks
   * Records an instance of metered or prepaid usage for a subscription.
   *
   * You can report metered or prepaid usage to Advanced Billing as often as you wish. You can
   * report usage as it happens or periodically, such as each night or once per billing period.
   *
   * Full documentation on how to create Components in the Advanced Billing UI can be located
   * [here](https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components).
   * Additionally, for information on how to record component usage against a subscription, see the
   * following resources:
   *
   * It is not possible to record metered usage for more than one component at a time. Usage should
   * be reported as one API call per component on a single subscription. For example, to record that
   * a subscriber has sent both an SMS Message and an Email, send an API call for each.
   *
   * See the following product documentation articles for more information:
   *
   * - [Create and Manage
   *   Components](https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components)
   * - [Recording Metered Component
   *   Usage](https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-metered-component-usage)
   * - [Reporting Prepaid Component
   *   Status](https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-prepaid-component-status)
   *
   * The `quantity` from usage for each component is accumulated to the `unit_balance` on the
   * [Component Line Item]($e/Subscription%20Components/readSubscriptionComponent) for the
   * subscription.
   *
   * ## Price Point ID usage
   *
   * If you are using price points, for metered and prepaid usage components Advanced Billing gives
   * you the option to specify a price point in your request.
   *
   * You do not need to specify a price point ID. If a price point is not included, the default
   * price point for the component will be used when the usage is recorded.
   *
   * ## Deducting Usage
   *
   * If you need to reverse a previous usage report or otherwise deduct from the current usage
   * balance, you can provide a negative quantity.
   *
   * Example:
   *
   * Previously recorded quantity was 5000:
   *
   * ```json
   * {
   *   "usage": {
   *     "quantity": 5000,
   *     "memo": "Recording 5000 units"
   *   }
   * }
   * ```
   *
   * To reduce the quantity to `0`, POST the following payload:
   *
   * ```json
   * {
   *   "usage": {
   *     "quantity": -5000,
   *     "memo": "Deducting 5000 units"
   *   }
   * }
   * ```
   * The `unit_balance` has a floor of `0`; negative unit balances are never allowed. For example,
   * if the usage balance is 100 and you deduct 200 units, the unit balance would then be `0`, not
   * `-100`.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.CreateUsageError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createUsage(
    request: SubscriptionComponents.CreateUsageRequestParams,
    options?: RequestOptions,
  ): ApiPromise<UsageResponse, SubscriptionComponents.CreateUsageError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          {
            name: "subscription_id_or_reference",
            value: request.subscriptionIdOrReference,
            schema: subscriptionIdOrReferenceSchema,
          },
          { name: "component_id", value: request.componentId, schema: componentIdModelSchema },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createUsageRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: usageResponseSchema },
        errorFactory: SubscriptionComponents.CreateUsageError,
      },
      options,
    );
  }

  /**
   * Deactivate Event-Based Component
   *
   * @remarks
   * Deactivates an event-based component for a single subscription. Deactivating the event-based
   * component causes Advanced Billing to ignore related events at subscription renewal.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deactivateEventBasedComponent(
    request: SubscriptionComponents.DeactivateEventBasedComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/deactivate.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.int() },
        ],
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
   * Delete Prepaid Usage Allocation
   *
   * @remarks
   * Deletes a prepaid usage allocation.
   *
   * Prepaid Usage components are unique in that their allocations are always additive. In order to
   * reduce a subscription's allocated quantity for a prepaid usage component, each allocation must
   * be destroyed individually via this endpoint.
   *
   * ## Credit Scheme
   *
   * By default, destroying an allocation will generate a service credit on the subscription. This
   * behavior can be modified with the optional `credit_scheme` parameter on this endpoint. The
   * accepted values are:
   *
   * 1. `none`: The allocation will be destroyed and the balances will be updated but no service
   *    credit or refund will be created.
   * 2. `credit`: The allocation will be destroyed and the balances will be updated and a service
   *    credit will be generated. This is also the default behavior if the `credit_scheme` param is
   *    not passed.
   * 3. `refund`: The allocation will be destroyed and the balances will be updated and a refund
   *    will be issued along with a Credit Note.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.DeletePrepaidUsageAllocationError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deletePrepaidUsageAllocation(
    request: SubscriptionComponents.DeletePrepaidUsageAllocationRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionComponents.DeletePrepaidUsageAllocationError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.int() },
          { name: "allocation_id", value: request.allocationId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => creditSchemeRequestSchema)),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionComponents.DeletePrepaidUsageAllocationError,
      },
      options,
    );
  }

  /**
   * List Allocations
   *
   * @remarks
   * Lists the 50 most recent Allocations, ordered by most recent first.
   *
   * ## On/Off Components
   *
   * When a subscription's on/off component has been toggled to on (`1`) or off (`0`), usage will be
   * logged in this response.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.ListAllocationsError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listAllocations(
    request: SubscriptionComponents.ListAllocationsRequest,
    options?: RequestOptions,
  ): ApiPromise<AllocationResponse[], SubscriptionComponents.ListAllocationsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/components/{component_id}/allocations.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.int() },
        ],
        query: [{ name: "page", value: request.page, schema: s.defaulted(s.int(), 1) }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => allocationResponseSchema)) },
        errorFactory: SubscriptionComponents.ListAllocationsError,
      },
      options,
    );
  }

  /**
   * List Subscription Components
   *
   * @remarks
   * Lists a subscription's applied components.
   *
   * ## Archived Components
   *
   * When requesting to list components for a given subscription, if the subscription contains
   * **archived** components they will be listed in the server response.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSubscriptionComponents(
    request: SubscriptionComponents.ListSubscriptionComponentsRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionComponentResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/components.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => subscriptionListDateFieldSchema)),
          },
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listSubscriptionComponentsFilterSchema)),
          },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
          {
            name: "price_point_ids",
            value: request.pricePointIds,
            schema: s.optional(s.lazy(() => includeNotNullSchema)),
          },
          {
            name: "product_family_ids",
            value: request.productFamilyIds,
            schema: s.optional(s.array(s.int())),
          },
          {
            name: "sort",
            value: request.sort,
            schema: s.optional(s.lazy(() => listSubscriptionComponentsSortSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.array(s.lazy(() => listSubscriptionComponentsIncludeSchema))),
          },
          { name: "in_use", value: request.inUse, schema: s.optional(s.boolean()) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => subscriptionComponentResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Subscription Components for Site
   *
   * @remarks
   * Lists components applied to each subscription.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSubscriptionComponentsForSite(
    request: SubscriptionComponents.ListSubscriptionComponentsForSiteRequest,
    options?: RequestOptions,
  ): ApiPromise<ListSubscriptionComponentsResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions_components.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "sort",
            value: request.sort,
            schema: s.optional(s.lazy(() => listSubscriptionComponentsSortSchema)),
          },
          {
            name: "direction",
            value: request.direction,
            schema: s.optional(s.lazy(() => sortingDirectionSchema)),
          },
          {
            name: "filter",
            value: request.filter,
            schema: s.optional(s.lazy(() => listSubscriptionComponentsForSiteFilterSchema)),
          },
          {
            name: "date_field",
            value: request.dateField,
            schema: s.optional(s.lazy(() => subscriptionListDateFieldSchema)),
          },
          { name: "start_date", value: request.startDate, schema: s.optional(s.string()) },
          { name: "start_datetime", value: request.startDatetime, schema: s.optional(s.string()) },
          { name: "end_date", value: request.endDate, schema: s.optional(s.string()) },
          { name: "end_datetime", value: request.endDatetime, schema: s.optional(s.string()) },
          { name: "subscription_ids", value: request.subscriptionIds, schema: s.optional(s.array(s.int())) },
          {
            name: "price_point_ids",
            value: request.pricePointIds,
            schema: s.optional(s.lazy(() => includeNotNullSchema)),
          },
          {
            name: "product_family_ids",
            value: request.productFamilyIds,
            schema: s.optional(s.array(s.int())),
          },
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.lazy(() => listSubscriptionComponentsIncludeSchema)),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listSubscriptionComponentsResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * List Usages
   *
   * @remarks
   * Lists usages associated with a subscription for a particular metered component. This will
   * display the previously recorded components for a subscription.
   *
   * This endpoint is not compatible with quantity-based components.
   *
   * ## Since Date and Until Date Usage
   *
   * Note: The `since_date` and `until_date` attributes each default to midnight on the date
   * specified. For example, in order to list usages for January 20th, you would need to append the
   * following to the URL.
   *
   * ```
   * ?since_date=2016-01-20&until_date=2016-01-21
   * ```
   *
   * ## Read Usage by Handle
   *
   * Use this endpoint to read the previously recorded components for a subscription. You can now
   * specify either the component id (integer) or the component handle prefixed by "handle:" to
   * specify the unique identifier for the component you are working with.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listUsages(
    request: SubscriptionComponents.ListUsagesRequest,
    options?: RequestOptions,
  ): ApiPromise<UsageResponse[], ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          {
            name: "subscription_id_or_reference",
            value: request.subscriptionIdOrReference,
            schema: subscriptionIdOrReferenceSchema,
          },
          { name: "component_id", value: request.componentId, schema: componentIdModelSchema },
        ],
        query: [
          { name: "since_id", value: request.sinceId, schema: s.optional(s.int()) },
          { name: "max_id", value: request.maxId, schema: s.optional(s.int()) },
          { name: "since_date", value: request.sinceDate, schema: s.optional(s.dateOnly()) },
          { name: "until_date", value: request.untilDate, schema: s.optional(s.dateOnly()) },
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: s.array(s.lazy(() => usageResponseSchema)) },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Preview Allocations
   *
   * @remarks
   * Previews a potential subscription's **quantity-based** or **on/off** component allocation in
   * the middle of the current billing period. This is useful if you want users to be able to see
   * the effect of a component operation before actually doing it.
   *
   * ## Fine-grained Component Control: Use with multiple `upgrade_charge`s or `downgrade_credits`
   *
   * When the allocation uses multiple different types of `upgrade_charge`s or `downgrade_credit`s,
   * the Allocation is viewed as an Allocation which uses "Fine-Grained Component Control". As a
   * result, the response will not include `direction` and `proration` within the
   * `allocation_preview`, but at the `line_items` and `allocations` level respectfully.
   *
   * See example below for Fine-Grained Component Control response.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.PreviewAllocationsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewAllocations(
    request: SubscriptionComponents.PreviewAllocationsRequestParams,
    options?: RequestOptions,
  ): ApiPromise<AllocationPreviewResponse, SubscriptionComponents.PreviewAllocationsError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/allocations/preview.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => previewAllocationsRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: allocationPreviewResponseSchema },
        errorFactory: SubscriptionComponents.PreviewAllocationsError,
      },
      options,
    );
  }

  /**
   * Read Subscription Component
   *
   * @remarks
   * Returns information for a specific component on a subscription.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.ReadSubscriptionComponentError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSubscriptionComponent(
    request: SubscriptionComponents.ReadSubscriptionComponentRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionComponentResponse, SubscriptionComponents.ReadSubscriptionComponentError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/components/{component_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.int() },
        ],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: subscriptionComponentResponseSchema },
        errorFactory: SubscriptionComponents.ReadSubscriptionComponentError,
      },
      options,
    );
  }

  /**
   * Event Ingestion
   *
   * @remarks
   * Records a single event for Events-Based Billing.
   *
   * Events-Based Billing is an evolved form of metered billing that is based on data-rich events
   * streamed in real-time from your system to Advanced Billing.
   *
   * These events can then be transformed, enriched, or analyzed to form the computed totals of
   * usage charges billed to your customers.
   *
   * This API allows you to stream events into the Advanced Billing data ingestion engine.
   *
   * For more information, see [Design Your
   * Catalog](https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes).
   *
   * Note: this endpoint differs from the standard URL for this API in that `events` and your site
   * subdomain are included in the path. For example:
   *
   * ```
   * https://events.chargify.com/my-site-subdomain/events/my-stream-api-handle
   * ```
   *
   * @returns Created
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  recordEvent(
    request: SubscriptionComponents.RecordEventRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.ebb("/events/{api_handle}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "api_handle", value: request.apiHandle, schema: s.string() }],
        query: [{ name: "store_uid", value: request.storeUid, schema: s.optional(s.string()) }],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "json", value: request.body, schema: s.optional(s.lazy(() => ebbEventSchema)) },
      },
      {
        success: { kind: "empty" },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Update Prepaid Usage Allocation Expiration Date
   *
   * @remarks
   * Updates the expiration date for a prepaid usage allocation. This expiration date can be changed
   * after the fact to allow for extending or shortening the allocation's active window.
   *
   * In order to change a prepaid usage allocation's expiration date, a PUT call must be made to the
   * allocation's endpoint with a new expiration date.
   *
   * ## Limitations
   *
   * A few limitations exist when changing an allocation's expiration date:
   *
   * - An expiration date can only be changed for an allocation that belongs to a price point with
   *   expiration interval options explicitly set.
   * - An expiration date can be changed towards the future with no limitations.
   * - An expiration date can be changed towards the past (essentially expiring it) up to the
   *   subscription's current period beginning date.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateError} when the
   * API answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updatePrepaidUsageAllocationExpirationDate(
    request: SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "component_id", value: request.componentId, schema: s.int() },
          { name: "allocation_id", value: request.allocationId, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateAllocationExpirationDateSchema)),
        },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionComponents.UpdatePrepaidUsageAllocationExpirationDateError,
      },
      options,
    );
  }
}

export namespace SubscriptionComponents {
  export type ActivateEventBasedComponentRequest = {
    /** The Advanced Billing id of the subscription */
    subscriptionId: number;
    /** The Advanced Billing id of the component */
    componentId: number;
    body?: ActivateEventBasedComponent;
  };

  export type AllocateComponentRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Advanced Billing id of the component */
    componentId: number;
    body?: CreateAllocationRequest;
  };

  export class AllocateComponentError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<AllocateComponentError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type AllocateComponentsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: AllocateComponents;
  };

  export class AllocateComponentsError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<AllocateComponentsError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type BulkRecordEventsRequest = {
    /** Identifies the Stream for which the events should be published. */
    apiHandle: string;
    /**
     * If you've attached your own Keen project as an Advanced Billing event data-store, use this
     * parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no
     * effect on Maxio Metering sites.
     */
    storeUid?: string;
    body?: EbbEvent[];
  };

  export type BulkResetSubscriptionComponentsPricePointsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export type BulkUpdateSubscriptionComponentsPricePointsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: BulkComponentsPricePointAssignment;
  };

  export class BulkUpdateSubscriptionComponentsPricePointsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"componentPricePointError1", ComponentPricePointError1>>;

    static readonly errors: ErrorDecoders<BulkUpdateSubscriptionComponentsPricePointsError> = [
      {
        on: 422,
        kind: "componentPricePointError1",
        decode: { kind: "json", schema: componentPricePointError1Schema },
      },
    ];
  }

  export type CreateUsageRequestParams = {
    /**
     * Either the Advanced Billing subscription ID (integer) or the subscription reference (string).
     * Important: In cases where a numeric string value matches both an existing subscription ID and
     * an existing subscription reference, the system will prioritize the subscription ID lookup.
     * For example, if both subscription ID 123 and subscription reference "123" exist, passing
     * "123" will return the subscription with ID 123.
     */
    subscriptionIdOrReference: SubscriptionIdOrReference;
    /**
     * Either the Advanced Billing id for the component or the component's handle prefixed by
     * `handle:`
     */
    componentId: ComponentIdModel;
    body?: CreateUsageRequest;
  };

  export class CreateUsageError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"errorListResponse1", ErrorListResponse1>>;

    static readonly errors: ErrorDecoders<CreateUsageError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type DeactivateEventBasedComponentRequest = {
    /** The Advanced Billing id of the subscription */
    subscriptionId: number;
    /** The Advanced Billing id of the component */
    componentId: number;
  };

  export type DeletePrepaidUsageAllocationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Advanced Billing id of the component */
    componentId: number;
    /** The Advanced Billing id of the allocation */
    allocationId: number;
    body?: CreditSchemeRequest;
  };

  export class DeletePrepaidUsageAllocationError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error404", undefined>
      | Declared<"subscriptionComponentAllocationError1", SubscriptionComponentAllocationError1>
    >;

    static readonly errors: ErrorDecoders<DeletePrepaidUsageAllocationError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "subscriptionComponentAllocationError1",
        decode: { kind: "json", schema: subscriptionComponentAllocationError1Schema },
      },
    ];
  }

  export type ListAllocationsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Advanced Billing id of the component */
    componentId: number;
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

  export class ListAllocationsError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error404", undefined> | Declared<"errorListResponse1", ErrorListResponse1>
    >;

    static readonly errors: ErrorDecoders<ListAllocationsError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListSubscriptionComponentsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /**
     * The type of filter you'd like to apply to your search. Use in query `date_field=updated_at`.
     */
    dateField?: SubscriptionListDateField;
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
    /** Filter to use for List Subscription Components operation */
    filter?: ListSubscriptionComponentsFilter;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
     * a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     */
    endDate?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or before exact time provided in query. You can
     * specify timezone in query - otherwise your site''s time zone will be used. If provided, this
     * parameter will be used instead of end_date.
     */
    endDatetime?: string;
    /**
     * Allows fetching components allocation only if price point id is present. Use in query
     * `price_point_ids=not_null`.
     */
    pricePointIds?: IncludeNotNull;
    /**
     * Allows fetching components allocation with matching product family id based on provided ids.
     * Use in query `product_family_ids=1,2,3`.
     */
    productFamilyIds?: number[];
    /** The attribute by which to sort. Use in query `sort=updated_at`. */
    sort?: ListSubscriptionComponentsSort;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified.
     */
    startDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site''s time zone will be used. If provided, this
     * parameter will be used instead of start_date.
     */
    startDatetime?: string;
    /**
     * Allows including additional data in the response. Use in query
     * `include=subscription,historic_usages`.
     */
    include?: ListSubscriptionComponentsInclude[];
    /**
     * If in_use is set to true, it returns only components that are currently in use. However, if
     * it's set to false or not provided, it returns all components connected with the subscription.
     */
    inUse?: boolean;
  };

  export type ListSubscriptionComponentsForSiteRequest = {
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
    /** The attribute by which to sort. Use in query: `sort=updated_at`. */
    sort?: ListSubscriptionComponentsSort;
    /** Controls the order in which results are returned. Use in query `direction=asc`. */
    direction?: SortingDirection;
    /** Filter to use for List Subscription Components For Site operation */
    filter?: ListSubscriptionComponentsForSiteFilter;
    /**
     * The type of filter you'd like to apply to your search. Use in query: `date_field=updated_at`.
     */
    dateField?: SubscriptionListDateField;
    /**
     * The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components
     * with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date
     * specified. Use in query `start_date=2011-12-15`.
     */
    startDate?: string;
    /**
     * The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or after exact time provided in query. You can specify
     * timezone in query - otherwise your site''s time zone will be used. If provided, this
     * parameter will be used instead of start_date. Use in query `start_datetime=2022-07-01
     * 09:00:05`.
     */
    startDatetime?: string;
    /**
     * The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
     * a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
     * Use in query `end_date=2011-12-16`.
     */
    endDate?: string;
    /**
     * The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
     * Returns components with a timestamp at or before exact time provided in query. You can
     * specify timezone in query - otherwise your site''s time zone will be used. If provided, this
     * parameter will be used instead of end_date. Use in query `end_datetime=2022-07-01 09:00:05`.
     */
    endDatetime?: string;
    /**
     * Allows fetching components allocation with matching subscription id based on provided ids.
     * Use in query `subscription_ids=1,2,3`.
     */
    subscriptionIds?: number[];
    /**
     * Allows fetching components allocation only if price point id is present. Use in query
     * `price_point_ids=not_null`.
     */
    pricePointIds?: IncludeNotNull;
    /**
     * Allows fetching components allocation with matching product family id based on provided ids.
     * Use in query `product_family_ids=1,2,3`.
     */
    productFamilyIds?: number[];
    /**
     * Allows including additional data in the response. Use in query
     * `include=subscription,historic_usages`.
     */
    include?: ListSubscriptionComponentsInclude;
  };

  export type ListUsagesRequest = {
    /**
     * Either the Advanced Billing subscription ID (integer) or the subscription reference (string).
     * Important: In cases where a numeric string value matches both an existing subscription ID and
     * an existing subscription reference, the system will prioritize the subscription ID lookup.
     * For example, if both subscription ID 123 and subscription reference "123" exist, passing
     * "123" will return the subscription with ID 123.
     */
    subscriptionIdOrReference: SubscriptionIdOrReference;
    /**
     * Either the Advanced Billing id for the component or the component's handle prefixed by
     * `handle:`
     */
    componentId: ComponentIdModel;
    /** Returns usages with an id greater than or equal to the one specified. */
    sinceId?: number;
    /** Returns usages with an id less than or equal to the one specified. */
    maxId?: number;
    /**
     * Returns usages with a created_at date greater than or equal to midnight (12:00 AM) on the
     * date specified.
     */
    sinceDate?: string;
    /**
     * Returns usages with a created_at date less than or equal to midnight (12:00 AM) on the date
     * specified.
     */
    untilDate?: string;
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

  export type PreviewAllocationsRequestParams = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: PreviewAllocationsRequest;
  };

  export class PreviewAllocationsError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"componentAllocationError1", ComponentAllocationError1>>;

    static readonly errors: ErrorDecoders<PreviewAllocationsError> = [
      {
        on: 422,
        kind: "componentAllocationError1",
        decode: { kind: "json", schema: componentAllocationError1Schema },
      },
    ];
  }

  export type ReadSubscriptionComponentRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /**
     * The Advanced Billing id of the component. Alternatively, the component's handle prefixed by
     * `handle:`
     */
    componentId: number;
  };

  export class ReadSubscriptionComponentError extends ApiError {
    declare readonly payload: ErrorPayload<Declared<"error404", undefined>>;

    static readonly errors: ErrorDecoders<ReadSubscriptionComponentError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type RecordEventRequest = {
    /** Identifies the Stream for which the event should be published. */
    apiHandle: string;
    /**
     * If you've attached your own Keen project as an Advanced Billing event data-store, use this
     * parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no
     * effect on Maxio Metering sites.
     */
    storeUid?: string;
    body?: EbbEvent;
  };

  export type UpdatePrepaidUsageAllocationExpirationDateRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The Advanced Billing id of the component */
    componentId: number;
    /** The Advanced Billing id of the allocation */
    allocationId: number;
    body?: UpdateAllocationExpirationDate;
  };

  export class UpdatePrepaidUsageAllocationExpirationDateError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error404", undefined>
      | Declared<"subscriptionComponentAllocationError1", SubscriptionComponentAllocationError1>
    >;

    static readonly errors: ErrorDecoders<UpdatePrepaidUsageAllocationExpirationDateError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      {
        on: 422,
        kind: "subscriptionComponentAllocationError1",
        decode: { kind: "json", schema: subscriptionComponentAllocationError1Schema },
      },
    ];
  }
}
