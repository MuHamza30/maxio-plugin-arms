from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class WalletTransaction(SdkBaseModel):
    """One append-only row on the wallet's ledger. Always appears bare inside a ``wallet_transactions`` array, never
    wrapped in its own key."""

    id: Optional[int] = UNSET
    """The Advanced Billing id of the ledger row."""

    wallet_id: Optional[int] = UNSET
    kind: Optional[str] = UNSET
    """The kind of ledger row. Known values: ``grant``, ``debit``, ``adjustment``, ``initial_balance``, and
    ``expiration``. More kinds are expected over time, so treat this as an open string and don't fail on one you don't
    recognize. Only ``grant`` and ``debit`` are accepted on `Create Wallet Transaction
    <$e/Wallet%20Transactions/createWalletTransaction>`__. ``adjustment`` rows are written by `Create Wallet Adjustment
    <$e/Wallet%20Adjustments/createWalletAdjustment>`__, ``initial_balance`` rows only by a seeded `Create Wallet
    <$e/Wallets/createWallet>`__, and ``expiration`` rows only by the automatic expiry sweep that writes off an
    unconsumed grant once its ``expires_at`` passes."""

    amount: Optional[str] = UNSET
    """A decimal string, **signed** on this resource. Non-negative for grants, negative for debits and expirations,
    either sign for adjustments. A grant row written after an overdraft repayment carries only what was left after the
    repayment (possibly ``"0.0"``), not the grant's ``original``."""

    grant_id: OptionalNullable[int] = UNSET
    """The grant this row is attributed to. ``null`` for an overdraft row (a ``kind: debit`` row draining the below-zero
    portion of a balance, attributed to no grant), for an overdraft-repayment row (the ``kind: grant`` row that pays an
    existing negative balance back to zero, written before any remainder becomes a new grant), and for an overdraft
    correction (a ``kind: adjustment`` row posted against an overdraft entry, which credits no grant)."""

    source_transaction_id: OptionalNullable[int] = UNSET
    """For an ``adjustment`` row posted against a specific usage entry, the id of the ``debit`` row it corrects.
    ``null`` for every other kind, and for adjustments made against a grant's balance directly."""

    source_corrections_total: OptionalNullable[str] = UNSET
    """For a ``debit`` row only, the signed sum (as a decimal string) of every adjustment posted against it so far
    (``"0.0"`` when none). ``null`` for every other kind. The row's own ``amount`` is never rewritten, so a caller
    deriving the entry's corrected quantity nets this out of ``amount``, and sends this value back as
    ``expected_source_corrections`` on a further correction."""

    balance_after: Optional[str] = UNSET
    """The wallet's posted balance immediately after this row was applied, as a decimal string. Compare it with the
    wallet's ``posted_balance``, not its ``balance``."""

    metered_from_at: OptionalNullable[RFC3339DateTime] = UNSET
    """For a row that closed a metered usage window (an hourly close, a depletion, or an expiry write-off), the start of
    that window. ``null`` on every other row."""

    metered_through_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The end of the usage window this row closed. ``null`` on every other row."""

    conversion_rate_applied: OptionalNullable[str] = UNSET
    """The meter-to-wallet-unit conversion rate applied to compute this row's ``amount``, as a decimal string. ``null``
    on every other row."""

    invoice_uid: OptionalNullable[str] = UNSET
    """The uid of the invoice behind a purchase's rows: the grant-creating row and, when the purchase repaid an
    overdraft, the repayment row. ``null`` on every other row."""

    memo: OptionalNullable[str] = UNSET
    """Free-text note. For an ``adjustment`` row, carries the required ``reason``."""

    created_at: Optional[RFC3339DateTime] = UNSET


class WalletTransactionDict(TypedDict):
    id: NotRequired[int]
    wallet_id: NotRequired[int]
    kind: NotRequired[str]
    amount: NotRequired[str]
    grant_id: NotRequired[int | None]
    source_transaction_id: NotRequired[int | None]
    source_corrections_total: NotRequired[str | None]
    balance_after: NotRequired[str]
    metered_from_at: NotRequired[RFC3339DateTime | None]
    metered_through_at: NotRequired[RFC3339DateTime | None]
    conversion_rate_applied: NotRequired[str | None]
    invoice_uid: NotRequired[str | None]
    memo: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
