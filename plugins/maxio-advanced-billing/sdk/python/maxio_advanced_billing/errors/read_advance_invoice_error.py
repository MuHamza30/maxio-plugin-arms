from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadAdvanceInvoiceErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadAdvanceInvoiceError:
    def map(self, status_code: int, content: bytes) -> ReadAdvanceInvoiceErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_advance_invoice_error_mapper: Final[ErrorMapper[ReadAdvanceInvoiceErrorBody]] = _ReadAdvanceInvoiceError()
