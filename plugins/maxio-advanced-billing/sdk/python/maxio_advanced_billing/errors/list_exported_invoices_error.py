from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ListExportedInvoicesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListExportedInvoicesError:
    def map(self, status_code: int, content: bytes) -> ListExportedInvoicesErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


list_exported_invoices_error_mapper: Final[ErrorMapper[ListExportedInvoicesErrorBody]] = _ListExportedInvoicesError()
