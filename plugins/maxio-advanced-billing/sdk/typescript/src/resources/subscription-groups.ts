import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  addSubscriptionToAGroupSchema,
  type AddSubscriptionToAGroup,
} from "../models/add-subscription-to-agroup.js";
import {
  createSubscriptionGroupRequestSchema,
  type CreateSubscriptionGroupRequest,
} from "../models/create-subscription-group-request.js";
import {
  deleteSubscriptionGroupResponseSchema,
  type DeleteSubscriptionGroupResponse,
} from "../models/delete-subscription-group-response.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import {
  fullSubscriptionGroupResponseSchema,
  type FullSubscriptionGroupResponse,
} from "../models/full-subscription-group-response.js";
import {
  listSubscriptionGroupsResponseSchema,
  type ListSubscriptionGroupsResponse,
} from "../models/list-subscription-groups-response.js";
import {
  subscriptionGroupCreateErrorResponse1Schema,
  type SubscriptionGroupCreateErrorResponse1,
} from "../models/subscription-group-create-error-response1.js";
import {
  subscriptionGroupIncludeSchema,
  type SubscriptionGroupInclude,
} from "../models/subscription-group-include.js";
import {
  subscriptionGroupResponseSchema,
  type SubscriptionGroupResponse,
} from "../models/subscription-group-response.js";
import {
  subscriptionGroupSignupErrorResponse1Schema,
  type SubscriptionGroupSignupErrorResponse1,
} from "../models/subscription-group-signup-error-response1.js";
import {
  subscriptionGroupSignupRequestSchema,
  type SubscriptionGroupSignupRequest,
} from "../models/subscription-group-signup-request.js";
import {
  subscriptionGroupSignupResponseSchema,
  type SubscriptionGroupSignupResponse,
} from "../models/subscription-group-signup-response.js";
import {
  subscriptionGroupUpdateErrorResponse1Schema,
  type SubscriptionGroupUpdateErrorResponse1,
} from "../models/subscription-group-update-error-response1.js";
import {
  subscriptionGroupsListIncludeSchema,
  type SubscriptionGroupsListInclude,
} from "../models/subscription-groups-list-include.js";
import {
  updateSubscriptionGroupRequestSchema,
  type UpdateSubscriptionGroupRequest,
} from "../models/update-subscription-group-request.js";
import type { Servers } from "../servers.js";

/**
 * The Subscription Group object links multiple subscriptions for a single customer under one shared
 * payment profile and collection method, so you can consolidate billing instead of managing payment
 * details separately for each subscription. For more information, see [Understand Subscription
 * Groups](https://docs.maxio.com/billing/subscriptions/configuration/subscription-groups/understand-subscription-groups).
 */
