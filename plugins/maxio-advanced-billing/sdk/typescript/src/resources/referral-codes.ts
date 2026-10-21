import type { AuthSchemes } from "../auth-schemes.js";
import { ApiError, type Declared, type ErrorDecoders, type ErrorPayload } from "../core/api-error.js";
import type { ApiPromise } from "../core/api-promise.js";
import type { RequestOptions } from "../core/api-request.js";
import type { RawClient } from "../core/raw-client.js";
import * as s from "../core/validation/index.js";
import {
  referralValidationResponseSchema,
  type ReferralValidationResponse,
} from "../models/referral-validation-response.js";
import {
  singleStringErrorResponse1Schema,
  type SingleStringErrorResponse1,
} from "../models/single-string-error-response1.js";
import type { Servers } from "../servers.js";

export class ReferralCodes {
  readonly #rawClient: RawClient;
  readonly #servers: Servers;
  readonly #auth: AuthSchemes;

  constructor(rawClient: RawClient, servers: Servers, auth: AuthSchemes) {
    this.#rawClient = rawClient;
    this.#servers = servers;
    this.#auth = auth;
  }

  /**
   * Validate Referral Code
   *
   * @remarks
   * Validates whether a referral code is valid and applicable within your site. This method is
   * useful for validating referral codes that are entered by a customer.
   *
   * For more information, see [Understanding
   * Referrals](https://docs.maxio.com/hc/en-us/articles/24286981223693-Understanding-Referrals) in
   * the product documentation.
   *
   * @returns OK
   *
   * @throws {@link ReferralCodes.ValidateReferralCodeError} when the API answers with an error
   * status — narrow on `err.payload.kind`
   *
   * @throws {@link MaxioAdvancedBillingError} when no usable response was produced: a connection
   * failure, a timeout, a body that would not decode, a value that would not encode, or a
   * credential that could not be obtained
   */
  validateReferralCode(
    request: ReferralCodes.ValidateReferralCodeRequest,
    options?: RequestOptions,
  ): ApiPromise<ReferralValidationResponse, ReferralCodes.ValidateReferralCodeError> {
    return this.#rawClient.execute(
      {
        method: "GET",
        urlTemplate: this.#servers.production("/referral_codes/validate.json"),
        auth: this.#auth.basicAuth,
        pathParams: [],
        query: [{ name: "code", value: request.code, schema: s.string() }],
        headers: [],
        body: { kind: "empty" },
      },
      {
        success: { kind: "json", schema: referralValidationResponseSchema },
        errorFactory: ReferralCodes.ValidateReferralCodeError,
      },
      options,
    );
  }
}

export namespace ReferralCodes {
  export type ValidateReferralCodeRequest = {
    /** The referral code you are trying to validate */
    code: string;
  };

  export class ValidateReferralCodeError extends ApiError {
    declare readonly payload: ErrorPayload<
      Declared<"singleStringErrorResponse1", SingleStringErrorResponse1>
    >;

    static readonly errors: ErrorDecoders<ValidateReferralCodeError> = [
      {
        on: 404,
        kind: "singleStringErrorResponse1",
        decode: { kind: "json", schema: singleStringErrorResponse1Schema },
      },
    ];
  }
}
