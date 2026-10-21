from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .credit_card_attributes import CreditCardAttributes, CreditCardAttributesDict
from .subscription_custom_price import SubscriptionCustomPrice, SubscriptionCustomPriceDict
from .unions.net_terms1 import NetTerms1, NetTerms1Dict
from .unions.snap_day1 import SnapDay1, SnapDay1Dict
from .update_subscription_component import UpdateSubscriptionComponent, UpdateSubscriptionComponentDict


class UpdateSubscription(SdkBaseModel):
    credit_card_attributes: Optional[CreditCardAttributes] = UNSET
    product_handle: Optional[str] = UNSET
    """Set to the handle of a different product to change the subscription's product."""

    product_id: Optional[int] = UNSET
    """Set to the id of a different product to change the subscription's product."""

    product_change_delayed: Optional[bool] = UNSET
    next_product_id: Optional[str] = UNSET
    """Set to an empty string to cancel a delayed product change."""

    next_product_price_point_id: Optional[str] = UNSET
    snap_day: Optional[SnapDay1] = UNSET
    """A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'."""

    initial_billing_at: Optional[RFC3339DateTime] = UNSET
    """(Optional) Set this attribute to a future date/time to update a subscription in the Awaiting Signup Date state,
    to Awaiting Signup. In the Awaiting Signup state, a subscription behaves like any other. It can be canceled,
    allocated to, or have its billing date changed, etc. When the ``initial_billing_at`` date hits, the subscription
    will transition to the expected state. If the product has a trial, the subscription will enter a trial, otherwise it
    will go active. Setup fees will be respected either before or after the trial, as configured on the price point. If
    the payment is due at the initial_billing_at and it fails the subscription will be immediately canceled. You can
    omit the initial_billing_at date to activate the subscription immediately. See the `subscription import
    <https://maxio.zendesk.com/hc/en-us/articles/24251489107213-Advanced-Billing-Subscription-Imports#date-format>`__
    documentation for more information about Date/Time formats."""

    defer_signup: bool = False
    """(Optional) Set this attribute to true to move the subscription from Awaiting Signup, to Awaiting Signup Date. Use
    this when you want to update a subscription that has an unknown initial billing date. When the first billing date is
    known, update a subscription to set the ``initial_billing_at`` date. The subscription moves to the awaiting signup
    with a scheduled initial billing date. You can omit the initial_billing_at date to activate the subscription
    immediately. See `Subscription States
    <https://maxio-chargify.zendesk.com/hc/en-us/articles/5404222005773-Subscription-States>`__ for more information."""

    next_billing_at: Optional[RFC3339DateTime] = UNSET
    branding_theme_id: OptionalNullable[int] = UNSET
    """The ID of the Branding Theme to assign to this subscription. When set, this subscription-level Branding Theme is
    used instead of the customer's default Branding Theme for subscription-related documents and communications that use
    subscription theming. Pass null or an empty value to clear the subscription-level Branding Theme. Available only
    when Branding Themes are enabled for the site. Not returned in the response."""

    expires_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp giving the expiration date of this subscription (if any). You may manually change the expiration date
    at any point during a subscription period."""

    payment_collection_method: Optional[str] = UNSET
    receives_invoice_emails: Optional[bool] = UNSET
    net_terms: Optional[NetTerms1] = UNSET
    stored_credential_transaction_id: Optional[int] = UNSET
    reference: Optional[str] = UNSET
    custom_price: Optional[SubscriptionCustomPrice] = UNSET
    """(Optional) Used in place of ``product_price_point_id`` to define a custom price point unique to the subscription.
    A subscription can have up to 30 custom price points. Exceeding this limit will result in an API error."""

    components: Optional[list[UpdateSubscriptionComponent]] = UNSET
    """(Optional) An array of component ids and custom prices to be added to the subscription."""

    dunning_communication_delay_enabled: Optional[bool] = UNSET
    """Enable Communication Delay feature, making sure no communication (email or SMS) is sent to the Customer between
    9PM and 8AM in time zone set by the ``dunning_communication_delay_time_zone`` attribute."""

    dunning_communication_delay_time_zone: OptionalNullable[str] = UNSET
    """Time zone for the Dunning Communication Delay feature."""

    product_price_point_id: Optional[int] = UNSET
    """Set to change the current product's price point."""

    product_price_point_handle: Optional[str] = UNSET
    """Set to change the current product's price point."""


class UpdateSubscriptionDict(TypedDict):
    credit_card_attributes: NotRequired[CreditCardAttributesDict]
    product_handle: NotRequired[str]
    product_id: NotRequired[int]
    product_change_delayed: NotRequired[bool]
    next_product_id: NotRequired[str]
    next_product_price_point_id: NotRequired[str]
    snap_day: NotRequired[SnapDay1Dict]
    initial_billing_at: NotRequired[RFC3339DateTime]
    defer_signup: NotRequired[bool]
    next_billing_at: NotRequired[RFC3339DateTime]
    branding_theme_id: NotRequired[int | None]
    expires_at: NotRequired[RFC3339DateTime]
    payment_collection_method: NotRequired[str]
    receives_invoice_emails: NotRequired[bool]
    net_terms: NotRequired[NetTerms1Dict]
    stored_credential_transaction_id: NotRequired[int]
    reference: NotRequired[str]
    custom_price: NotRequired[SubscriptionCustomPriceDict]
    components: NotRequired[list[UpdateSubscriptionComponentDict]]
    dunning_communication_delay_enabled: NotRequired[bool]
    dunning_communication_delay_time_zone: NotRequired[str | None]
    product_price_point_id: NotRequired[int]
    product_price_point_handle: NotRequired[str]
