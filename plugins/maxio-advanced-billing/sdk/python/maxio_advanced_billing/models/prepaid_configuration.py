from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrepaidConfiguration(SdkBaseModel):
    id: Optional[int] = UNSET
    initial_funding_amount_in_cents: Optional[int] = UNSET
    replenish_to_amount_in_cents: Optional[int] = UNSET
    auto_replenish: Optional[bool] = UNSET
    replenish_threshold_amount_in_cents: Optional[int] = UNSET


class PrepaidConfigurationDict(TypedDict):
    id: NotRequired[int]
    initial_funding_amount_in_cents: NotRequired[int]
    replenish_to_amount_in_cents: NotRequired[int]
    auto_replenish: NotRequired[bool]
    replenish_threshold_amount_in_cents: NotRequired[int]
