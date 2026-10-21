from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrepaymentAggregatedError(SdkBaseModel):
    amount_in_cents: Optional[list[str]] = UNSET
    base: Optional[list[str]] = UNSET
    external: Optional[list[str]] = UNSET


class PrepaymentAggregatedErrorDict(TypedDict):
    amount_in_cents: NotRequired[list[str]]
    base: NotRequired[list[str]]
    external: NotRequired[list[str]]
