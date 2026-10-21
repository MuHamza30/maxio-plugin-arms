from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaymentCollectionMethodChanged(SdkBaseModel):
    previous_value: str
    current_value: str


class PaymentCollectionMethodChangedDict(TypedDict):
    previous_value: str
    current_value: str
