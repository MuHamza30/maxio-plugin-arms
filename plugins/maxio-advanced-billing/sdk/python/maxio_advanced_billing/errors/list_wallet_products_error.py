from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ListWalletProductsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListWalletProductsError:
    def map(self, status_code: int, content: bytes) -> ListWalletProductsErrorBody:
        match status_code:
            case 403:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


list_wallet_products_error_mapper: Final[ErrorMapper[ListWalletProductsErrorBody]] = _ListWalletProductsError()
