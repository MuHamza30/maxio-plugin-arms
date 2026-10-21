from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

RecordPaymentForInvoiceErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _RecordPaymentForInvoiceError:
    def map(self, status_code: int, content: bytes) -> RecordPaymentForInvoiceErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


record_payment_for_invoice_error_mapper: Final[
    ErrorMapper[RecordPaymentForInvoiceErrorBody]
] = _RecordPaymentForInvoiceError()
