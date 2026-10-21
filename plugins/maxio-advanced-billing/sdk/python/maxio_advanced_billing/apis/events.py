from __future__ import annotations

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
from ..models.count_response import CountResponse
from ..models.enums.direction import Direction, DirectionOrStr
from ..models.enums.event_key import EventKeyOrStr
from ..models.enums.list_events_date_field import ListEventsDateFieldOrStr
from ..models.event_response import EventResponse
from ..server.server import Server


class Events:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EventsWithRawResponse(client, server, auth)

    def list_events(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        date_field: ListEventsDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[EventResponse]:
        """Lists events for a site.

        Events include various activity that happens around a Site. This information is **especially** useful to track
        down issues that arise when subscriptions are not created due to errors.

        Within the UI, Events are referred to as Site Activity. For more information, see `Site Activity
        <https://maxio.zendesk.com/hc/en-us/articles/24250671733517-Site-Activity>`__.

        Use query string filters to narrow down results. You can use the ``filter`` parameter to filter by event key.

        ### Legacy Filters

        The following keys are no longer supported.

        + ``payment_failure_recreated``
        + ``payment_success_recreated``
        + ``renewal_failure_recreated``
        + ``renewal_success_recreated``
        + ``zferral_revenue_post_failure`` - (Specific to the deprecated Zferral integration)
        + ``zferral_revenue_post_success`` - (Specific to the deprecated Zferral integration)

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ### Example Here’s an example event for the ``subscription_product_change`` event:

        ```
        {
            "event": {
                "id": 351,
                "key": "subscription_product_change",
                "message": "Product changed on Mark Alan's subscription from 'Basic' to 'Pro'",
                "subscription_id": 205,
                "event_specific_data": {
                    "new_product_id": 3,
                    "previous_product_id": 2
                },
                "created_at": "2012-01-30T10:43:31-05:00"
            }
        }
        ```

        Here’s an example event for the ``subscription_state_change`` event:

        ```
         {
             "event": {
                 "id": 353,
                 "key": "subscription_state_change",
                 "message": "State changed on Mark Alan's subscription to Pro from trialing to active",
                 "subscription_id": 205,
                 "event_specific_data": {
                     "new_subscription_state": "active",
                     "previous_subscription_state": "trialing"
                 },
                 "created_at": "2012-01-30T10:43:33-05:00"
             }
         }
        ```

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Plan changed on Subscription from previous plan to new plan”
        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_events(
                page=page,
                per_page=per_page,
                since_id=since_id,
                max_id=max_id,
                direction=direction,
                filter_=filter_,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                request_options=request_options,
            ),
        )

    def list_subscription_events(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[EventResponse]:
        """Lists events for a subscription.

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            subscription_id: The Chargify id of the subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_subscription_events(
                subscription_id,
                page=page,
                per_page=per_page,
                since_id=since_id,
                max_id=max_id,
                direction=direction,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    def read_events_count(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CountResponse:
        """Returns the total count of events for a given site.

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.read_events_count(
                page=page,
                per_page=per_page,
                since_id=since_id,
                max_id=max_id,
                direction=direction,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> EventsWithRawResponse:
        return self._with_raw_response


class AsyncEvents:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEventsWithRawResponse(client, server, auth)

    async def list_events(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        date_field: ListEventsDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[EventResponse]:
        """Lists events for a site.

        Events include various activity that happens around a Site. This information is **especially** useful to track
        down issues that arise when subscriptions are not created due to errors.

        Within the UI, Events are referred to as Site Activity. For more information, see `Site Activity
        <https://maxio.zendesk.com/hc/en-us/articles/24250671733517-Site-Activity>`__.

        Use query string filters to narrow down results. You can use the ``filter`` parameter to filter by event key.

        ### Legacy Filters

        The following keys are no longer supported.

        + ``payment_failure_recreated``
        + ``payment_success_recreated``
        + ``renewal_failure_recreated``
        + ``renewal_success_recreated``
        + ``zferral_revenue_post_failure`` - (Specific to the deprecated Zferral integration)
        + ``zferral_revenue_post_success`` - (Specific to the deprecated Zferral integration)

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ### Example Here’s an example event for the ``subscription_product_change`` event:

        ```
        {
            "event": {
                "id": 351,
                "key": "subscription_product_change",
                "message": "Product changed on Mark Alan's subscription from 'Basic' to 'Pro'",
                "subscription_id": 205,
                "event_specific_data": {
                    "new_product_id": 3,
                    "previous_product_id": 2
                },
                "created_at": "2012-01-30T10:43:31-05:00"
            }
        }
        ```

        Here’s an example event for the ``subscription_state_change`` event:

        ```
         {
             "event": {
                 "id": 353,
                 "key": "subscription_state_change",
                 "message": "State changed on Mark Alan's subscription to Pro from trialing to active",
                 "subscription_id": 205,
                 "event_specific_data": {
                     "new_subscription_state": "active",
                     "previous_subscription_state": "trialing"
                 },
                 "created_at": "2012-01-30T10:43:33-05:00"
             }
         }
        ```

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Plan changed on Subscription from previous plan to new plan”
        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_events(
                page=page,
                per_page=per_page,
                since_id=since_id,
                max_id=max_id,
                direction=direction,
                filter_=filter_,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                request_options=request_options,
            ),
        )

    async def list_subscription_events(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[EventResponse]:
        """Lists events for a subscription.

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            subscription_id: The Chargify id of the subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_subscription_events(
                subscription_id,
                page=page,
                per_page=per_page,
                since_id=since_id,
                max_id=max_id,
                direction=direction,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    async def read_events_count(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CountResponse:
        """Returns the total count of events for a given site.

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.read_events_count(
                page=page,
                per_page=per_page,
                since_id=since_id,
                max_id=max_id,
                direction=direction,
                filter_=filter_,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncEventsWithRawResponse:
        return self._with_raw_response


class EventsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_events(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        date_field: ListEventsDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[EventResponse], RawError]:
        """Lists events for a site.

        Events include various activity that happens around a Site. This information is **especially** useful to track
        down issues that arise when subscriptions are not created due to errors.

        Within the UI, Events are referred to as Site Activity. For more information, see `Site Activity
        <https://maxio.zendesk.com/hc/en-us/articles/24250671733517-Site-Activity>`__.

        Use query string filters to narrow down results. You can use the ``filter`` parameter to filter by event key.

        ### Legacy Filters

        The following keys are no longer supported.

        + ``payment_failure_recreated``
        + ``payment_success_recreated``
        + ``renewal_failure_recreated``
        + ``renewal_success_recreated``
        + ``zferral_revenue_post_failure`` - (Specific to the deprecated Zferral integration)
        + ``zferral_revenue_post_success`` - (Specific to the deprecated Zferral integration)

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ### Example Here’s an example event for the ``subscription_product_change`` event:

        ```
        {
            "event": {
                "id": 351,
                "key": "subscription_product_change",
                "message": "Product changed on Mark Alan's subscription from 'Basic' to 'Pro'",
                "subscription_id": 205,
                "event_specific_data": {
                    "new_product_id": 3,
                    "previous_product_id": 2
                },
                "created_at": "2012-01-30T10:43:31-05:00"
            }
        }
        ```

        Here’s an example event for the ``subscription_state_change`` event:

        ```
         {
             "event": {
                 "id": 353,
                 "key": "subscription_state_change",
                 "message": "State changed on Mark Alan's subscription to Pro from trialing to active",
                 "subscription_id": 205,
                 "event_specific_data": {
                     "new_subscription_state": "active",
                     "previous_subscription_state": "trialing"
                 },
                 "created_at": "2012-01-30T10:43:33-05:00"
             }
         }
        ```

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Plan changed on Subscription from previous plan to new plan”
        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/events.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[DirectionOrStr | None]("direction", direction),
                param[list[EventKeyOrStr] | None]("filter", filter_),
                param[ListEventsDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[EventResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_subscription_events(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[EventResponse], RawError]:
        """Lists events for a subscription.

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            subscription_id: The Chargify id of the subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/events.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[DirectionOrStr | None]("direction", direction),
                param[list[EventKeyOrStr] | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[EventResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def read_events_count(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CountResponse, RawError]:
        """Returns the total count of events for a given site.

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/events/count.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[DirectionOrStr | None]("direction", direction),
                param[list[EventKeyOrStr] | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[CountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEventsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_events(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        date_field: ListEventsDateFieldOrStr | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        start_datetime: str | None = None,
        end_datetime: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[EventResponse], RawError]:
        """Lists events for a site.

        Events include various activity that happens around a Site. This information is **especially** useful to track
        down issues that arise when subscriptions are not created due to errors.

        Within the UI, Events are referred to as Site Activity. For more information, see `Site Activity
        <https://maxio.zendesk.com/hc/en-us/articles/24250671733517-Site-Activity>`__.

        Use query string filters to narrow down results. You can use the ``filter`` parameter to filter by event key.

        ### Legacy Filters

        The following keys are no longer supported.

        + ``payment_failure_recreated``
        + ``payment_success_recreated``
        + ``renewal_failure_recreated``
        + ``renewal_success_recreated``
        + ``zferral_revenue_post_failure`` - (Specific to the deprecated Zferral integration)
        + ``zferral_revenue_post_success`` - (Specific to the deprecated Zferral integration)

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ### Example Here’s an example event for the ``subscription_product_change`` event:

        ```
        {
            "event": {
                "id": 351,
                "key": "subscription_product_change",
                "message": "Product changed on Mark Alan's subscription from 'Basic' to 'Pro'",
                "subscription_id": 205,
                "event_specific_data": {
                    "new_product_id": 3,
                    "previous_product_id": 2
                },
                "created_at": "2012-01-30T10:43:31-05:00"
            }
        }
        ```

        Here’s an example event for the ``subscription_state_change`` event:

        ```
         {
             "event": {
                 "id": 353,
                 "key": "subscription_state_change",
                 "message": "State changed on Mark Alan's subscription to Pro from trialing to active",
                 "subscription_id": 205,
                 "event_specific_data": {
                     "new_subscription_state": "active",
                     "previous_subscription_state": "trialing"
                 },
                 "created_at": "2012-01-30T10:43:33-05:00"
             }
         }
        ```

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Plan changed on Subscription from previous plan to new plan”
        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/events.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[DirectionOrStr | None]("direction", direction),
                param[list[EventKeyOrStr] | None]("filter", filter_),
                param[ListEventsDateFieldOrStr | None]("date_field", date_field),
                param[str | None]("start_date", start_date),
                param[str | None]("end_date", end_date),
                param[str | None]("start_datetime", start_datetime),
                param[str | None]("end_datetime", end_datetime),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[EventResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_subscription_events(
        self,
        subscription_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[EventResponse], RawError]:
        """Lists events for a subscription.

        ## Event Key The event type is identified by the key property. See `Event Key <$m/Event%20Key>`__ for a complete
        list of supported keys.

        ## Event Specific Data

        Different event types may include additional data in ``event_specific_data`` property. While some events share
        the same schema for ``event_specific_data``, others may not include it at all. For precise mappings from key to
        event_specific_data, refer to `Event <$m/Event>`__.

        ## Enhanced Catalog Experience

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            subscription_id: The Chargify id of the subscription.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/subscriptions/{subscription_id}/events.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[DirectionOrStr | None]("direction", direction),
                param[list[EventKeyOrStr] | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[EventResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def read_events_count(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        since_id: int | None = None,
        max_id: int | None = None,
        direction: DirectionOrStr | None = Direction.DESC,
        filter_: list[EventKeyOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CountResponse, RawError]:
        """Returns the total count of events for a given site.

        If you’re using the `enhanced Catalog experience
        <page:help/announcements/2026-announcements#new-catalog-experience-and-terminology>`__, you’ll see updated
        naming in webhook events and messages.

        Event name changes:

        - subscription_product_change → subscription_plan_change
        - component_allocation_change → allocation_change
        - component_billing_date_change → product_billing_date_change

        Message updates:

        - “Successful payment for allocation changes to Product on Subscription”
        - “Failed payment for allocation changes to Product on Subscription”
        - “Plan changed on Subscription from previous plan to new plan”

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            since_id: Returns events with an id greater than or equal to the one specified.
            max_id: Returns events with an id less than or equal to the one specified.
            direction: The sort direction of the returned events.
            filter_: You can pass multiple event keys after comma. Use in query
                ``filter=signup_success,payment_success``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/events/count.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[int | None]("since_id", since_id),
                param[int | None]("max_id", max_id),
                param[DirectionOrStr | None]("direction", direction),
                param[list[EventKeyOrStr] | None]("filter", filter_),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[CountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
