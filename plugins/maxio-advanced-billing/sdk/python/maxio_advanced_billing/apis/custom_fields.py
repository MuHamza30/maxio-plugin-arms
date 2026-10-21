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
from ..errors.create_metadata_error import CreateMetadataErrorBody, create_metadata_error_mapper
from ..errors.create_metafields_error import CreateMetafieldsErrorBody, create_metafields_error_mapper
from ..errors.delete_metadata_error import DeleteMetadataErrorBody, delete_metadata_error_mapper
from ..errors.delete_metafield_error import DeleteMetafieldErrorBody, delete_metafield_error_mapper
from ..errors.update_metadata_error import UpdateMetadataErrorBody, update_metadata_error_mapper
from ..errors.update_metafield_error import UpdateMetafieldErrorBody, update_metafield_error_mapper
from ..models.create_metadata_request import CreateMetadataRequest, CreateMetadataRequestDict
from ..models.create_metafields_request import CreateMetafieldsRequest, CreateMetafieldsRequestDict
from ..models.enums.basic_date_field import BasicDateFieldOrStr
from ..models.enums.resource_type import ResourceTypeOrStr
from ..models.enums.sorting_direction import SortingDirectionOrStr
from ..models.list_metafields_response import ListMetafieldsResponse
from ..models.metadata import Metadata
from ..models.metafield import Metafield
from ..models.paginated_metadata import PaginatedMetadata
from ..models.update_metadata_request import UpdateMetadataRequest, UpdateMetadataRequestDict
from ..models.update_metafields_request import UpdateMetafieldsRequest, UpdateMetafieldsRequestDict
from ..server.server import Server


