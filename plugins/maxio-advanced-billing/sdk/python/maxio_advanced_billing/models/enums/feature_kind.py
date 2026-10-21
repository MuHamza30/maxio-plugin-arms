from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeatureKind(str, Enum):
    """The behavior of a feature:
    - ``access_right``: a boolean entitlement. A subscriber either has access or does not.
    - ``usage_limit``: a quantified allowance measured over a recurring period (for example, "10,000 API calls per
        month").
    - ``service_right``: a free-form value (text, boolean, or number) that isn't a simple access flag or a metered
        limit."""

    ACCESS_RIGHT = "access_right"
    USAGE_LIMIT = "usage_limit"
    SERVICE_RIGHT = "service_right"

    __str__ = str.__str__


FeatureKindOrStr: TypeAlias = Annotated[FeatureKind | str, open_enum_validator(FeatureKind)]
