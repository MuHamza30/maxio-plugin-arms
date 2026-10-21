from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AttributeErrorModel(SdkBaseModel):
    attribute: list[str]


class AttributeErrorModelDict(TypedDict):
    attribute: list[str]
