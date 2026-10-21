from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.single_string_error_response1 import SingleStringErrorResponse1

ValidateReferralCodeErrorBody: TypeAlias = SingleStringErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ValidateReferralCodeError:
    def map(self, status_code: int, content: bytes) -> ValidateReferralCodeErrorBody:
        match status_code:
            case 404:
                return decode_json[SingleStringErrorResponse1](content)
            case _:
                return RawError(status_code, content)


validate_referral_code_error_mapper: Final[ErrorMapper[ValidateReferralCodeErrorBody]] = _ValidateReferralCodeError()
