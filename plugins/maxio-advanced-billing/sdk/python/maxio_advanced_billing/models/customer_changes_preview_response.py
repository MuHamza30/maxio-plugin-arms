from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .customer_change import CustomerChange, CustomerChangeDict


class CustomerChangesPreviewResponse(SdkBaseModel):
    changes: CustomerChange


class CustomerChangesPreviewResponseDict(TypedDict):
    changes: CustomerChangeDict
