from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

UpdateMetafieldErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateMetafieldError:
    def map(self, status_code: int, content: bytes) -> UpdateMetafieldErrorBody:
        match status_code:
            case 422:
                return decode_json[SingleErrorResponse1](content)
            case _:
                return RawError(status_code, content)


update_metafield_error_mapper: Final[ErrorMapper[UpdateMetafieldErrorBody]] = _UpdateMetafieldError()
