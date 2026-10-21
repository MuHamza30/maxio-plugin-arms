from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.cancel_delayed_cancellation_error import (
    CancelDelayedCancellationErrorBody,
    cancel_delayed_cancellation_error_mapper,
)
from ..errors.cancel_dunning_error import CancelDunningErrorBody, cancel_dunning_error_mapper
from ..errors.cancel_subscription_error import CancelSubscriptionErrorBody, cancel_subscription_error_mapper
from ..errors.initiate_delayed_cancellation_error import (
    InitiateDelayedCancellationErrorBody,
    initiate_delayed_cancellation_error_mapper,
)
from ..errors.pause_subscription_error import PauseSubscriptionErrorBody, pause_subscription_error_mapper
from ..errors.preview_renewal_error import PreviewRenewalErrorBody, preview_renewal_error_mapper
from ..errors.reactivate_subscription_error import ReactivateSubscriptionErrorBody, reactivate_subscription_error_mapper
from ..errors.resume_subscription_error import ResumeSubscriptionErrorBody, resume_subscription_error_mapper
from ..errors.retry_subscription_error import RetrySubscriptionErrorBody, retry_subscription_error_mapper
from ..errors.update_automatic_subscription_resumption_error import (
    UpdateAutomaticSubscriptionResumptionErrorBody,
    update_automatic_subscription_resumption_error_mapper,
)
from ..models.cancellation_request import CancellationRequest, CancellationRequestDict
from ..models.delayed_cancellation_response import DelayedCancellationResponse
from ..models.enums.resumption_charge import ResumptionCharge, ResumptionChargeOrStr
from ..models.pause_request import PauseRequest, PauseRequestDict
from ..models.reactivate_subscription_request import ReactivateSubscriptionRequest, ReactivateSubscriptionRequestDict
from ..models.renewal_preview_request import RenewalPreviewRequest, RenewalPreviewRequestDict
from ..models.renewal_preview_response import RenewalPreviewResponse
from ..models.subscription_response import SubscriptionResponse
from ..server.server import Server


