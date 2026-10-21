from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class WalletPurchase(SdkBaseModel):
    """A completed unit purchase."""

    id: int
    """The id of the grant this purchase created. When the wallet was overdrawn by at least the purchased quantity, the
    units repay the debt and the grant is still created, with ``remaining`` of ``0`` and ``original`` equal to the
    purchased quantity."""

    price_point_id: int
    """The price point the purchase was priced at."""

    invoice_uid: str
    """The uid of the invoice created to collect payment for this purchase."""

    quantity: str
    """The number of units purchased, as a decimal string."""

    expires_at: RFC3339DateTime | None
    """When the purchased units expire, following the funding entitlement's grant expiration policy. ``null`` when the
    wallet has no funding entitlement or its entitlements disagree on an expiration policy."""


class WalletPurchaseDict(TypedDict):
    id: int
    price_point_id: int
    invoice_uid: str
    quantity: str
    expires_at: RFC3339DateTime | None
