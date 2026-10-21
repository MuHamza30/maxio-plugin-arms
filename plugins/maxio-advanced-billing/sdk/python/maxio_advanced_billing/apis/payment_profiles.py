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
from ..errors.change_subscription_default_payment_profile_error import (
    ChangeSubscriptionDefaultPaymentProfileErrorBody,
    change_subscription_default_payment_profile_error_mapper,
)
from ..errors.change_subscription_group_default_payment_profile_error import (
    ChangeSubscriptionGroupDefaultPaymentProfileErrorBody,
    change_subscription_group_default_payment_profile_error_mapper,
)
from ..errors.create_payment_profile_error import CreatePaymentProfileErrorBody, create_payment_profile_error_mapper
from ..errors.delete_unused_payment_profile_error import (
    DeleteUnusedPaymentProfileErrorBody,
    delete_unused_payment_profile_error_mapper,
)
from ..errors.read_one_time_token_error import ReadOneTimeTokenErrorBody, read_one_time_token_error_mapper
from ..errors.read_payment_profile_error import ReadPaymentProfileErrorBody, read_payment_profile_error_mapper
from ..errors.send_request_update_payment_email_error import (
    SendRequestUpdatePaymentEmailErrorBody,
    send_request_update_payment_email_error_mapper,
)
from ..errors.update_payment_profile_error import UpdatePaymentProfileErrorBody, update_payment_profile_error_mapper
from ..errors.verify_bank_account_error import VerifyBankAccountErrorBody, verify_bank_account_error_mapper
from ..models.bank_account_response import BankAccountResponse
from ..models.bank_account_verification_request import (
    BankAccountVerificationRequest,
    BankAccountVerificationRequestDict,
)
from ..models.create_payment_profile_request import CreatePaymentProfileRequest, CreatePaymentProfileRequestDict
from ..models.get_one_time_token_request import GetOneTimeTokenRequest
from ..models.payment_profile_response import PaymentProfileResponse
from ..models.update_payment_profile_request import UpdatePaymentProfileRequest, UpdatePaymentProfileRequestDict
from ..server.server import Server


