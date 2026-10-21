from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadInvoicesExportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadInvoicesExportError:
    def map(self, status_code: int, content: bytes) -> ReadInvoicesExportErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_invoices_export_error_mapper: Final[ErrorMapper[ReadInvoicesExportErrorBody]] = _ReadInvoicesExportError()
