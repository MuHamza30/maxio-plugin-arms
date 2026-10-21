from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class WalletProductUsageTemplate(SdkBaseModel):
    """One wallet template billing through this Wallet Product, joined to the Feature and plan/component that assigns
    it, when there is one."""

    plan_name: OptionalNullable[str] = UNSET
    """The name of the product or component the Feature is assigned to. ``null`` when the wallet template has no
    assigning Feature."""

    wallet_template_name: OptionalNullable[str] = UNSET
    """The label set in ``wallet_behavior.name`` on the Feature, or the standalone wallet's own ``name``."""

    unit_name: Optional[str] = UNSET
    purchase_mechanism: OptionalNullable[str] = UNSET
    """A best-effort label for how this wallet is expected to be replenished. Currently reports ``"Overage"`` when the
    wallet template allows a negative balance, and ``null`` otherwise; there's no persisted field yet distinguishing,
    for example, an intended "Auto top-up" from "Purchase more" setup. Treat this as informational, not a stable
    enum."""

    price_point_name: OptionalNullable[str] = UNSET
    currency: Optional[str] = UNSET
    active: Optional[bool] = UNSET
    """``false`` when the assigning Feature is archived."""

    feature_template_id: OptionalNullable[int] = UNSET
    feature_template_name: OptionalNullable[str] = UNSET
    price_point_override: Optional[bool] = UNSET
    """``true`` when this wallet template is priced at a price point other than the Wallet Product's default."""


class WalletProductUsageTemplateDict(TypedDict):
    plan_name: NotRequired[str | None]
    wallet_template_name: NotRequired[str | None]
    unit_name: NotRequired[str]
    purchase_mechanism: NotRequired[str | None]
    price_point_name: NotRequired[str | None]
    currency: NotRequired[str]
    active: NotRequired[bool]
    feature_template_id: NotRequired[int | None]
    feature_template_name: NotRequired[str | None]
    price_point_override: NotRequired[bool]
