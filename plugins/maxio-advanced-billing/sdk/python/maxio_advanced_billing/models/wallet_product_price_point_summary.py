from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class WalletProductPricePointSummary(SdkBaseModel):
    """A summary of the Wallet Product's default price point, for rendering a catalog listing without a separate price
    points call."""

    archived_count: Optional[int] = UNSET
    """Number of archived price points on this Wallet Product."""

    pricing_scheme: OptionalNullable[str] = UNSET
    """The default price point's pricing scheme. ``null`` if the Wallet Product has no default price point."""

    tier_count: Optional[int] = UNSET
    """Number of price brackets on the default price point. A ``per_unit`` scheme always stores exactly one synthesized
    bracket, so this is ``1`` for ``per_unit``, not ``0``."""

    entry_price: OptionalNullable[str] = UNSET
    """The unit price of the default price point's first bracket, as a decimal string. ``null`` if there are no
    brackets."""

    final_price: OptionalNullable[str] = UNSET
    """The unit price of the default price point's last bracket, as a decimal string. ``null`` if there are no
    brackets."""


class WalletProductPricePointSummaryDict(TypedDict):
    archived_count: NotRequired[int]
    pricing_scheme: NotRequired[str | None]
    tier_count: NotRequired[int]
    entry_price: NotRequired[str | None]
    final_price: NotRequired[str | None]
