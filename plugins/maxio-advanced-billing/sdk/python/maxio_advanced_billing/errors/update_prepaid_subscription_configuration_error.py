from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.prepaid_configuration_error_response import PrepaidConfigurationErrorResponse

UpdatePrepaidSubscriptionConfigurationErrorBody: TypeAlias = PrepaidConfigurationErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _UpdatePrepaidSubscriptionConfigurationError:
    def map(self, status_code: int, content: bytes) -> UpdatePrepaidSubscriptionConfigurationErrorBody:
        match status_code:
            case 422:
                return decode_json[PrepaidConfigurationErrorResponse](content)
            case _:
                return RawError(status_code, content)


update_prepaid_subscription_configuration_error_mapper: Final[
    ErrorMapper[UpdatePrepaidSubscriptionConfigurationErrorBody]
] = _UpdatePrepaidSubscriptionConfigurationError()
