from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.tax_configuration_kind import TaxConfigurationKind, TaxConfigurationKindOrStr
from .enums.tax_destination_address import TaxDestinationAddressOrStr


class TaxConfiguration(SdkBaseModel):
    kind: TaxConfigurationKindOrStr = TaxConfigurationKind.CUSTOM
    destination_address: Optional[TaxDestinationAddressOrStr] = UNSET
    fully_configured: bool = False
    """Returns ``true`` when Chargify has been properly configured to charge tax using the specified tax system. More
    details about taxes: https://maxio.zendesk.com/hc/en-us/articles/24287012608909-Taxes-Overview"""


class TaxConfigurationDict(TypedDict):
    kind: NotRequired[TaxConfigurationKindOrStr]
    destination_address: NotRequired[TaxDestinationAddressOrStr]
    fully_configured: NotRequired[bool]
