from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

UpdateProductErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateProductError:
    def map(self, status_code: int, content: bytes) -> UpdateProductErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


update_product_error_mapper: Final[ErrorMapper[UpdateProductErrorBody]] = _UpdateProductError()
