from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .aggregated_entitlement import AggregatedEntitlement, AggregatedEntitlementDict


class AggregatedEntitlementsResponse(SdkBaseModel):
    subscription_id: int
    customer_id: int
    status: str
    """The subscription's current state, e.g. ``active``, ``trialing``, ``canceled``."""

    entitlements: list[AggregatedEntitlement]


class AggregatedEntitlementsResponseDict(TypedDict):
    subscription_id: int
    customer_id: int
    status: str
    entitlements: list[AggregatedEntitlementDict]
