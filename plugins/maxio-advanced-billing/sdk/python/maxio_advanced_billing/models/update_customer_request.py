from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_customer import UpdateCustomer, UpdateCustomerDict


class UpdateCustomerRequest(SdkBaseModel):
    customer: UpdateCustomer


class UpdateCustomerRequestDict(TypedDict):
    customer: UpdateCustomerDict
