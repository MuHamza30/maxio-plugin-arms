from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.issue_service_credit_error_response import IssueServiceCreditErrorResponse

IssueServiceCreditErrorBody: TypeAlias = IssueServiceCreditErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _IssueServiceCreditError:
    def map(self, status_code: int, content: bytes) -> IssueServiceCreditErrorBody:
        match status_code:
            case 422:
                return decode_json[IssueServiceCreditErrorResponse](content)
            case _:
                return RawError(status_code, content)


issue_service_credit_error_mapper: Final[ErrorMapper[IssueServiceCreditErrorBody]] = _IssueServiceCreditError()
