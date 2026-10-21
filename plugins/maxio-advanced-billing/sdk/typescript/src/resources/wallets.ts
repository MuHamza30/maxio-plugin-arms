import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import { createWalletRequestSchema, type CreateWalletRequest } from "../models/create-wallet-request.js";
import { status2Schema, type Status2 } from "../models/status2.js";
import { updateWalletRequestSchema, type UpdateWalletRequest } from "../models/update-wallet-request.js";
import { walletErrorResponse1Schema, type WalletErrorResponse1 } from "../models/wallet-error-response1.js";
import { walletResponseSchema, type WalletResponse } from "../models/wallet-response.js";
import { walletsListResponseSchema, type WalletsListResponse } from "../models/wallets-list-response.js";
import type { Servers } from "../servers.js";

/**
 * The Wallet object is a balance, owned by a subscription and denominated in the unit of a Wallet
 * Product, that you can create, fund, drain, and read through the API.
 *
 * Wallets suit prepaid allowances, credits, and consumption pools that don't map cleanly onto the
 * regular usage-billing cycle. Every balance change is recorded on the wallet's append-only ledger.
 * For more information, see [Understand
 * Wallets](https://docs.maxio.com/billing/catalog/wallets/understand-wallets).
 */
export class Wallets {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Archive Wallet
   *
   * @remarks
   * Archives the wallet: blocks further grants, debits, adjustments, and purchases (each returns
   * `422`), stops any metered drawdown, and stops recurring funding (its schedule is deactivated
   * with reason `wallet_archived`, not removed), while reads and the ledger stay available. Nothing
   * already on the wallet is destroyed or clawed back, but nothing on it can be spent either, by
   * any path, once archived. Idempotent: archiving an already-archived wallet returns the same
   * `200`. There is no restore endpoint.
   *
   * @returns The wallet, with `"status": "archived"`.
   *
   * @throws {@link Wallets.ArchiveWalletError} when the API answers with an error status — narrow
   * on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  archiveWallet(
    request: Wallets.ArchiveWalletRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletResponse, Wallets.ArchiveWalletError> {
    return this.#rawClient.execute(
      {
        method: "DELETE",
        urlTemplate: this.#servers.production("/wallets/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletResponseSchema },
        errorFactory: Wallets.ArchiveWalletError,
      },
      options,
    );
  }

  /**
   * Create Wallet
   *
   * @remarks
   * Creates a wallet owned by a subscription and denominated by a [Wallet
   * Product]($e/Wallet%20Products/createWalletProduct): only a Wallet Product can denominate a
   * wallet, not an ordinary component. The Wallet Product must be active; it never belongs to a
   * product family, so there's no family check against the subscription. It's **immutable for the
   * life of the wallet**; there's no way to repoint an existing wallet at a different one.
   *
   * This endpoint always creates a `manual` wallet. To provision a wallet automatically from a
   * usage-limit entitlement instead, configure `wallet_behavior` on the Feature behind that
   * entitlement (see [the Wallets concept
   * guide](page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature)) rather
   * than sending `entitlement_id` here.
   *
   * @returns Wallet created. The balance is `"0.0"` with no grants, unless a non-zero
   * `initial_balance` was given. In that case, the balance and its seeded grant are already
   * reflected.
   *
   * @throws {@link Wallets.CreateWalletError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createWallet(
    request: Wallets.CreateWalletRequestParams = {},
    options?: RequestOptions,
  ): ApiPromise<WalletResponse, Wallets.CreateWalletError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallets.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createWalletRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletResponseSchema },
        errorFactory: Wallets.CreateWalletError,
      },
      options,
    );
  }

  /**
   * List Wallets
   *
   * @remarks
   * Lists the wallets on your site, in creation order, paginated. Without `subscription_id`,
   * returns every wallet on the site. The API key is the tenancy boundary; `subscription_id` only
   * narrows the result set further. Archived wallets are included unless you filter them out with
   * `status=active`.
   *
   * @returns OK
   *
   * @throws {@link Wallets.ListWalletsError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listWallets(
    request: Wallets.ListWalletsRequest = {},
    options?: RequestOptions,
  ): ApiPromise<WalletsListResponse, Wallets.ListWalletsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/wallets.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
          { name: "subscription_id", value: request.subscriptionId, schema: s.optional(s.int()) },
          { name: "status", value: request.status, schema: s.optional(s.lazy(() => status2Schema)) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletsListResponseSchema },
        errorFactory: Wallets.ListWalletsError,
      },
      options,
    );
  }

  /**
   * Read Wallet
   *
   * @remarks
   * Returns the wallet's balance and grant breakdown. For an active, metered wallet on a site with
   * metered consumption enabled, this is the only operation that computes a live balance from meter
   * usage; see the wallet resource's `metered_*` fields. It is also the only operation where
   * `balance` can differ from `posted_balance`, and a grant's `remaining` from its
   * `posted_remaining`: the pending usage is drawn from the grants in drain order, so the grants'
   * `remaining` add up to `balance`. Readable regardless of status. Archiving a wallet doesn't
   * affect reads.
   *
   * @returns OK
   *
   * @throws {@link Wallets.ReadWalletError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  readWallet(
    request: Wallets.ReadWalletRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletResponse, Wallets.ReadWalletError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/wallets/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletResponseSchema },
        errorFactory: Wallets.ReadWalletError,
      },
      options,
    );
  }

  /**
   * Update Wallet
   *
   * @remarks
   * Updates the wallet's editable attributes. Only `name` is editable; any other attribute in the
   * body is ignored. Send only the attributes to change.
   *
   * @returns The updated wallet. Reports the stored balance, equal to `posted_balance`, with the
   * `metered_*` fields `null`, as on list, create, and archive.
   *
   * @throws {@link Wallets.UpdateWalletError} when the API answers with an error status — narrow on
   * `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  updateWallet(
    request: Wallets.UpdateWalletRequestParams,
    options?: RequestOptions,
  ): ApiPromise<WalletResponse, Wallets.UpdateWalletError> {
    return this.#rawClient.execute(
      {
        method: "PATCH",
        urlTemplate: this.#servers.production("/wallets/{id}.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "id", value: request.id, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => updateWalletRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletResponseSchema },
        errorFactory: Wallets.UpdateWalletError,
      },
      options,
    );
  }
}

export namespace Wallets {
  export type ArchiveWalletRequest = {
    /** The Advanced Billing id of the wallet. */
    id: number;
  };

  export class ArchiveWalletError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ArchiveWalletError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
    ];
  }

  export type CreateWalletRequestParams = {
    body?: CreateWalletRequest;
  };

  export class CreateWalletError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<CreateWalletError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 422,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }

  export type ListWalletsRequest = {
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
    /** Restricts the result to wallets owned by this subscription. */
    subscriptionId?: number;
    /**
     * Restricts the result by wallet status. An unrecognized value returns `422` rather than being
     * silently ignored.
     */
    status?: Status2;
  };

  export class ListWalletsError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ListWalletsError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 422, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
    ];
  }

  export type ReadWalletRequest = {
    /** The Advanced Billing id of the wallet. */
    id: number;
  };

  export class ReadWalletError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<ReadWalletError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
    ];
  }

  export type UpdateWalletRequestParams = {
    /** The Advanced Billing id of the wallet. */
    id: number;
    body?: UpdateWalletRequest;
  };

  export class UpdateWalletError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<UpdateWalletError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 422,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }
}
