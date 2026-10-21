from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..scheduled_renewal_item_request_body_component import (
    ScheduledRenewalItemRequestBodyComponent,
    ScheduledRenewalItemRequestBodyComponentDict,
)
from ..scheduled_renewal_item_request_body_product import (
    ScheduledRenewalItemRequestBodyProduct,
    ScheduledRenewalItemRequestBodyProductDict,
)

RenewalConfigurationItem: TypeAlias = Annotated[
    (
        Annotated[ScheduledRenewalItemRequestBodyComponent, Tag("Component")]
        | Annotated[ScheduledRenewalItemRequestBodyProduct, Tag("Product")]
    ),
    WireDiscriminator("item_type"),
]

RenewalConfigurationItemDict: TypeAlias = (
    ScheduledRenewalItemRequestBodyComponentDict | ScheduledRenewalItemRequestBodyProductDict
)
