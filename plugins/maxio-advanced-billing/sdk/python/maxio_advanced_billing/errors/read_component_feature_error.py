from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ReadComponentFeatureErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ReadComponentFeatureError:
    def map(self, status_code: int, content: bytes) -> ReadComponentFeatureErrorBody:
        match status_code:
            case 403:
                return decode_json[ErrorListResponse1](content)
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_component_feature_error_mapper: Final[ErrorMapper[ReadComponentFeatureErrorBody]] = _ReadComponentFeatureError()
