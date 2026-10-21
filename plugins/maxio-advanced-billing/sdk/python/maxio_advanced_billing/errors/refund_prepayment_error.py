from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.refund_prepayment_base_errors_response1 import RefundPrepaymentBaseErrorsResponse1
from ..models.unions.refund_prepayment_error_response import RefundPrepaymentErrorResponse

RefundPrepaymentErrorBody: TypeAlias = (
    RefundPrepaymentBaseErrorsResponse1 | str | RefundPrepaymentErrorResponse | RawError
)


@dataclass(frozen=True, slots=True)
class _RefundPrepaymentError:
    def map(self, status_code: int, content: bytes) -> RefundPrepaymentErrorBody:
        match status_code:
            case 400:
                return decode_json[RefundPrepaymentBaseErrorsResponse1](content)
            case 404:
                return decode_json[str](content)
            case 422:
                return decode_json[RefundPrepaymentErrorResponse](content)
            case _:
                return RawError(status_code, content)


refund_prepayment_error_mapper: Final[ErrorMapper[RefundPrepaymentErrorBody]] = _RefundPrepaymentError()
