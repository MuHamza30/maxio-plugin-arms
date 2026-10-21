import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import { uuid } from "../core/uuid.js";
import * as s from "../core/validation/index.js";
import {
  createWalletPurchaseRequestSchema,
  type CreateWalletPurchaseRequest,
} from "../models/create-wallet-purchase-request.js";
import { walletErrorResponse1Schema, type WalletErrorResponse1 } from "../models/wallet-error-response1.js";
import {
  walletPurchasePreviewResponseSchema,
  type WalletPurchasePreviewResponse,
} from "../models/wallet-purchase-preview-response.js";
import {
  walletPurchaseResultResponseSchema,
  type WalletPurchaseResultResponse,
} from "../models/wallet-purchase-result-response.js";
import type { Servers } from "../servers.js";

export class WalletPurchases {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Create Wallet Purchase
   *
   * @remarks
   * Purchases prepaid units for the wallet and charges the subscription's payment method for them,
   * using the wallet's `price_point_id` unless a different price point is named. A successful
   * purchase writes a grant of origin `purchase`, with its expiration following the funding
   * entitlement's grant expiration policy.
   *
   * How "charged" works depends on the subscription's collection method. For card/automatic
   * collection, the payment is attempted immediately; a decline writes nothing to the wallet, and
   * the call fails with a `422` naming the gateway's decline reason. For invoice-billed
   * (remittance) subscriptions, there's no immediate charge to decline: an invoice is drafted, the
   * wallet is credited right away, and the invoice is issued afterward. If issuing the invoice
   * fails at that point, the invoice is left in draft state and reported for follow-up, but the
   * call still returns `201` and the units already credited are **not** rolled back. See [Preview
   * Wallet Purchase]($e/Wallet%20Purchases/previewWalletPurchase) to quote a price before charging
   * anything.
   *
   * @returns Purchase completed. Charges the subscription's payment method and, once payment
   * succeeds, credits the wallet.
   *
   * @throws {@link WalletPurchases.CreateWalletPurchaseError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  createWalletPurchase(
    request: WalletPurchases.CreateWalletPurchaseRequestParams,
    options?: RequestOptions,
  ): ApiPromise<WalletPurchaseResultResponse, WalletPurchases.CreateWalletPurchaseError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallets/{wallet_id}/purchases.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "wallet_id", value: request.walletId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createWalletPurchaseRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletPurchaseResultResponseSchema },
        errorFactory: WalletPurchases.CreateWalletPurchaseError,
      },
      options,
    );
  }

  /**
   * Preview Wallet Purchase
   *
   * @remarks
   * Quotes the price for a purchase at the given quantity and price point, without charging the
   * payment method or writing to the wallet. Takes the same parameters as [Create Wallet
   * Purchase]($e/Wallet%20Purchases/createWalletPurchase).
   *
   * @returns A price quote. Charges nothing and writes nothing to the wallet.
   *
   * @throws {@link WalletPurchases.PreviewWalletPurchaseError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  previewWalletPurchase(
    request: WalletPurchases.PreviewWalletPurchaseRequest,
    options?: RequestOptions,
  ): ApiPromise<WalletPurchasePreviewResponse, WalletPurchases.PreviewWalletPurchaseError> {
    return this.#rawClient.execute(
      {
        method: "POST",
        urlTemplate: this.#servers.production("/wallets/{wallet_id}/purchases/preview.json"),
        auth: this.#auth.basicAuth,
        pathParams: [{ name: "wallet_id", value: request.walletId, schema: s.int() }],
        query: [],
        headers: [{ name: "Idempotency-Key", value: uuid(), schema: s.string() }],
        body: {
          kind: "json",
          value: request.body,
          schema: s.optional(s.lazy(() => createWalletPurchaseRequestSchema)),
        },
      },
      {
        success: { kind: "json", schema: walletPurchasePreviewResponseSchema },
        errorFactory: WalletPurchases.PreviewWalletPurchaseError,
      },
      options,
    );
  }
}

export namespace WalletPurchases {
  export type CreateWalletPurchaseRequestParams = {
    /** The Advanced Billing id of the wallet. */
    walletId: number;
    body?: CreateWalletPurchaseRequest;
  };

  export class CreateWalletPurchaseError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<CreateWalletPurchaseError> = [
      { on: 403, kind: "error403", decode: { kind: "empty" } },
      { on: 404, kind: "walletErrorResponse1", decode: { kind: "json", schema: walletErrorResponse1Schema } },
      {
        on: 422,
        kind: "walletErrorResponse12",
        decode: { kind: "json", schema: walletErrorResponse1Schema },
      },
    ];
  }

  export type PreviewWalletPurchaseRequest = {
    /** The Advanced Billing id of the wallet. */
    walletId: number;
    body?: CreateWalletPurchaseRequest;
  };

  export class PreviewWalletPurchaseError extends ApiError {
    declare readonly payload: ErrorPayload<
      | Declared<"error403", undefined>
      | Declared<"walletErrorResponse1", WalletErrorResponse1>
      | Declared<"walletErrorResponse12", WalletErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<PreviewWalletPurchaseError> = [
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
