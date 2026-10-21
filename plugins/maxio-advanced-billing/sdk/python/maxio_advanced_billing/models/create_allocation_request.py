from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_allocation import CreateAllocation, CreateAllocationDict


class CreateAllocationRequest(SdkBaseModel):
    allocation: CreateAllocation


class CreateAllocationRequestDict(TypedDict):
    allocation: CreateAllocationDict
