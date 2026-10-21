from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .issue_service_credit import IssueServiceCredit, IssueServiceCreditDict


class IssueServiceCreditRequest(SdkBaseModel):
    service_credit: IssueServiceCredit


class IssueServiceCreditRequestDict(TypedDict):
    service_credit: IssueServiceCreditDict
