from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

VoidInvoiceErrorBody: TypeAlias = Any | None | ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _VoidInvoiceError:
    def map(self, status_code: int, content: bytes) -> VoidInvoiceErrorBody:
        match status_code:
            case 404:
                return decode_json[Any | None](content)
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


void_invoice_error_mapper: Final[ErrorMapper[VoidInvoiceErrorBody]] = _VoidInvoiceError()