export class SubscriptionGroups {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Add Subscription to Group
   *
   * @remarks
   * Adds an existing subscription to a subscription group. For sites making use of the
   * [Relationship
   * Billing](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview)
   * and [Customer
   * Hierarchy](https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies)
   * features, it is possible to add existing subscriptions to subscription groups.
   *
   * Passing `group` parameters with a `target` containing a `type` and optional `id` is all that's
   * needed. When the `target` parameter specifies a `"customer"` or `"subscription"` that is
   * already part of a hierarchy, the subscription will become a member of the customer's
   * subscription group. If the target customer or subscription is not part of a subscription group,
   * a new group will be created and the subscription will become part of the group with the
   * specified target customer set as the responsible payer for the group's subscriptions.
   *
   * **Note:** In order to add an existing subscription to a subscription group, it must belong to
   * either the same customer record as the target, or be within the same customer hierarchy.
   *
   * Rather than specifying a customer, the `target` parameter could instead simply have a value of
   * * `"self"` which indicates the subscription will be paid for not by some other customer, but by
   *   the subscribing customer,
   * * `"parent"` which indicates the subscription will be paid for by the subscribing customer's
   *   parent within a customer hierarchy, or
   * * `"eldest"` which indicates the subscription will be paid for by the root-level customer in
   *   the subscribing customer's hierarchy.
   *
   * To create a new subscription into a subscription group, reference the following: [Create
   * Subscription in a Subscription
   * Group](https://developers.chargify.com/docs/api-docs/d571659cf0f24-create-subscription#subscription-in-a-subscription-group)
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  addSubscriptionToGroup(
    request: SubscriptionGroups.AddSubscriptionToGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionGroupResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/group.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => addSubscriptionToAGroupSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionGroupResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Create Subscription Group
   *
   * @remarks
   * Creates a subscription group with given members.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroups.CreateSubscriptionGroupError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createSubscriptionGroup(
    request: SubscriptionGroups.CreateSubscriptionGroupRequestParams,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionGroupResponse, SubscriptionGroups.CreateSubscriptionGroupError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createSubscriptionGroupRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionGroupResponseSchema },
        errorFactory: SubscriptionGroups.CreateSubscriptionGroupError,
      },
      options,
    );
  }

  /**
   * Delete Subscription Group
   *
   * @remarks
   * Deletes a subscription group. Only groups without members can be deleted.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroups.DeleteSubscriptionGroupError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  deleteSubscriptionGroup(
    request: SubscriptionGroups.DeleteSubscriptionGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<DeleteSubscriptionGroupResponse, SubscriptionGroups.DeleteSubscriptionGroupError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: deleteSubscriptionGroupResponseSchema },
        errorFactory: SubscriptionGroups.DeleteSubscriptionGroupError,
      },
      options,
    );
  }

  /**
   * Find Subscription Group
   *
   * @remarks
   * Finds the subscription group associated with a subscription.
   *
   * If the subscription is not in a group, this endpoint returns an error.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroups.FindSubscriptionGroupError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  findSubscriptionGroup(
    request: SubscriptionGroups.FindSubscriptionGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<FullSubscriptionGroupResponse, SubscriptionGroups.FindSubscriptionGroupError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscription_groups/lookup.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [{ name: "subscription_id", value: request.subscriptionId, schema: s.string() }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: fullSubscriptionGroupResponseSchema },
        errorFactory: SubscriptionGroups.FindSubscriptionGroupError,
      },
      options,
    );
  }

  /**
   * List Subscription Groups
   *
   * @remarks
   * Lists subscription groups for the site. The response is paginated and will return a `meta` key
   * with pagination information.
   *
   * #### Account Balance Information
   *
   * Account balance information for the subscription groups is not returned by default. If this
   * information is desired, the `include[]=account_balances` parameter must be provided with the
   * request.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listSubscriptionGroups(
    request: SubscriptionGroups.ListSubscriptionGroupsRequest,
    options?: RequestOptions,
  ): ApiPromise<ListSubscriptionGroupsResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscription_groups.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.array(s.lazy(() => subscriptionGroupsListIncludeSchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: listSubscriptionGroupsResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Read Subscription Group
   *
   * @remarks
   * Returns subscription group details.
   *
   * #### Current Billing Amount in Cents
   *
   * Current billing amount for the subscription group is not returned by default. If this
   * information is desired, the `include[]=current_billing_amount_in_cents` parameter must be
   * provided with the request.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readSubscriptionGroup(
    request: SubscriptionGroups.ReadSubscriptionGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<FullSubscriptionGroupResponse, ApiError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [
          {
            name: "include",
            value: request.include,
            schema: s.optional(s.array(s.lazy(() => subscriptionGroupIncludeSchema))),
          },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: fullSubscriptionGroupResponseSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }

  /**
   * Remove Subscription from Group
   *
   * @remarks
   * Removes an existing subscription from a subscription group. For sites making use of the
   * [Relationship
   * Billing](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview)
   * and [Customer
   * Hierarchy](https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies)
   * features, it is possible to remove an existing subscription from a subscription group.
   *
   * @returns No Content
   *
   * @throws {@link SubscriptionGroups.RemoveSubscriptionFromGroupError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  removeSubscriptionFromGroup(
    request: SubscriptionGroups.RemoveSubscriptionFromGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<undefined, SubscriptionGroups.RemoveSubscriptionFromGroupError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/subscriptions/{subscription_id}/group.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "subscription_id", value: request.subscriptionId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "empty" },
        errorFactory: SubscriptionGroups.RemoveSubscriptionFromGroupError,
      },
      options,
    );
  }

  /**
   * Subscription Group Signup
   *
   * @remarks
   * Creates multiple subscriptions at once under the same customer and consolidates them into a
   * subscription group.
   *
   * You must provide one and only one of the `payer_id`/`payer_reference`/`payer_attributes` for
   * the customer attached to the group.
   *
   * You must provide one and only one of the
   * `payment_profile_id`/`credit_card_attributes`/`bank_account_attributes` for the payment profile
   * attached to the group.
   *
   * Only one of the `subscriptions` can have `"primary": true` attribute set.
   *
   * When passing a product to a subscription you can use either `product_id` or `product_handle` or
   * `offer_id`. You can also use `custom_price` instead. The subscription request examples below
   * will be split into two sections. The first section, "Subscription Customization", will focus on
   * passing different information with a subscription, such as components, calendar billing, and
   * custom fields. These examples will presume you are using a secure chargify_token generated by
   * Maxio.js (formerly Chargify.js).
   *
   * @returns Created
   *
   * @throws {@link SubscriptionGroups.SignupWithSubscriptionGroupError} when the API answers with
   * an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  signupWithSubscriptionGroup(
    request: SubscriptionGroups.SignupWithSubscriptionGroupRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionGroupSignupResponse, SubscriptionGroups.SignupWithSubscriptionGroupError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/subscription_groups/signup.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => subscriptionGroupSignupRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionGroupSignupResponseSchema },
        errorFactory: SubscriptionGroups.SignupWithSubscriptionGroupError,
      },
      options,
    );
  }

  /**
   * Update Subscription Group Members
   *
   * @remarks
   * Updates subscription group members. `"member_ids"` should contain an array of both subscription
   * IDs to set as group members and subscription IDs already present in the groups. Not including
   * them will result in removing them from the subscription group. To clean up members, just leave
   * the array empty.
   *
   * @returns OK
   *
   * @throws {@link SubscriptionGroups.UpdateSubscriptionGroupMembersError} when the API answers
   * with an error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateSubscriptionGroupMembers(
    request: SubscriptionGroups.UpdateSubscriptionGroupMembersRequest,
    options?: RequestOptions,
  ): ApiPromise<SubscriptionGroupResponse, SubscriptionGroups.UpdateSubscriptionGroupMembersError> {
    return this.#rawClient.execute(
      {
        method: "PUT",
        urlTemplate: this.#servers.production("/subscription_groups/{uid}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "uid", value: request.uid, schema: s.string() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateSubscriptionGroupRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: subscriptionGroupResponseSchema },
        errorFactory: SubscriptionGroups.UpdateSubscriptionGroupMembersError,
      },
      options,
    );
  }
}

export namespace SubscriptionGroups {
  export type AddSubscriptionToGroupRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
    body?: AddSubscriptionToAGroup;
  };

  export type CreateSubscriptionGroupRequestParams = {
    body?: CreateSubscriptionGroupRequest;
  };

  export class CreateSubscriptionGroupError extends ApiError {
    declare readonly payload:
      | Declared<"subscriptionGroupCreateErrorResponse1", SubscriptionGroupCreateErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<CreateSubscriptionGroupError> = [
      {
        on: 422,
        kind: "subscriptionGroupCreateErrorResponse1",
        decode: { kind: "json", schema: subscriptionGroupCreateErrorResponse1Schema },
      },
    ];
  }

  export type DeleteSubscriptionGroupRequest = {
    /** The uid of the subscription group */
    uid: string;
  };

  export class DeleteSubscriptionGroupError extends ApiError {
    declare readonly payload: Declared<"error404", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<DeleteSubscriptionGroupError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type FindSubscriptionGroupRequest = {
    /** The Advanced Billing id of the subscription associated with the subscription group */
    subscriptionId: string;
  };

  export class FindSubscriptionGroupError extends ApiError {
    declare readonly payload: Declared<"error404", undefined> | Undeclared;

    static readonly errors: ErrorDecoders<FindSubscriptionGroupError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
    ];
  }

  export type ListSubscriptionGroupsRequest = {
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
     * A list of additional information to include in the response. The following values are
     * supported:
     *
     * - `account_balances`: Account balance information for the subscription groups. Use in query:
     *   `include[]=account_balances`
     */
    include?: SubscriptionGroupsListInclude[];
  };

  export type ReadSubscriptionGroupRequest = {
    /** The uid of the subscription group */
    uid: string;
    /**
     * Allows including additional data in the response. Use in query:
     * `include[]=current_billing_amount_in_cents`.
     */
    include?: SubscriptionGroupInclude[];
  };

  export type RemoveSubscriptionFromGroupRequest = {
    /** The Chargify id of the subscription. */
    subscriptionId: number;
  };

  export class RemoveSubscriptionFromGroupError extends ApiError {
    declare readonly payload:
      | Declared<"error404", undefined>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<RemoveSubscriptionFromGroupError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type SignupWithSubscriptionGroupRequest = {
    body?: SubscriptionGroupSignupRequest;
  };

  export class SignupWithSubscriptionGroupError extends ApiError {
    declare readonly payload:
      | Declared<"subscriptionGroupSignupErrorResponse1", SubscriptionGroupSignupErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<SignupWithSubscriptionGroupError> = [
      {
        on: 422,
        kind: "subscriptionGroupSignupErrorResponse1",
        decode: { kind: "json", schema: subscriptionGroupSignupErrorResponse1Schema },
      },
    ];
  }

  export type UpdateSubscriptionGroupMembersRequest = {
    /** The uid of the subscription group */
    uid: string;
    body?: UpdateSubscriptionGroupRequest;
  };

  export class UpdateSubscriptionGroupMembersError extends ApiError {
    declare readonly payload:
      | Declared<"subscriptionGroupUpdateErrorResponse1", SubscriptionGroupUpdateErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateSubscriptionGroupMembersError> = [
      {
        on: 422,
        kind: "subscriptionGroupUpdateErrorResponse1",
        decode: { kind: "json", schema: subscriptionGroupUpdateErrorResponse1Schema },
      },
    ];
  }
}
