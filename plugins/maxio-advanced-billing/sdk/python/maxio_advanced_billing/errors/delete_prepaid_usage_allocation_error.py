from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_component_allocation_error1 import SubscriptionComponentAllocationError1

DeletePrepaidUsageAllocationErrorBody: TypeAlias = SubscriptionComponentAllocationError1 | RawError


@dataclass(frozen=True, slots=True)
class _DeletePrepaidUsageAllocationError:
    def map(self, status_code: int, content: bytes) -> DeletePrepaidUsageAllocationErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[SubscriptionComponentAllocationError1](content)
            case _:
                return RawError(status_code, content)


delete_prepaid_usage_allocation_error_mapper: Final[
    ErrorMapper[DeletePrepaidUsageAllocationErrorBody]
] = _DeletePrepaidUsageAllocationError()
