from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .customer import Customer, CustomerDict


class CustomerResponse(SdkBaseModel):
    customer: Customer


class CustomerResponseDict(TypedDict):
    customer: CustomerDict
