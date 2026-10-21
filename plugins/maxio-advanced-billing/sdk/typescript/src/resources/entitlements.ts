import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import * as s from "../core/validation/index.js";
import {
  aggregatedEntitlementsResponseSchema,
  type AggregatedEntitlementsResponse,
} from "../models/aggregated-entitlements-response.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import type { Servers } from "../servers.js";

/**
 * Entitlements report what a subscription is allowed to do, and how much of it, based on the
 * features granted by the subscription's products and components.
 *
 * When more than one product or component grants the same feature, the values are aggregated into
 * one entry per feature key and periodicity. For more information, see [Read Subscription
 * Entitlements with the
 * API](https://docs.maxio.com/billing/catalog/entitlements/read-subscription-entitlements-with-the-api).
 */
export class Entitlements {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Read Subscription Entitlements
   *
   * @remarks
   * Returns every feature a subscription is entitled to, collapsed into one entry per feature key
   * and periodicity window across all products and components on the subscription. A `usage_limit`
   * feature granted with two different periodicities comes back as two entries sharing one
   * `feature_key`, each identified by its own `periodicity_key`.
   *
   * When more than one product or component grants the same feature key and periodicity, the values
   * are combined:
   * - **`access_right`** features are combined with a boolean OR. If any contributor grants access,
   *   the aggregate is `true`. `source_products` only lists the contributors that granted `true`.
   * - **`usage_limit`** features are summed across every contributor sharing the same periodicity
   *   window. `source_products` lists every contributor. Grants with different periodicities are
   *   not summed together. Each periodicity is returned as a separate entry.
   * - **`service_right`** features are not combined: one contributor's value wins. Do not rely on
   *   which one when several grant the same feature key.
   *
   * `enabled` reflects both the aggregated value and the subscription's state. The field is `false`
   * whenever the subscription is not in a live state (`active`, `trialing`, `assessing`,
   * `past_due`, `soft_failure`), regardless of the aggregated value. Entitlements deliberately stay
   * enabled through dunning.
   *
   * @returns OK
   *
   * @throws {@link Entitlements.ReadSubscriptionEntitlementsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSubscriptionEntitlements(
    request: Entitlements.ReadSubscriptionEntitlementsRequest,
    options?: RequestOptions,
  ): ApiPromise<AggregatedEntitlementsResponse, Entitlements.ReadSubscriptionEntitlementsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/entitlements.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: aggregatedEntitlementsResponseSchema },
        errorFactory: Entitlements.ReadSubscriptionEntitlementsError,
      },
      options,
    );
  }
}

export namespace Entitlements {
  export type ReadSubscriptionEntitlementsRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class ReadSubscriptionEntitlementsError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"error404", undefined>
      | Undeclared;

    static readonly errors: ErrorDecoders<ReadSubscriptionEntitlementsError> = [
      { on: 403, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }
}
