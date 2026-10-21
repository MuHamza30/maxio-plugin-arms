from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

IssueInvoiceErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _IssueInvoiceError:
    def map(self, status_code: int, content: bytes) -> IssueInvoiceErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


issue_invoice_error_mapper: Final[ErrorMapper[IssueInvoiceErrorBody]] = _IssueInvoiceError()
