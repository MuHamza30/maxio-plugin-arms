from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .prepaid_usage_allocation_detail import PrepaidUsageAllocationDetail, PrepaidUsageAllocationDetailDict
from .unions.new_overage_unit_balance import NewOverageUnitBalance, NewOverageUnitBalanceDict
from .unions.new_unit_balance import NewUnitBalance, NewUnitBalanceDict


class PrepaidUsage(SdkBaseModel):
    previous_unit_balance: str
    previous_overage_unit_balance: str
    new_unit_balance: NewUnitBalance
    new_overage_unit_balance: NewOverageUnitBalance
    usage_quantity: int
    overage_usage_quantity: int
    component_id: int
    component_handle: str
    memo: str
    allocation_details: list[PrepaidUsageAllocationDetail]


class PrepaidUsageDict(TypedDict):
    previous_unit_balance: str
    previous_overage_unit_balance: str
    new_unit_balance: NewUnitBalanceDict
    new_overage_unit_balance: NewOverageUnitBalanceDict
    usage_quantity: int
    overage_usage_quantity: int
    component_id: int
    component_handle: str
    memo: str
    allocation_details: list[PrepaidUsageAllocationDetailDict]
