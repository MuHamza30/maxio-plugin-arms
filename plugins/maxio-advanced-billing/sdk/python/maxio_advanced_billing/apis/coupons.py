from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.create_coupon_error import CreateCouponErrorBody, create_coupon_error_mapper
from ..errors.create_or_update_coupon_currency_prices_error import (
    CreateOrUpdateCouponCurrencyPricesErrorBody,
    create_or_update_coupon_currency_prices_error_mapper,
)
from ..errors.delete_coupon_subcode_error import DeleteCouponSubcodeErrorBody, delete_coupon_subcode_error_mapper
from ..errors.update_coupon_error import UpdateCouponErrorBody, update_coupon_error_mapper
from ..errors.validate_coupon_error import ValidateCouponErrorBody, validate_coupon_error_mapper
from ..models.coupon_currency_request import CouponCurrencyRequest, CouponCurrencyRequestDict
from ..models.coupon_currency_response import CouponCurrencyResponse
from ..models.coupon_request import CouponRequest, CouponRequestDict
from ..models.coupon_response import CouponResponse
from ..models.coupon_subcodes import CouponSubcodes, CouponSubcodesDict
from ..models.coupon_subcodes_response import CouponSubcodesResponse
from ..models.coupon_usage import CouponUsage
from ..models.list_coupons_filter import ListCouponsFilter, ListCouponsFilterDict
from ..server.server import Server


