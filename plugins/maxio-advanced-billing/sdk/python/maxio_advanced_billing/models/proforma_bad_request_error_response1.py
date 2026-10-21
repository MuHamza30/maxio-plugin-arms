from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .proforma_error import ProformaError, ProformaErrorDict


class ProformaBadRequestErrorResponse1(SdkBaseModel):
    errors: Optional[ProformaError] = UNSET


class ProformaBadRequestErrorResponse1Dict(TypedDict):
    errors: NotRequired[ProformaErrorDict]
