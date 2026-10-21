from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.wallet_hard_stop_overflow import WalletHardStopOverflowOrStr
from .unions.conversion_rate import ConversionRate, ConversionRateDict
from .unions.initial_balance import InitialBalance, InitialBalanceDict
from .unions.wallet_product_id import WalletProductId, WalletProductIdDict


class Wallet1(SdkBaseModel):
    subscription_id: int
    """The subscription that will own the wallet."""

    wallet_product_id: WalletProductId
    """The `Wallet Product <$e/Wallet%20Products/createWalletProduct>`__ that will denominate the wallet: its numeric
    id, or its handle prefixed with ``handle:`` (for example ``handle:token-pack``). A bare handle with no prefix is
    looked up as an id and returns ``404``. Immutable once the wallet is created."""

    name: OptionalNullable[str] = UNSET
    """(Optional) A merchant-facing label for the wallet. Surrounding spaces are stripped; a blank value is stored as
    ``null``."""

    depletion_policy: Optional[str] = UNSET
    """Defaults to ``hard_stop``, currently the only supported value."""

    hard_stop_overflow: Optional[WalletHardStopOverflowOrStr] = UNSET
    """Defaults to ``discard``."""

    meter_id: Optional[int] = UNSET
    """Pairs the wallet with a merchant-owned metering meter, so its balance factors in live usage (see the wallet
    resource's ``meter`` and ``metered_through_at`` fields). Only a ``sum`` or ``count`` meter can be paired. Requires
    metered wallet consumption to be enabled for the site, checked whenever this or ``conversion_rate`` is sent: ``403``
    (plain text, not JSON) if it isn't. A meter id that doesn't resolve to a merchant-owned meter on this site,
    including a system-maintained shadow meter, is ``404``. Immutable once the wallet is created."""

    conversion_rate: Optional[ConversionRate] = UNSET
    """How many wallet units one meter unit is worth, as a decimal string with at most 8 fractional digits, greater than
    ``0`` and below 10^16. Send fractional values as strings: a JSON number with a decimal point is rejected with
    ``422``, because a double-precision float may already have lost precision before the request arrives. Only
    meaningful with ``meter_id``. Defaults to ``"1.0"``. Immutable once the wallet is created."""

    price_point_id: Optional[int] = UNSET
    """The price point used to price `Create Wallet Purchase <$e/Wallet%20Purchases/createWalletPurchase>`__ calls
    against this wallet. Must belong to the Wallet Product, and can't be archived or a subscription-specific custom
    price point. Defaults to the Wallet Product's default price point. Immutable once the wallet is created."""

    initial_balance: Optional[InitialBalance] = UNSET
    """(Optional) A free opening balance, not a purchase and not reflected on any invoice. When non-zero, wallet
    creation also writes an initial-balance grant and a matching ``initial_balance`` ledger row. Omitted or exactly
    ``0`` creates a zero-balance wallet, not an error. Encoded as a decimal string with at most 8 fractional digits, and
    must be non-negative and below 10^16. Send fractional values as strings: a JSON number with a decimal point is
    rejected with ``422``, because a double-precision float may already have lost precision before the request
    arrives."""

    initial_balance_expires_at: OptionalNullable[str] = UNSET
    """An expiration for the initial-balance grant. Only accepted together with a non-zero ``initial_balance``, and must
    be in the future. Accepts either a bare calendar date (``YYYY-MM-DD``), resolved to the end of that day in the
    site's time zone, or a full timestamp. A calendar day that doesn't exist, such as ``2027-02-30``, is rejected with
    ``422`` rather than rolled into the next month."""


class Wallet1Dict(TypedDict):
    subscription_id: int
    wallet_product_id: WalletProductIdDict
    name: NotRequired[str | None]
    depletion_policy: NotRequired[str]
    hard_stop_overflow: NotRequired[WalletHardStopOverflowOrStr]
    meter_id: NotRequired[int]
    conversion_rate: NotRequired[ConversionRateDict]
    price_point_id: NotRequired[int]
    initial_balance: NotRequired[InitialBalanceDict]
    initial_balance_expires_at: NotRequired[str | None]
