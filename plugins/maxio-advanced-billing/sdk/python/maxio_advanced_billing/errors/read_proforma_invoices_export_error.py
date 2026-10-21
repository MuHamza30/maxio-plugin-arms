from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadProformaInvoicesExportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadProformaInvoicesExportError:
    def map(self, status_code: int, content: bytes) -> ReadProformaInvoicesExportErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_proforma_invoices_export_error_mapper: Final[
    ErrorMapper[ReadProformaInvoicesExportErrorBody]
] = _ReadProformaInvoicesExportError()
