from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BillingManifestLineItemKind(str, Enum):
    """A handle for the billing manifest line item kind"""

    BASELINE = "baseline"
    INITIAL = "initial"
    TRIAL = "trial"
    COUPON = "coupon"
    COMPONENT = "component"
    TAX = "tax"

    __str__ = str.__str__


BillingManifestLineItemKindOrStr: TypeAlias = Annotated[
    BillingManifestLineItemKind | str, open_enum_validator(BillingManifestLineItemKind)
]
