from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TrialType(str, Enum):
    """Indicates how a trial is handled when the trial period ends and there is no credit card on file. For
    ``no_obligation``, the subscription transitions to a Trial Ended state. Maxio will not send any emails or
    statements. For ``payment_expected``, the subscription transitions to a Past Due state. Maxio will send normal
    dunning emails and statements according to your other settings."""

    NO_OBLIGATION = "no_obligation"
    PAYMENT_EXPECTED = "payment_expected"

    __str__ = str.__str__


TrialTypeOrStr: TypeAlias = Annotated[TrialType | str, open_enum_validator(TrialType)]
