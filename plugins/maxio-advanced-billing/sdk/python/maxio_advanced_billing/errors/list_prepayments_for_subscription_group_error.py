from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ListPrepaymentsForSubscriptionGroupErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListPrepaymentsForSubscriptionGroupError:
    def map(self, status_code: int, content: bytes) -> ListPrepaymentsForSubscriptionGroupErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


list_prepayments_for_subscription_group_error_mapper: Final[
    ErrorMapper[ListPrepaymentsForSubscriptionGroupErrorBody]
] = _ListPrepaymentsForSubscriptionGroupError()
