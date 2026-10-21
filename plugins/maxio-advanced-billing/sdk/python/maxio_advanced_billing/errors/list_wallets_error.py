from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.wallet_error_response1 import WalletErrorResponse1

ListWalletsErrorBody: TypeAlias = WalletErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ListWalletsError:
    def map(self, status_code: int, content: bytes) -> ListWalletsErrorBody:
        match status_code:
            case 403:
                return RawError(status_code, content)
            case 422:
                return decode_json[WalletErrorResponse1](content)
            case _:
                return RawError(status_code, content)


list_wallets_error_mapper: Final[ErrorMapper[ListWalletsErrorBody]] = _ListWalletsError()
