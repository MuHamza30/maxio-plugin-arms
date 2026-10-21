from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionDateField(str, Enum):
    CURRENT_PERIOD_ENDS_AT = "current_period_ends_at"
    CURRENT_PERIOD_STARTS_AT = "current_period_starts_at"
    CREATED_AT = "created_at"
    ACTIVATED_AT = "activated_at"
    CANCELED_AT = "canceled_at"
    EXPIRES_AT = "expires_at"
    TRIAL_STARTED_AT = "trial_started_at"
    TRIAL_ENDED_AT = "trial_ended_at"
    UPDATED_AT = "updated_at"

    __str__ = str.__str__


SubscriptionDateFieldOrStr: TypeAlias = Annotated[
    SubscriptionDateField | str, open_enum_validator(SubscriptionDateField)
]
