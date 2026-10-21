from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.expiration_interval_unit import ExpirationIntervalUnitOrStr
from .enums.interval_unit import IntervalUnitOrStr
from .enums.trial_type import TrialTypeOrStr


class CreateOrUpdateProduct(SdkBaseModel):
    name: str
    """The product name"""

    handle: Optional[str] = UNSET
    """The product API handle"""

    description: str
    """The product description"""

    accounting_code: Optional[str] = UNSET
    """E.g. Internal ID or SKU Number"""

    require_credit_card: Optional[bool] = UNSET
    """Deprecated value that can be ignored unless you have legacy hosted pages. For Public Signup Page users, read this
    attribute from under the signup page."""

    price_in_cents: int
    """The product price, in integer cents"""

    interval: int
    """The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this product
    would renew every 30 days."""

    interval_unit: IntervalUnitOrStr
    """A string representing the interval unit for this product, either month or day"""

    trial_price_in_cents: Optional[int] = UNSET
    """The product trial price, in integer cents"""

    trial_interval: Optional[int] = UNSET
    """The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of day would mean this
    product trial would last 30 days."""

    trial_interval_unit: OptionalNullable[IntervalUnitOrStr] = UNSET
    """A string representing the trial interval unit for this product, either month or day"""

    trial_type: OptionalNullable[TrialTypeOrStr] = UNSET
    """Indicates how a trial is handled when the trial period ends and there is no credit card on file. For
    ``no_obligation``, the subscription transitions to a Trial Ended state. Maxio will not send any emails or
    statements. For ``payment_expected``, the subscription transitions to a Past Due state. Maxio will send normal
    dunning emails and statements according to your other settings."""

    expiration_interval: Optional[int] = UNSET
    """The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an expiration_interval_unit
    of day would mean this product would expire after 30 days."""

    expiration_interval_unit: OptionalNullable[ExpirationIntervalUnitOrStr] = UNSET
    """A string representing the expiration interval unit for this product, either month, day or never"""

    auto_create_signup_page: Optional[bool] = UNSET
    tax_code: Optional[str] = UNSET
    """A string representing the tax code related to the product type. This is especially important when using AvaTax to
    tax based on locale. This attribute has a max length of 25 characters."""

    unspsc_code: OptionalNullable[str] = UNSET
    """(Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the
    commodity code on invoice line items for this product instead of the default derived from item_category."""


class CreateOrUpdateProductDict(TypedDict):
    name: str
    handle: NotRequired[str]
    description: str
    accounting_code: NotRequired[str]
    require_credit_card: NotRequired[bool]
    price_in_cents: int
    interval: int
    interval_unit: IntervalUnitOrStr
    trial_price_in_cents: NotRequired[int]
    trial_interval: NotRequired[int]
    trial_interval_unit: NotRequired[IntervalUnitOrStr | None]
    trial_type: NotRequired[TrialTypeOrStr | None]
    expiration_interval: NotRequired[int]
    expiration_interval_unit: NotRequired[ExpirationIntervalUnitOrStr | None]
    auto_create_signup_page: NotRequired[bool]
    tax_code: NotRequired[str]
    unspsc_code: NotRequired[str | None]
