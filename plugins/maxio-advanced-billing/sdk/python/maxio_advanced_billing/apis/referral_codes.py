from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.validate_referral_code_error import ValidateReferralCodeErrorBody, validate_referral_code_error_mapper
from ..models.referral_validation_response import ReferralValidationResponse
from ..server.server import Server


class ReferralCodes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReferralCodesWithRawResponse(client, server, auth)

    def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReferralValidationResponse:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        For more information, see `Understanding Referrals
        <https://docs.maxio.com/hc/en-us/articles/24286981223693-Understanding-Referrals>`__ in the product
        documentation.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``SingleStringErrorResponse1 | RawError``."""
        return unwrap(self._with_raw_response.validate_referral_code(code, request_options=request_options))

    @property
    def with_raw_response(self) -> ReferralCodesWithRawResponse:
        return self._with_raw_response


class AsyncReferralCodes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReferralCodesWithRawResponse(client, server, auth)

    async def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReferralValidationResponse:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        For more information, see `Understanding Referrals
        <https://docs.maxio.com/hc/en-us/articles/24286981223693-Understanding-Referrals>`__ in the product
        documentation.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``SingleStringErrorResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.validate_referral_code(code, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncReferralCodesWithRawResponse:
        return self._with_raw_response


class ReferralCodesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReferralValidationResponse, ValidateReferralCodeErrorBody]:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        For more information, see `Understanding Referrals
        <https://docs.maxio.com/hc/en-us/articles/24286981223693-Understanding-Referrals>`__ in the product
        documentation.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/referral_codes/validate.json"),
            query_params=[param[str]("code", code)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ReferralValidationResponse],
            error_mapper=validate_referral_code_error_mapper,
            request_options=request_options,
        )


class AsyncReferralCodesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def validate_referral_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReferralValidationResponse, ValidateReferralCodeErrorBody]:
        """Validates whether a referral code is valid and applicable within your site. This method is useful for
        validating referral codes that are entered by a customer.

        For more information, see `Understanding Referrals
        <https://docs.maxio.com/hc/en-us/articles/24286981223693-Understanding-Referrals>`__ in the product
        documentation.

        Args:
            code: The referral code you are trying to validate
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/referral_codes/validate.json"),
            query_params=[param[str]("code", code)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ReferralValidationResponse],
            error_mapper=validate_referral_code_error_mapper,
            request_options=request_options,
        )
