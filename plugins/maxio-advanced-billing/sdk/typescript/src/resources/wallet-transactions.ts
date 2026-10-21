import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createWalletTransactionRequestSchema,
  type CreateWalletTransactionRequest,
} from "../models/create-wallet-transaction-request.js";
import { walletErrorResponse1Schema, type WalletErrorResponse1 } from "../models/wallet-error-response1.js";
import {
  walletTransactionResultResponseSchema,
  type WalletTransactionResultResponse,
} from "../models/wallet-transaction-result-response.js";
import {
  walletTransactionsListResponseSchema,
  type WalletTransactionsListResponse,
} from "../models/wallet-transactions-list-response.js";
import type { Servers } from "../servers.js";

export class WalletTransactions {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Wallet Transaction
   *
   * @remarks
   * Grants units to the wallet, or debits units from it, depending on `kind`. `amount` is always
   * sent positive, and `kind` determines the direction written to the ledger.
   *
   * **`kind: grant`**: a one-time manual top-up. On a non-negative balance, this creates a grant
   * and writes one ledger row. On a negative balance, it repays the overdraft first (a `kind:
   * grant` row with `grant_id: null`, for the repaid amount), then creates the grant: its
   * `original` is always the full `amount` sent, and its `remaining` is what's left after the
   * overdraft was repaid, which is `0` if the overdraft absorbed the whole top-up. The grant row is
   * still written, and its `amount` is that `remaining`, not `original`, so the ledger rows sum to
   * the balance change. A grant may carry `expires_at`; a debit may not.
   *
   * **`kind: debit`**: direct consumption. Drains grants earliest-expiration-first, one `kind:
   * debit` row per grant touched, plus any overdue expiration rows this same call triggers first
   * (see below):
   * - Under the wallet's default `hard_stop_overflow: discard`, the drain is capped at the
   *   available balance. For a metered wallet, that cap is the live metered balance, not the stored
   *   one, so a debit can drain less than its stored balance would suggest, or even drain nothing
   *   at all (`201` with `drained_amount: "0.0"`) if live usage has already consumed what the
   *   ledger hadn't caught up to yet. A debit against a wallet whose *stored* balance is already
   *   zero or negative (`discard` only ever reaches zero) returns `422 "Wallet is depleted"`.
   *   Before that failure is returned, this call still expires any grants that were already
   *   overdue, so a `422` response can still leave new `kind: expiration` rows written.
   * - Under `hard_stop_overflow: allow_negative`, the full amount is deducted. The excess past the
   *   wallet's grants is booked as one overdraft row with `grant_id: null`, `rejected_amount` is
   *   always `"0.0"`, and the balance goes negative.
   *
   * @returns Transaction applied. For `kind: grant`, the ledger row(s) written plus the new
   * balance. For `kind: debit`, one row per grant touched plus the requested/drained/rejected
   * accounting and the new balance.
   *
   * @throws {@link WalletTransactions.CreateWalletTransactionError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createWalletTransaction(
    request: WalletTransactions.CreateWalletTransactionRequestParams,
    options?: RequestOptions,
  ): ApiPromise<WalletTransactionResultResponse, WalletTransactions.CreateWalletTransactionError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallets/{wallet_id}/transactions.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "wallet_id", value: request.walletId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createWalletTransactionRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletTransactionResultResponseSchema },
        errorFactory: WalletTransactions.CreateWalletTransactionError,
      },
      options,
    );
  }

  /**
   * List Wallet Transactions
   *
   * @remarks
   * Lists the wallet's append-only ledger, newest first, paginated.
   *
   * @returns OK
   *
   * @throws {@link WalletTransactions.ListWalletTransactionsError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  listWalletTransactions(
    request: WalletTransactions.ListWalletTransactionsRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletTransactionsListResponse, WalletTransactions.ListWalletTransactionsError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/wallets/{wallet_id}/transactions.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "wallet_id", value: request.walletId, schema: s.int() }],
        query: [
          { name: "page", value: request.page, schema: s.defaulted(s.int(), 1) },
          { name: "per_page", value: request.perPage, schema: s.defaulted(s.int(), 20) },
        ],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: walletTransactionsListResponseSchema },
        errorFactory: WalletTransactions.ListWalletTransactionsError,
      },
      options,
    );
  }
}

export namespace WalletTransactions {
  export type CreateWalletTransactionRequestParams = {
    /** The Advanced Billing id of the wallet. */
    walletId: number;
    body?: CreateWalletTransactionRequest;
  };

  export class CreateWalletTransactionError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
      | Declared<"walletErrorResponse13", WalletErrorResponse1>
      | Declared<"walletErrorResponse14", WalletErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateWalletTransactionError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 422,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
      {
        on: 500,
        kind: "walletErrorResponse13",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
      {
        on: 503,
        kind: "walletErrorResponse14",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }

  export type ListWalletTransactionsRequest = {
    /** The Advanced Billing id of the wallet. */
    walletId: number;
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

  export class ListWalletTransactionsError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"error403", undefined> | Declared<"walletErrorResponse1", WalletErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<ListWalletTransactionsError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
    ];
  }
}