class PaymentProfiles:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentProfilesWithRawResponse(client, server, auth)

    def change_subscription_default_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentProfileResponse:
        """Changes the default payment profile on the subscription to the existing payment profile with the specified
        ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.change_subscription_default_payment_profile(
                subscription_id, payment_profile_id, request_options=request_options
            ),
        )

    def change_subscription_group_default_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentProfileResponse:
        """Changes the default payment profile on the subscription group to the existing payment profile with the
        specified ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        The new payment profile must belong to the subscription group's customer, otherwise you will receive an error.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.change_subscription_group_default_payment_profile(
                uid, payment_profile_id, request_options=request_options
            ),
        )

    def create_payment_profile(
        self,
        *,
        body: CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentProfileResponse:
        """Creates a payment profile for a customer.

        When you create a new payment profile for a customer via the API, it does not automatically make the profile
        current for any of the customer’s subscriptions. To use the payment profile as the default, you must set it
        explicitly for the subscription or subscription group.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating payment profiles.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        See the following articles to learn more about subscriptions and payments:

        + `Subscriber Payment Details
            <https://maxio.zendesk.com/hc/en-us/articles/24251599929613-Subscription-Summary-Payment-Details-Tab>`__
        + `Self Service Pages <https://maxio.zendesk.com/hc/en-us/articles/24261425318541-Self-Service-Pages>`__ (Allows
            credit card updates by Subscriber)
        + `Public Signup Pages payment settings
            <https://maxio.zendesk.com/hc/en-us/articles/24261368332557-Individual-Page-Settings>`__
        + `Taxes <https://developers.chargify.com/docs/developer-docs/d2e9e34db740e-signups#taxes>`__
        + `Maxio.js (formerly Chargify.js)
            <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview>`__
            + `Maxio.js with GoCardless - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQZKCER8CFK40MR6XJ>`__
            + `Maxio.js with GoCardless - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QR09JVHWW0MCA7HVJV>`__
            + `Maxio.js with Stripe Direct Debit - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQFKKN8Z7B7DZ9AJS5>`__
            + `Maxio.js with Stripe Direct Debit - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QRECQQ4ECS3ZA55GY7>`__
            + `Maxio.js with Stripe BECS Direct Debit - minimal example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-gateway>`__
            + `Maxio.js with Stripe BECS Direct Debit - full example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#full-example-with-sepa-direct-debit-stripe-gateway>`__
        + `Full documentation on GoCardless <https://maxio.zendesk.com/hc/en-us/articles/24176159136909-GoCardless>`__
        + `Full documentation on Stripe SEPA Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BECS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BACS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: When following the IBAN or the Local Bank details examples, a customer, bank account and mandate will
                be created in your current vault. If the customer, bank account, and mandate already exist in your
                vault, follow the Import example to link the payment profile into Advanced Billing.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_payment_profile(body=body, request_options=request_options))

    def delete_subscription_group_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a Payment Profile belonging to a Subscription Group.

        **Note**: If the Payment Profile belongs to multiple Subscription Groups and/or Subscriptions, it will be
        removed from all of them.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_subscription_group_payment_profile(
                uid, payment_profile_id, request_options=request_options
            ),
        )

    def delete_subscriptions_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a payment profile belonging to the customer on the subscription.

        If the customer has multiple subscriptions, the payment profile is removed from all of them.

        If you delete the default payment profile for a subscription, you need to specify another payment profile to be
        the default through the API, or either prompt the user to enter a card in the billing portal or on the
        self-service page, or visit the Payment Details tab on the subscription in the Admin UI and use the “Add New
        Credit Card” or “Make Active Payment Method” link, (depending on whether there are other cards present).

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_subscriptions_payment_profile(
                subscription_id, payment_profile_id, request_options=request_options
            ),
        )

    def delete_unused_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes an unused payment profile.

        If the payment profile is in use by one or more subscriptions or groups, an error message is returned.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.delete_unused_payment_profile(payment_profile_id, request_options=request_options)
        )

    def list_payment_profiles(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        customer_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PaymentProfileResponse]:
        """Lists all active payment profiles for a site, or for one customer within a site. If no payment profiles are
        found, this endpoint returns an empty array.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            customer_id: The ID of the customer for which you wish to list payment profiles
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_payment_profiles(
                page=page, per_page=per_page, customer_id=customer_id, request_options=request_options
            ),
        )

    def read_one_time_token(
        self, chargify_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOneTimeTokenRequest:
        """Returns the one-time token data, including credit card or ACH details, associated with the provided token ID.
        One Time Tokens aka Advanced Billing Tokens house the credit card or ACH (Authorize.Net or Stripe only) data for
        a customer.

        You can use One Time Tokens while creating a subscription or payment profile instead of passing all bank account
        or credit card data directly to a given API endpoint.

        To obtain a One Time Token you have to use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__.

        Args:
            chargify_token: Advanced Billing Token
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.read_one_time_token(chargify_token, request_options=request_options))

    def read_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentProfileResponse:
        """Returns a payment profile identified by its unique ID.

        Note that a different JSON object will be returned if the card method on file is a bank account.

        ### Response for Bank Account

        Example response for Bank Account:

        ```
        {
          "payment_profile": {
            "id": 10089892,
            "first_name": "Chester",
            "last_name": "Tester",
            "created_at": "2025-01-01T00:00:00-05:00",
            "updated_at": "2025-01-01T00:00:00-05:00",
            "customer_id": 14543792,
            "current_vault": "bogus",
            "vault_token": "0011223344",
            "billing_address": "456 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "customer_vault_token": null,
            "billing_address_2": "",
            "bank_name": "Bank of Kansas City",
            "masked_bank_routing_number": "XXXX6789",
            "masked_bank_account_number": "XXXX3344",
            "bank_account_type": "checking",
            "bank_account_holder_type": "personal",
            "payment_type": "bank_account",
            "site_gateway_setting_id": 1,
            "gateway_handle": null
          }
        }
        ```

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.read_payment_profile(payment_profile_id, request_options=request_options))

    def send_request_update_payment_email(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Sends a "request payment update" email to the customer associated with the subscription.

        If you attempt to send a "request payment update" email more than five times within a 30-minute period, you will
        receive a ``422`` response with an error message in the body. This error message will indicate that the request
        has been rejected due to excessive attempts, and will provide instructions on how to resubmit the request.

        Additionally, if you attempt to send a "request payment update" email for a subscription that does not exist,
        you will receive a ``404`` error response. This error message will indicate that the subscription could not be
        found, and will provide instructions on how to correct the error and resubmit the request.

        These error responses are designed to prevent excessive or invalid requests, and to provide clear and helpful
        information to users who encounter errors during the request process.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.send_request_update_payment_email(subscription_id, request_options=request_options)
        )

    def update_payment_profile(
        self,
        payment_profile_id: int,
        *,
        body: UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentProfileResponse:
        """Updates a payment profile.

        ## Partial Card Updates

        In the event that you are using the Authorize.net, Stripe, Cybersource, Forte or Braintree Blue payment
        gateways, you can update just the billing and contact information for a payment method. Note the lack of
        credit-card related data contained in the JSON payload.

        In this case, the following JSON is acceptable:

        ```
        {
          "payment_profile": {
            "first_name": "Kelly",
            "last_name": "Test",
            "billing_address": "789 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "billing_address_2": null
          }
        }
        ```

        The result will be that you have updated the billing information for the card, yet retained the original card
        number data.

        ## Specific notes on updating payment profiles

        - Merchants with **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe** as their
            payment gateway can update their Customer’s credit cards without passing in the full credit card number and
            CVV.

        - If you are using **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe**, Advanced
            Billing will ignore the credit card number and CVV when processing an update via the API, and attempt a
            partial update instead. If you wish to change the card number on a payment profile, you will need to create
            a new payment profile for the given customer.

        - A Payment Profile cannot be updated with the attributes of another type of Payment Profile. For example, if
            the payment profile you are attempting to update is a credit card, you cannot pass in bank account
            attributes (like ``bank_account_number``), and vice versa.

        - Updating a payment profile directly will not trigger an attempt to capture a past-due balance. If this is the
            intent, update the card details via the Subscription instead.

        - If you are using Authorize.net or Stripe, you may elect to manually trigger a retry for a past due
            subscription after a partial update.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorStringMapResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_payment_profile(
                payment_profile_id, body=body, request_options=request_options
            ),
        )

    def verify_bank_account(
        self,
        bank_account_id: int,
        *,
        body: BankAccountVerificationRequest | BankAccountVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankAccountResponse:
        """Verifies a bank account. Submit the two small deposit amounts the customer received in their bank account to
        verify the bank account. (Stripe only)

        Args:
            bank_account_id: Identifier of the bank account in the system.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.verify_bank_account(bank_account_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> PaymentProfilesWithRawResponse:
        return self._with_raw_response


class AsyncPaymentProfiles:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentProfilesWithRawResponse(client, server, auth)

    async def change_subscription_default_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentProfileResponse:
        """Changes the default payment profile on the subscription to the existing payment profile with the specified
        ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.change_subscription_default_payment_profile(
                subscription_id, payment_profile_id, request_options=request_options
            ),
        )

    async def change_subscription_group_default_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentProfileResponse:
        """Changes the default payment profile on the subscription group to the existing payment profile with the
        specified ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        The new payment profile must belong to the subscription group's customer, otherwise you will receive an error.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.change_subscription_group_default_payment_profile(
                uid, payment_profile_id, request_options=request_options
            ),
        )

    async def create_payment_profile(
        self,
        *,
        body: CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentProfileResponse:
        """Creates a payment profile for a customer.

        When you create a new payment profile for a customer via the API, it does not automatically make the profile
        current for any of the customer’s subscriptions. To use the payment profile as the default, you must set it
        explicitly for the subscription or subscription group.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating payment profiles.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        See the following articles to learn more about subscriptions and payments:

        + `Subscriber Payment Details
            <https://maxio.zendesk.com/hc/en-us/articles/24251599929613-Subscription-Summary-Payment-Details-Tab>`__
        + `Self Service Pages <https://maxio.zendesk.com/hc/en-us/articles/24261425318541-Self-Service-Pages>`__ (Allows
            credit card updates by Subscriber)
        + `Public Signup Pages payment settings
            <https://maxio.zendesk.com/hc/en-us/articles/24261368332557-Individual-Page-Settings>`__
        + `Taxes <https://developers.chargify.com/docs/developer-docs/d2e9e34db740e-signups#taxes>`__
        + `Maxio.js (formerly Chargify.js)
            <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview>`__
            + `Maxio.js with GoCardless - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQZKCER8CFK40MR6XJ>`__
            + `Maxio.js with GoCardless - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QR09JVHWW0MCA7HVJV>`__
            + `Maxio.js with Stripe Direct Debit - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQFKKN8Z7B7DZ9AJS5>`__
            + `Maxio.js with Stripe Direct Debit - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QRECQQ4ECS3ZA55GY7>`__
            + `Maxio.js with Stripe BECS Direct Debit - minimal example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-gateway>`__
            + `Maxio.js with Stripe BECS Direct Debit - full example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#full-example-with-sepa-direct-debit-stripe-gateway>`__
        + `Full documentation on GoCardless <https://maxio.zendesk.com/hc/en-us/articles/24176159136909-GoCardless>`__
        + `Full documentation on Stripe SEPA Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BECS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BACS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: When following the IBAN or the Local Bank details examples, a customer, bank account and mandate will
                be created in your current vault. If the customer, bank account, and mandate already exist in your
                vault, follow the Import example to link the payment profile into Advanced Billing.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_payment_profile(body=body, request_options=request_options))

    async def delete_subscription_group_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a Payment Profile belonging to a Subscription Group.

        **Note**: If the Payment Profile belongs to multiple Subscription Groups and/or Subscriptions, it will be
        removed from all of them.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_subscription_group_payment_profile(
                uid, payment_profile_id, request_options=request_options
            ),
        )

    async def delete_subscriptions_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a payment profile belonging to the customer on the subscription.

        If the customer has multiple subscriptions, the payment profile is removed from all of them.

        If you delete the default payment profile for a subscription, you need to specify another payment profile to be
        the default through the API, or either prompt the user to enter a card in the billing portal or on the
        self-service page, or visit the Payment Details tab on the subscription in the Admin UI and use the “Add New
        Credit Card” or “Make Active Payment Method” link, (depending on whether there are other cards present).

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_subscriptions_payment_profile(
                subscription_id, payment_profile_id, request_options=request_options
            ),
        )

    async def delete_unused_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes an unused payment profile.

        If the payment profile is in use by one or more subscriptions or groups, an error message is returned.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_unused_payment_profile(
                payment_profile_id, request_options=request_options
            ),
        )

    async def list_payment_profiles(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        customer_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PaymentProfileResponse]:
        """Lists all active payment profiles for a site, or for one customer within a site. If no payment profiles are
        found, this endpoint returns an empty array.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            customer_id: The ID of the customer for which you wish to list payment profiles
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_payment_profiles(
                page=page, per_page=per_page, customer_id=customer_id, request_options=request_options
            ),
        )

    async def read_one_time_token(
        self, chargify_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOneTimeTokenRequest:
        """Returns the one-time token data, including credit card or ACH details, associated with the provided token ID.
        One Time Tokens aka Advanced Billing Tokens house the credit card or ACH (Authorize.Net or Stripe only) data for
        a customer.

        You can use One Time Tokens while creating a subscription or payment profile instead of passing all bank account
        or credit card data directly to a given API endpoint.

        To obtain a One Time Token you have to use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__.

        Args:
            chargify_token: Advanced Billing Token
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.read_one_time_token(chargify_token, request_options=request_options)
        )

    async def read_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentProfileResponse:
        """Returns a payment profile identified by its unique ID.

        Note that a different JSON object will be returned if the card method on file is a bank account.

        ### Response for Bank Account

        Example response for Bank Account:

        ```
        {
          "payment_profile": {
            "id": 10089892,
            "first_name": "Chester",
            "last_name": "Tester",
            "created_at": "2025-01-01T00:00:00-05:00",
            "updated_at": "2025-01-01T00:00:00-05:00",
            "customer_id": 14543792,
            "current_vault": "bogus",
            "vault_token": "0011223344",
            "billing_address": "456 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "customer_vault_token": null,
            "billing_address_2": "",
            "bank_name": "Bank of Kansas City",
            "masked_bank_routing_number": "XXXX6789",
            "masked_bank_account_number": "XXXX3344",
            "bank_account_type": "checking",
            "bank_account_holder_type": "personal",
            "payment_type": "bank_account",
            "site_gateway_setting_id": 1,
            "gateway_handle": null
          }
        }
        ```

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_payment_profile(payment_profile_id, request_options=request_options)
        )

    async def send_request_update_payment_email(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Sends a "request payment update" email to the customer associated with the subscription.

        If you attempt to send a "request payment update" email more than five times within a 30-minute period, you will
        receive a ``422`` response with an error message in the body. This error message will indicate that the request
        has been rejected due to excessive attempts, and will provide instructions on how to resubmit the request.

        Additionally, if you attempt to send a "request payment update" email for a subscription that does not exist,
        you will receive a ``404`` error response. This error message will indicate that the subscription could not be
        found, and will provide instructions on how to correct the error and resubmit the request.

        These error responses are designed to prevent excessive or invalid requests, and to provide clear and helpful
        information to users who encounter errors during the request process.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.send_request_update_payment_email(
                subscription_id, request_options=request_options
            ),
        )

    async def update_payment_profile(
        self,
        payment_profile_id: int,
        *,
        body: UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentProfileResponse:
        """Updates a payment profile.

        ## Partial Card Updates

        In the event that you are using the Authorize.net, Stripe, Cybersource, Forte or Braintree Blue payment
        gateways, you can update just the billing and contact information for a payment method. Note the lack of
        credit-card related data contained in the JSON payload.

        In this case, the following JSON is acceptable:

        ```
        {
          "payment_profile": {
            "first_name": "Kelly",
            "last_name": "Test",
            "billing_address": "789 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "billing_address_2": null
          }
        }
        ```

        The result will be that you have updated the billing information for the card, yet retained the original card
        number data.

        ## Specific notes on updating payment profiles

        - Merchants with **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe** as their
            payment gateway can update their Customer’s credit cards without passing in the full credit card number and
            CVV.

        - If you are using **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe**, Advanced
            Billing will ignore the credit card number and CVV when processing an update via the API, and attempt a
            partial update instead. If you wish to change the card number on a payment profile, you will need to create
            a new payment profile for the given customer.

        - A Payment Profile cannot be updated with the attributes of another type of Payment Profile. For example, if
            the payment profile you are attempting to update is a credit card, you cannot pass in bank account
            attributes (like ``bank_account_number``), and vice versa.

        - Updating a payment profile directly will not trigger an attempt to capture a past-due balance. If this is the
            intent, update the card details via the Subscription instead.

        - If you are using Authorize.net or Stripe, you may elect to manually trigger a retry for a past due
            subscription after a partial update.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorStringMapResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_payment_profile(
                payment_profile_id, body=body, request_options=request_options
            ),
        )

    async def verify_bank_account(
        self,
        bank_account_id: int,
        *,
        body: BankAccountVerificationRequest | BankAccountVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankAccountResponse:
        """Verifies a bank account. Submit the two small deposit amounts the customer received in their bank account to
        verify the bank account. (Stripe only)

        Args:
            bank_account_id: Identifier of the bank account in the system.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.verify_bank_account(
                bank_account_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncPaymentProfilesWithRawResponse:
        return self._with_raw_response


class PaymentProfilesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def change_subscription_default_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentProfileResponse, ChangeSubscriptionDefaultPaymentProfileErrorBody]:
        """Changes the default payment profile on the subscription to the existing payment profile with the specified
        ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_payment_profile.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id), param[int]("payment_profile_id", payment_profile_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PaymentProfileResponse],
            error_mapper=change_subscription_default_payment_profile_error_mapper,
            request_options=request_options,
        )

    def change_subscription_group_default_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentProfileResponse, ChangeSubscriptionGroupDefaultPaymentProfileErrorBody]:
        """Changes the default payment profile on the subscription group to the existing payment profile with the
        specified ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        The new payment profile must belong to the subscription group's customer, otherwise you will receive an error.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscription_groups/{uid}/payment_profiles/{payment_profile_id}/change_payment_profile.json"
            ),
            path_params=[param[str]("uid", uid), param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PaymentProfileResponse],
            error_mapper=change_subscription_group_default_payment_profile_error_mapper,
            request_options=request_options,
        )

    def create_payment_profile(
        self,
        *,
        body: CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentProfileResponse, CreatePaymentProfileErrorBody]:
        """Creates a payment profile for a customer.

        When you create a new payment profile for a customer via the API, it does not automatically make the profile
        current for any of the customer’s subscriptions. To use the payment profile as the default, you must set it
        explicitly for the subscription or subscription group.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating payment profiles.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        See the following articles to learn more about subscriptions and payments:

        + `Subscriber Payment Details
            <https://maxio.zendesk.com/hc/en-us/articles/24251599929613-Subscription-Summary-Payment-Details-Tab>`__
        + `Self Service Pages <https://maxio.zendesk.com/hc/en-us/articles/24261425318541-Self-Service-Pages>`__ (Allows
            credit card updates by Subscriber)
        + `Public Signup Pages payment settings
            <https://maxio.zendesk.com/hc/en-us/articles/24261368332557-Individual-Page-Settings>`__
        + `Taxes <https://developers.chargify.com/docs/developer-docs/d2e9e34db740e-signups#taxes>`__
        + `Maxio.js (formerly Chargify.js)
            <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview>`__
            + `Maxio.js with GoCardless - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQZKCER8CFK40MR6XJ>`__
            + `Maxio.js with GoCardless - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QR09JVHWW0MCA7HVJV>`__
            + `Maxio.js with Stripe Direct Debit - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQFKKN8Z7B7DZ9AJS5>`__
            + `Maxio.js with Stripe Direct Debit - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QRECQQ4ECS3ZA55GY7>`__
            + `Maxio.js with Stripe BECS Direct Debit - minimal example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-gateway>`__
            + `Maxio.js with Stripe BECS Direct Debit - full example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#full-example-with-sepa-direct-debit-stripe-gateway>`__
        + `Full documentation on GoCardless <https://maxio.zendesk.com/hc/en-us/articles/24176159136909-GoCardless>`__
        + `Full documentation on Stripe SEPA Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BECS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BACS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: When following the IBAN or the Local Bank details examples, a customer, bank account and mandate will
                be created in your current vault. If the customer, bank account, and mandate already exist in your
                vault, follow the Import example to link the payment profile into Advanced Billing.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/payment_profiles.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PaymentProfileResponse],
            error_mapper=create_payment_profile_error_mapper,
            request_options=request_options,
        )

    def delete_subscription_group_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a Payment Profile belonging to a Subscription Group.

        **Note**: If the Payment Profile belongs to multiple Subscription Groups and/or Subscriptions, it will be
        removed from all of them.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscription_groups/{uid}/payment_profiles/{payment_profile_id}.json"
            ),
            path_params=[param[str]("uid", uid), param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_subscriptions_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a payment profile belonging to the customer on the subscription.

        If the customer has multiple subscriptions, the payment profile is removed from all of them.

        If you delete the default payment profile for a subscription, you need to specify another payment profile to be
        the default through the API, or either prompt the user to enter a card in the billing portal or on the
        self-service page, or visit the Payment Details tab on the subscription in the Admin UI and use the “Add New
        Credit Card” or “Make Active Payment Method” link, (depending on whether there are other cards present).

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id), param[int]("payment_profile_id", payment_profile_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_unused_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteUnusedPaymentProfileErrorBody]:
        """Deletes an unused payment profile.

        If the payment profile is in use by one or more subscriptions or groups, an error message is returned.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/payment_profiles/{payment_profile_id}.json"),
            path_params=[param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_unused_payment_profile_error_mapper,
            request_options=request_options,
        )

    def list_payment_profiles(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        customer_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PaymentProfileResponse], RawError]:
        """Lists all active payment profiles for a site, or for one customer within a site. If no payment profiles are
        found, this endpoint returns an empty array.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            customer_id: The ID of the customer for which you wish to list payment profiles
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/payment_profiles.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("customer_id", customer_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[PaymentProfileResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_one_time_token(
        self, chargify_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOneTimeTokenRequest, ReadOneTimeTokenErrorBody]:
        """Returns the one-time token data, including credit card or ACH details, associated with the provided token ID.
        One Time Tokens aka Advanced Billing Tokens house the credit card or ACH (Authorize.Net or Stripe only) data for
        a customer.

        You can use One Time Tokens while creating a subscription or payment profile instead of passing all bank account
        or credit card data directly to a given API endpoint.

        To obtain a One Time Token you have to use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__.

        Args:
            chargify_token: Advanced Billing Token
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/one_time_tokens/{chargify_token}.json"),
            path_params=[param[str]("chargify_token", chargify_token)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[GetOneTimeTokenRequest],
            error_mapper=read_one_time_token_error_mapper,
            request_options=request_options,
        )

    def read_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentProfileResponse, ReadPaymentProfileErrorBody]:
        """Returns a payment profile identified by its unique ID.

        Note that a different JSON object will be returned if the card method on file is a bank account.

        ### Response for Bank Account

        Example response for Bank Account:

        ```
        {
          "payment_profile": {
            "id": 10089892,
            "first_name": "Chester",
            "last_name": "Tester",
            "created_at": "2025-01-01T00:00:00-05:00",
            "updated_at": "2025-01-01T00:00:00-05:00",
            "customer_id": 14543792,
            "current_vault": "bogus",
            "vault_token": "0011223344",
            "billing_address": "456 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "customer_vault_token": null,
            "billing_address_2": "",
            "bank_name": "Bank of Kansas City",
            "masked_bank_routing_number": "XXXX6789",
            "masked_bank_account_number": "XXXX3344",
            "bank_account_type": "checking",
            "bank_account_holder_type": "personal",
            "payment_type": "bank_account",
            "site_gateway_setting_id": 1,
            "gateway_handle": null
          }
        }
        ```

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/payment_profiles/{payment_profile_id}.json"),
            path_params=[param[int]("payment_profile_id", payment_profile_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PaymentProfileResponse],
            error_mapper=read_payment_profile_error_mapper,
            request_options=request_options,
        )

    def send_request_update_payment_email(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SendRequestUpdatePaymentEmailErrorBody]:
        """Sends a "request payment update" email to the customer associated with the subscription.

        If you attempt to send a "request payment update" email more than five times within a 30-minute period, you will
        receive a ``422`` response with an error message in the body. This error message will indicate that the request
        has been rejected due to excessive attempts, and will provide instructions on how to resubmit the request.

        Additionally, if you attempt to send a "request payment update" email for a subscription that does not exist,
        you will receive a ``404`` error response. This error message will indicate that the subscription could not be
        found, and will provide instructions on how to correct the error and resubmit the request.

        These error responses are designed to prevent excessive or invalid requests, and to provide clear and helpful
        information to users who encounter errors during the request process.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/request_payment_profiles_update.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=send_request_update_payment_email_error_mapper,
            request_options=request_options,
        )

    def update_payment_profile(
        self,
        payment_profile_id: int,
        *,
        body: UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentProfileResponse, UpdatePaymentProfileErrorBody]:
        """Updates a payment profile.

        ## Partial Card Updates

        In the event that you are using the Authorize.net, Stripe, Cybersource, Forte or Braintree Blue payment
        gateways, you can update just the billing and contact information for a payment method. Note the lack of
        credit-card related data contained in the JSON payload.

        In this case, the following JSON is acceptable:

        ```
        {
          "payment_profile": {
            "first_name": "Kelly",
            "last_name": "Test",
            "billing_address": "789 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "billing_address_2": null
          }
        }
        ```

        The result will be that you have updated the billing information for the card, yet retained the original card
        number data.

        ## Specific notes on updating payment profiles

        - Merchants with **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe** as their
            payment gateway can update their Customer’s credit cards without passing in the full credit card number and
            CVV.

        - If you are using **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe**, Advanced
            Billing will ignore the credit card number and CVV when processing an update via the API, and attempt a
            partial update instead. If you wish to change the card number on a payment profile, you will need to create
            a new payment profile for the given customer.

        - A Payment Profile cannot be updated with the attributes of another type of Payment Profile. For example, if
            the payment profile you are attempting to update is a credit card, you cannot pass in bank account
            attributes (like ``bank_account_number``), and vice versa.

        - Updating a payment profile directly will not trigger an attempt to capture a past-due balance. If this is the
            intent, update the card details via the Subscription instead.

        - If you are using Authorize.net or Stripe, you may elect to manually trigger a retry for a past due
            subscription after a partial update.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/payment_profiles/{payment_profile_id}.json"),
            path_params=[param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PaymentProfileResponse],
            error_mapper=update_payment_profile_error_mapper,
            request_options=request_options,
        )

    def verify_bank_account(
        self,
        bank_account_id: int,
        *,
        body: BankAccountVerificationRequest | BankAccountVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankAccountResponse, VerifyBankAccountErrorBody]:
        """Verifies a bank account. Submit the two small deposit amounts the customer received in their bank account to
        verify the bank account. (Stripe only)

        Args:
            bank_account_id: Identifier of the bank account in the system.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/bank_accounts/{bank_account_id}/verification.json"),
            path_params=[param[int]("bank_account_id", bank_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankAccountVerificationRequest | BankAccountVerificationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BankAccountResponse],
            error_mapper=verify_bank_account_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentProfilesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def change_subscription_default_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentProfileResponse, ChangeSubscriptionDefaultPaymentProfileErrorBody]:
        """Changes the default payment profile on the subscription to the existing payment profile with the specified
        ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_payment_profile.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id), param[int]("payment_profile_id", payment_profile_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PaymentProfileResponse],
            error_mapper=change_subscription_default_payment_profile_error_mapper,
            request_options=request_options,
        )

    async def change_subscription_group_default_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentProfileResponse, ChangeSubscriptionGroupDefaultPaymentProfileErrorBody]:
        """Changes the default payment profile on the subscription group to the existing payment profile with the
        specified ID.

        You must elect to change the existing payment profile to a new payment profile ID in order to receive a
        satisfactory response from this endpoint.

        The new payment profile must belong to the subscription group's customer, otherwise you will receive an error.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscription_groups/{uid}/payment_profiles/{payment_profile_id}/change_payment_profile.json"
            ),
            path_params=[param[str]("uid", uid), param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PaymentProfileResponse],
            error_mapper=change_subscription_group_default_payment_profile_error_mapper,
            request_options=request_options,
        )

    async def create_payment_profile(
        self,
        *,
        body: CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentProfileResponse, CreatePaymentProfileErrorBody]:
        """Creates a payment profile for a customer.

        When you create a new payment profile for a customer via the API, it does not automatically make the profile
        current for any of the customer’s subscriptions. To use the payment profile as the default, you must set it
        explicitly for the subscription or subscription group.

        Select an option from the **Request Examples** drop-down on the right side of the portal to see examples of
        common scenarios for creating payment profiles.

        Do not use real card information for testing. See the Sites articles that cover `testing your site setup
        <https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overview#testing-overview-0-0>`__ for more
        details on testing in your sandbox.

        Note that collecting and sending raw card details in production requires `PCI compliance
        <https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compliance#pci-compliance-0-0>`__ on your end. If
        your business is not PCI compliant, use `Maxio.js (formerly Chargify.js)
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__ to
        collect credit card or bank account information.

        See the following articles to learn more about subscriptions and payments:

        + `Subscriber Payment Details
            <https://maxio.zendesk.com/hc/en-us/articles/24251599929613-Subscription-Summary-Payment-Details-Tab>`__
        + `Self Service Pages <https://maxio.zendesk.com/hc/en-us/articles/24261425318541-Self-Service-Pages>`__ (Allows
            credit card updates by Subscriber)
        + `Public Signup Pages payment settings
            <https://maxio.zendesk.com/hc/en-us/articles/24261368332557-Individual-Page-Settings>`__
        + `Taxes <https://developers.chargify.com/docs/developer-docs/d2e9e34db740e-signups#taxes>`__
        + `Maxio.js (formerly Chargify.js)
            <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview>`__
            + `Maxio.js with GoCardless - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQZKCER8CFK40MR6XJ>`__
            + `Maxio.js with GoCardless - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QR09JVHWW0MCA7HVJV>`__
            + `Maxio.js with Stripe Direct Debit - minimal example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QQFKKN8Z7B7DZ9AJS5>`__
            + `Maxio.js with Stripe Direct Debit - full example
                <https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01K0PJ15QRECQQ4ECS3ZA55GY7>`__
            + `Maxio.js with Stripe BECS Direct Debit - minimal example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-gateway>`__
            + `Maxio.js with Stripe BECS Direct Debit - full example
                <https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-examples#full-example-with-sepa-direct-debit-stripe-gateway>`__
        + `Full documentation on GoCardless <https://maxio.zendesk.com/hc/en-us/articles/24176159136909-GoCardless>`__
        + `Full documentation on Stripe SEPA Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BECS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__
        + `Full documentation on Stripe BACS Direct Debit
            <https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-and-BECS-Direct-Debit>`__

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            body: When following the IBAN or the Local Bank details examples, a customer, bank account and mandate will
                be created in your current vault. If the customer, bank account, and mandate already exist in your
                vault, follow the Import example to link the payment profile into Advanced Billing.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/payment_profiles.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePaymentProfileRequest | CreatePaymentProfileRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PaymentProfileResponse],
            error_mapper=create_payment_profile_error_mapper,
            request_options=request_options,
        )

    async def delete_subscription_group_payment_profile(
        self, uid: str, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a Payment Profile belonging to a Subscription Group.

        **Note**: If the Payment Profile belongs to multiple Subscription Groups and/or Subscriptions, it will be
        removed from all of them.

        Args:
            uid: The uid of the subscription group
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscription_groups/{uid}/payment_profiles/{payment_profile_id}.json"
            ),
            path_params=[param[str]("uid", uid), param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_subscriptions_payment_profile(
        self, subscription_id: int, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deletes a payment profile belonging to the customer on the subscription.

        If the customer has multiple subscriptions, the payment profile is removed from all of them.

        If you delete the default payment profile for a subscription, you need to specify another payment profile to be
        the default through the API, or either prompt the user to enter a card in the billing portal or on the
        self-service page, or visit the Payment Details tab on the subscription in the Admin UI and use the “Add New
        Credit Card” or “Make Active Payment Method” link, (depending on whether there are other cards present).

        Args:
            subscription_id: The Chargify id of the subscription.
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id), param[int]("payment_profile_id", payment_profile_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_unused_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteUnusedPaymentProfileErrorBody]:
        """Deletes an unused payment profile.

        If the payment profile is in use by one or more subscriptions or groups, an error message is returned.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/payment_profiles/{payment_profile_id}.json"),
            path_params=[param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_unused_payment_profile_error_mapper,
            request_options=request_options,
        )

    async def list_payment_profiles(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        customer_id: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PaymentProfileResponse], RawError]:
        """Lists all active payment profiles for a site, or for one customer within a site. If no payment profiles are
        found, this endpoint returns an empty array.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            customer_id: The ID of the customer for which you wish to list payment profiles
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/payment_profiles.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("customer_id", customer_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[PaymentProfileResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_one_time_token(
        self, chargify_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOneTimeTokenRequest, ReadOneTimeTokenErrorBody]:
        """Returns the one-time token data, including credit card or ACH details, associated with the provided token ID.
        One Time Tokens aka Advanced Billing Tokens house the credit card or ACH (Authorize.Net or Stripe only) data for
        a customer.

        You can use One Time Tokens while creating a subscription or payment profile instead of passing all bank account
        or credit card data directly to a given API endpoint.

        To obtain a One Time Token you have to use `Chargify.js
        <https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify-js-Overview#chargify-js-overview-0-0>`__.

        Args:
            chargify_token: Advanced Billing Token
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/one_time_tokens/{chargify_token}.json"),
            path_params=[param[str]("chargify_token", chargify_token)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[GetOneTimeTokenRequest],
            error_mapper=read_one_time_token_error_mapper,
            request_options=request_options,
        )

    async def read_payment_profile(
        self, payment_profile_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentProfileResponse, ReadPaymentProfileErrorBody]:
        """Returns a payment profile identified by its unique ID.

        Note that a different JSON object will be returned if the card method on file is a bank account.

        ### Response for Bank Account

        Example response for Bank Account:

        ```
        {
          "payment_profile": {
            "id": 10089892,
            "first_name": "Chester",
            "last_name": "Tester",
            "created_at": "2025-01-01T00:00:00-05:00",
            "updated_at": "2025-01-01T00:00:00-05:00",
            "customer_id": 14543792,
            "current_vault": "bogus",
            "vault_token": "0011223344",
            "billing_address": "456 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "customer_vault_token": null,
            "billing_address_2": "",
            "bank_name": "Bank of Kansas City",
            "masked_bank_routing_number": "XXXX6789",
            "masked_bank_account_number": "XXXX3344",
            "bank_account_type": "checking",
            "bank_account_holder_type": "personal",
            "payment_type": "bank_account",
            "site_gateway_setting_id": 1,
            "gateway_handle": null
          }
        }
        ```

        Args:
            payment_profile_id: The Chargify id of the payment profile
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/payment_profiles/{payment_profile_id}.json"),
            path_params=[param[int]("payment_profile_id", payment_profile_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PaymentProfileResponse],
            error_mapper=read_payment_profile_error_mapper,
            request_options=request_options,
        )

    async def send_request_update_payment_email(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, SendRequestUpdatePaymentEmailErrorBody]:
        """Sends a "request payment update" email to the customer associated with the subscription.

        If you attempt to send a "request payment update" email more than five times within a 30-minute period, you will
        receive a ``422`` response with an error message in the body. This error message will indicate that the request
        has been rejected due to excessive attempts, and will provide instructions on how to resubmit the request.

        Additionally, if you attempt to send a "request payment update" email for a subscription that does not exist,
        you will receive a ``404`` error response. This error message will indicate that the subscription could not be
        found, and will provide instructions on how to correct the error and resubmit the request.

        These error responses are designed to prevent excessive or invalid requests, and to provide clear and helpful
        information to users who encounter errors during the request process.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/request_payment_profiles_update.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=send_request_update_payment_email_error_mapper,
            request_options=request_options,
        )

    async def update_payment_profile(
        self,
        payment_profile_id: int,
        *,
        body: UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentProfileResponse, UpdatePaymentProfileErrorBody]:
        """Updates a payment profile.

        ## Partial Card Updates

        In the event that you are using the Authorize.net, Stripe, Cybersource, Forte or Braintree Blue payment
        gateways, you can update just the billing and contact information for a payment method. Note the lack of
        credit-card related data contained in the JSON payload.

        In this case, the following JSON is acceptable:

        ```
        {
          "payment_profile": {
            "first_name": "Kelly",
            "last_name": "Test",
            "billing_address": "789 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "billing_address_2": null
          }
        }
        ```

        The result will be that you have updated the billing information for the card, yet retained the original card
        number data.

        ## Specific notes on updating payment profiles

        - Merchants with **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe** as their
            payment gateway can update their Customer’s credit cards without passing in the full credit card number and
            CVV.

        - If you are using **Authorize.net**, **Cybersource**, **Forte**, **Braintree Blue** or **Stripe**, Advanced
            Billing will ignore the credit card number and CVV when processing an update via the API, and attempt a
            partial update instead. If you wish to change the card number on a payment profile, you will need to create
            a new payment profile for the given customer.

        - A Payment Profile cannot be updated with the attributes of another type of Payment Profile. For example, if
            the payment profile you are attempting to update is a credit card, you cannot pass in bank account
            attributes (like ``bank_account_number``), and vice versa.

        - Updating a payment profile directly will not trigger an attempt to capture a past-due balance. If this is the
            intent, update the card details via the Subscription instead.

        - If you are using Authorize.net or Stripe, you may elect to manually trigger a retry for a past due
            subscription after a partial update.

        Args:
            payment_profile_id: The Chargify id of the payment profile
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/payment_profiles/{payment_profile_id}.json"),
            path_params=[param[int]("payment_profile_id", payment_profile_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentProfileRequest | UpdatePaymentProfileRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PaymentProfileResponse],
            error_mapper=update_payment_profile_error_mapper,
            request_options=request_options,
        )

    async def verify_bank_account(
        self,
        bank_account_id: int,
        *,
        body: BankAccountVerificationRequest | BankAccountVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankAccountResponse, VerifyBankAccountErrorBody]:
        """Verifies a bank account. Submit the two small deposit amounts the customer received in their bank account to
        verify the bank account. (Stripe only)

        Args:
            bank_account_id: Identifier of the bank account in the system.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/bank_accounts/{bank_account_id}/verification.json"),
            path_params=[param[int]("bank_account_id", bank_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankAccountVerificationRequest | BankAccountVerificationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BankAccountResponse],
            error_mapper=verify_bank_account_error_mapper,
            request_options=request_options,
        )
