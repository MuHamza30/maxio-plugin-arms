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
  subscriptionMigrationPreviewRequestSchema,
  type SubscriptionMigrationPreviewRequest,
} from "../models/subscription-migration-preview-request.js";
import {
  subscriptionMigrationPreviewResponseSchema,
  type SubscriptionMigrationPreviewResponse,
} from "../models/subscription-migration-preview-response.js";
import {
  subscriptionProductMigrationRequestSchema,
  type SubscriptionProductMigrationRequest,
} from "../models/subscription-product-migration-request.js";
import { subscriptionResponseSchema, type SubscriptionResponse } from "../models/subscription-response.js";
import type { Servers } from "../servers.js";

/**
 * Use the Subscription Products object to migrate a subscription from one product or price point to
 * another, including previewing the effects of a migration before committing to it. For more
 * information, see [Upgrade or Downgrade a
 * Subscription](https://docs.maxio.com/billing/subscriptions/management/subscription-actions/upgrade-or-downgrade-a-subscription).
 */
export class SubscriptionProducts {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Migrate Subscription Product
   *
   * @remarks
   * Migrates a subscription to a different product.
   *
   * To create a migration, you must pass the `product_id` or `product_handle` in the object when
   * you send a POST request. You can also pass either a `product_price_point_id` or
   * `product_price_point_handle` to choose which price point the subscription is moved to. If no
   * price point identifier is passed, the subscription is moved to the product's default price
   * point. The response is the updated subscription.
   *
   * ## Valid Subscriptions
   *
   * Subscriptions should be in the `active` or `trialing` state to be migrated.
   *
   * (For backwards compatibility reasons, it is possible to migrate a subscription that is in the
   * `trial_ended` state via the API, however this is not recommended. Since `trial_ended` is an
   * end-of-life state, the subscription should be canceled, the product changed, and then the
   * subscription can be reactivated.)
   *
   * For more information, see [Product Changes and
   * Migrations](https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations).
   *
   * ## Failed Migrations
   *
   * Important note: One of the most common ways that a migration can fail is when the attempt is
   * made to migrate a subscription to its current product.
   *
   * ## 3D Secure (3DS) Authentication post-authentication flow
   *
   * When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA),
   * the request enters a post-authentication flow where a 422 Unprocessable Entity status is
   * returned with an action_link that will direct the customer through 3DS Authentication.
   *
   * See the [3D Secure Post-Authentication
   * Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow)
   * article in the product documentation to learn how to manage the redirect flow.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionProducts.MigrateSubscriptionProductError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  migrateSubscriptionProduct(
    request: SubscriptionProducts.MigrateSubscriptionProductRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionResponse, SubscriptionProducts.MigrateSubscriptionProductError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/migrations.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => subscriptionProductMigrationRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionResponseSchema },
        errorFactory: SubscriptionProducts.MigrateSubscriptionProductError,
      },
      options,
    );
  }

  /**
   * Preview Subscription Product Migration
   *
   * @remarks
   * Previews the charges resulting from migrating a subscription to a different product.
   *
   * ## Previewing a future date
   * It is also possible to preview the migration for a date in the future, as long as it's still
   * within the subscription's current billing period, by passing a `proration_date` along with the
   * request (e.g., `"proration_date": "2020-12-18T18:25:43.511Z"`).
   *
   * This will calculate the prorated adjustment, charge, payment and credit applied values assuming
   * the migration is done at that date in the future as opposed to right now.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionProducts.PreviewSubscriptionProductMigrationError} when the API
   * answers with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewSubscriptionProductMigration(
    request: SubscriptionProducts.PreviewSubscriptionProductMigrationRequest,
    options?: RequestOptions,
  ): ApiPromise<
    SubscriptionMigrationPreviewResponse,
    SubscriptionProducts.PreviewSubscriptionProductMigrationError
  > {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/migrations/preview.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => subscriptionMigrationPreviewRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionMigrationPreviewResponseSchema },
        errorFactory: SubscriptionProducts.PreviewSubscriptionProductMigrationError,
      },
      options,
    );
  }
}

export namespace SubscriptionProducts {
  export type MigrateSubscriptionProductRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: SubscriptionProductMigrationRequest;
  };

  export class MigrateSubscriptionProductError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<MigrateSubscriptionProductError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type PreviewSubscriptionProductMigrationRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: SubscriptionMigrationPreviewRequest;
  };

  export class PreviewSubscriptionProductMigrationError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<PreviewSubscriptionProductMigrationError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }
}
