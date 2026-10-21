from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.archive_feature_template_error import (
    ArchiveFeatureTemplateErrorBody,
    archive_feature_template_error_mapper,
)
from ..errors.create_feature_template_error import CreateFeatureTemplateErrorBody, create_feature_template_error_mapper
from ..errors.list_feature_templates_error import ListFeatureTemplatesErrorBody, list_feature_templates_error_mapper
from ..errors.read_feature_template_error import ReadFeatureTemplateErrorBody, read_feature_template_error_mapper
from ..errors.restore_feature_template_error import (
    RestoreFeatureTemplateErrorBody,
    restore_feature_template_error_mapper,
)
from ..errors.update_feature_template_error import UpdateFeatureTemplateErrorBody, update_feature_template_error_mapper
from ..models.create_feature_template_request import CreateFeatureTemplateRequest, CreateFeatureTemplateRequestDict
from ..models.enums.kind import KindOrStr
from ..models.enums.sort_by import SortBy, SortByOrStr
from ..models.enums.sort_direction import SortDirection, SortDirectionOrStr
from ..models.enums.status1 import Status1, Status1OrStr
from ..models.feature_template_response import FeatureTemplateResponse
from ..models.feature_templates_list_response import FeatureTemplatesListResponse
from ..models.update_feature_template_request import UpdateFeatureTemplateRequest, UpdateFeatureTemplateRequestDict
from ..server.server import Server


