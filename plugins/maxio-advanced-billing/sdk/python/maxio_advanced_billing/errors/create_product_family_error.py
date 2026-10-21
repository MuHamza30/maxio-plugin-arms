from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CreateProductFamilyErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateProductFamilyError:
    def map(self, status_code: int, content: bytes) -> CreateProductFamilyErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


create_product_family_error_mapper: Final[ErrorMapper[CreateProductFamilyErrorBody]] = _CreateProductFamilyError()
