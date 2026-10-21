from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .bank_account_payment_profile import BankAccountPaymentProfile, BankAccountPaymentProfileDict
from .credit_card_payment_profile import CreditCardPaymentProfile, CreditCardPaymentProfileDict
from .customer import Customer, CustomerDict
from .enums.cancellation_method import CancellationMethodOrStr
from .enums.collection_method import CollectionMethodOrStr
from .enums.price_point_type import PricePointTypeOrStr
from .enums.subscription_state import SubscriptionStateOrStr
from .nested_subscription_group import NestedSubscriptionGroup, NestedSubscriptionGroupDict
from .prepaid_configuration import PrepaidConfiguration, PrepaidConfigurationDict
from .product import Product, ProductDict
from .subscription_included_coupon import SubscriptionIncludedCoupon, SubscriptionIncludedCouponDict


class Subscription(SdkBaseModel):
    id: Optional[int] = UNSET
    """The subscription unique id within Chargify."""

    state: Optional[SubscriptionStateOrStr] = UNSET
    """The state of a subscription.
    * **Live States**
        * ``active`` - A normal, active subscription. It is not in a trial and is paid and up to date.
        * ``assessing`` - An internal (transient) state that indicates a subscription is in the middle of periodic
            assessment. Do not base any access decisions in your app on this state, as it may not always be exposed.
        * ``pending`` - An internal (transient) state that indicates a subscription is in the creation process. Do not
            base any access decisions in your app on this state, as it may not always be exposed.
        * ``trialing`` - A subscription in trialing state has a valid trial subscription. This type of subscription may
            transition to active once payment is received when the trial has ended. Otherwise, it may go to a Problem or
            End of Life state.
        * ``paused`` - An internal state that indicates that your account with Advanced Billing is in arrears.
    * **Problem States**
        * ``past_due`` - Indicates that the most recent payment has failed, and payment is past due for this
            subscription. If you have enabled our automated dunning, this subscription will be in the dunning process
            (additional status and callbacks from the dunning process will be available in the future). If you are
            handling dunning and payment updates yourself, you will want to use this state to initiate a payment update
            from your customers.
        * ``soft_failure`` - Indicates that normal assessment/processing of the subscription has failed for a reason
            that cannot be fixed by the Customer. For example, a Soft Fail may result from a timeout at the gateway or
            incorrect credentials on your part. The subscriptions should be retried automatically. An interface is being
            built for you to review problems resulting from these events to take manual action when needed.
        * ``unpaid`` - Indicates an unpaid subscription. A subscription is marked unpaid if the retry period expires and
            you have configured your `Dunning
            <https://maxio.zendesk.com/hc/en-us/articles/24287076583565-Dunning-Overview>`__ settings to have a Final
            Action of ``mark the subscription unpaid``.
    * **End of Life States**
        * ``canceled`` - Indicates a canceled subscription. This may happen at your request (via the API or the web
            interface) or due to the expiration of the `Dunning
            <https://maxio.zendesk.com/hc/en-us/articles/24287076583565-Dunning-Overview>`__ process without payment.
            See the `Reactivation
            <https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming>`__ documentation for
            info on how to restart a canceled subscription.
        While a subscription is canceled, its period will not advance, it will not accrue any new charges, and Advanced
        Billing will not attempt to collect the overdue balance.
        * ``expired`` - Indicates a subscription that has expired due to running its normal life cycle. Some products
            may be configured to have an expiration period. An expired subscription then is one that stayed active until
            it fulfilled its full period.
        * ``failed_to_create`` - Indicates that signup has failed. (You may see this state in a signup_failure webhook.)
        * ``on_hold`` - Indicates that a subscription’s billing has been temporarily stopped. While it is expected that
            the subscription will resume and return to active status, this is still treated as an “End of Life” state
            because the customer is not paying for services during this time.
        * ``suspended`` - Indicates that a prepaid subscription has used up all their prepayment balance. If a
            prepayment is applied, it will return to an active state.
        * ``trial_ended`` - A subscription in a trial_ended state is a subscription that completed a no-obligation trial
            and did not have a card on file at the expiration of the trial period. See `Product Pricing – No Obligation
            Trials <https://maxio.zendesk.com/hc/en-us/articles/24261076617869-Product-Editing>`__ for more details.

    See `Subscription States <https://maxio.zendesk.com/hc/en-us/articles/24252119027853-Subscription-States>`__ for
    more info about subscription states and state transitions."""

    balance_in_cents: Optional[int] = UNSET
    """Gives the current outstanding subscription balance in the number of cents."""

    total_revenue_in_cents: Optional[int] = UNSET
    """Gives the total revenue from the subscription in the number of cents."""

    product_price_in_cents: Optional[int] = UNSET
    """(Added Nov 5 2013) The recurring amount of the product (and version), currently subscribed. NOTE: this may differ
    from the current price of the product, if you’ve changed the price of the product but haven’t moved this
    subscription to a newer version."""

    product_version_number: Optional[int] = UNSET
    """The version of the product for the subscription. Note that this is a deprecated field kept for
    backwards-compatibility."""

    current_period_ends_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp relating to the end of the current (recurring) period (i.e., when the next regularly scheduled
    attempted charge will occur)"""

    next_assessment_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp that indicates when capture of payment will be tried or retried. This value will usually track the
    current_period_ends_at, but will diverge if a renewal payment fails and must be retried. In that case, the
    current_period_ends_at will advance to the end of the next period (time doesn’t stop because a payment was missed)
    but the next_assessment_at will be scheduled for the auto-retry time (e.g., 24 hours in the future, in some
    cases)."""

    trial_started_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp for when the trial period (if any) began"""

    trial_ended_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp for when the trial period (if any) ended"""

    activated_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp for when the subscription began (i.e., when it came out of trial, or when it began in the case of no
    trial)"""

    expires_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp giving the expiration date of this subscription (if any)"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """The creation date for this subscription"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """The date of last update for this subscription"""

    cancellation_message: OptionalNullable[str] = UNSET
    """Seller-provided reason for, or note about, the cancellation."""

    cancellation_method: OptionalNullable[CancellationMethodOrStr] = UNSET
    """The process used to cancel the subscription, if the subscription has been canceled. It is nil if the
    subscription's state is not canceled."""

    cancel_at_end_of_period: OptionalNullable[bool] = UNSET
    """Whether or not the subscription will (or has) canceled at the end of the period."""

    canceled_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp of the most recent cancellation"""

    current_period_started_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp relating to the start of the current (recurring) period"""

    previous_state: Optional[SubscriptionStateOrStr] = UNSET
    """Only valid for webhook payloads The previous state for webhooks that have indicated a change in state. For normal
    API calls, this will always be the same as the state (current state)."""

    signup_payment_id: Optional[int] = UNSET
    """The ID of the transaction that generated the revenue"""

    signup_revenue: Optional[str] = UNSET
    """The revenue, formatted as a string of decimal separated dollars and cents, from the subscription signup ($50.00
    would be formatted as 50.00)"""

    delayed_cancel_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp for when the subscription is currently set to cancel."""

    coupon_code: OptionalNullable[str] = UNSET
    """(deprecated) The coupon code of the single coupon currently applied to the subscription. See coupon_codes instead
    as subscriptions can now have more than one coupon."""

    snap_day: OptionalNullable[str] = UNSET
    """A day of month that subscription will be processed on. Can be 1 up to 28 or 'end'."""

    payment_collection_method: Optional[CollectionMethodOrStr] = UNSET
    """The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options
    are - ``invoice``, ``automatic``. For current Relationship Invoicing Architecture valid options are -
    ``remittance``, ``automatic``, ``prepaid``."""

    customer: Optional[Customer] = UNSET
    product: Optional[Product] = UNSET
    credit_card: Optional[CreditCardPaymentProfile] = UNSET
    group: OptionalNullable[NestedSubscriptionGroup] = UNSET
    bank_account: Optional[BankAccountPaymentProfile] = UNSET
    payment_type: OptionalNullable[str] = UNSET
    """The payment profile type for the active profile on file."""

    referral_code: OptionalNullable[str] = UNSET
    """The subscription's unique code that can be given to referrals."""

    next_product_id: OptionalNullable[int] = UNSET
    """If a delayed product change is scheduled, the ID of the product that the subscription will be changed to at the
    next renewal."""

    next_product_handle: OptionalNullable[str] = UNSET
    """If a delayed product change is scheduled, the handle of the product that the subscription will be changed to at
    the next renewal."""

    coupon_use_count: OptionalNullable[int] = UNSET
    """(deprecated) How many times the subscription's single coupon has been used. This field has no replacement for
    multiple coupons."""

    coupon_uses_allowed: OptionalNullable[int] = UNSET
    """(deprecated) How many times the subscription's single coupon may be used. This field has no replacement for
    multiple coupons."""

    reason_code: OptionalNullable[str] = UNSET
    """The churn reason code associated to a canceled subscription."""

    automatically_resume_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The date the subscription is scheduled to automatically resume from the on_hold state."""

    coupon_codes: Optional[list[str]] = UNSET
    """An array for all the coupons attached to the subscription."""

    offer_id: OptionalNullable[int] = UNSET
    """The ID of the offer associated with the subscription."""

    payer_id: OptionalNullable[int] = UNSET
    """On Relationship Invoicing, the ID of the individual paying for the subscription. Defaults to the Customer ID
    unless the 'Customer Hierarchies & WhoPays' feature is enabled."""

    current_billing_amount_in_cents: Optional[int] = UNSET
    """The balance in cents plus the estimated renewal amount in cents. Returned ONLY for the readSubscription operation
    as it's a compute intensive operation."""

    product_price_point_id: Optional[int] = UNSET
    """The product price point currently subscribed to."""

    product_price_point_type: Optional[PricePointTypeOrStr] = UNSET
    """Price point type. We expose the following types:
    1. **default**: a price point that is marked as a default price for a certain product.
    2. **custom**: a custom price point.
    3. **catalog**: a price point that is **not** marked as a default price for a certain product and is **not** a
        custom one."""

    next_product_price_point_id: OptionalNullable[int] = UNSET
    """If a delayed product change is scheduled, the ID of the product price point that the subscription will be changed
    to at the next renewal."""

    net_terms: OptionalNullable[int] = UNSET
    """On Relationship Invoicing, the number of days before a renewal invoice is due."""

    stored_credential_transaction_id: OptionalNullable[int] = UNSET
    """For European sites subject to PSD2 and using 3D Secure, this can be used to reference a previous transaction for
    the customer. This will ensure the card will be charged successfully at renewal."""

    reference: OptionalNullable[str] = UNSET
    """The reference value (provided by your app) for the subscription itself."""

    on_hold_at: OptionalNullable[RFC3339DateTime] = UNSET
    """The timestamp of the most recent on hold action."""

    prepaid_dunning: Optional[bool] = UNSET
    """Boolean representing whether the subscription is prepaid and currently in dunning. Only returned for Relationship
    Invoicing sites with the feature enabled."""

    coupons: Optional[list[SubscriptionIncludedCoupon]] = UNSET
    """Additional coupon data. To use this data you also have to include the following param in the request:
    ``include[]=coupons``. Only in Read Subscription Endpoint."""

    dunning_communication_delay_enabled: Optional[bool] = UNSET
    """Enable Communication Delay feature, making sure no communication (email or SMS) is sent to the Customer between
    9PM and 8AM in time zone set by the ``dunning_communication_delay_time_zone`` attribute."""

    dunning_communication_delay_time_zone: OptionalNullable[str] = UNSET
    """Time zone for the Dunning Communication Delay feature."""

    receives_invoice_emails: OptionalNullable[bool] = UNSET
    locale: OptionalNullable[str] = UNSET
    currency: Optional[str] = UNSET
    scheduled_cancellation_at: OptionalNullable[RFC3339DateTime] = UNSET
    credit_balance_in_cents: Optional[int] = UNSET
    prepayment_balance_in_cents: Optional[int] = UNSET
    prepaid_configuration: OptionalNullable[PrepaidConfiguration] = UNSET
    self_service_page_token: Optional[str] = UNSET
    """Returned only for list/read Subscription operation when ``include[]=self_service_page_token`` parameter is
    provided."""


