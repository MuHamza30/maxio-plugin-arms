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
from ..errors.create_subscription_group_error import (
    CreateSubscriptionGroupErrorBody,
    create_subscription_group_error_mapper,
)
from ..errors.delete_subscription_group_error import (
    DeleteSubscriptionGroupErrorBody,
    delete_subscription_group_error_mapper,
)
from ..errors.find_subscription_group_error import FindSubscriptionGroupErrorBody, find_subscription_group_error_mapper
from ..errors.remove_subscription_from_group_error import (
    RemoveSubscriptionFromGroupErrorBody,
    remove_subscription_from_group_error_mapper,
)
from ..errors.signup_with_subscription_group_error import (
    SignupWithSubscriptionGroupErrorBody,
    signup_with_subscription_group_error_mapper,
)
from ..errors.update_subscription_group_members_error import (
    UpdateSubscriptionGroupMembersErrorBody,
    update_subscription_group_members_error_mapper,
)
from ..models.add_subscription_to_a_group import AddSubscriptionToAGroup, AddSubscriptionToAGroupDict
from ..models.create_subscription_group_request import (
    CreateSubscriptionGroupRequest,
    CreateSubscriptionGroupRequestDict,
)
from ..models.delete_subscription_group_response import DeleteSubscriptionGroupResponse
from ..models.enums.subscription_group_include import SubscriptionGroupIncludeOrStr
from ..models.enums.subscription_groups_list_include import SubscriptionGroupsListIncludeOrStr
from ..models.full_subscription_group_response import FullSubscriptionGroupResponse
from ..models.list_subscription_groups_response import ListSubscriptionGroupsResponse
from ..models.subscription_group_response import SubscriptionGroupResponse
from ..models.subscription_group_signup_request import (
    SubscriptionGroupSignupRequest,
    SubscriptionGroupSignupRequestDict,
)
from ..models.subscription_group_signup_response import SubscriptionGroupSignupResponse
from ..models.update_subscription_group_request import (
    UpdateSubscriptionGroupRequest,
    UpdateSubscriptionGroupRequestDict,
)
from ..server.server import Server


class SubscriptionGroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionGroupsWithRawResponse(client, server, auth)

    def add_subscription_to_group(
        self,
        subscription_id: int,
        *,
        body: AddSubscriptionToAGroup | AddSubscriptionToAGroupDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupResponse:
        """Adds an existing subscription to a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to add existing subscriptions to subscription groups.

        Passing ``group`` parameters with a ``target`` containing a ``type`` and optional ``id`` is all that's needed.
        When the ``target`` parameter specifies a ``"customer"`` or ``"subscription"`` that is already part of a
        hierarchy, the subscription will become a member of the customer's subscription group. If the target customer or
        subscription is not part of a subscription group, a new group will be created and the subscription will become
        part of the group with the specified target customer set as the responsible payer for the group's subscriptions.

        **Note:** In order to add an existing subscription to a subscription group, it must belong to either the same
        customer record as the target, or be within the same customer hierarchy.

        Rather than specifying a customer, the ``target`` parameter could instead simply have a value of
        * ``"self"`` which indicates the subscription will be paid for not by some other customer, but by the
            subscribing customer,
        * ``"parent"`` which indicates the subscription will be paid for by the subscribing customer's parent within a
            customer hierarchy, or
        * ``"eldest"`` which indicates the subscription will be paid for by the root-level customer in the subscribing
            customer's hierarchy.

        To create a new subscription into a subscription group, reference the following: `Create Subscription in a
        Subscription Group
        <https://developers.chargify.com/docs/api-docs/d571659cf0f24-create-subscription#subscription-in-a-subscription-group>`__

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.add_subscription_to_group(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def create_subscription_group(
        self,
        *,
        body: CreateSubscriptionGroupRequest | CreateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupResponse:
        """Creates a subscription group with given members.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionGroupCreateErrorResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.create_subscription_group(body=body, request_options=request_options))

    def delete_subscription_group(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteSubscriptionGroupResponse:
        """Deletes a subscription group.
         Only groups without members can be deleted.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_subscription_group(uid, request_options=request_options))

    def find_subscription_group(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FullSubscriptionGroupResponse:
        """Finds the subscription group associated with a subscription.

        If the subscription is not in a group, this endpoint returns an error.

        Args:
            subscription_id: The Advanced Billing id of the subscription associated with the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.find_subscription_group(subscription_id, request_options=request_options))

    def list_subscription_groups(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include: list[SubscriptionGroupsListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionGroupsResponse:
        """Lists subscription groups for the site. The response is paginated and will return a ``meta`` key with
        pagination information.

        #### Account Balance Information

        Account balance information for the subscription groups is not returned by default. If this information is
        desired, the ``include[]=account_balances`` parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include: A list of additional information to include in the response. The following values are supported: -
                ``account_balances``: Account balance information for the subscription groups. Use in query:
                ``include[]=account_balances``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_subscription_groups(
                page=page, per_page=per_page, include=include, request_options=request_options
            ),
        )

    def read_subscription_group(
        self,
        uid: str,
        *,
        include: list[SubscriptionGroupIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FullSubscriptionGroupResponse:
        """Returns subscription group details.

        #### Current Billing Amount in Cents

        Current billing amount for the subscription group is not returned by default. If this information is desired,
        the ``include[]=current_billing_amount_in_cents`` parameter must be provided with the request.

        Args:
            uid: The uid of the subscription group
            include: Allows including additional data in the response. Use in query:
                ``include[]=current_billing_amount_in_cents``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_subscription_group(uid, include=include, request_options=request_options)
        )

    def remove_subscription_from_group(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes an existing subscription from a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to remove an existing subscription from a subscription group.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.remove_subscription_from_group(subscription_id, request_options=request_options)
        )

    def signup_with_subscription_group(
        self,
        *,
        body: SubscriptionGroupSignupRequest | SubscriptionGroupSignupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupSignupResponse:
        """Creates multiple subscriptions at once under the same customer and consolidates them into a subscription
        group.

        You must provide one and only one of the ``payer_id``/``payer_reference``/``payer_attributes`` for the customer
        attached to the group.

        You must provide one and only one of the
        ``payment_profile_id``/``credit_card_attributes``/``bank_account_attributes`` for the payment profile attached
        to the group.

        Only one of the ``subscriptions`` can have ``"primary": true`` attribute set.

        When passing a product to a subscription you can use either ``product_id`` or ``product_handle`` or
        ``offer_id``. You can also use ``custom_price`` instead. The subscription request examples below will be split
        into two sections. The first section, "Subscription Customization", will focus on passing different information
        with a subscription, such as components, calendar billing, and custom fields. These examples will presume you
        are using a secure chargify_token generated by Maxio.js (formerly Chargify.js).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionGroupSignupErrorResponse1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.signup_with_subscription_group(body=body, request_options=request_options)
        )

    def update_subscription_group_members(
        self,
        uid: str,
        *,
        body: UpdateSubscriptionGroupRequest | UpdateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupResponse:
        """Updates subscription group members. ``"member_ids"`` should contain an array of both subscription IDs to set
        as group members and subscription IDs already present in the groups. Not including them will result in removing
        them from the subscription group. To clean up members, just leave the array empty.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionGroupUpdateErrorResponse1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.update_subscription_group_members(uid, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> SubscriptionGroupsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionGroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionGroupsWithRawResponse(client, server, auth)

    async def add_subscription_to_group(
        self,
        subscription_id: int,
        *,
        body: AddSubscriptionToAGroup | AddSubscriptionToAGroupDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupResponse:
        """Adds an existing subscription to a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to add existing subscriptions to subscription groups.

        Passing ``group`` parameters with a ``target`` containing a ``type`` and optional ``id`` is all that's needed.
        When the ``target`` parameter specifies a ``"customer"`` or ``"subscription"`` that is already part of a
        hierarchy, the subscription will become a member of the customer's subscription group. If the target customer or
        subscription is not part of a subscription group, a new group will be created and the subscription will become
        part of the group with the specified target customer set as the responsible payer for the group's subscriptions.

        **Note:** In order to add an existing subscription to a subscription group, it must belong to either the same
        customer record as the target, or be within the same customer hierarchy.

        Rather than specifying a customer, the ``target`` parameter could instead simply have a value of
        * ``"self"`` which indicates the subscription will be paid for not by some other customer, but by the
            subscribing customer,
        * ``"parent"`` which indicates the subscription will be paid for by the subscribing customer's parent within a
            customer hierarchy, or
        * ``"eldest"`` which indicates the subscription will be paid for by the root-level customer in the subscribing
            customer's hierarchy.

        To create a new subscription into a subscription group, reference the following: `Create Subscription in a
        Subscription Group
        <https://developers.chargify.com/docs/api-docs/d571659cf0f24-create-subscription#subscription-in-a-subscription-group>`__

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.add_subscription_to_group(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def create_subscription_group(
        self,
        *,
        body: CreateSubscriptionGroupRequest | CreateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupResponse:
        """Creates a subscription group with given members.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionGroupCreateErrorResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.create_subscription_group(body=body, request_options=request_options)
        )

    async def delete_subscription_group(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteSubscriptionGroupResponse:
        """Deletes a subscription group.
         Only groups without members can be deleted.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.delete_subscription_group(uid, request_options=request_options))

    async def find_subscription_group(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FullSubscriptionGroupResponse:
        """Finds the subscription group associated with a subscription.

        If the subscription is not in a group, this endpoint returns an error.

        Args:
            subscription_id: The Advanced Billing id of the subscription associated with the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.find_subscription_group(subscription_id, request_options=request_options)
        )

    async def list_subscription_groups(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include: list[SubscriptionGroupsListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionGroupsResponse:
        """Lists subscription groups for the site. The response is paginated and will return a ``meta`` key with
        pagination information.

        #### Account Balance Information

        Account balance information for the subscription groups is not returned by default. If this information is
        desired, the ``include[]=account_balances`` parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include: A list of additional information to include in the response. The following values are supported: -
                ``account_balances``: Account balance information for the subscription groups. Use in query:
                ``include[]=account_balances``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_subscription_groups(
                page=page, per_page=per_page, include=include, request_options=request_options
            ),
        )

    async def read_subscription_group(
        self,
        uid: str,
        *,
        include: list[SubscriptionGroupIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FullSubscriptionGroupResponse:
        """Returns subscription group details.

        #### Current Billing Amount in Cents

        Current billing amount for the subscription group is not returned by default. If this information is desired,
        the ``include[]=current_billing_amount_in_cents`` parameter must be provided with the request.

        Args:
            uid: The uid of the subscription group
            include: Allows including additional data in the response. Use in query:
                ``include[]=current_billing_amount_in_cents``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_subscription_group(uid, include=include, request_options=request_options)
        )

    async def remove_subscription_from_group(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes an existing subscription from a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to remove an existing subscription from a subscription group.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.remove_subscription_from_group(
                subscription_id, request_options=request_options
            ),
        )

    async def signup_with_subscription_group(
        self,
        *,
        body: SubscriptionGroupSignupRequest | SubscriptionGroupSignupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupSignupResponse:
        """Creates multiple subscriptions at once under the same customer and consolidates them into a subscription
        group.

        You must provide one and only one of the ``payer_id``/``payer_reference``/``payer_attributes`` for the customer
        attached to the group.

        You must provide one and only one of the
        ``payment_profile_id``/``credit_card_attributes``/``bank_account_attributes`` for the payment profile attached
        to the group.

        Only one of the ``subscriptions`` can have ``"primary": true`` attribute set.

        When passing a product to a subscription you can use either ``product_id`` or ``product_handle`` or
        ``offer_id``. You can also use ``custom_price`` instead. The subscription request examples below will be split
        into two sections. The first section, "Subscription Customization", will focus on passing different information
        with a subscription, such as components, calendar billing, and custom fields. These examples will presume you
        are using a secure chargify_token generated by Maxio.js (formerly Chargify.js).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionGroupSignupErrorResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.signup_with_subscription_group(body=body, request_options=request_options)
        )

    async def update_subscription_group_members(
        self,
        uid: str,
        *,
        body: UpdateSubscriptionGroupRequest | UpdateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionGroupResponse:
        """Updates subscription group members. ``"member_ids"`` should contain an array of both subscription IDs to set
        as group members and subscription IDs already present in the groups. Not including them will result in removing
        them from the subscription group. To clean up members, just leave the array empty.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionGroupUpdateErrorResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_subscription_group_members(
                uid, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionGroupsWithRawResponse:
        return self._with_raw_response


class SubscriptionGroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_subscription_to_group(
        self,
        subscription_id: int,
        *,
        body: AddSubscriptionToAGroup | AddSubscriptionToAGroupDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupResponse, RawError]:
        """Adds an existing subscription to a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to add existing subscriptions to subscription groups.

        Passing ``group`` parameters with a ``target`` containing a ``type`` and optional ``id`` is all that's needed.
        When the ``target`` parameter specifies a ``"customer"`` or ``"subscription"`` that is already part of a
        hierarchy, the subscription will become a member of the customer's subscription group. If the target customer or
        subscription is not part of a subscription group, a new group will be created and the subscription will become
        part of the group with the specified target customer set as the responsible payer for the group's subscriptions.

        **Note:** In order to add an existing subscription to a subscription group, it must belong to either the same
        customer record as the target, or be within the same customer hierarchy.

        Rather than specifying a customer, the ``target`` parameter could instead simply have a value of
        * ``"self"`` which indicates the subscription will be paid for not by some other customer, but by the
            subscribing customer,
        * ``"parent"`` which indicates the subscription will be paid for by the subscribing customer's parent within a
            customer hierarchy, or
        * ``"eldest"`` which indicates the subscription will be paid for by the root-level customer in the subscribing
            customer's hierarchy.

        To create a new subscription into a subscription group, reference the following: `Create Subscription in a
        Subscription Group
        <https://developers.chargify.com/docs/api-docs/d571659cf0f24-create-subscription#subscription-in-a-subscription-group>`__

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/group.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddSubscriptionToAGroup | AddSubscriptionToAGroupDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_subscription_group(
        self,
        *,
        body: CreateSubscriptionGroupRequest | CreateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupResponse, CreateSubscriptionGroupErrorBody]:
        """Creates a subscription group with given members.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionGroupRequest | CreateSubscriptionGroupRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionGroupResponse],
            error_mapper=create_subscription_group_error_mapper,
            request_options=request_options,
        )

    def delete_subscription_group(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteSubscriptionGroupResponse, DeleteSubscriptionGroupErrorBody]:
        """Deletes a subscription group.
         Only groups without members can be deleted.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscription_groups/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[DeleteSubscriptionGroupResponse],
            error_mapper=delete_subscription_group_error_mapper,
            request_options=request_options,
        )

    def find_subscription_group(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FullSubscriptionGroupResponse, FindSubscriptionGroupErrorBody]:
        """Finds the subscription group associated with a subscription.

        If the subscription is not in a group, this endpoint returns an error.

        Args:
            subscription_id: The Advanced Billing id of the subscription associated with the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/lookup.json"),
            query_params=[param[str]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FullSubscriptionGroupResponse],
            error_mapper=find_subscription_group_error_mapper,
            request_options=request_options,
        )

    def list_subscription_groups(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include: list[SubscriptionGroupsListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionGroupsResponse, RawError]:
        """Lists subscription groups for the site. The response is paginated and will return a ``meta`` key with
        pagination information.

        #### Account Balance Information

        Account balance information for the subscription groups is not returned by default. If this information is
        desired, the ``include[]=account_balances`` parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include: A list of additional information to include in the response. The following values are supported: -
                ``account_balances``: Account balance information for the subscription groups. Use in query:
                ``include[]=account_balances``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[SubscriptionGroupsListIncludeOrStr] | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListSubscriptionGroupsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_subscription_group(
        self,
        uid: str,
        *,
        include: list[SubscriptionGroupIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FullSubscriptionGroupResponse, RawError]:
        """Returns subscription group details.

        #### Current Billing Amount in Cents

        Current billing amount for the subscription group is not returned by default. If this information is desired,
        the ``include[]=current_billing_amount_in_cents`` parameter must be provided with the request.

        Args:
            uid: The uid of the subscription group
            include: Allows including additional data in the response. Use in query:
                ``include[]=current_billing_amount_in_cents``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            query_params=[param[list[SubscriptionGroupIncludeOrStr] | None]("include", include)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FullSubscriptionGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_subscription_from_group(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveSubscriptionFromGroupErrorBody]:
        """Removes an existing subscription from a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to remove an existing subscription from a subscription group.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/group.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=remove_subscription_from_group_error_mapper,
            request_options=request_options,
        )

    def signup_with_subscription_group(
        self,
        *,
        body: SubscriptionGroupSignupRequest | SubscriptionGroupSignupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupSignupResponse, SignupWithSubscriptionGroupErrorBody]:
        """Creates multiple subscriptions at once under the same customer and consolidates them into a subscription
        group.

        You must provide one and only one of the ``payer_id``/``payer_reference``/``payer_attributes`` for the customer
        attached to the group.

        You must provide one and only one of the
        ``payment_profile_id``/``credit_card_attributes``/``bank_account_attributes`` for the payment profile attached
        to the group.

        Only one of the ``subscriptions`` can have ``"primary": true`` attribute set.

        When passing a product to a subscription you can use either ``product_id`` or ``product_handle`` or
        ``offer_id``. You can also use ``custom_price`` instead. The subscription request examples below will be split
        into two sections. The first section, "Subscription Customization", will focus on passing different information
        with a subscription, such as components, calendar billing, and custom fields. These examples will presume you
        are using a secure chargify_token generated by Maxio.js (formerly Chargify.js).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/signup.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionGroupSignupRequest | SubscriptionGroupSignupRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionGroupSignupResponse],
            error_mapper=signup_with_subscription_group_error_mapper,
            request_options=request_options,
        )

    def update_subscription_group_members(
        self,
        uid: str,
        *,
        body: UpdateSubscriptionGroupRequest | UpdateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupResponse, UpdateSubscriptionGroupMembersErrorBody]:
        """Updates subscription group members. ``"member_ids"`` should contain an array of both subscription IDs to set
        as group members and subscription IDs already present in the groups. Not including them will result in removing
        them from the subscription group. To clean up members, just leave the array empty.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscription_groups/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionGroupRequest | UpdateSubscriptionGroupRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionGroupResponse],
            error_mapper=update_subscription_group_members_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionGroupsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_subscription_to_group(
        self,
        subscription_id: int,
        *,
        body: AddSubscriptionToAGroup | AddSubscriptionToAGroupDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupResponse, RawError]:
        """Adds an existing subscription to a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to add existing subscriptions to subscription groups.

        Passing ``group`` parameters with a ``target`` containing a ``type`` and optional ``id`` is all that's needed.
        When the ``target`` parameter specifies a ``"customer"`` or ``"subscription"`` that is already part of a
        hierarchy, the subscription will become a member of the customer's subscription group. If the target customer or
        subscription is not part of a subscription group, a new group will be created and the subscription will become
        part of the group with the specified target customer set as the responsible payer for the group's subscriptions.

        **Note:** In order to add an existing subscription to a subscription group, it must belong to either the same
        customer record as the target, or be within the same customer hierarchy.

        Rather than specifying a customer, the ``target`` parameter could instead simply have a value of
        * ``"self"`` which indicates the subscription will be paid for not by some other customer, but by the
            subscribing customer,
        * ``"parent"`` which indicates the subscription will be paid for by the subscribing customer's parent within a
            customer hierarchy, or
        * ``"eldest"`` which indicates the subscription will be paid for by the root-level customer in the subscribing
            customer's hierarchy.

        To create a new subscription into a subscription group, reference the following: `Create Subscription in a
        Subscription Group
        <https://developers.chargify.com/docs/api-docs/d571659cf0f24-create-subscription#subscription-in-a-subscription-group>`__

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/group.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddSubscriptionToAGroup | AddSubscriptionToAGroupDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_subscription_group(
        self,
        *,
        body: CreateSubscriptionGroupRequest | CreateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupResponse, CreateSubscriptionGroupErrorBody]:
        """Creates a subscription group with given members.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionGroupRequest | CreateSubscriptionGroupRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionGroupResponse],
            error_mapper=create_subscription_group_error_mapper,
            request_options=request_options,
        )

    async def delete_subscription_group(
        self, uid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteSubscriptionGroupResponse, DeleteSubscriptionGroupErrorBody]:
        """Deletes a subscription group.
         Only groups without members can be deleted.

        Args:
            uid: The uid of the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscription_groups/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[DeleteSubscriptionGroupResponse],
            error_mapper=delete_subscription_group_error_mapper,
            request_options=request_options,
        )

    async def find_subscription_group(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FullSubscriptionGroupResponse, FindSubscriptionGroupErrorBody]:
        """Finds the subscription group associated with a subscription.

        If the subscription is not in a group, this endpoint returns an error.

        Args:
            subscription_id: The Advanced Billing id of the subscription associated with the subscription group
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/lookup.json"),
            query_params=[param[str]("subscription_id", subscription_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FullSubscriptionGroupResponse],
            error_mapper=find_subscription_group_error_mapper,
            request_options=request_options,
        )

    async def list_subscription_groups(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        include: list[SubscriptionGroupsListIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionGroupsResponse, RawError]:
        """Lists subscription groups for the site. The response is paginated and will return a ``meta`` key with
        pagination information.

        #### Account Balance Information

        Account balance information for the subscription groups is not returned by default. If this information is
        desired, the ``include[]=account_balances`` parameter must be provided with the request.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            include: A list of additional information to include in the response. The following values are supported: -
                ``account_balances``: Account balance information for the subscription groups. Use in query:
                ``include[]=account_balances``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[list[SubscriptionGroupsListIncludeOrStr] | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListSubscriptionGroupsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_subscription_group(
        self,
        uid: str,
        *,
        include: list[SubscriptionGroupIncludeOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FullSubscriptionGroupResponse, RawError]:
        """Returns subscription group details.

        #### Current Billing Amount in Cents

        Current billing amount for the subscription group is not returned by default. If this information is desired,
        the ``include[]=current_billing_amount_in_cents`` parameter must be provided with the request.

        Args:
            uid: The uid of the subscription group
            include: Allows including additional data in the response. Use in query:
                ``include[]=current_billing_amount_in_cents``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscription_groups/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            query_params=[param[list[SubscriptionGroupIncludeOrStr] | None]("include", include)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FullSubscriptionGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_subscription_from_group(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RemoveSubscriptionFromGroupErrorBody]:
        """Removes an existing subscription from a subscription group. For sites making use of the `Relationship Billing
        <https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Advanced-Billing-Invoices-Overview>`__ and `Customer
        Hierarchy
        <https://maxio.zendesk.com/hc/en-us/articles/24252185211533-Customer-Hierarchies-WhoPays#customer-hierarchies>`__
        features, it is possible to remove an existing subscription from a subscription group.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/group.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=remove_subscription_from_group_error_mapper,
            request_options=request_options,
        )

    async def signup_with_subscription_group(
        self,
        *,
        body: SubscriptionGroupSignupRequest | SubscriptionGroupSignupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupSignupResponse, SignupWithSubscriptionGroupErrorBody]:
        """Creates multiple subscriptions at once under the same customer and consolidates them into a subscription
        group.

        You must provide one and only one of the ``payer_id``/``payer_reference``/``payer_attributes`` for the customer
        attached to the group.

        You must provide one and only one of the
        ``payment_profile_id``/``credit_card_attributes``/``bank_account_attributes`` for the payment profile attached
        to the group.

        Only one of the ``subscriptions`` can have ``"primary": true`` attribute set.

        When passing a product to a subscription you can use either ``product_id`` or ``product_handle`` or
        ``offer_id``. You can also use ``custom_price`` instead. The subscription request examples below will be split
        into two sections. The first section, "Subscription Customization", will focus on passing different information
        with a subscription, such as components, calendar billing, and custom fields. These examples will presume you
        are using a secure chargify_token generated by Maxio.js (formerly Chargify.js).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscription_groups/signup.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscriptionGroupSignupRequest | SubscriptionGroupSignupRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionGroupSignupResponse],
            error_mapper=signup_with_subscription_group_error_mapper,
            request_options=request_options,
        )

    async def update_subscription_group_members(
        self,
        uid: str,
        *,
        body: UpdateSubscriptionGroupRequest | UpdateSubscriptionGroupRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionGroupResponse, UpdateSubscriptionGroupMembersErrorBody]:
        """Updates subscription group members. ``"member_ids"`` should contain an array of both subscription IDs to set
        as group members and subscription IDs already present in the groups. Not including them will result in removing
        them from the subscription group. To clean up members, just leave the array empty.

        Args:
            uid: The uid of the subscription group
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscription_groups/{uid}.json"),
            path_params=[param[str]("uid", uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSubscriptionGroupRequest | UpdateSubscriptionGroupRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionGroupResponse],
            error_mapper=update_subscription_group_members_error_mapper,
            request_options=request_options,
        )