class SubscriptionStatus:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionStatusWithRawResponse(client, server, auth)

    def cancel_delayed_cancellation(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> DelayedCancellationResponse:
        """Removes the delayed cancellation from a subscription, ensuring it is not canceled at the end of the current
        period. The request will reset the ``cancel_at_end_of_period`` flag to ``false``.

        This endpoint is idempotent. If the subscription was not set to cancel in the future, removing the delayed
        cancellation has no effect and the call will be successful.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.cancel_delayed_cancellation(subscription_id, request_options=request_options)
        )

    def cancel_dunning(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Cancels the active dunning process for a subscription and sets it to active.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.cancel_dunning(subscription_id, request_options=request_options))

    def cancel_subscription(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Cancels the Subscription. The Delete method sets the Subscription state to ``canceled``. To cancel the
        subscription immediately, omit any schedule parameters from the request. To use the schedule options, the
        Schedule Subscription Cancellation feature must be enabled on your site.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``CancelSubscriptionErrorResponse |
                RawError``."""
        return unwrap(
            self._with_raw_response.cancel_subscription(subscription_id, body=body, request_options=request_options)
        )

    def initiate_delayed_cancellation(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DelayedCancellationResponse:
        """Cancels a subscription at the end of the current billing period based on the subscription's current product.
        You cannot set ``cancel_at_end_of_period`` at subscription creation, or if the subscription is past due.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.initiate_delayed_cancellation(
                subscription_id, body=body, request_options=request_options
            ),
        )

    def pause_subscription(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Places the subscription on hold, preventing it from renewing.

        ## Limitations

        You may not place a subscription on hold if the ``next_billing_at`` date is within 24 hours.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.pause_subscription(subscription_id, body=body, request_options=request_options)
        )

    def preview_renewal(
        self,
        subscription_id: int,
        *,
        body: RenewalPreviewRequest | RenewalPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RenewalPreviewResponse:
        """Previews a subscription’s next renewal assessment. Renewal Preview is an object representing a subscription’s
        next assessment. You can retrieve it to see a snapshot of how much your customer will be charged on their next
        renewal.

        The "Next Billing" amount and "Next Billing" date are already represented in the UI on each Subscriber's
        Summary. For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Optional Component Fields

        This endpoint is particularly useful because it returns the computed billing amount for the base product and the
        components which are in use by a subscriber.

        By default, the preview includes billing details for all components _at their **current** quantities_. This
        means:

        * Current ``allocated_quantity`` for quantity-based components
        * Current enabled/disabled status for on/off components
        * Current metered usage ``unit_balance`` for metered components
        * Current metric quantity value for events recorded thus far for events-based components

        In the above statements, "current" means the quantity or value as of the call to the renewal preview endpoint.
        End-of-period values for components are not predicted, so metered or events-based usage may be less than it will
        eventually be at the end of the period.

        Optionally, **you can provide your own custom quantities** for any component to see a billing preview for
        non-current quantities. This is accomplished by sending a request body with data under the ``components`` key.
        See the request body documentation below.

        ## Preview Behavior

        Sending a ``POST`` request to this endpoint returns preview data without modifying the subscription. This method
        previews data, but does not log any changes against a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.preview_renewal(subscription_id, body=body, request_options=request_options)
        )

    def reactivate_subscription(
        self,
        subscription_id: int,
        *,
        body: ReactivateSubscriptionRequest | ReactivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Reactivates a previously canceled subscription. For details on how the reactivation works, and how to
        reactivate subscriptions through the application, see `reactivation
        <https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming>`__.

        **Note: The term "resume" is used also during another process in Advanced Billing. This occurs when an on-hold
        subscription is "resumed". This returns the subscription to an active state.**

        + The response returns the subscription object in the ``active`` or ``trialing`` state.
        + The ``canceled_at`` and ``cancellation_message`` fields do not have values.
        + The method works for "Canceled" or "Trial Ended" subscriptions.
        + It will not work for items not marked as "Canceled", "Unpaid", or "Trial Ended".

        ## Resume the current billing period for a subscription

        A subscription is considered "resumable" if you are attempting to reactivate within the billing period the
        subscription was canceled in.

        A resumed subscription's billing date remains the same as before it was canceled. In other words, it does not
        start a new billing period. Payment may or may not be collected for a resumed subscription, depending on whether
        or not the subscription had a balance when it was canceled (for example, if it was canceled because of dunning).

        Consider a subscription which was created on June 1st, and would renew on July 1st. The subscription is then
        canceled on June 15.

        If a reactivation with ``resume: true`` were attempted _before_ what would have been the next billing date of
        July 1st, then Advanced Billing would resume the subscription.

        If a reactivation with ``resume: true`` were attempted _after_ what would have been the next billing date of
        July 1st, then Advanced Billing would not resume the subscription, and instead it would be reactivated with a
        new billing period.

        If a reactivation with ``resume: false``, or where 'resume' is omitted were attempted, then Advanced Billing
        would reactivate the subscription with a new billing period regardless of whether or not resuming the previous
        billing period was possible.

        | Canceled | Reactivation | Resumable? |
        |---|---|---|
        | Jun 15 | June 28 | Yes |
        | Jun 15 | July 2 | No |

        ## Reactivation Scenarios

        ### Reactivating Canceled Subscription While Preserving Balance

        + Given you have a product that costs $20
        + Given you have a canceled subscription to the $20 product
            + 1 charge should exist for $20
            + 1 payment should exist for $20
        + When the subscription has canceled due to dunning, it retained a negative balance of $20

        #### Results

        The resulting charges upon reactivation will be:
        + 1 charge for $20 for the new product
        + 1 charge for $20 for the balance due
        + Total charges = $40

        + The subscription will transition to active
        + The subscription balance will be zero

        ### Reactivating a Canceled Subscription With Coupon

        + Given you have a canceled subscription
        + It has no current period defined
        + You have a coupon code "EARLYBIRD"
        + The coupon is set to recur for 6 periods

        PUT request sent to:
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?coupon_code=EARLYBIRD``

        #### Results

        + The subscription will transition to active
        + The subscription should have applied a coupon with code "EARLYBIRD"

        ### Reactivating Canceled Subscription With a Trial, Without the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + PUT request to
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``


        #### Results
        + The subscription will transition to active

        ### Reactivating Canceled Subscription With Trial, With the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?include_trial=1``


        #### Results

        + The subscription will transition to trialing

        ### Reactivating Trial Ended Subscription

        + Given you have a trial_ended subscription
        + Send a PUT request to ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``

        #### Results

        + The subscription will transition to active

        ### Resuming a Canceled Subscription

        + Given you have a ``canceled`` subscription and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed

        ### Attempting to resume a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active, with a new billing period.

        ### Attempting to resume but not reactivate a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume[require_resume]=true``
        + The response status should be "422 UNPROCESSABLE ENTITY"
        + The subscription should be canceled with the following response
        ```
          {
            "errors": ["Request was 'resume only', but this subscription cannot be resumed."]
          }
        ```

        #### Results

        + The subscription should remain ``canceled``
        + The next billing date should not have changed

        ### Resuming Subscription Which Was Trialing

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + And the subscription was canceled in the middle of a trial
        + And there is still time left on the trial
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to trialing
        + The next billing date should not have changed

        ### Resuming Subscription Which Was trial_ended

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed
        + Any product-related charges should have been collected

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.reactivate_subscription(subscription_id, body=body, request_options=request_options)
        )

    def resume_subscription(
        self,
        subscription_id: int,
        *,
        calendar_billing_resumption_charge: ResumptionChargeOrStr | None = ResumptionCharge.PRORATED,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Resumes a paused (on-hold) subscription. If the normal next renewal date has not passed, the subscription
        will return to active and will renew on that date. Otherwise, it will behave like a reactivation, setting the
        billing date to 'now' and charging the subscriber.

        Args:
            subscription_id: The Chargify id of the subscription.
            calendar_billing_resumption_charge: (For calendar billing subscriptions only) The way that the resumed
                subscription's charge should be handled.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.resume_subscription(
                subscription_id,
                calendar_billing_resumption_charge=calendar_billing_resumption_charge,
                request_options=request_options,
            ),
        )

    def retry_subscription(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Retries collecting the balance due on a past-due subscription without waiting for the next scheduled attempt.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(self._with_raw_response.retry_subscription(subscription_id, request_options=request_options))

    def update_automatic_subscription_resumption(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Updates the date on which a paused subscription will automatically resume.

        To update a subscription's resume date, use this method to change or update the ``automatically_resume_at``
        date.

        ### Remove the resume date

        Alternatively, you can change the ``automatically_resume_at`` to ``null`` if you would like the subscription to
        not have a resume date.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_automatic_subscription_resumption(
                subscription_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SubscriptionStatusWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptionStatus:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionStatusWithRawResponse(client, server, auth)

    async def cancel_delayed_cancellation(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> DelayedCancellationResponse:
        """Removes the delayed cancellation from a subscription, ensuring it is not canceled at the end of the current
        period. The request will reset the ``cancel_at_end_of_period`` flag to ``false``.

        This endpoint is idempotent. If the subscription was not set to cancel in the future, removing the delayed
        cancellation has no effect and the call will be successful.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_delayed_cancellation(subscription_id, request_options=request_options)
        )

    async def cancel_dunning(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Cancels the active dunning process for a subscription and sets it to active.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(await self._with_raw_response.cancel_dunning(subscription_id, request_options=request_options))

    async def cancel_subscription(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Cancels the Subscription. The Delete method sets the Subscription state to ``canceled``. To cancel the
        subscription immediately, omit any schedule parameters from the request. To use the schedule options, the
        Schedule Subscription Cancellation feature must be enabled on your site.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``CancelSubscriptionErrorResponse |
                RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def initiate_delayed_cancellation(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DelayedCancellationResponse:
        """Cancels a subscription at the end of the current billing period based on the subscription's current product.
        You cannot set ``cancel_at_end_of_period`` at subscription creation, or if the subscription is past due.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Not Found Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.initiate_delayed_cancellation(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def pause_subscription(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Places the subscription on hold, preventing it from renewing.

        ## Limitations

        You may not place a subscription on hold if the ``next_billing_at`` date is within 24 hours.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.pause_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def preview_renewal(
        self,
        subscription_id: int,
        *,
        body: RenewalPreviewRequest | RenewalPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RenewalPreviewResponse:
        """Previews a subscription’s next renewal assessment. Renewal Preview is an object representing a subscription’s
        next assessment. You can retrieve it to see a snapshot of how much your customer will be charged on their next
        renewal.

        The "Next Billing" amount and "Next Billing" date are already represented in the UI on each Subscriber's
        Summary. For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Optional Component Fields

        This endpoint is particularly useful because it returns the computed billing amount for the base product and the
        components which are in use by a subscriber.

        By default, the preview includes billing details for all components _at their **current** quantities_. This
        means:

        * Current ``allocated_quantity`` for quantity-based components
        * Current enabled/disabled status for on/off components
        * Current metered usage ``unit_balance`` for metered components
        * Current metric quantity value for events recorded thus far for events-based components

        In the above statements, "current" means the quantity or value as of the call to the renewal preview endpoint.
        End-of-period values for components are not predicted, so metered or events-based usage may be less than it will
        eventually be at the end of the period.

        Optionally, **you can provide your own custom quantities** for any component to see a billing preview for
        non-current quantities. This is accomplished by sending a request body with data under the ``components`` key.
        See the request body documentation below.

        ## Preview Behavior

        Sending a ``POST`` request to this endpoint returns preview data without modifying the subscription. This method
        previews data, but does not log any changes against a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.preview_renewal(subscription_id, body=body, request_options=request_options)
        )

    async def reactivate_subscription(
        self,
        subscription_id: int,
        *,
        body: ReactivateSubscriptionRequest | ReactivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Reactivates a previously canceled subscription. For details on how the reactivation works, and how to
        reactivate subscriptions through the application, see `reactivation
        <https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming>`__.

        **Note: The term "resume" is used also during another process in Advanced Billing. This occurs when an on-hold
        subscription is "resumed". This returns the subscription to an active state.**

        + The response returns the subscription object in the ``active`` or ``trialing`` state.
        + The ``canceled_at`` and ``cancellation_message`` fields do not have values.
        + The method works for "Canceled" or "Trial Ended" subscriptions.
        + It will not work for items not marked as "Canceled", "Unpaid", or "Trial Ended".

        ## Resume the current billing period for a subscription

        A subscription is considered "resumable" if you are attempting to reactivate within the billing period the
        subscription was canceled in.

        A resumed subscription's billing date remains the same as before it was canceled. In other words, it does not
        start a new billing period. Payment may or may not be collected for a resumed subscription, depending on whether
        or not the subscription had a balance when it was canceled (for example, if it was canceled because of dunning).

        Consider a subscription which was created on June 1st, and would renew on July 1st. The subscription is then
        canceled on June 15.

        If a reactivation with ``resume: true`` were attempted _before_ what would have been the next billing date of
        July 1st, then Advanced Billing would resume the subscription.

        If a reactivation with ``resume: true`` were attempted _after_ what would have been the next billing date of
        July 1st, then Advanced Billing would not resume the subscription, and instead it would be reactivated with a
        new billing period.

        If a reactivation with ``resume: false``, or where 'resume' is omitted were attempted, then Advanced Billing
        would reactivate the subscription with a new billing period regardless of whether or not resuming the previous
        billing period was possible.

        | Canceled | Reactivation | Resumable? |
        |---|---|---|
        | Jun 15 | June 28 | Yes |
        | Jun 15 | July 2 | No |

        ## Reactivation Scenarios

        ### Reactivating Canceled Subscription While Preserving Balance

        + Given you have a product that costs $20
        + Given you have a canceled subscription to the $20 product
            + 1 charge should exist for $20
            + 1 payment should exist for $20
        + When the subscription has canceled due to dunning, it retained a negative balance of $20

        #### Results

        The resulting charges upon reactivation will be:
        + 1 charge for $20 for the new product
        + 1 charge for $20 for the balance due
        + Total charges = $40

        + The subscription will transition to active
        + The subscription balance will be zero

        ### Reactivating a Canceled Subscription With Coupon

        + Given you have a canceled subscription
        + It has no current period defined
        + You have a coupon code "EARLYBIRD"
        + The coupon is set to recur for 6 periods

        PUT request sent to:
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?coupon_code=EARLYBIRD``

        #### Results

        + The subscription will transition to active
        + The subscription should have applied a coupon with code "EARLYBIRD"

        ### Reactivating Canceled Subscription With a Trial, Without the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + PUT request to
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``


        #### Results
        + The subscription will transition to active

        ### Reactivating Canceled Subscription With Trial, With the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?include_trial=1``


        #### Results

        + The subscription will transition to trialing

        ### Reactivating Trial Ended Subscription

        + Given you have a trial_ended subscription
        + Send a PUT request to ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``

        #### Results

        + The subscription will transition to active

        ### Resuming a Canceled Subscription

        + Given you have a ``canceled`` subscription and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed

        ### Attempting to resume a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active, with a new billing period.

        ### Attempting to resume but not reactivate a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume[require_resume]=true``
        + The response status should be "422 UNPROCESSABLE ENTITY"
        + The subscription should be canceled with the following response
        ```
          {
            "errors": ["Request was 'resume only', but this subscription cannot be resumed."]
          }
        ```

        #### Results

        + The subscription should remain ``canceled``
        + The next billing date should not have changed

        ### Resuming Subscription Which Was Trialing

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + And the subscription was canceled in the middle of a trial
        + And there is still time left on the trial
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to trialing
        + The next billing date should not have changed

        ### Resuming Subscription Which Was trial_ended

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed
        + Any product-related charges should have been collected

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.reactivate_subscription(
                subscription_id, body=body, request_options=request_options
            ),
        )

    async def resume_subscription(
        self,
        subscription_id: int,
        *,
        calendar_billing_resumption_charge: ResumptionChargeOrStr | None = ResumptionCharge.PRORATED,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Resumes a paused (on-hold) subscription. If the normal next renewal date has not passed, the subscription
        will return to active and will renew on that date. Otherwise, it will behave like a reactivation, setting the
        billing date to 'now' and charging the subscriber.

        Args:
            subscription_id: The Chargify id of the subscription.
            calendar_billing_resumption_charge: (For calendar billing subscriptions only) The way that the resumed
                subscription's charge should be handled.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.resume_subscription(
                subscription_id,
                calendar_billing_resumption_charge=calendar_billing_resumption_charge,
                request_options=request_options,
            ),
        )

    async def retry_subscription(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubscriptionResponse:
        """Retries collecting the balance due on a past-due subscription without waiting for the next scheduled attempt.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.retry_subscription(subscription_id, request_options=request_options)
        )

    async def update_automatic_subscription_resumption(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubscriptionResponse:
        """Updates the date on which a paused subscription will automatically resume.

        To update a subscription's resume date, use this method to change or update the ``automatically_resume_at``
        date.

        ### Remove the resume date

        Alternatively, you can change the ``automatically_resume_at`` to ``null`` if you would like the subscription to
        not have a resume date.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: Unprocessable Entity (WebDAV) ``error`` is ``ErrorListResponse1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_automatic_subscription_resumption(
                subscription_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSubscriptionStatusWithRawResponse:
        return self._with_raw_response


class SubscriptionStatusWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_delayed_cancellation(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DelayedCancellationResponse, CancelDelayedCancellationErrorBody]:
        """Removes the delayed cancellation from a subscription, ensuring it is not canceled at the end of the current
        period. The request will reset the ``cancel_at_end_of_period`` flag to ``false``.

        This endpoint is idempotent. If the subscription was not set to cancel in the future, removing the delayed
        cancellation has no effect and the call will be successful.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/delayed_cancel.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[DelayedCancellationResponse],
            error_mapper=cancel_delayed_cancellation_error_mapper,
            request_options=request_options,
        )

    def cancel_dunning(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, CancelDunningErrorBody]:
        """Cancels the active dunning process for a subscription and sets it to active.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/cancel_dunning.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=cancel_dunning_error_mapper,
            request_options=request_options,
        )

    def cancel_subscription(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, CancelSubscriptionErrorBody]:
        """Cancels the Subscription. The Delete method sets the Subscription state to ``canceled``. To cancel the
        subscription immediately, omit any schedule parameters from the request. To use the schedule options, the
        Schedule Subscription Cancellation feature must be enabled on your site.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancellationRequest | CancellationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=cancel_subscription_error_mapper,
            request_options=request_options,
        )

    def initiate_delayed_cancellation(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DelayedCancellationResponse, InitiateDelayedCancellationErrorBody]:
        """Cancels a subscription at the end of the current billing period based on the subscription's current product.
        You cannot set ``cancel_at_end_of_period`` at subscription creation, or if the subscription is past due.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/delayed_cancel.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancellationRequest | CancellationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[DelayedCancellationResponse],
            error_mapper=initiate_delayed_cancellation_error_mapper,
            request_options=request_options,
        )

    def pause_subscription(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, PauseSubscriptionErrorBody]:
        """Places the subscription on hold, preventing it from renewing.

        ## Limitations

        You may not place a subscription on hold if the ``next_billing_at`` date is within 24 hours.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/hold.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PauseRequest | PauseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=pause_subscription_error_mapper,
            request_options=request_options,
        )

    def preview_renewal(
        self,
        subscription_id: int,
        *,
        body: RenewalPreviewRequest | RenewalPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RenewalPreviewResponse, PreviewRenewalErrorBody]:
        """Previews a subscription’s next renewal assessment. Renewal Preview is an object representing a subscription’s
        next assessment. You can retrieve it to see a snapshot of how much your customer will be charged on their next
        renewal.

        The "Next Billing" amount and "Next Billing" date are already represented in the UI on each Subscriber's
        Summary. For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Optional Component Fields

        This endpoint is particularly useful because it returns the computed billing amount for the base product and the
        components which are in use by a subscriber.

        By default, the preview includes billing details for all components _at their **current** quantities_. This
        means:

        * Current ``allocated_quantity`` for quantity-based components
        * Current enabled/disabled status for on/off components
        * Current metered usage ``unit_balance`` for metered components
        * Current metric quantity value for events recorded thus far for events-based components

        In the above statements, "current" means the quantity or value as of the call to the renewal preview endpoint.
        End-of-period values for components are not predicted, so metered or events-based usage may be less than it will
        eventually be at the end of the period.

        Optionally, **you can provide your own custom quantities** for any component to see a billing preview for
        non-current quantities. This is accomplished by sending a request body with data under the ``components`` key.
        See the request body documentation below.

        ## Preview Behavior

        Sending a ``POST`` request to this endpoint returns preview data without modifying the subscription. This method
        previews data, but does not log any changes against a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/renewals/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RenewalPreviewRequest | RenewalPreviewRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[RenewalPreviewResponse],
            error_mapper=preview_renewal_error_mapper,
            request_options=request_options,
        )

    def reactivate_subscription(
        self,
        subscription_id: int,
        *,
        body: ReactivateSubscriptionRequest | ReactivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ReactivateSubscriptionErrorBody]:
        """Reactivates a previously canceled subscription. For details on how the reactivation works, and how to
        reactivate subscriptions through the application, see `reactivation
        <https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming>`__.

        **Note: The term "resume" is used also during another process in Advanced Billing. This occurs when an on-hold
        subscription is "resumed". This returns the subscription to an active state.**

        + The response returns the subscription object in the ``active`` or ``trialing`` state.
        + The ``canceled_at`` and ``cancellation_message`` fields do not have values.
        + The method works for "Canceled" or "Trial Ended" subscriptions.
        + It will not work for items not marked as "Canceled", "Unpaid", or "Trial Ended".

        ## Resume the current billing period for a subscription

        A subscription is considered "resumable" if you are attempting to reactivate within the billing period the
        subscription was canceled in.

        A resumed subscription's billing date remains the same as before it was canceled. In other words, it does not
        start a new billing period. Payment may or may not be collected for a resumed subscription, depending on whether
        or not the subscription had a balance when it was canceled (for example, if it was canceled because of dunning).

        Consider a subscription which was created on June 1st, and would renew on July 1st. The subscription is then
        canceled on June 15.

        If a reactivation with ``resume: true`` were attempted _before_ what would have been the next billing date of
        July 1st, then Advanced Billing would resume the subscription.

        If a reactivation with ``resume: true`` were attempted _after_ what would have been the next billing date of
        July 1st, then Advanced Billing would not resume the subscription, and instead it would be reactivated with a
        new billing period.

        If a reactivation with ``resume: false``, or where 'resume' is omitted were attempted, then Advanced Billing
        would reactivate the subscription with a new billing period regardless of whether or not resuming the previous
        billing period was possible.

        | Canceled | Reactivation | Resumable? |
        |---|---|---|
        | Jun 15 | June 28 | Yes |
        | Jun 15 | July 2 | No |

        ## Reactivation Scenarios

        ### Reactivating Canceled Subscription While Preserving Balance

        + Given you have a product that costs $20
        + Given you have a canceled subscription to the $20 product
            + 1 charge should exist for $20
            + 1 payment should exist for $20
        + When the subscription has canceled due to dunning, it retained a negative balance of $20

        #### Results

        The resulting charges upon reactivation will be:
        + 1 charge for $20 for the new product
        + 1 charge for $20 for the balance due
        + Total charges = $40

        + The subscription will transition to active
        + The subscription balance will be zero

        ### Reactivating a Canceled Subscription With Coupon

        + Given you have a canceled subscription
        + It has no current period defined
        + You have a coupon code "EARLYBIRD"
        + The coupon is set to recur for 6 periods

        PUT request sent to:
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?coupon_code=EARLYBIRD``

        #### Results

        + The subscription will transition to active
        + The subscription should have applied a coupon with code "EARLYBIRD"

        ### Reactivating Canceled Subscription With a Trial, Without the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + PUT request to
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``


        #### Results
        + The subscription will transition to active

        ### Reactivating Canceled Subscription With Trial, With the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?include_trial=1``


        #### Results

        + The subscription will transition to trialing

        ### Reactivating Trial Ended Subscription

        + Given you have a trial_ended subscription
        + Send a PUT request to ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``

        #### Results

        + The subscription will transition to active

        ### Resuming a Canceled Subscription

        + Given you have a ``canceled`` subscription and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed

        ### Attempting to resume a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active, with a new billing period.

        ### Attempting to resume but not reactivate a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume[require_resume]=true``
        + The response status should be "422 UNPROCESSABLE ENTITY"
        + The subscription should be canceled with the following response
        ```
          {
            "errors": ["Request was 'resume only', but this subscription cannot be resumed."]
          }
        ```

        #### Results

        + The subscription should remain ``canceled``
        + The next billing date should not have changed

        ### Resuming Subscription Which Was Trialing

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + And the subscription was canceled in the middle of a trial
        + And there is still time left on the trial
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to trialing
        + The next billing date should not have changed

        ### Resuming Subscription Which Was trial_ended

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed
        + Any product-related charges should have been collected

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/reactivate.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReactivateSubscriptionRequest | ReactivateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=reactivate_subscription_error_mapper,
            request_options=request_options,
        )

    def resume_subscription(
        self,
        subscription_id: int,
        *,
        calendar_billing_resumption_charge: ResumptionChargeOrStr | None = ResumptionCharge.PRORATED,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ResumeSubscriptionErrorBody]:
        """Resumes a paused (on-hold) subscription. If the normal next renewal date has not passed, the subscription
        will return to active and will renew on that date. Otherwise, it will behave like a reactivation, setting the
        billing date to 'now' and charging the subscriber.

        Args:
            subscription_id: The Chargify id of the subscription.
            calendar_billing_resumption_charge: (For calendar billing subscriptions only) The way that the resumed
                subscription's charge should be handled.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/resume.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[ResumptionChargeOrStr | None](
                    "calendar_billing['resumption_charge']", calendar_billing_resumption_charge
                ),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=resume_subscription_error_mapper,
            request_options=request_options,
        )

    def retry_subscription(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, RetrySubscriptionErrorBody]:
        """Retries collecting the balance due on a past-due subscription without waiting for the next scheduled attempt.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/retry.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=retry_subscription_error_mapper,
            request_options=request_options,
        )

    def update_automatic_subscription_resumption(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, UpdateAutomaticSubscriptionResumptionErrorBody]:
        """Updates the date on which a paused subscription will automatically resume.

        To update a subscription's resume date, use this method to change or update the ``automatically_resume_at``
        date.

        ### Remove the resume date

        Alternatively, you can change the ``automatically_resume_at`` to ``null`` if you would like the subscription to
        not have a resume date.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/hold.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PauseRequest | PauseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[SubscriptionResponse],
            error_mapper=update_automatic_subscription_resumption_error_mapper,
            request_options=request_options,
        )


class AsyncSubscriptionStatusWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_delayed_cancellation(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DelayedCancellationResponse, CancelDelayedCancellationErrorBody]:
        """Removes the delayed cancellation from a subscription, ensuring it is not canceled at the end of the current
        period. The request will reset the ``cancel_at_end_of_period`` flag to ``false``.

        This endpoint is idempotent. If the subscription was not set to cancel in the future, removing the delayed
        cancellation has no effect and the call will be successful.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}/delayed_cancel.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[DelayedCancellationResponse],
            error_mapper=cancel_delayed_cancellation_error_mapper,
            request_options=request_options,
        )

    async def cancel_dunning(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, CancelDunningErrorBody]:
        """Cancels the active dunning process for a subscription and sets it to active.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/cancel_dunning.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=cancel_dunning_error_mapper,
            request_options=request_options,
        )

    async def cancel_subscription(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, CancelSubscriptionErrorBody]:
        """Cancels the Subscription. The Delete method sets the Subscription state to ``canceled``. To cancel the
        subscription immediately, omit any schedule parameters from the request. To use the schedule options, the
        Schedule Subscription Cancellation feature must be enabled on your site.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.production("/subscriptions/{subscription_id}.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancellationRequest | CancellationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=cancel_subscription_error_mapper,
            request_options=request_options,
        )

    async def initiate_delayed_cancellation(
        self,
        subscription_id: int,
        *,
        body: CancellationRequest | CancellationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DelayedCancellationResponse, InitiateDelayedCancellationErrorBody]:
        """Cancels a subscription at the end of the current billing period based on the subscription's current product.
        You cannot set ``cancel_at_end_of_period`` at subscription creation, or if the subscription is past due.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/delayed_cancel.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancellationRequest | CancellationRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[DelayedCancellationResponse],
            error_mapper=initiate_delayed_cancellation_error_mapper,
            request_options=request_options,
        )

    async def pause_subscription(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, PauseSubscriptionErrorBody]:
        """Places the subscription on hold, preventing it from renewing.

        ## Limitations

        You may not place a subscription on hold if the ``next_billing_at`` date is within 24 hours.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/hold.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PauseRequest | PauseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=pause_subscription_error_mapper,
            request_options=request_options,
        )

    async def preview_renewal(
        self,
        subscription_id: int,
        *,
        body: RenewalPreviewRequest | RenewalPreviewRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RenewalPreviewResponse, PreviewRenewalErrorBody]:
        """Previews a subscription’s next renewal assessment. Renewal Preview is an object representing a subscription’s
        next assessment. You can retrieve it to see a snapshot of how much your customer will be charged on their next
        renewal.

        The "Next Billing" amount and "Next Billing" date are already represented in the UI on each Subscriber's
        Summary. For more information, see `Subscriber Interface Overview
        <https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subscriber-Interface-Overview>`__.

        ## Optional Component Fields

        This endpoint is particularly useful because it returns the computed billing amount for the base product and the
        components which are in use by a subscriber.

        By default, the preview includes billing details for all components _at their **current** quantities_. This
        means:

        * Current ``allocated_quantity`` for quantity-based components
        * Current enabled/disabled status for on/off components
        * Current metered usage ``unit_balance`` for metered components
        * Current metric quantity value for events recorded thus far for events-based components

        In the above statements, "current" means the quantity or value as of the call to the renewal preview endpoint.
        End-of-period values for components are not predicted, so metered or events-based usage may be less than it will
        eventually be at the end of the period.

        Optionally, **you can provide your own custom quantities** for any component to see a billing preview for
        non-current quantities. This is accomplished by sending a request body with data under the ``components`` key.
        See the request body documentation below.

        ## Preview Behavior

        Sending a ``POST`` request to this endpoint returns preview data without modifying the subscription. This method
        previews data, but does not log any changes against a subscription.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/renewals/preview.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RenewalPreviewRequest | RenewalPreviewRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[RenewalPreviewResponse],
            error_mapper=preview_renewal_error_mapper,
            request_options=request_options,
        )

    async def reactivate_subscription(
        self,
        subscription_id: int,
        *,
        body: ReactivateSubscriptionRequest | ReactivateSubscriptionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ReactivateSubscriptionErrorBody]:
        """Reactivates a previously canceled subscription. For details on how the reactivation works, and how to
        reactivate subscriptions through the application, see `reactivation
        <https://maxio.zendesk.com/hc/en-us/articles/24252109503629-Reactivating-and-Resuming>`__.

        **Note: The term "resume" is used also during another process in Advanced Billing. This occurs when an on-hold
        subscription is "resumed". This returns the subscription to an active state.**

        + The response returns the subscription object in the ``active`` or ``trialing`` state.
        + The ``canceled_at`` and ``cancellation_message`` fields do not have values.
        + The method works for "Canceled" or "Trial Ended" subscriptions.
        + It will not work for items not marked as "Canceled", "Unpaid", or "Trial Ended".

        ## Resume the current billing period for a subscription

        A subscription is considered "resumable" if you are attempting to reactivate within the billing period the
        subscription was canceled in.

        A resumed subscription's billing date remains the same as before it was canceled. In other words, it does not
        start a new billing period. Payment may or may not be collected for a resumed subscription, depending on whether
        or not the subscription had a balance when it was canceled (for example, if it was canceled because of dunning).

        Consider a subscription which was created on June 1st, and would renew on July 1st. The subscription is then
        canceled on June 15.

        If a reactivation with ``resume: true`` were attempted _before_ what would have been the next billing date of
        July 1st, then Advanced Billing would resume the subscription.

        If a reactivation with ``resume: true`` were attempted _after_ what would have been the next billing date of
        July 1st, then Advanced Billing would not resume the subscription, and instead it would be reactivated with a
        new billing period.

        If a reactivation with ``resume: false``, or where 'resume' is omitted were attempted, then Advanced Billing
        would reactivate the subscription with a new billing period regardless of whether or not resuming the previous
        billing period was possible.

        | Canceled | Reactivation | Resumable? |
        |---|---|---|
        | Jun 15 | June 28 | Yes |
        | Jun 15 | July 2 | No |

        ## Reactivation Scenarios

        ### Reactivating Canceled Subscription While Preserving Balance

        + Given you have a product that costs $20
        + Given you have a canceled subscription to the $20 product
            + 1 charge should exist for $20
            + 1 payment should exist for $20
        + When the subscription has canceled due to dunning, it retained a negative balance of $20

        #### Results

        The resulting charges upon reactivation will be:
        + 1 charge for $20 for the new product
        + 1 charge for $20 for the balance due
        + Total charges = $40

        + The subscription will transition to active
        + The subscription balance will be zero

        ### Reactivating a Canceled Subscription With Coupon

        + Given you have a canceled subscription
        + It has no current period defined
        + You have a coupon code "EARLYBIRD"
        + The coupon is set to recur for 6 periods

        PUT request sent to:
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?coupon_code=EARLYBIRD``

        #### Results

        + The subscription will transition to active
        + The subscription should have applied a coupon with code "EARLYBIRD"

        ### Reactivating Canceled Subscription With a Trial, Without the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + PUT request to
        ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``


        #### Results
        + The subscription will transition to active

        ### Reactivating Canceled Subscription With Trial, With the include_trial Flag

        + Given you have a canceled subscription
        + The product associated with the subscription has a trial

        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?include_trial=1``


        #### Results

        + The subscription will transition to trialing

        ### Reactivating Trial Ended Subscription

        + Given you have a trial_ended subscription
        + Send a PUT request to ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json``

        #### Results

        + The subscription will transition to active

        ### Resuming a Canceled Subscription

        + Given you have a ``canceled`` subscription and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed

        ### Attempting to resume a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active, with a new billing period.

        ### Attempting to resume but not reactivate a subscription which is not resumable

        + Given you have a ``canceled`` subscription, and it is not resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume[require_resume]=true``
        + The response status should be "422 UNPROCESSABLE ENTITY"
        + The subscription should be canceled with the following response
        ```
          {
            "errors": ["Request was 'resume only', but this subscription cannot be resumed."]
          }
        ```

        #### Results

        + The subscription should remain ``canceled``
        + The next billing date should not have changed

        ### Resuming Subscription Which Was Trialing

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + And the subscription was canceled in the middle of a trial
        + And there is still time left on the trial
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to trialing
        + The next billing date should not have changed

        ### Resuming Subscription Which Was trial_ended

        + Given you have a ``trial_ended`` subscription, and it is resumable
        + Send a PUT request to
            ``https://acme.chargify.com/subscriptions/{subscription_id}/reactivate.json?resume=true``

        #### Results

        + The subscription will transition to active
        + The next billing date should not have changed
        + Any product-related charges should have been collected

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/reactivate.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReactivateSubscriptionRequest | ReactivateSubscriptionRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=reactivate_subscription_error_mapper,
            request_options=request_options,
        )

    async def resume_subscription(
        self,
        subscription_id: int,
        *,
        calendar_billing_resumption_charge: ResumptionChargeOrStr | None = ResumptionCharge.PRORATED,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, ResumeSubscriptionErrorBody]:
        """Resumes a paused (on-hold) subscription. If the normal next renewal date has not passed, the subscription
        will return to active and will renew on that date. Otherwise, it will behave like a reactivation, setting the
        billing date to 'now' and charging the subscriber.

        Args:
            subscription_id: The Chargify id of the subscription.
            calendar_billing_resumption_charge: (For calendar billing subscriptions only) The way that the resumed
                subscription's charge should be handled.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.production("/subscriptions/{subscription_id}/resume.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            query_params=[
                param[ResumptionChargeOrStr | None](
                    "calendar_billing['resumption_charge']", calendar_billing_resumption_charge
                ),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=resume_subscription_error_mapper,
            request_options=request_options,
        )

    async def retry_subscription(
        self, subscription_id: int, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubscriptionResponse, RetrySubscriptionErrorBody]:
        """Retries collecting the balance due on a past-due subscription without waiting for the next scheduled attempt.

        ## 3D Secure (3DS) Authentication post-authentication flow

        When a payment requires 3DS Authentication to adhere to Strong Customer Authentication (SCA), the request enters
        a post-authentication flow where a 422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.

        See the `3D Secure Post-Authentication Flow
        <https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-Authentication-Flow>`__ article in the
        product documentation to learn how to manage the redirect flow.

        Args:
            subscription_id: The Chargify id of the subscription.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/retry.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=retry_subscription_error_mapper,
            request_options=request_options,
        )

    async def update_automatic_subscription_resumption(
        self,
        subscription_id: int,
        *,
        body: PauseRequest | PauseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubscriptionResponse, UpdateAutomaticSubscriptionResumptionErrorBody]:
        """Updates the date on which a paused subscription will automatically resume.

        To update a subscription's resume date, use this method to change or update the ``automatically_resume_at``
        date.

        ### Remove the resume date

        Alternatively, you can change the ``automatically_resume_at`` to ``null`` if you would like the subscription to
        not have a resume date.

        Args:
            subscription_id: The Chargify id of the subscription.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.production("/subscriptions/{subscription_id}/hold.json"),
            path_params=[param[int]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PauseRequest | PauseRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=async_json_decoder[SubscriptionResponse],
            error_mapper=update_automatic_subscription_resumption_error_mapper,
            request_options=request_options,
        )
