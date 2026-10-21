from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteMetadataErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteMetadataError:
    def map(self, status_code: int, content: bytes) -> DeleteMetadataErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_metadata_error_mapper: Final[ErrorMapper[DeleteMetadataErrorBody]] = _DeleteMetadataError()
