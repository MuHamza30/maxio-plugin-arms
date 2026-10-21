from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

ExportProformaInvoicesErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ExportProformaInvoicesError:
    def map(self, status_code: int, content: bytes) -> ExportProformaInvoicesErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 409:
                return decode_json[SingleErrorResponse1](content)
            case _:
                return RawError(status_code, content)


export_proforma_invoices_error_mapper: Final[
    ErrorMapper[ExportProformaInvoicesErrorBody]
] = _ExportProformaInvoicesError()
