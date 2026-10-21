from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .calendar_billing import CalendarBilling, CalendarBillingDict
from .subscription_custom_price import SubscriptionCustomPrice, SubscriptionCustomPriceDict
from .subscription_group_signup_component import SubscriptionGroupSignupComponent, SubscriptionGroupSignupComponentDict


class SubscriptionGroupSignupItem(SdkBaseModel):
    product_handle: Optional[str] = UNSET
    """The API Handle of the product for which you are creating a subscription. Required, unless a ``product_id`` is
    given instead."""

    product_id: Optional[int] = UNSET
    """The Product ID of the product for which you are creating a subscription. You can pass either ``product_id`` or
    ``product_handle``."""

    product_price_point_id: Optional[int] = UNSET
    """The ID of the particular price point on the product."""

    product_price_point_handle: Optional[str] = UNSET
    """The user-friendly API handle of a product's particular price point."""

    offer_id: Optional[int] = UNSET
    """Use in place of passing product and component information to set up the subscription with an existing offer. May
    be either the Chargify ID of the offer or its handle prefixed with ``handle:``."""

    reference: Optional[str] = UNSET
    """The reference value (provided by your app) for the subscription itself."""

    primary: Optional[bool] = UNSET
    """One of the subscriptions must be marked as primary in the group."""

    currency: Optional[str] = UNSET
    """(Optional) If Multi-Currency is enabled and the currency is configured in Chargify, pass it at signup to create a
    subscription on a non-default currency. Note that you cannot update the currency of an existing subscription."""

    coupon_codes: Optional[list[str]] = UNSET
    """An array for all the coupons attached to the subscription."""

    components: Optional[list[SubscriptionGroupSignupComponent]] = UNSET
    custom_price: Optional[SubscriptionCustomPrice] = UNSET
    """(Optional) Used in place of ``product_price_point_id`` to define a custom price point unique to the subscription.
    A subscription can have up to 30 custom price points. Exceeding this limit will result in an API error."""

    calendar_billing: Optional[CalendarBilling] = UNSET
    """(Optional). Cannot be used when also specifying next_billing_at."""

    metafields: Optional[dict[str, str]] = UNSET
    """(Optional) A set of key/value pairs representing custom fields and their values. Metafields will be created
    “on-the-fly” in your site for a given key, if they have not been created yet."""


class SubscriptionGroupSignupItemDict(TypedDict):
    product_handle: NotRequired[str]
    product_id: NotRequired[int]
    product_price_point_id: NotRequired[int]
    product_price_point_handle: NotRequired[str]
    offer_id: NotRequired[int]
    reference: NotRequired[str]
    primary: NotRequired[bool]
    currency: NotRequired[str]
    coupon_codes: NotRequired[list[str]]
    components: NotRequired[list[SubscriptionGroupSignupComponentDict]]
    custom_price: NotRequired[SubscriptionCustomPriceDict]
    calendar_billing: NotRequired[CalendarBillingDict]
    metafields: NotRequired[dict[str, str]]
