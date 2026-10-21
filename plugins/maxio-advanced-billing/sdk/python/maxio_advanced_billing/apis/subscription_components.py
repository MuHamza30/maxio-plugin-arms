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
from ..errors.allocate_component_error import AllocateComponentErrorBody, allocate_component_error_mapper
from ..errors.allocate_components_error import AllocateComponentsErrorBody, allocate_components_error_mapper
from ..errors.bulk_update_subscription_components_price_points_error import (
    BulkUpdateSubscriptionComponentsPricePointsErrorBody,
    bulk_update_subscription_components_price_points_error_mapper,
)
from ..errors.create_usage_error import CreateUsageErrorBody, create_usage_error_mapper
from ..errors.delete_prepaid_usage_allocation_error import (
    DeletePrepaidUsageAllocationErrorBody,
    delete_prepaid_usage_allocation_error_mapper,
)
from ..errors.list_allocations_error import ListAllocationsErrorBody, list_allocations_error_mapper
from ..errors.preview_allocations_error import PreviewAllocationsErrorBody, preview_allocations_error_mapper
from ..errors.read_subscription_component_error import (
    ReadSubscriptionComponentErrorBody,
    read_subscription_component_error_mapper,
)
from ..errors.update_prepaid_usage_allocation_expiration_date_error import (
    UpdatePrepaidUsageAllocationExpirationDateErrorBody,
    update_prepaid_usage_allocation_expiration_date_error_mapper,
)
from ..models.activate_event_based_component import ActivateEventBasedComponent, ActivateEventBasedComponentDict
from ..models.allocate_components import AllocateComponents, AllocateComponentsDict
from ..models.allocation_preview_response import AllocationPreviewResponse
from ..models.allocation_response import AllocationResponse
from ..models.bulk_components_price_point_assignment import (
    BulkComponentsPricePointAssignment,
    BulkComponentsPricePointAssignmentDict,
)
from ..models.create_allocation_request import CreateAllocationRequest, CreateAllocationRequestDict
from ..models.create_usage_request import CreateUsageRequest, CreateUsageRequestDict
from ..models.credit_scheme_request import CreditSchemeRequest, CreditSchemeRequestDict
from ..models.ebb_event import EbbEvent, EbbEventDict
from ..models.enums.include_not_null import IncludeNotNullOrStr
from ..models.enums.list_subscription_components_include import ListSubscriptionComponentsIncludeOrStr
from ..models.enums.list_subscription_components_sort import ListSubscriptionComponentsSortOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.enums.subscription_list_date_field import SubscriptionListDateFieldOrStr
from ..models.list_subscription_components_filter import (
    ListSubscriptionComponentsFilter,
    ListSubscriptionComponentsFilterDict,
)
from ..models.list_subscription_components_for_site_filter import (
    ListSubscriptionComponentsForSiteFilter,
    ListSubscriptionComponentsForSiteFilterDict,
)
from ..models.list_subscription_components_response import ListSubscriptionComponentsResponse
from ..models.preview_allocations_request import PreviewAllocationsRequest, PreviewAllocationsRequestDict
from ..models.subscription_component_response import SubscriptionComponentResponse
from ..models.subscription_response import SubscriptionResponse
from ..models.unions.component_id_model import ComponentIdModel, ComponentIdModelDict
from ..models.unions.subscription_id_or_reference import SubscriptionIdOrReference, SubscriptionIdOrReferenceDict
from ..models.update_allocation_expiration_date import (
    UpdateAllocationExpirationDate,
    UpdateAllocationExpirationDateDict,
)
from ..models.usage_response import UsageResponse
from ..server.server import Server


