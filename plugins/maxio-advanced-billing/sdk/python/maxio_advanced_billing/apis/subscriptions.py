from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
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
from ..errors.activate_subscription_error import ActivateSubscriptionErrorBody, activate_subscription_error_mapper
from ..errors.apply_coupons_to_subscription_error import (
    ApplyCouponsToSubscriptionErrorBody,
    apply_coupons_to_subscription_error_mapper,
)
from ..errors.create_subscription_error import CreateSubscriptionErrorBody, create_subscription_error_mapper
from ..errors.find_subscription_error import FindSubscriptionErrorBody, find_subscription_error_mapper
from ..errors.override_subscription_error import OverrideSubscriptionErrorBody, override_subscription_error_mapper
from ..errors.purge_subscription_error import PurgeSubscriptionErrorBody, purge_subscription_error_mapper
from ..errors.remove_coupon_from_subscription_error import (
    RemoveCouponFromSubscriptionErrorBody,
    remove_coupon_from_subscription_error_mapper,
)
from ..errors.update_prepaid_subscription_configuration_error import (
    UpdatePrepaidSubscriptionConfigurationErrorBody,
    update_prepaid_subscription_configuration_error_mapper,
)
from ..errors.update_subscription_error import UpdateSubscriptionErrorBody, update_subscription_error_mapper
from ..models.activate_subscription_request import ActivateSubscriptionRequest, ActivateSubscriptionRequestDict
from ..models.add_coupons_request import AddCouponsRequest, AddCouponsRequestDict
from ..models.create_subscription_request import CreateSubscriptionRequest, CreateSubscriptionRequestDict
from ..models.enums.collection_method1 import CollectionMethod1OrStr
from ..models.enums.group_status import GroupStatusOrStr
from ..models.enums.q_scope import QScopeOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.enums.subscription_date_field import SubscriptionDateFieldOrStr
from ..models.enums.subscription_include import SubscriptionIncludeOrStr
from ..models.enums.subscription_list_include import SubscriptionListIncludeOrStr
from ..models.enums.subscription_purge_type import SubscriptionPurgeTypeOrStr
from ..models.enums.subscription_sort import SubscriptionSort, SubscriptionSortOrStr
from ..models.enums.subscription_state_filter import SubscriptionStateFilterOrStr
from ..models.override_subscription_request import OverrideSubscriptionRequest, OverrideSubscriptionRequestDict
from ..models.prepaid_configuration_response import PrepaidConfigurationResponse
from ..models.subscription_preview_response import SubscriptionPreviewResponse
from ..models.subscription_response import SubscriptionResponse
from ..models.unions.product1 import Product1, Product1Dict
from ..models.update_subscription_request import UpdateSubscriptionRequest, UpdateSubscriptionRequestDict
from ..models.upsert_prepaid_configuration_request import (
    UpsertPrepaidConfigurationRequest,
    UpsertPrepaidConfigurationRequestDict,
)
from ..server.server import Server


class Subscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionsWithRawResponse(client, server, auth)

    def activate_subscription(
        self,
        subscription_id: int,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Activates awaiting signup and trialing subscriptions. This feature is only available on the Relationship
        Invoicing architecture. Subscriptions in a group cannot be activated immediately.

        The ``revert_on_failure`` parameter controls the behavior upon activation failure.
        - If set to ``true`` and something goes wrong i.e. payment fails, the subscription's state does not change. The
            subscription’s billing period also remains the same.
        - If set to ``false`` and something goes wrong i.e. payment fails, the activation continues and enters an end of
            life state. For trialing subscriptions, that is either trial ended (if the trial is no obligation), past due
            (if the trial has an obligation), or canceled (if the site has no dunning strategy, or has a strategy that
            says to cancel immediately). For awaiting signup subscriptions, that is always canceled.

        The default activation failure behavior can be configured per activation attempt, or you can set a default value
        under Config > Settings > Subscription Activation Settings.

        ## Activation Scenarios

        ### Activate Awaiting Signup subscription

        - Given you have a product without trial
        - Given you have a site without dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Active
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| Canceled
        ```

        - Given you have a product with trial
        - Given you have a site with dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Trialing
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| PD[Past Due]
        ```

        ### Activate Trialing subscription

        For more information about the behavior of trialing subscriptions, see `Trialing Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trialing-Subscriptions>`__. When the
        ``revert_on_failure`` parameter is set to ``true``, the subscription's state remains Trialing; the invoice from
        activation is voided, and any prepayments and credits applied to the invoice are returned to the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.activate_subscription(subscription_id, body=body, request_options=request_options)
        )

    def apply_coupons_to_subscription(
        self,
        subscription_id: int,
        *,
        code: str | None = None,
        body: AddCouponsRequest | AddCouponsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Applies one or more coupon codes to an existing subscription.

        An existing subscription can accommodate multiple discounts/coupon codes. This is only applicable if each coupon
        is stackable. For more information on stackable coupons, we recommend reviewing our `coupon documentation.
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#stackability-rules>`__

        ## Query Parameters vs Request Body Parameters

        Passing in a coupon code as a query parameter will add the code to the subscription, completely replacing all
        existing coupon codes on the subscription.

        For this reason, using this query parameter on this endpoint has been deprecated in favor of using the request
        body parameters as described below. When passing in request body parameters, the list of coupon codes will
        simply be added to any existing list of codes on the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            code: A code for the coupon that would be applied to a subscription
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionAddCouponError1 | RawError``."""
        return unwrap(
            self._with_raw_response.apply_coupons_to_subscription(
                subscription_id, code=code, body=body, request_options=request_options
            ),
        )

    def create_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Creates a Subscription for a customer and product.

        Specify the product with ``product_id`` or ``product_handle``. To set a specific product price point, use
        ``product_price_point_handle`` or ``product_price_point_id``.

        Identify an existing customer with ``customer_id`` or ``customer_reference``. Optionally, include an existing
        payment profile using ``payment_profile_id``. To create a new customer, pass customer_attributes.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating subscriptions.

        ## List vs Sales Pricing

        When a subscription uses custom pricing as the sales price, you can optionally provide a list price for any
        item. If omitted, the list price defaults to the sales price. The difference between the list price and sales
        price is used to calculate implicit discounts, which appear on Invoices and in reporting. List price can also
        support revenue allocations in `Advanced Revenue
        <https://docs.maxio.com/hc/en-us/articles/24177001342861-Create-and-Configure-RevenueBooks>`__.

        If your site has list pricing enabled, the API accepts ``custom_price.list_price_point_id`` for custom pricing,
        validates and persists it, and returns list price metadata in subscription responses. If list pricing is
        disabled, this input is ignored and related response fields are omitted.

        When list pricing is enabled:

        - Subscription → Product ``product_price_point_list_price_point_id`` (integer)
        - ``product_price_point_list_price_point_handle`` (string)
        - Subscription Components (when components are included in the response, such as with subscriptions built from
            components or component serialization paths) ``component_id`` (integer)
        - ``price_point_id`` (integer)
        - ``list_price_point_id`` (integer)

        When list pricing is disabled:

        - Subscription → Product ``product_price_point_list_price_point_id``: omitted
        - ``product_price_point_list_price_point_handle``: omitted
        - Subscription Components ``list_price_point_id``: omitted

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)
        - a configured metered component

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters. See the `Subscription Signups <page:introduction/basic-concepts/subscription-signup>`__
        article for more information on working with subscriptions in Advanced Billing.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_subscription(body=body, request_options=request_options))

    def find_subscription(
        self, *, reference: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Finds a subscription by its reference.

        Args:
            reference: Subscription reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.find_subscription(reference=reference, request_options=request_options))

    def list_subscriptions(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: SubscriptionSortOrStr | None = SubscriptionSort.SIGNUP_DATE,
        direction: SortingDirectionOrStr | None = None,
        state: SubscriptionStateFilterOrStr | None = None,
        product: Product1 | Product1Dict | None = None,
        q: str | None = None,
        q_scope: QScopeOrStr | None = None,
        customer_id: int | None = None,
        product_price_point_id: int | None = None,
        coupon: int | None = None,
        coupon_code: str | None = None,
        collection_method: CollectionMethod1OrStr | None = None,
        branding_theme_id: int | None = None,
        date_field: SubscriptionDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        metadata: dict[str, str] | None = None,
        group_status: GroupStatusOrStr | None = None,
        dunning_exemption: bool | None = None,
        payment_gateways: str | None = None,
        currencies: str | None = None,
        include: list[SubscriptionListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SubscriptionResponse]:
        """Lists subscriptions for a site. Use the query string filters and pagination to control responses from the
        server.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Search for a subscription

        Use the query strings below to search for a subscription using the criteria available. The return value will be
        an array.

        ## Self-Service Page token

        Self-Service Page token for the subscriptions is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            state: The current state of the subscription
            product: Filter subscriptions by product. Accepts product ID or exact product name. Product handle is not
                supported.
            q: Search string.
            q_scope: Scope of fields used by the q search.
            customer_id: The Advanced Billing id of the customer.
            product_price_point_id: The ID of the product price point. If supplied, product is required.
            coupon: The numeric id of the coupon currently applied to the subscription. (This can be found in the URL
                when editing a coupon. Note that the coupon code cannot be used.)
            coupon_code: The coupon code currently applied to the subscription
            collection_method: The collection method for the subscription.
            branding_theme_id: Filter subscriptions by the ID of an assigned Branding Theme. Branding Themes is a beta
                feature. See `Understand Branding Themes
                <https://docs.maxio.com/hc/en-us/articles/43796895662093-Understand-Branding-Themes#understand-branding-themes-0-0>`__
                for more information.
            date_field: The type of filter you'd like to apply to your search. Allowed Values: , current_period_ends_at,
                current_period_starts_at, created_at, activated_at, canceled_at, expires_at, trial_started_at,
                trial_ended_at, updated_at
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use
                in query ``start_date=2022-07-01``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2022-08-01``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date. Use in query ``end_datetime=2022-08-01 10:00:05``.
            metadata: The value of the metadata field specified in the parameter. Use in query
                ``metadata[my-field]=value&metadata[other-field]=another_value``.
            group_status: Filter by whether a subscription is in a group.
            dunning_exemption: Filter by dunning exemption status.
            payment_gateways: Comma-separated payment gateway identifiers.
            currencies: Comma-separated currency codes.
            include: Allows including additional data in the response. Use in query:
                ``include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_subscriptions(
                page=page,
                per_page=per_page,
                sort=sort,
                direction=direction,
                state=state,
                product=product,
                q=q,
                q_scope=q_scope,
                customer_id=customer_id,
                product_price_point_id=product_price_point_id,
                coupon=coupon,
                coupon_code=coupon_code,
                collection_method=collection_method,
                branding_theme_id=branding_theme_id,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                metadata=metadata,
                group_status=group_status,
                dunning_exemption=dunning_exemption,
                payment_gateways=payment_gateways,
                currencies=currencies,
                include=include,
                request_options=request_options,
            ),
        )

    def override_subscription(
        self,
        subscription_id: int,
        *,
        body: OverrideSubscriptionRequest | OverrideSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Sets certain subscription fields that are usually managed automatically. Some of the fields can be set via
        the normal Subscriptions Update API, but others can only be set using this endpoint.

        This endpoint is provided for cases where you need to “align” Advanced Billing data with data that happened in
        your system, perhaps before you started using Advanced Billing. For example, you may choose to import your
        historical subscription data, and would like the activation and cancellation dates in Advanced Billing to match
        your existing historical dates. Advanced Billing does not backfill historical events (i.e. from the Events API),
        but some static data can be changed via this API.

        Why are some fields only settable from this endpoint, and not the normal subscription create and update
        endpoints? Because we want users of this endpoint to be aware that these fields are usually managed by Advanced
        Billing, and using this API means **you are stepping out on your own.**

        Changing these fields will not affect any other attributes. For example, adding an expiration date will not
        affect the next assessment date on the subscription.

        If you regularly need to override the current_period_starts_at for new subscriptions, this can also be
        accomplished by setting both ``previous_billing_at`` and ``next_billing_at`` at subscription creation. See the
        documentation on `Importing Subscriptions <./b3A6MTQxMDgzODg-create-subscription#subscriptions-import>`__ for
        more information.

        ## Limitations

        When passing ``current_period_starts_at`` some validations are made:

        1. The subscription needs to be unbilled (no statements or invoices).
        2. The value passed must be a valid date/time. We recommend using the iso 8601 format.
        3. The value passed must be before the current date/time.

        If unpermitted parameters are sent, a 400 HTTP response is sent along with a string giving the reason for the
        problem.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: Only these fields are available to be set.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.override_subscription(subscription_id, body=body, request_options=request_options)
        )

    def preview_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionPreviewResponse:
        """Previews a subscription by POSTing the same JSON or XML as for a subscription creation.

        The "Next Billing" amount and "Next Billing" date are represented in each Subscriber's Summary.

        This endpoint does not create a subscription; it is meant to serve as a prediction.

        For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Taxable Subscriptions

        This endpoint previews taxes applicable to a purchase. For taxes to be previewed, the following conditions must
        be met:

        + Taxes must be configured on the subscription
        + The preview must be for the purchase of a taxable product or component, or combination of the two.
        + The subscription payload must contain a full billing or shipping address to calculate tax

        For more information about creating taxable previews, see `Taxes
        <https://maxio.zendesk.com/hc/en-us/sections/24287012349325-Taxes>`__.

        You do **not** need to include a card number to generate tax information when you are previewing a subscription.
        However, when you actually want to create the subscription, you must include the credit card information if you
        want the billing address to be stored. The billing address and the credit card information are stored together
        within the payment profile object. Also, you cannot send a billing address without payment profile information,
        as the address is stored on the card.

        You can pass shipping and billing addresses and still decide not to calculate taxes. To do that, pass
        ``skip_billing_manifest_taxes: true`` attribute.

        ## Non-taxable Subscriptions

        If you'd like to calculate subscriptions that do not include tax, you can leave off the billing information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.preview_subscription(body=body, request_options=request_options))

    def purge_subscription(
        self,
        subscription_id: int,
        ack: int,
        *,
        cascade: list[SubscriptionPurgeTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Purges an individual subscription for sites in test mode.

        Provide the subscription ID in the URL. To confirm, supply the customer ID in the query string ``ack``
        parameter. You may also delete the customer record and/or payment profiles by passing ``cascade`` parameters.
        For example, to delete just the customer record, the query params would be:
        ``?ack={customer_id}&cascade[]=customer``

        If you need to remove subscriptions from a live site, contact support to discuss your use case.

        ### Delete customer and payment profile

        The query params will be: ``?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile``

        Args:
            subscription_id: The Chargify id of the subscription.
            ack: id of the customer.
            cascade: Options are "customer" or "payment_profile". Use in query:
                ``cascade[]=customer&cascade[]=payment_profile``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``SubscriptionResponse | RawError``."""
        return unwrap(
            self._with_raw_response.purge_subscription(
                subscription_id, ack, cascade=cascade, request_options=request_options
            ),
        )

    def read_subscription(
        self,
        subscription_id: int,
        *,
        include: list[SubscriptionIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Retrieves subscription details.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Self-Service Page token

        Self-Service Page token for the subscription is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            subscription_id: The Chargify id of the subscription.
            include: Allows including additional data in the response. Use in query:
                ``include[]=coupons&include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_subscription(subscription_id, include=include, request_options=request_options)
        )

    def remove_coupon_from_subscription(
        self,
        subscription_id: int,
        *,
        coupon_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Removes a coupon from an existing subscription.

        For more information on the expected behavior of removing a coupon from a subscription, see `Coupons and
        Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#removing-a-coupon>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            coupon_code: The coupon code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionRemoveCouponErrors1 | RawError``."""
        return unwrap(
            self._with_raw_response.remove_coupon_from_subscription(
                subscription_id, coupon_code=coupon_code, request_options=request_options
            ),
        )

    def update_prepaid_subscription_configuration(
        self,
        subscription_id: int,
        *,
        body: UpsertPrepaidConfigurationRequest | UpsertPrepaidConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PrepaidConfigurationResponse:
        """Updates a subscription's prepaid configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``PrepaidConfigurationErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.update_prepaid_subscription_configuration(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def update_subscription(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Updates one or more attributes of a subscription.

        ## Update Subscription Payment Method

        Change the card that your subscriber uses for their subscription. You can also use this method to change the
        expiration date of the card **if your gateway allows**.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        > Note: Partial card updates for **Authorize.Net** are not allowed via this endpoint. The existing Payment
            Profile must be directly updated instead.

        ## Update Product

        You also use this method to change the subscription to a different product by setting a new value for
        product_handle. A product change can be done in two different ways, **product change** or **delayed product
        change**.

        ### Product Change

        You can change a subscription's product. The new payment amount is calculated and charged at the normal start of
        the next period. If you require complex product changes or prorated upgrades and downgrades instead, please see
        the documentation on `Migrating Subscription Products
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations#product-changes-and-migrations-0-0>`__.

        To perform a product change, set either the ``product_handle`` or ``product_id`` attribute to that of a
        different product from the same site as the subscription. You can also change the price point by passing in
        either ``product_price_point_id`` or ``product_price_point_handle`` - otherwise the new product's default price
        point is used.

        ### Delayed Product Change

        This method also changes the product and/or price point, and the new payment amount is calculated and charged at
        the normal start of the next period.

        This method schedules the product change to happen automatically at the subscription’s next renewal date. To
        perform a delayed product change, set the ``product_handle`` attribute as you would in a regular product change,
        but also set the ``product_change_delayed`` attribute to ``true``. No proration applies in this case.

        You can also perform a delayed change to the price point by passing in either ``product_price_point_id`` or
        ``product_price_point_handle``

        > **Note:** To cancel a delayed product change, set ``next_product_id`` to an empty string.

        ## Billing Date Changes

        You can update dates for a subscription.

        ### Regular Billing Date Changes

        Send the ``next_billing_at`` to set the next billing date for the subscription. After that date passes and the
        subscription is processed, the following billing date will be set according to the subscription's product
        period.

        > Note: If you pass an invalid date, the correct date is automatically set to the correct date. For example, if
            February 30 is passed, the next billing would be set to March 2nd in a non-leap year.

        The server response will not return data under the key/value pair of ``next_billing_at``. View the key/value
        pair of ``current_period_ends_at`` to verify that the ``next_billing_at`` date has been changed successfully.

        ### Calendar Billing and Snap Day Changes

        For a subscription using Calendar Billing, setting the next billing date is a bit different. Send the
        ``snap_day`` attribute to change the calendar billing date for **a subscription using a product eligible for
        calendar billing**.

        > Note: If you change the product associated with a subscription that contains a ``snap_day`` and immediately
            READ/GET the subscription data, it will still contain the original ``snap_day``. The ``snap_day`` will be
            reset to ``null`` on the next billing cycle. This is because a product change is instantaneous and only
            affects the product associated with a subscription.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, ``product``,
        ``product_price_point_id``, and ``product_price_point_type`` are returned as ``null``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_subscription(subscription_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionsWithRawResponse(client, server, auth)

    async def activate_subscription(
        self,
        subscription_id: int,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Activates awaiting signup and trialing subscriptions. This feature is only available on the Relationship
        Invoicing architecture. Subscriptions in a group cannot be activated immediately.

        The ``revert_on_failure`` parameter controls the behavior upon activation failure.
        - If set to ``true`` and something goes wrong i.e. payment fails, the subscription's state does not change. The
            subscription’s billing period also remains the same.
        - If set to ``false`` and something goes wrong i.e. payment fails, the activation continues and enters an end of
            life state. For trialing subscriptions, that is either trial ended (if the trial is no obligation), past due
            (if the trial has an obligation), or canceled (if the site has no dunning strategy, or has a strategy that
            says to cancel immediately). For awaiting signup subscriptions, that is always canceled.

        The default activation failure behavior can be configured per activation attempt, or you can set a default value
        under Config > Settings > Subscription Activation Settings.

        ## Activation Scenarios

        ### Activate Awaiting Signup subscription

        - Given you have a product without trial
        - Given you have a site without dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Active
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| Canceled
        ```

        - Given you have a product with trial
        - Given you have a site with dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Trialing
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| PD[Past Due]
        ```

        ### Activate Trialing subscription

        For more information about the behavior of trialing subscriptions, see `Trialing Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trialing-Subscriptions>`__. When the
        ``revert_on_failure`` parameter is set to ``true``, the subscription's state remains Trialing; the invoice from
        activation is voided, and any prepayments and credits applied to the invoice are returned to the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``ErrorArrayMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.activate_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def apply_coupons_to_subscription(
        self,
        subscription_id: int,
        *,
        code: str | None = None,
        body: AddCouponsRequest | AddCouponsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Applies one or more coupon codes to an existing subscription.

        An existing subscription can accommodate multiple discounts/coupon codes. This is only applicable if each coupon
        is stackable. For more information on stackable coupons, we recommend reviewing our `coupon documentation.
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#stackability-rules>`__

        ## Query Parameters vs Request Body Parameters

        Passing in a coupon code as a query parameter will add the code to the subscription, completely replacing all
        existing coupon codes on the subscription.

        For this reason, using this query parameter on this endpoint has been deprecated in favor of using the request
        body parameters as described below. When passing in request body parameters, the list of coupon codes will
        simply be added to any existing list of codes on the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            code: A code for the coupon that would be applied to a subscription
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionAddCouponError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.apply_coupons_to_subscription(
                subscription_id, code=code, body=body, request_options=request_options
            ),
        )

    async def create_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Creates a Subscription for a customer and product.

        Specify the product with ``product_id`` or ``product_handle``. To set a specific product price point, use
        ``product_price_point_handle`` or ``product_price_point_id``.

        Identify an existing customer with ``customer_id`` or ``customer_reference``. Optionally, include an existing
        payment profile using ``payment_profile_id``. To create a new customer, pass customer_attributes.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating subscriptions.

        ## List vs Sales Pricing

        When a subscription uses custom pricing as the sales price, you can optionally provide a list price for any
        item. If omitted, the list price defaults to the sales price. The difference between the list price and sales
        price is used to calculate implicit discounts, which appear on Invoices and in reporting. List price can also
        support revenue allocations in `Advanced Revenue
        <https://docs.maxio.com/hc/en-us/articles/24177001342861-Create-and-Configure-RevenueBooks>`__.

        If your site has list pricing enabled, the API accepts ``custom_price.list_price_point_id`` for custom pricing,
        validates and persists it, and returns list price metadata in subscription responses. If list pricing is
        disabled, this input is ignored and related response fields are omitted.

        When list pricing is enabled:

        - Subscription → Product ``product_price_point_list_price_point_id`` (integer)
        - ``product_price_point_list_price_point_handle`` (string)
        - Subscription Components (when components are included in the response, such as with subscriptions built from
            components or component serialization paths) ``component_id`` (integer)
        - ``price_point_id`` (integer)
        - ``list_price_point_id`` (integer)

        When list pricing is disabled:

        - Subscription → Product ``product_price_point_list_price_point_id``: omitted
        - ``product_price_point_list_price_point_handle``: omitted
        - Subscription Components ``list_price_point_id``: omitted

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)
        - a configured metered component

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters. See the `Subscription Signups <page:introduction/basic-concepts/subscription-signup>`__
        article for more information on working with subscriptions in Advanced Billing.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_subscription(body=body, request_options=request_options))

    async def find_subscription(
        self, *, reference: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Finds a subscription by its reference.

        Args:
            reference: Subscription reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.find_subscription(reference=reference, request_options=request_options)
        )

    async def list_subscriptions(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: SubscriptionSortOrStr | None = SubscriptionSort.SIGNUP_DATE,
        direction: SortingDirectionOrStr | None = None,
        state: SubscriptionStateFilterOrStr | None = None,
        product: Product1 | Product1Dict | None = None,
        q: str | None = None,
        q_scope: QScopeOrStr | None = None,
        customer_id: int | None = None,
        product_price_point_id: int | None = None,
        coupon: int | None = None,
        coupon_code: str | None = None,
        collection_method: CollectionMethod1OrStr | None = None,
        branding_theme_id: int | None = None,
        date_field: SubscriptionDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        metadata: dict[str, str] | None = None,
        group_status: GroupStatusOrStr | None = None,
        dunning_exemption: bool | None = None,
        payment_gateways: str | None = None,
        currencies: str | None = None,
        include: list[SubscriptionListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SubscriptionResponse]:
        """Lists subscriptions for a site. Use the query string filters and pagination to control responses from the
        server.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Search for a subscription

        Use the query strings below to search for a subscription using the criteria available. The return value will be
        an array.

        ## Self-Service Page token

        Self-Service Page token for the subscriptions is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            state: The current state of the subscription
            product: Filter subscriptions by product. Accepts product ID or exact product name. Product handle is not
                supported.
            q: Search string.
            q_scope: Scope of fields used by the q search.
            customer_id: The Advanced Billing id of the customer.
            product_price_point_id: The ID of the product price point. If supplied, product is required.
            coupon: The numeric id of the coupon currently applied to the subscription. (This can be found in the URL
                when editing a coupon. Note that the coupon code cannot be used.)
            coupon_code: The coupon code currently applied to the subscription
            collection_method: The collection method for the subscription.
            branding_theme_id: Filter subscriptions by the ID of an assigned Branding Theme. Branding Themes is a beta
                feature. See `Understand Branding Themes
                <https://docs.maxio.com/hc/en-us/articles/43796895662093-Understand-Branding-Themes#understand-branding-themes-0-0>`__
                for more information.
            date_field: The type of filter you'd like to apply to your search. Allowed Values: , current_period_ends_at,
                current_period_starts_at, created_at, activated_at, canceled_at, expires_at, trial_started_at,
                trial_ended_at, updated_at
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use
                in query ``start_date=2022-07-01``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2022-08-01``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date. Use in query ``end_datetime=2022-08-01 10:00:05``.
            metadata: The value of the metadata field specified in the parameter. Use in query
                ``metadata[my-field]=value&metadata[other-field]=another_value``.
            group_status: Filter by whether a subscription is in a group.
            dunning_exemption: Filter by dunning exemption status.
            payment_gateways: Comma-separated payment gateway identifiers.
            currencies: Comma-separated currency codes.
            include: Allows including additional data in the response. Use in query:
                ``include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_subscriptions(
                page=page,
                per_page=per_page,
                sort=sort,
                direction=direction,
                state=state,
                product=product,
                q=q,
                q_scope=q_scope,
                customer_id=customer_id,
                product_price_point_id=product_price_point_id,
                coupon=coupon,
                coupon_code=coupon_code,
                collection_method=collection_method,
                branding_theme_id=branding_theme_id,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                metadata=metadata,
                group_status=group_status,
                dunning_exemption=dunning_exemption,
                payment_gateways=payment_gateways,
                currencies=currencies,
                include=include,
                request_options=request_options,
            ),
        )

    async def override_subscription(
        self,
        subscription_id: int,
        *,
        body: OverrideSubscriptionRequest | OverrideSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Sets certain subscription fields that are usually managed automatically. Some of the fields can be set via
        the normal Subscriptions Update API, but others can only be set using this endpoint.

        This endpoint is provided for cases where you need to “align” Advanced Billing data with data that happened in
        your system, perhaps before you started using Advanced Billing. For example, you may choose to import your
        historical subscription data, and would like the activation and cancellation dates in Advanced Billing to match
        your existing historical dates. Advanced Billing does not backfill historical events (i.e. from the Events API),
        but some static data can be changed via this API.

        Why are some fields only settable from this endpoint, and not the normal subscription create and update
        endpoints? Because we want users of this endpoint to be aware that these fields are usually managed by Advanced
        Billing, and using this API means **you are stepping out on your own.**

        Changing these fields will not affect any other attributes. For example, adding an expiration date will not
        affect the next assessment date on the subscription.

        If you regularly need to override the current_period_starts_at for new subscriptions, this can also be
        accomplished by setting both ``previous_billing_at`` and ``next_billing_at`` at subscription creation. See the
        documentation on `Importing Subscriptions <./b3A6MTQxMDgzODg-create-subscription#subscriptions-import>`__ for
        more information.

        ## Limitations

        When passing ``current_period_starts_at`` some validations are made:

        1. The subscription needs to be unbilled (no statements or invoices).
        2. The value passed must be a valid date/time. We recommend using the iso 8601 format.
        3. The value passed must be before the current date/time.

        If unpermitted parameters are sent, a 400 HTTP response is sent along with a string giving the reason for the
        problem.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: Only these fields are available to be set.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.override_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def preview_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionPreviewResponse:
        """Previews a subscription by POSTing the same JSON or XML as for a subscription creation.

        The "Next Billing" amount and "Next Billing" date are represented in each Subscriber's Summary.

        This endpoint does not create a subscription; it is meant to serve as a prediction.

        For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Taxable Subscriptions

        This endpoint previews taxes applicable to a purchase. For taxes to be previewed, the following conditions must
        be met:

        + Taxes must be configured on the subscription
        + The preview must be for the purchase of a taxable product or component, or combination of the two.
        + The subscription payload must contain a full billing or shipping address to calculate tax

        For more information about creating taxable previews, see `Taxes
        <https://maxio.zendesk.com/hc/en-us/sections/24287012349325-Taxes>`__.

        You do **not** need to include a card number to generate tax information when you are previewing a subscription.
        However, when you actually want to create the subscription, you must include the credit card information if you
        want the billing address to be stored. The billing address and the credit card information are stored together
        within the payment profile object. Also, you cannot send a billing address without payment profile information,
        as the address is stored on the card.

        You can pass shipping and billing addresses and still decide not to calculate taxes. To do that, pass
        ``skip_billing_manifest_taxes: true`` attribute.

        ## Non-taxable Subscriptions

        If you'd like to calculate subscriptions that do not include tax, you can leave off the billing information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.preview_subscription(body=body, request_options=request_options))

    async def purge_subscription(
        self,
        subscription_id: int,
        ack: int,
        *,
        cascade: list[SubscriptionPurgeTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Purges an individual subscription for sites in test mode.

        Provide the subscription ID in the URL. To confirm, supply the customer ID in the query string ``ack``
        parameter. You may also delete the customer record and/or payment profiles by passing ``cascade`` parameters.
        For example, to delete just the customer record, the query params would be:
        ``?ack={customer_id}&cascade[]=customer``

        If you need to remove subscriptions from a live site, contact support to discuss your use case.

        ### Delete customer and payment profile

        The query params will be: ``?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile``

        Args:
            subscription_id: The Chargify id of the subscription.
            ack: id of the customer.
            cascade: Options are "customer" or "payment_profile". Use in query:
                ``cascade[]=customer&cascade[]=payment_profile``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Bad Request ``error`` is ``SubscriptionResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.purge_subscription(
                subscription_id, ack, cascade=cascade, request_options=request_options
            ),
        )

    async def read_subscription(
        self,
        subscription_id: int,
        *,
        include: list[SubscriptionIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Retrieves subscription details.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Self-Service Page token

        Self-Service Page token for the subscription is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            subscription_id: The Chargify id of the subscription.
            include: Allows including additional data in the response. Use in query:
                ``include[]=coupons&include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_subscription(
                subscription_id, include=include, request_options=request_options
            ),
        )

    async def remove_coupon_from_subscription(
        self,
        subscription_id: int,
        *,
        coupon_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Removes a coupon from an existing subscription.

        For more information on the expected behavior of removing a coupon from a subscription, see `Coupons and
        Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#removing-a-coupon>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            coupon_code: The coupon code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionRemoveCouponErrors1 | RawError``."""
        return unwrap(
            await self._with_raw_response.remove_coupon_from_subscription(
                subscription_id, coupon_code=coupon_code, request_options=request_options
            ),
        )

    async def update_prepaid_subscription_configuration(
        self,
        subscription_id: int,
        *,
        body: UpsertPrepaidConfigurationRequest | UpsertPrepaidConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PrepaidConfigurationResponse:
        """Updates a subscription's prepaid configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``PrepaidConfigurationErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.update_prepaid_subscription_configuration(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def update_subscription(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Updates one or more attributes of a subscription.

        ## Update Subscription Payment Method

        Change the card that your subscriber uses for their subscription. You can also use this method to change the
        expiration date of the card **if your gateway allows**.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        > Note: Partial card updates for **Authorize.Net** are not allowed via this endpoint. The existing Payment
            Profile must be directly updated instead.

        ## Update Product

        You also use this method to change the subscription to a different product by setting a new value for
        product_handle. A product change can be done in two different ways, **product change** or **delayed product
        change**.

        ### Product Change

        You can change a subscription's product. The new payment amount is calculated and charged at the normal start of
        the next period. If you require complex product changes or prorated upgrades and downgrades instead, please see
        the documentation on `Migrating Subscription Products
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations#product-changes-and-migrations-0-0>`__.

        To perform a product change, set either the ``product_handle`` or ``product_id`` attribute to that of a
        different product from the same site as the subscription. You can also change the price point by passing in
        either ``product_price_point_id`` or ``product_price_point_handle`` - otherwise the new product's default price
        point is used.

        ### Delayed Product Change

        This method also changes the product and/or price point, and the new payment amount is calculated and charged at
        the normal start of the next period.

        This method schedules the product change to happen automatically at the subscription’s next renewal date. To
        perform a delayed product change, set the ``product_handle`` attribute as you would in a regular product change,
        but also set the ``product_change_delayed`` attribute to ``true``. No proration applies in this case.

        You can also perform a delayed change to the price point by passing in either ``product_price_point_id`` or
        ``product_price_point_handle``

        > **Note:** To cancel a delayed product change, set ``next_product_id`` to an empty string.

        ## Billing Date Changes

        You can update dates for a subscription.

        ### Regular Billing Date Changes

        Send the ``next_billing_at`` to set the next billing date for the subscription. After that date passes and the
        subscription is processed, the following billing date will be set according to the subscription's product
        period.

        > Note: If you pass an invalid date, the correct date is automatically set to the correct date. For example, if
            February 30 is passed, the next billing would be set to March 2nd in a non-leap year.

        The server response will not return data under the key/value pair of ``next_billing_at``. View the key/value
        pair of ``current_period_ends_at`` to verify that the ``next_billing_at`` date has been changed successfully.

        ### Calendar Billing and Snap Day Changes

        For a subscription using Calendar Billing, setting the next billing date is a bit different. Send the
        ``snap_day`` attribute to change the calendar billing date for **a subscription using a product eligible for
        calendar billing**.

        > Note: If you change the product associated with a subscription that contains a ``snap_day`` and immediately
            READ/GET the subscription data, it will still contain the original ``snap_day``. The ``snap_day`` will be
            reset to ``null`` on the next billing cycle. This is because a product change is instantaneous and only
            affects the product associated with a subscription.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, ``product``,
        ``product_price_point_id``, and ``product_price_point_type`` are returned as ``null``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        return self._with_raw_response


class SubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_subscription(
        self,
        subscription_id: int,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ActivateSubscriptionErrorBody]:
        """Activates awaiting signup and trialing subscriptions. This feature is only available on the Relationship
        Invoicing architecture. Subscriptions in a group cannot be activated immediately.

        The ``revert_on_failure`` parameter controls the behavior upon activation failure.
        - If set to ``true`` and something goes wrong i.e. payment fails, the subscription's state does not change. The
            subscription’s billing period also remains the same.
        - If set to ``false`` and something goes wrong i.e. payment fails, the activation continues and enters an end of
            life state. For trialing subscriptions, that is either trial ended (if the trial is no obligation), past due
            (if the trial has an obligation), or canceled (if the site has no dunning strategy, or has a strategy that
            says to cancel immediately). For awaiting signup subscriptions, that is always canceled.

        The default activation failure behavior can be configured per activation attempt, or you can set a default value
        under Config > Settings > Subscription Activation Settings.

        ## Activation Scenarios

        ### Activate Awaiting Signup subscription

        - Given you have a product without trial
        - Given you have a site without dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Active
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| Canceled
        ```

        - Given you have a product with trial
        - Given you have a site with dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Trialing
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| PD[Past Due]
        ```

        ### Activate Trialing subscription

        For more information about the behavior of trialing subscriptions, see `Trialing Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trialing-Subscriptions>`__. When the
        ``revert_on_failure`` parameter is set to ``true``, the subscription's state remains Trialing; the invoice from
        activation is voided, and any prepayments and credits applied to the invoice are returned to the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/activate.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=activate_subscription_error_mapper,
            request_options=request_options,
        )

    def apply_coupons_to_subscription(
        self,
        subscription_id: int,
        *,
        code: str | None = None,
        body: AddCouponsRequest | AddCouponsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ApplyCouponsToSubscriptionErrorBody]:
        """Applies one or more coupon codes to an existing subscription.

        An existing subscription can accommodate multiple discounts/coupon codes. This is only applicable if each coupon
        is stackable. For more information on stackable coupons, we recommend reviewing our `coupon documentation.
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#stackability-rules>`__

        ## Query Parameters vs Request Body Parameters

        Passing in a coupon code as a query parameter will add the code to the subscription, completely replacing all
        existing coupon codes on the subscription.

        For this reason, using this query parameter on this endpoint has been deprecated in favor of using the request
        body parameters as described below. When passing in request body parameters, the list of coupon codes will
        simply be added to any existing list of codes on the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            code: A code for the coupon that would be applied to a subscription
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/add_coupon.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[str | None]("code", code)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddCouponsRequest | AddCouponsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=apply_coupons_to_subscription_error_mapper,
            request_options=request_options,
        )

    def create_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, CreateSubscriptionErrorBody]:
        """Creates a Subscription for a customer and product.

        Specify the product with ``product_id`` or ``product_handle``. To set a specific product price point, use
        ``product_price_point_handle`` or ``product_price_point_id``.

        Identify an existing customer with ``customer_id`` or ``customer_reference``. Optionally, include an existing
        payment profile using ``payment_profile_id``. To create a new customer, pass customer_attributes.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating subscriptions.

        ## List vs Sales Pricing

        When a subscription uses custom pricing as the sales price, you can optionally provide a list price for any
        item. If omitted, the list price defaults to the sales price. The difference between the list price and sales
        price is used to calculate implicit discounts, which appear on Invoices and in reporting. List price can also
        support revenue allocations in `Advanced Revenue
        <https://docs.maxio.com/hc/en-us/articles/24177001342861-Create-and-Configure-RevenueBooks>`__.

        If your site has list pricing enabled, the API accepts ``custom_price.list_price_point_id`` for custom pricing,
        validates and persists it, and returns list price metadata in subscription responses. If list pricing is
        disabled, this input is ignored and related response fields are omitted.

        When list pricing is enabled:

        - Subscription → Product ``product_price_point_list_price_point_id`` (integer)
        - ``product_price_point_list_price_point_handle`` (string)
        - Subscription Components (when components are included in the response, such as with subscriptions built from
            components or component serialization paths) ``component_id`` (integer)
        - ``price_point_id`` (integer)
        - ``list_price_point_id`` (integer)

        When list pricing is disabled:

        - Subscription → Product ``product_price_point_list_price_point_id``: omitted
        - ``product_price_point_list_price_point_handle``: omitted
        - Subscription Components ``list_price_point_id``: omitted

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)
        - a configured metered component

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters. See the `Subscription Signups <page:introduction/basic-concepts/subscription-signup>`__
        article for more information on working with subscriptions in Advanced Billing.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=create_subscription_error_mapper,
            request_options=request_options,
        )

    def find_subscription(
        self, *, reference: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, FindSubscriptionErrorBody]:
        """Finds a subscription by its reference.

        Args:
            reference: Subscription reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/lookup.json"),
            query_params=[param[str | None]("reference", reference)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=find_subscription_error_mapper,
            request_options=request_options,
        )

    def list_subscriptions(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: SubscriptionSortOrStr | None = SubscriptionSort.SIGNUP_DATE,
        direction: SortingDirectionOrStr | None = None,
        state: SubscriptionStateFilterOrStr | None = None,
        product: Product1 | Product1Dict | None = None,
        q: str | None = None,
        q_scope: QScopeOrStr | None = None,
        customer_id: int | None = None,
        product_price_point_id: int | None = None,
        coupon: int | None = None,
        coupon_code: str | None = None,
        collection_method: CollectionMethod1OrStr | None = None,
        branding_theme_id: int | None = None,
        date_field: SubscriptionDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        metadata: dict[str, str] | None = None,
        group_status: GroupStatusOrStr | None = None,
        dunning_exemption: bool | None = None,
        payment_gateways: str | None = None,
        currencies: str | None = None,
        include: list[SubscriptionListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SubscriptionResponse], RawError]:
        """Lists subscriptions for a site. Use the query string filters and pagination to control responses from the
        server.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Search for a subscription

        Use the query strings below to search for a subscription using the criteria available. The return value will be
        an array.

        ## Self-Service Page token

        Self-Service Page token for the subscriptions is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            state: The current state of the subscription
            product: Filter subscriptions by product. Accepts product ID or exact product name. Product handle is not
                supported.
            q: Search string.
            q_scope: Scope of fields used by the q search.
            customer_id: The Advanced Billing id of the customer.
            product_price_point_id: The ID of the product price point. If supplied, product is required.
            coupon: The numeric id of the coupon currently applied to the subscription. (This can be found in the URL
                when editing a coupon. Note that the coupon code cannot be used.)
            coupon_code: The coupon code currently applied to the subscription
            collection_method: The collection method for the subscription.
            branding_theme_id: Filter subscriptions by the ID of an assigned Branding Theme. Branding Themes is a beta
                feature. See `Understand Branding Themes
                <https://docs.maxio.com/hc/en-us/articles/43796895662093-Understand-Branding-Themes#understand-branding-themes-0-0>`__
                for more information.
            date_field: The type of filter you'd like to apply to your search. Allowed Values: , current_period_ends_at,
                current_period_starts_at, created_at, activated_at, canceled_at, expires_at, trial_started_at,
                trial_ended_at, updated_at
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use
                in query ``start_date=2022-07-01``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2022-08-01``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date. Use in query ``end_datetime=2022-08-01 10:00:05``.
            metadata: The value of the metadata field specified in the parameter. Use in query
                ``metadata[my-field]=value&metadata[other-field]=another_value``.
            group_status: Filter by whether a subscription is in a group.
            dunning_exemption: Filter by dunning exemption status.
            payment_gateways: Comma-separated payment gateway identifiers.
            currencies: Comma-separated currency codes.
            include: Allows including additional data in the response. Use in query:
                ``include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SubscriptionSortOrStr | None]("sort", sort),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[SubscriptionStateFilterOrStr | None]("state", state),
                param[Product1 | Product1Dict | None]("product", product),
                param[str | None]("q", q),
                param[QScopeOrStr | None]("q_scope", q_scope),
                param[int | None]("customer_id", customer_id),
                param[int | None]("product_price_point_id", product_price_point_id),
                param[int | None]("coupon", coupon),
                param[str | None]("coupon_code", coupon_code),
                param[CollectionMethod1OrStr | None]("collection_method", collection_method),
                param[int | None]("branding_theme_id", branding_theme_id),
                param[SubscriptionDateFieldOrStr | None]("date_field", date_field),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[dict[str, str] | None]("metadata", metadata),
                param[GroupStatusOrStr | None]("group_status", group_status),
                param[bool | None]("dunning_exemption", dunning_exemption),
                param[str | None]("payment_gateways", payment_gateways),
                param[str | None]("currencies", currencies),
                param[list[SubscriptionListIncludeOrStr] | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[SubscriptionResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def override_subscription(
        self,
        subscription_id: int,
        *,
        body: OverrideSubscriptionRequest | OverrideSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, OverrideSubscriptionErrorBody]:
        """Sets certain subscription fields that are usually managed automatically. Some of the fields can be set via
        the normal Subscriptions Update API, but others can only be set using this endpoint.

        This endpoint is provided for cases where you need to “align” Advanced Billing data with data that happened in
        your system, perhaps before you started using Advanced Billing. For example, you may choose to import your
        historical subscription data, and would like the activation and cancellation dates in Advanced Billing to match
        your existing historical dates. Advanced Billing does not backfill historical events (i.e. from the Events API),
        but some static data can be changed via this API.

        Why are some fields only settable from this endpoint, and not the normal subscription create and update
        endpoints? Because we want users of this endpoint to be aware that these fields are usually managed by Advanced
        Billing, and using this API means **you are stepping out on your own.**

        Changing these fields will not affect any other attributes. For example, adding an expiration date will not
        affect the next assessment date on the subscription.

        If you regularly need to override the current_period_starts_at for new subscriptions, this can also be
        accomplished by setting both ``previous_billing_at`` and ``next_billing_at`` at subscription creation. See the
        documentation on `Importing Subscriptions <./b3A6MTQxMDgzODg-create-subscription#subscriptions-import>`__ for
        more information.

        ## Limitations

        When passing ``current_period_starts_at`` some validations are made:

        1. The subscription needs to be unbilled (no statements or invoices).
        2. The value passed must be a valid date/time. We recommend using the iso 8601 format.
        3. The value passed must be before the current date/time.

        If unpermitted parameters are sent, a 400 HTTP response is sent along with a string giving the reason for the
        problem.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: Only these fields are available to be set.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/override.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OverrideSubscriptionRequest | OverrideSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=override_subscription_error_mapper,
            request_options=request_options,
        )

    def preview_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionPreviewResponse, RawError]:
        """Previews a subscription by POSTing the same JSON or XML as for a subscription creation.

        The "Next Billing" amount and "Next Billing" date are represented in each Subscriber's Summary.

        This endpoint does not create a subscription; it is meant to serve as a prediction.

        For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Taxable Subscriptions

        This endpoint previews taxes applicable to a purchase. For taxes to be previewed, the following conditions must
        be met:

        + Taxes must be configured on the subscription
        + The preview must be for the purchase of a taxable product or component, or combination of the two.
        + The subscription payload must contain a full billing or shipping address to calculate tax

        For more information about creating taxable previews, see `Taxes
        <https://maxio.zendesk.com/hc/en-us/sections/24287012349325-Taxes>`__.

        You do **not** need to include a card number to generate tax information when you are previewing a subscription.
        However, when you actually want to create the subscription, you must include the credit card information if you
        want the billing address to be stored. The billing address and the credit card information are stored together
        within the payment profile object. Also, you cannot send a billing address without payment profile information,
        as the address is stored on the card.

        You can pass shipping and billing addresses and still decide not to calculate taxes. To do that, pass
        ``skip_billing_manifest_taxes: true`` attribute.

        ## Non-taxable Subscriptions

        If you'd like to calculate subscriptions that do not include tax, you can leave off the billing information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/preview.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionPreviewResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def purge_subscription(
        self,
        subscription_id: int,
        ack: int,
        *,
        cascade: list[SubscriptionPurgeTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, PurgeSubscriptionErrorBody]:
        """Purges an individual subscription for sites in test mode.

        Provide the subscription ID in the URL. To confirm, supply the customer ID in the query string ``ack``
        parameter. You may also delete the customer record and/or payment profiles by passing ``cascade`` parameters.
        For example, to delete just the customer record, the query params would be:
        ``?ack={customer_id}&cascade[]=customer``

        If you need to remove subscriptions from a live site, contact support to discuss your use case.

        ### Delete customer and payment profile

        The query params will be: ``?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile``

        Args:
            subscription_id: The Chargify id of the subscription.
            ack: id of the customer.
            cascade: Options are "customer" or "payment_profile". Use in query:
                ``cascade[]=customer&cascade[]=payment_profile``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/purge.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[int]("ack", ack), param[list[SubscriptionPurgeTypeOrStr] | None]("cascade", cascade)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=purge_subscription_error_mapper,
            request_options=request_options,
        )

    def read_subscription(
        self,
        subscription_id: int,
        *,
        include: list[SubscriptionIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, RawError]:
        """Retrieves subscription details.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Self-Service Page token

        Self-Service Page token for the subscription is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            subscription_id: The Chargify id of the subscription.
            include: Allows including additional data in the response. Use in query:
                ``include[]=coupons&include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[list[SubscriptionIncludeOrStr] | None]("include", include)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_coupon_from_subscription(
        self,
        subscription_id: int,
        *,
        coupon_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, RemoveCouponFromSubscriptionErrorBody]:
        """Removes a coupon from an existing subscription.

        For more information on the expected behavior of removing a coupon from a subscription, see `Coupons and
        Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#removing-a-coupon>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            coupon_code: The coupon code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/remove_coupon.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[str | None]("coupon_code", coupon_code)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[str],
            error_mapper=remove_coupon_from_subscription_error_mapper,
            request_options=request_options,
        )

    def update_prepaid_subscription_configuration(
        self,
        subscription_id: int,
        *,
        body: UpsertPrepaidConfigurationRequest | UpsertPrepaidConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PrepaidConfigurationResponse, UpdatePrepaidSubscriptionConfigurationErrorBody]:
        """Updates a subscription's prepaid configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/prepaid_configurations.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertPrepaidConfigurationRequest | UpsertPrepaidConfigurationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PrepaidConfigurationResponse],
            error_mapper=update_prepaid_subscription_configuration_error_mapper,
            request_options=request_options,
        )

    def update_subscription(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, UpdateSubscriptionErrorBody]:
        """Updates one or more attributes of a subscription.

        ## Update Subscription Payment Method

        Change the card that your subscriber uses for their subscription. You can also use this method to change the
        expiration date of the card **if your gateway allows**.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        > Note: Partial card updates for **Authorize.Net** are not allowed via this endpoint. The existing Payment
            Profile must be directly updated instead.

        ## Update Product

        You also use this method to change the subscription to a different product by setting a new value for
        product_handle. A product change can be done in two different ways, **product change** or **delayed product
        change**.

        ### Product Change

        You can change a subscription's product. The new payment amount is calculated and charged at the normal start of
        the next period. If you require complex product changes or prorated upgrades and downgrades instead, please see
        the documentation on `Migrating Subscription Products
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations#product-changes-and-migrations-0-0>`__.

        To perform a product change, set either the ``product_handle`` or ``product_id`` attribute to that of a
        different product from the same site as the subscription. You can also change the price point by passing in
        either ``product_price_point_id`` or ``product_price_point_handle`` - otherwise the new product's default price
        point is used.

        ### Delayed Product Change

        This method also changes the product and/or price point, and the new payment amount is calculated and charged at
        the normal start of the next period.

        This method schedules the product change to happen automatically at the subscription’s next renewal date. To
        perform a delayed product change, set the ``product_handle`` attribute as you would in a regular product change,
        but also set the ``product_change_delayed`` attribute to ``true``. No proration applies in this case.

        You can also perform a delayed change to the price point by passing in either ``product_price_point_id`` or
        ``product_price_point_handle``

        > **Note:** To cancel a delayed product change, set ``next_product_id`` to an empty string.

        ## Billing Date Changes

        You can update dates for a subscription.

        ### Regular Billing Date Changes

        Send the ``next_billing_at`` to set the next billing date for the subscription. After that date passes and the
        subscription is processed, the following billing date will be set according to the subscription's product
        period.

        > Note: If you pass an invalid date, the correct date is automatically set to the correct date. For example, if
            February 30 is passed, the next billing would be set to March 2nd in a non-leap year.

        The server response will not return data under the key/value pair of ``next_billing_at``. View the key/value
        pair of ``current_period_ends_at`` to verify that the ``next_billing_at`` date has been changed successfully.

        ### Calendar Billing and Snap Day Changes

        For a subscription using Calendar Billing, setting the next billing date is a bit different. Send the
        ``snap_day`` attribute to change the calendar billing date for **a subscription using a product eligible for
        calendar billing**.

        > Note: If you change the product associated with a subscription that contains a ``snap_day`` and immediately
            READ/GET the subscription data, it will still contain the original ``snap_day``. The ``snap_day`` will be
            reset to ``null`` on the next billing cycle. This is because a product change is instantaneous and only
            affects the product associated with a subscription.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, ``product``,
        ``product_price_point_id``, and ``product_price_point_type`` are returned as ``null``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionRequest | UpdateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=update_subscription_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_subscription(
        self,
        subscription_id: int,
        *,
        body: ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ActivateSubscriptionErrorBody]:
        """Activates awaiting signup and trialing subscriptions. This feature is only available on the Relationship
        Invoicing architecture. Subscriptions in a group cannot be activated immediately.

        The ``revert_on_failure`` parameter controls the behavior upon activation failure.
        - If set to ``true`` and something goes wrong i.e. payment fails, the subscription's state does not change. The
            subscription’s billing period also remains the same.
        - If set to ``false`` and something goes wrong i.e. payment fails, the activation continues and enters an end of
            life state. For trialing subscriptions, that is either trial ended (if the trial is no obligation), past due
            (if the trial has an obligation), or canceled (if the site has no dunning strategy, or has a strategy that
            says to cancel immediately). For awaiting signup subscriptions, that is always canceled.

        The default activation failure behavior can be configured per activation attempt, or you can set a default value
        under Config > Settings > Subscription Activation Settings.

        ## Activation Scenarios

        ### Activate Awaiting Signup subscription

        - Given you have a product without trial
        - Given you have a site without dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Active
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| Canceled
        ```

        - Given you have a product with trial
        - Given you have a site with dunning strategy

        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Trialing
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| PD[Past Due]
        ```

        ### Activate Trialing subscription

        For more information about the behavior of trialing subscriptions, see `Trialing Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trialing-Subscriptions>`__. When the
        ``revert_on_failure`` parameter is set to ``true``, the subscription's state remains Trialing; the invoice from
        activation is voided, and any prepayments and credits applied to the invoice are returned to the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/activate.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateSubscriptionRequest | ActivateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=activate_subscription_error_mapper,
            request_options=request_options,
        )

    async def apply_coupons_to_subscription(
        self,
        subscription_id: int,
        *,
        code: str | None = None,
        body: AddCouponsRequest | AddCouponsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ApplyCouponsToSubscriptionErrorBody]:
        """Applies one or more coupon codes to an existing subscription.

        An existing subscription can accommodate multiple discounts/coupon codes. This is only applicable if each coupon
        is stackable. For more information on stackable coupons, we recommend reviewing our `coupon documentation.
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#stackability-rules>`__

        ## Query Parameters vs Request Body Parameters

        Passing in a coupon code as a query parameter will add the code to the subscription, completely replacing all
        existing coupon codes on the subscription.

        For this reason, using this query parameter on this endpoint has been deprecated in favor of using the request
        body parameters as described below. When passing in request body parameters, the list of coupon codes will
        simply be added to any existing list of codes on the subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            code: A code for the coupon that would be applied to a subscription
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/add_coupon.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[str | None]("code", code)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddCouponsRequest | AddCouponsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=apply_coupons_to_subscription_error_mapper,
            request_options=request_options,
        )

    async def create_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, CreateSubscriptionErrorBody]:
        """Creates a Subscription for a customer and product.

        Specify the product with ``product_id`` or ``product_handle``. To set a specific product price point, use
        ``product_price_point_handle`` or ``product_price_point_id``.

        Identify an existing customer with ``customer_id`` or ``customer_reference``. Optionally, include an existing
        payment profile using ``payment_profile_id``. To create a new customer, pass customer_attributes.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating subscriptions.

        ## List vs Sales Pricing

        When a subscription uses custom pricing as the sales price, you can optionally provide a list price for any
        item. If omitted, the list price defaults to the sales price. The difference between the list price and sales
        price is used to calculate implicit discounts, which appear on Invoices and in reporting. List price can also
        support revenue allocations in `Advanced Revenue
        <https://docs.maxio.com/hc/en-us/articles/24177001342861-Create-and-Configure-RevenueBooks>`__.

        If your site has list pricing enabled, the API accepts ``custom_price.list_price_point_id`` for custom pricing,
        validates and persists it, and returns list price metadata in subscription responses. If list pricing is
        disabled, this input is ignored and related response fields are omitted.

        When list pricing is enabled:

        - Subscription → Product ``product_price_point_list_price_point_id`` (integer)
        - ``product_price_point_list_price_point_handle`` (string)
        - Subscription Components (when components are included in the response, such as with subscriptions built from
            components or component serialization paths) ``component_id`` (integer)
        - ``price_point_id`` (integer)
        - ``list_price_point_id`` (integer)

        When list pricing is disabled:

        - Subscription → Product ``product_price_point_list_price_point_id``: omitted
        - ``product_price_point_list_price_point_handle``: omitted
        - Subscription Components ``list_price_point_id``: omitted

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)
        - a configured metered component

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters. See the `Subscription Signups <page:introduction/basic-concepts/subscription-signup>`__
        article for more information on working with subscriptions in Advanced Billing.

        ## Payment information

        Payment information may be required to create a subscription, depending on the options for the Product being
        subscribed. See `product options <https://docs.maxio.com/hc/en-us/articles/24261076617869-Edit-Products>`__ for
        more information. See the `Payments Profile <$e/Payment%20Profiles/createPaymentProfile>`__ endpoint for details
        on payment parameters.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=create_subscription_error_mapper,
            request_options=request_options,
        )

    async def find_subscription(
        self, *, reference: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, FindSubscriptionErrorBody]:
        """Finds a subscription by its reference.

        Args:
            reference: Subscription reference
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/lookup.json"),
            query_params=[param[str | None]("reference", reference)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=find_subscription_error_mapper,
            request_options=request_options,
        )

    async def list_subscriptions(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: SubscriptionSortOrStr | None = SubscriptionSort.SIGNUP_DATE,
        direction: SortingDirectionOrStr | None = None,
        state: SubscriptionStateFilterOrStr | None = None,
        product: Product1 | Product1Dict | None = None,
        q: str | None = None,
        q_scope: QScopeOrStr | None = None,
        customer_id: int | None = None,
        product_price_point_id: int | None = None,
        coupon: int | None = None,
        coupon_code: str | None = None,
        collection_method: CollectionMethod1OrStr | None = None,
        branding_theme_id: int | None = None,
        date_field: SubscriptionDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        metadata: dict[str, str] | None = None,
        group_status: GroupStatusOrStr | None = None,
        dunning_exemption: bool | None = None,
        payment_gateways: str | None = None,
        currencies: str | None = None,
        include: list[SubscriptionListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SubscriptionResponse], RawError]:
        """Lists subscriptions for a site. Use the query string filters and pagination to control responses from the
        server.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Search for a subscription

        Use the query strings below to search for a subscription using the criteria available. The return value will be
        an array.

        ## Self-Service Page token

        Self-Service Page token for the subscriptions is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            state: The current state of the subscription
            product: Filter subscriptions by product. Accepts product ID or exact product name. Product handle is not
                supported.
            q: Search string.
            q_scope: Scope of fields used by the q search.
            customer_id: The Advanced Billing id of the customer.
            product_price_point_id: The ID of the product price point. If supplied, product is required.
            coupon: The numeric id of the coupon currently applied to the subscription. (This can be found in the URL
                when editing a coupon. Note that the coupon code cannot be used.)
            coupon_code: The coupon code currently applied to the subscription
            collection_method: The collection method for the subscription.
            branding_theme_id: Filter subscriptions by the ID of an assigned Branding Theme. Branding Themes is a beta
                feature. See `Understand Branding Themes
                <https://docs.maxio.com/hc/en-us/articles/43796895662093-Understand-Branding-Themes#understand-branding-themes-0-0>`__
                for more information.
            date_field: The type of filter you'd like to apply to your search. Allowed Values: , current_period_ends_at,
                current_period_starts_at, created_at, activated_at, canceled_at, expires_at, trial_started_at,
                trial_ended_at, updated_at
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use
                in query ``start_date=2022-07-01``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2022-08-01``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time provided in query. You can specify
                timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be
                used instead of end_date. Use in query ``end_datetime=2022-08-01 10:00:05``.
            metadata: The value of the metadata field specified in the parameter. Use in query
                ``metadata[my-field]=value&metadata[other-field]=another_value``.
            group_status: Filter by whether a subscription is in a group.
            dunning_exemption: Filter by dunning exemption status.
            payment_gateways: Comma-separated payment gateway identifiers.
            currencies: Comma-separated currency codes.
            include: Allows including additional data in the response. Use in query:
                ``include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SubscriptionSortOrStr | None]("sort", sort),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[SubscriptionStateFilterOrStr | None]("state", state),
                param[Product1 | Product1Dict | None]("product", product),
                param[str | None]("q", q),
                param[QScopeOrStr | None]("q_scope", q_scope),
                param[int | None]("customer_id", customer_id),
                param[int | None]("product_price_point_id", product_price_point_id),
                param[int | None]("coupon", coupon),
                param[str | None]("coupon_code", coupon_code),
                param[CollectionMethod1OrStr | None]("collection_method", collection_method),
                param[int | None]("branding_theme_id", branding_theme_id),
                param[SubscriptionDateFieldOrStr | None]("date_field", date_field),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[dict[str, str] | None]("metadata", metadata),
                param[GroupStatusOrStr | None]("group_status", group_status),
                param[bool | None]("dunning_exemption", dunning_exemption),
                param[str | None]("payment_gateways", payment_gateways),
                param[str | None]("currencies", currencies),
                param[list[SubscriptionListIncludeOrStr] | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[SubscriptionResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def override_subscription(
        self,
        subscription_id: int,
        *,
        body: OverrideSubscriptionRequest | OverrideSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, OverrideSubscriptionErrorBody]:
        """Sets certain subscription fields that are usually managed automatically. Some of the fields can be set via
        the normal Subscriptions Update API, but others can only be set using this endpoint.

        This endpoint is provided for cases where you need to “align” Advanced Billing data with data that happened in
        your system, perhaps before you started using Advanced Billing. For example, you may choose to import your
        historical subscription data, and would like the activation and cancellation dates in Advanced Billing to match
        your existing historical dates. Advanced Billing does not backfill historical events (i.e. from the Events API),
        but some static data can be changed via this API.

        Why are some fields only settable from this endpoint, and not the normal subscription create and update
        endpoints? Because we want users of this endpoint to be aware that these fields are usually managed by Advanced
        Billing, and using this API means **you are stepping out on your own.**

        Changing these fields will not affect any other attributes. For example, adding an expiration date will not
        affect the next assessment date on the subscription.

        If you regularly need to override the current_period_starts_at for new subscriptions, this can also be
        accomplished by setting both ``previous_billing_at`` and ``next_billing_at`` at subscription creation. See the
        documentation on `Importing Subscriptions <./b3A6MTQxMDgzODg-create-subscription#subscriptions-import>`__ for
        more information.

        ## Limitations

        When passing ``current_period_starts_at`` some validations are made:

        1. The subscription needs to be unbilled (no statements or invoices).
        2. The value passed must be a valid date/time. We recommend using the iso 8601 format.
        3. The value passed must be before the current date/time.

        If unpermitted parameters are sent, a 400 HTTP response is sent along with a string giving the reason for the
        problem.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: Only these fields are available to be set.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/override.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OverrideSubscriptionRequest | OverrideSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=override_subscription_error_mapper,
            request_options=request_options,
        )

    async def preview_subscription(
        self,
        *,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionPreviewResponse, RawError]:
        """Previews a subscription by POSTing the same JSON or XML as for a subscription creation.

        The "Next Billing" amount and "Next Billing" date are represented in each Subscriber's Summary.

        This endpoint does not create a subscription; it is meant to serve as a prediction.

        For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Subscriptions can now work independently from the catalog

         If you have the new `Catalog experience
            <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, you can
            create subscriptions without a ``product_id`` or ``product_handle`` using POST /subscriptions, building them
            entirely from components.

        A valid subscription must include at least one active component with:
        - a positive ``allocated_quantity``,
        - a positive ``unit_balance``, or
        - 'enabled: true' (for on/off components)

        ``component_id`` can be provided as a numeric ID or in handle: format. If ``trial_interval`` and
        ``trial_interval_unit`` are included, they are applied at creation.

        In the response, product and product price point fields are null, and component details are returned instead.

        This functionality is supported in the API, but is not currently supported in SDKs.

        ## Taxable Subscriptions

        This endpoint previews taxes applicable to a purchase. For taxes to be previewed, the following conditions must
        be met:

        + Taxes must be configured on the subscription
        + The preview must be for the purchase of a taxable product or component, or combination of the two.
        + The subscription payload must contain a full billing or shipping address to calculate tax

        For more information about creating taxable previews, see `Taxes
        <https://maxio.zendesk.com/hc/en-us/sections/24287012349325-Taxes>`__.

        You do **not** need to include a card number to generate tax information when you are previewing a subscription.
        However, when you actually want to create the subscription, you must include the credit card information if you
        want the billing address to be stored. The billing address and the credit card information are stored together
        within the payment profile object. Also, you cannot send a billing address without payment profile information,
        as the address is stored on the card.

        You can pass shipping and billing addresses and still decide not to calculate taxes. To do that, pass
        ``skip_billing_manifest_taxes: true`` attribute.

        ## Non-taxable Subscriptions

        If you'd like to calculate subscriptions that do not include tax, you can leave off the billing information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/preview.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionPreviewResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def purge_subscription(
        self,
        subscription_id: int,
        ack: int,
        *,
        cascade: list[SubscriptionPurgeTypeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, PurgeSubscriptionErrorBody]:
        """Purges an individual subscription for sites in test mode.

        Provide the subscription ID in the URL. To confirm, supply the customer ID in the query string ``ack``
        parameter. You may also delete the customer record and/or payment profiles by passing ``cascade`` parameters.
        For example, to delete just the customer record, the query params would be:
        ``?ack={customer_id}&cascade[]=customer``

        If you need to remove subscriptions from a live site, contact support to discuss your use case.

        ### Delete customer and payment profile

        The query params will be: ``?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile``

        Args:
            subscription_id: The Chargify id of the subscription.
            ack: id of the customer.
            cascade: Options are "customer" or "payment_profile". Use in query:
                ``cascade[]=customer&cascade[]=payment_profile``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/purge.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[int]("ack", ack), param[list[SubscriptionPurgeTypeOrStr] | None]("cascade", cascade)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=purge_subscription_error_mapper,
            request_options=request_options,
        )

    async def read_subscription(
        self,
        subscription_id: int,
        *,
        include: list[SubscriptionIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, RawError]:
        """Retrieves subscription details.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, 'product',
        'product_price_point_id', and 'product_price_point_type' are returned as 'null'.

        ## Self-Service Page token

        Self-Service Page token for the subscription is not returned by default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the request.

        Args:
            subscription_id: The Chargify id of the subscription.
            include: Allows including additional data in the response. Use in query:
                ``include[]=coupons&include[]=self_service_page_token``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[list[SubscriptionIncludeOrStr] | None]("include", include)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_coupon_from_subscription(
        self,
        subscription_id: int,
        *,
        coupon_code: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, RemoveCouponFromSubscriptionErrorBody]:
        """Removes a coupon from an existing subscription.

        For more information on the expected behavior of removing a coupon from a subscription, see `Coupons and
        Subscriptions
        <https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coupons-and-Subscriptions#removing-a-coupon>`__.

        Args:
            subscription_id: The Chargify id of the subscription.
            coupon_code: The coupon code
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/remove_coupon.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[param[str | None]("coupon_code", coupon_code)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[str],
            error_mapper=remove_coupon_from_subscription_error_mapper,
            request_options=request_options,
        )

    async def update_prepaid_subscription_configuration(
        self,
        subscription_id: int,
        *,
        body: UpsertPrepaidConfigurationRequest | UpsertPrepaidConfigurationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PrepaidConfigurationResponse, UpdatePrepaidSubscriptionConfigurationErrorBody]:
        """Updates a subscription's prepaid configuration.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/prepaid_configurations.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertPrepaidConfigurationRequest | UpsertPrepaidConfigurationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PrepaidConfigurationResponse],
            error_mapper=update_prepaid_subscription_configuration_error_mapper,
            request_options=request_options,
        )

    async def update_subscription(
        self,
        subscription_id: int,
        *,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, UpdateSubscriptionErrorBody]:
        """Updates one or more attributes of a subscription.

        ## Update Subscription Payment Method

        Change the card that your subscriber uses for their subscription. You can also use this method to change the
        expiration date of the card **if your gateway allows**.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        > Note: Partial card updates for **Authorize.Net** are not allowed via this endpoint. The existing Payment
            Profile must be directly updated instead.

        ## Update Product

        You also use this method to change the subscription to a different product by setting a new value for
        product_handle. A product change can be done in two different ways, **product change** or **delayed product
        change**.

        ### Product Change

        You can change a subscription's product. The new payment amount is calculated and charged at the normal start of
        the next period. If you require complex product changes or prorated upgrades and downgrades instead, please see
        the documentation on `Migrating Subscription Products
        <https://docs.maxio.com/hc/en-us/articles/24252069837581-Product-Changes-and-Migrations#product-changes-and-migrations-0-0>`__.

        To perform a product change, set either the ``product_handle`` or ``product_id`` attribute to that of a
        different product from the same site as the subscription. You can also change the price point by passing in
        either ``product_price_point_id`` or ``product_price_point_handle`` - otherwise the new product's default price
        point is used.

        ### Delayed Product Change

        This method also changes the product and/or price point, and the new payment amount is calculated and charged at
        the normal start of the next period.

        This method schedules the product change to happen automatically at the subscription’s next renewal date. To
        perform a delayed product change, set the ``product_handle`` attribute as you would in a regular product change,
        but also set the ``product_change_delayed`` attribute to ``true``. No proration applies in this case.

        You can also perform a delayed change to the price point by passing in either ``product_price_point_id`` or
        ``product_price_point_handle``

        > **Note:** To cancel a delayed product change, set ``next_product_id`` to an empty string.

        ## Billing Date Changes

        You can update dates for a subscription.

        ### Regular Billing Date Changes

        Send the ``next_billing_at`` to set the next billing date for the subscription. After that date passes and the
        subscription is processed, the following billing date will be set according to the subscription's product
        period.

        > Note: If you pass an invalid date, the correct date is automatically set to the correct date. For example, if
            February 30 is passed, the next billing would be set to March 2nd in a non-leap year.

        The server response will not return data under the key/value pair of ``next_billing_at``. View the key/value
        pair of ``current_period_ends_at`` to verify that the ``next_billing_at`` date has been changed successfully.

        ### Calendar Billing and Snap Day Changes

        For a subscription using Calendar Billing, setting the next billing date is a bit different. Send the
        ``snap_day`` attribute to change the calendar billing date for **a subscription using a product eligible for
        calendar billing**.

        > Note: If you change the product associated with a subscription that contains a ``snap_day`` and immediately
            READ/GET the subscription data, it will still contain the original ``snap_day``. The ``snap_day`` will be
            reset to ``null`` on the next billing cycle. This is because a product change is instantaneous and only
            affects the product associated with a subscription.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, some
        subscriptions may not have an associated product. For subscriptions without an associated product, ``product``,
        ``product_price_point_id``, and ``product_price_point_type`` are returned as ``null``.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionRequest | UpdateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=update_subscription_error_mapper,
            request_options=request_options,
        )
