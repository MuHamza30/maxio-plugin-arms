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
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.archive_component_error import ArchiveComponentErrorBody, archive_component_error_mapper
from ..errors.create_event_based_component_error import (
    CreateEventBasedComponentErrorBody,
    create_event_based_component_error_mapper,
)
from ..errors.create_metered_component_error import (
    CreateMeteredComponentErrorBody,
    create_metered_component_error_mapper,
)
from ..errors.create_on_off_component_error import CreateOnOffComponentErrorBody, create_on_off_component_error_mapper
from ..errors.create_prepaid_usage_component_error import (
    CreatePrepaidUsageComponentErrorBody,
    create_prepaid_usage_component_error_mapper,
)
from ..errors.create_quantity_based_component_error import (
    CreateQuantityBasedComponentErrorBody,
    create_quantity_based_component_error_mapper,
)
from ..errors.update_component_error import UpdateComponentErrorBody, update_component_error_mapper
from ..errors.update_product_family_component_error import (
    UpdateProductFamilyComponentErrorBody,
    update_product_family_component_error_mapper,
)
from ..models.component import Component
from ..models.component_response import ComponentResponse
from ..models.create_ebb_component import CreateEbbComponent, CreateEbbComponentDict
from ..models.create_metered_component import CreateMeteredComponent, CreateMeteredComponentDict
from ..models.create_on_off_component import CreateOnOffComponent, CreateOnOffComponentDict
from ..models.create_prepaid_component import CreatePrepaidComponent, CreatePrepaidComponentDict
from ..models.create_quantity_based_component import CreateQuantityBasedComponent, CreateQuantityBasedComponentDict
from ..models.enums.basic_date_field import BasicDateFieldOrStr
from ..models.list_components_filter import ListComponentsFilter, ListComponentsFilterDict
from ..models.update_component_request import UpdateComponentRequest, UpdateComponentRequestDict
from ..server.server import Server


