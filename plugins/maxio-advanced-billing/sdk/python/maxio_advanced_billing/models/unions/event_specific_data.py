from __future__ import annotations

from typing import TypeAlias

from ..chjs_tokenization_failure import ChjsTokenizationFailure, ChjsTokenizationFailureDict
from ..chjs_tokenization_success import ChjsTokenizationSuccess, ChjsTokenizationSuccessDict
from ..component_allocation_change import ComponentAllocationChange, ComponentAllocationChangeDict
from ..credit_account_balance_changed import CreditAccountBalanceChanged, CreditAccountBalanceChangedDict
from ..custom_field_value_change import CustomFieldValueChange, CustomFieldValueChangeDict
from ..dunning_step_reached import DunningStepReached, DunningStepReachedDict
from ..invoice_issued import InvoiceIssued, InvoiceIssuedDict
from ..item_price_point_changed import ItemPricePointChanged, ItemPricePointChangedDict
from ..metered_usage import MeteredUsage, MeteredUsageDict
from ..payment_collection_method_changed import PaymentCollectionMethodChanged, PaymentCollectionMethodChangedDict
from ..payment_related_events import PaymentRelatedEvents, PaymentRelatedEventsDict
from ..pending_cancellation_change import PendingCancellationChange, PendingCancellationChangeDict
from ..prepaid_subscription_balance_changed import (
    PrepaidSubscriptionBalanceChanged,
    PrepaidSubscriptionBalanceChangedDict,
)
from ..prepaid_usage import PrepaidUsage, PrepaidUsageDict
from ..prepayment_account_balance_changed import PrepaymentAccountBalanceChanged, PrepaymentAccountBalanceChangedDict
from ..proforma_invoice_issued import ProformaInvoiceIssued, ProformaInvoiceIssuedDict
from ..refund_success import RefundSuccess, RefundSuccessDict
from ..subscription_group_signup_event_data import (
    SubscriptionGroupSignupEventData,
    SubscriptionGroupSignupEventDataDict,
)
from ..subscription_product_change import SubscriptionProductChange, SubscriptionProductChangeDict
from ..subscription_state_change import SubscriptionStateChange, SubscriptionStateChangeDict

EventSpecificData: TypeAlias = (
    SubscriptionProductChange
    | SubscriptionStateChange
    | PaymentRelatedEvents
    | RefundSuccess
    | ComponentAllocationChange
    | MeteredUsage
    | PrepaidUsage
    | DunningStepReached
    | InvoiceIssued
    | PendingCancellationChange
    | PrepaidSubscriptionBalanceChanged
    | ProformaInvoiceIssued
    | SubscriptionGroupSignupEventData
    | CreditAccountBalanceChanged
    | PrepaymentAccountBalanceChanged
    | PaymentCollectionMethodChanged
    | ItemPricePointChanged
    | CustomFieldValueChange
    | ChjsTokenizationSuccess
    | ChjsTokenizationFailure
)
"""The schema varies based on the event key. The key-to-event data mapping is as follows:

* ``subscription_product_change``, ``subscription_product_change_scheduled`` - SubscriptionProductChange
* ``subscription_state_change`` - SubscriptionStateChange
* ``signup_success``, ``delayed_signup_creation_success``, ``payment_success``, ``payment_failure``,
    ``renewal_success``, ``renewal_failure``, ``chargeback_lost``, ``chargeback_accepted``, ``chargeback_closed`` -
    PaymentRelatedEvents
* ``refund_success`` - RefundSuccess
* ``component_allocation_change`` - ComponentAllocationChange
* ``metered_usage`` - MeteredUsage
* ``prepaid_usage`` - PrepaidUsage
* ``dunning_step_reached`` - DunningStepReached
* ``invoice_issued`` - InvoiceIssued
* ``pending_cancellation_change`` - PendingCancellationChange
* ``prepaid_subscription_balance_changed`` - PrepaidSubscriptionBalanceChanged
* ``subscription_group_signup_success`` and ``subscription_group_signup_failure`` - SubscriptionGroupSignupEventData
* ``proforma_invoice_issued`` - ProformaInvoiceIssued
* ``subscription_prepayment_account_balance_changed`` - PrepaymentAccountBalanceChanged
* ``payment_collection_method_changed`` - PaymentCollectionMethodChanged
* ``subscription_service_credit_account_balance_changed`` - CreditAccountBalanceChanged
* ``item_price_point_changed`` - ItemPricePointChanged
* ``custom_field_value_change`` - CustomFieldValueChange
* ``chjs_tokenization_success`` - ChjsTokenizationSuccess
* ``chjs_tokenization_failure`` - ChjsTokenizationFailure
* The rest, that is ``delayed_signup_creation_failure``, ``billing_date_change``, ``expiration_date_change``,
    ``expiring_card``,
``customer_update``, ``customer_create``, ``customer_delete``, ``upgrade_downgrade_success``,
``upgrade_downgrade_failure``, ``statement_closed``, ``statement_settled``, ``subscription_card_update``,
``subscription_group_card_update``, ``subscription_bank_account_update``, ``refund_failure``,
``upcoming_renewal_notice``, ``trial_end_notice``, ``direct_debit_payment_paid_out``, ``direct_debit_payment_rejected``,
``direct_debit_payment_pending``, ``pending_payment_created``, ``pending_payment_failed``,
``pending_payment_completed``, don't have event_specific_data defined, ``renewal_success_recreated``,
``renewal_failure_recreated``, ``payment_success_recreated``, ``payment_failure_recreated``, ``subscription_deletion``,
``subscription_group_bank_account_update``, ``subscription_paypal_account_update``,
``subscription_group_paypal_account_update``, ``subscription_customer_change``, ``account_transaction_changed``,
``go_cardless_payment_paid_out``, ``go_cardless_payment_rejected``, ``go_cardless_payment_pending``,
``stripe_direct_debit_payment_paid_out``, ``stripe_direct_debit_payment_rejected``,
``stripe_direct_debit_payment_pending``, ``maxio_payments_direct_debit_payment_paid_out``,
``maxio_payments_direct_debit_payment_rejected``, ``maxio_payments_direct_debit_payment_pending``,
``invoice_in_collections_canceled``, ``subscription_added_to_group``, ``subscription_removed_from_group``,
``chargeback_opened``, ``chargeback_lost``, ``chargeback_accepted``, ``chargeback_closed``, ``chargeback_won``,
``payment_collection_method_changed``, ``component_billing_date_changed``, ``subscription_term_renewal_scheduled``,
``subscription_term_renewal_pending``, ``subscription_term_renewal_activated``, ``subscription_term_renewal_removed``
they map to ``null`` instead."""

EventSpecificDataDict: TypeAlias = (
    SubscriptionProductChangeDict
    | SubscriptionStateChangeDict
    | PaymentRelatedEventsDict
    | RefundSuccessDict
    | ComponentAllocationChangeDict
    | MeteredUsageDict
    | PrepaidUsageDict
    | DunningStepReachedDict
    | InvoiceIssuedDict
    | PendingCancellationChangeDict
    | PrepaidSubscriptionBalanceChangedDict
    | ProformaInvoiceIssuedDict
    | SubscriptionGroupSignupEventDataDict
    | CreditAccountBalanceChangedDict
    | PrepaymentAccountBalanceChangedDict
    | PaymentCollectionMethodChangedDict
    | ItemPricePointChangedDict
    | CustomFieldValueChangeDict
    | ChjsTokenizationSuccessDict
    | ChjsTokenizationFailureDict
)
