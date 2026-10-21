from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class NetTerms(SdkBaseModel):
    default_net_terms: int = 0
    automatic_net_terms: int = 0
    remittance_net_terms: int = 0
    net_terms_on_remittance_signups_enabled: bool = False
    custom_net_terms_enabled: bool = False


class NetTermsDict(TypedDict):
    default_net_terms: NotRequired[int]
    automatic_net_terms: NotRequired[int]
    remittance_net_terms: NotRequired[int]
    net_terms_on_remittance_signups_enabled: NotRequired[bool]
    custom_net_terms_enabled: NotRequired[bool]
