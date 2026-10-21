from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteCouponSubcodeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteCouponSubcodeError:
    def map(self, status_code: int, content: bytes) -> DeleteCouponSubcodeErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_coupon_subcode_error_mapper: Final[ErrorMapper[DeleteCouponSubcodeErrorBody]] = _DeleteCouponSubcodeError()
