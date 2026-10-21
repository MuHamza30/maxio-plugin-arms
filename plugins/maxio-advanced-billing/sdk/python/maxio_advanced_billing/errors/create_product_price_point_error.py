from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.product_price_point_error_response1 import ProductPricePointErrorResponse1

CreateProductPricePointErrorBody: TypeAlias = ProductPricePointErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateProductPricePointError:
    def map(self, status_code: int, content: bytes) -> CreateProductPricePointErrorBody:
        match status_code:
            case 422:
                return decode_json[ProductPricePointErrorResponse1](content)
            case _:
                return RawError(status_code, content)


create_product_price_point_error_mapper: Final[
    ErrorMapper[CreateProductPricePointErrorBody]
] = _CreateProductPricePointError()
