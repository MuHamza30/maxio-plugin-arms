from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_note import CreditNote, CreditNoteDict


class ListCreditNotesResponse(SdkBaseModel):
    credit_notes: list[CreditNote]


class ListCreditNotesResponseDict(TypedDict):
    credit_notes: list[CreditNoteDict]
