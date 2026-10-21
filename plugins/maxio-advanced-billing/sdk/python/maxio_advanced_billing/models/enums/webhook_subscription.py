from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookSubscription(str, Enum):
    BILLING_DATE_CHANGE = "billing_date_change"
    COMPONENT_ALLOCATION_CHANGE = "component_allocation_change"
    CHJS_TOKENIZATION_FAILURE = "chjs_tokenization_failure"
    CHJS_TOKENIZATION_SUCCESS = "chjs_tokenization_success"
    CUSTOMER_CREATE = "customer_create"
    CUSTOMER_UPDATE = "customer_update"
    DUNNING_STEP_REACHED = "dunning_step_reached"
    EXPIRING_CARD = "expiring_card"
    EXPIRATION_DATE_CHANGE = "expiration_date_change"
    INVOICE_ISSUED = "invoice_issued"
    INVOICE_PENDING = "invoice_pending"
    METERED_USAGE = "metered_usage"
    PAYMENT_FAILURE = "payment_failure"
    PAYMENT_SUCCESS = "payment_success"
    DIRECT_DEBIT_PAYMENT_PENDING = "direct_debit_payment_pending"
    DIRECT_DEBIT_PAYMENT_PAID_OUT = "direct_debit_payment_paid_out"
    DIRECT_DEBIT_PAYMENT_REJECTED = "direct_debit_payment_rejected"
    PREPAID_SUBSCRIPTION_BALANCE_CHANGED = "prepaid_subscription_balance_changed"
    PREPAID_USAGE = "prepaid_usage"
    REFUND_FAILURE = "refund_failure"
    REFUND_SUCCESS = "refund_success"
    RENEWAL_FAILURE = "renewal_failure"
    RENEWAL_SUCCESS = "renewal_success"
    SIGNUP_FAILURE = "signup_failure"
    SIGNUP_SUCCESS = "signup_success"
    STATEMENT_CLOSED = "statement_closed"
    STATEMENT_SETTLED = "statement_settled"
    SUBSCRIPTION_CARD_UPDATE = "subscription_card_update"
    SUBSCRIPTION_GROUP_CARD_UPDATE = "subscription_group_card_update"
    SUBSCRIPTION_PRODUCT_CHANGE = "subscription_product_change"
    SUBSCRIPTION_PRODUCT_CHANGE_SCHEDULED = "subscription_product_change_scheduled"
    SUBSCRIPTION_STATE_CHANGE = "subscription_state_change"
    TRIAL_END_NOTICE = "trial_end_notice"
    UPCOMING_RENEWAL_NOTICE = "upcoming_renewal_notice"
    UPGRADE_DOWNGRADE_FAILURE = "upgrade_downgrade_failure"
    UPGRADE_DOWNGRADE_SUCCESS = "upgrade_downgrade_success"
    PENDING_CANCELLATION_CHANGE = "pending_cancellation_change"
    SUBSCRIPTION_PREPAYMENT_ACCOUNT_BALANCE_CHANGED = "subscription_prepayment_account_balance_changed"
    SUBSCRIPTION_SERVICE_CREDIT_ACCOUNT_BALANCE_CHANGED = "subscription_service_credit_account_balance_changed"

    __str__ = str.__str__


WebhookSubscriptionOrStr: TypeAlias = Annotated[WebhookSubscription | str, open_enum_validator(WebhookSubscription)]
