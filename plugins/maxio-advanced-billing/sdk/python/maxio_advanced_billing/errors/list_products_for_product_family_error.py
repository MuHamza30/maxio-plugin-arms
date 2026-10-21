from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json

ListProductsForProductFamilyErrorBody: TypeAlias = str | RawError


@dataclass(frozen=True, slots=True)
class _ListProductsForProductFamilyError:
    def map(self, status_code: int, content: bytes) -> ListProductsForProductFamilyErrorBody:
        match status_code:
            case 404:
                return decode_json[str](content)
            case _:
                return RawError(status_code, content)


list_products_for_product_family_error_mapper: Final[
    ErrorMapper[ListProductsForProductFamilyErrorBody]
] = _ListProductsForProductFamilyError()
