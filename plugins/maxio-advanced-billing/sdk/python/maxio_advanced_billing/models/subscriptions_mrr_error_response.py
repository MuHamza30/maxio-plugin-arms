from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .attribute_error_model import AttributeErrorModel, AttributeErrorModelDict


class SubscriptionsMrrErrorResponse(SdkBaseModel):
    errors: AttributeErrorModel


class SubscriptionsMrrErrorResponseDict(TypedDict):
    errors: AttributeErrorModelDict
