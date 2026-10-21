from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ListExportedSubscriptionsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListExportedSubscriptionsError:
    def map(self, status_code: int, content: bytes) -> ListExportedSubscriptionsErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


list_exported_subscriptions_error_mapper: Final[
    ErrorMapper[ListExportedSubscriptionsErrorBody]
] = _ListExportedSubscriptionsError()