class CustomFields:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomFieldsWithRawResponse(client, server, auth)

    def create_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: CreateMetadataRequest | CreateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metadata]:
        """Creates metadata and metafields for a specific subscription or customer, or updates metadata values of
        existing metafields for a subscription or customer. Metadata values are limited to 2 KB in size.

        If you create metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field. You can update the input_type
        for the metafield with the `Update Metafield <$e/Custom%20Fields/updateMetafield>`__ endpoint.

        >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_metadata(
                resource_type, resource_id, body=body, request_options=request_options
            ),
        )

    def create_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: CreateMetafieldsRequest | CreateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metafield]:
        """Creates metafields on a Site for either the Subscriptions or Customers resource.

        Metafields and their metadata are created in the Custom Fields configuration page on your Site. Metafields can
        be populated with metadata when you create them or later with the `Update Metafield
        <$e/Custom%20Fields/updateMetafield>`__, `Create Metadata <$e/Custom%20Fields/createMetadata>`__, or `Update
        Metadata <$e/Custom%20Fields/updateMetadata>`__ endpoints. The Create Metadata and Update Metadata endpoints
        allow you to add metafields and metadata values to a specific subscription or customer.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        > Note: After creating a metafield, the resource type cannot be modified.

        In the UI and product documentation, metafields and metadata are called Custom Fields.

        - Metafield is the custom field
        - Metadata is the data populating the custom field.

        See `Custom Fields Reference
        <https://docs.maxio.com/hc/en-us/articles/24266140850573-Custom-Fields-Reference>`__ and `Custom Fields Tab
        <https://maxio.zendesk.com/hc/en-us/articles/24251701302925-Subscription-Summary-Custom-Fields-Tab>`__ for
        information on using Custom Fields in the Advanced Billing UI.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_metafields(resource_type, body=body, request_options=request_options)
        )

    def delete_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        name: str | None = None,
        names: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes one or more metafields (and associated metadata) from the specified subscription or customer.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            name: Name of field to be removed.
            names: Names of fields to be removed. Use in query:
                ``names[]=field1&names[]=my-field&names[]=another-field``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_metadata(
                resource_type, resource_id, name=name, names=names, request_options=request_options
            ),
        )

    def delete_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes a metafield from your Site. Removes the metafield and associated metadata from all Subscriptions or
        Customers resources on the Site.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: The name of the metafield to be deleted
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_metafield(resource_type, name=name, request_options=request_options)
        )

    def list_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedMetadata:
        """Lists metadata and metafields for a specific customer or subscription.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
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
            self._with_raw_response.list_metadata(
                resource_type, resource_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    def list_metadata_for_resource_type(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        with_deleted: bool | None = None,
        resource_ids: list[int] | None = None,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedMetadata:
        """Lists metadata for a specified array of subscriptions or customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            with_deleted: Allow to fetch deleted metadata.
            resource_ids: Allow to fetch metadata for multiple records based on provided ids. Use in query:
                ``resource_ids[]=122&resource_ids[]=123&resource_ids[]=124``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_metadata_for_resource_type(
                resource_type,
                page=page,
                per_page=per_page,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                with_deleted=with_deleted,
                resource_ids=resource_ids,
                direction=direction,
                request_options=request_options,
            ),
        )

    def list_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMetafieldsResponse:
        """Lists the metafields and their associated details for a Site and resource type. You can filter the request to
        a specific metafield.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: Filter by the name of the metafield.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_metafields(
                resource_type,
                name=name,
                page=page,
                per_page=per_page,
                direction=direction,
                request_options=request_options,
            ),
        )

    def update_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: UpdateMetadataRequest | UpdateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metadata]:
        """Updates metadata and metafields on the Site and the customer or subscription specified, and updates the
        metadata value on a subscription or customer.

        If you update metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field to the Site and to the
        subscription or customer you specify. You can update the input_type for the metafield with the Update Metafield
        endpoint.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for the
        Subscription resource and another 100 for the Customer resource.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_metadata(
                resource_type, resource_id, body=body, request_options=request_options
            ),
        )

    def update_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: UpdateMetafieldsRequest | UpdateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metafield]:
        """Updates metafields on your Site for a resource type. Depending on the request structure, you can update or
        add metafields and metadata to the Subscriptions or Customers resource.

        With this endpoint, you can:

        - Add metafields. If the metafield specified in current_name does not exist, a new metafield is added.
          >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
            Subscriptions and another 100 for Customers.

        - Change the name of a metafield.
          >Note: To keep the metafield name the same and only update the metadata for the metafield, you must use the
            current metafield name in both the ``current_name`` and ``name`` parameters.

        - Change the input type for the metafield. For example, you can change a metafield input type from text to a
            dropdown. If you change the input type from text to a dropdown or radio, you must update the specific
            subscriptions or customers where the metafield was used to reflect the updated metafield and metadata.

        - Add metadata values to the existing metadata for a dropdown or radio metafield.
          >Note: Updates to metadata overwrite. To add one or more values, you must specify all metadata values
            including the new value you want to add.

        - Add new metadata to a dropdown or radio for a metafield that was created without metadata.

        - Remove metadata for a dropdown or radio for a metafield.
          >Note: Updates to metadata overwrite existing values. To remove one or more values, specify all metadata
            values except those you want to remove.

        - Add or update scope settings for a metafield.
          >Note: Scope changes overwrite existing settings. You must specify the complete scope, including the changes
            you want to make.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_metafield(resource_type, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> CustomFieldsWithRawResponse:
        return self._with_raw_response


class AsyncCustomFields:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomFieldsWithRawResponse(client, server, auth)

    async def create_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: CreateMetadataRequest | CreateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metadata]:
        """Creates metadata and metafields for a specific subscription or customer, or updates metadata values of
        existing metafields for a subscription or customer. Metadata values are limited to 2 KB in size.

        If you create metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field. You can update the input_type
        for the metafield with the `Update Metafield <$e/Custom%20Fields/updateMetafield>`__ endpoint.

        >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_metadata(
                resource_type, resource_id, body=body, request_options=request_options
            ),
        )

    async def create_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: CreateMetafieldsRequest | CreateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metafield]:
        """Creates metafields on a Site for either the Subscriptions or Customers resource.

        Metafields and their metadata are created in the Custom Fields configuration page on your Site. Metafields can
        be populated with metadata when you create them or later with the `Update Metafield
        <$e/Custom%20Fields/updateMetafield>`__, `Create Metadata <$e/Custom%20Fields/createMetadata>`__, or `Update
        Metadata <$e/Custom%20Fields/updateMetadata>`__ endpoints. The Create Metadata and Update Metadata endpoints
        allow you to add metafields and metadata values to a specific subscription or customer.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        > Note: After creating a metafield, the resource type cannot be modified.

        In the UI and product documentation, metafields and metadata are called Custom Fields.

        - Metafield is the custom field
        - Metadata is the data populating the custom field.

        See `Custom Fields Reference
        <https://docs.maxio.com/hc/en-us/articles/24266140850573-Custom-Fields-Reference>`__ and `Custom Fields Tab
        <https://maxio.zendesk.com/hc/en-us/articles/24251701302925-Subscription-Summary-Custom-Fields-Tab>`__ for
        information on using Custom Fields in the Advanced Billing UI.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_metafields(resource_type, body=body, request_options=request_options)
        )

    async def delete_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        name: str | None = None,
        names: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes one or more metafields (and associated metadata) from the specified subscription or customer.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            name: Name of field to be removed.
            names: Names of fields to be removed. Use in query:
                ``names[]=field1&names[]=my-field&names[]=another-field``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_metadata(
                resource_type, resource_id, name=name, names=names, request_options=request_options
            ),
        )

    async def delete_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes a metafield from your Site. Removes the metafield and associated metadata from all Subscriptions or
        Customers resources on the Site.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: The name of the metafield to be deleted
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_metafield(resource_type, name=name, request_options=request_options)
        )

    async def list_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedMetadata:
        """Lists metadata and metafields for a specific customer or subscription.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
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
            await self._with_raw_response.list_metadata(
                resource_type, resource_id, page=page, per_page=per_page, request_options=request_options
            ),
        )

    async def list_metadata_for_resource_type(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        with_deleted: bool | None = None,
        resource_ids: list[int] | None = None,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaginatedMetadata:
        """Lists metadata for a specified array of subscriptions or customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            with_deleted: Allow to fetch deleted metadata.
            resource_ids: Allow to fetch metadata for multiple records based on provided ids. Use in query:
                ``resource_ids[]=122&resource_ids[]=123&resource_ids[]=124``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_metadata_for_resource_type(
                resource_type,
                page=page,
                per_page=per_page,
                date_field=date_field,
                start_date=start_date,
                end_date=end_date,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                with_deleted=with_deleted,
                resource_ids=resource_ids,
                direction=direction,
                request_options=request_options,
            ),
        )

    async def list_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMetafieldsResponse:
        """Lists the metafields and their associated details for a Site and resource type. You can filter the request to
        a specific metafield.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: Filter by the name of the metafield.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_metafields(
                resource_type,
                name=name,
                page=page,
                per_page=per_page,
                direction=direction,
                request_options=request_options,
            ),
        )

    async def update_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: UpdateMetadataRequest | UpdateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metadata]:
        """Updates metadata and metafields on the Site and the customer or subscription specified, and updates the
        metadata value on a subscription or customer.

        If you update metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field to the Site and to the
        subscription or customer you specify. You can update the input_type for the metafield with the Update Metafield
        endpoint.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for the
        Subscription resource and another 100 for the Customer resource.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_metadata(
                resource_type, resource_id, body=body, request_options=request_options
            ),
        )

    async def update_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: UpdateMetafieldsRequest | UpdateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Metafield]:
        """Updates metafields on your Site for a resource type. Depending on the request structure, you can update or
        add metafields and metadata to the Subscriptions or Customers resource.

        With this endpoint, you can:

        - Add metafields. If the metafield specified in current_name does not exist, a new metafield is added.
          >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
            Subscriptions and another 100 for Customers.

        - Change the name of a metafield.
          >Note: To keep the metafield name the same and only update the metadata for the metafield, you must use the
            current metafield name in both the ``current_name`` and ``name`` parameters.

        - Change the input type for the metafield. For example, you can change a metafield input type from text to a
            dropdown. If you change the input type from text to a dropdown or radio, you must update the specific
            subscriptions or customers where the metafield was used to reflect the updated metafield and metadata.

        - Add metadata values to the existing metadata for a dropdown or radio metafield.
          >Note: Updates to metadata overwrite. To add one or more values, you must specify all metadata values
            including the new value you want to add.

        - Add new metadata to a dropdown or radio for a metafield that was created without metadata.

        - Remove metadata for a dropdown or radio for a metafield.
          >Note: Updates to metadata overwrite existing values. To remove one or more values, specify all metadata
            values except those you want to remove.

        - Add or update scope settings for a metafield.
          >Note: Scope changes overwrite existing settings. You must specify the complete scope, including the changes
            you want to make.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``SingleErrorResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_metafield(resource_type, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncCustomFieldsWithRawResponse:
        return self._with_raw_response


class CustomFieldsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: CreateMetadataRequest | CreateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metadata], CreateMetadataErrorBody]:
        """Creates metadata and metafields for a specific subscription or customer, or updates metadata values of
        existing metafields for a subscription or customer. Metadata values are limited to 2 KB in size.

        If you create metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field. You can update the input_type
        for the metafield with the `Update Metafield <$e/Custom%20Fields/updateMetafield>`__ endpoint.

        >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMetadataRequest | CreateMetadataRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[Metadata]],
            error_mapper=create_metadata_error_mapper,
            request_options=request_options,
        )

    def create_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: CreateMetafieldsRequest | CreateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metafield], CreateMetafieldsErrorBody]:
        """Creates metafields on a Site for either the Subscriptions or Customers resource.

        Metafields and their metadata are created in the Custom Fields configuration page on your Site. Metafields can
        be populated with metadata when you create them or later with the `Update Metafield
        <$e/Custom%20Fields/updateMetafield>`__, `Create Metadata <$e/Custom%20Fields/createMetadata>`__, or `Update
        Metadata <$e/Custom%20Fields/updateMetadata>`__ endpoints. The Create Metadata and Update Metadata endpoints
        allow you to add metafields and metadata values to a specific subscription or customer.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        > Note: After creating a metafield, the resource type cannot be modified.

        In the UI and product documentation, metafields and metadata are called Custom Fields.

        - Metafield is the custom field
        - Metadata is the data populating the custom field.

        See `Custom Fields Reference
        <https://docs.maxio.com/hc/en-us/articles/24266140850573-Custom-Fields-Reference>`__ and `Custom Fields Tab
        <https://maxio.zendesk.com/hc/en-us/articles/24251701302925-Subscription-Summary-Custom-Fields-Tab>`__ for
        information on using Custom Fields in the Advanced Billing UI.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMetafieldsRequest | CreateMetafieldsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[Metafield]],
            error_mapper=create_metafields_error_mapper,
            request_options=request_options,
        )

    def delete_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        name: str | None = None,
        names: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteMetadataErrorBody]:
        """Deletes one or more metafields (and associated metadata) from the specified subscription or customer.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            name: Name of field to be removed.
            names: Names of fields to be removed. Use in query:
                ``names[]=field1&names[]=my-field&names[]=another-field``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            query_params=[param[str | None]("name", name), param[list[str] | None]("names", names)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_metadata_error_mapper,
            request_options=request_options,
        )

    def delete_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteMetafieldErrorBody]:
        """Deletes a metafield from your Site. Removes the metafield and associated metadata from all Subscriptions or
        Customers resources on the Site.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: The name of the metafield to be deleted
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            query_params=[param[str | None]("name", name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=delete_metafield_error_mapper,
            request_options=request_options,
        )

    def list_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedMetadata, RawError]:
        """Lists metadata and metafields for a specific customer or subscription.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
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
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PaginatedMetadata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_metadata_for_resource_type(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        with_deleted: bool | None = None,
        resource_ids: list[int] | None = None,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedMetadata, RawError]:
        """Lists metadata for a specified array of subscriptions or customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            with_deleted: Allow to fetch deleted metadata.
            resource_ids: Allow to fetch metadata for multiple records based on provided ids. Use in query:
                ``resource_ids[]=122&resource_ids[]=123&resource_ids[]=124``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/{resource_type}/metadata.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[bool | None]("with_deleted", with_deleted),
                param[list[int] | None]("resource_ids", resource_ids),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[PaginatedMetadata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMetafieldsResponse, RawError]:
        """Lists the metafields and their associated details for a Site and resource type. You can filter the request to
        a specific metafield.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: Filter by the name of the metafield.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            query_params=[
                param[str | None]("name", name),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[ListMetafieldsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: UpdateMetadataRequest | UpdateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metadata], UpdateMetadataErrorBody]:
        """Updates metadata and metafields on the Site and the customer or subscription specified, and updates the
        metadata value on a subscription or customer.

        If you update metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field to the Site and to the
        subscription or customer you specify. You can update the input_type for the metafield with the Update Metafield
        endpoint.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for the
        Subscription resource and another 100 for the Customer resource.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMetadataRequest | UpdateMetadataRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[Metadata]],
            error_mapper=update_metadata_error_mapper,
            request_options=request_options,
        )

    def update_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: UpdateMetafieldsRequest | UpdateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metafield], UpdateMetafieldErrorBody]:
        """Updates metafields on your Site for a resource type. Depending on the request structure, you can update or
        add metafields and metadata to the Subscriptions or Customers resource.

        With this endpoint, you can:

        - Add metafields. If the metafield specified in current_name does not exist, a new metafield is added.
          >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
            Subscriptions and another 100 for Customers.

        - Change the name of a metafield.
          >Note: To keep the metafield name the same and only update the metadata for the metafield, you must use the
            current metafield name in both the ``current_name`` and ``name`` parameters.

        - Change the input type for the metafield. For example, you can change a metafield input type from text to a
            dropdown. If you change the input type from text to a dropdown or radio, you must update the specific
            subscriptions or customers where the metafield was used to reflect the updated metafield and metadata.

        - Add metadata values to the existing metadata for a dropdown or radio metafield.
          >Note: Updates to metadata overwrite. To add one or more values, you must specify all metadata values
            including the new value you want to add.

        - Add new metadata to a dropdown or radio for a metafield that was created without metadata.

        - Remove metadata for a dropdown or radio for a metafield.
          >Note: Updates to metadata overwrite existing values. To remove one or more values, specify all metadata
            values except those you want to remove.

        - Add or update scope settings for a metafield.
          >Note: Scope changes overwrite existing settings. You must specify the complete scope, including the changes
            you want to make.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMetafieldsRequest | UpdateMetafieldsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[Metafield]],
            error_mapper=update_metafield_error_mapper,
            request_options=request_options,
        )


class AsyncCustomFieldsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: CreateMetadataRequest | CreateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metadata], CreateMetadataErrorBody]:
        """Creates metadata and metafields for a specific subscription or customer, or updates metadata values of
        existing metafields for a subscription or customer. Metadata values are limited to 2 KB in size.

        If you create metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field. You can update the input_type
        for the metafield with the `Update Metafield <$e/Custom%20Fields/updateMetafield>`__ endpoint.

        >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMetadataRequest | CreateMetadataRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[Metadata]],
            error_mapper=create_metadata_error_mapper,
            request_options=request_options,
        )

    async def create_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: CreateMetafieldsRequest | CreateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metafield], CreateMetafieldsErrorBody]:
        """Creates metafields on a Site for either the Subscriptions or Customers resource.

        Metafields and their metadata are created in the Custom Fields configuration page on your Site. Metafields can
        be populated with metadata when you create them or later with the `Update Metafield
        <$e/Custom%20Fields/updateMetafield>`__, `Create Metadata <$e/Custom%20Fields/createMetadata>`__, or `Update
        Metadata <$e/Custom%20Fields/updateMetadata>`__ endpoints. The Create Metadata and Update Metadata endpoints
        allow you to add metafields and metadata values to a specific subscription or customer.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
        Subscriptions and another 100 for Customers.

        > Note: After creating a metafield, the resource type cannot be modified.

        In the UI and product documentation, metafields and metadata are called Custom Fields.

        - Metafield is the custom field
        - Metadata is the data populating the custom field.

        See `Custom Fields Reference
        <https://docs.maxio.com/hc/en-us/articles/24266140850573-Custom-Fields-Reference>`__ and `Custom Fields Tab
        <https://maxio.zendesk.com/hc/en-us/articles/24251701302925-Subscription-Summary-Custom-Fields-Tab>`__ for
        information on using Custom Fields in the Advanced Billing UI.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMetafieldsRequest | CreateMetafieldsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[Metafield]],
            error_mapper=create_metafields_error_mapper,
            request_options=request_options,
        )

    async def delete_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        name: str | None = None,
        names: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteMetadataErrorBody]:
        """Deletes one or more metafields (and associated metadata) from the specified subscription or customer.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            name: Name of field to be removed.
            names: Names of fields to be removed. Use in query:
                ``names[]=field1&names[]=my-field&names[]=another-field``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            query_params=[param[str | None]("name", name), param[list[str] | None]("names", names)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_metadata_error_mapper,
            request_options=request_options,
        )

    async def delete_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DeleteMetafieldErrorBody]:
        """Deletes a metafield from your Site. Removes the metafield and associated metadata from all Subscriptions or
        Customers resources on the Site.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: The name of the metafield to be deleted
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            query_params=[param[str | None]("name", name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=delete_metafield_error_mapper,
            request_options=request_options,
        )

    async def list_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedMetadata, RawError]:
        """Lists metadata and metafields for a specific customer or subscription.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
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
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            query_params=[param[int | None]("page", page), param[int | None]("per_page", per_page)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PaginatedMetadata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_metadata_for_resource_type(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        date_field: BasicDateFieldOrStr | None = None,
        start_date: Date | None = None,
        end_date: Date | None = None,
        start_datetime: RFC3339DateTime | None = None,
        end_datetime: RFC3339DateTime | None = None,
        with_deleted: bool | None = None,
        resource_ids: list[int] | None = None,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaginatedMetadata, RawError]:
        """Lists metadata for a specified array of subscriptions or customers.

        Args:
            resource_type: The resource type to which the metafields belong.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            date_field: The type of filter you would like to apply to your search.
            start_date: The start date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified.
            end_date: The end date (format YYYY-MM-DD) with which to filter the date_field. Returns metadata with a
                timestamp up to and including 11:59:59PM in your site’s time zone on the date specified.
            start_datetime: The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or after exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of start_date.
            end_datetime: The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns metadata with a timestamp at or before exact time provided in query. You can specify timezone in
                query - otherwise your site's time zone will be used. If provided, this parameter will be used instead
                of end_date.
            with_deleted: Allow to fetch deleted metadata.
            resource_ids: Allow to fetch metadata for multiple records based on provided ids. Use in query:
                ``resource_ids[]=122&resource_ids[]=123&resource_ids[]=124``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/{resource_type}/metadata.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[BasicDateFieldOrStr | None]("date_field", date_field),
                param[Date | None]("start_date", start_date),
                param[Date | None]("end_date", end_date),
                param[RFC3339DateTime | None]("start_datetime", start_datetime),
                param[RFC3339DateTime | None]("end_datetime", end_datetime),
                param[bool | None]("with_deleted", with_deleted),
                param[list[int] | None]("resource_ids", resource_ids),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[PaginatedMetadata],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_metafields(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        name: str | None = None,
        page: int | None = 1,
        per_page: int | None = 20,
        direction: SortingDirectionOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMetafieldsResponse, RawError]:
        """Lists the metafields and their associated details for a Site and resource type. You can filter the request to
        a specific metafield.

        Args:
            resource_type: The resource type to which the metafields belong.
            name: Filter by the name of the metafield.
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            direction: Controls the order in which results are returned. Use in query ``direction=asc``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            query_params=[
                param[str | None]("name", name),
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[SortingDirectionOrStr | None]("direction", direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[ListMetafieldsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_metadata(
        self,
        resource_type: ResourceTypeOrStr,
        resource_id: int,
        *,
        body: UpdateMetadataRequest | UpdateMetadataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metadata], UpdateMetadataErrorBody]:
        """Updates metadata and metafields on the Site and the customer or subscription specified, and updates the
        metadata value on a subscription or customer.

        If you update metadata on a subscription or customer with a metafield that does not already exist, the metafield
        is created with the metadata you specify and it is always added as a text field to the Site and to the
        subscription or customer you specify. You can update the input_type for the metafield with the Update Metafield
        endpoint.

        Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for the
        Subscription resource and another 100 for the Customer resource.

        Args:
            resource_type: The resource type to which the metafields belong.
            resource_id: The Advanced Billing id of the customer or the subscription for which the metadata applies
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/{resource_type}/{resource_id}/metadata.json"),
            path_params=[
                param[ResourceTypeOrStr]("resource_type", resource_type), param[int]("resource_id", resource_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMetadataRequest | UpdateMetadataRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[Metadata]],
            error_mapper=update_metadata_error_mapper,
            request_options=request_options,
        )

    async def update_metafield(
        self,
        resource_type: ResourceTypeOrStr,
        *,
        body: UpdateMetafieldsRequest | UpdateMetafieldsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Metafield], UpdateMetafieldErrorBody]:
        """Updates metafields on your Site for a resource type. Depending on the request structure, you can update or
        add metafields and metadata to the Subscriptions or Customers resource.

        With this endpoint, you can:

        - Add metafields. If the metafield specified in current_name does not exist, a new metafield is added.
          >Note: Each site is limited to 100 unique metafields per resource. This means you can have 100 metafields for
            Subscriptions and another 100 for Customers.

        - Change the name of a metafield.
          >Note: To keep the metafield name the same and only update the metadata for the metafield, you must use the
            current metafield name in both the ``current_name`` and ``name`` parameters.

        - Change the input type for the metafield. For example, you can change a metafield input type from text to a
            dropdown. If you change the input type from text to a dropdown or radio, you must update the specific
            subscriptions or customers where the metafield was used to reflect the updated metafield and metadata.

        - Add metadata values to the existing metadata for a dropdown or radio metafield.
          >Note: Updates to metadata overwrite. To add one or more values, you must specify all metadata values
            including the new value you want to add.

        - Add new metadata to a dropdown or radio for a metafield that was created without metadata.

        - Remove metadata for a dropdown or radio for a metafield.
          >Note: Updates to metadata overwrite existing values. To remove one or more values, specify all metadata
            values except those you want to remove.

        - Add or update scope settings for a metafield.
          >Note: Scope changes overwrite existing settings. You must specify the complete scope, including the changes
            you want to make.

        Args:
            resource_type: The resource type to which the metafields belong.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/{resource_type}/metafields.json"),
            path_params=[param[ResourceTypeOrStr]("resource_type", resource_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMetafieldsRequest | UpdateMetafieldsRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[list[Metafield]],
            error_mapper=update_metafield_error_mapper,
            request_options=request_options,
        )
