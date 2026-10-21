from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ListProductFeaturesErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ListProductFeaturesError:
    def map(self, status_code: int, content: bytes) -> ListProductFeaturesErrorBody:
        match status_code:
            case 403:
                return decode_json[ErrorListResponse1](content)
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


list_product_features_error_mapper: Final[ErrorMapper[ListProductFeaturesErrorBody]] = _ListProductFeaturesError()
