from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_customer import CreateCustomer, CreateCustomerDict


class CreateCustomerRequest(SdkBaseModel):
    customer: CreateCustomer


class CreateCustomerRequestDict(TypedDict):
    customer: CreateCustomerDict
