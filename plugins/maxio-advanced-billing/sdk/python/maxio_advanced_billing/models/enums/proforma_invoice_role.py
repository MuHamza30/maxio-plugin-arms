from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProformaInvoiceRole(str, Enum):
    """'proforma' value is deprecated in favor of proforma_adhoc and proforma_automatic."""

    UNSET = "unset"
    PROFORMA = "proforma"
    PROFORMA_ADHOC = "proforma_adhoc"
    PROFORMA_AUTOMATIC = "proforma_automatic"

    __str__ = str.__str__


ProformaInvoiceRoleOrStr: TypeAlias = Annotated[ProformaInvoiceRole | str, open_enum_validator(ProformaInvoiceRole)]
