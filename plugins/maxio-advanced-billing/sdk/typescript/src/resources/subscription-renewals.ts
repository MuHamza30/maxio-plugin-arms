import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  scheduledRenewalConfigurationItemRequestSchema,
  type ScheduledRenewalConfigurationItemRequest,
} from "../models/scheduled-renewal-configuration-item-request.js";
import {
  scheduledRenewalConfigurationItemResponseSchema,
  type ScheduledRenewalConfigurationItemResponse,
} from "../models/scheduled-renewal-configuration-item-response.js";
import {
  scheduledRenewalConfigurationRequestSchema,
  type ScheduledRenewalConfigurationRequest,
} from "../models/scheduled-renewal-configuration-request.js";
import {
  scheduledRenewalConfigurationResponseSchema,
  type ScheduledRenewalConfigurationResponse,
} from "../models/scheduled-renewal-configuration-response.js";
import {
  scheduledRenewalConfigurationsResponseSchema,
  type ScheduledRenewalConfigurationsResponse,
} from "../models/scheduled-renewal-configurations-response.js";
import {
  scheduledRenewalLockInRequestSchema,
  type ScheduledRenewalLockInRequest,
} from "../models/scheduled-renewal-lock-in-request.js";
import {
  scheduledRenewalUpdateRequestSchema,
  type ScheduledRenewalUpdateRequest,
} from "../models/scheduled-renewal-update-request.js";
import { statusSchema, type Status } from "../models/status.js";
import type { Servers } from "../servers.js";

/**
 * The Subscription Renewals object lets you schedule, preview, and manage a subscription's upcoming
 * renewal, including locking in specific pricing or canceling a scheduled renewal before it takes
 * effect. For more information, see [Understand Scheduled
 * Renewal](https://docs.maxio.com/billing/subscriptions/configuration/term-renewal/scheduled-renewal).
 */