class FeatureTemplates:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FeatureTemplatesWithRawResponse(client, server, auth)

    def archive_feature_template(
        self, id_: int, *, remove_from_catalog: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Archives a feature template. Archived feature templates are not addressable via `Read Feature Template
        <$e/Feature%20Templates/readFeatureTemplate>`__ or `Update Feature Template
        <$e/Feature%20Templates/updateFeatureTemplate>`__. Both endpoints return ``404`` until the template is restored.

        The feature template record itself is never hard-deleted, and can always be restored with `Restore Feature
        Template <$e/Feature%20Templates/restoreFeatureTemplate>`__. Reversibility does not extend to
        ``remove_from_catalog=true``: the feature catalog items and entitlements that parameter destroys are gone
        permanently, and restoring the template will not bring subscriber access back.

        Args:
            id_: The Advanced Billing id of the feature template.
            remove_from_catalog: When ``true``, also destroys every feature catalog item created from this template and
                cascades to their entitlements, revoking subscriber access immediately. When ``false`` (default), the
                feature template and its feature catalog items are archived, and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.archive_feature_template(
                id_, remove_from_catalog=remove_from_catalog, request_options=request_options
            ),
        )

    def create_feature_template(
        self,
        *,
        body: CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureTemplateResponse:
        """Defines a new feature at the site level. Feature templates aren't billable on their own. Attach a template to
        products or components to grant the feature to subscribers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Forbidden Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.create_feature_template(body=body, request_options=request_options))

    def list_feature_templates(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        status: Status1OrStr | None = Status1.ACTIVE,
        q: str | None = None,
        kind: KindOrStr | None = None,
        updated_from: Date | None = None,
        updated_to: Date | None = None,
        sort_by: SortByOrStr | None = SortBy.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureTemplatesListResponse:
        """Lists the feature templates defined for your site, active (non-archived) ones by default. Pass
        ``status=archived`` or ``status=all`` to widen the result set.

        Supply ``page`` or ``per_page`` to paginate. Without either parameter, the response includes the full result
        set.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            status: Filters by archived state. Defaults to ``active`` (non-archived templates only).
            q: Filters to feature templates whose name contains this substring (case-insensitive).
            kind: Filters by feature kind.
            updated_from: Returns feature templates updated on or after this date.
            updated_to: Returns feature templates updated on or before this date.
            sort_by: The field to sort results by.
            sort_direction: The sort direction of the returned feature templates.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_feature_templates(
                page=page,
                per_page=per_page,
                status=status,
                q=q,
                kind=kind,
                updated_from=updated_from,
                updated_to=updated_to,
                sort_by=sort_by,
                sort_direction=sort_direction,
                request_options=request_options,
            ),
        )

    def read_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureTemplateResponse:
        """Returns a single feature template. Archived feature templates are not addressable here and return ``404``.
        Restore a template first to read or update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.read_feature_template(id_, request_options=request_options))

    def restore_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureTemplateResponse:
        """Clears the feature template's archived state. Feature catalog items created from this template are not
        automatically restored. Restore each one individually.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.restore_feature_template(id_, request_options=request_options))

    def update_feature_template(
        self,
        id_: int,
        *,
        body: UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureTemplateResponse:
        """Updates the name, description, unit, value type, default value, or default periodicity of a feature template.
        ``key`` is rejected on every update. ``kind`` is rejected once any feature catalog item has been created from
        this template.

        Archived feature templates are not addressable here and return ``404``. Restore a template first to update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(self._with_raw_response.update_feature_template(id_, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> FeatureTemplatesWithRawResponse:
        return self._with_raw_response


class AsyncFeatureTemplates:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFeatureTemplatesWithRawResponse(client, server, auth)

    async def archive_feature_template(
        self, id_: int, *, remove_from_catalog: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Archives a feature template. Archived feature templates are not addressable via `Read Feature Template
        <$e/Feature%20Templates/readFeatureTemplate>`__ or `Update Feature Template
        <$e/Feature%20Templates/updateFeatureTemplate>`__. Both endpoints return ``404`` until the template is restored.

        The feature template record itself is never hard-deleted, and can always be restored with `Restore Feature
        Template <$e/Feature%20Templates/restoreFeatureTemplate>`__. Reversibility does not extend to
        ``remove_from_catalog=true``: the feature catalog items and entitlements that parameter destroys are gone
        permanently, and restoring the template will not bring subscriber access back.

        Args:
            id_: The Advanced Billing id of the feature template.
            remove_from_catalog: When ``true``, also destroys every feature catalog item created from this template and
                cascades to their entitlements, revoking subscriber access immediately. When ``false`` (default), the
                feature template and its feature catalog items are archived, and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.archive_feature_template(
                id_, remove_from_catalog=remove_from_catalog, request_options=request_options
            ),
        )

    async def create_feature_template(
        self,
        *,
        body: CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureTemplateResponse:
        """Defines a new feature at the site level. Feature templates aren't billable on their own. Attach a template to
        products or components to grant the feature to subscribers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created

        Raises:
            ApiError: Forbidden Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.create_feature_template(body=body, request_options=request_options))

    async def list_feature_templates(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        status: Status1OrStr | None = Status1.ACTIVE,
        q: str | None = None,
        kind: KindOrStr | None = None,
        updated_from: Date | None = None,
        updated_to: Date | None = None,
        sort_by: SortByOrStr | None = SortBy.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureTemplatesListResponse:
        """Lists the feature templates defined for your site, active (non-archived) ones by default. Pass
        ``status=archived`` or ``status=all`` to widen the result set.

        Supply ``page`` or ``per_page`` to paginate. Without either parameter, the response includes the full result
        set.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            status: Filters by archived state. Defaults to ``active`` (non-archived templates only).
            q: Filters to feature templates whose name contains this substring (case-insensitive).
            kind: Filters by feature kind.
            updated_from: Returns feature templates updated on or after this date.
            updated_to: Returns feature templates updated on or before this date.
            sort_by: The field to sort results by.
            sort_direction: The sort direction of the returned feature templates.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_feature_templates(
                page=page,
                per_page=per_page,
                status=status,
                q=q,
                kind=kind,
                updated_from=updated_from,
                updated_to=updated_to,
                sort_by=sort_by,
                sort_direction=sort_direction,
                request_options=request_options,
            ),
        )

    async def read_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureTemplateResponse:
        """Returns a single feature template. Archived feature templates are not addressable here and return ``404``.
        Restore a template first to read or update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.read_feature_template(id_, request_options=request_options))

    async def restore_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> FeatureTemplateResponse:
        """Clears the feature template's archived state. Feature catalog items created from this template are not
        automatically restored. Restore each one individually.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(await self._with_raw_response.restore_feature_template(id_, request_options=request_options))

    async def update_feature_template(
        self,
        id_: int,
        *,
        body: UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeatureTemplateResponse:
        """Updates the name, description, unit, value type, default value, or default periodicity of a feature template.
        ``key`` is rejected on every update. ``kind`` is rejected once any feature catalog item has been created from
        this template.

        Archived feature templates are not addressable here and return ``404``. Restore a template first to update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Forbidden Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_feature_template(id_, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncFeatureTemplatesWithRawResponse:
        return self._with_raw_response


class FeatureTemplatesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_feature_template(
        self, id_: int, *, remove_from_catalog: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ArchiveFeatureTemplateErrorBody]:
        """Archives a feature template. Archived feature templates are not addressable via `Read Feature Template
        <$e/Feature%20Templates/readFeatureTemplate>`__ or `Update Feature Template
        <$e/Feature%20Templates/updateFeatureTemplate>`__. Both endpoints return ``404`` until the template is restored.

        The feature template record itself is never hard-deleted, and can always be restored with `Restore Feature
        Template <$e/Feature%20Templates/restoreFeatureTemplate>`__. Reversibility does not extend to
        ``remove_from_catalog=true``: the feature catalog items and entitlements that parameter destroys are gone
        permanently, and restoring the template will not bring subscriber access back.

        Args:
            id_: The Advanced Billing id of the feature template.
            remove_from_catalog: When ``true``, also destroys every feature catalog item created from this template and
                cascades to their entitlements, revoking subscriber access immediately. When ``false`` (default), the
                feature template and its feature catalog items are archived, and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/features/{id}.json"),
            path_params=[param[int]("id", id_)],
            query_params=[param[bool | None]("remove_from_catalog", remove_from_catalog)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=archive_feature_template_error_mapper,
            request_options=request_options,
        )

    def create_feature_template(
        self,
        *,
        body: CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureTemplateResponse, CreateFeatureTemplateErrorBody]:
        """Defines a new feature at the site level. Feature templates aren't billable on their own. Attach a template to
        products or components to grant the feature to subscribers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/features.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureTemplateResponse],
            error_mapper=create_feature_template_error_mapper,
            request_options=request_options,
        )

    def list_feature_templates(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        status: Status1OrStr | None = Status1.ACTIVE,
        q: str | None = None,
        kind: KindOrStr | None = None,
        updated_from: Date | None = None,
        updated_to: Date | None = None,
        sort_by: SortByOrStr | None = SortBy.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureTemplatesListResponse, ListFeatureTemplatesErrorBody]:
        """Lists the feature templates defined for your site, active (non-archived) ones by default. Pass
        ``status=archived`` or ``status=all`` to widen the result set.

        Supply ``page`` or ``per_page`` to paginate. Without either parameter, the response includes the full result
        set.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            status: Filters by archived state. Defaults to ``active`` (non-archived templates only).
            q: Filters to feature templates whose name contains this substring (case-insensitive).
            kind: Filters by feature kind.
            updated_from: Returns feature templates updated on or after this date.
            updated_to: Returns feature templates updated on or before this date.
            sort_by: The field to sort results by.
            sort_direction: The sort direction of the returned feature templates.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/features.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Status1OrStr | None]("status", status),
                param[str | None]("q", q),
                param[KindOrStr | None]("kind", kind),
                param[Date | None]("updated_from", updated_from),
                param[Date | None]("updated_to", updated_to),
                param[SortByOrStr | None]("sort_by", sort_by),
                param[SortDirectionOrStr | None]("sort_direction", sort_direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureTemplatesListResponse],
            error_mapper=list_feature_templates_error_mapper,
            request_options=request_options,
        )

    def read_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureTemplateResponse, ReadFeatureTemplateErrorBody]:
        """Returns a single feature template. Archived feature templates are not addressable here and return ``404``.
        Restore a template first to read or update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.production("/features/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureTemplateResponse],
            error_mapper=read_feature_template_error_mapper,
            request_options=request_options,
        )

    def restore_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureTemplateResponse, RestoreFeatureTemplateErrorBody]:
        """Clears the feature template's archived state. Feature catalog items created from this template are not
        automatically restored. Restore each one individually.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/features/{id}/restore.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureTemplateResponse],
            error_mapper=restore_feature_template_error_mapper,
            request_options=request_options,
        )

    def update_feature_template(
        self,
        id_: int,
        *,
        body: UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureTemplateResponse, UpdateFeatureTemplateErrorBody]:
        """Updates the name, description, unit, value type, default value, or default periodicity of a feature template.
        ``key`` is rejected on every update. ``kind`` is rejected once any feature catalog item has been created from
        this template.

        Archived feature templates are not addressable here and return ``404``. Restore a template first to update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/features/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[FeatureTemplateResponse],
            error_mapper=update_feature_template_error_mapper,
            request_options=request_options,
        )


class AsyncFeatureTemplatesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_feature_template(
        self, id_: int, *, remove_from_catalog: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, ArchiveFeatureTemplateErrorBody]:
        """Archives a feature template. Archived feature templates are not addressable via `Read Feature Template
        <$e/Feature%20Templates/readFeatureTemplate>`__ or `Update Feature Template
        <$e/Feature%20Templates/updateFeatureTemplate>`__. Both endpoints return ``404`` until the template is restored.

        The feature template record itself is never hard-deleted, and can always be restored with `Restore Feature
        Template <$e/Feature%20Templates/restoreFeatureTemplate>`__. Reversibility does not extend to
        ``remove_from_catalog=true``: the feature catalog items and entitlements that parameter destroys are gone
        permanently, and restoring the template will not bring subscriber access back.

        Args:
            id_: The Advanced Billing id of the feature template.
            remove_from_catalog: When ``true``, also destroys every feature catalog item created from this template and
                cascades to their entitlements, revoking subscriber access immediately. When ``false`` (default), the
                feature template and its feature catalog items are archived, and existing entitlements are preserved.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/features/{id}.json"),
            path_params=[param[int]("id", id_)],
            query_params=[param[bool | None]("remove_from_catalog", remove_from_catalog)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_empty_response,
            error_mapper=archive_feature_template_error_mapper,
            request_options=request_options,
        )

    async def create_feature_template(
        self,
        *,
        body: CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureTemplateResponse, CreateFeatureTemplateErrorBody]:
        """Defines a new feature at the site level. Feature templates aren't billable on their own. Attach a template to
        products or components to grant the feature to subscribers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/features.json"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFeatureTemplateRequest | CreateFeatureTemplateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureTemplateResponse],
            error_mapper=create_feature_template_error_mapper,
            request_options=request_options,
        )

    async def list_feature_templates(
        self,
        *,
        page: int | None = 1,
        per_page: int | None = 20,
        status: Status1OrStr | None = Status1.ACTIVE,
        q: str | None = None,
        kind: KindOrStr | None = None,
        updated_from: Date | None = None,
        updated_to: Date | None = None,
        sort_by: SortByOrStr | None = SortBy.NAME,
        sort_direction: SortDirectionOrStr | None = SortDirection.ASC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureTemplatesListResponse, ListFeatureTemplatesErrorBody]:
        """Lists the feature templates defined for your site, active (non-archived) ones by default. Pass
        ``status=archived`` or ``status=all`` to widen the result set.

        Supply ``page`` or ``per_page`` to paginate. Without either parameter, the response includes the full result
        set.

        Args:
            page: Result records are organized in pages. By default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can start navigating through the pages to
                consume the results. You do this by passing in a page parameter. Retrieve the next page by adding
                ?page=2 to the query string. If there are no results to return, then an empty result set will be
                returned. Use in query ``page=1``.
            per_page: This parameter indicates how many records to fetch in each request. Default value is 20. The
                maximum allowed values is 200; any per_page value over 200 will be changed to 200. Use in query
                ``per_page=200``.
            status: Filters by archived state. Defaults to ``active`` (non-archived templates only).
            q: Filters to feature templates whose name contains this substring (case-insensitive).
            kind: Filters by feature kind.
            updated_from: Returns feature templates updated on or after this date.
            updated_to: Returns feature templates updated on or before this date.
            sort_by: The field to sort results by.
            sort_direction: The sort direction of the returned feature templates.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/features.json"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("per_page", per_page),
                param[Status1OrStr | None]("status", status),
                param[str | None]("q", q),
                param[KindOrStr | None]("kind", kind),
                param[Date | None]("updated_from", updated_from),
                param[Date | None]("updated_to", updated_to),
                param[SortByOrStr | None]("sort_by", sort_by),
                param[SortDirectionOrStr | None]("sort_direction", sort_direction),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureTemplatesListResponse],
            error_mapper=list_feature_templates_error_mapper,
            request_options=request_options,
        )

    async def read_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureTemplateResponse, ReadFeatureTemplateErrorBody]:
        """Returns a single feature template. Archived feature templates are not addressable here and return ``404``.
        Restore a template first to read or update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.production("/features/{id}.json"),
            path_params=[param[int]("id", id_)],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureTemplateResponse],
            error_mapper=read_feature_template_error_mapper,
            request_options=request_options,
        )

    async def restore_feature_template(
        self, id_: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FeatureTemplateResponse, RestoreFeatureTemplateErrorBody]:
        """Clears the feature template's archived state. Feature catalog items created from this template are not
        automatically restored. Restore each one individually.

        Args:
            id_: The Advanced Billing id of the feature template.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/features/{id}/restore.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureTemplateResponse],
            error_mapper=restore_feature_template_error_mapper,
            request_options=request_options,
        )

    async def update_feature_template(
        self,
        id_: int,
        *,
        body: UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeatureTemplateResponse, UpdateFeatureTemplateErrorBody]:
        """Updates the name, description, unit, value type, default value, or default periodicity of a feature template.
        ``key`` is rejected on every update. ``kind`` is rejected once any feature catalog item has been created from
        this template.

        Archived feature templates are not addressable here and return ``404``. Restore a template first to update it.

        Args:
            id_: The Advanced Billing id of the feature template.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/features/{id}.json"),
            path_params=[param[int]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFeatureTemplateRequest | UpdateFeatureTemplateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[FeatureTemplateResponse],
            error_mapper=update_feature_template_error_mapper,
            request_options=request_options,
        )