class SubscriptionDict(TypedDict):
    id: NotRequired[int]
    state: NotRequired[SubscriptionStateOrStr]
    balance_in_cents: NotRequired[int]
    total_revenue_in_cents: NotRequired[int]
    product_price_in_cents: NotRequired[int]
    product_version_number: NotRequired[int]
    current_period_ends_at: NotRequired[RFC3339DateTime | None]
    next_assessment_at: NotRequired[RFC3339DateTime | None]
    trial_started_at: NotRequired[RFC3339DateTime | None]
    trial_ended_at: NotRequired[RFC3339DateTime | None]
    activated_at: NotRequired[RFC3339DateTime | None]
    expires_at: NotRequired[RFC3339DateTime | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    cancellation_message: NotRequired[str | None]
    cancellation_method: NotRequired[CancellationMethodOrStr | None]
    cancel_at_end_of_period: NotRequired[bool | None]
    canceled_at: NotRequired[RFC3339DateTime | None]
    current_period_started_at: NotRequired[RFC3339DateTime | None]
    previous_state: NotRequired[SubscriptionStateOrStr]
    signup_payment_id: NotRequired[int]
    signup_revenue: NotRequired[str]
    delayed_cancel_at: NotRequired[RFC3339DateTime | None]
    coupon_code: NotRequired[str | None]
    snap_day: NotRequired[str | None]
    payment_collection_method: NotRequired[CollectionMethodOrStr]
    customer: NotRequired[CustomerDict]
    product: NotRequired[ProductDict]
    credit_card: NotRequired[CreditCardPaymentProfileDict]
    group: NotRequired[NestedSubscriptionGroupDict | None]
    bank_account: NotRequired[BankAccountPaymentProfileDict]
    payment_type: NotRequired[str | None]
    referral_code: NotRequired[str | None]
    next_product_id: NotRequired[int | None]
    next_product_handle: NotRequired[str | None]
    coupon_use_count: NotRequired[int | None]
    coupon_uses_allowed: NotRequired[int | None]
    reason_code: NotRequired[str | None]
    automatically_resume_at: NotRequired[RFC3339DateTime | None]
    coupon_codes: NotRequired[list[str]]
    offer_id: NotRequired[int | None]
    payer_id: NotRequired[int | None]
    current_billing_amount_in_cents: NotRequired[int]
    product_price_point_id: NotRequired[int]
    product_price_point_type: NotRequired[PricePointTypeOrStr]
    next_product_price_point_id: NotRequired[int | None]
    net_terms: NotRequired[int | None]
    stored_credential_transaction_id: NotRequired[int | None]
    reference: NotRequired[str | None]
    on_hold_at: NotRequired[RFC3339DateTime | None]
    prepaid_dunning: NotRequired[bool]
    coupons: NotRequired[list[SubscriptionIncludedCouponDict]]
    dunning_communication_delay_enabled: NotRequired[bool]
    dunning_communication_delay_time_zone: NotRequired[str | None]
    receives_invoice_emails: NotRequired[bool | None]
    locale: NotRequired[str | None]
    currency: NotRequired[str]
    scheduled_cancellation_at: NotRequired[RFC3339DateTime | None]
    credit_balance_in_cents: NotRequired[int]
    prepayment_balance_in_cents: NotRequired[int]
    prepaid_configuration: NotRequired[PrepaidConfigurationDict | None]
    self_service_page_token: NotRequired[str]
