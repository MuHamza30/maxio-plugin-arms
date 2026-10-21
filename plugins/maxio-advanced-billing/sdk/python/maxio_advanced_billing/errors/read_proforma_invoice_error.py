from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadProformaInvoiceErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadProformaInvoiceError:
    def map(self, status_code: int, content: bytes) -> ReadProformaInvoiceErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_proforma_invoice_error_mapper: Final[ErrorMapper[ReadProformaInvoiceErrorBody]] = _ReadProformaInvoiceError()
