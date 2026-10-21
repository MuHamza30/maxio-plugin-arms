from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ArchiveComponentPricePointErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ArchiveComponentPricePointError:
    def map(self, status_code: int, content: bytes) -> ArchiveComponentPricePointErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


archive_component_price_point_error_mapper: Final[
    ErrorMapper[ArchiveComponentPricePointErrorBody]
] = _ArchiveComponentPricePointError()
