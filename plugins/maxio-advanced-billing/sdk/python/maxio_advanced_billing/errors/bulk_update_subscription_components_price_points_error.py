from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.component_price_point_error1 import ComponentPricePointError1

BulkUpdateSubscriptionComponentsPricePointsErrorBody: TypeAlias = ComponentPricePointError1 | RawError


@dataclass(frozen=True, slots=True)
class _BulkUpdateSubscriptionComponentsPricePointsError:
    def map(self, status_code: int, content: bytes) -> BulkUpdateSubscriptionComponentsPricePointsErrorBody:
        match status_code:
            case 422:
                return decode_json[ComponentPricePointError1](content)
            case _:
                return RawError(status_code, content)


bulk_update_subscription_components_price_points_error_mapper: Final[
    ErrorMapper[BulkUpdateSubscriptionComponentsPricePointsErrorBody]
] = _BulkUpdateSubscriptionComponentsPricePointsError()
