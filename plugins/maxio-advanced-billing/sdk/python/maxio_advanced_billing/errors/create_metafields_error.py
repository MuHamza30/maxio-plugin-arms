from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

CreateMetafieldsErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateMetafieldsError:
    def map(self, status_code: int, content: bytes) -> CreateMetafieldsErrorBody:
        match status_code:
            case 422:
                return decode_json[SingleErrorResponse1](content)
            case _:
                return RawError(status_code, content)


create_metafields_error_mapper: Final[ErrorMapper[CreateMetafieldsErrorBody]] = _CreateMetafieldsError()