export class SubscriptionRenewals {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Cancel Scheduled Renewal
   *
   * @remarks
   * Cancels a scheduled renewal configuration.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionRenewals.CancelScheduledRenewalConfigurationError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  cancelScheduledRenewalConfiguration(
    request: SubscriptionRenewals.CancelScheduledRenewalConfigurationRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationResponse,
    SubscriptionRenewals.CancelScheduledRenewalConfigurationError
  > {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{id}/cancel.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationResponseSchema },
        errorFactory: SubscriptionRenewals.CancelScheduledRenewalConfigurationError,
      },
      options,
    );
  }

  /**
   * Create Scheduled Renewal
   *
   * @remarks
   * Creates a scheduled renewal configuration for a subscription. The scheduled renewal is based on
   * the subscription’s current product and component setup.
   *
   * @returns Created
   *
   * @throws {@link SubscriptionRenewals.CreateScheduledRenewalConfigurationError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createScheduledRenewalConfiguration(
    request: SubscriptionRenewals.CreateScheduledRenewalConfigurationRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationResponse,
    SubscriptionRenewals.CreateScheduledRenewalConfigurationError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/scheduled_renewals.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => scheduledRenewalConfigurationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationResponseSchema },
        errorFactory: SubscriptionRenewals.CreateScheduledRenewalConfigurationError,
      },
      options,
    );
  }

  /**
   * Create Scheduled Renewal Configuration Item
   *
   * @remarks
   * Adds product and component line items to the scheduled renewal.
   *
   * If your site has list vs sales pricing enabled, accepts
   * renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted
   * value follows existing/default behavior; with list vs sales pricing disabled, parameter is
   * ignored (no validation/behavioral impact). This functionality is supported in the API, but is
   * not currently supported in SDKs.
   *
   * @returns Created
   *
   * @throws {@link SubscriptionRenewals.CreateScheduledRenewalConfigurationItemError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createScheduledRenewalConfigurationItem(
    request: SubscriptionRenewals.CreateScheduledRenewalConfigurationItemRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationItemResponse,
    SubscriptionRenewals.CreateScheduledRenewalConfigurationItemError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          {
            name: "scheduled_renewals_configuration_id",
            value: request.scheduledRenewalsConfigurationId,
            schema: s.int(),
          },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => scheduledRenewalConfigurationItemRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationItemResponseSchema },
        errorFactory: SubscriptionRenewals.CreateScheduledRenewalConfigurationItemError,
      },
      options,
    );
  }

  /**
   * Delete Scheduled Renewal Configuration Item
   *
   * @remarks
   * Removes an item from the pending renewal configuration.
   *
   * @returns No Content
   *
   * @throws {@link SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteScheduledRenewalConfigurationItem(
    request: SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          {
            name: "scheduled_renewals_configuration_id",
            value: request.scheduledRenewalsConfigurationId,
            schema: s.int(),
          },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionRenewals.DeleteScheduledRenewalConfigurationItemError,
      },
      options,
    );
  }

  /**
   * List Scheduled Renewals
   *
   * @remarks
   * Lists scheduled renewal configurations for the subscription and permits an optional status
   * query filter.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listScheduledRenewalConfigurations(
    request: SubscriptionRenewals.ListScheduledRenewalConfigurationsRequest,
    options?: RequestOptions,
  ): ApiPromise<ScheduledRenewalConfigurationsResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/scheduled_renewals.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [{ name: "status", value: request.status, schema: s.optional(s.lazy(() => statusSchema)) }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationsResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Immediate Renewal Lock-In
   *
   * @remarks
   * Locks in the renewal immediately.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionRenewals.LockInScheduledRenewalImmediatelyError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  lockInScheduledRenewalImmediately(
    request: SubscriptionRenewals.LockInScheduledRenewalImmediatelyRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationResponse,
    SubscriptionRenewals.LockInScheduledRenewalImmediatelyError
  > {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{id}/immediate_lock_in.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationResponseSchema },
        errorFactory: SubscriptionRenewals.LockInScheduledRenewalImmediatelyError,
      },
      options,
    );
  }

  /**
   * Read Scheduled Renewal
   *
   * @remarks
   * Retrieves the configuration settings for the scheduled renewal.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readScheduledRenewalConfiguration(
    request: SubscriptionRenewals.ReadScheduledRenewalConfigurationRequest,
    options?: RequestOptions,
  ): ApiPromise<ScheduledRenewalConfigurationResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Scheduled Renewal Lock-In
   *
   * @remarks
   * Schedules a future lock-in date for the renewal.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionRenewals.ScheduleScheduledRenewalLockInError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  scheduleScheduledRenewalLockIn(
    request: SubscriptionRenewals.ScheduleScheduledRenewalLockInRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationResponse,
    SubscriptionRenewals.ScheduleScheduledRenewalLockInError
  > {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{id}/schedule_lock_in.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => scheduledRenewalLockInRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationResponseSchema },
        errorFactory: SubscriptionRenewals.ScheduleScheduledRenewalLockInError,
      },
      options,
    );
  }

  /**
   * Unpublish Scheduled Renewal
   *
   * @remarks
   * Restores a scheduled renewal configuration to an editable state.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionRenewals.UnpublishScheduledRenewalConfigurationError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  unpublishScheduledRenewalConfiguration(
    request: SubscriptionRenewals.UnpublishScheduledRenewalConfigurationRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationResponse,
    SubscriptionRenewals.UnpublishScheduledRenewalConfigurationError
  > {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{id}/unpublish.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationResponseSchema },
        errorFactory: SubscriptionRenewals.UnpublishScheduledRenewalConfigurationError,
      },
      options,
    );
  }

  /**
   * Update Scheduled Renewal
   *
   * @remarks
   * Updates an existing configuration.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionRenewals.UpdateScheduledRenewalConfigurationError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateScheduledRenewalConfiguration(
    request: SubscriptionRenewals.UpdateScheduledRenewalConfigurationRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationResponse,
    SubscriptionRenewals.UpdateScheduledRenewalConfigurationError
  > {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => scheduledRenewalConfigurationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationResponseSchema },
        errorFactory: SubscriptionRenewals.UpdateScheduledRenewalConfigurationError,
      },
      options,
    );
  }

  /**
   * Update Scheduled Renewal Configuration Item
   *
   * @remarks
   * Updates an existing configuration item’s pricing and quantity.
   *
   * If you site has list vs sales pricing enabled, accepts
   * renewal_configuration_item.custom_price.list_price_point_id, validates and persists it; omitted
   * value follows existing/default behavior; with list vs sales pricing disabled, parameter is
   * ignored (no validation/behavioral impact). This functionality is supported in the API, but is
   * not currently supported in SDKs.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateScheduledRenewalConfigurationItem(
    request: SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemRequest,
    options?: RequestOptions,
  ): ApiPromise<
    ScheduledRenewalConfigurationItemResponse,
    SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemError
  > {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production(
          "/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json",
        ),
        auth: this.#auth.basicAuth,
        pathParams: [
          { name: "subscription_id", value: request.subscriptionId, schema: s.int() },
          {
            name: "scheduled_renewals_configuration_id",
            value: request.scheduledRenewalsConfigurationId,
            schema: s.int(),
          },
          { name: "id", value: request.id, schema: s.int() },
        ],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => scheduledRenewalUpdateRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: scheduledRenewalConfigurationItemResponseSchema },
        errorFactory: SubscriptionRenewals.UpdateScheduledRenewalConfigurationItemError,
      },
      options,
    );
  }
}

export namespace SubscriptionRenewals {
  export type CancelScheduledRenewalConfigurationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The renewal id. */
    id: number;
  };

  export class CancelScheduledRenewalConfigurationError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CancelScheduledRenewalConfigurationError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateScheduledRenewalConfigurationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: ScheduledRenewalConfigurationRequest;
  };

  export class CreateScheduledRenewalConfigurationError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateScheduledRenewalConfigurationError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type CreateScheduledRenewalConfigurationItemRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The scheduled renewal configuration id. */
    scheduledRenewalsConfigurationId: number;
    body?: ScheduledRenewalConfigurationItemRequest;
  };

  export class CreateScheduledRenewalConfigurationItemError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<CreateScheduledRenewalConfigurationItemError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type DeleteScheduledRenewalConfigurationItemRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The scheduled renewal configuration id. */
    scheduledRenewalsConfigurationId: number;
    /** The scheduled renewal configuration item id. */
    id: number;
  };

  export class DeleteScheduledRenewalConfigurationItemError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<DeleteScheduledRenewalConfigurationItemError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ListScheduledRenewalConfigurationsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** (Optional) Status filter for scheduled renewal configurations. */
    status?: Status;
  };

  export type LockInScheduledRenewalImmediatelyRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The renewal id. */
    id: number;
  };

  export class LockInScheduledRenewalImmediatelyError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<LockInScheduledRenewalImmediatelyError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadScheduledRenewalConfigurationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The renewal id. */
    id: number;
  };

  export type ScheduleScheduledRenewalLockInRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The renewal id. */
    id: number;
    body?: ScheduledRenewalLockInRequest;
  };

  export class ScheduleScheduledRenewalLockInError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<ScheduleScheduledRenewalLockInError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UnpublishScheduledRenewalConfigurationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The renewal id. */
    id: number;
  };

  export class UnpublishScheduledRenewalConfigurationError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<UnpublishScheduledRenewalConfigurationError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateScheduledRenewalConfigurationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The renewal id. */
    id: number;
    body?: ScheduledRenewalConfigurationRequest;
  };

  export class UpdateScheduledRenewalConfigurationError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<UpdateScheduledRenewalConfigurationError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type UpdateScheduledRenewalConfigurationItemRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    /** The scheduled renewal configuration id. */
    scheduledRenewalsConfigurationId: number;
    /** The scheduled renewal configuration item id. */
    id: number;
    body?: ScheduledRenewalUpdateRequest;
  };

  export class UpdateScheduledRenewalConfigurationItemError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<UpdateScheduledRenewalConfigurationItemError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
