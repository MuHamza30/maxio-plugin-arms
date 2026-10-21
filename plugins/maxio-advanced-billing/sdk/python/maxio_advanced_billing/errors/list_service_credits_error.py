from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ListServiceCreditsErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ListServiceCreditsError:
    def map(self, status_code: int, content: bytes) -> ListServiceCreditsErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


list_service_credits_error_mapper: Final[ErrorMapper[ListServiceCreditsErrorBody]] = _ListServiceCreditsError()