class Components:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ComponentsWithRawResponse(client, server, auth)

    def archive_component(
        self, product_family_id: int, component_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Component:
        """Archives the component; all current subscribers will continue to be charged as usual.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.archive_component(product_family_id, component_id, request_options=request_options)
        )

    def create_event_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateEbbComponent | CreateEbbComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates an event-based component definition under the specified product family. An event-based component can
        then be added and “allocated” for a subscription.

        Event-based components are similar to other component types, in that you define the component parameters (such
        as name and taxability) and the pricing. A key difference for the event-based component is that it must be
        attached to a metric. This is because the metric provides the component with the actual quantity used in
        computing what and how much will be billed each period for each subscription.

        So, instead of reporting usage directly for each component (as you would with metered components), the usage is
        derived from analysis of your events.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_event_based_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    def create_metered_component(
        self,
        product_family_id: str,
        *,
        body: CreateMeteredComponent | CreateMeteredComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates a metered component definition under the specified product family. A metered component can then be
        added and “allocated” for a subscription.

        Metered components are used to bill for any type of unit that resets to 0 at the end of the billing period
        (think daily Google Ads clicks or monthly cell phone minutes). This is most commonly associated with usage-based
        billing and many other pricing schemes.

        Note that this is different from recurring quantity-based components, which DO NOT reset to zero at the start of
        every billing period. If you want to bill for a quantity of something that does not change unless you change it,
        then you want quantity components, instead.

        #### Hybrid Pricing A ``volume``, ``tiered``, or ``stairstep`` metered component can combine its primary pricing
        with a secondary pricing model (the ``overage_pricing`` parameter) so both bill as a single invoice line item
        instead of two. This does not apply to metered components configured for event-based billing (metric, meter, or
        formula). See `Hybrid Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and
        configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_metered_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    def create_on_off_component(
        self,
        product_family_id: str,
        *,
        body: CreateOnOffComponent | CreateOnOffComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates an On/Off component definition under the specified product family. An On/Off component can then be
        added and “allocated” for a subscription.

        On/off components are used for any flat fee, recurring add on (think $99/month for tech support or a flat add on
        shipping fee).

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_on_off_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    def create_prepaid_usage_component(
        self,
        product_family_id: str,
        *,
        body: CreatePrepaidComponent | CreatePrepaidComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates a prepaid usage component definition under the specified product family. A prepaid component can then
        be added and “allocated” for a subscription.

        Prepaid components allow customers to pre-purchase units that can be used up over time on their subscription. In
        a sense, they are the mirror image of metered components; while metered components charge at the end of the
        period for the amount of units used, prepaid components are charged for at the time of purchase, and usage is
        subsequently tracked against the amount purchased.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_prepaid_usage_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    def create_quantity_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates a Quantity Based component definition under the specified product family. A Quantity Based component
        can then be added and “allocated” for a subscription.

        When defining a Quantity Based component, you can choose one of two types: #### Recurring Recurring
        quantity-based components are used to bill for the number of some unit (think monthly software user licenses or
        the number of pairs of socks in a box-a-month club). This is most commonly associated with billing for user
        licenses, number of users, number of employees, etc.

        #### One-time One-time quantity-based components are used to create ad hoc usage charges that do not recur. For
        example, at the time of signup, you might want to charge your customer a one-time fee for onboarding or other
        services.

        The allocated quantity for one-time quantity-based components immediately gets reset back to zero after the
        allocation is made.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__. #### Hybrid Pricing A
        ``volume``, ``tiered``, or ``stairstep`` component can combine its primary pricing with a secondary pricing
        model (the ``overage_pricing`` parameter) so both bill as a single invoice line item instead of two. See `Hybrid
        Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_quantity_based_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    def find_component(self, handle: str, *, request_options: RequestOptionsOrDict | None = None) -> ComponentResponse:
        """Returns information for a component matching the provided handle. You can identify your components with a
        handle so you don't have to save or reference the IDs we generate.

        Args:
            handle: The handle of the component to find
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.find_component(handle, request_options=request_options))

    def list_components(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ComponentResponse]:
        """Lists components for a site.

        Args:
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_components(
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                include_archived=include_archived,
                page=page,
                per_page=per_page,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    def list_components_for_product_family(
        self,
        product_family_id: int,
        *,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        date_field: BasicDateFieldOrStr | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ComponentResponse]:
        """Lists components for a particular product family.

        Args:
            product_family_id: The Advanced Billing id of the product family
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=created_at``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_components_for_product_family(
                product_family_id,
                include_archived=include_archived,
                page=page,
                per_page=per_page,
                filter_=filter_,
                date_field=date_field,
                end_date=end_date,
                end_datetime=end_datetime,
                start_date=start_date,
                start_datetime=start_datetime,
                request_options=request_options,
            ),
        )

    def read_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Returns information regarding a component from a specific product family.

        You can read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_component(
                product_family_id, component_id, include_features=include_features, request_options=request_options
            ),
        )

    def update_component(
        self,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Updates a component.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            component_id: The id or handle of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_component(component_id, body=body, request_options=request_options)
        )

    def update_product_family_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Updates a component from a specific product family.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_product_family_component(
                product_family_id, component_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ComponentsWithRawResponse:
        return self._with_raw_response


class AsyncComponents:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncComponentsWithRawResponse(client, server, auth)

    async def archive_component(
        self, product_family_id: int, component_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Component:
        """Archives the component; all current subscribers will continue to be charged as usual.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.archive_component(
                product_family_id, component_id, request_options=request_options
            ),
        )

    async def create_event_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateEbbComponent | CreateEbbComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates an event-based component definition under the specified product family. An event-based component can
        then be added and “allocated” for a subscription.

        Event-based components are similar to other component types, in that you define the component parameters (such
        as name and taxability) and the pricing. A key difference for the event-based component is that it must be
        attached to a metric. This is because the metric provides the component with the actual quantity used in
        computing what and how much will be billed each period for each subscription.

        So, instead of reporting usage directly for each component (as you would with metered components), the usage is
        derived from analysis of your events.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_event_based_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    async def create_metered_component(
        self,
        product_family_id: str,
        *,
        body: CreateMeteredComponent | CreateMeteredComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates a metered component definition under the specified product family. A metered component can then be
        added and “allocated” for a subscription.

        Metered components are used to bill for any type of unit that resets to 0 at the end of the billing period
        (think daily Google Ads clicks or monthly cell phone minutes). This is most commonly associated with usage-based
        billing and many other pricing schemes.

        Note that this is different from recurring quantity-based components, which DO NOT reset to zero at the start of
        every billing period. If you want to bill for a quantity of something that does not change unless you change it,
        then you want quantity components, instead.

        #### Hybrid Pricing A ``volume``, ``tiered``, or ``stairstep`` metered component can combine its primary pricing
        with a secondary pricing model (the ``overage_pricing`` parameter) so both bill as a single invoice line item
        instead of two. This does not apply to metered components configured for event-based billing (metric, meter, or
        formula). See `Hybrid Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and
        configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_metered_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    async def create_on_off_component(
        self,
        product_family_id: str,
        *,
        body: CreateOnOffComponent | CreateOnOffComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates an On/Off component definition under the specified product family. An On/Off component can then be
        added and “allocated” for a subscription.

        On/off components are used for any flat fee, recurring add on (think $99/month for tech support or a flat add on
        shipping fee).

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_on_off_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    async def create_prepaid_usage_component(
        self,
        product_family_id: str,
        *,
        body: CreatePrepaidComponent | CreatePrepaidComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates a prepaid usage component definition under the specified product family. A prepaid component can then
        be added and “allocated” for a subscription.

        Prepaid components allow customers to pre-purchase units that can be used up over time on their subscription. In
        a sense, they are the mirror image of metered components; while metered components charge at the end of the
        period for the amount of units used, prepaid components are charged for at the time of purchase, and usage is
        subsequently tracked against the amount purchased.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_prepaid_usage_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    async def create_quantity_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Creates a Quantity Based component definition under the specified product family. A Quantity Based component
        can then be added and “allocated” for a subscription.

        When defining a Quantity Based component, you can choose one of two types: #### Recurring Recurring
        quantity-based components are used to bill for the number of some unit (think monthly software user licenses or
        the number of pairs of socks in a box-a-month club). This is most commonly associated with billing for user
        licenses, number of users, number of employees, etc.

        #### One-time One-time quantity-based components are used to create ad hoc usage charges that do not recur. For
        example, at the time of signup, you might want to charge your customer a one-time fee for onboarding or other
        services.

        The allocated quantity for one-time quantity-based components immediately gets reset back to zero after the
        allocation is made.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__. #### Hybrid Pricing A
        ``volume``, ``tiered``, or ``stairstep`` component can combine its primary pricing with a secondary pricing
        model (the ``overage_pricing`` parameter) so both bill as a single invoice line item instead of two. See `Hybrid
        Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_quantity_based_component(
                product_family_id, body=body, request_options=request_options
            ),
        )

    async def find_component(
        self, handle: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ComponentResponse:
        """Returns information for a component matching the provided handle. You can identify your components with a
        handle so you don't have to save or reference the IDs we generate.

        Args:
            handle: The handle of the component to find
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.find_component(handle, request_options=request_options))

    async def list_components(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ComponentResponse]:
        """Lists components for a site.

        Args:
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_components(
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                include_archived=include_archived,
                page=page,
                per_page=per_page,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    async def list_components_for_product_family(
        self,
        product_family_id: int,
        *,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        date_field: BasicDateFieldOrStr | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[ComponentResponse]:
        """Lists components for a particular product family.

        Args:
            product_family_id: The Advanced Billing id of the product family
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=created_at``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_components_for_product_family(
                product_family_id,
                include_archived=include_archived,
                page=page,
                per_page=per_page,
                filter_=filter_,
                date_field=date_field,
                end_date=end_date,
                end_datetime=end_datetime,
                start_date=start_date,
                start_datetime=start_datetime,
                request_options=request_options,
            ),
        )

    async def read_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Returns information regarding a component from a specific product family.

        You can read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_component(
                product_family_id, component_id, include_features=include_features, request_options=request_options
            ),
        )

    async def update_component(
        self,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Updates a component.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            component_id: The id or handle of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_component(component_id, body=body, request_options=request_options)
        )

    async def update_product_family_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ComponentResponse:
        """Updates a component from a specific product family.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_product_family_component(
                product_family_id, component_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncComponentsWithRawResponse:
        return self._with_raw_response


class ComponentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_component(
        self, product_family_id: int, component_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Component, ArchiveComponentErrorBody]:
        """Archives the component; all current subscribers will continue to be charged as usual.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/product_families/{product_family_id}/components/{component_id}.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[Component],
            error_mapper=archive_component_error_mapper,
            request_options=request_options,
        )

    def create_event_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateEbbComponent | CreateEbbComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateEventBasedComponentErrorBody]:
        """Creates an event-based component definition under the specified product family. An event-based component can
        then be added and “allocated” for a subscription.

        Event-based components are similar to other component types, in that you define the component parameters (such
        as name and taxability) and the pricing. A key difference for the event-based component is that it must be
        attached to a metric. This is because the metric provides the component with the actual quantity used in
        computing what and how much will be billed each period for each subscription.

        So, instead of reporting usage directly for each component (as you would with metered components), the usage is
        derived from analysis of your events.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/event_based_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateEbbComponent | CreateEbbComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=create_event_based_component_error_mapper,
            request_options=request_options,
        )

    def create_metered_component(
        self,
        product_family_id: str,
        *,
        body: CreateMeteredComponent | CreateMeteredComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateMeteredComponentErrorBody]:
        """Creates a metered component definition under the specified product family. A metered component can then be
        added and “allocated” for a subscription.

        Metered components are used to bill for any type of unit that resets to 0 at the end of the billing period
        (think daily Google Ads clicks or monthly cell phone minutes). This is most commonly associated with usage-based
        billing and many other pricing schemes.

        Note that this is different from recurring quantity-based components, which DO NOT reset to zero at the start of
        every billing period. If you want to bill for a quantity of something that does not change unless you change it,
        then you want quantity components, instead.

        #### Hybrid Pricing A ``volume``, ``tiered``, or ``stairstep`` metered component can combine its primary pricing
        with a secondary pricing model (the ``overage_pricing`` parameter) so both bill as a single invoice line item
        instead of two. This does not apply to metered components configured for event-based billing (metric, meter, or
        formula). See `Hybrid Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and
        configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/metered_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMeteredComponent | CreateMeteredComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=create_metered_component_error_mapper,
            request_options=request_options,
        )

    def create_on_off_component(
        self,
        product_family_id: str,
        *,
        body: CreateOnOffComponent | CreateOnOffComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateOnOffComponentErrorBody]:
        """Creates an On/Off component definition under the specified product family. An On/Off component can then be
        added and “allocated” for a subscription.

        On/off components are used for any flat fee, recurring add on (think $99/month for tech support or a flat add on
        shipping fee).

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/on_off_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOnOffComponent | CreateOnOffComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=create_on_off_component_error_mapper,
            request_options=request_options,
        )

    def create_prepaid_usage_component(
        self,
        product_family_id: str,
        *,
        body: CreatePrepaidComponent | CreatePrepaidComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreatePrepaidUsageComponentErrorBody]:
        """Creates a prepaid usage component definition under the specified product family. A prepaid component can then
        be added and “allocated” for a subscription.

        Prepaid components allow customers to pre-purchase units that can be used up over time on their subscription. In
        a sense, they are the mirror image of metered components; while metered components charge at the end of the
        period for the amount of units used, prepaid components are charged for at the time of purchase, and usage is
        subsequently tracked against the amount purchased.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/prepaid_usage_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePrepaidComponent | CreatePrepaidComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=create_prepaid_usage_component_error_mapper,
            request_options=request_options,
        )

    def create_quantity_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateQuantityBasedComponentErrorBody]:
        """Creates a Quantity Based component definition under the specified product family. A Quantity Based component
        can then be added and “allocated” for a subscription.

        When defining a Quantity Based component, you can choose one of two types: #### Recurring Recurring
        quantity-based components are used to bill for the number of some unit (think monthly software user licenses or
        the number of pairs of socks in a box-a-month club). This is most commonly associated with billing for user
        licenses, number of users, number of employees, etc.

        #### One-time One-time quantity-based components are used to create ad hoc usage charges that do not recur. For
        example, at the time of signup, you might want to charge your customer a one-time fee for onboarding or other
        services.

        The allocated quantity for one-time quantity-based components immediately gets reset back to zero after the
        allocation is made.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__. #### Hybrid Pricing A
        ``volume``, ``tiered``, or ``stairstep`` component can combine its primary pricing with a secondary pricing
        model (the ``overage_pricing`` parameter) so both bill as a single invoice line item instead of two. See `Hybrid
        Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/product_families/{product_family_id}/quantity_based_components.json"
            ),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=create_quantity_based_component_error_mapper,
            request_options=request_options,
        )

    def find_component(
        self, handle: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComponentResponse, RawError]:
        """Returns information for a component matching the provided handle. You can identify your components with a
        handle so you don't have to save or reference the IDs we generate.

        Args:
            handle: The handle of the component to find
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/lookup.json"),
            query_params=[param[str]("handle", handle)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_components(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ComponentResponse], RawError]:
        """Lists components for a site.

        Args:
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components.json"),
            query_params=[
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[bool | None]("include_archived", include_archived),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListComponentsFilter | ListComponentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ComponentResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_components_for_product_family(
        self,
        product_family_id: int,
        *,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        date_field: BasicDateFieldOrStr | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ComponentResponse], RawError]:
        """Lists components for a particular product family.

        Args:
            product_family_id: The Advanced Billing id of the product family
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=created_at``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/components.json"),
            path_params=[param[int]("product_family_id", product_family_id)],
            query_params=[
                param[bool | None]("include_archived", include_archived),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListComponentsFilter | ListComponentsFilterDict | None]("filter", filter_),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("end_date", end_date),
                param[str | None]("end_datetime", end_datetime),
                param[str | None]("start_date", start_date),
                param[str | None]("start_datetime", start_datetime),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[ComponentResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, RawError]:
        """Returns information regarding a component from a specific product family.

        You can read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/product_families/{product_family_id}/components/{component_id}.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[str]("component_id", component_id)],
            query_params=[param[bool | None]("include_features", include_features)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_component(
        self,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, UpdateComponentErrorBody]:
        """Updates a component.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            component_id: The id or handle of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/components/{component_id}.json"),
            path_params=[param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateComponentRequest | UpdateComponentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=update_component_error_mapper,
            request_options=request_options,
        )

    def update_product_family_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, UpdateProductFamilyComponentErrorBody]:
        """Updates a component from a specific product family.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/product_families/{product_family_id}/components/{component_id}.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateComponentRequest | UpdateComponentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ComponentResponse],
            error_mapper=update_product_family_component_error_mapper,
            request_options=request_options,
        )


class AsyncComponentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_component(
        self, product_family_id: int, component_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Component, ArchiveComponentErrorBody]:
        """Archives the component; all current subscribers will continue to be charged as usual.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production(
                "/product_families/{product_family_id}/components/{component_id}.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[Component],
            error_mapper=archive_component_error_mapper,
            request_options=request_options,
        )

    async def create_event_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateEbbComponent | CreateEbbComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateEventBasedComponentErrorBody]:
        """Creates an event-based component definition under the specified product family. An event-based component can
        then be added and “allocated” for a subscription.

        Event-based components are similar to other component types, in that you define the component parameters (such
        as name and taxability) and the pricing. A key difference for the event-based component is that it must be
        attached to a metric. This is because the metric provides the component with the actual quantity used in
        computing what and how much will be billed each period for each subscription.

        So, instead of reporting usage directly for each component (as you would with metered components), the usage is
        derived from analysis of your events.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/event_based_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateEbbComponent | CreateEbbComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=create_event_based_component_error_mapper,
            request_options=request_options,
        )

    async def create_metered_component(
        self,
        product_family_id: str,
        *,
        body: CreateMeteredComponent | CreateMeteredComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateMeteredComponentErrorBody]:
        """Creates a metered component definition under the specified product family. A metered component can then be
        added and “allocated” for a subscription.

        Metered components are used to bill for any type of unit that resets to 0 at the end of the billing period
        (think daily Google Ads clicks or monthly cell phone minutes). This is most commonly associated with usage-based
        billing and many other pricing schemes.

        Note that this is different from recurring quantity-based components, which DO NOT reset to zero at the start of
        every billing period. If you want to bill for a quantity of something that does not change unless you change it,
        then you want quantity components, instead.

        #### Hybrid Pricing A ``volume``, ``tiered``, or ``stairstep`` metered component can combine its primary pricing
        with a secondary pricing model (the ``overage_pricing`` parameter) so both bill as a single invoice line item
        instead of two. This does not apply to metered components configured for event-based billing (metric, meter, or
        formula). See `Hybrid Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and
        configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/metered_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMeteredComponent | CreateMeteredComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=create_metered_component_error_mapper,
            request_options=request_options,
        )

    async def create_on_off_component(
        self,
        product_family_id: str,
        *,
        body: CreateOnOffComponent | CreateOnOffComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateOnOffComponentErrorBody]:
        """Creates an On/Off component definition under the specified product family. An On/Off component can then be
        added and “allocated” for a subscription.

        On/off components are used for any flat fee, recurring add on (think $99/month for tech support or a flat add on
        shipping fee).

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/on_off_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOnOffComponent | CreateOnOffComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=create_on_off_component_error_mapper,
            request_options=request_options,
        )

    async def create_prepaid_usage_component(
        self,
        product_family_id: str,
        *,
        body: CreatePrepaidComponent | CreatePrepaidComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreatePrepaidUsageComponentErrorBody]:
        """Creates a prepaid usage component definition under the specified product family. A prepaid component can then
        be added and “allocated” for a subscription.

        Prepaid components allow customers to pre-purchase units that can be used up over time on their subscription. In
        a sense, they are the mirror image of metered components; while metered components charge at the end of the
        period for the amount of units used, prepaid components are charged for at the time of purchase, and usage is
        subsequently tracked against the amount purchased.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``; sending a blank value results in a validation error.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/product_families/{product_family_id}/prepaid_usage_components.json"),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePrepaidComponent | CreatePrepaidComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=create_prepaid_usage_component_error_mapper,
            request_options=request_options,
        )

    async def create_quantity_based_component(
        self,
        product_family_id: str,
        *,
        body: CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, CreateQuantityBasedComponentErrorBody]:
        """Creates a Quantity Based component definition under the specified product family. A Quantity Based component
        can then be added and “allocated” for a subscription.

        When defining a Quantity Based component, you can choose one of two types: #### Recurring Recurring
        quantity-based components are used to bill for the number of some unit (think monthly software user licenses or
        the number of pairs of socks in a box-a-month club). This is most commonly associated with billing for user
        licenses, number of users, number of employees, etc.

        #### One-time One-time quantity-based components are used to create ad hoc usage charges that do not recur. For
        example, at the time of signup, you might want to charge your customer a one-time fee for onboarding or other
        services.

        The allocated quantity for one-time quantity-based components immediately gets reset back to zero after the
        allocation is made.

        For more information, see `Components Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__. #### Hybrid Pricing A
        ``volume``, ``tiered``, or ``stairstep`` component can combine its primary pricing with a secondary pricing
        model (the ``overage_pricing`` parameter) so both bill as a single invoice line item instead of two. See `Hybrid
        Pricing <page:introduction/basic-concepts/hybrid-pricing>`__ for requirements and configuration details.

        For more information on components, see our documentation `here
        <https://maxio.zendesk.com/hc/en-us/articles/24261141522189-Components-Overview>`__.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: Either the product family's id or its handle prefixed with ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production(
                "/product_families/{product_family_id}/quantity_based_components.json"
            ),
            path_params=[param[str]("product_family_id", product_family_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateQuantityBasedComponent | CreateQuantityBasedComponentDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=create_quantity_based_component_error_mapper,
            request_options=request_options,
        )

    async def find_component(
        self, handle: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ComponentResponse, RawError]:
        """Returns information for a component matching the provided handle. You can identify your components with a
        handle so you don't have to save or reference the IDs we generate.

        Args:
            handle: The handle of the component to find
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components/lookup.json"),
            query_params=[param[str]("handle", handle)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_components(
        self,
        *,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ComponentResponse], RawError]:
        """Lists components for a site.

        Args:
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/components.json"),
            query_params=[
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
                param[bool | None]("include_archived", include_archived),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListComponentsFilter | ListComponentsFilterDict | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ComponentResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_components_for_product_family(
        self,
        product_family_id: int,
        *,
        include_archived: bool | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        filter_: ListComponentsFilter | ListComponentsFilterDict | None = None,
        date_field: BasicDateFieldOrStr | None = None,
        end_date: str | None = None,
        end_datetime: str | None = None,
        start_date: str | None = None,
        start_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[ComponentResponse], RawError]:
        """Lists components for a particular product family.

        Args:
            product_family_id: The Advanced Billing id of the product family
            include_archived: Include archived items.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            filter_: Filter to use for List Components operations
            date_field: The type of filter you would like to apply to your search. Use in query
                ``date_field=created_at``.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns components with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or before exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of end_date.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns components with
                a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns components with a timestamp at or after exact time provided in query. You can specify timezone
                in query - otherwise your site's time zone will be used. If provided, this parameter will be used
                instead of start_date.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/product_families/{product_family_id}/components.json"),
            path_params=[param[int]("product_family_id", product_family_id)],
            query_params=[
                param[bool | None]("include_archived", include_archived),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[ListComponentsFilter | ListComponentsFilterDict | None]("filter", filter_),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("end_date", end_date),
                param[str | None]("end_datetime", end_datetime),
                param[str | None]("start_date", start_date),
                param[str | None]("start_datetime", start_datetime),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[ComponentResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        include_features: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, RawError]:
        """Returns information regarding a component from a specific product family.

        You can read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            include_features: When ``true``, embeds the active feature catalog items for each result in a ``features``
                array. Default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production(
                "/product_families/{product_family_id}/components/{component_id}.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[str]("component_id", component_id)],
            query_params=[param[bool | None]("include_features", include_features)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_component(
        self,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, UpdateComponentErrorBody]:
        """Updates a component.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            component_id: The id or handle of the component
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/components/{component_id}.json"),
            path_params=[param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateComponentRequest | UpdateComponentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=update_component_error_mapper,
            request_options=request_options,
        )

    async def update_product_family_component(
        self,
        product_family_id: int,
        component_id: str,
        *,
        body: UpdateComponentRequest | UpdateComponentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ComponentResponse, UpdateProductFamilyComponentErrorBody]:
        """Updates a component from a specific product family.

        You may read the component by either the component's id or handle. When using the handle, it must be prefixed
        with ``handle:``.

        If you have the new `Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__ enabled, taxable
        components must include a non-blank ``tax_code``. Sending ``"tax_code": ""`` returns ``422``.

        Args:
            product_family_id: The Advanced Billing id of the product family to which the component belongs
            component_id: Either the Advanced Billing id of the component or the handle for the component prefixed with
                ``handle:``
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production(
                "/product_families/{product_family_id}/components/{component_id}.json"
            ),
            path_params=[param[int]("product_family_id", product_family_id), param[str]("component_id", component_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateComponentRequest | UpdateComponentRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ComponentResponse],
            error_mapper=update_product_family_component_error_mapper,
            request_options=request_options,
        )
