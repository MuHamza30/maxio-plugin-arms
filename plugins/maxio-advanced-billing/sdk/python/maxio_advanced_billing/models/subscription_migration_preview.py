from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionMigrationPreview(SdkBaseModel):
    prorated_adjustment_in_cents: Optional[int] = UNSET
    """The amount of the prorated adjustment that would be issued for the current subscription."""

    charge_in_cents: Optional[int] = UNSET
    """The amount of the charge that would be created for the new product."""

    payment_due_in_cents: Optional[int] = UNSET
    """The amount of the payment due in the case of an upgrade."""

    credit_applied_in_cents: Optional[int] = UNSET
    """Represents a credit in cents that is applied to your subscription as part of a migration process for a specific
    product, which reduces the amount owed for the subscription."""


class SubscriptionMigrationPreviewDict(TypedDict):
    prorated_adjustment_in_cents: NotRequired[int]
    charge_in_cents: NotRequired[int]
    payment_due_in_cents: NotRequired[int]
    credit_applied_in_cents: NotRequired[int]
