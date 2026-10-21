from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_group_signup_error_response1 import SubscriptionGroupSignupErrorResponse1

SignupWithSubscriptionGroupErrorBody: TypeAlias = SubscriptionGroupSignupErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _SignupWithSubscriptionGroupError:
    def map(self, status_code: int, content: bytes) -> SignupWithSubscriptionGroupErrorBody:
        match status_code:
            case 422:
                return decode_json[SubscriptionGroupSignupErrorResponse1](content)
            case _:
                return RawError(status_code, content)


signup_with_subscription_group_error_mapper: Final[
    ErrorMapper[SignupWithSubscriptionGroupErrorBody]
] = _SignupWithSubscriptionGroupError()
