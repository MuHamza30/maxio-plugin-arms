from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_array_map_response1 import ErrorArrayMapResponse1
from ..models.proforma_bad_request_error_response1 import ProformaBadRequestErrorResponse1

CreateSignupProformaInvoiceErrorBody: TypeAlias = ProformaBadRequestErrorResponse1 | ErrorArrayMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateSignupProformaInvoiceError:
    def map(self, status_code: int, content: bytes) -> CreateSignupProformaInvoiceErrorBody:
        match status_code:
            case 400:
                return decode_json[ProformaBadRequestErrorResponse1](content)
            case 422:
                return decode_json[ErrorArrayMapResponse1](content)
            case _:
                return RawError(status_code, content)


create_signup_proforma_invoice_error_mapper: Final[
    ErrorMapper[CreateSignupProformaInvoiceErrorBody]
] = _CreateSignupProformaInvoiceError()
