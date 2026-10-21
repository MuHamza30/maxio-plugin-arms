from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .list_mrr_response_result import ListMrrResponseResult, ListMrrResponseResultDict


class ListMrrResponse(SdkBaseModel):
    mrr: ListMrrResponseResult


class ListMrrResponseDict(TypedDict):
    mrr: ListMrrResponseResultDict
