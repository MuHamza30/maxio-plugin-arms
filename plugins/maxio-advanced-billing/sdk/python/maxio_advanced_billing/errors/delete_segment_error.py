from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteSegmentErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteSegmentError:
    def map(self, status_code: int, content: bytes) -> DeleteSegmentErrorBody:
        match status_code:
            case 404 | 422:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_segment_error_mapper: Final[ErrorMapper[DeleteSegmentErrorBody]] = _DeleteSegmentError()