class SubscriptionComponents:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionComponentsWithRawResponse(client, server, auth)

    def activate_event_based_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: ActivateEventBasedComponent | ActivateEventBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Activates an event-based component for a single subscription.

        To bill your subscribers on your Events data under the Events-Based Billing feature, the components must be
        activated for the subscriber.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Use this endpoint to activate an event-based component for a single subscription. Activating an event-based
        component causes billing for events when the subscription is renewed.

        Note: it is possible to stream events for a subscription at any time, regardless of component activation status.
        The activation status only determines if the subscription should be billed for event-based component usage at
        renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.activate_event_based_component(
                subscription_id, component_id, body=body, request_options=request_options
            ),
        )

    def allocate_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: CreateAllocationRequest | CreateAllocationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllocationResponse:
        """Creates an allocation, sets the current allocated quantity for the component, and records a memo. Allocations
        can only be updated for Quantity, On/Off, and Prepaid Components.

        When creating an allocation via the API, you can pass the ``upgrade_charge``, ``downgrade_credit``, and
        ``accrue_charge`` to be applied.

        > **Note:** These proration and accrual fields are ignored for Prepaid Components since this component type
            always generates charges immediately without proration.

        For information on prorated components and upgrade/downgrade schemes, see `Setting Component Allocations.
        <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration>`__

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        Documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.allocate_component(
                subscription_id, component_id, body=body, request_options=request_options
            ),
        )

    def allocate_components(
        self,
        subscription_id: int,
        *,
        body: AllocateComponents | AllocateComponentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AllocationResponse]:
        """Creates multiple allocations, sets the current allocated quantity for each of the components, and records a
        memo. A ``component_id`` is required for each allocation.

        The charges and/or credits that are created will be rolled up into a single total which is used to determine
        whether this is an upgrade or a downgrade.

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.allocate_components(subscription_id, body=body, request_options=request_options)
        )

    def bulk_record_events(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: list[EbbEvent | EbbEventDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Records a collection of events.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path.

        A maximum of 1000 events can be published in a single request. A 422 will be returned if this limit is exceeded.

        Args:
            api_handle: Identifies the Stream for which the events should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.bulk_record_events(
                api_handle, store_uid=store_uid, body=body, request_options=request_options
            ),
        )

    def bulk_reset_subscription_components_price_points(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Resets all of a subscription's components to use the current default.

        **Note**: this will update the price point for all of the subscription's components, even ones that have not
        been allocated yet.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.bulk_reset_subscription_components_price_points(
                subscription_id, request_options=request_options
            ),
        )

    def bulk_update_subscription_components_price_points(
        self,
        subscription_id: int,
        *,
        body: BulkComponentsPricePointAssignment | BulkComponentsPricePointAssignmentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkComponentsPricePointAssignment:
        """Updates the price points on one or more of a subscription's components.

        The ``price_point`` key can take either a:
        1. Price point id (integer)
        2. Price point handle (string)
        3. ``"_default"`` string, which will reset the price point to the component's current default price point.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ComponentPricePointError1 | RawError``."""
        return unwrap(
            self._with_raw_response.bulk_update_subscription_components_price_points(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def create_usage(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        body: CreateUsageRequest | CreateUsageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageResponse:
        """Records an instance of metered or prepaid usage for a subscription.

        You can report metered or prepaid usage to Advanced Billing as often as you wish. You can report usage as it
        happens or periodically, such as each night or once per billing period.

        Full documentation on how to create Components in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__.
        Additionally, for information on how to record component usage against a subscription, see the following
        resources:

        It is not possible to record metered usage for more than one component at a time. Usage should be reported as
        one API call per component on a single subscription. For example, to record that a subscriber has sent both an
        SMS Message and an Email, send an API call for each.

        See the following product documentation articles for more information:

        - `Create and Manage Components
            <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__
        - `Recording Metered Component Usage
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-metered-component-usage>`__
        - `Reporting Prepaid Component Status
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-prepaid-component-status>`__

        The ``quantity`` from usage for each component is accumulated to the ``unit_balance`` on the `Component Line
        Item <$e/Subscription%20Components/readSubscriptionComponent>`__ for the subscription.

        ## Price Point ID usage

        If you are using price points, for metered and prepaid usage components Advanced Billing gives you the option to
        specify a price point in your request.

        You do not need to specify a price point ID. If a price point is not included, the default price point for the
        component will be used when the usage is recorded.

        ## Deducting Usage

        If you need to reverse a previous usage report or otherwise deduct from the current usage balance, you can
        provide a negative quantity.

        Example:

        Previously recorded quantity was 5000:

        ```json
        {
          "usage": {
            "quantity": 5000,
            "memo": "Recording 5000 units"
          }
        }
        ```

        To reduce the quantity to ``0``, POST the following payload:

        ```json
        {
          "usage": {
            "quantity": -5000,
            "memo": "Deducting 5000 units"
          }
        }
        ```
        The ``unit_balance`` has a floor of ``0``; negative unit balances are never allowed. For example, if the usage
        balance is 100 and you deduct 200 units, the unit balance would then be ``0``, not ``-100``.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_usage(
                subscription_id_or_reference, component_id, body=body, request_options=request_options
            ),
        )

    def deactivate_event_based_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deactivates an event-based component for a single subscription. Deactivating the event-based component causes
        Advanced Billing to ignore related events at subscription renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.deactivate_event_based_component(
                subscription_id, component_id, request_options=request_options
            ),
        )

    def delete_prepaid_usage_allocation(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: CreditSchemeRequest | CreditSchemeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes a prepaid usage allocation.

        Prepaid Usage components are unique in that their allocations are always additive. In order to reduce a
        subscription's allocated quantity for a prepaid usage component, each allocation must be destroyed individually
        via this endpoint.

        ## Credit Scheme

        By default, destroying an allocation will generate a service credit on the subscription. This behavior can be
        modified with the optional ``credit_scheme`` parameter on this endpoint. The accepted values are:

        1. ``none``: The allocation will be destroyed and the balances will be updated but no service credit or refund
            will be created.
        2. ``credit``: The allocation will be destroyed and the balances will be updated and a service credit will be
            generated. This is also the default behavior if the ``credit_scheme`` param is not passed.
        3. ``refund``: The allocation will be destroyed and the balances will be updated and a refund will be issued
            along with a Credit Note.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionComponentAllocationError1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.delete_prepaid_usage_allocation(
                subscription_id, component_id, allocation_id, body=body, request_options=request_options
            ),
        )

    def list_allocations(
        self,
        subscription_id: int,
        component_id: int,
        *,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AllocationResponse]:
        """Lists the 50 most recent Allocations, ordered by most recent first.

        ## On/Off Components

        When a subscription's on/off component has been toggled to on (``1``) or off (``0``), usage will be logged in
        this response.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_allocations(
                subscription_id, component_id, page=page, request_options=request_options
            ),
        )

    def list_subscription_components(
        self,
        subscription_id: int,
        *,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsFilter | ListSubscriptionComponentsFilterDict | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        include: list[ListSubscriptionComponentsIncludeOrStr] | None = None,
        in_use: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SubscriptionComponentResponse]:
        """Lists a subscription's applied components.

        ## Archived Components

        When requesting to list components for a given subscription, if the subscription contains **archived**
        components they will be listed in the server response.

        Args:
            subscription_id: The Chargify id of the subscription.
            date_field: The type of filter you'd like to apply to your search. Use in query ``date_field=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components operation
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            sort: The attribute by which to sort. Use in query ``sort=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            in_use: If in_use is set to true, it returns only components that are currently in use. However, if it's set
                to false or not provided, it returns all components connected with the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_subscription_components(
                subscription_id,
                date_field=date_field,
                direction=direction,
                filter_=filter_,
                end_date=end_date,
                end_datetime=end_datetime,
                price_point_ids=price_point_ids,
                product_family_ids=product_family_ids,
                sort=sort,
                start_date=start_date,
                start_datetime=start_datetime,
                include=include,
                in_use=in_use,
                request_options=request_options,
            ),
        )

    def list_subscription_components_for_site(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsForSiteFilter | ListSubscriptionComponentsForSiteFilterDict | None = None,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        subscription_ids: list[int] | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        include: ListSubscriptionComponentsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionComponentsResponse:
        """Lists components applied to each subscription.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort. Use in query: ``sort=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components For Site operation
            date_field: The type of filter you'd like to apply to your search. Use in query: ``date_field=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in
                query ``start_date=2011-12-15``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2011-12-16``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date. Use in query ``end_datetime=2022-07-01 09:00:05``.
            subscription_ids: Allows fetching components allocation with matching subscription id based on provided ids.
                Use in query ``subscription_ids=1,2,3``.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_subscription_components_for_site(
                page=page,
                per_page=per_page,
                sort=sort,
                direction=direction,
                filter_=filter_,
                date_field=date_field,
                start_date=start_date,
                start_datetime=start_datetime,
                end_date=end_date,
                end_datetime=end_datetime,
                subscription_ids=subscription_ids,
                price_point_ids=price_point_ids,
                product_family_ids=product_family_ids,
                include=include,
                request_options=request_options,
            ),
        )

    def list_usages(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        since_id: int | None = None,
        max_id: int | None = None,
        since_date: Date | None = None,
        until_date: Date | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UsageResponse]:
        """Lists usages associated with a subscription for a particular metered component. This will display the
        previously recorded components for a subscription.

        This endpoint is not compatible with quantity-based components.

        ## Since Date and Until Date Usage

        Note: The ``since_date`` and ``until_date`` attributes each default to midnight on the date specified. For
        example, in order to list usages for January 20th, you would need to append the following to the URL.

        ```
        ?since_date=2016-01-20&until_date=2016-01-21
        ```

        ## Read Usage by Handle

        Use this endpoint to read the previously recorded components for a subscription. You can now specify either the
        component id (integer) or the component handle prefixed by "handle:" to specify the unique identifier for the
        component you are working with.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            since_id: Returns usages with an id greater than or equal to the one specified.
            max_id: Returns usages with an id less than or equal to the one specified.
            since_date: Returns usages with a created_at date greater than or equal to midnight (12:00 AM) on the date
                specified.
            until_date: Returns usages with a created_at date less than or equal to midnight (12:00 AM) on the date
                specified.
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
            self._with_raw_response.list_usages(
                subscription_id_or_reference,
                component_id,
                since_id=since_id,
                max_id=max_id,
                since_date=since_date,
                until_date=until_date,
                page=page,
                per_page=per_page,
                request_options=request_options,
            ),
        )

    def preview_allocations(
        self,
        subscription_id: int,
        *,
        body: PreviewAllocationsRequest | PreviewAllocationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllocationPreviewResponse:
        """Previews a potential subscription's **quantity-based** or **on/off** component allocation in the middle of
        the current billing period. This is useful if you want users to be able to see the effect of a component
        operation before actually doing it.

        ## Fine-grained Component Control: Use with multiple ``upgrade_charge``s or ``downgrade_credits``

        When the allocation uses multiple different types of ``upgrade_charge``s or ``downgrade_credit``s, the
        Allocation is viewed as an Allocation which uses "Fine-Grained Component Control". As a result, the response
        will not include ``direction`` and ``proration`` within the ``allocation_preview``, but at the ``line_items``
        and ``allocations`` level respectfully.

        See example below for Fine-Grained Component Control response.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ComponentAllocationError1 | RawError``."""
        return unwrap(
            self._with_raw_response.preview_allocations(subscription_id, body=body, request_options=request_options)
        )

    def read_subscription_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionComponentResponse:
        """Returns information for a specific component on a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component. Alternatively, the component's handle prefixed by
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_subscription_component(
                subscription_id, component_id, request_options=request_options
            ),
        )

    def record_event(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: EbbEvent | EbbEventDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Records a single event for Events-Based Billing.

        Events-Based Billing is an evolved form of metered billing that is based on data-rich events streamed in
        real-time from your system to Advanced Billing.

        These events can then be transformed, enriched, or analyzed to form the computed totals of usage charges billed
        to your customers.

        This API allows you to stream events into the Advanced Billing data ingestion engine.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path. For example:

        ```
        https://events.chargify.com/my-site-subdomain/events/my-stream-api-handle
        ```

        Args:
            api_handle: Identifies the Stream for which the event should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.record_event(
                api_handle, store_uid=store_uid, body=body, request_options=request_options
            ),
        )

    def update_prepaid_usage_allocation_expiration_date(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: UpdateAllocationExpirationDate | UpdateAllocationExpirationDateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the expiration date for a prepaid usage allocation. This expiration date can be changed after the
        fact to allow for extending or shortening the allocation's active window.

        In order to change a prepaid usage allocation's expiration date, a PUT call must be made to the allocation's
        endpoint with a new expiration date.

        ## Limitations

        A few limitations exist when changing an allocation's expiration date:

        - An expiration date can only be changed for an allocation that belongs to a price point with expiration
            interval options explicitly set.
        - An expiration date can be changed towards the future with no limitations.
        - An expiration date can be changed towards the past (essentially expiring it) up to the subscription's current
            period beginning date.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionComponentAllocationError1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.update_prepaid_usage_allocation_expiration_date(
                subscription_id, component_id, allocation_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SubscriptionComponentsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionComponents:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionComponentsWithRawResponse(client, server, auth)

    async def activate_event_based_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: ActivateEventBasedComponent | ActivateEventBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Activates an event-based component for a single subscription.

        To bill your subscribers on your Events data under the Events-Based Billing feature, the components must be
        activated for the subscriber.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Use this endpoint to activate an event-based component for a single subscription. Activating an event-based
        component causes billing for events when the subscription is renewed.

        Note: it is possible to stream events for a subscription at any time, regardless of component activation status.
        The activation status only determines if the subscription should be billed for event-based component usage at
        renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.activate_event_based_component(
                subscription_id, component_id, body=body, request_options=request_options
            ),
        )

    async def allocate_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: CreateAllocationRequest | CreateAllocationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllocationResponse:
        """Creates an allocation, sets the current allocated quantity for the component, and records a memo. Allocations
        can only be updated for Quantity, On/Off, and Prepaid Components.

        When creating an allocation via the API, you can pass the ``upgrade_charge``, ``downgrade_credit``, and
        ``accrue_charge`` to be applied.

        > **Note:** These proration and accrual fields are ignored for Prepaid Components since this component type
            always generates charges immediately without proration.

        For information on prorated components and upgrade/downgrade schemes, see `Setting Component Allocations.
        <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration>`__

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        Documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.allocate_component(
                subscription_id, component_id, body=body, request_options=request_options
            ),
        )

    async def allocate_components(
        self,
        subscription_id: int,
        *,
        body: AllocateComponents | AllocateComponentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AllocationResponse]:
        """Creates multiple allocations, sets the current allocated quantity for each of the components, and records a
        memo. A ``component_id`` is required for each allocation.

        The charges and/or credits that are created will be rolled up into a single total which is used to determine
        whether this is an upgrade or a downgrade.

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.allocate_components(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def bulk_record_events(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: list[EbbEvent | EbbEventDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Records a collection of events.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path.

        A maximum of 1000 events can be published in a single request. A 422 will be returned if this limit is exceeded.

        Args:
            api_handle: Identifies the Stream for which the events should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_record_events(
                api_handle, store_uid=store_uid, body=body, request_options=request_options
            ),
        )

    async def bulk_reset_subscription_components_price_points(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Resets all of a subscription's components to use the current default.

        **Note**: this will update the price point for all of the subscription's components, even ones that have not
        been allocated yet.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_reset_subscription_components_price_points(
                subscription_id, request_options=request_options
            ),
        )

    async def bulk_update_subscription_components_price_points(
        self,
        subscription_id: int,
        *,
        body: BulkComponentsPricePointAssignment | BulkComponentsPricePointAssignmentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkComponentsPricePointAssignment:
        """Updates the price points on one or more of a subscription's components.

        The ``price_point`` key can take either a:
        1. Price point id (integer)
        2. Price point handle (string)
        3. ``"_default"`` string, which will reset the price point to the component's current default price point.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ComponentPricePointError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_update_subscription_components_price_points(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def create_usage(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        body: CreateUsageRequest | CreateUsageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageResponse:
        """Records an instance of metered or prepaid usage for a subscription.

        You can report metered or prepaid usage to Advanced Billing as often as you wish. You can report usage as it
        happens or periodically, such as each night or once per billing period.

        Full documentation on how to create Components in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__.
        Additionally, for information on how to record component usage against a subscription, see the following
        resources:

        It is not possible to record metered usage for more than one component at a time. Usage should be reported as
        one API call per component on a single subscription. For example, to record that a subscriber has sent both an
        SMS Message and an Email, send an API call for each.

        See the following product documentation articles for more information:

        - `Create and Manage Components
            <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__
        - `Recording Metered Component Usage
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-metered-component-usage>`__
        - `Reporting Prepaid Component Status
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-prepaid-component-status>`__

        The ``quantity`` from usage for each component is accumulated to the ``unit_balance`` on the `Component Line
        Item <$e/Subscription%20Components/readSubscriptionComponent>`__ for the subscription.

        ## Price Point ID usage

        If you are using price points, for metered and prepaid usage components Advanced Billing gives you the option to
        specify a price point in your request.

        You do not need to specify a price point ID. If a price point is not included, the default price point for the
        component will be used when the usage is recorded.

        ## Deducting Usage

        If you need to reverse a previous usage report or otherwise deduct from the current usage balance, you can
        provide a negative quantity.

        Example:

        Previously recorded quantity was 5000:

        ```json
        {
          "usage": {
            "quantity": 5000,
            "memo": "Recording 5000 units"
          }
        }
        ```

        To reduce the quantity to ``0``, POST the following payload:

        ```json
        {
          "usage": {
            "quantity": -5000,
            "memo": "Deducting 5000 units"
          }
        }
        ```
        The ``unit_balance`` has a floor of ``0``; negative unit balances are never allowed. For example, if the usage
        balance is 100 and you deduct 200 units, the unit balance would then be ``0``, not ``-100``.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_usage(
                subscription_id_or_reference, component_id, body=body, request_options=request_options
            ),
        )

    async def deactivate_event_based_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deactivates an event-based component for a single subscription. Deactivating the event-based component causes
        Advanced Billing to ignore related events at subscription renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.deactivate_event_based_component(
                subscription_id, component_id, request_options=request_options
            ),
        )

    async def delete_prepaid_usage_allocation(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: CreditSchemeRequest | CreditSchemeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes a prepaid usage allocation.

        Prepaid Usage components are unique in that their allocations are always additive. In order to reduce a
        subscription's allocated quantity for a prepaid usage component, each allocation must be destroyed individually
        via this endpoint.

        ## Credit Scheme

        By default, destroying an allocation will generate a service credit on the subscription. This behavior can be
        modified with the optional ``credit_scheme`` parameter on this endpoint. The accepted values are:

        1. ``none``: The allocation will be destroyed and the balances will be updated but no service credit or refund
            will be created.
        2. ``credit``: The allocation will be destroyed and the balances will be updated and a service credit will be
            generated. This is also the default behavior if the ``credit_scheme`` param is not passed.
        3. ``refund``: The allocation will be destroyed and the balances will be updated and a refund will be issued
            along with a Credit Note.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionComponentAllocationError1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.delete_prepaid_usage_allocation(
                subscription_id, component_id, allocation_id, body=body, request_options=request_options
            ),
        )

    async def list_allocations(
        self,
        subscription_id: int,
        component_id: int,
        *,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[AllocationResponse]:
        """Lists the 50 most recent Allocations, ordered by most recent first.

        ## On/Off Components

        When a subscription's on/off component has been toggled to on (``1``) or off (``0``), usage will be logged in
        this response.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_allocations(
                subscription_id, component_id, page=page, request_options=request_options
            ),
        )

    async def list_subscription_components(
        self,
        subscription_id: int,
        *,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsFilter | ListSubscriptionComponentsFilterDict | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        include: list[ListSubscriptionComponentsIncludeOrStr] | None = None,
        in_use: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[SubscriptionComponentResponse]:
        """Lists a subscription's applied components.

        ## Archived Components

        When requesting to list components for a given subscription, if the subscription contains **archived**
        components they will be listed in the server response.

        Args:
            subscription_id: The Chargify id of the subscription.
            date_field: The type of filter you'd like to apply to your search. Use in query ``date_field=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components operation
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            sort: The attribute by which to sort. Use in query ``sort=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            in_use: If in_use is set to true, it returns only components that are currently in use. However, if it's set
                to false or not provided, it returns all components connected with the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_subscription_components(
                subscription_id,
                date_field=date_field,
                direction=direction,
                filter_=filter_,
                end_date=end_date,
                end_datetime=end_datetime,
                price_point_ids=price_point_ids,
                product_family_ids=product_family_ids,
                sort=sort,
                start_date=start_date,
                start_datetime=start_datetime,
                include=include,
                in_use=in_use,
                request_options=request_options,
            ),
        )

    async def list_subscription_components_for_site(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsForSiteFilter | ListSubscriptionComponentsForSiteFilterDict | None = None,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        subscription_ids: list[int] | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        include: ListSubscriptionComponentsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionComponentsResponse:
        """Lists components applied to each subscription.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort. Use in query: ``sort=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components For Site operation
            date_field: The type of filter you'd like to apply to your search. Use in query: ``date_field=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in
                query ``start_date=2011-12-15``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2011-12-16``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date. Use in query ``end_datetime=2022-07-01 09:00:05``.
            subscription_ids: Allows fetching components allocation with matching subscription id based on provided ids.
                Use in query ``subscription_ids=1,2,3``.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_subscription_components_for_site(
                page=page,
                per_page=per_page,
                sort=sort,
                direction=direction,
                filter_=filter_,
                date_field=date_field,
                start_date=start_date,
                start_datetime=start_datetime,
                end_date=end_date,
                end_datetime=end_datetime,
                subscription_ids=subscription_ids,
                price_point_ids=price_point_ids,
                product_family_ids=product_family_ids,
                include=include,
                request_options=request_options,
            ),
        )

    async def list_usages(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        since_id: int | None = None,
        max_id: int | None = None,
        since_date: Date | None = None,
        until_date: Date | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[UsageResponse]:
        """Lists usages associated with a subscription for a particular metered component. This will display the
        previously recorded components for a subscription.

        This endpoint is not compatible with quantity-based components.

        ## Since Date and Until Date Usage

        Note: The ``since_date`` and ``until_date`` attributes each default to midnight on the date specified. For
        example, in order to list usages for January 20th, you would need to append the following to the URL.

        ```
        ?since_date=2016-01-20&until_date=2016-01-21
        ```

        ## Read Usage by Handle

        Use this endpoint to read the previously recorded components for a subscription. You can now specify either the
        component id (integer) or the component handle prefixed by "handle:" to specify the unique identifier for the
        component you are working with.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            since_id: Returns usages with an id greater than or equal to the one specified.
            max_id: Returns usages with an id less than or equal to the one specified.
            since_date: Returns usages with a created_at date greater than or equal to midnight (12:00 AM) on the date
                specified.
            until_date: Returns usages with a created_at date less than or equal to midnight (12:00 AM) on the date
                specified.
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
            await self._with_raw_response.list_usages(
                subscription_id_or_reference,
                component_id,
                since_id=since_id,
                max_id=max_id,
                since_date=since_date,
                until_date=until_date,
                page=page,
                per_page=per_page,
                request_options=request_options,
            ),
        )

    async def preview_allocations(
        self,
        subscription_id: int,
        *,
        body: PreviewAllocationsRequest | PreviewAllocationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AllocationPreviewResponse:
        """Previews a potential subscription's **quantity-based** or **on/off** component allocation in the middle of
        the current billing period. This is useful if you want users to be able to see the effect of a component
        operation before actually doing it.

        ## Fine-grained Component Control: Use with multiple ``upgrade_charge``s or ``downgrade_credits``

        When the allocation uses multiple different types of ``upgrade_charge``s or ``downgrade_credit``s, the
        Allocation is viewed as an Allocation which uses "Fine-Grained Component Control". As a result, the response
        will not include ``direction`` and ``proration`` within the ``allocation_preview``, but at the ``line_items``
        and ``allocations`` level respectfully.

        See example below for Fine-Grained Component Control response.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ComponentAllocationError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.preview_allocations(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def read_subscription_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionComponentResponse:
        """Returns information for a specific component on a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component. Alternatively, the component's handle prefixed by
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_subscription_component(
                subscription_id, component_id, request_options=request_options
            ),
        )

    async def record_event(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: EbbEvent | EbbEventDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Records a single event for Events-Based Billing.

        Events-Based Billing is an evolved form of metered billing that is based on data-rich events streamed in
        real-time from your system to Advanced Billing.

        These events can then be transformed, enriched, or analyzed to form the computed totals of usage charges billed
        to your customers.

        This API allows you to stream events into the Advanced Billing data ingestion engine.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path. For example:

        ```
        https://events.chargify.com/my-site-subdomain/events/my-stream-api-handle
        ```

        Args:
            api_handle: Identifies the Stream for which the event should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.record_event(
                api_handle, store_uid=store_uid, body=body, request_options=request_options
            ),
        )

    async def update_prepaid_usage_allocation_expiration_date(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: UpdateAllocationExpirationDate | UpdateAllocationExpirationDateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the expiration date for a prepaid usage allocation. This expiration date can be changed after the
        fact to allow for extending or shortening the allocation's active window.

        In order to change a prepaid usage allocation's expiration date, a PUT call must be made to the allocation's
        endpoint with a new expiration date.

        ## Limitations

        A few limitations exist when changing an allocation's expiration date:

        - An expiration date can only be changed for an allocation that belongs to a price point with expiration
            interval options explicitly set.
        - An expiration date can be changed towards the future with no limitations.
        - An expiration date can be changed towards the past (essentially expiring it) up to the subscription's current
            period beginning date.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``SubscriptionComponentAllocationError1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_prepaid_usage_allocation_expiration_date(
                subscription_id, component_id, allocation_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionComponentsWithRawResponse:
        return self._with_raw_response


class SubscriptionComponentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activate_event_based_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: ActivateEventBasedComponent | ActivateEventBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Activates an event-based component for a single subscription.

        To bill your subscribers on your Events data under the Events-Based Billing feature, the components must be
        activated for the subscriber.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Use this endpoint to activate an event-based component for a single subscription. Activating an event-based
        component causes billing for events when the subscription is renewed.

        Note: it is possible to stream events for a subscription at any time, regardless of component activation status.
        The activation status only determines if the subscription should be billed for event-based component usage at
        renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/activate.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateEventBasedComponent | ActivateEventBasedComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def allocate_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: CreateAllocationRequest | CreateAllocationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllocationResponse, AllocateComponentErrorBody]:
        """Creates an allocation, sets the current allocated quantity for the component, and records a memo. Allocations
        can only be updated for Quantity, On/Off, and Prepaid Components.

        When creating an allocation via the API, you can pass the ``upgrade_charge``, ``downgrade_credit``, and
        ``accrue_charge`` to be applied.

        > **Note:** These proration and accrual fields are ignored for Prepaid Components since this component type
            always generates charges immediately without proration.

        For information on prorated components and upgrade/downgrade schemes, see `Setting Component Allocations.
        <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration>`__

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        Documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAllocationRequest | CreateAllocationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[AllocationResponse],
            error_mapper=allocate_component_error_mapper,
            request_options=request_options,
        )

    def allocate_components(
        self,
        subscription_id: int,
        *,
        body: AllocateComponents | AllocateComponentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AllocationResponse], AllocateComponentsErrorBody]:
        """Creates multiple allocations, sets the current allocated quantity for each of the components, and records a
        memo. A ``component_id`` is required for each allocation.

        The charges and/or credits that are created will be rolled up into a single total which is used to determine
        whether this is an upgrade or a downgrade.

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/allocations.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AllocateComponents | AllocateComponentsDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[AllocationResponse]],
            error_mapper=allocate_components_error_mapper,
            request_options=request_options,
        )

    def bulk_record_events(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: list[EbbEvent | EbbEventDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Records a collection of events.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path.

        A maximum of 1000 events can be published in a single request. A 422 will be returned if this limit is exceeded.

        Args:
            api_handle: Identifies the Stream for which the events should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.ebb("/events/{api_handle}/bulk.json"),
            path_params=[param[str]("api_handle", api_handle)],
            query_params=[param[str | None]("store_uid", store_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[EbbEvent | EbbEventDict] | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_reset_subscription_components_price_points(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, RawError]:
        """Resets all of a subscription's components to use the current default.

        **Note**: this will update the price point for all of the subscription's components, even ones that have not
        been allocated yet.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/price_points/reset.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_update_subscription_components_price_points(
        self,
        subscription_id: int,
        *,
        body: BulkComponentsPricePointAssignment | BulkComponentsPricePointAssignmentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkComponentsPricePointAssignment, BulkUpdateSubscriptionComponentsPricePointsErrorBody]:
        """Updates the price points on one or more of a subscription's components.

        The ``price_point`` key can take either a:
        1. Price point id (integer)
        2. Price point handle (string)
        3. ``"_default"`` string, which will reset the price point to the component's current default price point.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/price_points.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkComponentsPricePointAssignment | BulkComponentsPricePointAssignmentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[BulkComponentsPricePointAssignment],
            error_mapper=bulk_update_subscription_components_price_points_error_mapper,
            request_options=request_options,
        )

    def create_usage(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        body: CreateUsageRequest | CreateUsageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageResponse, CreateUsageErrorBody]:
        """Records an instance of metered or prepaid usage for a subscription.

        You can report metered or prepaid usage to Advanced Billing as often as you wish. You can report usage as it
        happens or periodically, such as each night or once per billing period.

        Full documentation on how to create Components in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__.
        Additionally, for information on how to record component usage against a subscription, see the following
        resources:

        It is not possible to record metered usage for more than one component at a time. Usage should be reported as
        one API call per component on a single subscription. For example, to record that a subscriber has sent both an
        SMS Message and an Email, send an API call for each.

        See the following product documentation articles for more information:

        - `Create and Manage Components
            <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__
        - `Recording Metered Component Usage
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-metered-component-usage>`__
        - `Reporting Prepaid Component Status
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-prepaid-component-status>`__

        The ``quantity`` from usage for each component is accumulated to the ``unit_balance`` on the `Component Line
        Item <$e/Subscription%20Components/readSubscriptionComponent>`__ for the subscription.

        ## Price Point ID usage

        If you are using price points, for metered and prepaid usage components Advanced Billing gives you the option to
        specify a price point in your request.

        You do not need to specify a price point ID. If a price point is not included, the default price point for the
        component will be used when the usage is recorded.

        ## Deducting Usage

        If you need to reverse a previous usage report or otherwise deduct from the current usage balance, you can
        provide a negative quantity.

        Example:

        Previously recorded quantity was 5000:

        ```json
        {
          "usage": {
            "quantity": 5000,
            "memo": "Recording 5000 units"
          }
        }
        ```

        To reduce the quantity to ``0``, POST the following payload:

        ```json
        {
          "usage": {
            "quantity": -5000,
            "memo": "Deducting 5000 units"
          }
        }
        ```
        The ``unit_balance`` has a floor of ``0``; negative unit balances are never allowed. For example, if the usage
        balance is 100 and you deduct 200 units, the unit balance would then be ``0``, not ``-100``.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json"
            ),
            path_params=[
                param[SubscriptionIdOrReference | SubscriptionIdOrReferenceDict](
                    "subscription_id_or_reference", subscription_id_or_reference
                ),
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateUsageRequest | CreateUsageRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[UsageResponse],
            error_mapper=create_usage_error_mapper,
            request_options=request_options,
        )

    def deactivate_event_based_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deactivates an event-based component for a single subscription. Deactivating the event-based component causes
        Advanced Billing to ignore related events at subscription renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/deactivate.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_prepaid_usage_allocation(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: CreditSchemeRequest | CreditSchemeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeletePrepaidUsageAllocationErrorBody]:
        """Deletes a prepaid usage allocation.

        Prepaid Usage components are unique in that their allocations are always additive. In order to reduce a
        subscription's allocated quantity for a prepaid usage component, each allocation must be destroyed individually
        via this endpoint.

        ## Credit Scheme

        By default, destroying an allocation will generate a service credit on the subscription. This behavior can be
        modified with the optional ``credit_scheme`` parameter on this endpoint. The accepted values are:

        1. ``none``: The allocation will be destroyed and the balances will be updated but no service credit or refund
            will be created.
        2. ``credit``: The allocation will be destroyed and the balances will be updated and a service credit will be
            generated. This is also the default behavior if the ``credit_scheme`` param is not passed.
        3. ``refund``: The allocation will be destroyed and the balances will be updated and a refund will be issued
            along with a Credit Note.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("component_id", component_id),
                param[int]("allocation_id", allocation_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreditSchemeRequest | CreditSchemeRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_prepaid_usage_allocation_error_mapper,
            request_options=request_options,
        )

    def list_allocations(
        self,
        subscription_id: int,
        component_id: int,
        *,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AllocationResponse], ListAllocationsErrorBody]:
        """Lists the 50 most recent Allocations, ordered by most recent first.

        ## On/Off Components

        When a subscription's on/off component has been toggled to on (``1``) or off (``0``), usage will be logged in
        this response.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            query_params=[param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[AllocationResponse]],
            error_mapper=list_allocations_error_mapper,
            request_options=request_options,
        )

    def list_subscription_components(
        self,
        subscription_id: int,
        *,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsFilter | ListSubscriptionComponentsFilterDict | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        include: list[ListSubscriptionComponentsIncludeOrStr] | None = None,
        in_use: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SubscriptionComponentResponse], RawError]:
        """Lists a subscription's applied components.

        ## Archived Components

        When requesting to list components for a given subscription, if the subscription contains **archived**
        components they will be listed in the server response.

        Args:
            subscription_id: The Chargify id of the subscription.
            date_field: The type of filter you'd like to apply to your search. Use in query ``date_field=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components operation
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            sort: The attribute by which to sort. Use in query ``sort=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            in_use: If in_use is set to true, it returns only components that are currently in use. However, if it's set
                to false or not provided, it returns all components connected with the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/components.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[SubscriptionListDateFieldOrStr | None]("date_field", date_field),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListSubscriptionComponentsFilter | ListSubscriptionComponentsFilterDict | None](
                    "filter", filter_
                ),
                param[str | None]("end_date", end_date),
                param[str | None]("end_datetime", end_datetime),
                param[IncludeNotNullOrStr | None]("price_point_ids", price_point_ids),
                param[list[int] | None]("product_family_ids", product_family_ids),
                param[ListSubscriptionComponentsSortOrStr | None]("sort", sort),
                param[str | None]("start_date", start_date),
                param[str | None]("start_datetime", start_datetime),
                param[list[ListSubscriptionComponentsIncludeOrStr] | None]("include", include),
                param[bool | None]("in_use", in_use),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[SubscriptionComponentResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_subscription_components_for_site(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsForSiteFilter | ListSubscriptionComponentsForSiteFilterDict | None = None,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        subscription_ids: list[int] | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        include: ListSubscriptionComponentsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionComponentsResponse, RawError]:
        """Lists components applied to each subscription.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort. Use in query: ``sort=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components For Site operation
            date_field: The type of filter you'd like to apply to your search. Use in query: ``date_field=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in
                query ``start_date=2011-12-15``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2011-12-16``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date. Use in query ``end_datetime=2022-07-01 09:00:05``.
            subscription_ids: Allows fetching components allocation with matching subscription id based on provided ids.
                Use in query ``subscription_ids=1,2,3``.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions_components.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListSubscriptionComponentsSortOrStr | None]("sort", sort),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListSubscriptionComponentsForSiteFilter | ListSubscriptionComponentsForSiteFilterDict | None](
                    "filter", filter_
                ),
                param[SubscriptionListDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_date", end_date),
                param[str | None]("end_datetime", end_datetime),
                param[list[int] | None]("subscription_ids", subscription_ids),
                param[IncludeNotNullOrStr | None]("price_point_ids", price_point_ids),
                param[list[int] | None]("product_family_ids", product_family_ids),
                param[ListSubscriptionComponentsIncludeOrStr | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListSubscriptionComponentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_usages(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        since_id: int | None = None,
        max_id: int | None = None,
        since_date: Date | None = None,
        until_date: Date | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UsageResponse], RawError]:
        """Lists usages associated with a subscription for a particular metered component. This will display the
        previously recorded components for a subscription.

        This endpoint is not compatible with quantity-based components.

        ## Since Date and Until Date Usage

        Note: The ``since_date`` and ``until_date`` attributes each default to midnight on the date specified. For
        example, in order to list usages for January 20th, you would need to append the following to the URL.

        ```
        ?since_date=2016-01-20&until_date=2016-01-21
        ```

        ## Read Usage by Handle

        Use this endpoint to read the previously recorded components for a subscription. You can now specify either the
        component id (integer) or the component handle prefixed by "handle:" to specify the unique identifier for the
        component you are working with.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            since_id: Returns usages with an id greater than or equal to the one specified.
            max_id: Returns usages with an id less than or equal to the one specified.
            since_date: Returns usages with a created_at date greater than or equal to midnight (12:00 AM) on the date
                specified.
            until_date: Returns usages with a created_at date less than or equal to midnight (12:00 AM) on the date
                specified.
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
            url_template=self._server.production(
                "/subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json"
            ),
            path_params=[
                param[SubscriptionIdOrReference | SubscriptionIdOrReferenceDict](
                    "subscription_id_or_reference", subscription_id_or_reference
                ),
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
            ],
            query_params=[
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[Date | None]("since_date", since_date),
                param[Date | None]("until_date", until_date),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[UsageResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def preview_allocations(
        self,
        subscription_id: int,
        *,
        body: PreviewAllocationsRequest | PreviewAllocationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllocationPreviewResponse, PreviewAllocationsErrorBody]:
        """Previews a potential subscription's **quantity-based** or **on/off** component allocation in the middle of
        the current billing period. This is useful if you want users to be able to see the effect of a component
        operation before actually doing it.

        ## Fine-grained Component Control: Use with multiple ``upgrade_charge``s or ``downgrade_credits``

        When the allocation uses multiple different types of ``upgrade_charge``s or ``downgrade_credit``s, the
        Allocation is viewed as an Allocation which uses "Fine-Grained Component Control". As a result, the response
        will not include ``direction`` and ``proration`` within the ``allocation_preview``, but at the ``line_items``
        and ``allocations`` level respectfully.

        See example below for Fine-Grained Component Control response.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/allocations/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PreviewAllocationsRequest | PreviewAllocationsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[AllocationPreviewResponse],
            error_mapper=preview_allocations_error_mapper,
            request_options=request_options,
        )

    def read_subscription_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionComponentResponse, ReadSubscriptionComponentErrorBody]:
        """Returns information for a specific component on a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component. Alternatively, the component's handle prefixed by
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/components/{component_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionComponentResponse],
            error_mapper=read_subscription_component_error_mapper,
            request_options=request_options,
        )

    def record_event(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: EbbEvent | EbbEventDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Records a single event for Events-Based Billing.

        Events-Based Billing is an evolved form of metered billing that is based on data-rich events streamed in
        real-time from your system to Advanced Billing.

        These events can then be transformed, enriched, or analyzed to form the computed totals of usage charges billed
        to your customers.

        This API allows you to stream events into the Advanced Billing data ingestion engine.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path. For example:

        ```
        https://events.chargify.com/my-site-subdomain/events/my-stream-api-handle
        ```

        Args:
            api_handle: Identifies the Stream for which the event should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.ebb("/events/{api_handle}.json"),
            path_params=[param[str]("api_handle", api_handle)],
            query_params=[param[str | None]("store_uid", store_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EbbEvent | EbbEventDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_prepaid_usage_allocation_expiration_date(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: UpdateAllocationExpirationDate | UpdateAllocationExpirationDateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdatePrepaidUsageAllocationExpirationDateErrorBody]:
        """Updates the expiration date for a prepaid usage allocation. This expiration date can be changed after the
        fact to allow for extending or shortening the allocation's active window.

        In order to change a prepaid usage allocation's expiration date, a PUT call must be made to the allocation's
        endpoint with a new expiration date.

        ## Limitations

        A few limitations exist when changing an allocation's expiration date:

        - An expiration date can only be changed for an allocation that belongs to a price point with expiration
            interval options explicitly set.
        - An expiration date can be changed towards the future with no limitations.
        - An expiration date can be changed towards the past (essentially expiring it) up to the subscription's current
            period beginning date.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("component_id", component_id),
                param[int]("allocation_id", allocation_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAllocationExpirationDate | UpdateAllocationExpirationDateDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=update_prepaid_usage_allocation_expiration_date_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionComponentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activate_event_based_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: ActivateEventBasedComponent | ActivateEventBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Activates an event-based component for a single subscription.

        To bill your subscribers on your Events data under the Events-Based Billing feature, the components must be
        activated for the subscriber.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Use this endpoint to activate an event-based component for a single subscription. Activating an event-based
        component causes billing for events when the subscription is renewed.

        Note: it is possible to stream events for a subscription at any time, regardless of component activation status.
        The activation status only determines if the subscription should be billed for event-based component usage at
        renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/activate.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActivateEventBasedComponent | ActivateEventBasedComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def allocate_component(
        self,
        subscription_id: int,
        component_id: int,
        *,
        body: CreateAllocationRequest | CreateAllocationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllocationResponse, AllocateComponentErrorBody]:
        """Creates an allocation, sets the current allocated quantity for the component, and records a memo. Allocations
        can only be updated for Quantity, On/Off, and Prepaid Components.

        When creating an allocation via the API, you can pass the ``upgrade_charge``, ``downgrade_credit``, and
        ``accrue_charge`` to be applied.

        > **Note:** These proration and accrual fields are ignored for Prepaid Components since this component type
            always generates charges immediately without proration.

        For information on prorated components and upgrade/downgrade schemes, see `Setting Component Allocations.
        <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration>`__

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        Documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAllocationRequest | CreateAllocationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[AllocationResponse],
            error_mapper=allocate_component_error_mapper,
            request_options=request_options,
        )

    async def allocate_components(
        self,
        subscription_id: int,
        *,
        body: AllocateComponents | AllocateComponentsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AllocationResponse], AllocateComponentsErrorBody]:
        """Creates multiple allocations, sets the current allocated quantity for each of the components, and records a
        memo. A ``component_id`` is required for each allocation.

        The charges and/or credits that are created will be rolled up into a single total which is used to determine
        whether this is an upgrade or a downgrade.

        ### Order of Resolution for upgrade_charge and downgrade_credit

        1. Per allocation in API call (within a single allocation of the ``allocations`` array)
        2. `Component-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__
        3. Allocation API call top level (outside of the ``allocations`` array)
        4. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        ### Order of Resolution for accrue charge

        1. Allocation API call top level (outside of the ``allocations`` array)
        2. `Site-level default value
            <https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Component-Allocations-Proration#proration-schemes>`__

        > **Note:** Proration uses the current price of the component as well as the current tax rates. Changes to
            either may cause the prorated charge/credit to be wrong.

        For more information, see the `Component Allocations
        <https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Component-Allocations-Overview>`__ product
        documentation.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/allocations.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AllocateComponents | AllocateComponentsDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[AllocationResponse]],
            error_mapper=allocate_components_error_mapper,
            request_options=request_options,
        )

    async def bulk_record_events(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: list[EbbEvent | EbbEventDict] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Records a collection of events.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path.

        A maximum of 1000 events can be published in a single request. A 422 will be returned if this limit is exceeded.

        Args:
            api_handle: Identifies the Stream for which the events should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.ebb("/events/{api_handle}/bulk.json"),
            path_params=[param[str]("api_handle", api_handle)],
            query_params=[param[str | None]("store_uid", store_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[EbbEvent | EbbEventDict] | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_reset_subscription_components_price_points(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, RawError]:
        """Resets all of a subscription's components to use the current default.

        **Note**: this will update the price point for all of the subscription's components, even ones that have not
        been allocated yet.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/price_points/reset.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_update_subscription_components_price_points(
        self,
        subscription_id: int,
        *,
        body: BulkComponentsPricePointAssignment | BulkComponentsPricePointAssignmentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkComponentsPricePointAssignment, BulkUpdateSubscriptionComponentsPricePointsErrorBody]:
        """Updates the price points on one or more of a subscription's components.

        The ``price_point`` key can take either a:
        1. Price point id (integer)
        2. Price point handle (string)
        3. ``"_default"`` string, which will reset the price point to the component's current default price point.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/price_points.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkComponentsPricePointAssignment | BulkComponentsPricePointAssignmentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[BulkComponentsPricePointAssignment],
            error_mapper=bulk_update_subscription_components_price_points_error_mapper,
            request_options=request_options,
        )

    async def create_usage(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        body: CreateUsageRequest | CreateUsageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageResponse, CreateUsageErrorBody]:
        """Records an instance of metered or prepaid usage for a subscription.

        You can report metered or prepaid usage to Advanced Billing as often as you wish. You can report usage as it
        happens or periodically, such as each night or once per billing period.

        Full documentation on how to create Components in the Advanced Billing UI can be located `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__.
        Additionally, for information on how to record component usage against a subscription, see the following
        resources:

        It is not possible to record metered usage for more than one component at a time. Usage should be reported as
        one API call per component on a single subscription. For example, to record that a subscriber has sent both an
        SMS Message and an Email, send an API call for each.

        See the following product documentation articles for more information:

        - `Create and Manage Components
            <https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Create-Edit-and-Archive-Components>`__
        - `Recording Metered Component Usage
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-metered-component-usage>`__
        - `Reporting Prepaid Component Status
            <https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Reporting-Component-Allocations#reporting-prepaid-component-status>`__

        The ``quantity`` from usage for each component is accumulated to the ``unit_balance`` on the `Component Line
        Item <$e/Subscription%20Components/readSubscriptionComponent>`__ for the subscription.

        ## Price Point ID usage

        If you are using price points, for metered and prepaid usage components Advanced Billing gives you the option to
        specify a price point in your request.

        You do not need to specify a price point ID. If a price point is not included, the default price point for the
        component will be used when the usage is recorded.

        ## Deducting Usage

        If you need to reverse a previous usage report or otherwise deduct from the current usage balance, you can
        provide a negative quantity.

        Example:

        Previously recorded quantity was 5000:

        ```json
        {
          "usage": {
            "quantity": 5000,
            "memo": "Recording 5000 units"
          }
        }
        ```

        To reduce the quantity to ``0``, POST the following payload:

        ```json
        {
          "usage": {
            "quantity": -5000,
            "memo": "Deducting 5000 units"
          }
        }
        ```
        The ``unit_balance`` has a floor of ``0``; negative unit balances are never allowed. For example, if the usage
        balance is 100 and you deduct 200 units, the unit balance would then be ``0``, not ``-100``.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json"
            ),
            path_params=[
                param[SubscriptionIdOrReference | SubscriptionIdOrReferenceDict](
                    "subscription_id_or_reference", subscription_id_or_reference
                ),
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateUsageRequest | CreateUsageRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[UsageResponse],
            error_mapper=create_usage_error_mapper,
            request_options=request_options,
        )

    async def deactivate_event_based_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Deactivates an event-based component for a single subscription. Deactivating the event-based component causes
        Advanced Billing to ignore related events at subscription renewal.

        Args:
            subscription_id: The Advanced Billing id of the subscription
            component_id: The Advanced Billing id of the component
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/deactivate.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_prepaid_usage_allocation(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: CreditSchemeRequest | CreditSchemeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeletePrepaidUsageAllocationErrorBody]:
        """Deletes a prepaid usage allocation.

        Prepaid Usage components are unique in that their allocations are always additive. In order to reduce a
        subscription's allocated quantity for a prepaid usage component, each allocation must be destroyed individually
        via this endpoint.

        ## Credit Scheme

        By default, destroying an allocation will generate a service credit on the subscription. This behavior can be
        modified with the optional ``credit_scheme`` parameter on this endpoint. The accepted values are:

        1. ``none``: The allocation will be destroyed and the balances will be updated but no service credit or refund
            will be created.
        2. ``credit``: The allocation will be destroyed and the balances will be updated and a service credit will be
            generated. This is also the default behavior if the ``credit_scheme`` param is not passed.
        3. ``refund``: The allocation will be destroyed and the balances will be updated and a refund will be issued
            along with a Credit Note.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("component_id", component_id),
                param[int]("allocation_id", allocation_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreditSchemeRequest | CreditSchemeRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_prepaid_usage_allocation_error_mapper,
            request_options=request_options,
        )

    async def list_allocations(
        self,
        subscription_id: int,
        component_id: int,
        *,
        page: int | None = 1,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[AllocationResponse], ListAllocationsErrorBody]:
        """Lists the 50 most recent Allocations, ordered by most recent first.

        ## On/Off Components

        When a subscription's on/off component has been toggled to on (``1``) or off (``0``), usage will be logged in
        this response.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations.json"
            ),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            query_params=[param[int | None]("page", page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[AllocationResponse]],
            error_mapper=list_allocations_error_mapper,
            request_options=request_options,
        )

    async def list_subscription_components(
        self,
        subscription_id: int,
        *,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsFilter | ListSubscriptionComponentsFilterDict | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        include: list[ListSubscriptionComponentsIncludeOrStr] | None = None,
        in_use: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[SubscriptionComponentResponse], RawError]:
        """Lists a subscription's applied components.

        ## Archived Components

        When requesting to list components for a given subscription, if the subscription contains **archived**
        components they will be listed in the server response.

        Args:
            subscription_id: The Chargify id of the subscription.
            date_field: The type of filter you'd like to apply to your search. Use in query ``date_field=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components operation
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            sort: The attribute by which to sort. Use in query ``sort=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            in_use: If in_use is set to true, it returns only components that are currently in use. However, if it's set
                to false or not provided, it returns all components connected with the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/components.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[SubscriptionListDateFieldOrStr | None]("date_field", date_field),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListSubscriptionComponentsFilter | ListSubscriptionComponentsFilterDict | None](
                    "filter", filter_
                ),
                param[str | None]("end_date", end_date),
                param[str | None]("end_datetime", end_datetime),
                param[IncludeNotNullOrStr | None]("price_point_ids", price_point_ids),
                param[list[int] | None]("product_family_ids", product_family_ids),
                param[ListSubscriptionComponentsSortOrStr | None]("sort", sort),
                param[str | None]("start_date", start_date),
                param[str | None]("start_datetime", start_datetime),
                param[list[ListSubscriptionComponentsIncludeOrStr] | None]("include", include),
                param[bool | None]("in_use", in_use),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[SubscriptionComponentResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_subscription_components_for_site(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        sort: ListSubscriptionComponentsSortOrStr | None = None,
        direction: SortingDirectionOrStr | None = None,
        filter_: ListSubscriptionComponentsForSiteFilter | ListSubscriptionComponentsForSiteFilterDict | None = None,
        date_field: SubscriptionListDateFieldOrStr | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        subscription_ids: list[int] | None = None,
        price_point_ids: IncludeNotNullOrStr | None = None,
        product_family_ids: list[int] | None = None,
        include: ListSubscriptionComponentsIncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionComponentsResponse, RawError]:
        """Lists components applied to each subscription.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            sort: The attribute by which to sort. Use in query: ``sort=updated_at``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            filter_: Filter to use for List Subscription Components For Site operation
            date_field: The type of filter you'd like to apply to your search. Use in query: ``date_field=updated_at``.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in
                query ``start_date=2011-12-15``.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of start_date. Use in query ``start_datetime=2022-07-01 09:00:05``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query
                ``end_date=2011-12-16``.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site''s time zone will be used. If provided, this parameter will be used
                instead of end_date. Use in query ``end_datetime=2022-07-01 09:00:05``.
            subscription_ids: Allows fetching components allocation with matching subscription id based on provided ids.
                Use in query ``subscription_ids=1,2,3``.
            price_point_ids: Allows fetching components allocation only if price point id is present. Use in query
                ``price_point_ids=not_null``.
            product_family_ids: Allows fetching components allocation with matching product family id based on provided
                ids. Use in query ``product_family_ids=1,2,3``.
            include: Allows including additional data in the response. Use in query
                ``include=subscription,historic_usages``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions_components.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListSubscriptionComponentsSortOrStr | None]("sort", sort),
                param[SortingDirectionOrStr | None]("direction", direction),
                param[ListSubscriptionComponentsForSiteFilter | ListSubscriptionComponentsForSiteFilterDict | None](
                    "filter", filter_
                ),
                param[SubscriptionListDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_date", end_date),
                param[str | None]("end_datetime", end_datetime),
                param[list[int] | None]("subscription_ids", subscription_ids),
                param[IncludeNotNullOrStr | None]("price_point_ids", price_point_ids),
                param[list[int] | None]("product_family_ids", product_family_ids),
                param[ListSubscriptionComponentsIncludeOrStr | None]("include", include),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListSubscriptionComponentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_usages(
        self,
        subscription_id_or_reference: SubscriptionIdOrReference | SubscriptionIdOrReferenceDict,
        component_id: ComponentIdModel | ComponentIdModelDict,
        *,
        since_id: int | None = None,
        max_id: int | None = None,
        since_date: Date | None = None,
        until_date: Date | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[UsageResponse], RawError]:
        """Lists usages associated with a subscription for a particular metered component. This will display the
        previously recorded components for a subscription.

        This endpoint is not compatible with quantity-based components.

        ## Since Date and Until Date Usage

        Note: The ``since_date`` and ``until_date`` attributes each default to midnight on the date specified. For
        example, in order to list usages for January 20th, you would need to append the following to the URL.

        ```
        ?since_date=2016-01-20&until_date=2016-01-21
        ```

        ## Read Usage by Handle

        Use this endpoint to read the previously recorded components for a subscription. You can now specify either the
        component id (integer) or the component handle prefixed by "handle:" to specify the unique identifier for the
        component you are working with.

        Args:
            subscription_id_or_reference: Either the Advanced Billing subscription ID (integer) or the subscription
                reference (string). Important: In cases where a numeric string value matches both an existing
                subscription ID and an existing subscription reference, the system will prioritize the subscription ID
                lookup. For example, if both subscription ID 123 and subscription reference "123" exist, passing "123"
                will return the subscription with ID 123.
            component_id: Either the Advanced Billing id for the component or the component's handle prefixed by
                ``handle:``
            since_id: Returns usages with an id greater than or equal to the one specified.
            max_id: Returns usages with an id less than or equal to the one specified.
            since_date: Returns usages with a created_at date greater than or equal to midnight (12:00 AM) on the date
                specified.
            until_date: Returns usages with a created_at date less than or equal to midnight (12:00 AM) on the date
                specified.
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
            url_template=self._server.production(
                "/subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json"
            ),
            path_params=[
                param[SubscriptionIdOrReference | SubscriptionIdOrReferenceDict](
                    "subscription_id_or_reference", subscription_id_or_reference
                ),
                param[ComponentIdModel | ComponentIdModelDict]("component_id", component_id),
            ],
            query_params=[
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[Date | None]("since_date", since_date),
                param[Date | None]("until_date", until_date),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[UsageResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def preview_allocations(
        self,
        subscription_id: int,
        *,
        body: PreviewAllocationsRequest | PreviewAllocationsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AllocationPreviewResponse, PreviewAllocationsErrorBody]:
        """Previews a potential subscription's **quantity-based** or **on/off** component allocation in the middle of
        the current billing period. This is useful if you want users to be able to see the effect of a component
        operation before actually doing it.

        ## Fine-grained Component Control: Use with multiple ``upgrade_charge``s or ``downgrade_credits``

        When the allocation uses multiple different types of ``upgrade_charge``s or ``downgrade_credit``s, the
        Allocation is viewed as an Allocation which uses "Fine-Grained Component Control". As a result, the response
        will not include ``direction`` and ``proration`` within the ``allocation_preview``, but at the ``line_items``
        and ``allocations`` level respectfully.

        See example below for Fine-Grained Component Control response.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/allocations/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PreviewAllocationsRequest | PreviewAllocationsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[AllocationPreviewResponse],
            error_mapper=preview_allocations_error_mapper,
            request_options=request_options,
        )

    async def read_subscription_component(
        self, subscription_id: int, component_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionComponentResponse, ReadSubscriptionComponentErrorBody]:
        """Returns information for a specific component on a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component. Alternatively, the component's handle prefixed by
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/components/{component_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id), param[int]("component_id", component_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionComponentResponse],
            error_mapper=read_subscription_component_error_mapper,
            request_options=request_options,
        )

    async def record_event(
        self,
        api_handle: str,
        *,
        store_uid: str | None = None,
        body: EbbEvent | EbbEventDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Records a single event for Events-Based Billing.

        Events-Based Billing is an evolved form of metered billing that is based on data-rich events streamed in
        real-time from your system to Advanced Billing.

        These events can then be transformed, enriched, or analyzed to form the computed totals of usage charges billed
        to your customers.

        This API allows you to stream events into the Advanced Billing data ingestion engine.

        For more information, see `Design Your Catalog
        <https://docs.maxio.com/hc/en-us/articles/24181036583053-Design-Your-Catalog?method=componenttypes>`__.

        Note: this endpoint differs from the standard URL for this API in that ``events`` and your site subdomain are
        included in the path. For example:

        ```
        https://events.chargify.com/my-site-subdomain/events/my-stream-api-handle
        ```

        Args:
            api_handle: Identifies the Stream for which the event should be published.
            store_uid: If you've attached your own Keen project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store. This applies to Legacy Metering sites only — it has no effect on
                Maxio Metering sites.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.ebb("/events/{api_handle}.json"),
            path_params=[param[str]("api_handle", api_handle)],
            query_params=[param[str | None]("store_uid", store_uid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EbbEvent | EbbEventDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_prepaid_usage_allocation_expiration_date(
        self,
        subscription_id: int,
        component_id: int,
        allocation_id: int,
        *,
        body: UpdateAllocationExpirationDate | UpdateAllocationExpirationDateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdatePrepaidUsageAllocationExpirationDateErrorBody]:
        """Updates the expiration date for a prepaid usage allocation. This expiration date can be changed after the
        fact to allow for extending or shortening the allocation's active window.

        In order to change a prepaid usage allocation's expiration date, a PUT call must be made to the allocation's
        endpoint with a new expiration date.

        ## Limitations

        A few limitations exist when changing an allocation's expiration date:

        - An expiration date can only be changed for an allocation that belongs to a price point with expiration
            interval options explicitly set.
        - An expiration date can be changed towards the future with no limitations.
        - An expiration date can be changed towards the past (essentially expiring it) up to the subscription's current
            period beginning date.

        Args:
            subscription_id: The Chargify id of the subscription.
            component_id: The Advanced Billing id of the component
            allocation_id: The Advanced Billing id of the allocation
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json"
            ),
            path_params=[
                param[int]("subscription_id", subscription_id),
                param[int]("component_id", component_id),
                param[int]("allocation_id", allocation_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAllocationExpirationDate | UpdateAllocationExpirationDateDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=update_prepaid_usage_allocation_expiration_date_error_mapper,
            request_options=request_options,
        )
