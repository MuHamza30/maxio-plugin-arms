from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .dunner_data import DunnerData, DunnerDataDict
from .dunning_step_data import DunningStepData, DunningStepDataDict


class DunningStepReached(SdkBaseModel):
    dunner: DunnerData
    current_step: DunningStepData
    next_step: DunningStepData


class DunningStepReachedDict(TypedDict):
    dunner: DunnerDataDict
    current_step: DunningStepDataDict
    next_step: DunningStepDataDict
