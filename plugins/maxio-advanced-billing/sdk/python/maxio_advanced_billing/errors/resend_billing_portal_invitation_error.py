from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ResendBillingPortalInvitationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ResendBillingPortalInvitationError:
    def map(self, status_code: int, content: bytes) -> ResendBillingPortalInvitationErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


resend_billing_portal_invitation_error_mapper: Final[
    ErrorMapper[ResendBillingPortalInvitationErrorBody]
] = _ResendBillingPortalInvitationError()
