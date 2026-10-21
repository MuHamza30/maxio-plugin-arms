from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json

BulkCreateProductPricePointsErrorBody: TypeAlias = dict[str, Any] | RawError


@dataclass(frozen=True, slots=True)
class _BulkCreateProductPricePointsError:
    def map(self, status_code: int, content: bytes) -> BulkCreateProductPricePointsErrorBody:
        match status_code:
            case 422:
                return decode_json[dict[str, Any]](content)
            case _:
                return RawError(status_code, content)


bulk_create_product_price_points_error_mapper: Final[
    ErrorMapper[BulkCreateProductPricePointsErrorBody]
] = _BulkCreateProductPricePointsError()
