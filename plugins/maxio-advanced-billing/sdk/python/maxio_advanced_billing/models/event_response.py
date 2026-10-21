from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .event import Event, EventDict


class EventResponse(SdkBaseModel):
    event: Event


class EventResponseDict(TypedDict):
    event: EventDict
