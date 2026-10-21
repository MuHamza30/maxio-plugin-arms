from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardType(str, Enum):
    """The type of card used."""

    VISA = "visa"
    MASTER = "master"
    ELO = "elo"
    CABAL = "cabal"
    ALELO = "alelo"
    DISCOVER = "discover"
    AMERICAN_EXPRESS = "american_express"
    NARANJA = "naranja"
    DINERS_CLUB = "diners_club"
    JCB = "jcb"
    DANKORT = "dankort"
    MAESTRO = "maestro"
    MAESTRO_NO_LUHN = "maestro_no_luhn"
    FORBRUGSFORENINGEN = "forbrugsforeningen"
    SODEXO = "sodexo"
    ALIA = "alia"
    VR = "vr"
    UNIONPAY = "unionpay"
    CARNET = "carnet"
    CARTES_BANCAIRES = "cartes_bancaires"
    OLIMPICA = "olimpica"
    CREDITEL = "creditel"
    CONFIABLE = "confiable"
    SYNCHRONY = "synchrony"
    ROUTEX = "routex"
    MADA = "mada"
    BP_PLUS = "bp_plus"
    PASSCARD = "passcard"
    EDENRED = "edenred"
    ANDA = "anda"
    TARJETA_D = "tarjeta-d"
    HIPERCARD = "hipercard"
    BOGUS = "bogus"
    SWITCH = "switch"
    SOLO = "solo"
    LASER = "laser"

    __str__ = str.__str__


CardTypeOrStr: TypeAlias = Annotated[CardType | str, open_enum_validator(CardType)]
