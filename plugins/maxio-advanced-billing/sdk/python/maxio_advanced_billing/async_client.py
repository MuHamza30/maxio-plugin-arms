from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.advance_invoice import AsyncAdvanceInvoice
from .apis.api_exports import AsyncApiExports
from .apis.billing_portal import AsyncBillingPortal
from .apis.component_features import AsyncComponentFeatures
from .apis.component_price_points import AsyncComponentPricePoints
from .apis.components import AsyncComponents
from .apis.coupons import AsyncCoupons
from .apis.custom_fields import AsyncCustomFields
from .apis.customers import AsyncCustomers
from .apis.entitlements import AsyncEntitlements
from .apis.events import AsyncEvents
from .apis.events_based_billing_segments import AsyncEventsBasedBillingSegments
from .apis.feature_templates import AsyncFeatureTemplates
from .apis.insights import AsyncInsights
from .apis.invoices import AsyncInvoices
from .apis.offers import AsyncOffers
from .apis.payment_profiles import AsyncPaymentProfiles
from .apis.product_families import AsyncProductFamilies
from .apis.product_features import AsyncProductFeatures
from .apis.product_price_points import AsyncProductPricePoints
from .apis.products import AsyncProducts
from .apis.proforma_invoices import AsyncProformaInvoices
from .apis.reason_codes import AsyncReasonCodes
from .apis.referral_codes import AsyncReferralCodes
from .apis.sales_commissions import AsyncSalesCommissions
from .apis.sites import AsyncSites
from .apis.subscription_components import AsyncSubscriptionComponents
from .apis.subscription_group_invoice_account import AsyncSubscriptionGroupInvoiceAccount
from .apis.subscription_group_status import AsyncSubscriptionGroupStatus
from .apis.subscription_groups import AsyncSubscriptionGroups
from .apis.subscription_invoice_account import AsyncSubscriptionInvoiceAccount
from .apis.subscription_notes import AsyncSubscriptionNotes
from .apis.subscription_products import AsyncSubscriptionProducts
from .apis.subscription_renewals import AsyncSubscriptionRenewals
from .apis.subscription_status import AsyncSubscriptionStatus
from .apis.subscriptions import AsyncSubscriptions
from .apis.wallet_adjustments import AsyncWalletAdjustments
from .apis.wallet_products import AsyncWalletProducts
from .apis.wallet_purchases import AsyncWalletPurchases
from .apis.wallet_transactions import AsyncWalletTransactions
from .apis.wallets import AsyncWallets
from .apis.webhooks import AsyncWebhooks
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseMaxioAdvancedBillingClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncRawClient,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    LoggingOptionsOrDict,
    RetryOptionsOrDict,
    no_auth,
    param,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class AsyncMaxioAdvancedBillingClient(BaseMaxioAdvancedBillingClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "us",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
    ) -> None:
        super().__init__(
            environment=environment,
            timeout=timeout,
            server_config=server_config,
            retry_options=retry_options,
            logging_options=logging_options,
        )
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
            retry_options=self._retry_options,
            logging_options=self._logging_options,
            global_headers=[
                param[str]("User-Agent", "MaxioAdvancedBillingClient/1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth
        )

    @cached_property
    def api_exports(self) -> AsyncApiExports:
        return AsyncApiExports(self._raw_client, self._server, self._auth)

    @cached_property
    def advance_invoice(self) -> AsyncAdvanceInvoice:
        return AsyncAdvanceInvoice(self._raw_client, self._server, self._auth)

    @cached_property
    def billing_portal(self) -> AsyncBillingPortal:
        return AsyncBillingPortal(self._raw_client, self._server, self._auth)

    @cached_property
    def component_features(self) -> AsyncComponentFeatures:
        return AsyncComponentFeatures(self._raw_client, self._server, self._auth)

    @cached_property
    def component_price_points(self) -> AsyncComponentPricePoints:
        return AsyncComponentPricePoints(self._raw_client, self._server, self._auth)

    @cached_property
    def components(self) -> AsyncComponents:
        return AsyncComponents(self._raw_client, self._server, self._auth)

    @cached_property
    def coupons(self) -> AsyncCoupons:
        return AsyncCoupons(self._raw_client, self._server, self._auth)

    @cached_property
    def custom_fields(self) -> AsyncCustomFields:
        return AsyncCustomFields(self._raw_client, self._server, self._auth)

    @cached_property
    def customers(self) -> AsyncCustomers:
        return AsyncCustomers(self._raw_client, self._server, self._auth)

    @cached_property
    def entitlements(self) -> AsyncEntitlements:
        return AsyncEntitlements(self._raw_client, self._server, self._auth)

    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._raw_client, self._server, self._auth)

    @cached_property
    def events_based_billing_segments(self) -> AsyncEventsBasedBillingSegments:
        return AsyncEventsBasedBillingSegments(self._raw_client, self._server, self._auth)

    @cached_property
    def feature_templates(self) -> AsyncFeatureTemplates:
        return AsyncFeatureTemplates(self._raw_client, self._server, self._auth)

    @cached_property
    def insights(self) -> AsyncInsights:
        return AsyncInsights(self._raw_client, self._server, self._auth)

    @cached_property
    def invoices(self) -> AsyncInvoices:
        return AsyncInvoices(self._raw_client, self._server, self._auth)

    @cached_property
    def offers(self) -> AsyncOffers:
        return AsyncOffers(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_profiles(self) -> AsyncPaymentProfiles:
        return AsyncPaymentProfiles(self._raw_client, self._server, self._auth)

    @cached_property
    def product_families(self) -> AsyncProductFamilies:
        return AsyncProductFamilies(self._raw_client, self._server, self._auth)

    @cached_property
    def product_features(self) -> AsyncProductFeatures:
        return AsyncProductFeatures(self._raw_client, self._server, self._auth)

    @cached_property
    def product_price_points(self) -> AsyncProductPricePoints:
        return AsyncProductPricePoints(self._raw_client, self._server, self._auth)

    @cached_property
    def products(self) -> AsyncProducts:
        return AsyncProducts(self._raw_client, self._server, self._auth)

    @cached_property
    def proforma_invoices(self) -> AsyncProformaInvoices:
        return AsyncProformaInvoices(self._raw_client, self._server, self._auth)

    @cached_property
    def reason_codes(self) -> AsyncReasonCodes:
        return AsyncReasonCodes(self._raw_client, self._server, self._auth)

    @cached_property
    def referral_codes(self) -> AsyncReferralCodes:
        return AsyncReferralCodes(self._raw_client, self._server, self._auth)

    @cached_property
    def sales_commissions(self) -> AsyncSalesCommissions:
        return AsyncSalesCommissions(self._raw_client, self._server, self._auth)

    @cached_property
    def sites(self) -> AsyncSites:
        return AsyncSites(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_components(self) -> AsyncSubscriptionComponents:
        return AsyncSubscriptionComponents(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_group_invoice_account(self) -> AsyncSubscriptionGroupInvoiceAccount:
        return AsyncSubscriptionGroupInvoiceAccount(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_group_status(self) -> AsyncSubscriptionGroupStatus:
        return AsyncSubscriptionGroupStatus(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_groups(self) -> AsyncSubscriptionGroups:
        return AsyncSubscriptionGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_invoice_account(self) -> AsyncSubscriptionInvoiceAccount:
        return AsyncSubscriptionInvoiceAccount(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_notes(self) -> AsyncSubscriptionNotes:
        return AsyncSubscriptionNotes(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_products(self) -> AsyncSubscriptionProducts:
        return AsyncSubscriptionProducts(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_renewals(self) -> AsyncSubscriptionRenewals:
        return AsyncSubscriptionRenewals(self._raw_client, self._server, self._auth)

    @cached_property
    def subscription_status(self) -> AsyncSubscriptionStatus:
        return AsyncSubscriptionStatus(self._raw_client, self._server, self._auth)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        return AsyncSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def wallet_adjustments(self) -> AsyncWalletAdjustments:
        return AsyncWalletAdjustments(self._raw_client, self._server, self._auth)

    @cached_property
    def wallet_products(self) -> AsyncWalletProducts:
        return AsyncWalletProducts(self._raw_client, self._server, self._auth)

    @cached_property
    def wallet_purchases(self) -> AsyncWalletPurchases:
        return AsyncWalletPurchases(self._raw_client, self._server, self._auth)

    @cached_property
    def wallet_transactions(self) -> AsyncWalletTransactions:
        return AsyncWalletTransactions(self._raw_client, self._server, self._auth)

    @cached_property
    def wallets(self) -> AsyncWallets:
        return AsyncWallets(self._raw_client, self._server, self._auth)

    @cached_property
    def webhooks(self) -> AsyncWebhooks:
        return AsyncWebhooks(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncMaxioAdvancedBillingClient
