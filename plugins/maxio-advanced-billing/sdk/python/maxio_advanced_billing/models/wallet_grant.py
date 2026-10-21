from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.origin import OriginOrStr


class WalletGrant(SdkBaseModel):
    """A funding tranche embedded on the wallet. ``original`` is the amount the grant was created with;
    ``posted_remaining`` is what debits and adjustments written to the ledger have left; ``remaining`` is what can still
    be spent. Debits drain grants earliest-expiration-first (grants with no expiration are drained last)."""

    id: Optional[int] = UNSET
    """The Advanced Billing id of the grant."""

    name: Optional[str] = UNSET
    """The memo the grant was created with, or `Grant"""

    original: Optional[str] = UNSET
    """The amount the grant was created with, encoded as a decimal string. Never changes after creation."""

    remaining: Optional[str] = UNSET
    """What the grant can still spend, encoded as a decimal string. On `Read Wallet <$e/Wallets/readWallet>`__ for a
    metered wallet whose ``balance`` is the live figure, this is ``posted_remaining`` less the pending usage drawn from
    this grant in drain order: usage past a grant spills to the next one, and usage past every grant is an overdraft
    that belongs to no grant. It never goes below zero, and the grants' ``remaining`` add up to the wallet's ``balance``
    whenever ``balance`` is zero or more. Everywhere else it equals ``posted_remaining``."""

    posted_remaining: Optional[str] = UNSET
    """The grant's remainder from written ledger entries alone, encoded as a decimal string. Always present. This is the
    figure an adjustment checks ``expected_remaining`` and its bounds against, so send it back, not ``remaining``, when
    correcting a grant."""

    expires_at: OptionalNullable[RFC3339DateTime] = UNSET
    """When this grant's unconsumed remainder is automatically written off. ``null`` for an evergreen grant."""

    expires_on: OptionalNullable[Date] = UNSET
    """The calendar day ``expires_at`` falls on, already resolved in the site's time zone."""

    expired_at: OptionalNullable[RFC3339DateTime] = UNSET
    """When the expiry sweep actually wrote this grant's remainder off. Usually falls shortly after ``expires_at``; use
    ``expires_on`` for the date the grant expired, not this field. ``null`` if the grant was never written off
    (including a grant simply spent to zero before its ``expires_at``)."""

    expired_on: OptionalNullable[Date] = UNSET
    """The calendar day ``expired_at`` falls on, resolved in the site's time zone."""

    origin: Optional[OriginOrStr] = UNSET
    """How the grant was created. ``recurring`` comes from the wallet's automatic funding schedule (see the wallet's
    ``recurring_funding`` array). ``manual`` comes from a one-time grant posted to `Create Wallet Transaction
    <$e/Wallet%20Transactions/createWalletTransaction>`__. ``initial_balance`` comes from a non-zero ``initial_balance``
    at wallet creation. ``allowance_increase`` comes from raising a funding entitlement's allowance while it's already
    funding a wallet. ``purchase`` comes from `Create Wallet Purchase
    <$e/Wallet%20Purchases/createWalletPurchase>`__."""

    granted_for_period_start: OptionalNullable[RFC3339DateTime] = UNSET
    """For a ``recurring`` grant, the start of the funding cadence period this grant covers. ``null`` for every other
    origin. After a gap in funding (see ``skipped_periods``), this is the period currently in progress, not the oldest
    period that was missed."""

    invoice_uid: OptionalNullable[str] = UNSET
    """The uid of the invoice that paid for this grant, for a grant with ``origin`` of ``purchase``. ``null`` for every
    other origin."""

    created_at: Optional[RFC3339DateTime] = UNSET


class WalletGrantDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    original: NotRequired[str]
    remaining: NotRequired[str]
    posted_remaining: NotRequired[str]
    expires_at: NotRequired[RFC3339DateTime | None]
    expires_on: NotRequired[Date | None]
    expired_at: NotRequired[RFC3339DateTime | None]
    expired_on: NotRequired[Date | None]
    origin: NotRequired[OriginOrStr]
    granted_for_period_start: NotRequired[RFC3339DateTime | None]
    invoice_uid: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
