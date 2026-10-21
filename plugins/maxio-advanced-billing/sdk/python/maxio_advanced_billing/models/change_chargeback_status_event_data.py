from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.chargeback_status import ChargebackStatusOrStr


class ChangeChargebackStatusEventData(SdkBaseModel):
    """Example schema for an ``change_chargeback_status`` event"""

    chargeback_status: ChargebackStatusOrStr


class ChangeChargebackStatusEventDataDict(TypedDict):
    chargeback_status: ChargebackStatusOrStr
