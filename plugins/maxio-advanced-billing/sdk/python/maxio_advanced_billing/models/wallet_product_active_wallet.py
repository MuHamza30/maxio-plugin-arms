from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class WalletProductActiveWallet(SdkBaseModel):
    """One active wallet drawing on this Wallet Product."""

    id: Optional[int] = UNSET
    """The Advanced Billing id of the wallet."""

    subscription_id: Optional[int] = UNSET
    company_name: Optional[str] = UNSET
    """The owning customer's organization name, falling back to their full name, then to ``"Customer #<id>"``.
    ``"Customer"`` (with no id) when the wallet's subscription has no customer at all."""

    purchase_mechanism: OptionalNullable[str] = UNSET
    """See the same field on `Wallet Product Usage Template <$m/Wallet%20Product%20Usage%20Template>`__. The same
    caveats apply."""

    price_point_name: OptionalNullable[str] = UNSET
    currency: Optional[str] = UNSET
    active: Optional[bool] = UNSET
    """``false`` when the wallet's Feature is archived."""


class WalletProductActiveWalletDict(TypedDict):
    id: NotRequired[int]
    subscription_id: NotRequired[int]
    company_name: NotRequired[str]
    purchase_mechanism: NotRequired[str | None]
    price_point_name: NotRequired[str | None]
    currency: NotRequired[str]
    active: NotRequired[bool]
