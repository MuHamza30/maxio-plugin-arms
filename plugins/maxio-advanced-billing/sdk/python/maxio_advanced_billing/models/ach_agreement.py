from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AchAgreement(SdkBaseModel):
    """(Optional) If passed, the proof of the authorized ACH agreement terms will be persisted."""

    agreement_terms: Optional[str] = UNSET
    """(Required when providing ACH agreement params) The ACH authorization agreement terms."""

    authorizer_first_name: Optional[str] = UNSET
    """(Required when providing ACH agreement params) The first name of the person authorizing the ACH agreement."""

    authorizer_last_name: Optional[str] = UNSET
    """(Required when providing ACH agreement params) The last name of the person authorizing the ACH agreement."""

    ip_address: Optional[str] = UNSET
    """(Required when providing ACH agreement params) The IP address of the person authorizing the ACH agreement."""


class AchAgreementDict(TypedDict):
    agreement_terms: NotRequired[str]
    authorizer_first_name: NotRequired[str]
    authorizer_last_name: NotRequired[str]
    ip_address: NotRequired[str]
