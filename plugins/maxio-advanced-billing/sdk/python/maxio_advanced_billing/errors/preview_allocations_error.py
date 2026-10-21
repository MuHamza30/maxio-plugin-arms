from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.component_allocation_error1 import ComponentAllocationError1

PreviewAllocationsErrorBody: TypeAlias = ComponentAllocationError1 | RawError


@dataclass(frozen=True, slots=True)
class _PreviewAllocationsError:
    def map(self, status_code: int, content: bytes) -> PreviewAllocationsErrorBody:
        match status_code:
            case 422:
                return decode_json[ComponentAllocationError1](content)
            case _:
                return RawError(status_code, content)


preview_allocations_error_mapper: Final[ErrorMapper[PreviewAllocationsErrorBody]] = _PreviewAllocationsError()
