from __future__ import annotations

from typing import TypeAlias

from ..customer_error import CustomerError, CustomerErrorDict

Errors1: TypeAlias = CustomerError | list[str]

Errors1Dict: TypeAlias = CustomerErrorDict | list[str]
