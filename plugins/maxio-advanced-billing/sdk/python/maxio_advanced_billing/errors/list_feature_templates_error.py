from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ListFeatureTemplatesErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ListFeatureTemplatesError:
    def map(self, status_code: int, content: bytes) -> ListFeatureTemplatesErrorBody:
        match status_code:
            case 403:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


list_feature_templates_error_mapper: Final[ErrorMapper[ListFeatureTemplatesErrorBody]] = _ListFeatureTemplatesError()
