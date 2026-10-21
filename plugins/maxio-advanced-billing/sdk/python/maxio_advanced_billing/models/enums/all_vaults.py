from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AllVaults(str, Enum):
    """The vault that stores the payment profile with the provided ``vault_token``. Use ``bogus`` for testing."""

    ADYEN = "adyen"
    AUTHORIZENET = "authorizenet"
    BEANSTREAM = "beanstream"
    BLUE_SNAP = "blue_snap"
    BOGUS = "bogus"
    BRAINTREE1 = "braintree1"
    BRAINTREE_BLUE = "braintree_blue"
    CHECKOUT = "checkout"
    CYBERSOURCE = "cybersource"
    ELAVON = "elavon"
    EWAY = "eway"
    EWAY_RAPID = "eway_rapid"
    EWAY_RAPID_STD = "eway_rapid_std"
    FIRSTDATA = "firstdata"
    FORTE = "forte"
    GOCARDLESS = "gocardless"
    LITLE = "litle"
    MAXIO_PAYMENTS = "maxio_payments"
    MAXP = "maxp"
    MODUSLINK = "moduslink"
    MONERIS = "moneris"
    NMI = "nmi"
    ORBITAL = "orbital"
    PAYMENT_EXPRESS = "payment_express"
    PAYMILL = "paymill"
    PAYPAL = "paypal"
    PAYPAL_COMPLETE = "paypal_complete"
    PIN = "pin"
    SQUARE = "square"
    STRIPE = "stripe"
    STRIPE_CONNECT = "stripe_connect"
    TRUST_COMMERCE = "trust_commerce"
    UNIPAAS = "unipaas"
    WIRECARD = "wirecard"

    __str__ = str.__str__


AllVaultsOrStr: TypeAlias = Annotated[AllVaults | str, open_enum_validator(AllVaults)]
