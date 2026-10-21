import * as s from "../../core/validation/index.js";
import type { Schema } from "../../core/validation/schema.js";
import { chjsTokenizationFailureSchema, type ChjsTokenizationFailure } from "../chjs-tokenization-failure.js";
import { chjsTokenizationSuccessSchema, type ChjsTokenizationSuccess } from "../chjs-tokenization-success.js";
import {
  componentAllocationChangeSchema,
  type ComponentAllocationChange,
} from "../component-allocation-change.js";
import {
  creditAccountBalanceChangedSchema,
  type CreditAccountBalanceChanged,
} from "../credit-account-balance-changed.js";
import { customFieldValueChangeSchema, type CustomFieldValueChange } from "../custom-field-value-change.js";
import { dunningStepReachedSchema, type DunningStepReached } from "../dunning-step-reached.js";
import { invoiceIssuedSchema, type InvoiceIssued } from "../invoice-issued.js";
import { itemPricePointChangedSchema, type ItemPricePointChanged } from "../item-price-point-changed.js";
import { meteredUsageSchema, type MeteredUsage } from "../metered-usage.js";
import {
  paymentCollectionMethodChangedSchema,
  type PaymentCollectionMethodChanged,
} from "../payment-collection-method-changed.js";
import { paymentRelatedEventsSchema, type PaymentRelatedEvents } from "../payment-related-events.js";
import {
  pendingCancellationChangeSchema,
  type PendingCancellationChange,
} from "../pending-cancellation-change.js";
import {
  prepaidSubscriptionBalanceChangedSchema,
  type PrepaidSubscriptionBalanceChanged,
} from "../prepaid-subscription-balance-changed.js";
import { prepaidUsageSchema, type PrepaidUsage } from "../prepaid-usage.js";
import {
  prepaymentAccountBalanceChangedSchema,
  type PrepaymentAccountBalanceChanged,
} from "../prepayment-account-balance-changed.js";
import { proformaInvoiceIssuedSchema, type ProformaInvoiceIssued } from "../proforma-invoice-issued.js";
import { refundSuccessSchema, type RefundSuccess } from "../refund-success.js";
import {
  subscriptionGroupSignupEventDataSchema,
  type SubscriptionGroupSignupEventData,
} from "../subscription-group-signup-event-data.js";
import {
  subscriptionProductChangeSchema,
  type SubscriptionProductChange,
} from "../subscription-product-change.js";
import { subscriptionStateChangeSchema, type SubscriptionStateChange } from "../subscription-state-change.js";

