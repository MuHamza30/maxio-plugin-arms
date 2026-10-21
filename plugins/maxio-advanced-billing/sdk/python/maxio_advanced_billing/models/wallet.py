from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.owner_type import OwnerTypeOrStr
from .enums.wallet_hard_stop_overflow import WalletHardStopOverflowOrStr
from .enums.wallet_origin import WalletOriginOrStr
from .enums.wallet_status import WalletStatusOrStr
from .meter import Meter, MeterDict
from .wallet_grant import WalletGrant, WalletGrantDict
from .wallet_recurring_funding import WalletRecurringFunding, WalletRecurringFundingDict


class Wallet(SdkBaseModel):
    """A balance, denominated in the unit of a Wallet Product, owned by a subscription. Grants and recurring funding
    schedules are embedded so a single read shows the full balance breakdown."""

    id: Optional[int] = UNSET
    """The Advanced Billing id of the wallet."""

    owner_type: Optional[OwnerTypeOrStr] = UNSET
    """The polymorphic owner type. ``subscription`` is the only value currently supported."""

    owner_id: Optional[int] = UNSET
    """The id of the owning subscription."""

    name: OptionalNullable[str] = UNSET
    """(Optional) A merchant-facing label for the wallet, set on create and changeable with `Update Wallet
    <$e/Wallets/updateWallet>`__. Surrounding spaces are stripped; a blank value is stored as ``null``."""

    wallet_product_id: Optional[int] = UNSET
    """The id of the `Wallet Product <$e/Wallet%20Products/createWalletProduct>`__ that denominates the wallet.
    Immutable for the life of the wallet."""

    wallet_product_name: Optional[str] = UNSET
    """The name of the Wallet Product that denominates the wallet."""

    unit: Optional[str] = UNSET
    """The billing product's unit name, immutable for the life of the wallet."""

    price_point_id: OptionalNullable[int] = UNSET
    """The price point that priced this wallet's `purchases <$e/Wallet%20Purchases/createWalletPurchase>`__, set on
    create and immutable afterward. Defaults to the Wallet Product's default price point; ``null`` if the Wallet Product
    has none and none was given on create."""

    balance: Optional[str] = UNSET
    """What the wallet can spend now, encoded as a decimal string to avoid floating-point precision loss. This is the
    number to enforce against. For a metered wallet, it includes usage not yet posted to the ledger, through
    ``metered_through_at``, but only in the response from `Read Wallet <$e/Wallets/readWallet>`__; every other response
    (list, create, update, archive) reports the balance as of the last ledger write, equal to ``posted_balance``, even
    for a metered wallet. The grants' ``remaining`` follow this figure, so they add up to it whenever it is zero or
    more."""

    posted_balance: Optional[str] = UNSET
    """The balance from written ledger entries alone: grants funded, minus debits written to the ledger, as a decimal
    string. Always present, also for a wallet with no meter. It equals ``balance`` wherever no live metered balance is
    computed: list, create, update, and archive responses, an unlinked or archived wallet, and a read where
    ``metered_stale`` is ``true``. Only an active, metered wallet read through `Read Wallet <$e/Wallets/readWallet>`__,
    with ``metered_stale`` not ``true``, can have a ``balance`` below its ``posted_balance``. It stays exact when
    ``metered_stale`` is ``true``. Reconcile the transactions list (``balance_after``) against this figure, not against
    ``balance``."""

    meter: OptionalNullable[Meter] = UNSET
    """The metering meter this wallet is paired with, or ``null`` for a wallet with no meter. Set on create and
    immutable afterward."""

    metered_through_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The point up to which live meter usage has been factored into ``balance``. Populated only in the response from
    `Read Wallet <$e/Wallets/readWallet>`__, for an active, metered wallet on a site with metered consumption enabled;
    ``null`` everywhere else, including list, create, update, and archive responses for the same wallet."""

    metered_recheck_after_seconds: OptionalNullable[int] = UNSET
    """How many seconds to wait before re-reading ``balance`` to see usage past ``metered_through_at``. Same
    availability as ``metered_through_at``."""

    metered_stale: OptionalNullable[bool] = UNSET
    """``true`` when live usage could not be read fresh and ``balance`` reflects an earlier snapshot. Same availability
    as ``metered_through_at``."""

    status: Optional[WalletStatusOrStr] = UNSET
    depletion_policy: Optional[str] = UNSET
    """What happens when a debit would take the wallet below zero. Known values: ``hard_stop`` (the only value you can
    set today). More values are expected over time, so treat this as an open string and don't fail on one you don't
    recognize. At the zero boundary, ``hard_stop`` behaves as set by ``hard_stop_overflow``."""

    hard_stop_overflow: Optional[WalletHardStopOverflowOrStr] = UNSET
    """Behavior at the hard-stop boundary. ``discard`` drains the wallet to zero and rejects the excess (the default).
    ``allow_negative`` deducts the full amount, letting the balance go negative. The excess past the wallet's grants is
    booked as an overdraft ledger row with ``grant_id`` set to ``null``."""

    origin: Optional[WalletOriginOrStr] = UNSET
    """How the wallet came to exist. ``manual`` for a wallet created directly with `Create Wallet
    <$e/Wallets/createWallet>`__. ``feature`` for a wallet auto-provisioned because a subscription resolved a
    usage-limit entitlement whose Feature has ``wallet_behavior`` configured."""

    feature_key: OptionalNullable[str] = UNSET
    """The key of the Feature this wallet was provisioned for, when ``origin`` is ``feature``. ``null`` for a ``manual``
    wallet."""

    grants: Optional[list[WalletGrant]] = UNSET
    """Every grant on the wallet, including ones already spent or expired, in drain order (the order debits would
    consume the still-open ones in): the soonest-expiring grant first, evergreen grants last."""

    recurring_funding: Optional[list[WalletRecurringFunding]] = UNSET
    """The wallet's automatic funding schedules, if any. Empty for a ``manual`` wallet with no funding entitlement. A
    wallet funds automatically when it's provisioned from a Feature with ``wallet_behavior`` configured; see `the
    Wallets concept guide <page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-feature>`__."""

    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET


class WalletDict(TypedDict):
    id: NotRequired[int]
    owner_type: NotRequired[OwnerTypeOrStr]
    owner_id: NotRequired[int]
    name: NotRequired[str | None]
    wallet_product_id: NotRequired[int]
    wallet_product_name: NotRequired[str]
    unit: NotRequired[str]
    price_point_id: NotRequired[int | None]
    balance: NotRequired[str]
    posted_balance: NotRequired[str]
    meter: NotRequired[MeterDict | None]
    metered_through_at: NotRequired[RFC3339DateTime | None]
    metered_recheck_after_seconds: NotRequired[int | None]
    metered_stale: NotRequired[bool | None]
    status: NotRequired[WalletStatusOrStr]
    depletion_policy: NotRequired[str]
    hard_stop_overflow: NotRequired[WalletHardStopOverflowOrStr]
    origin: NotRequired[WalletOriginOrStr]
    feature_key: NotRequired[str | None]
    grants: NotRequired[list[WalletGrantDict]]
    recurring_funding: NotRequired[list[WalletRecurringFundingDict]]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
