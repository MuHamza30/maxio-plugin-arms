from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CreateComponentFeatureErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateComponentFeatureError:
    def map(self, status_code: int, content: bytes) -> CreateComponentFeatureErrorBody:
        match status_code:
            case 403 | 422:
                return decode_json[ErrorListResponse1](content)
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


create_component_feature_error_mapper: Final[
    ErrorMapper[CreateComponentFeatureErrorBody]
] = _CreateComponentFeatureError()
