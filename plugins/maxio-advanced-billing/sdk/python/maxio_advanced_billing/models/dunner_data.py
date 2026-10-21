from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class DunnerData(SdkBaseModel):
    state: str
    subscription_id: int
    revenue_at_risk_in_cents: int
    created_at: RFC3339DateTime
    attempts: int
    last_attempted_at: RFC3339DateTime


class DunnerDataDict(TypedDict):
    state: str
    subscription_id: int
    revenue_at_risk_in_cents: int
    created_at: RFC3339DateTime
    attempts: int
    last_attempted_at: RFC3339DateTime
