from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_array_map_response1 import ErrorArrayMapResponse1

CreateInvoiceErrorBody: TypeAlias = ErrorArrayMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateInvoiceError:
    def map(self, status_code: int, content: bytes) -> CreateInvoiceErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorArrayMapResponse1](content)
            case _:
                return RawError(status_code, content)


create_invoice_error_mapper: Final[ErrorMapper[CreateInvoiceErrorBody]] = _CreateInvoiceError()
