from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteMetafieldErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteMetafieldError:
    def map(self, status_code: int, content: bytes) -> DeleteMetafieldErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_metafield_error_mapper: Final[ErrorMapper[DeleteMetafieldErrorBody]] = _DeleteMetafieldError()
