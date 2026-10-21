from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreateSignupProformaPreviewInclude(str, Enum):
    NEXT_PROFORMA_INVOICE = "next_proforma_invoice"

    __str__ = str.__str__


CreateSignupProformaPreviewIncludeOrStr: TypeAlias = Annotated[
    CreateSignupProformaPreviewInclude | str, open_enum_validator(CreateSignupProformaPreviewInclude)
]
