from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .on_off_component import OnOffComponent, OnOffComponentDict


class CreateOnOffComponent(SdkBaseModel):
    on_off_component: OnOffComponent


class CreateOnOffComponentDict(TypedDict):
    on_off_component: OnOffComponentDict
