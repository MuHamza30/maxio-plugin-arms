from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ListComponentsFilter(SdkBaseModel):
    ids: Optional[list[int]] = UNSET
    """Allows fetching components with matching id based on provided value. Use in query ``filter[ids]=1,2,3``."""

    use_site_exchange_rate: Optional[bool] = UNSET
    """Allows fetching components with matching use_site_exchange_rate based on provided value (refers to default price
    point). Use in query ``filter[use_site_exchange_rate]=true``."""


class ListComponentsFilterDict(TypedDict):
    ids: NotRequired[list[int]]
    use_site_exchange_rate: NotRequired[bool]