/**
 * The schema varies based on the event key. The key-to-event data mapping is as follows:
 *
 * * `subscription_product_change`, `subscription_product_change_scheduled` -
 *   SubscriptionProductChange
 * * `subscription_state_change` - SubscriptionStateChange
 * * `signup_success`, `delayed_signup_creation_success`, `payment_success`, `payment_failure`,
 *   `renewal_success`, `renewal_failure`, `chargeback_lost`, `chargeback_accepted`,
 *   `chargeback_closed` - PaymentRelatedEvents
 * * `refund_success` - RefundSuccess
 * * `component_allocation_change` - ComponentAllocationChange
 * * `metered_usage` - MeteredUsage
 * * `prepaid_usage` - PrepaidUsage
 * * `dunning_step_reached` - DunningStepReached
 * * `invoice_issued` - InvoiceIssued
 * * `pending_cancellation_change` - PendingCancellationChange
 * * `prepaid_subscription_balance_changed` - PrepaidSubscriptionBalanceChanged
 * * `subscription_group_signup_success` and `subscription_group_signup_failure` -
 *   SubscriptionGroupSignupEventData
 * * `proforma_invoice_issued` - ProformaInvoiceIssued
 * * `subscription_prepayment_account_balance_changed` - PrepaymentAccountBalanceChanged
 * * `payment_collection_method_changed` - PaymentCollectionMethodChanged
 * * `subscription_service_credit_account_balance_changed` - CreditAccountBalanceChanged
 * * `item_price_point_changed` - ItemPricePointChanged
 * * `custom_field_value_change` - CustomFieldValueChange
 * * `chjs_tokenization_success` - ChjsTokenizationSuccess
 * * `chjs_tokenization_failure` - ChjsTokenizationFailure
 * * The rest, that is `delayed_signup_creation_failure`, `billing_date_change`,
 *   `expiration_date_change`, `expiring_card`, `customer_update`, `customer_create`,
 *   `customer_delete`, `upgrade_downgrade_success`, `upgrade_downgrade_failure`,
 *   `statement_closed`, `statement_settled`, `subscription_card_update`,
 *   `subscription_group_card_update`, `subscription_bank_account_update`, `refund_failure`,
 *   `upcoming_renewal_notice`, `trial_end_notice`, `direct_debit_payment_paid_out`,
 *   `direct_debit_payment_rejected`, `direct_debit_payment_pending`, `pending_payment_created`,
 *   `pending_payment_failed`, `pending_payment_completed`, don't have event_specific_data defined,
 *   `renewal_success_recreated`, `renewal_failure_recreated`, `payment_success_recreated`,
 *   `payment_failure_recreated`, `subscription_deletion`, `subscription_group_bank_account_update`,
 *   `subscription_paypal_account_update`, `subscription_group_paypal_account_update`,
 *   `subscription_customer_change`, `account_transaction_changed`, `go_cardless_payment_paid_out`,
 *   `go_cardless_payment_rejected`, `go_cardless_payment_pending`,
 *   `stripe_direct_debit_payment_paid_out`, `stripe_direct_debit_payment_rejected`,
 *   `stripe_direct_debit_payment_pending`, `maxio_payments_direct_debit_payment_paid_out`,
 *   `maxio_payments_direct_debit_payment_rejected`, `maxio_payments_direct_debit_payment_pending`,
 *   `invoice_in_collections_canceled`, `subscription_added_to_group`,
 *   `subscription_removed_from_group`, `chargeback_opened`, `chargeback_lost`,
 *   `chargeback_accepted`, `chargeback_closed`, `chargeback_won`,
 *   `payment_collection_method_changed`, `component_billing_date_changed`,
 *   `subscription_term_renewal_scheduled`, `subscription_term_renewal_pending`,
 *   `subscription_term_renewal_activated`, `subscription_term_renewal_removed` they map to `null`
 *   instead.
 */
export type EventSpecificData =
  | SubscriptionProductChange
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
  | ChjsTokenizationFailure;

export const eventSpecificDataSchema: Schema<EventSpecificData> = s.of<EventSpecificData>(
  s.union([
    s.lazy(() => subscriptionProductChangeSchema),
    s.lazy(() => subscriptionStateChangeSchema),
    s.lazy(() => paymentRelatedEventsSchema),
    s.lazy(() => refundSuccessSchema),
    s.lazy(() => componentAllocationChangeSchema),
    s.lazy(() => meteredUsageSchema),
    s.lazy(() => prepaidUsageSchema),
    s.lazy(() => dunningStepReachedSchema),
    s.lazy(() => invoiceIssuedSchema),
    s.lazy(() => pendingCancellationChangeSchema),
    s.lazy(() => prepaidSubscriptionBalanceChangedSchema),
    s.lazy(() => proformaInvoiceIssuedSchema),
    s.lazy(() => subscriptionGroupSignupEventDataSchema),
    s.lazy(() => creditAccountBalanceChangedSchema),
    s.lazy(() => prepaymentAccountBalanceChangedSchema),
    s.lazy(() => paymentCollectionMethodChangedSchema),
    s.lazy(() => itemPricePointChangedSchema),
    s.lazy(() => customFieldValueChangeSchema),
    s.lazy(() => chjsTokenizationSuccessSchema),
    s.lazy(() => chjsTokenizationFailureSchema),
  ]),
);
