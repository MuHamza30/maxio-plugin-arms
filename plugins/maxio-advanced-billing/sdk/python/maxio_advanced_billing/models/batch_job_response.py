from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .batch_job import BatchJob, BatchJobDict


class BatchJobResponse(SdkBaseModel):
    batchjob: BatchJob


class BatchJobResponseDict(TypedDict):
    batchjob: BatchJobDict