class Coupons:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CouponsWithRawResponse(client, server, auth)

    def archive_coupon(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> CouponResponse:
        """Archives a coupon, making it unavailable for future use while remaining active on existing subscriptions.
        Archiving makes that Coupon unavailable for future use, but allows it to remain attached and functional on
        existing Subscriptions that are using it. The ``archived_at`` date and time will be assigned.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.archive_coupon(product_family_id, coupon_id, request_options=request_options)
        )

    def create_coupon(
        self,
        product_family_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Creates a coupon under the specified product family.

        You can create either a flat amount coupon, by specifying ``amount_in_cents``, or percentage coupon by
        specifying ``percentage``.

        See `Apply Coupons to Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__ for information on
        applying a coupon to a subscription in the Advanced Billing UI.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_coupon(product_family_id, body=body, request_options=request_options)
        )

    def create_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponSubcodesResponse:
        """Creates subcodes for an existing coupon.

        Coupon Subcodes allow you to create a set of unique codes that allow you to expand the use of one coupon.

        For example:

        Master Coupon Code:

        + SPRING2020

        Coupon Subcodes:

        + SPRING90210
        + DP80302
        + SPRINGBALTIMORE

        When creating a coupon subcode, you must specify a coupon to attach it to using the coupon_id. Valid coupon
        subcodes are all capital letters, contain only letters and numbers, and do not have any spaces. Lowercase
        letters are capitalized before the subcode is created.

        Note: If you are using any of the allowed special characters ("%", "@", "+", "-", "_", and "."), you must encode
        them for use in the URL.

            % to %25
            @ to %40
            + to %2B
            - to %2D
            _ to %5F
            . to %2E

        So, if the coupon subcode is ``20%OFF``, the URL to delete this coupon subcode would be:
        ``https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>``.

        For more information on coupon codes and applying coupons to subscriptions, see `Coupon Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24261208729229-Coupon-Codes>`__ and `Coupons and Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.create_coupon_subcodes(coupon_id, body=body, request_options=request_options)
        )

    def create_or_update_coupon_currency_prices(
        self,
        coupon_id: int,
        *,
        body: CouponCurrencyRequest | CouponCurrencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponCurrencyResponse:
        """Creates and/or updates currency prices for an existing coupon. Multiple prices can be created or updated in a
        single request but each of the currencies must be defined on the site level already and the coupon must be an
        amount-based coupon, not percentage.

        Currency pricing for coupons must mirror the setup of the primary coupon pricing - if the primary coupon is
        percentage based, you will not be able to define pricing in non-primary currencies.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorStringMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_or_update_coupon_currency_prices(
                coupon_id, body=body, request_options=request_options
            ),
        )

    def delete_coupon_subcode(
        self, coupon_id: int, subcode: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a specific subcode from a coupon.

        ## Example

        Given a coupon with an ID of 567, and a coupon subcode of 20OFF, the URL to ``DELETE`` this coupon subcode would
        be:

        ```
        http://subdomain.chargify.com/coupons/567/codes/20OFF.<format>
        ```

        Note: If you are using any of the allowed special characters (“%”, “@”, “+”, “-”, “_”, and “.”), you must encode
        them for use in the URL.

        | Special character | Encoding |
        |-------------------|----------|
        | % | %25 |
        | @ | %40 |
        | + | %2B |
        | – | %2D |
        | _ | %5F |
        | . | %2E |

        ## Percent Encoding Example

        Or if the coupon subcode is 20%OFF, the URL to delete this coupon subcode would be:
        @https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>.

        Args:
            coupon_id: The Advanced Billing id of the coupon to which the subcode belongs
            subcode: The subcode of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_coupon_subcode(coupon_id, subcode, request_options=request_options)
        )

    def find_coupon(
        self,
        *,
        product_family_id: int | None = None,
        code: str | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Searches for a coupon by code.

        If you have more than one product family and if the coupon you are trying to find does not belong to the default
        product family in your site, you need to specify (either in the URL or as a query string param) the
        ``product_family_id``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            code: The code of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.find_coupon(
                product_family_id=product_family_id,
                code=code,
                currency_prices=currency_prices,
                request_options=request_options,
            ),
        )

    def list_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponSubcodes:
        """Lists the subcodes attached to a coupon.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_coupon_subcodes(
                coupon_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    def list_coupons(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CouponResponse]:
        """Lists coupons for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_coupons(
                page=page,
                per_page=per_page,
                filter_=filter_,
                currency_prices=currency_prices,
                request_options=request_options,
            ),
        )

    def list_coupons_for_product_family(
        self,
        product_family_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CouponResponse]:
        """Lists coupons for a specific product family in a site.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_coupons_for_product_family(
                product_family_id,
                page=page,
                per_page=per_page,
                filter_=filter_,
                currency_prices=currency_prices,
                request_options=request_options,
            ),
        )

    def read_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Returns a coupon by its system-assigned ID. You must identify the Coupon in this call by the ID parameter
        assigned to it.

        If instead you would like to find a Coupon using a Coupon code, use the `Find Coupon <$e/Coupons/findCoupon>`__
        endpoint.

        If the coupon is set to ``use_site_exchange_rate: true``, it returns pricing based on the current exchange rate.
        If the flag is set to false, it returns all of the defined prices for each currency.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_coupon(
                product_family_id, coupon_id, currency_prices=currency_prices, request_options=request_options
            ),
        )

    def read_coupon_usage(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CouponUsage]:
        """Lists coupon usage details, one entry per product.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs.
            coupon_id: The Advanced Billing id of the coupon.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_coupon_usage(product_family_id, coupon_id, request_options=request_options)
        )

    def update_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Updates a coupon.

        You can restrict a coupon to only apply to specific products / components by optionally passing in hashes of
        ``restricted_products`` and/or ``restricted_components`` in the format: ``{ "<product/component_id>":
        boolean_value }``

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_coupon(
                product_family_id, coupon_id, body=body, request_options=request_options
            ),
        )

    def update_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponSubcodesResponse:
        """Updates the subcodes for a coupon, replacing all existing subcodes with the new list. Send an array of new
        coupon subcodes.

        **Note**: All current subcodes for that Coupon will be deleted first, and replaced with the list of subcodes
        sent to this endpoint. The response will contain:

        + The created subcodes,

        + Subcodes that were not created because they already exist,

        + Any subcodes not created because they are invalid.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_coupon_subcodes(coupon_id, body=body, request_options=request_options)
        )

    def validate_coupon(
        self, code: str, *, product_family_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CouponResponse:
        """Verifies whether a specific coupon code is valid. This method is useful for validating coupon codes that are
        entered by a customer.

        If you have more than one product family and if the coupon you are validating does not belong to the first
        product family in your site, you need to specify the product family, either in the URL or as a query string
        param. This can be done by supplying the id or the handle in the ``handle:my-family`` format.

        Supplying the ``product_family_handle`` in the URL:

        ```
        https://<subdomain>.chargify.com/product_families/handle:<product_family_handle>/coupons/validate.<format>?code=<coupon_code>
        ```

        Supplying the ``product_family_id`` as a query parameter:

        ```
        https://<subdomain>.chargify.com/coupons/validate.<format>?code=<coupon_code>&product_family_id=<id>
        ```

        Args:
            code: The code of the coupon
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``SingleStringErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.validate_coupon(
                code, product_family_id=product_family_id, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> CouponsWithRawResponse:
        return self._with_raw_response


class AsyncCoupons:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCouponsWithRawResponse(client, server, auth)

    async def archive_coupon(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> CouponResponse:
        """Archives a coupon, making it unavailable for future use while remaining active on existing subscriptions.
        Archiving makes that Coupon unavailable for future use, but allows it to remain attached and functional on
        existing Subscriptions that are using it. The ``archived_at`` date and time will be assigned.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.archive_coupon(product_family_id, coupon_id, request_options=request_options)
        )

    async def create_coupon(
        self,
        product_family_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Creates a coupon under the specified product family.

        You can create either a flat amount coupon, by specifying ``amount_in_cents``, or percentage coupon by
        specifying ``percentage``.

        See `Apply Coupons to Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__ for information on
        applying a coupon to a subscription in the Advanced Billing UI.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_coupon(product_family_id, body=body, request_options=request_options)
        )

    async def create_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponSubcodesResponse:
        """Creates subcodes for an existing coupon.

        Coupon Subcodes allow you to create a set of unique codes that allow you to expand the use of one coupon.

        For example:

        Master Coupon Code:

        + SPRING2020

        Coupon Subcodes:

        + SPRING90210
        + DP80302
        + SPRINGBALTIMORE

        When creating a coupon subcode, you must specify a coupon to attach it to using the coupon_id. Valid coupon
        subcodes are all capital letters, contain only letters and numbers, and do not have any spaces. Lowercase
        letters are capitalized before the subcode is created.

        Note: If you are using any of the allowed special characters ("%", "@", "+", "-", "_", and "."), you must encode
        them for use in the URL.

            % to %25
            @ to %40
            + to %2B
            - to %2D
            _ to %5F
            . to %2E

        So, if the coupon subcode is ``20%OFF``, the URL to delete this coupon subcode would be:
        ``https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>``.

        For more information on coupon codes and applying coupons to subscriptions, see `Coupon Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24261208729229-Coupon-Codes>`__ and `Coupons and Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.create_coupon_subcodes(coupon_id, body=body, request_options=request_options)
        )

    async def create_or_update_coupon_currency_prices(
        self,
        coupon_id: int,
        *,
        body: CouponCurrencyRequest | CouponCurrencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponCurrencyResponse:
        """Creates and/or updates currency prices for an existing coupon. Multiple prices can be created or updated in a
        single request but each of the currencies must be defined on the site level already and the coupon must be an
        amount-based coupon, not percentage.

        Currency pricing for coupons must mirror the setup of the primary coupon pricing - if the primary coupon is
        percentage based, you will not be able to define pricing in non-primary currencies.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorStringMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_or_update_coupon_currency_prices(
                coupon_id, body=body, request_options=request_options
            ),
        )

    async def delete_coupon_subcode(
        self, coupon_id: int, subcode: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a specific subcode from a coupon.

        ## Example

        Given a coupon with an ID of 567, and a coupon subcode of 20OFF, the URL to ``DELETE`` this coupon subcode would
        be:

        ```
        http://subdomain.chargify.com/coupons/567/codes/20OFF.<format>
        ```

        Note: If you are using any of the allowed special characters (“%”, “@”, “+”, “-”, “_”, and “.”), you must encode
        them for use in the URL.

        | Special character | Encoding |
        |-------------------|----------|
        | % | %25 |
        | @ | %40 |
        | + | %2B |
        | – | %2D |
        | _ | %5F |
        | . | %2E |

        ## Percent Encoding Example

        Or if the coupon subcode is 20%OFF, the URL to delete this coupon subcode would be:
        @https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>.

        Args:
            coupon_id: The Advanced Billing id of the coupon to which the subcode belongs
            subcode: The subcode of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_coupon_subcode(coupon_id, subcode, request_options=request_options)
        )

    async def find_coupon(
        self,
        *,
        product_family_id: int | None = None,
        code: str | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Searches for a coupon by code.

        If you have more than one product family and if the coupon you are trying to find does not belong to the default
        product family in your site, you need to specify (either in the URL or as a query string param) the
        ``product_family_id``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            code: The code of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.find_coupon(
                product_family_id=product_family_id,
                code=code,
                currency_prices=currency_prices,
                request_options=request_options,
            ),
        )

    async def list_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponSubcodes:
        """Lists the subcodes attached to a coupon.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_coupon_subcodes(
                coupon_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def list_coupons(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CouponResponse]:
        """Lists coupons for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_coupons(
                page=page,
                per_page=per_page,
                filter_=filter_,
                currency_prices=currency_prices,
                request_options=request_options,
            ),
        )

    async def list_coupons_for_product_family(
        self,
        product_family_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[CouponResponse]:
        """Lists coupons for a specific product family in a site.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_coupons_for_product_family(
                product_family_id,
                page=page,
                per_page=per_page,
                filter_=filter_,
                currency_prices=currency_prices,
                request_options=request_options,
            ),
        )

    async def read_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Returns a coupon by its system-assigned ID. You must identify the Coupon in this call by the ID parameter
        assigned to it.

        If instead you would like to find a Coupon using a Coupon code, use the `Find Coupon <$e/Coupons/findCoupon>`__
        endpoint.

        If the coupon is set to ``use_site_exchange_rate: true``, it returns pricing based on the current exchange rate.
        If the flag is set to false, it returns all of the defined prices for each currency.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_coupon(
                product_family_id, coupon_id, currency_prices=currency_prices, request_options=request_options
            ),
        )

    async def read_coupon_usage(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[CouponUsage]:
        """Lists coupon usage details, one entry per product.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs.
            coupon_id: The Advanced Billing id of the coupon.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_coupon_usage(
                product_family_id, coupon_id, request_options=request_options
            ),
        )

    async def update_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponResponse:
        """Updates a coupon.

        You can restrict a coupon to only apply to specific products / components by optionally passing in hashes of
        ``restricted_products`` and/or ``restricted_components`` in the format: ``{ "<product/component_id>":
        boolean_value }``

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_coupon(
                product_family_id, coupon_id, body=body, request_options=request_options
            ),
        )

    async def update_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CouponSubcodesResponse:
        """Updates the subcodes for a coupon, replacing all existing subcodes with the new list. Send an array of new
        coupon subcodes.

        **Note**: All current subcodes for that Coupon will be deleted first, and replaced with the list of subcodes
        sent to this endpoint. The response will contain:

        + The created subcodes,

        + Subcodes that were not created because they already exist,

        + Any subcodes not created because they are invalid.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_coupon_subcodes(coupon_id, body=body, request_options=request_options)
        )

    async def validate_coupon(
        self, code: str, *, product_family_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CouponResponse:
        """Verifies whether a specific coupon code is valid. This method is useful for validating coupon codes that are
        entered by a customer.

        If you have more than one product family and if the coupon you are validating does not belong to the first
        product family in your site, you need to specify the product family, either in the URL or as a query string
        param. This can be done by supplying the id or the handle in the ``handle:my-family`` format.

        Supplying the ``product_family_handle`` in the URL:

        ```
        https://<subdomain>.chargify.com/product_families/handle:<product_family_handle>/coupons/validate.<format>?code=<coupon_code>
        ```

        Supplying the ``product_family_id`` as a query parameter:

        ```
        https://<subdomain>.chargify.com/coupons/validate.<format>?code=<coupon_code>&product_family_id=<id>
        ```

        Args:
            code: The code of the coupon
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``SingleStringErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.validate_coupon(
                code, product_family_id=product_family_id, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCouponsWithRawResponse:
        return self._with_raw_response


class CouponsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_coupon(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CouponResponse, RawError]:
        """Archives a coupon, making it unavailable for future use while remaining active on existing subscriptions.
        Archiving makes that Coupon unavailable for future use, but allows it to remain attached and functional on
        existing Subscriptions that are using it. The ``archived_at`` date and time will be assigned.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/product_families/{product_family_id}/coupons/{coupon_id}.json"),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_coupon(
        self,
        product_family_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, CreateCouponErrorBody]:
        """Creates a coupon under the specified product family.

        You can create either a flat amount coupon, by specifying ``amount_in_cents``, or percentage coupon by
        specifying ``percentage``.

        See `Apply Coupons to Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__ for information on
        applying a coupon to a subscription in the Advanced Billing UI.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/coupons.json"),
            path_params=[param[int]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponRequest | CouponRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponResponse],
            error_mapper=create_coupon_error_mapper,
            request_options=request_options,
        )

    def create_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponSubcodesResponse, RawError]:
        """Creates subcodes for an existing coupon.

        Coupon Subcodes allow you to create a set of unique codes that allow you to expand the use of one coupon.

        For example:

        Master Coupon Code:

        + SPRING2020

        Coupon Subcodes:

        + SPRING90210
        + DP80302
        + SPRINGBALTIMORE

        When creating a coupon subcode, you must specify a coupon to attach it to using the coupon_id. Valid coupon
        subcodes are all capital letters, contain only letters and numbers, and do not have any spaces. Lowercase
        letters are capitalized before the subcode is created.

        Note: If you are using any of the allowed special characters ("%", "@", "+", "-", "_", and "."), you must encode
        them for use in the URL.

            % to %25
            @ to %40
            + to %2B
            - to %2D
            _ to %5F
            . to %2E

        So, if the coupon subcode is ``20%OFF``, the URL to delete this coupon subcode would be:
        ``https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>``.

        For more information on coupon codes and applying coupons to subscriptions, see `Coupon Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24261208729229-Coupon-Codes>`__ and `Coupons and Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/coupons/{coupon_id}/codes.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponSubcodes | CouponSubcodesDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponSubcodesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_or_update_coupon_currency_prices(
        self,
        coupon_id: int,
        *,
        body: CouponCurrencyRequest | CouponCurrencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponCurrencyResponse, CreateOrUpdateCouponCurrencyPricesErrorBody]:
        """Creates and/or updates currency prices for an existing coupon. Multiple prices can be created or updated in a
        single request but each of the currencies must be defined on the site level already and the coupon must be an
        amount-based coupon, not percentage.

        Currency pricing for coupons must mirror the setup of the primary coupon pricing - if the primary coupon is
        percentage based, you will not be able to define pricing in non-primary currencies.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/coupons/{coupon_id}/currency_prices.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponCurrencyRequest | CouponCurrencyRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponCurrencyResponse],
            error_mapper=create_or_update_coupon_currency_prices_error_mapper,
            request_options=request_options,
        )

    def delete_coupon_subcode(
        self, coupon_id: int, subcode: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCouponSubcodeErrorBody]:
        """Deletes a specific subcode from a coupon.

        ## Example

        Given a coupon with an ID of 567, and a coupon subcode of 20OFF, the URL to ``DELETE`` this coupon subcode would
        be:

        ```
        http://subdomain.chargify.com/coupons/567/codes/20OFF.<format>
        ```

        Note: If you are using any of the allowed special characters (“%”, “@”, “+”, “-”, “_”, and “.”), you must encode
        them for use in the URL.

        | Special character | Encoding |
        |-------------------|----------|
        | % | %25 |
        | @ | %40 |
        | + | %2B |
        | – | %2D |
        | _ | %5F |
        | . | %2E |

        ## Percent Encoding Example

        Or if the coupon subcode is 20%OFF, the URL to delete this coupon subcode would be:
        @https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>.

        Args:
            coupon_id: The Advanced Billing id of the coupon to which the subcode belongs
            subcode: The subcode of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/coupons/{coupon_id}/codes/{subcode}.json"),
            path_params=[param[int]("coupon_id", coupon_id), param[str]("subcode", subcode)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_coupon_subcode_error_mapper,
            request_options=request_options,
        )

    def find_coupon(
        self,
        *,
        product_family_id: int | None = None,
        code: str | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, RawError]:
        """Searches for a coupon by code.

        If you have more than one product family and if the coupon you are trying to find does not belong to the default
        product family in your site, you need to specify (either in the URL or as a query string param) the
        ``product_family_id``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            code: The code of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons/find.json"),
            query_params=[
                param[int | None]("product_family_id", product_family_id),
                param[str | None]("code", code),
                param[bool | None]("currency_prices", currency_prices),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponSubcodes, RawError]:
        """Lists the subcodes attached to a coupon.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons/{coupon_id}/codes.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponSubcodes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_coupons(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CouponResponse], RawError]:
        """Lists coupons for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListCouponsFilter | ListCouponsFilterDict | None]("filter", filter_),
                param[bool | None]("currency_prices", currency_prices),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[CouponResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_coupons_for_product_family(
        self,
        product_family_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CouponResponse], RawError]:
        """Lists coupons for a specific product family in a site.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/coupons.json"),
            path_params=[param[int]("product_family_id", product_family_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListCouponsFilter | ListCouponsFilterDict | None]("filter", filter_),
                param[bool | None]("currency_prices", currency_prices),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[CouponResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, RawError]:
        """Returns a coupon by its system-assigned ID. You must identify the Coupon in this call by the ID parameter
        assigned to it.

        If instead you would like to find a Coupon using a Coupon code, use the `Find Coupon <$e/Coupons/findCoupon>`__
        endpoint.

        If the coupon is set to ``use_site_exchange_rate: true``, it returns pricing based on the current exchange rate.
        If the flag is set to false, it returns all of the defined prices for each currency.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/coupons/{coupon_id}.json"),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            query_params=[param[bool | None]("currency_prices", currency_prices)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_coupon_usage(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CouponUsage], RawError]:
        """Lists coupon usage details, one entry per product.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs.
            coupon_id: The Advanced Billing id of the coupon.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/product_families/{product_family_id}/coupons/{coupon_id}/usage.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[CouponUsage]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, UpdateCouponErrorBody]:
        """Updates a coupon.

        You can restrict a coupon to only apply to specific products / components by optionally passing in hashes of
        ``restricted_products`` and/or ``restricted_components`` in the format: ``{ "<product/component_id>":
        boolean_value }``

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/product_families/{product_family_id}/coupons/{coupon_id}.json"),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponRequest | CouponRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponResponse],
            error_mapper=update_coupon_error_mapper,
            request_options=request_options,
        )

    def update_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponSubcodesResponse, RawError]:
        """Updates the subcodes for a coupon, replacing all existing subcodes with the new list. Send an array of new
        coupon subcodes.

        **Note**: All current subcodes for that Coupon will be deleted first, and replaced with the list of subcodes
        sent to this endpoint. The response will contain:

        + The created subcodes,

        + Subcodes that were not created because they already exist,

        + Any subcodes not created because they are invalid.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/coupons/{coupon_id}/codes.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponSubcodes | CouponSubcodesDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponSubcodesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def validate_coupon(
        self, code: str, *, product_family_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CouponResponse, ValidateCouponErrorBody]:
        """Verifies whether a specific coupon code is valid. This method is useful for validating coupon codes that are
        entered by a customer.

        If you have more than one product family and if the coupon you are validating does not belong to the first
        product family in your site, you need to specify the product family, either in the URL or as a query string
        param. This can be done by supplying the id or the handle in the ``handle:my-family`` format.

        Supplying the ``product_family_handle`` in the URL:

        ```
        https://<subdomain>.chargify.com/product_families/handle:<product_family_handle>/coupons/validate.<format>?code=<coupon_code>
        ```

        Supplying the ``product_family_id`` as a query parameter:

        ```
        https://<subdomain>.chargify.com/coupons/validate.<format>?code=<coupon_code>&product_family_id=<id>
        ```

        Args:
            code: The code of the coupon
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons/validate.json"),
            query_params=[param[str]("code", code), param[int | None]("product_family_id", product_family_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CouponResponse],
            error_mapper=validate_coupon_error_mapper,
            request_options=request_options,
        )


class AsyncCouponsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_coupon(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CouponResponse, RawError]:
        """Archives a coupon, making it unavailable for future use while remaining active on existing subscriptions.
        Archiving makes that Coupon unavailable for future use, but allows it to remain attached and functional on
        existing Subscriptions that are using it. The ``archived_at`` date and time will be assigned.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/product_families/{product_family_id}/coupons/{coupon_id}.json"),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_coupon(
        self,
        product_family_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, CreateCouponErrorBody]:
        """Creates a coupon under the specified product family.

        You can create either a flat amount coupon, by specifying ``amount_in_cents``, or percentage coupon by
        specifying ``percentage``.

        See `Apply Coupons to Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__ for information on
        applying a coupon to a subscription in the Advanced Billing UI.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/coupons.json"),
            path_params=[param[int]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponRequest | CouponRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponResponse],
            error_mapper=create_coupon_error_mapper,
            request_options=request_options,
        )

    async def create_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponSubcodesResponse, RawError]:
        """Creates subcodes for an existing coupon.

        Coupon Subcodes allow you to create a set of unique codes that allow you to expand the use of one coupon.

        For example:

        Master Coupon Code:

        + SPRING2020

        Coupon Subcodes:

        + SPRING90210
        + DP80302
        + SPRINGBALTIMORE

        When creating a coupon subcode, you must specify a coupon to attach it to using the coupon_id. Valid coupon
        subcodes are all capital letters, contain only letters and numbers, and do not have any spaces. Lowercase
        letters are capitalized before the subcode is created.

        Note: If you are using any of the allowed special characters ("%", "@", "+", "-", "_", and "."), you must encode
        them for use in the URL.

            % to %25
            @ to %40
            + to %2B
            - to %2D
            _ to %5F
            . to %2E

        So, if the coupon subcode is ``20%OFF``, the URL to delete this coupon subcode would be:
        ``https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>``.

        For more information on coupon codes and applying coupons to subscriptions, see `Coupon Codes
        <https://maxio.zendesk.com/hc/en-us/articles/24261208729229-Coupon-Codes>`__ and `Coupons and Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions>`__.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/coupons/{coupon_id}/codes.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponSubcodes | CouponSubcodesDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponSubcodesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_or_update_coupon_currency_prices(
        self,
        coupon_id: int,
        *,
        body: CouponCurrencyRequest | CouponCurrencyRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponCurrencyResponse, CreateOrUpdateCouponCurrencyPricesErrorBody]:
        """Creates and/or updates currency prices for an existing coupon. Multiple prices can be created or updated in a
        single request but each of the currencies must be defined on the site level already and the coupon must be an
        amount-based coupon, not percentage.

        Currency pricing for coupons must mirror the setup of the primary coupon pricing - if the primary coupon is
        percentage based, you will not be able to define pricing in non-primary currencies.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/coupons/{coupon_id}/currency_prices.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponCurrencyRequest | CouponCurrencyRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponCurrencyResponse],
            error_mapper=create_or_update_coupon_currency_prices_error_mapper,
            request_options=request_options,
        )

    async def delete_coupon_subcode(
        self, coupon_id: int, subcode: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCouponSubcodeErrorBody]:
        """Deletes a specific subcode from a coupon.

        ## Example

        Given a coupon with an ID of 567, and a coupon subcode of 20OFF, the URL to ``DELETE`` this coupon subcode would
        be:

        ```
        http://subdomain.chargify.com/coupons/567/codes/20OFF.<format>
        ```

        Note: If you are using any of the allowed special characters (“%”, “@”, “+”, “-”, “_”, and “.”), you must encode
        them for use in the URL.

        | Special character | Encoding |
        |-------------------|----------|
        | % | %25 |
        | @ | %40 |
        | + | %2B |
        | – | %2D |
        | _ | %5F |
        | . | %2E |

        ## Percent Encoding Example

        Or if the coupon subcode is 20%OFF, the URL to delete this coupon subcode would be:
        @https://<subdomain>.chargify.com/coupons/567/codes/20%25OFF.<format>.

        Args:
            coupon_id: The Advanced Billing id of the coupon to which the subcode belongs
            subcode: The subcode of the coupon
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/coupons/{coupon_id}/codes/{subcode}.json"),
            path_params=[param[int]("coupon_id", coupon_id), param[str]("subcode", subcode)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_coupon_subcode_error_mapper,
            request_options=request_options,
        )

    async def find_coupon(
        self,
        *,
        product_family_id: int | None = None,
        code: str | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, RawError]:
        """Searches for a coupon by code.

        If you have more than one product family and if the coupon you are trying to find does not belong to the default
        product family in your site, you need to specify (either in the URL or as a query string param) the
        ``product_family_id``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            code: The code of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons/find.json"),
            query_params=[
                param[int | None]("product_family_id", product_family_id),
                param[str | None]("code", code),
                param[bool | None]("currency_prices", currency_prices),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponSubcodes, RawError]:
        """Lists the subcodes attached to a coupon.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons/{coupon_id}/codes.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponSubcodes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_coupons(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CouponResponse], RawError]:
        """Lists coupons for a site.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListCouponsFilter | ListCouponsFilterDict | None]("filter", filter_),
                param[bool | None]("currency_prices", currency_prices),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[CouponResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_coupons_for_product_family(
        self,
        product_family_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 30,
        filter_: ListCouponsFilter | ListCouponsFilterDict | None = None,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[CouponResponse], RawError]:
        """Lists coupons for a specific product family in a site.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 30. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Coupons operations
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response. Use in query
                ``currency_prices=true``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/coupons.json"),
            path_params=[param[int]("product_family_id", product_family_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListCouponsFilter | ListCouponsFilterDict | None]("filter", filter_),
                param[bool | None]("currency_prices", currency_prices),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[CouponResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        currency_prices: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, RawError]:
        """Returns a coupon by its system-assigned ID. You must identify the Coupon in this call by the ID parameter
        assigned to it.

        If instead you would like to find a Coupon using a Coupon code, use the `Find Coupon <$e/Coupons/findCoupon>`__
        endpoint.

        If the coupon is set to ``use_site_exchange_rate: true``, it returns pricing based on the current exchange rate.
        If the flag is set to false, it returns all of the defined prices for each currency.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            currency_prices: (Optional) If you have defined multiple currencies at the site level, you can pass
                ``?currency_prices=true`` to include an array of currency price data in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/coupons/{coupon_id}.json"),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            query_params=[param[bool | None]("currency_prices", currency_prices)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_coupon_usage(
        self, product_family_id: int, coupon_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[CouponUsage], RawError]:
        """Lists coupon usage details, one entry per product.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs.
            coupon_id: The Advanced Billing id of the coupon.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/product_families/{product_family_id}/coupons/{coupon_id}/usage.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[CouponUsage]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_coupon(
        self,
        product_family_id: int,
        coupon_id: int,
        *,
        body: CouponRequest | CouponRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponResponse, UpdateCouponErrorBody]:
        """Updates a coupon.

        You can restrict a coupon to only apply to specific products / components by optionally passing in hashes of
        ``restricted_products`` and/or ``restricted_components`` in the format: ``{ "<product/component_id>":
        boolean_value }``

        Args:
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/product_families/{product_family_id}/coupons/{coupon_id}.json"),
            path_params=[param[int]("product_family_id", product_family_id), param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponRequest | CouponRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponResponse],
            error_mapper=update_coupon_error_mapper,
            request_options=request_options,
        )

    async def update_coupon_subcodes(
        self,
        coupon_id: int,
        *,
        body: CouponSubcodes | CouponSubcodesDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CouponSubcodesResponse, RawError]:
        """Updates the subcodes for a coupon, replacing all existing subcodes with the new list. Send an array of new
        coupon subcodes.

        **Note**: All current subcodes for that Coupon will be deleted first, and replaced with the list of subcodes
        sent to this endpoint. The response will contain:

        + The created subcodes,

        + Subcodes that were not created because they already exist,

        + Any subcodes not created because they are invalid.

        Args:
            coupon_id: The Advanced Billing id of the coupon
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/coupons/{coupon_id}/codes.json"),
            path_params=[param[int]("coupon_id", coupon_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CouponSubcodes | CouponSubcodesDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponSubcodesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def validate_coupon(
        self, code: str, *, product_family_id: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CouponResponse, ValidateCouponErrorBody]:
        """Verifies whether a specific coupon code is valid. This method is useful for validating coupon codes that are
        entered by a customer.

        If you have more than one product family and if the coupon you are validating does not belong to the first
        product family in your site, you need to specify the product family, either in the URL or as a query string
        param. This can be done by supplying the id or the handle in the ``handle:my-family`` format.

        Supplying the ``product_family_handle`` in the URL:

        ```
        https://<subdomain>.chargify.com/product_families/handle:<product_family_handle>/coupons/validate.<format>?code=<coupon_code>
        ```

        Supplying the ``product_family_id`` as a query parameter:

        ```
        https://<subdomain>.chargify.com/coupons/validate.<format>?code=<coupon_code>&product_family_id=<id>
        ```

        Args:
            code: The code of the coupon
            product_family_id: The Advanced Billing id of the product family to which the coupon belongs
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/coupons/validate.json"),
            query_params=[param[str]("code", code), param[int | None]("product_family_id", product_family_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CouponResponse],
            error_mapper=validate_coupon_error_mapper,
            request_options=request_options,
        )
