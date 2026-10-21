from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ListExportedProformaInvoicesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListExportedProformaInvoicesError:
    def map(self, status_code: int, content: bytes) -> ListExportedProformaInvoicesErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


list_exported_proforma_invoices_error_mapper: Final[
    ErrorMapper[ListExportedProformaInvoicesErrorBody]
] = _ListExportedProformaInvoicesError()
