from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadSubscriptionsExportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadSubscriptionsExportError:
    def map(self, status_code: int, content: bytes) -> ReadSubscriptionsExportErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_subscriptions_export_error_mapper: Final[
    ErrorMapper[ReadSubscriptionsExportErrorBody]
] = _ReadSubscriptionsExportError()
