import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { autoInviteSchema, type AutoInvite } from "../models/auto-invite.js";
import { customerResponseSchema, type CustomerResponse } from "../models/customer-response.js";
import { errorListResponse1Schema, type ErrorListResponse1 } from "../models/error-list-response1.js";
import { portalManagementLinkSchema, type PortalManagementLink } from "../models/portal-management-link.js";
import { resentInvitationSchema, type ResentInvitation } from "../models/resent-invitation.js";
import { revokedInvitationSchema, type RevokedInvitation } from "../models/revoked-invitation.js";
import {
  tooManyManagementLinkRequestsError1Schema,
  type TooManyManagementLinkRequestsError1,
} from "../models/too-many-management-link-requests-error1.js";
import type { Servers } from "../servers.js";

/**
 * The Billing Portal object allows you to enable, disable, and manage customer access to the
 * self-service Billing Portal, where customers can view invoices and manage their own payment
 * details. For more information, see [Understand the Billing
 * Portal](https://docs.maxio.com/billing/billing-portal/overview/understand-the-billing-portal).
 */
export class BillingPortal {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Enable Billing Portal for Customer
   *
   * @remarks
   * Enables Billing Portal access for a customer, with an option to send an invitation email at the
   * same time.
   *
   * ## Billing Portal Security
   *
   * If your customer has been invited to the Billing Portal, they receive a link to manage their
   * subscription (the “Management URL”) automatically at the bottom of their statements, invoices,
   * and receipts. **This link changes periodically for security and is only valid for 65 days.**
   *
   * If you need to provide your customer their Management URL through other means, you can retrieve
   * it [via the API]($e/Billing%20Portal/readBillingPortalLink). Because the URL is
   * cryptographically signed with a timestamp, merchants cannot generate the URL without requesting
   * it through the API.
   *
   * To prevent abuse and overuse, request a new URL only when absolutely necessary. Management URLs
   * are good for 65 days, so you should re-use a previously generated one as much as possible. If
   * you use the URL frequently (such as to display on your website), **do not** make an API request
   * every time.
   *
   * For more information configuring the Billing Portal, see [Billing Portal
   * Overview](https://maxio.zendesk.com/hc/en-us/articles/24252412965133-Billing-Portal-Overview).
   *
   * @returns OK
   *
   * @throws {@link BillingPortal.EnableBillingPortalForCustomerError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  enableBillingPortalForCustomer(
    request: BillingPortal.EnableBillingPortalForCustomerRequest,
    options?: RequestOptions,
  ): ApiPromise<CustomerResponse, BillingPortal.EnableBillingPortalForCustomerError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/portal/customers/{customer_id}/enable.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "customer_id", value: request.customerId, schema: s.int() }],
        query: [
          {
            name: "auto_invite",
            value: request.autoInvite,
            schema: s.optional(s.lazy(() => autoInviteSchema)),
          },
        ],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: customerResponseSchema },
        errorFactory: BillingPortal.EnableBillingPortalForCustomerError,
      },
      options,
    );
  }

  /**
   * Read Billing Portal Management Link
   *
   * @remarks
   * Returns the exact URL required for a subscriber to access the Billing Portal.
   *
   * ## Management Link Request Rules
   *
   * + When retrieving a management URL, multiple requests for the same customer in a short period
   *   return the **same** URL
   * + A new URL is not generated for 15 days
   * + You must cache and remember this URL if you are going to need it again within 15 days
   * + Only request a new URL after the `new_link_available_at` date
   * + You are limited to 15 requests for the same URL. If you make more than 15 requests before
   *   `new_link_available_at`, you are blocked from further Management URL requests (with a
   *   response code `429`).
   *
   * @returns OK
   *
   * @throws {@link BillingPortal.ReadBillingPortalLinkError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readBillingPortalLink(
    request: BillingPortal.ReadBillingPortalLinkRequest,
    options?: RequestOptions,
  ): ApiPromise<PortalManagementLink, BillingPortal.ReadBillingPortalLinkError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/portal/customers/{customer_id}/management_link.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "customer_id", value: request.customerId, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: portalManagementLinkSchema },
        errorFactory: BillingPortal.ReadBillingPortalLinkError,
      },
      options,
    );
  }

  /**
   * Resend Billing Portal Invitation
   *
   * @remarks
   * Resends a customer's Billing Portal invitation.
   *
   * If you attempt to resend an invitation 5 times within 30 minutes, you will receive a `422`
   * response with an `error` message in the body.
   *
   * If you attempt to resend an invitation when the Billing Portal is already disabled for a
   * Customer, you will receive a `422` error response.
   *
   * If you attempt to resend an invitation when the Customer does not exist, you will receive a
   * `404` error response.
   *
   * ## Limitations
   *
   * This endpoint will only return a JSON response.
   *
   * @returns OK
   *
   * @throws {@link BillingPortal.ResendBillingPortalInvitationError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  resendBillingPortalInvitation(
    request: BillingPortal.ResendBillingPortalInvitationRequest,
    options?: RequestOptions,
  ): ApiPromise<ResentInvitation, BillingPortal.ResendBillingPortalInvitationError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/portal/customers/{customer_id}/invitations/invite.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "customer_id", value: request.customerId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: resentInvitationSchema },
        errorFactory: BillingPortal.ResendBillingPortalInvitationError,
      },
      options,
    );
  }

  /**
   * Revoke Billing Portal Invitation for Customer
   *
   * @remarks
   * Revokes a customer's Billing Portal invitation.
   *
   * If you attempt to revoke an invitation when the Billing Portal is already disabled for a
   * Customer, you will receive a 422 error response.
   *
   * ## Limitations
   *
   * This endpoint will only return a JSON response.
   *
   * @returns OK
   *
   * @throws {@link ApiError} when the API answers with an error status
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  revokeBillingPortalAccess(
    request: BillingPortal.RevokeBillingPortalAccessRequest,
    options?: RequestOptions,
  ): ApiPromise<RevokedInvitation, ApiError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/portal/customers/{customer_id}/invitations/revoke.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "customer_id", value: request.customerId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: revokedInvitationSchema },
        errorFactory: ApiError,
      },
      options,
    );
  }
}

export namespace BillingPortal {
  export type EnableBillingPortalForCustomerRequest = {
    /** The Chargify id of the customer */
    customerId: number;
    /**
     * When set to 1, an Invitation email will be sent to the Customer. When set to 0, or not sent,
     * an email will not be sent. Use in query: `auto_invite=1`.
     */
    autoInvite?: AutoInvite;
  };

  export class EnableBillingPortalForCustomerError extends ApiError {
    declare readonly payload: Declared<"errorListResponse1", ErrorListResponse1> | Undeclared;

    static readonly errors: ErrorDecoders<EnableBillingPortalForCustomerError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type ReadBillingPortalLinkRequest = {
    /** The Chargify id of the customer */
    customerId: number;
  };

  export class ReadBillingPortalLinkError extends ApiError {
    declare readonly payload:
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Declared<"tooManyManagementLinkRequestsError1", TooManyManagementLinkRequestsError1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ReadBillingPortalLinkError> = [
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
      {
        on: 429,
        kind: "tooManyManagementLinkRequestsError1",
        decode: { kind: "json", schema: tooManyManagementLinkRequestsError1Schema },
      },
    ];
  }

  export type ResendBillingPortalInvitationRequest = {
    /** The Chargify id of the customer */
    customerId: number;
  };

  export class ResendBillingPortalInvitationError extends ApiError {
    declare readonly payload:
      | Declared<"error404", undefined>
      | Declared<"errorListResponse1", ErrorListResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ResendBillingPortalInvitationError> = [
      { on: 404, kind: "error404", decode: { kind: "empty" } },
      { on: 422, kind: "errorListResponse1", decode: { kind: "json", schema: errorListResponse1Schema } },
    ];
  }

  export type RevokeBillingPortalAccessRequest = {
    /** The Chargify id of the customer */
    customerId: number;
  };
}
