from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_component_allocation_error1 import SubscriptionComponentAllocationError1

UpdatePrepaidUsageAllocationExpirationDateErrorBody: TypeAlias = SubscriptionComponentAllocationError1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdatePrepaidUsageAllocationExpirationDateError:
    def map(self, status_code: int, content: bytes) -> UpdatePrepaidUsageAllocationExpirationDateErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[SubscriptionComponentAllocationError1](content)
            case _:
                return RawError(status_code, content)


update_prepaid_usage_allocation_expiration_date_error_mapper: Final[
    ErrorMapper[UpdatePrepaidUsageAllocationExpirationDateErrorBody]
] = _UpdatePrepaidUsageAllocationExpirationDateError()
