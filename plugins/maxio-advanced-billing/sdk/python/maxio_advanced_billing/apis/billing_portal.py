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
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.enable_billing_portal_for_customer_error import (
    EnableBillingPortalForCustomerErrorBody,
    enable_billing_portal_for_customer_error_mapper,
)
from ..errors.read_billing_portal_link_error import (
    ReadBillingPortalLinkErrorBody,
    read_billing_portal_link_error_mapper,
)
from ..errors.resend_billing_portal_invitation_error import (
    ResendBillingPortalInvitationErrorBody,
    resend_billing_portal_invitation_error_mapper,
)
from ..models.customer_response import CustomerResponse
from ..models.enums.auto_invite import AutoInviteOrInt
from ..models.portal_management_link import PortalManagementLink
from ..models.resent_invitation import ResentInvitation
from ..models.revoked_invitation import RevokedInvitation
from ..server.server import Server


class BillingPortal:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BillingPortalWithRawResponse(client, server, auth)

    def enable_billing_portal_for_customer(
        self,
        customer_id: int,
        *,
        auto_invite: AutoInviteOrInt | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Enables Billing Portal access for a customer, with an option to send an invitation email at the same time.

        ## Billing Portal Security

        If your customer has been invited to the Billing Portal, they receive a link to manage their subscription (the
        “Management URL”) automatically at the bottom of their statements, invoices, and receipts. **This link changes
        periodically for security and is only valid for 65 days.**

        If you need to provide your customer their Management URL through other means, you can retrieve it `via the API
        <$e/Billing%20Portal/readBillingPortalLink>`__. Because the URL is cryptographically signed with a timestamp,
        merchants cannot generate the URL without requesting it through the API.

        To prevent abuse and overuse, request a new URL only when absolutely necessary. Management URLs are good for 65
        days, so you should re-use a previously generated one as much as possible. If you use the URL frequently (such
        as to display on your website), **do not** make an API request every time.

        For more information configuring the Billing Portal, see `Billing Portal Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252412965133-Billing-Portal-Overview>`__.

        Args:
            customer_id: The Chargify id of the customer
            auto_invite: When set to 1, an Invitation email will be sent to the Customer. When set to 0, or not sent, an
                email will not be sent. Use in query: ``auto_invite=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.enable_billing_portal_for_customer(
                customer_id, auto_invite=auto_invite, request_options=request_options
            ),
        )

    def read_billing_portal_link(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PortalManagementLink:
        """Returns the exact URL required for a subscriber to access the Billing Portal.

        ## Management Link Request Rules

        + When retrieving a management URL, multiple requests for the same customer in a short period return the
            **same** URL
        + A new URL is not generated for 15 days
        + You must cache and remember this URL if you are going to need it again within 15 days
        + Only request a new URL after the ``new_link_available_at`` date
        + You are limited to 15 requests for the same URL. If you make more than 15 requests before
            ``new_link_available_at``, you are blocked from further Management URL requests (with a response code
            ``429``).

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) Too Many Requests ``error`` is ``ErrorListResponse1 |
                TooManyManagementLinkRequestsError1 | RawError``."""
        return unwrap(self._with_raw_response.read_billing_portal_link(customer_id, request_options=request_options))

    def resend_billing_portal_invitation(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ResentInvitation:
        """Resends a customer's Billing Portal invitation.

        If you attempt to resend an invitation 5 times within 30 minutes, you will receive a ``422`` response with an
        ``error`` message in the body.

        If you attempt to resend an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a ``422`` error response.

        If you attempt to resend an invitation when the Customer does not exist, you will receive a ``404`` error
        response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.resend_billing_portal_invitation(customer_id, request_options=request_options)
        )

    def revoke_billing_portal_access(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> RevokedInvitation:
        """Revokes a customer's Billing Portal invitation.

        If you attempt to revoke an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a 422 error response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.revoke_billing_portal_access(customer_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> BillingPortalWithRawResponse:
        return self._with_raw_response


class AsyncBillingPortal:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBillingPortalWithRawResponse(client, server, auth)

    async def enable_billing_portal_for_customer(
        self,
        customer_id: int,
        *,
        auto_invite: AutoInviteOrInt | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CustomerResponse:
        """Enables Billing Portal access for a customer, with an option to send an invitation email at the same time.

        ## Billing Portal Security

        If your customer has been invited to the Billing Portal, they receive a link to manage their subscription (the
        “Management URL”) automatically at the bottom of their statements, invoices, and receipts. **This link changes
        periodically for security and is only valid for 65 days.**

        If you need to provide your customer their Management URL through other means, you can retrieve it `via the API
        <$e/Billing%20Portal/readBillingPortalLink>`__. Because the URL is cryptographically signed with a timestamp,
        merchants cannot generate the URL without requesting it through the API.

        To prevent abuse and overuse, request a new URL only when absolutely necessary. Management URLs are good for 65
        days, so you should re-use a previously generated one as much as possible. If you use the URL frequently (such
        as to display on your website), **do not** make an API request every time.

        For more information configuring the Billing Portal, see `Billing Portal Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252412965133-Billing-Portal-Overview>`__.

        Args:
            customer_id: The Chargify id of the customer
            auto_invite: When set to 1, an Invitation email will be sent to the Customer. When set to 0, or not sent, an
                email will not be sent. Use in query: ``auto_invite=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.enable_billing_portal_for_customer(
                customer_id, auto_invite=auto_invite, request_options=request_options
            ),
        )

    async def read_billing_portal_link(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> PortalManagementLink:
        """Returns the exact URL required for a subscriber to access the Billing Portal.

        ## Management Link Request Rules

        + When retrieving a management URL, multiple requests for the same customer in a short period return the
            **same** URL
        + A new URL is not generated for 15 days
        + You must cache and remember this URL if you are going to need it again within 15 days
        + Only request a new URL after the ``new_link_available_at`` date
        + You are limited to 15 requests for the same URL. If you make more than 15 requests before
            ``new_link_available_at``, you are blocked from further Management URL requests (with a response code
            ``429``).

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) Too Many Requests ``error`` is ``ErrorListResponse1 |
                TooManyManagementLinkRequestsError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.read_billing_portal_link(customer_id, request_options=request_options)
        )

    async def resend_billing_portal_invitation(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ResentInvitation:
        """Resends a customer's Billing Portal invitation.

        If you attempt to resend an invitation 5 times within 30 minutes, you will receive a ``422`` response with an
        ``error`` message in the body.

        If you attempt to resend an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a ``422`` error response.

        If you attempt to resend an invitation when the Customer does not exist, you will receive a ``404`` error
        response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.resend_billing_portal_invitation(customer_id, request_options=request_options)
        )

    async def revoke_billing_portal_access(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> RevokedInvitation:
        """Revokes a customer's Billing Portal invitation.

        If you attempt to revoke an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a 422 error response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.revoke_billing_portal_access(customer_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncBillingPortalWithRawResponse:
        return self._with_raw_response


class BillingPortalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def enable_billing_portal_for_customer(
        self,
        customer_id: int,
        *,
        auto_invite: AutoInviteOrInt | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, EnableBillingPortalForCustomerErrorBody]:
        """Enables Billing Portal access for a customer, with an option to send an invitation email at the same time.

        ## Billing Portal Security

        If your customer has been invited to the Billing Portal, they receive a link to manage their subscription (the
        “Management URL”) automatically at the bottom of their statements, invoices, and receipts. **This link changes
        periodically for security and is only valid for 65 days.**

        If you need to provide your customer their Management URL through other means, you can retrieve it `via the API
        <$e/Billing%20Portal/readBillingPortalLink>`__. Because the URL is cryptographically signed with a timestamp,
        merchants cannot generate the URL without requesting it through the API.

        To prevent abuse and overuse, request a new URL only when absolutely necessary. Management URLs are good for 65
        days, so you should re-use a previously generated one as much as possible. If you use the URL frequently (such
        as to display on your website), **do not** make an API request every time.

        For more information configuring the Billing Portal, see `Billing Portal Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252412965133-Billing-Portal-Overview>`__.

        Args:
            customer_id: The Chargify id of the customer
            auto_invite: When set to 1, an Invitation email will be sent to the Customer. When set to 0, or not sent, an
                email will not be sent. Use in query: ``auto_invite=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/portal/customers/{customer_id}/enable.json"),
            path_params=[param[int]("customer_id", customer_id)],
            query_params=[param[AutoInviteOrInt | None]("auto_invite", auto_invite)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CustomerResponse],
            error_mapper=enable_billing_portal_for_customer_error_mapper,
            request_options=request_options,
        )

    def read_billing_portal_link(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PortalManagementLink, ReadBillingPortalLinkErrorBody]:
        """Returns the exact URL required for a subscriber to access the Billing Portal.

        ## Management Link Request Rules

        + When retrieving a management URL, multiple requests for the same customer in a short period return the
            **same** URL
        + A new URL is not generated for 15 days
        + You must cache and remember this URL if you are going to need it again within 15 days
        + Only request a new URL after the ``new_link_available_at`` date
        + You are limited to 15 requests for the same URL. If you make more than 15 requests before
            ``new_link_available_at``, you are blocked from further Management URL requests (with a response code
            ``429``).

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/portal/customers/{customer_id}/management_link.json"),
            path_params=[param[int]("customer_id", customer_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PortalManagementLink],
            error_mapper=read_billing_portal_link_error_mapper,
            request_options=request_options,
        )

    def resend_billing_portal_invitation(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ResentInvitation, ResendBillingPortalInvitationErrorBody]:
        """Resends a customer's Billing Portal invitation.

        If you attempt to resend an invitation 5 times within 30 minutes, you will receive a ``422`` response with an
        ``error`` message in the body.

        If you attempt to resend an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a ``422`` error response.

        If you attempt to resend an invitation when the Customer does not exist, you will receive a ``404`` error
        response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/portal/customers/{customer_id}/invitations/invite.json"),
            path_params=[param[int]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ResentInvitation],
            error_mapper=resend_billing_portal_invitation_error_mapper,
            request_options=request_options,
        )

    def revoke_billing_portal_access(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevokedInvitation, RawError]:
        """Revokes a customer's Billing Portal invitation.

        If you attempt to revoke an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a 422 error response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/portal/customers/{customer_id}/invitations/revoke.json"),
            path_params=[param[int]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[RevokedInvitation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBillingPortalWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def enable_billing_portal_for_customer(
        self,
        customer_id: int,
        *,
        auto_invite: AutoInviteOrInt | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CustomerResponse, EnableBillingPortalForCustomerErrorBody]:
        """Enables Billing Portal access for a customer, with an option to send an invitation email at the same time.

        ## Billing Portal Security

        If your customer has been invited to the Billing Portal, they receive a link to manage their subscription (the
        “Management URL”) automatically at the bottom of their statements, invoices, and receipts. **This link changes
        periodically for security and is only valid for 65 days.**

        If you need to provide your customer their Management URL through other means, you can retrieve it `via the API
        <$e/Billing%20Portal/readBillingPortalLink>`__. Because the URL is cryptographically signed with a timestamp,
        merchants cannot generate the URL without requesting it through the API.

        To prevent abuse and overuse, request a new URL only when absolutely necessary. Management URLs are good for 65
        days, so you should re-use a previously generated one as much as possible. If you use the URL frequently (such
        as to display on your website), **do not** make an API request every time.

        For more information configuring the Billing Portal, see `Billing Portal Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252412965133-Billing-Portal-Overview>`__.

        Args:
            customer_id: The Chargify id of the customer
            auto_invite: When set to 1, an Invitation email will be sent to the Customer. When set to 0, or not sent, an
                email will not be sent. Use in query: ``auto_invite=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/portal/customers/{customer_id}/enable.json"),
            path_params=[param[int]("customer_id", customer_id)],
            query_params=[param[AutoInviteOrInt | None]("auto_invite", auto_invite)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CustomerResponse],
            error_mapper=enable_billing_portal_for_customer_error_mapper,
            request_options=request_options,
        )

    async def read_billing_portal_link(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PortalManagementLink, ReadBillingPortalLinkErrorBody]:
        """Returns the exact URL required for a subscriber to access the Billing Portal.

        ## Management Link Request Rules

        + When retrieving a management URL, multiple requests for the same customer in a short period return the
            **same** URL
        + A new URL is not generated for 15 days
        + You must cache and remember this URL if you are going to need it again within 15 days
        + Only request a new URL after the ``new_link_available_at`` date
        + You are limited to 15 requests for the same URL. If you make more than 15 requests before
            ``new_link_available_at``, you are blocked from further Management URL requests (with a response code
            ``429``).

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/portal/customers/{customer_id}/management_link.json"),
            path_params=[param[int]("customer_id", customer_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PortalManagementLink],
            error_mapper=read_billing_portal_link_error_mapper,
            request_options=request_options,
        )

    async def resend_billing_portal_invitation(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ResentInvitation, ResendBillingPortalInvitationErrorBody]:
        """Resends a customer's Billing Portal invitation.

        If you attempt to resend an invitation 5 times within 30 minutes, you will receive a ``422`` response with an
        ``error`` message in the body.

        If you attempt to resend an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a ``422`` error response.

        If you attempt to resend an invitation when the Customer does not exist, you will receive a ``404`` error
        response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/portal/customers/{customer_id}/invitations/invite.json"),
            path_params=[param[int]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ResentInvitation],
            error_mapper=resend_billing_portal_invitation_error_mapper,
            request_options=request_options,
        )

    async def revoke_billing_portal_access(
        self, customer_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevokedInvitation, RawError]:
        """Revokes a customer's Billing Portal invitation.

        If you attempt to revoke an invitation when the Billing Portal is already disabled for a Customer, you will
        receive a 422 error response.

        ## Limitations

        This endpoint will only return a JSON response.

        Args:
            customer_id: The Chargify id of the customer
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/portal/customers/{customer_id}/invitations/revoke.json"),
            path_params=[param[int]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[RevokedInvitation],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
