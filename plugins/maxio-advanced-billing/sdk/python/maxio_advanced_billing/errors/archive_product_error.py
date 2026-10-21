from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ArchiveProductErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ArchiveProductError:
    def map(self, status_code: int, content: bytes) -> ArchiveProductErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


archive_product_error_mapper: Final[ErrorMapper[ArchiveProductErrorBody]] = _ArchiveProductError()
