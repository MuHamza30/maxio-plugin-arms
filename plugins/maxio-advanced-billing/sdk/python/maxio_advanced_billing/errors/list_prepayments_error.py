from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ListPrepaymentsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListPrepaymentsError:
    def map(self, status_code: int, content: bytes) -> ListPrepaymentsErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


list_prepayments_error_mapper: Final[ErrorMapper[ListPrepaymentsErrorBody]] = _ListPrepaymentsError()
