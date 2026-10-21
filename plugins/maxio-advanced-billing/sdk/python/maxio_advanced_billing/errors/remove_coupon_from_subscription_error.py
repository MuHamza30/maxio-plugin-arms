from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_remove_coupon_errors1 import SubscriptionRemoveCouponErrors1

RemoveCouponFromSubscriptionErrorBody: TypeAlias = SubscriptionRemoveCouponErrors1 | RawError


@dataclass(frozen=True, slots=True)
class _RemoveCouponFromSubscriptionError:
    def map(self, status_code: int, content: bytes) -> RemoveCouponFromSubscriptionErrorBody:
        match status_code:
            case 422:
                return decode_json[SubscriptionRemoveCouponErrors1](content)
            case _:
                return RawError(status_code, content)


remove_coupon_from_subscription_error_mapper: Final[
    ErrorMapper[RemoveCouponFromSubscriptionErrorBody]
] = _RemoveCouponFromSubscriptionError()
