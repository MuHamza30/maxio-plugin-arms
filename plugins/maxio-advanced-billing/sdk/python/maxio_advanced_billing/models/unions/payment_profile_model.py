from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..get_one_time_token_bank_account_payment_profile import (
    GetOneTimeTokenBankAccountPaymentProfile,
    GetOneTimeTokenBankAccountPaymentProfileDict,
)
from ..get_one_time_token_payment_profile import GetOneTimeTokenPaymentProfile, GetOneTimeTokenPaymentProfileDict

PaymentProfileModel: TypeAlias = Annotated[
    (
        Annotated[GetOneTimeTokenPaymentProfile, Tag("credit_card")]
        | Annotated[GetOneTimeTokenBankAccountPaymentProfile, Tag("bank_account")]
    ),
    WireDiscriminator("payment_type"),
]

PaymentProfileModelDict: TypeAlias = GetOneTimeTokenPaymentProfileDict | GetOneTimeTokenBankAccountPaymentProfileDict
