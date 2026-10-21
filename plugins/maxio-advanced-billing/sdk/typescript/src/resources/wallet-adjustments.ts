import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type Undeclared } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import type { ErrorDecoders } from "../core/response-decoder.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createWalletAdjustmentRequestSchema,
  type CreateWalletAdjustmentRequest,
} from "../models/create-wallet-adjustment-request.js";
import { walletErrorResponse1Schema, type WalletErrorResponse1 } from "../models/wallet-error-response1.js";
import {
  walletGrantResultResponseSchema,
  type WalletGrantResultResponse,
} from "../models/wallet-grant-result-response.js";
import type { Servers } from "../servers.js";

/**
 * Wallet Adjustments post a signed correction against a specific grant, or against an overdraft, on
 * a wallet's ledger. Adjustments are intended for support and operations corrections, and each
 * adjustment requires a reason that is recorded on the ledger. For more information, see
 * [Understand Wallets](https://docs.maxio.com/billing/catalog/wallets/understand-wallets).
 */
export class WalletAdjustments {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Wallet Adjustment
   *
   * @remarks
   * Posts a signed correction against a specific grant (or, for an overdraft entry, against the
   * overdraft): positive adds units to the grant, negative removes them. `reason` is required and
   * is written to the ledger row's `memo`. Writes exactly one ledger row, of kind `adjustment`.
   *
   * Use `source_transaction_id` to name a specific `debit` row when you're correcting one recorded
   * consumption rather than the grant's balance as a whole. When it names a grant-attributed debit,
   * it's recorded for audit only: naming it doesn't change how `amount` is applied, and more than
   * one adjustment may name the same row. When it names an overdraft entry, it switches the
   * correction to the overdraft path described below.
   *
   * An overdraft entry (a `debit` row with no `grant_id`, written when an `allow_negative` wallet
   * consumes past its grants) can be corrected without a `grant_id`. That correction is
   * credit-only, credits no grant, and is bounded by the usage the entry still records and by the
   * overdraft the wallet still owes. Once a later grant has repaid the overdraft, correct that
   * grant's balance instead.
   *
   * An adjustment corrects the ledger, so it works on the grant's recorded remainder,
   * `posted_remaining`, not on `remaining`, which on a metered wallet read through [Read
   * Wallet]($e/Wallets/readWallet) also subtracts usage not yet posted. Send `posted_remaining`
   * back as `expected_remaining`; sending `remaining` on a metered wallet with pending usage
   * returns `409`.
   *
   * `expected_remaining` and `expected_source_corrections` are optional optimistic-concurrency
   * checks; see their field descriptions. Use them when the correction's `amount` was derived from
   * a value read earlier that might have moved since.
   *
   * @returns The ledger row written, plus the wallet's new balance.
   *
   * @throws {@link WalletAdjustments.CreateWalletAdjustmentError} when the API answers with an
   * error status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createWalletAdjustment(
    request: WalletAdjustments.CreateWalletAdjustmentRequestParams,
    options?: RequestOptions,
  ): ApiPromise<WalletGrantResultResponse, WalletAdjustments.CreateWalletAdjustmentError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallets/{wallet_id}/adjustments.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "wallet_id", value: request.walletId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createWalletAdjustmentRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletGrantResultResponseSchema },
        errorFactory: WalletAdjustments.CreateWalletAdjustmentError,
      },
      options,
    );
  }
}

export namespace WalletAdjustments {
  export type CreateWalletAdjustmentRequestParams = {
    /** The Advanced Billing id of the wallet. */
    walletId: number;
    body?: CreateWalletAdjustmentRequest;
  };

  export class CreateWalletAdjustmentError extends ApiError {
    declare readonly payload:
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
      | Declared<"walletErrorResponse13", WalletErrorResponse1>
      | Undeclared;

    static readonly errors: ErrorDecoders<CreateWalletAdjustmentError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 409,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
      {
        on: 422,
        kind: "walletErrorResponse13",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }
}
