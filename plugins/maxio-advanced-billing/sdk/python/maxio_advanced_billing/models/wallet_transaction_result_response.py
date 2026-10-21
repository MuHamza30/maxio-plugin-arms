from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wallet_transaction import WalletTransaction, WalletTransactionDict


class WalletTransactionResultResponse(SdkBaseModel):
    """Returned by `Create Wallet Transaction <$e/Wallet%20Transactions/createWalletTransaction>`__.
    ``wallet_transactions`` and ``balance`` are always present. ``requested_amount``, ``drained_amount``, and
    ``rejected_amount`` are present only when the request's ``kind`` was ``debit``."""

    wallet_transactions: list[WalletTransaction]
    requested_amount: Optional[str] = UNSET
    """``kind: debit`` only. The amount that was requested, as a decimal string."""

    drained_amount: Optional[str] = UNSET
    """``kind: debit`` only. The amount actually drained from the wallet's grants, as a decimal string."""

    rejected_amount: Optional[str] = UNSET
    """``kind: debit`` only, as a decimal string. Under ``hard_stop_overflow: discard``, this is the requested amount
    minus what the wallet could cover (``"0.0"`` on a full drain). Always ``"0.0"`` under ``allow_negative``; nothing is
    rejected, and the balance goes negative instead."""

    balance: str
    """The wallet's new balance, as a decimal string."""


class WalletTransactionResultResponseDict(TypedDict):
    wallet_transactions: list[WalletTransactionDict]
    requested_amount: NotRequired[str]
    drained_amount: NotRequired[str]
    rejected_amount: NotRequired[str]
    balance: str
