from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

UpdateMetadataErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateMetadataError:
    def map(self, status_code: int, content: bytes) -> UpdateMetadataErrorBody:
        match status_code:
            case 422:
                return decode_json[SingleErrorResponse1](content)
            case _:
                return RawError(status_code, content)


update_metadata_error_mapper: Final[ErrorMapper[UpdateMetadataErrorBody]] = _UpdateMetadataError()
