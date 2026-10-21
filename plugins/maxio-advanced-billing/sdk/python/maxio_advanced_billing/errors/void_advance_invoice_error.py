from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

VoidAdvanceInvoiceErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _VoidAdvanceInvoiceError:
    def map(self, status_code: int, content: bytes) -> VoidAdvanceInvoiceErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


void_advance_invoice_error_mapper: Final[ErrorMapper[VoidAdvanceInvoiceErrorBody]] = _VoidAdvanceInvoiceError()
