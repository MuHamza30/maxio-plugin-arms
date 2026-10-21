from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.wallet_error_response1 import WalletErrorResponse1

UpdateWalletProductErrorBody: TypeAlias = WalletErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateWalletProductError:
    def map(self, status_code: int, content: bytes) -> UpdateWalletProductErrorBody:
        match status_code:
            case 403:
                return RawError(status_code, content)
            case 404 | 422:
                return decode_json[WalletErrorResponse1](content)
            case _:
                return RawError(status_code, content)


update_wallet_product_error_mapper: Final[ErrorMapper[UpdateWalletProductErrorBody]] = _UpdateWalletProductError()
